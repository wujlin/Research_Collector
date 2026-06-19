# Ben Eysenbach: Designing Simpler and More Principled RL Algorithms

- Video: [Ben Eysenbach Designing Simpler and More Principled RL Algorithms](https://www.youtube.com/watch?v=EXMjEQvyzs0)
- Channel: Generally Intelligent Podcast
- Duration: 1:45:56
- Transcript: `youtube/transcripts/EXMjEQvyzs0-ben-eysenbach-designing-simpler-principled-rl-algorithms/`
- Slides / frames: `youtube/slides/EXMjEQvyzs0-ben-eysenbach-designing-simpler-and-more-principled-rl-algorithms/`
- Related series note: [ben-eysenbach-self-supervised-rl-series.md](./ben-eysenbach-self-supervised-rl-series.md)

这期访谈和已有的 Eysenbach self-supervised RL 系列笔记不完全重复。系列笔记主要整理 DIAYN、C-Learning、contrastive RL 等技术主线；这期访谈更像一张研究路线图：为什么 Eysenbach 会从真实机器人瓶颈出发，转向 reward specification、skill learning、goal-conditioned RL，再把 RL 重写成概率预测和概率最大化问题。

核心判断可以概括成一句话：更简单、更有原则的 RL，不是少做数学或少做实验，而是先问清楚统计问题是什么，输入输出是什么，目标函数真正想表达什么，然后尽量把 RL 和 supervised / unsupervised learning 放进同一个概率语言里。

## 1. 00:00-05:40：从视觉预测转向行动控制

访谈开头先讲研究背景。Eysenbach 早期做 computer vision，但很快意识到，预测本身不是终点。我们关心天气预测，是因为它会影响是否带伞；关心医学图像诊断，是因为它会影响治疗决策。也就是说，机器学习最终常常要服务行动。

这就是他转向 reinforcement learning 的原因：不是只预测世界会怎样，而是控制世界中将会发生什么。这个转向把问题从“输入到标签”推进到“输入到行动，再到长期后果”。

他也讲了一个研究方法论：research is about answering questions。实验、数据集、超参数和方法实现都只是支持问题的工具。真正要判断的是：实验是否支持某个有意思的结论。这一点贯穿后面所有算法讨论。

## 2. 05:48-10:58：真实机器人瓶颈不是只缺一个更强算法

Eysenbach 早期关心的问题是：为什么 RL 方法不能直接拿一个 GitHub repo 跑到机器人上就得到好结果。答案不是“算法还不够聪明”这么简单，而是现实系统有大量工程细节会改变学习问题。

机器人会碰坏东西、把物体推出工作区、受光照变化影响、受硬件磨损和漂移影响。论文 demo 通常只展示成功片段，隐藏了大量人工 reset、环境调试和失败恢复。这些问题会让真实采样非常昂贵，也会让训练分布和测试分布不断漂移。

Leave No Trace 这条线针对的是一种具体安全概念：避免进入不可逆状态。例如把物体推下桌子后，机械臂够不到，任务就需要人类介入。这里的 safety 不是泛泛讲 bias、fairness 或 reward misspecification，而是更物理的“不要把系统带到无法自我恢复的位置”。

这一步对后面很重要：如果 RL 要进入真实系统，算法必须减少人类工程和人工 reset 的需求。

## 3. 10:00-16:28：reward 难写，所以转向 goal 和 skill

下一个瓶颈是 reward specification。即使有了安全机制，研究者仍然需要告诉机器人什么状态是好状态，什么行为算成功。这种人工 reward 工程很脆弱。

Goal-conditioned RL 是一种缓解方式。与其为每个任务写 reward，不如给定当前状态和目标状态，让 agent 学会从这里到那里。这样，任务被重写成 reachability 问题：哪些动作能让未来状态更接近目标。

DIAYN 则从另一个角度处理 reward 缺失：如果没有外部 reward，能不能先让 agent 学会一组可区分的行为模式。Eysenbach 用 Alice 和 Bob 的通信游戏解释 mutual information 目标。Alice 设置 latent skill，机器人执行行为，Bob 观察行为并猜 Alice 设置了什么。如果 Bob 能猜出来，说明不同 skill 真的产生了可区分的行为。

这个直觉很强：skill 不是人手写的宏动作，而是从“latent code 能否通过行为传递信息”中自动出现的行为坐标。

## 4. 16:39-24:56：DIAYN 的问题是可区分不等于有用

访谈里最有价值的地方，是没有把 DIAYN 讲成万能方法。主持人追问一个关键问题：如果 agent 只是用手肘角度编码 A 到 Z，这当然可区分，但对走路或下游任务未必有用。

Eysenbach 承认这个问题真实存在。原始 mutual information 目标只要求行为能传递 skill code，不保证这些行为符合人类认为有用的任务结构。后续工作可以限制 Bob 能看到什么、引入额外任务目标、或者让行为必须在更粗粒度上可区分，从而减少“用无意义细节作弊”的机会。

这里形成一个重要边界：unsupervised skill learning 不是自动学会所有好行为，而是在没有 reward 的时候提供一个行为探索和行为压缩机制。它需要和下游目标、探索约束、表示学习或层级控制结合。

## 5. 24:41-35:25：information geometry 给出正反两面结果

后来 Eysenbach 试图证明 skill learning 到底好在哪里。Information geometry 那篇工作的结论有两面。

负面结果是：用 mutual information 学到的 skills 不会最优解决所有可能 reward function。原因是这里的“距离”不是人类直觉中的物理距离或步数距离，而是 probability distributions 之间的距离。两个行为在状态分布上可能很接近，虽然在任务意义上很不一样；反过来也可能成立。

正面结果是：如果把 skill learning 理解为 initialization，而不是理解为“预先学会所有任务”，它就有理论意义。问题类似 facility assignment：在城市里放医院，不是保证每个人就在医院旁边，而是尽量让最远的人也不要太远。skills 也是这样，它们像一组分布空间里的初始点，让未来任务在适应时离某个已有 skill 不太远。

所以 DIAYN 的合理解释不是：

```text
learn many skills -> solve every reward optimally
```

而是：

```text
learn diverse behavior modes -> provide good starting points -> adapt faster to downstream tasks
```

这和已有系列笔记里的 occupancy / future-state distribution 线可以接起来。

## 6. 35:26-49:18：goal-conditioned RL 是更 grounded 的 skill learning

Eysenbach 接着说明 goal-conditioned RL 和 skill learning 的关系。DIAYN 的 Alice 和 Bob 需要发明一套行为语言：某种动作模式代表某个 code。Goal-conditioned RL 更 grounded，因为 Alice 发送的不是任意字母，而是目标状态本身。机器人只需要到达那个状态，Bob 也只需要判断是否到达或接近那个状态。

这让 goal-conditioned RL 更容易学，也更容易和 planning 结合。Search on the Replay Buffer 这条线就是把 RL 和经典 planning 拼起来：RL 学一个 local goal-conditioned policy，也学一个状态间可达性的距离或 Q 函数；planning 方法再用这些局部连接搭图，找一串 waypoints。

这解决了两类方法各自的短板。规划擅长长时程推理，但需要符号化状态和局部可达性；RL 能处理高维观测，但长 horizon 弱。把两者合起来，局部 policy 处理高维控制，图搜索处理长程 waypoint 组合。

限制也很清楚：随着状态维度和自由度上升，breadcrumbs 数量会爆炸。二维导航可行，不代表复杂浏览器任务、机器人操作或高维连续控制都能直接套用。

## 7. 55:00-65:49：conditional imitation 可以用 Bayes 重新解释

访谈后半段进入 imitation-based goal reaching。问题是：给定已有 trajectory data，能不能从过去成功片段中学习“如果我想达到未来某个状态，在当前状态应采取什么动作”。

这个问题看起来像 supervised imitation，但 Eysenbach 强调它和 RL 很接近。关键在 future-state sampling：训练样本由当前状态、动作和某个未来状态组成；如果未来状态按几何分布采样，它就和 RL 里的 discounted future reward 很像。

于是可以用 Bayes rule 把两个概率联系起来：

```text
action given current state and goal
goal given current state and action
```

后者对应 reachability 或 discounted reward，前者对应 conditional imitation policy。两者之间差一个 regularizer。这个 regularizer 解释了为什么 imitation-based methods 在小数据、offline setting 里可能很好，因为它们很保守；也解释了为什么在有大量数据或能继续交互采样时，它们可能过度保守。

这也解释了 “Imitating Past Successes Can Be Very Suboptimal” 的问题：如果历史数据有偏，单纯模仿过去成功路径可能越来越偏。解决思路是同时训练 goal-conditioned imitation 和 non-conditioned imitation，再用二者概率比去抵消额外 regularization。

## 8. 66:09-78:58：contrastive RL 把 reachability 变成表示学习

Eysenbach 最兴奋的一条线是用 contrastive learning 解 goal-conditioned RL。直觉来自视频或序列表示学习：同一条 trajectory 中相近的帧应该表示相近，远离或不同 trajectory 的帧应该表示不同。

RL 版本的关键是把 action 也放进表示学习里。模型学习的不是普通视觉 embedding，而是和“采取某个动作后能否到达某个未来状态”相关的 embedding。若 future state 仍按几何分布采样，那么表示之间的相似度就对应未来到达某状态的 likelihood。

这给了一个很不一样的 RL 解法。它不需要显式预测下一帧像素，也不需要长 rollout。给定目标状态，比较不同动作预测出的 future representation 哪个更接近 goal representation，然后选更接近的动作。

Eysenbach 把它说成一种“像 world model 但不预测完整世界”的方法。它预测 future state 的 representation，而不是 next-state kernel 或像素。这和 LeCun / JEPA 的 latent prediction 线有强连接：不要为所有表面细节建模，只保留行动决策所需的结构。

它的优点是快，且避免一部分 model-based rollout 的 compounding error。限制仍然是 exploration：如果机器人进入没见过的状态，表示和 policy 都可能失效。Eysenbach 提到一个开放方向：用 representation space 里未覆盖的区域来驱动探索。

## 9. 82:19-87:45：语言、CLIP 和开放目标

contrastive RL 的一个自然扩展是接语言。CLIP 用 contrastive learning 连接图像和文本；Eysenbach 的方法用 contrastive learning 连接 state-action 和 future states。既然二者都是概率/对比学习问题，就可能把任务目标从 goal image 换成 language description。

这很重要，因为很多真实任务无法给出目标图像。比如“把厨房打扫干净”，你未必有一张严格目标图；语言描述反而更自然。用语言指定目标，也可能避免某些 goal image 的过窄约束，例如把物体悬停在目标位置但没有真正放下。

这里的总判断是：goal-conditioned RL、contrastive learning、CLIP、VAE、language models 都可以被放到概率建模语言里。bits 是 probability 的 log 形式，contrastive learning 在区分概率分布，LLM 在最大化 next-token likelihood，RL 也可以被写成 future probability maximization。

## 10. 87:50-105:25：研究方法、应用和 LLM 风险

Eysenbach 对研究实践的建议很实用。第一，明确统计问题：输入是什么，输出是什么，目标函数是什么，能否直接优化。很多 RL 争论会因为没有先说清这个问题而混乱。

第二，记录实验前的问题，而不是只在实验后追最好的 learning curve。他会在实验日志里写明要检验的假设，再回来解释结果。这样失败实验也能产生信息。

第三，重视可视化和 debugging。RL 很容易因为 simulator、摄像头、光照、reward prediction 等细节失败，只看曲线不够。

应用判断上，他认为 robotics 很重要，但未必是 RL 最早大规模落地的地方。真实机器人数据慢、硬件复杂、漂移严重。相比之下，交通控制、物理科学、化学合成、生物工程等领域可能有更便宜、更快或更大规模的数据流。

他对 LLM 的态度也很清楚：LLM 很强，但它们训练目标是模仿数据，不是优化长期结果。用它们做医疗、治疗或其他高风险决策时，必须区分“会生成像样回答”和“会改善长期 outcome”。RLHF 之所以重要，是因为它开始把语言模型接到稀疏反馈和目标优化上，但这只是起点。

## 11. 和当前研究线的连接

这篇访谈适合放在三条已有线索之间：

- 和 3Blue1Brown entropy 线：Eysenbach 把 RL 也翻译成 probability、likelihood、bits 和 mutual information，因此 prediction / compression / control 不是孤立概念。
- 和 LeCun world model 线：contrastive RL 和 JEPA 都反对预测全部表面细节，都更关心可行动的 latent future representation。
- 和 Simchowitz continuous control 线：Eysenbach 讲的是如何用 goal、contrastive representation 和 skills 设计更简单的 RL；Simchowitz提醒，部署时还要面对连续动作误差、coverage 和 stability。

这期的核心价值不是某个单一算法，而是一个研究范式：把 RL 从“调一个脆弱算法”改写成“明确统计对象、学习可达性概率、用表示空间连接目标和行动”。这也是为什么标题里的 simpler 和 principled 是一件事：问题定义更清楚，算法才可能更简单。
