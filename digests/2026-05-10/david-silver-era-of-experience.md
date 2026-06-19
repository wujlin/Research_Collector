# David Silver：The Era of Experience

- Video: [Is human data enough? | David Silver](https://www.youtube.com/watch?v=zzXyPGEtseI)
- Speaker: David Silver
- Channel: Google DeepMind
- Transcript: `youtube/transcripts/zzXyPGEtseI-is-human-data-enough-david-silver-era-of-experience/`
- Keyframes: `youtube/slides/zzXyPGEtseI-is-human-data-enough-with-david-silver/curated/`

插图检查：这期视频不是正式讲座，没有可复用的 slide deck。`curated/` 里的 14 张图基本都是访谈人物截图，信息量主要来自 transcript，而不是画面本身。因此正文不再内嵌这些低信息 keyframes，只保留路径供回查。这样笔记篇幅可以让给论证展开。

这期访谈的中心问题是：当前 AI 主要依赖人类数据，尤其是互联网上的人类文本、图像、视频和偏好反馈；但如果目标是让 AI 超越人类已有知识，仅靠人类数据是否足够？David Silver 的回答是：人类数据已经极大推动了 AI，但它有上限。下一阶段需要让 agent 通过与世界互动产生自己的 experience，并用这些 experience 持续改进自己。

## 1. 00:00-03:26：从“人类数据时代”转向“经验时代”

访谈开头先把当前主流 AI 路线界定为 human data era。这里的 human data 不只是自然语言文本，也包括图像、视频、代码、标注、排序偏好和人类写下来的专家知识。模型通过学习这些数据，获得的是人类已经表达出来的知识。

Silver 并不否认这条路线的价值。相反，他承认人类数据是最近一轮 AI 进步的核心燃料。问题在于，这种燃料有结构性上限：它来自人类已经知道、已经做过、已经记录过的东西。如果模型永远只在这些记录上做模仿和压缩，它可以越来越像人类，但很难稳定地产生超出人类知识边界的发现。

所以他提出 era of experience。这里的 experience 不是“更多语料”，也不是让模型自己生成更多类似互联网文本的 synthetic data，而是 agent 在环境中行动后得到的后果数据。线性地说，学习对象从静态语料库变成了闭环过程：

$$
\text{act in the world}
\rightarrow
\text{observe consequences}
\rightarrow
\text{update policy}
\rightarrow
\text{generate better experience}.
$$

这个转变的关键不只是数据来源变了，而是学习逻辑变了。human data era 的模型主要问：“人类在类似情境下会怎么说或怎么做？”experience era 的 agent 则问：“我采取这个行动以后，世界会怎样反馈？这种反馈是否说明我应该改变策略？”

## 2. 03:26-10:30：AlphaZero 是 experience-based AI 的原型

AlphaZero 是 Silver 用来解释 experience-based AI 的核心例子。这里的 “Zero” 不是说系统没有结构，而是说它不使用人类棋谱作为训练数据。它仍然知道游戏规则，也有搜索算法、policy network 和 value function；但它不先模仿职业棋手。

AlphaZero 的学习链条可以按五步理解。

第一步，给定一个环境。围棋、国际象棋或将棋的规则定义了哪些行动合法、状态如何转移、什么时候结束。

第二步，初始化一个策略和值函数。policy 负责给出下一步候选行动，value function 负责估计当前局面对最终胜负的意义。

第三步，系统通过 self-play 生成经验。它自己和自己对弈，产生大量状态、行动和最终胜负。

第四步，用最终结果反推哪些行动更好。赢棋给正反馈，输棋给负反馈；系统把这些反馈转成对 policy 和 value function 的更新。

第五步，更新后的系统继续自我对弈。更强的策略会进入更高级的局面，于是下一轮 self-play 会产生更有价值的训练数据。

所以 AlphaZero 的数据不是一次性收集好的固定数据集，而是由 agent 当前能力动态生成的。agent 越强，它探索到的状态空间越高级；状态空间越高级，训练信号又越能推动下一轮能力增长。

这也是 Silver 引入 “bitter lesson” 的地方。人类知识很有用，但如果系统结构过度适配人类数据，它可能反而被人类分布限制。AlphaGo 早期用人类棋谱启动；AlphaZero 去掉人类棋谱后，反而迫使系统把重点放在“如何自己学习”上，最终突破人类棋谱提供的起点。

## 3. 10:30-15:00：Move 37 的意义不是一个妙手，而是一条无限发现链

Move 37 常被当成 AlphaGo 的传奇瞬间。Silver 在访谈里强调的不是这一步棋本身有多漂亮，而是它暴露了一种更深的机制：当系统不再只复制人类行为分布，而是通过自己的经验搜索策略空间时，它会发现人类原本不会下、也不会首先相信的动作。

如果一个模型主要被训练成“像人类一样回答”或“像人类一样行动”，它自然会受到人类行为分布的约束。它可以更稳定、更流畅、更符合偏好，但很难系统性地产生人类分布之外的策略。Move 37 的意义就在于，它是人类分布之外的一个可见信号。

更重要的是，Move 37 不是孤立发现。Silver 把它看成一条无限发现链中的一个节点：系统通过 self-play、search、value estimation 和 policy update 不断产生新经验；每一轮经验又改变下一轮探索。真正有价值的不是“一次发现”，而是“可以持续发现”的机制。

这也是它和普通 synthetic data 的区别。如果 synthetic data 只是由已有模型生成更多相似文本，那么它仍然围绕旧分布循环。experience-based learning 的燃料来自行动后果，因而有机会持续把系统推向新问题、新状态和新策略。

## 4. 15:00-23:00：RLHF 有用，但它不是 grounding 的终点

访谈随后转向今天的 LLM。现代 LLM 也使用 reinforcement learning，最典型的是 RLHF：模型生成多个回答，人类评价哪个更好，然后模型被训练得更符合人类偏好。

Silver 对 RLHF 的判断是双重的。第一，它非常有用。RLHF 把只会模仿互联网文本的模型，调整成更有用、更符合人类交互需求的系统。没有这一层，LLM 很难成为今天这种可对话、可协作的工具。

第二，它不是 grounded experience 的终点。RLHF 的 reward 通常来自人类对输出的预先判断：回答还没有真正进入世界、还没有产生后果，人类标注者就已经判断它好不好。这个反馈能让模型更会说、更安全、更讨人喜欢，但不等于让模型从真实后果中学习。

Silver 这里的 grounding 不是“文本里提到了现实世界”，而是“行动被世界检验”。例如，一个系统提出科学假设，真正 grounded 的反馈不是人类觉得它听起来合理，而是实验、仿真、证明器或真实环境给出结果。只有当反馈来自行动后果，agent 才能学习哪些行动真的改变了世界。

这也解释了他为什么谨慎看待 synthetic data。如果 synthetic data 只是由模型生成更多语言材料，那么它仍然可能停留在人类风格文本的回音室里。真正可持续的燃料应该是 agent 自己遇到的问题、采取的行动、得到的后果，以及这些后果对下一轮策略的约束。

## 5. 23:00-33:00：AlphaProof 展示了可验证环境中的 experience learning

AlphaProof 是访谈中从棋类走向更一般智能任务的关键例子。数学证明和棋类不同，但它们有一个共同点：都存在可自动验证的反馈。

在棋类里，环境规则给出最终胜负。赢了就是正反馈，输了就是负反馈。在形式化数学里，Lean 这样的 proof assistant 可以判断一个证明步骤或完整证明是否有效。于是数学证明也可以被改写成一个 reinforcement learning 环境。

这个映射可以按对象对应来读：

- 状态：当前证明上下文。
- 行动：下一步证明策略或 tactic。
- 转移：proof assistant 根据行动更新证明状态。
- 终止：证明完成，或者路径失败。
- reward：证明被验证通过，或者没有通过。

这和普通 LLM 输出自然语言证明不同。自然语言证明可能看起来合理，但仍然可能有幻觉或漏洞；形式证明系统则会给出明确验证结果。AlphaProof 的意义在于，它把“数学是否正确”变成了 agent 可以反复试错、反复学习的环境反馈。

Silver 提到 AlphaProof 在 IMO 水平问题上取得银牌级表现。这里的重要性不只是分数，而是它说明 experience learning 不只适用于游戏。只要一个领域能提供可验证反馈，就可以把“求解问题”改写成“在环境中行动并从验证结果学习”。

## 6. 33:00-41:00：经验时代的难点是如何定义 reward

experience-based AI 的瓶颈不是让模型产生行动，而是让行动后果变成可靠的 reward。棋类和形式数学是相对容易的，因为反馈清楚：赢或输、证明成功或失败。但现实世界的问题通常没有这么干净。

比如“优化健康”不是一个天然的一维数值。它可能涉及心率、睡眠、BMI、运动量、焦虑水平、长期疾病风险、用户主观感受等多个指标。不同人在不同阶段对这些指标的重视程度也不同。把这样的问题粗暴压成一个固定 reward，很容易产生错误优化。

Silver 的思路不是放弃 reward，而是让 reward 具有适应性。系统可以先从一组可观测指标开始，例如 resting heart rate、BMI 或睡眠质量；然后根据人的反馈和长期结果，逐步学习哪些指标更能代表目标。也就是说，人的反馈不是被排除在外，而是被放到环境反馈的一部分里。

这里需要区分两种 human feedback。第一种是 RLHF 式的预先评价：人类看一段输出，说它好不好。第二种是环境中的反馈：agent 行动后，人作为世界的一部分给出反应，长期结果也被记录下来。Silver 批评的是前一种被当作唯一 grounding；他更看重后一种，因为它与行动后果绑定。

这也连到 alignment 风险。经典 paperclip maximizer 问题来自固定目标的极端优化：如果目标函数狭窄且不变，系统可能为了最大化一个指标破坏其他价值。Silver 的设想是让 reward 能随着真实反馈修正，但这并不自动解决风险。相反，它说明 experience era 需要更认真地研究 reward construction、goal adaptation 和安全约束。

## 7. 41:00-49:30：未来 agent 需要持续生命史，而不是一次性对话

访谈后段把问题推进到 agent 的时间尺度。今天很多 AI 交互是短暂的：用户输入，模型回答，会话结束。模型没有真正连续的生命史，也没有像动物或人那样在多年经验流中持续适应自己的目标、能力和世界模型。

Silver 认为 experience era 需要改变这一点。未来 agent 不应只是一次性问答系统，而应拥有持续的经验流：它在环境中行动，保存结果，更新信念，修正策略，并在长期历史中积累能力。

这会改变 agent 的学习单位。当前 LLM 的核心单位通常是 token、prompt、conversation 或 batch；experience-based agent 的核心单位更接近 trajectory：

$$
(s_0, a_0, r_0, s_1, a_1, r_1, \ldots).
$$

这里的状态、行动、反馈和后续状态构成一条连续链。模型学到的不是“如何生成下一段文本”，而是“在一个持续世界中，哪些行动会带来哪些后果”。

结尾 Fan Hui 的回忆把技术问题拉回人类经验。AlphaGo 最初击败他时，围棋共同体感到震动；但随后 AI 也打开了新的围棋理解方式。这个故事说明，AI 超越人类数据不只是性能提升，也会改变人类自己探索世界的方式。era of experience 的目标不是抛弃人类，而是让人类数据从“能力上限”变成“起点、反馈源和共同演化环境”。

## 8. 对我们研究框架的启发

这期访谈和 HJB、HJ-sampler、VI primer 的共同点在于，它们都把问题从“拟合一个静态映射”推进到“学习一个可用于决策、采样或控制的过程”。LLM 的 human data 路线更像从已有样本分布中做条件生成；Silver 的 experience 路线则要求系统在环境中生成新数据，并用后果反馈更新策略。

对 synthetic city / mobility / inverse problem 方向来说，这个区分很重要。当前我们的问题可以写成

$$
\mathbf{c} \mapsto \mathbf{p},
$$

也就是从 census summaries、marginals 或 PUMA 约束生成 joint distribution 或 population allocation。但如果只做这个映射，模型仍然主要停留在 observation-conditioned generation：它回答“给定约束，生成一个看起来合理的解”。

experience 视角会再往前推一步。生成出来的 population、route、activity chain 或 OD flow 不应该只在静态统计量上看起来合理，还应该进入某个可评估环境中产生后果。例如：

- 路径是否可达，是否违反路网和时间预算。
- 活动链是否能在时空约束下闭合。
- 群体流量是否造成不合理拥堵或空间集中。
- 生成的 joint distribution 是否能稳定解释多个尺度的观测。
- 轨迹群体是否形成可重复的 corridor、mode 或 convention。

这样一来，模型不只是一次性从 observation 反演参数，而是形成一条闭环：

$$
\text{constraints}
\rightarrow
\text{generate plausible solutions}
\rightarrow
\text{simulate or evaluate consequences}
\rightarrow
\text{update posterior / policy / generator}.
$$

这条线也能和 VI primer 的 UQ 逻辑接起来。因为 inverse problem 本来就是 ill-posed 的，同一组观测可能对应多种 plausible solutions。experience layer 的作用不是立刻消除不确定性，而是让这些候选解进入环境，通过后果反馈逐步区分：哪些解只是统计上匹配，哪些解在动态和空间机制上也站得住。

因此，Silver 这期访谈对我们的启发不是简单地“以后要做 RL”。更准确地说，它提示我们：如果研究对象缺乏清晰物理方程，但存在可模拟、可检验、可约束的环境后果，那么可以把生成问题从静态条件映射升级为 experience-conditioned inference。这个升级可能成为连接 conditional generation、uncertainty quantification、agent-based simulation 和 mobility dynamics 的中间层。
