# 研究备忘录：World Model 作为可学习的非平衡动力学

- Source interview: [xie-saining-world-model-interview.md](./xie-saining-world-model-interview.md)
- Core transcript anchor: [transcript.md](../transcripts/BV1tew5zVEDf-对谢赛宁的7小时马拉松访谈世界模型逃出硅谷反openaiami-labs两次拒绝ilya杨立昆李飞飞和42/transcript.md)
- Related project notes:
  - [landauer-to-generative-models.md](./landauer-to-generative-models.md)
  - [takahiro-sagawa-stochastic-thermodynamics.md](./takahiro-sagawa-stochastic-thermodynamics.md)
  - [dynamical-regimes-of-diffusion-models.md](../../library/ai_for_physics/generative_dynamics/dynamical-regimes-of-diffusion-models.md)
  - [fluctuating-entropy-production-on-the-coarse-grained-level.md](../../digests/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level.md)

## 核心判断

如果把谢赛宁在访谈里说的 `world model` 译成你当前最熟悉的语言，它最接近的不是“更强的视频生成模型”，而是：

`从部分可观测、带噪声、非平衡的真实系统中，学出一个足够好的有效状态表示和演化规律，使得预测、规划和决策成为可能。`

这句话之所以重要，是因为它把 `world model` 从一个 AI 圈热词，重新落回了你已经在读的几条硬主线：

- `state / hidden state`
- `stochastic dynamics`
- `Fokker-Planck / master equation`
- `coarse-graining`
- `memory / non-Markovianity`
- `irreversibility / entropy production`

## 1. 先把访谈里的定义压到最小

谢赛宁在访谈里给了一个非常直接的定义：给定当前状态 `s_t` 和动作 `a_t`，系统需要通过一个预测函数，去得到下一个状态。这个定义并不新，和 `control theory`、`model predictive control`、`model-based RL` 的经典结构是一致的。

所以如果只保留骨架，他的 `world model` 至少包含 4 个部分：

1. 一个能够表示系统当前状态的内部变量。
2. 一个把 `state + action` 映射到未来状态的动力学规则。
3. 一个基于未来演化做 planning 的机制。
4. 一个足够抽象、但又足够保真的状态表示，使它既不淹死在原始数据里，也不丢掉决策所需的信息。

这一点和你在随机动力学里熟悉的对象是同构的。差别不在数学结构，而在于：物理里常常先有模型再去分析；这里则是从高维观测里反过来学模型。

## 2. 和统计物理最直接的接点：状态演化

从统计物理的视角看，`world model` 的最直接版本就是一个可学习的动力学：

- 微观层：路径、轨迹、状态跳变、随机扰动。
- 中观层：有效状态、记忆变量、控制输入。
- 宏观层：分布演化、稳态、涨落、不可逆性。

这恰好对应你现在的桥梁语言：

- `Langevin` 处理随机轨迹。
- `Fokker-Planck` 处理概率密度如何随时间演化。
- `master equation` 处理离散状态之间的跃迁。

所以从这个角度，`world model` 不必理解成一个“会说话的模型”，而更像一个：

`learned effective dynamics`

也就是，模型不一定显式写出所有微观细节，但它足以提供对未来演化的有效预测。

## 3. Fokker-Planck 为什么是这条线上的核心翻译层

你已有的笔记里已经有一句很重要的话：

`Fokker-Planck 不是单独一个方向，而是把路径级随机动力学翻译成分布演化的翻译层。`

这句话几乎可以直接作为 `world model` 和统计物理的桥。

因为一旦你不再执着于“下一帧像素怎么生成”，而是问：

- 当前状态分布是什么？
- 在控制或干预下它怎么变？
- 哪些变化更可能，哪些变化更不可能？

那问题就自然进入了：

- `partial_t rho = - div J`
- 概率守恒
- 概率流
- 控制下的分布搬运

从这里往前走，`prediction` 就不只是单条轨迹预测，而是：

`distributional prediction`

这在真实世界里更合理，因为真实世界本来就是高维、带噪声、部分可观测的。

## 4. Coarse-graining 是 world model 的真正难点之一

访谈里谢赛宁不断强调：

- 系统不可能在像素层精确表征一切。
- 状态必须是某种更抽象、更有决策意义的表示。
- 语言只是某种已存在的抽象，但不是唯一也不是最终抽象。

这和你在 `coarse-grained irreversibility` 那篇里读到的逻辑是直接相连的。

现实系统里，观测者看到的常常不是完整微观态，而只是粗粒化后的事件、信号或片段。问题变成：

- 什么样的 coarse variable 才是稳定的？
- 什么样的事件切分能保留未来预测所需的信息？
- 什么样的隐藏变量才值得被显式建模？

这其实正是 `representation learning` 在动力系统里的版本。

所以更精确地说，`world model` 不只是“学动力学”，而是：

`学一套足够好的 coarse-grained state，使动力学可以被有效预测。`

这就是它和 `representation learning` 的内在连接。

## 5. irreversibility 不是旁支，而是核心信号

如果一个系统真要面向真实世界，那么它就不可能只活在可逆、静态、无历史的空间里。真实系统里会有：

- dissipative process
- hidden driving
- hysteresis
- memory
- time-reversal asymmetry

也就是说，`world model` 真正要面对的对象，本来就是非平衡系统。

你那篇关于 coarse-grained entropy production 的笔记已经给出一个关键判断：

`真正高信息量的对象，不是全局总量，而是轨迹片段上的结构化不对称。`

这对于 `world model` 很重要，因为：

- 系统不只要知道“下一步可能是什么”
- 还要知道“哪些演化是自然的，哪些是不自然的”
- 还要知道“哪些不可逆结构在驱动当前过程”

换句话说，一个成熟的 `world model` 不只是生成合理观测，而应该能在内部捕捉：

- hidden state
- causal asymmetry
- dynamical constraint
- feasible vs infeasible transitions

从统计物理语言看，这就是把 `irreversibility` 当成有用信号，而不只是噪声或副产品。

## 6. diffusion model 理论为什么是最现实的近桥

你现在最接近这条大图景的现成资产，其实不是“机器人”，而是对生成模型动力学的物理解读。

[dynamical-regimes-of-diffusion-models.md](../../library/ai_for_physics/generative_dynamics/dynamical-regimes-of-diffusion-models.md) 已经展示了一条很清楚的路线：

- 把 backward dynamics 当作真正的动力学对象来分析。
- 讨论 speciation、collapse、memorization，而不只是 sample quality。
- 用统计物理去问：模型什么时候真的学到结构，什么时候只是塌回样本。

这条路的重要性在于，它说明你完全可以把 AI 系统看成一个高维非平衡系统，而不是把“神经网络”当成一个独立于物理之外的黑盒。

如果再往前走一步，问题就自然会变成：

- 什么是好的 latent state？
- 什么样的 latent dynamics 才真能 support planning？
- 什么时候 representation 是在压缩真实结构，什么时候只是在记忆表面统计？

这一步，就是从 diffusion dynamics 走向真正的 `world model dynamics`。

## 7. memory / non-Markovianity 是另一条关键桥

你刚读完的 [non-markovian-rock-paper-scissors-games.md](../../digests/2026-04-13/non-markovian-rock-paper-scissors-games.md) 有一个很有价值的提醒：

`时间统计本身就会改写选择规则。`

这对 `world model` 特别重要。因为真实世界里的很多关键现象根本不是无记忆过程：

- waiting-time structure matters
- history matters
- hidden context matters

所以如果一个系统只能学到无记忆的 `next token` 或极短期的 `next frame` 统计，它离真正有用的 world model 还差很远。

从你的角度看，更值得押注的问题是：

`world model 需要怎样的 memory representation，才能把 non-Markovian 结构吸收到状态里？`

这其实已经同时碰到了：

- stochastic process theory
- latent state modeling
- predictive representation learning

## 8. McKean-Vlasov / measure-valued 路线提供了群体版 world model

`world model` 很容易被误读成“单体 agent 的脑子”。但如果把视角放大到群体、粒子系统、交互系统，它也可以是：

- density-level predictive model
- mean-field model
- measure-valued dynamics

这就是为什么 [MVNN](../../library/statistical_physics/non_equilibrium_dynamics/nonequilibrium/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-pa.md) 这类工作对你是重要资产。

因为它们已经在问：

- 如何从粒子数据学出群体演化规律？
- 如何从样本路径恢复分布级动力学？

这类问题和 `world model` 的关系很直接。差别只是：

- 一边面向科学系统
- 一边面向通用智能

但底层数学问题高度相似。

## 9. 一个更稳的总括

如果要把这套桥接压成一句工作定义，我会写成：

`World model can be viewed as a learned effective theory for partially observed, noisy, nonequilibrium dynamics, where representation learning serves to construct the right coarse-grained state and prediction serves to evolve it under action and uncertainty.`

中文就是：

`世界模型可以被理解为一种针对部分可观测、带噪声、非平衡动力学的可学习有效理论；其中表征学习负责构造合适的粗粒化状态，而预测机制负责在动作和不确定性下推进这个状态。`

## 10. 这条线最值得你自己推进的研究问题

如果往你自己的项目上落，我觉得最值得继续追的不是“造一个完整 world model”，而是下面这些更硬的问题：

1. `representation` 和 `coarse-graining` 的对应关系能否写清楚？
   也就是，什么样的 latent state 才能同时保留预测力和决策相关性。

2. 能否用 `entropy production` 或时间反演不对称，来评估一个 learned representation 是否保留了真实动力学结构？

3. `Fokker-Planck / continuity equation` 能否作为 world-model pretraining 的分布级约束语言，而不是只作为物理解释层？

4. non-Markovian 过程能否通过扩展状态空间，被吸收到一个更高维但 Markov 的 latent dynamics 里？

5. diffusion / flow / score 模型里，什么时候学到的是“可规划的 dynamics”，什么时候学到的只是“可采样的 statistics”？

## 11. 这份备忘录当前的作用

这不是一个结论稿，而是一个方向校准稿。

它的作用不是证明谢赛宁这条线一定对，而是帮你判断一件事：

`为什么你会天然对他的 world model 叙事有感觉。`

原因不是因为它时髦，而是因为它和你已经在读的统计物理主线，确实共享一组更基础的问题：

- 什么是状态？
- 什么是有效变量？
- 什么是可预测的动力学？
- 什么是不可逆性？
- 什么是隐藏驱动？
- 什么样的抽象既足够压缩，又足够可控？

如果这几组问题继续往前推，它们很可能会在 `representation learning for nonequilibrium dynamics` 这里真正汇合。
