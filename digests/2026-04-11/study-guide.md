---
title: "Study Guide"
digest_type: "study_guide"
date: "2026-04-11"
---

# Study Guide 2026-04-11

## Today Focus

今天只精读两篇，不再摊开第三篇：

1. `Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility`
2. `Dynamical regimes of diffusion models`

这个顺序对应的是：

`随机热力学主线深化 -> AI for physics 理论前沿`

第一篇解决你当前最直接的问题：有限观测下如何定位不可逆性。第二篇用统计物理去分析 diffusion model，本质上是在补你后面要走的 `AI for physics` 支线。

## Reading Protocol

今天两篇统一按这条线读：

`问题 -> 为什么重要 -> 对象 -> 演化 -> 量 -> 方法 -> 证据 -> 你要带走什么`

每篇至少写下这 8 句：

1. 它在解决什么具体问题？
2. 为什么这个问题值得解决？
3. 它研究的对象是什么？
4. 对象怎么演化？
5. 它关心的核心量是什么？
6. 它用了什么方法？
7. 最有说服力的证据是什么？
8. 你最后应该带走哪一个概念或结构？

## Paper 1

### Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility

- 为什么先读：
  这是比昨天那篇弱 preprint 更可信的 `entropy production inference` 文献，而且作者线很强，直接来自 `Udo Seifert` 这条随机热力学主线。
- 论文链接：
  https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.023175
- 本地 PDF：
  [fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.pdf](/Users/jinlin/Desktop/Project/Research_Collector/pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.pdf)

#### 1. 问题

这篇解决的问题是：

`当系统只能被粗粒化地观测时，还能不能定义、推断并局域化 entropy production？`

这里的难点不是熵产生本身，而是：

- 真实系统往往不是“全可见”的
- 一旦隐藏自由度存在，标准随机热力学的轨迹公式就不再能直接套用
- 你不仅想估计总的 irreversibility，还想知道它在时间和空间上“发生在哪里”

#### 2. 为什么重要

这篇值得读，不是因为它只是又给了一个 bound，而是因为它处理的是更现实的问题：

`有限观测下的不可逆性推断。`

这正好接你现在关心的几件事：

- coarse-graining 之后，熵产生还剩下什么
- 只看局部片段或事件时，能不能做 thermodynamic inference
- hidden driving 能不能被定位，而不是只被平均掉

#### 3. 对象

优先抓住这几个对象：

- coarse-grained trajectories
- snippets / Markovian events
- fluctuating entropy production
- hidden driving

这篇的对象不是完整微观动力学，而是“观测层可见到的事件结构”。

#### 4. 演化

这里要重点确认：

- 他们如何从完整轨迹切成 `snippets`
- `Markovian events` 在这里扮演什么角色
- coarse-grained 动力学下，哪些随机热力学结构还保留，哪些已经丢失

先确定他们到底把“部分可见动力学”重写成了什么可计算对象。

#### 5. 量

这篇的核心量是：

- fluctuating entropy production
- irreversibility localization
- hidden driving detection

这里最重要的问题不是“总熵产生是多少”，而是：

`能不能把不可逆性定位到具体时间段、空间位置或事件类型上。`

#### 6. 方法

方法层先回答这两个问题：

1. 它怎样把 coarse-grained 事件重新组织成可定义 entropy production 的对象。
2. 它的 inference 是只给 bound，还是能给 trajectory-level / event-level attribution。

可以先把方法压成一句话：

`这篇是在为“部分可见系统的 entropy production”重建一个仍然能落到轨迹上的定义。`

#### 7. 证据

优先看：

- 理论定义是否闭合
- 是否给出 hidden driving 的检测例子
- 时间/空间局域化是不是方法真正独有的能力

#### 8. 你要带走什么

结论：

`entropy production 不只是一个总量；在 coarse-grained setting 下，真正有价值的是能否把 irreversibility 重新局域化。`

#### Linear Reading Notes

这一篇最适合按下面这条线读：

1. 标准随机热力学默认系统是完整可观测的。
2. 真实系统常常只能部分观测，于是只剩 coarse-grained dynamics。
3. 现有方法大多只能推平均 entropy production 或 coarse-grained 动力学本身。
4. 作者要把 `trajectory-level entropy production` 重新搬到 coarse-grained level。
5. 为此他们引入 `Markovian events` 和 `snippets` 作为基本单元。
6. 在这些基本单元上定义 coarse-grained fluctuating entropy production。
7. 最终目标不是只给总量，而是把 irreversibility 局域化到时间、空间和事件上，并检测 hidden driving。

#### Intro Logic

`Introduction` 的主线是：

1. 随机热力学已经能处理完整可观测的小系统，并给出 `Jarzynski equality`、`fluctuation theorem` 等普适关系。
2. 真实系统常常不能完整观测，或者系统与环境根本分不干净。
3. 这会自然产生 `effective / coarse-grained dynamics`，而标准轨迹级随机热力学不能直接套用。
4. 现有工作大致分成两条线：一条做平均量的 thermodynamic inference，另一条研究 coarse-grained dynamics 本身，但两者尚未真正统一。
5. 这篇文章要把这两条线接起来：在 coarse-grained level 上重新建立 `fluctuating entropy production`。

#### Figure 1

`Figure 1` 不是结果图，而是问题设定图。它在说明：即使 coarse-grained 描述里出现了不能视为标准 Markov state 的可观测状态，作者仍然想在这些局部轨迹片段上定义有物理意义的 entropy production。

图里的关键信息是：

- 深势阱对应的状态可以近似视为 `Markov states`
- 浅势阱对应的状态不能被干净地视为 `Markov states`
- 原因是缺少清楚的 `time-scale separation`
- 作者的方法正是为这种“整体 coarse-grained dynamics 不再简单 Markov”的情形设计的

#### Clear Time-Scale Separation

`clear time-scale separation` 的意思是：系统里存在明显快慢不同的过程，而且快过程先完成，慢过程后发生。典型图像是：

- 阱内弛豫是快过程
- 阱间跃迁是慢过程

若两者满足

$$
\tau_{\mathrm{intra}} \ll \tau_{\mathrm{inter}},
$$

那么一个势阱就可以近似成 `Markov state`。如果这种分离不清楚，系统离开一个可见状态时仍然保留进入该状态的历史信息，粗粒化后的动力学就会带记忆。

#### General Setup

这一节的重点是：如果观察者只能看到 coarse-grained trajectory，那么要定义不可逆性，首先必须知道这条 coarse-grained trajectory 的正向概率和反向概率各是什么。

逻辑是：

1. 微观层有完整轨迹 $\gamma$ 和对应的 path weight $P[\gamma]$。
2. 观察者只能看到它的投影 $\Gamma$，也就是 coarse-grained trajectory。
3. $\Gamma$ 本身也有 path weight $P[\Gamma]$，它由微观权重 $P[\gamma]$ 和 coarse-graining 映射 $\gamma \mapsto \Gamma$ 唯一决定。
4. 若要在 coarse-grained level 上定义 entropy production，就还必须知道反向轨迹 $\tilde{\Gamma}$ 及其概率 $P[\tilde{\Gamma}]$。

这里的关键提醒是：时间反演不只是把电影倒放，还要知道观测量本身在时间反演下怎么变。

#### State-Based vs Transition-Based

这篇反复区分两种 coarse-grained 描述：

- `state-based description`：记录系统当前处于哪个状态
- `transition-based description`：记录系统刚刚发生了哪次跳变

前者更像“当前在哪”，后者更像“刚刚怎么动了”。这一区别之所以重要，是因为时间反演对两者的作用不同。

#### Even vs Odd Observables

作者还区分了时间反演下的两类 observables：

- `even observables`：时间反演后不变，例如状态标签、overdamped 位置变量
- `odd observables`：时间反演后要变号或变方向，例如速度、动量、跳变方向

这篇的一个优点是：他们给出的 coarse-grained entropy production 识别公式对 even 和 odd observables 都适用。不同点不在公式长相，而在如何正确构造反向事件和反向轨迹。

#### Markovian Events

`Markovian event` 是这篇最关键的新对象。它不是普通可见状态，而是这样一种特殊事件：一旦观测到它，未来演化就与更早的过去条件独立。

正式定义是

$$
P[\gamma^+ \mid I,\gamma^-] = P[\gamma^+ \mid I].
$$

物理意思是：给定事件 $I$ 后，系统的动力学记忆被切断。作者不要求整个 coarse-grained dynamics 都是 Markov 的，但要求存在这样的局部事件，作为切分轨迹的锚点。

一般情况下，Markovian event 要写成

$$
I \equiv (I,\tau),
$$

因为在非平稳系统里，绝对时间 $\tau$ 也是事件的一部分。只有在 stationary system 中，$\tau$ 才可以省掉。

#### Snippets

`snippet` 是由两个 Markovian events 夹住的一段局部 coarse-grained trajectory。它不是任意片段，而是作者后面定义 entropy production 的基本归因单元。

如果一条 coarse-grained trajectory 写成

$$
\Gamma=(I_0 \to I_1 \to \cdots \to I_n),
$$

那么相邻两个 Markovian events 之间的那段

$$
I_{k-1} \to I_k
$$

就是一个 snippet。作者后面不是直接给整条轨迹一个黑箱总量，而是先给每个 snippet 定义 entropy production，再把它们相加。

#### Figure 2

`Figure 2` 的作用，是把这篇文章后面会用到的三类 coarse-graining 场景并排摆出来。它不是在定义新公式，而是在说明：同一套 `Markovian event + snippet` 框架，可以落在不同的观测层上。

这里先固定两个对象：

- `Markovian event`：一个观测，一旦发生，就足以从动力学角度确定系统此刻的微观状态
- `snippet`：一段从一个 Markovian event 出发、到下一个 Markovian event 结束的 coarse-grained trajectory

对应的 snippet entropy production 写成

$$
\Delta S[\Gamma_s]
=
\ln \frac{P(I)\,P[\Gamma_s \mid I]}{P(J)\,P[\tilde{\Gamma}_s \mid \tilde{J}]}.
$$

在 stationary 的记号下，也可以写成

$$
\Delta S[\Gamma_s]
=
\ln \frac{P(I)\,\psi_{I \to J}(t;O)}{P(J)\,\psi_{\tilde J \to \tilde I}(t;\tilde O)}.
$$

`Figure 2` 有四个 panel。

**(a) 6 态微观网络，只有四个跃迁可见**

这一幅给出完整的微观 Markov 网络。真实系统有 6 个状态和多条跃迁，但观察者只能看到四个 transition events：

$$
K=(1 \to 2),\quad \tilde K=(2 \to 1),\quad L=(3 \to 4),\quad \tilde L=(4 \to 3).
$$

这说明这里的粗粒化是按跃迁事件来定义的。观察者看不到完整状态图，只能在时间序列里识别出少数仪器真正能分辨的跃迁。

**(b) `(a)` 的 coarse-grained description**

这一幅把 `(a)` 中所有不可见的微观状态和不可见跃迁折叠成一个 `hidden` 块。观察者真正看到的，只剩四类可观测事件

$$
K,\ \tilde K,\ L,\ \tilde L
$$

它们对应的是 hidden 内部动力学向外显露出来的少数可见跃迁。

这幅图在表达一个关键重写：对观察者而言，系统不再首先表现为“状态网络”，而是表现为“事件序列”。因此 coarse-grained trajectory 更自然地写成

$$
I \xrightarrow[t,O]{} J,
$$

也就是从一个可观测事件到下一个可观测事件的 snippet。对观察者来说，能直接测到的数据只有两类：发生了哪个事件，以及相邻两个事件之间隔了多久。因此一条 coarse-grained trajectory 的典型样子就是

$$
\tilde K \xrightarrow{t_1} L \xrightarrow{t_2} \tilde K \xrightarrow{t_3} \tilde L \xrightarrow{t_4} K \cdots
$$

每两个相邻可观测事件之间就是一个 snippet。

**(c) 9 态网络，观测的是两个单独状态和一个复合状态**

这一幅说明 coarse-graining 不一定是观测某几个跃迁，也可以是观测某几个状态，或者把多个微观状态合并成一个可见状态。这里的 `lumped state` 指的就是这种“把几个底层状态压成一个状态标签”的对象。图里可见的是状态 `1`、状态 `4`，以及复合状态

$$
H=\{8,9\}.
$$

这表示观察者能够分辨“系统是否进入了由 8 和 9 组成的这片区域”，但不能分辨它此刻到底在 `8` 还是在 `9`。如果 `8` 和 `9` 的后续动力学不同，那么 `H` 本身就不再完全确定微观状态，因此它不是严格的 Markovian event，而更像 snippet 内部的附加观测 $O_k$。这个 panel 的作用，是把“状态级粗粒化”和“非马尔可夫附加信息”同时摆出来。

**(d) 5 态网络，驱动循环完全藏在不可见部分**

这一幅给出最强的 hidden-driving 场景。这里先把两个词讲清楚：

- `hidden driving`：系统里确实存在持续把过程推离平衡的驱动力，但这个驱动力所在的循环或通道本身并不直接可见
- `affinity 下界`：这里的 `affinity` 就是一个循环沿某个方向被持续偏置的强度，定量上可以写成该循环正向速率乘积与反向速率乘积之比的对数。它衡量的是“系统绕这条循环更愿意顺时针还是逆时针走”，若为零就对应 detailed balance，若不为零就对应非平衡驱动。由于观察者看不见隐藏循环里的全部速率，通常拿不到它的精确值；本文能保证的是，从可见 waiting-time 统计里仍可推出这个驱动力的下界。

在这张图里，观察者只能看到状态 `1` 和 `2`，但不可见部分里存在一个被顺时针驱动的循环

$$
3 \to 4 \to 5 \to 3.
$$

这里的 driving 是“hidden”的，因为真正打破 detailed balance 的循环完全位于观察者看不到的子网络中。`hidden driving detection` 的意思，就是只凭可见层上的 waiting-time statistics 和 snippet asymmetry，去判断这种隐藏驱动是否存在。

这幅图的重点不是让你立刻算 entropy production，而是说明：即使不可逆性完全藏在未观测到的循环里，coarse-grained statistics 仍然可能留下痕迹。后面给出的 `affinity 下界`，就是针对这种场景推出来的：

$$
\max_C |A_C|
\ge
a_{I \to J}
=
\sup_t \Delta S[I \xrightarrow{t} J]
-
\inf_t \Delta S[I \xrightarrow{t} J].
$$

也就是说，如果同一类 snippet 在不同持续时间 $t$ 下给出不同的 coarse-grained entropy production，就说明 hidden 部分里存在被驱动的循环，而且这种时间依赖的振幅还能给出隐藏 affinity 的下界。

所以 `Figure 2` 的线性逻辑是：

- `(a)` 给出一个“只能观测少数跃迁事件”的微观例子
- `(b)` 把它重写成观察者真正面对的事件序列描述
- `(c)` 说明 coarse-graining 还可以包含复合状态这类更粗的可见信息
- `(d)` 说明即使驱动循环完全藏在 hidden layer，仍然值得在 coarse-grained level 上定义 entropy production 和做 inference

#### Fluctuation Relation and Consistency

核心关系：

$$
e^{-\Delta S[\Gamma]} = \left\langle e^{-\Delta s}\mid \Gamma \right\rangle.
$$

**第 1 步：先看微观层定义**

在微观层，entropy production 的标准结构是正反轨迹概率比：

$$
\Delta s[\gamma] \sim \ln \frac{P[\gamma]}{P[\tilde{\gamma}]}.
$$

乘上负号后，比值会变成倒数：

$$
-\Delta s[\gamma] \sim \ln \frac{P[\tilde{\gamma}]}{P[\gamma]}.
$$

因此取指数后得到

$$
e^{-\Delta s[\gamma]} \sim \frac{P[\tilde{\gamma}]}{P[\gamma]}.
$$

这里写“近似同结构”只是提醒：本文对 snippet 和 endpoint 做了更细的处理，但骨架仍然是这条正反轨迹概率比。

**第 2 步：对固定的 coarse-grained trajectory 做条件平均**

对同一条 coarse-grained trajectory $\Gamma$，底层通常对应很多条不同的微观轨迹 $\gamma$。所以

$$
\left\langle e^{-\Delta s}\mid \Gamma \right\rangle
=
\sum_{\gamma \mapsto \Gamma}
P[\gamma \mid \Gamma]\,
e^{-\Delta s[\gamma]}.
$$

再把条件概率写成

$$
P[\gamma \mid \Gamma] = \frac{P[\gamma]}{P[\Gamma]},
$$

就得到

$$
\left\langle e^{-\Delta s}\mid \Gamma \right\rangle
=
\frac{1}{P[\Gamma]}
\sum_{\gamma \mapsto \Gamma}
P[\gamma]\,e^{-\Delta s[\gamma]}.
$$

代入上面的微观结构后，右边就变成

$$
\left\langle e^{-\Delta s}\mid \Gamma \right\rangle
\sim
\frac{1}{P[\Gamma]}
\sum_{\gamma \mapsto \Gamma}
P[\tilde{\gamma}].
$$

**第 3 步：把“所有映到 $\Gamma$ 的微观轨迹”变成“所有映到 $\tilde{\Gamma}$ 的反向微观轨迹”**

对每条映到 $\Gamma$ 的微观轨迹 $\gamma$ 做时间反演，就得到一条映到 $\tilde{\Gamma}$ 的反向微观轨迹 $\tilde{\gamma}$。因此上面那一堆反向轨迹权重的和，就是 coarse-grained 反向轨迹的概率：

$$
\sum_{\gamma \mapsto \Gamma} P[\tilde{\gamma}] = P[\tilde{\Gamma}].
$$

所以

$$
\left\langle e^{-\Delta s}\mid \Gamma \right\rangle
=
\frac{P[\tilde{\Gamma}]}{P[\Gamma]}
=
e^{-\Delta S[\Gamma]}.
$$

这就是那条精确关系的来源。

**第 4 步：它为什么和 fluctuation 直接相关**

因为对固定的 coarse-grained trajectory $\Gamma$，微观层并不是只有一条轨迹，而是一簇彼此不同的 $\gamma$。这些微观轨迹的 entropy production $\Delta s[\gamma]$ 会涨落；coarse-grained entropy production 不是它们的普通平均，而是它们的条件指数平均。

因此这篇讨论的不是单纯的平均 entropy production，而是 fluctuation-level relation。

**第 5 步：为什么 Jensen 不等式可以直接用**

一旦固定 $\Gamma$，所有满足 $\gamma \mapsto \Gamma$ 的微观轨迹就定义了一个条件分布

$$
P[\gamma \mid \Gamma].
$$

在这个条件分布下，$\Delta s$ 是一个随机变量。取

$$
f(x)=e^{-x},
$$

则

$$
f''(x)=e^{-x}>0,
$$

因此 $f$ 是凸函数。对条件分布使用 Jensen 不等式，

$$
f\!\left(\langle \Delta s \mid \Gamma \rangle\right)
\le
\left\langle f(\Delta s)\mid \Gamma \right\rangle.
$$

代回 $f(x)=e^{-x}$，就得到

$$
\left\langle e^{-\Delta s}\mid \Gamma \right\rangle
\ge
e^{-\langle \Delta s \mid \Gamma \rangle},
$$

于是

$$
e^{-\Delta S[\Gamma]}
\ge
e^{-\langle \Delta s \mid \Gamma \rangle}.
$$

由于 $e^{-x}$ 是单调递减函数，两边去指数后不等号方向反转，就得到

$$
\Delta S[\Gamma] \le \langle \Delta s \mid \Gamma \rangle.
$$

这条不等式的物理含义是：coarse-graining 会丢失信息，因此 coarse-grained level 上看到的不可逆性不会超过与它兼容的微观熵产生的条件平均值。

**第 6 步：什么叫“把 fluctuating entropy production 推广到 coarse-grained level”**

标准随机热力学的重要进展之一，是把 entropy production 从系统平均量推广成单条微观轨迹上的涨落量 $\Delta s[\gamma]$。这意味着不可逆性不只表现为

$$
\langle \Delta s \rangle,
$$

还表现为每一条具体轨迹各自的

$$
\Delta s[\gamma].
$$

这里的“系统级”与“轨迹级”区别就在于：

- 系统级：只关心总体平均，例如平均熵产生率、总平均耗散、整体不可逆性强弱
- 轨迹级：对每一条具体路径都赋一个物理量，例如单条轨迹的 entropy production

如果一个量只在平均后才有意义，那么它只能回答“系统整体上是否不可逆”。如果一个量在单条路径上就有定义，那么它还能回答“哪条路径更不可逆”“哪段 snippet 贡献了更多 irreversibility”。

这篇文章的关键推进，就是把这种轨迹级结构从微观轨迹 $\gamma$ 推广到 coarse-grained trajectory $\Gamma$。式

$$
\Delta S[\Gamma]
$$

不是只为了再求一个平均值

$$
\langle \Delta S \rangle,
$$

而是要让每一条 coarse-grained trajectory 本身就带有物理上可解释的 entropy production。原文所说的 `beyond its expectation value`，就是指 $\Delta S[\Gamma]$ 的意义不止体现在平均值上；它本身就是一个可用于轨迹比较、局域归因和 hidden driving 检测的涨落量。

#### Figure 3

`Figure 3` 的作用，是把上一节刚建立的观点真正画出来：

`coarse-grained entropy production 不只是平均量，它在单条轨迹、单类 snippet 和有限样本下都是会涨落的。`

这里先把图里的三个层次分清楚。作者先定义：

$$
\Delta s(t),\quad \Delta S(t),
$$

分别表示到时间 $t$ 为止，微观层和 coarse-grained 层的累计 entropy production。对应的瞬时平均速率写成

$$
\sigma(t)=\frac{\Delta s(t)}{t},
\qquad
\hat{\sigma}(t)=\frac{\Delta S(t)}{t}.
$$

然后，若只看某一类固定 snippet，也就是所有都从事件 $I$ 开始并以事件 $J$ 结束的 realizations，作者再定义局域化后的 entropy-production rate

$$
\sigma_{I\to J}(N)
=
\frac{1}{T(N)}
\sum_{i=1}^{N}\Delta s[\gamma_i],
$$

以及它的 coarse-grained 对应量

$$
\hat{\sigma}_{I\to J}(N)
=
\frac{1}{T(N)}
\sum_{i=1}^{N}\Delta S[\Gamma_i^s].
$$

因此，`Figure 3` 不是只在画一个总平均值，而是在按

`累计量 -> 速率 -> 局域 snippet 速率`

这条线往下细化。

**第 1 步：先看 `(a)`，它展示的是累计 entropy production。**

蓝线是微观层的 $\Delta s(t)$，红线是 coarse-grained 层的 $\Delta S(t)$。实线对应一条具体轨迹，虚线对应相应的期望值。这里最重要的信息不是数值大小，而是结构：entropy production 沿单条轨迹不是一个平滑常数，而是一个随时间随机累积的量。与此同时，红线整体低于蓝线，说明 coarse-graining 会丢失一部分不可逆性信息，因此 coarse-grained level 上累计到的 entropy production 更少。

**第 2 步：再看 `(b)`，它把累计量改写成 entropy-production rate。**

这一幅给出五条样本轨迹上的 $\sigma(t)$ 和 $\hat{\sigma}(t)$。这一步要说明：即使换成“每单位时间的熵产生率”，它依然不是一条稳定不动的曲线，而是会围绕平均值上下波动。图中的深色虚线给出对应的期望值，微观层大约是 $\langle \sigma \rangle \simeq 2.9$，coarse-grained 层大约是 $\langle \hat{\sigma} \rangle \simeq 1.7$。因此 `(b)` 进一步确认了两件事：第一，熵产生率本身也是涨落量；第二，粗粒化会系统性压低你能观测到的 irreversibility。

**第 3 步：`Figure 3` 的关键在 `(c)`，因为它第一次把熵产生局域到一类固定 snippet 上。**

这里作者不再统计整条轨迹，而只统计所有起点和终点都是

$$
\tilde K = (2 \to 1)
$$

的 snippets，也就是所有 $\tilde K \to \tilde K$ 的 realizations。这样做的目的，是把“总熵产生会不会波动”这个问题，缩小成“某一类局部事件的熵产生率会不会波动”。

**第 4 步：为什么同样都是 $\tilde K \to \tilde K$，`(c)` 里还会出现明显波动？**

这正是正文后面那段话在解释的内容。粗粒化层面看，每一次 realization 都只是“从 $\tilde K$ 出发，最后又回到 $\tilde K$”。但在微观层面，这类 realizations 对应很多条不同的隐藏路径。它们虽然起点和终点相同，中间经过的微观状态序列却不同，因此等待时间也往往不同。由于本文的 coarse-grained entropy production 来自正反 waiting-time statistics 的对数比，所以 waiting time 一旦变了，对应的 entropy production 也会变。换句话说，粗粒化虽然隐藏了路径形状，但没有抹掉路径持续时间，而 duration 的涨落本身就携带了 irreversibility 的信息。

**第 5 步：读 `(c)` 时，蓝色和红色的角色也要分清。**

蓝色对应 microscopic level，红色对应 coarse-grained level。蓝色更高、更散，是因为微观层保留了完整路径信息，所以看到的不可逆性更强，也更细。红色整体更低，说明 coarse-graining 丢掉了一部分关于正反不对称的信息，但仍然保留下非零的 entropy production。原图 caption 还特别提醒：蓝色点里包含单次微观 realization 的值，而正文中的 conditional bound 针对的是条件平均，因此不能把那条不等式直接逐点套到每个蓝色散点上。

**第 6 步：`(c)` 上方的 inset 给出的是收敛图。**

它展示随着样本数 $N$ 增加，局域化后的 entropy-production rate 会逐步趋于稳定。文中给出的收敛值是

$$
\sigma_{\tilde K\to \tilde K}(N)\to 1.15,
\qquad
\hat{\sigma}_{\tilde K\to \tilde K}(N)\to 0.70.
$$

这说明单次 realization 虽然噪声很大，但把越来越多次同类 snippet 累积起来之后，局域 entropy production rate 仍然会收敛到明确的期望值。

**第 7 步：把 `(a)(b)(c)` 连起来，`Figure 3` 的整张图其实在证明同一个主张。**

`(a)` 先说明 entropy production 在单条轨迹上就是随机累积的。`(b)` 再说明对应的 rate 也会波动。`(c)` 则把这种涨落性进一步压缩到一类固定 snippet 上，表明即使在 coarse-grained observation 下，只要 waiting-time asymmetry 还在，fluctuating entropy production 就不会消失，而是会以局域事件速率的形式保留下来。

因此，`Figure 3` 在全文中的位置非常关键。它不是在重复“平均 coarse-grained entropy production 小于微观 entropy production”这种结论，而是在更强的层面上展示：coarse-grained entropy production 依然可以被当作 trajectory-level quantity 来使用。后面的 `Table I` 正是在这个基础上继续往前走，把这种局域化能力进一步细分到不同事件对和不同时间窗口上。

#### Hidden Driving

`Section III` 是全文真正把“coarse-grained fluctuating entropy production”变成推断工具的一节。前面作者已经说明：在 coarse-grained level 上，单条 snippet 也有物理上可解释的 entropy production。这里作者进一步问：既然这个量会随 waiting time 波动，它能不能被反过来拿来检测 hidden driving？

这个 subsection 最好按下面这条线读。

**第 1 步：先明确 hidden driving 是什么。**

在 coarse-grained setup 里，观察者只能看到少数 Markovian events，其他微观状态和跃迁都被压进 hidden part。hidden part 不一定只是平衡背景，它本身也可能处于非平衡，并包含持续被驱动的循环。如果这些内部过程既不直接驱动任意两个可见 Markovian events 之间的转移，也不留下额外可见 observables，那么它们就是本文所说的 `hidden driving`。因此，作者真正想检测的不是“hidden part 是否复杂”，而是“hidden part 里是否存在真正被驱动的循环”。

**第 2 步：在 Markov network 里，hidden driving 的最典型来源是 hidden cycle 的非零 affinity。**

这里的 affinity 可以理解为一个循环沿某个方向被持续偏置的强度。若 affinity 为零，就对应 detailed balance；若 affinity 非零，就说明循环内部存在持续的不可逆流和持续耗散。困难在于，这种 hidden cycle 往往不会在可见层上表现成显式净流，所以光看可见事件标签，常常根本看不出它的存在。

**第 3 步：作者因此不去盯可见 current，而是固定一类可见 snippet，去看 waiting-time 统计。**

他们考察固定起点和终点的 snippets

$$
I \xrightarrow{t} J
$$

以及相应的 coarse-grained entropy production

$$
\Delta S[I \xrightarrow{t} J].
$$

如果 hidden part 只是平衡背景，那么同一类 snippet 的正反不对称通常不会在不同持续时间上表现出很强的结构差异。相反，若 hidden layer 中存在被驱动的循环，那么不同持续时间常常对应不同的隐藏路径族，这些路径族对正反过程的偏置不同，于是

$$
\Delta S[I \xrightarrow{t} J]
$$

就会显著依赖于 $t$。

**第 4 步：作者把这种时间依赖的振幅提取成一个量。**

他们定义

$$
\Delta a_{I\to J}
\equiv
\sup_t \Delta S[I \xrightarrow{t} J]
-
\inf_t \Delta S[I \xrightarrow{t} J].
$$

这个量不是新的 entropy production，而是同一类可见 snippet 在所有可能持续时间上，entropy production 的最大值和最小值相差多少。换句话说，$\Delta a_{I\to J}$ 测量的是该 snippet 的时间非均匀性有多强。

**第 5 步：这个振幅之所以重要，是因为它直接给出 hidden affinity 的下界。**

作者证明

$$
\max_C |A_C|
\ge
\Delta a_{I\to J},
$$

其中最大值遍历所有夹在 $I$ 和 $J$ 之间的 hidden cycles。物理意思是：可见层上观察到的时间依赖，不可能比隐藏循环里最大的真实驱动力还大。反过来说，只要

$$
\Delta a_{I\to J} > 0,
$$

就已经说明 hidden part 里至少存在一个 affinity 非零的 driven cycle，而且它的驱动力至少有这么大。于是这个框架同时完成了两件事：一方面它给出 detection，另一方面它还给出 lower bound。

**第 6 步：为什么作者还讨论“额外 observables”能不能加入？**

因为只看 $I$、$J$ 和总时长 $t$ 有时不够细。理论上，你还可以把 snippet 写成

$$
I \xrightarrow[t,O]{} J,
$$

其中 $O$ 表示这段过程中额外记录到的可见信息。这样做的目标，是进一步把混在一起的路径族拆开，从而更准确地定位 hidden driving。

**第 7 步：但这些额外 observables 不是随便加的。**

作者后面的 affinity bound 证明，依赖于构造一个与真实物理时间反演在给定 coarse graining 下不可区分的“部分时间反演”或“数学时间反演” $R$。因此，一旦加入额外 observable，新的 coarse-grained 描述仍然必须允许这样的 $R$ 存在。对本文的构造来说，这意味着额外 observables 必须在时间反演下是 even 的。于是，snippet 的总持续时间 $t$ 可以保留，但 snippet 内部更细的 waiting times 一般不能直接作为额外数据 $O$，因为它们会破坏时间反演的一致性。

**第 8 步：`Figure 5` 就是在演示“合适的额外 observable 会怎样改善推断”。**

`Figure 5(a)` 先给出一个最简单的可检测示意。那里画的是

$$
a_{1\to 6}(t),
$$

蓝线随 $t$ 明显变化，并给出

$$
\Delta a_{1\to 6} \simeq 3.3.
$$

这一步只是用一个最直接的例子说明：只要 $a(t)$ 随时间变化，hidden driving 就已经在可见层上留下了痕迹。

**第 9 步：`Figure 5(b)` 才真正展示“加入额外 observable 之后，localization 会增强”。**

这里作者考虑一个网络，其中观察者能看到状态 $1$、状态 $4$，以及 compound state

$$
H=\{8,9\}.
$$

于是从 $1$ 到 $4$ 的 snippets 可以再分成三类：

- 不经过 $H$ 的 $1 \to 4$
- 至少经过一次 $H$ 的 $1 \to 4$
- 不区分是否经过 $H$ 的全部 $1 \to 4$

图中的三条曲线对应的就是这三种统计。

**第 10 步：这三条曲线的物理结论是分工明确的。**

蓝线对应“不经过 $H$”的 trajectories，几乎是常数

$$
a(t) \simeq -0.51,
$$

几乎不随 $t$ 变化，所以它的 $\Delta a$ 近乎为零。这说明 $H$ 外部没有可检测的 hidden driving。绿色曲线对应“经过 $H$”的 trajectories，它随 $t$ 明显变化，并给出

$$
\Delta a \simeq 3.4.
$$

这说明真正的 hidden driving 主要和 $H$ 及其相关回路绑定在一起。红线对应把是否经过 $H$ 的信息丢掉之后的整体统计，此时只得到

$$
\Delta a \simeq 0.9,
$$

说明如果不利用这条额外 observable，信号会被混合平均，得到的 affinity 下界会明显变松。于是 `Figure 5(b)` 的真正信息是：合适的、时间反演下自洽的额外 observable，确实能把隐藏不可逆性从混合背景里剥离出来。

**第 11 步：作者最后还主动给出一个失效情形。**

他们指出，这个判据并不是无条件万能的，可能出现

$$
\Delta a = 0
\qquad \text{despite} \qquad
A \neq 0.
$$

如果一个 driven cycle 和其余网络只通过单一状态相连，或者更一般地，被封装在一个 compound state 里，并且所有进出该 compound state 的转移都满足 direction-time independence，那么外部可见 observables 就无法感受到内部驱动的方向性。此时，内部确实存在非零 affinity，但它不会让外部看到的 $a(t)$ 产生可辨别的时间依赖，因此从黑箱外部的 observables 出发就无法推断这部分 irreversibility。

**第 12 步：所以这个 subsection 的最终结论不是“任何 hidden driving 都能被抓出来”，而是一个更精确的说法。**

`只要 hidden driving 会在可见 snippet 的 waiting-time asymmetry 上留下痕迹，coarse-grained fluctuating entropy production 就能把它检测出来，并给出 hidden affinity 的下界；而合适的额外 observable 还能显著增强这种 localization。`

最后一句关于 recent preprint 的比较，也是在强调这一点：思想上都是利用 coarse-grained time statistics 的不对称来探测 hidden irreversibility，只是那篇工作用的是 propagator 的对数比，这里用的是 waiting-time distributions 的对数比，并且自然嵌进了 `Markovian event + snippet` 的框架。

## Paper 2

### Dynamical regimes of diffusion models

- 为什么第二篇读它：
  这篇不是泛泛的 diffusion 应用，而是用统计物理直接分析 diffusion model 的生成动力学，正好接你后面 `AI for physics` 的理论支线。
- 论文链接：
  https://www.nature.com/articles/s41467-024-54281-3
- 本地 PDF：
  [dynamical-regimes-of-diffusion-models.pdf](/Users/jinlin/Desktop/Project/Research_Collector/pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.pdf)

#### 1. 问题

这篇解决的问题是：

`diffusion model 的反向生成过程，在高维和大样本极限下，到底处于什么动力学机制之下。`

它不是在问“效果好不好”，而是在问：

- 生成轨迹什么时候只是噪声
- 什么时候开始识别类别结构
- 什么时候开始向训练样本塌缩

#### 2. 为什么重要

这篇值得你读，不是因为它发在 `NC`，而是因为它把一个你以后一定会碰到的问题说清楚了：

`diffusion model 到底是在 generalize，还是在 memorize。`

这和你后面想连接的 `statistical physics -> generative dynamics` 非常直接，因为它把：

- symmetry breaking
- glassy collapse
- curse of dimensionality

都翻译到了 diffusion model 的动力学语言里。

#### 3. 对象

优先抓住：

- forward noising process
- backward generative process
- exact empirical score
- high-dimensional data distribution

这篇的对象不是单个神经网络技巧，而是整个 backward diffusion trajectory。

#### 4. 演化

作者把 backward process 分成三个 regime：

1. 纯噪声阶段
2. `speciation` 阶段
3. `collapse` 阶段

先问：

`每个 regime 的物理图像是什么，切换时间由什么控制。`

#### 5. 量

这里的核心量是：

- speciation time
- collapse time
- correlation matrix spectrum
- excess entropy

关键点：

`一个时间由谱结构控制，另一个时间由熵结构控制。`

#### 6. 方法

方法不是常规机器学习实验，而是：

- 高维极限
- 统计物理分析
- Gaussian mixture toy model
- 再对真实数据集做数值验证

所以这篇要学的不是“怎么训练 diffusion model”，而是“怎么用统计物理给 diffusion dynamics 建相图”。

#### 7. 证据

优先看：

- Gaussian mixture 是否给出完整解析图像
- CIFAR-10 / ImageNet / LSUN 是否支持三阶段结构
- speciation 与 collapse 的预测时间是否可由数据结构估计

#### 8. 你要带走什么

结论：

`diffusion model 的 backward process 不是单一的 denoising 流，而是具有阶段结构的高维随机动力学。`

## Minimum Output

今天只需要产出两段笔记，每篇各 5 句即可。

### Paper 1

1. coarse-grained 情况下，作者重新定义了什么对象。
2. 它怎样把 irreversibility 定位到时间、空间或事件上。
3. 这个框架相对普通总熵产生估计多了什么信息。
4. hidden driving 在这里怎样被检测。
5. 哪个概念最值得放进你的主线。

### Paper 2

1. diffusion model 的三个 dynamical regimes 分别是什么。
2. speciation 和 collapse 各自对应什么物理图像。
3. 哪个时间由谱结构控制，哪个时间由熵结构控制。
4. 这篇怎样把 phase transition / glassy language 引进 generative model。
5. 它对你理解 `AI for physics` 最有用的一点是什么。
