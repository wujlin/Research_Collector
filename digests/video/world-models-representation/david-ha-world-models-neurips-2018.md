# David Ha: Recurrent World Models Facilitate Policy Evolution

- Source video: https://youtu.be/HzA8LRqhujk
- Paper: https://papers.nips.cc/paper/7512-recurrent-world-models-facilitate-policy-evolution
- Interactive article: https://worldmodels.github.io/
- Transcript: [transcript.md](../../transcripts/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018/transcript.md)
- Curated slides: [curated/index.md](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/index.md)

## Slide Overview

![Curated contact sheet](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/contact_sheet.jpg)

## 1. 从 mental model 到 world model

![Mental world models](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/01-mental-world-models.jpg)

报告一开始没有直接从算法公式进入，而是先借用 cognitive neuroscience 里的 mental model 概念。人的行动不是直接由外部世界本身决定，而是由我们在头脑里形成的世界表征决定。这个表征来自过往经验，会影响我们如何解释眼前状态、如何评估机会、如何选择行动。

把这句话放到强化学习里，就得到这篇工作的基本问题：agent 能不能也先学出一个内部世界模型，然后通过这个模型来理解环境和选择动作？如果可以，agent 面对的就不再是原始像素流，而是经过内部模型压缩和预测后的状态。

这里的“世界模型”不是一个抽象口号，而是一个可以训练的 generative model。它要做两件事：第一，把高维观测压缩成低维表示；第二，在这个低维空间里预测未来可能发生什么。只有这两件事连起来，agent 才能在“自己想象出来的未来”中训练策略。

## 2. 为什么先压缩空间：VAE 负责视觉表征

![Variational autoencoder](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/02-variational-autoencoder.jpg)

游戏环境每一步给 agent 的输入通常是图像。图像是高维对象，如果直接把像素交给控制器，控制器既要学视觉表示，又要学时间动力学，还要学动作策略，问题会混在一起。

作者的第一步是把空间表征单独拿出来，用 VAE 处理。VAE 的 encoder 把当前图像 $x_t$ 压缩成低维 latent vector $z_t$，decoder 再从 $z_t$ 重建图像。这样做的目标不是生成漂亮图片，而是得到一个足够紧凑、足够保留任务信息的状态表示。

线性地说，VAE 在这里承担的是 perception module 的角色：

- 原始输入是像素图像 $x_t$。
- VAE encoder 输出低维空间状态 $z_t$。
- 控制器以后不直接看 $x_t$，只看 $z_t$。
- 如果 $z_t$ 仍然能保留道路、怪物、火球等关键结构，那么后续控制就可以在低维空间里进行。

这一步的意义是把“看见世界”从“在世界里行动”中拆出来。作者不是让一个大策略网络端到端硬学，而是先学一个可复用的视觉压缩器。

## 3. 为什么还需要时间：RNN 负责未来分布

![Density network / RNN transition](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/03-density-rnn-dynamics.jpg)

只有 $z_t$ 还不够，因为单帧图像主要告诉 agent “现在在哪里”，但不告诉它“接下来会怎样”。例如赛车是否正在接近弯道、怪物火球是否正在飞来，这些都依赖时间上下文。

所以作者引入第二个模块 $M$，也就是 recurrent model。它接收当前 latent state、历史 hidden state 和 action，并预测下一步 latent state 的分布。更准确地说，它不是只输出一个确定的 $z_{t+1}$，而是输出一个概率分布：

$$
p(z_{t+1}\mid z_t, h_t, a_t).
$$

这里的 $h_t$ 是 RNN hidden state。它可以理解成模型对过去轨迹的压缩记忆。于是系统里出现了两个互补的低维对象：$z_t$ 表示当前空间状态，$h_t$ 表示历史和时间上下文。

这一步把 world model 从静态 representation 推进到 dynamics model。VAE 只回答“现在这一帧长什么样”；RNN 进一步回答“在当前状态和动作之后，未来可能怎么变”。

## 4. 小控制器为什么足够：把策略学习压到低维空间

作者接着把 $z_t$ 和 $h_t$ 喂给一个很小的线性 controller $C$。这个 controller 的输入是低维空间状态和时间状态，输出是 action $a_t$。它看不到原始像素，只能通过 VAE 和 RNN 给出的内部表示来行动。

这就是中文标题里“VAE + RNN + 小控制器”的来源。但这里的小控制器不是为了简陋，而是一个有意设计的实验约束。作者想验证的是：如果一个 world model 已经学到了足够好的空间和时间表示，那么控制器本身是否可以非常小？

这个设计带来一个重要分工：

- $V$：学习空间压缩，把图像变成 $z_t$。
- $M$：学习时间动力学，把历史压缩成 $h_t$，并预测未来 $z_{t+1}$ 的分布。
- $C$：只在 $(z_t,h_t)$ 上选择动作，不再负责理解像素和建模未来。

这样一来，强化学习最困难的 credit assignment 问题被限制在一个很小的参数空间里。报告里说 $V$ 和 $M$ 加起来有数百万参数，但 controller 少于一千个参数，因此甚至可以用 CMA-ES 这类 evolution strategies 来优化。

## 5. CarRacing：先证明空间加时间真的有用

![CarRacing training procedure](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/04-carracing-training-procedure.jpg)

第一个实验是 OpenAI Gym 的 CarRacing-v0。任务是从像素输入出发，让赛车沿随机生成的赛道尽可能快地行驶。训练流程很清楚：

- 先用 random policy 收集一批 rollouts。
- 用这些图像训练 VAE，把每帧编码成 $z_t$。
- 把原始数据集转换成 latent sequence。
- 用 latent sequence 训练 RNN $M$，让它预测未来 latent vector 的分布。
- 固定 $V$ 和 $M$，再训练小 controller $C$ 最大化累计 reward。

这里有一个关键点：$V$ 和 $M$ 在训练时不看 reward。它们只是在无监督地学习空间压缩和时间预测。reward 只进入最后的 controller 优化阶段。

![Spatial only vs spatial plus temporal inputs](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/05-spatial-temporal-inputs.jpg)

作者做了一个很有解释力的对比。只给 controller $z_t$，也就是只给空间信息时，agent 也能学会开车，但策略不稳，遇到急弯容易摇摆和错过转向时机。再给 controller $h_t$，也就是加入 RNN 的时间状态后，策略明显更稳，能更像是在提前预判弯道。

这说明 $h_t$ 不是可有可无的附加特征。它提供了“未来趋势”的信息，使 controller 不只是对当前图像做反应，而是在某种程度上根据内部预测行动。

![CarRacing result](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/06-carracing-results.jpg)

CarRacing 的结果是平均分超过 900，达到当时解决该任务的标准。更重要的是，这个结果不是靠一个很大的端到端 policy network 得到的，而是靠一个预先学出的 world model 加一个非常小的 controller 得到的。

## 6. 从“用模型辅助控制”到“在梦里训练”

CarRacing 证明了 $V$ 和 $M$ 可以给 controller 提供有用表示，但这还不是这篇工作最有趣的地方。这里要先区分两个层次，否则很容易误解。

第一层，是“在 latent space 里做决策”。CarRacing 已经是这样：真实环境给出图像 $x_t$，VAE 把它编码成 $z_t$，RNN 给出历史状态 $h_t$，controller 根据 $(z_t,h_t)$ 输出动作 $a_t$。也就是说，controller 看到的不是原始像素，而是 world model 提供的内部表征。

这里的关键概念是“状态转移”。在强化学习里，agent 每一步都处在某个状态里，选择一个动作，然后环境返回下一步发生了什么。线性写就是：

$$
(s_t,a_t)\longrightarrow (s_{t+1}, r_t, d_t).
$$

其中 $s_t$ 是当前状态，$a_t$ 是动作，$s_{t+1}$ 是下一状态，$r_t$ 是 reward，$d_t$ 表示 episode 是否结束。这个从“当前状态 + 动作”到“下一状态 + 奖励 + 终止信号”的映射，就是状态转移。

在像素环境里，真实状态转移通常由真实 simulator 完成。例如 CarRacing 中，controller 输出转向、油门、刹车以后，真实游戏引擎会更新赛车位置、速度和赛道画面，然后给出下一帧图像、reward 和是否冲出赛道或结束。

但这时环境本身仍然是真实的。controller 输出动作以后，动作 $a_t$ 还是被送回真实 CarRacing simulator；下一帧 $x_{t+1}$、reward、是否终止，都由真实环境产生。world model 在这里主要负责“看世界”和“提供记忆”，还没有真正替代环境。

第二层，才是“在 latent environment 里训练”。这一步的问题是：既然 $M$ 能预测下一步 latent state，那么能不能不再调用真实环境，而是让 $M$ 自己生成 $z_{t+1}$、reward 和 termination signal？如果可以，controller 就不只是用 latent state 做决策，而是在一个由模型生成的内部世界里反复试错。

所以前半段和后半段的区别不是“是否使用 latent space”，而是：

- 前半段：真实环境负责状态转移，即真实 simulator 产生 $x_{t+1}$、reward 和终止信号；world model 只把真实观测编码成 latent representation。
- 后半段：learned world model 负责生成状态转移，即模型自己采样 $z_{t+1}$，并预测 reward 和终止信号；controller 直接在模型想象出来的 latent rollout 里训练。

这就是为什么作者说下一步更关键：让 $M$ 替代真实环境，意味着 world model 从 perception / memory module 变成了一个 latent simulator。agent 不只是“通过模型看世界”，而是“在模型生成的世界里练习行动”，然后再把策略迁移回真实环境。

![Train controller inside latent space environment](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/07-latent-environment-controller.jpg)

为了做到这一点，RNN $M$ 后面接一个 mixture density network layer。它输出下一步 latent vector 的概率分布。每一步可以从这个分布里采样一个新的 $z_{t+1}$，再把它反馈给模型，继续生成下一步。这样就形成了一个不依赖真实像素、不依赖真实环境模拟器的 latent rollout。

这里“想象未来”不是比喻，而是一个具体采样过程：

$$
z_{t+1}\sim p_M(z_{t+1}\mid z_t,h_t,a_t).
$$

controller 在这个采样出来的 latent trajectory 上行动，得到奖励和终止信号，并被优化。它训练时看到的不是真实世界，而是 $M$ 生成的 dream environment。

## 7. Doom TakeCover：梦境训练为什么会出问题

作者用 Doom TakeCover 测试 dream training。这个环境里，agent 被困在房间里，怪物不断发射火球，目标是尽可能活得久。

![Doom TakeCover setup](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/08-doom-takecover-setup.jpg)

这个实验比 CarRacing 多了一个关键要求：world model 不仅要预测下一步 latent vector，还要预测 agent 是否死亡。原因是如果要用 $M$ 替代真实环境，就必须让它也给出 episode 的终止事件。否则 controller 不知道什么时候结束，也无法正确计算 survival reward。

但是第一次直接在 dream environment 里训练并不成功。问题不是 controller 太弱，而是 world model 不完美。agent 学会了利用模型漏洞，而不是学会真实环境中的生存策略。

报告里给出的例子很直观：agent 在内部模型中学到一种特殊运动方式，让火球在生成时被“神奇地熄灭”。这在 $M$ 的生成环境里有效，但回到真实 Doom 环境里当然无效。这就是 model exploitation：策略不是在解决真实任务，而是在攻击模型误差。

## 8. 温度参数：把梦境变得更随机，反而更可迁移

![Cheating the world model](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/09-cheating-world-model.jpg)

作者的解决方法不是让 controller 更复杂，而是调节 world model 采样过程中的 temperature。温度越高，生成环境越随机，agent 面对的不确定性越强。

这个思路很有意思。低温环境更确定，看起来更容易训练，但也更容易让 agent 找到模型漏洞。高温环境更嘈杂，agent 有时甚至会无缘无故死亡，但这会迫使策略更保守、更稳健，减少对模型细节漏洞的依赖。

![Temperature and transfer result](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/10-doom-temperature-results.jpg)

结果呈现出一个 trade-off。提高 temperature 后，agent 在 virtual environment 里的分数下降，因为环境变难了；但迁移到真实环境后的分数反而上升，因为策略不再过度利用内部模型的漏洞。温度过高也会带来代价，策略可能过度风险规避，平均 reward 会下降。

线性地说，这一段建立了一个关键判断：world model 不是越确定越好。用于训练策略的生成环境需要适当不确定性，否则 controller 会把模型误差当作可利用规律。

## 9. 局限：随机数据覆盖不了需要探索的状态

作者随后明确指出当前方法的一个核心局限。前面的流程假设 random policy 收集到的数据已经覆盖了环境的大部分重要状态。但这在很多任务里不成立。

例如 swing-up pendulum。随机策略主要看到杆子向下摆的状态，很少看到杆子被成功甩上去以后会发生什么。world model 如果只在这些数据上训练，就会缺少“杆子向上”这一部分状态空间的经验。

这样训练出的 controller 可能会学会把杆子甩起来，但一旦进入数据稀缺区域，world model 就不知道接下来该如何预测，controller 也不知道该如何稳定控制。

所以问题不是 $V$、$M$、$C$ 的结构完全失效，而是初始数据分布太窄。world model 的想象能力被它见过的数据限制住了。它不能可靠想象自己从未接触过的状态区域。

## 10. 迭代训练：让策略反过来扩展 world model 的经验

![Iterative world model training](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/11-iterative-training-policy.jpg)

为了解决数据覆盖问题，作者提出一个简单的 iterative loop。流程变成：

- 先用已有数据训练 world model。
- 在 world model 里训练 controller。
- 把 controller 放回真实环境中执行。
- 用它访问到的新状态收集更多数据。
- 用新增数据继续改进 world model。
- 再训练更好的 controller。

这一步把 world model 和 policy learning 从一次性流水线变成循环过程。controller 不再只是 world model 的使用者，也间接成为 world model 数据分布的扩展器。

![Model-based RL follow-up](../../slides/HzA8LRqhujk-recurrent-world-models-facilitate-policy-evolution-david-ha-neurips-2018-oral/curated/12-model-based-rl-followup.jpg)

报告最后把这个方向连接到后续工作。David Ha 提到他们在后续论文中使用更复杂的 stochastic dynamics model，不再把 VAE 和 RNN 完全分开训练，而是更端到端地学习 dynamics model，并用 planning module 替代简单线性 controller。这条线后来会发展到 PlaNet、Dreamer 等基于 latent imagination 的 model-based RL 方法。

## 11. 这场报告的真正主线

这场 NeurIPS oral 不是单纯介绍一个 VAE + RNN + controller 的工程拼装。它真正推进的是一个三层判断。

第一层，控制问题可以先通过 representation learning 降维。agent 不必直接在像素空间里学策略，而可以先把空间状态压缩成 $z_t$。

第二层，好的状态表示还必须包含时间。单帧 latent $z_t$ 只能描述当前视觉状态，RNN hidden state $h_t$ 才把过去轨迹和未来趋势带进来。

第三层，如果 dynamics model 足够好，agent 不仅可以通过它看世界，还可以在它生成的内部环境中训练。这就是“能想象未来的世界模型”的核心含义。

所以整篇工作的逻辑不是：

- 用 VAE 压缩图像；
- 用 RNN 预测未来；
- 用小控制器输出动作。

更准确地说，它是：

- 先把高维观测降成低维空间状态；
- 再把时间演化建模成 latent transition distribution；
- 再让 controller 只在这个内部世界里学习行动；
- 最后测试这种内部世界能不能替代真实环境的一部分训练成本。

## 12. 和我们当前阅读框架的连接

这篇 work 和我们前面读过的 HJB / HJ-sampler / VI primer 有一个共同点：它也在避免直接在原始高维对象上硬学。

在 HJB 那篇里，直接学高维控制场太重，所以转向学习标量势函数 $W$ 或 $U$。在 VI primer 里，后验分布难算，所以把推断转成可优化的变分问题。在 World Models 里，直接从像素到动作的策略学习太难，所以先学一个低维 latent world，再在这个 latent world 上做控制。

差异也很清楚。HJB / HJ-sampler 的核心语言是控制代价、势函数、路径采样和后验；这篇的核心语言是 model-based RL、latent dynamics、dream environment 和 policy transfer。它没有明确的物理 PDE 或 HJB 结构，但它同样在处理一个“高维观测到低维可控结构”的问题。

对我们现在关心的城市生成和 inverse problem 来说，这篇的启发是：如果直接从 summaries / observations 到完整 joint distribution 很难，也许可以先问有没有一个中间的 latent world model。这个 latent world 不一定是物理方程，但它至少要承担两个功能：压缩可观测结构，并模拟在条件变化下可能出现的未来或样本族。

## 13. 读这篇时最值得保留的几个问题

- World model 学到的是环境的真实因果结构，还是只学到了足够支持当前任务的预测结构？
- 如果训练数据来自随机 policy，那么 latent world 的覆盖范围由什么决定？
- 当 controller 在 dream environment 里训练时，怎样防止它利用模型漏洞？
- temperature 这种“让模型更随机”的方法，本质上是在做鲁棒控制，还是只是经验性正则化？
- 对我们自己的问题，如果没有明确物理方程，能否用 learned latent dynamics 作为弱世界模型？

## Self-Check

- 笔记按视频时间线展开，覆盖了 mental model 动机、VAE、RNN、controller、CarRacing、Doom dream training、temperature、防作弊、迭代训练和后续工作。
- 图片直接嵌入正文，全部来自 `curated/`，没有混用 root-level raw frames。
- transcript 和 slide 链接都指向本地 Research_Collector 结构。
- 右侧会议栏和讲者小窗已从 curated slides 中裁掉，contact sheet 已重新生成。
