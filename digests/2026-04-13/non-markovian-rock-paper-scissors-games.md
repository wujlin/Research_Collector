---
title: "Non-Markovian rock-paper-scissors games"
paper_title: "Non-Markovian rock-paper-scissors games"
digest_type: "paper_note"
date: "2026-04-13"
---

# Non-Markovian Rock-Paper-Scissors Games

## Core Answer

这篇文章的核心回答是：在三物种循环竞争的 `zero-sum rock-paper-scissors` 模型里，系统最终由谁存活，不只取决于平均增长率，还强烈取决于 waiting-time distribution 是否是指数分布，以及 waiting-time fluctuation 有多大。换句话说，一旦把 `Markovian exponential clock` 换成具有长期记忆和非指数等待时间的更新过程，经典的 `law of the weakest` 就不再稳固，甚至会被改写。

## 0. Reading Frame

为了防止后面一上来就陷进生物学比喻，先把这篇文章的阅读框架固定下来：

1. 它要解决的问题是：memory 和 nonexponential waiting times 会怎样改变经典多物种竞争动力学。
2. 它重要的地方在于：真实生态相互作用常常不是无记忆的 Poisson clock，而是带有长 waiting time 和强波动。
3. 它研究的对象是 `zero-sum rock-paper-scissors (zRPS)`，也就是三物种循环竞争的最简模型。
4. 它的核心对照是：`Markovian benchmark` 对应指数等待时间，`non-Markovian extension` 对应更一般的 waiting-time law。
5. 它真正关心的结果不是瞬时轨迹，而是 large well-mixed population 里“最终哪一个 species 最可能胜出”。
6. 它最关键的比较量不是只有平均 waiting time，还包括 waiting-time distribution 的形状，尤其是 `coefficient of variation`。
7. 你最后要带走的是：在非马尔可夫竞争里，时间统计本身就会改写选择规则，而不是只在原来的规则上加一点噪声。

## 1. What The zRPS Model Actually Is

先把名字拆开。

`rock-paper-scissors` 指的是一种循环竞争关系：一种 species 压制第二种，第二种压制第三种，第三种再压制第一种。它不是合作网络，而是一个闭环的竞争结构。

如果用三个 species 表示，最常见的写法就是：

$$
A \to B,\qquad B \to C,\qquad C \to A
$$

这里的箭头不是“变成”，而是“在竞争中压制 / 取代 / 战胜”的方向。和石头剪刀布完全一样，没有绝对最强者，只有循环优势。

`zero-sum` 的意思是：一个 species 的增长，直接对应另一个 species 的减少，系统总个体数保持不变，或者至少每次基本事件只是在 species 之间重新分配占据者，而不是凭空增减总量。

所以这确实是一个 `many-body population problem`，但不是那种复杂到一上来就要处理全空间相关函数的多体问题。更准确地说：

1. 微观基本事件通常是 pairwise competition。
2. 宏观状态却是三个 species 的总体数量或密度。
3. 因此它在系统层面是 many-body stochastic dynamics，在事件层面却是非常简洁的循环相互作用。

这正是为什么 zRPS 常被当作理论模型：结构足够简单，能清楚看出规则改动以后谁在改变最终命运。

## 2. What The Abstract Is Doing

这个 abstract 的逻辑不是在堆背景，而是沿着一条很清楚的线往前推。

第一步，作者先指出现实动机。真实 species interaction 往往有 `long-term memory`，连续事件之间的 waiting time 差异很大，而且还存在长时间相关。这意味着：真实系统的时间结构并不像 Poisson process 那样干净。

第二步，他们马上指出这会动摇什么。它动摇的是最常见的 `Markovian assumption`。因为一旦 waiting time 带有记忆、相关和重尾，系统未来就不能只由当前状态决定，而会和已经经历过多久、过去等待了多久有关。

第三步，作者选择一个最简但不平凡的对象来研究这个问题：`zero-sum rock-paper-scissors`。这一步很关键，因为他们不是在一开始就上复杂生态网络，而是先用一个标准循环竞争模型把“memory 改写竞争结局”这件事讲清楚。

第四步，他们声明自己的工作不是只做数值实验，而是建立一个 `general non-Markovian formalism`。也就是说，他们要给出一套能处理一般 waiting-time law 的理论框架，而不是只展示某个特殊分布下的模拟现象。

第五步，他们先回到经典 Markovian benchmark。若 waiting time 是指数分布，系统就是 Markovian。此时 large well-mixed population 的结局服从一个很经典的规则，叫做 `law of the weakest (LOW)`：增长率最低的 species 反而最可能长期存活。

第六步，作者真正的新结论才出现：一旦 waiting time 不再是指数分布，这个 survival behavior 和 `LOW` 都会被显著改变。尤其关键的不是只有平均 waiting time，而是 waiting-time fluctuation 本身，特别是 `coefficient of variation`。

第七步，这就把文章的主结论压出来了：在 non-Markovian evolutionary dynamics 里，`时间统计不是背景噪声，而是决定最终选择规则的一部分`。

## 3. How To Read The Abstract In One Line

一句话总结这个 abstract：

`经典 zRPS 模型里“谁能活到最后”这件事，本来由无记忆指数时钟控制；这篇文章证明，一旦相互作用时钟变成带记忆的非指数过程，最终的生存规则本身就会被 waiting-time distribution 及其波动强度改写。`

## 4. Immediate Questions To Carry Forward

接下来读正文时，最值得追的不是泛泛的生态学背景，而是下面四个问题：

1. 他们怎样精确定义 non-Markovian waiting-time dynamics。
2. `law of the weakest` 在 Markovian 情况下到底是怎么得出来的。
3. 非指数 waiting times 是通过平均值、尾部，还是通过 `coefficient of variation` 改写结果。
4. 这个框架最后给出的，是定性图像、相图，还是显式可计算的胜出条件。

## 5. A. Basic Model: The Markovian Benchmark They Will Later Deform

![Figure 1a: Markovian zRPS dynamics in the ternary simplex](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-01-figure-01.jpg)

![Figure 1b: power-law waiting time on the A+B reaction](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-01-figure-02.jpg)

![Figure 1c: gamma waiting time on the A+B reaction](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-01-figure-03.jpg)

![Figure 1d: RGB fixation-color legend](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-01-figure-04.jpg)

这一小节的任务不是直接给 non-Markovian 结果，而是先把后面所有比较都要依赖的 `Markovian benchmark` 固定下来。换句话说，作者先要回答：经典 zRPS 在最标准、最干净的设定下，状态空间长什么样，动力学怎样演化，fixation 问题到底是怎样出现的。

第一步，作者先定义系统对象。系统是一个 `well-mixed` 的有限群体，总人数固定为

$$
N=n_A+n_B+n_C.
$$

这里 `well-mixed` 的意思是：不考虑空间位置，每个个体都近似随机接触其他个体。因此系统状态只由三个 species 的数量

$$
n_A,\qquad n_B,\qquad n_C
$$

决定，而不由空间分布决定。这一步要记住，因为后面文章讨论的不是“空间结构 + 记忆”共同作用，而是先把空间拿掉，只看 waiting-time memory 怎么改写竞争结局。

第二步，作者把循环竞争规则写成最标准的三条 `predation with reproduction` 反应：

$$
A+B \xrightarrow{k_A/N} A+A,\qquad
B+C \xrightarrow{k_B/N} B+B,\qquad
C+A \xrightarrow{k_C/N} C+C.
$$

这里的含义是：prey 被杀死，同时 predator 复制一个自己，因此总人数不变。这正是 `zero-sum` 的具体体现。后面所有 `payoff`、`predation-reproduction rate` 和 `law of the weakest`，说的其实都是这里的

$$
k_A,\qquad k_B,\qquad k_C.
$$

第三步，作者先给出无限大群体、无噪声极限下的 mean-field 方程。写成种群比例

$$
a=\frac{n_A}{N},\qquad b=\frac{n_B}{N},\qquad c=\frac{n_C}{N},
$$

Markovian dynamics obey

$$
\dot a=a(k_A b-k_C c),\qquad
\dot b=b(k_B c-k_A a),\qquad
\dot c=c(k_C a-k_B b).
$$

这三条式子的结构非常重要，因为后面 non-Markovian 推广时，作者改写的正是这里的有效反应项，而不是整个模型对象。

第四步，作者指出这个 deterministic mean-field 系统有两类 steady states。一类是三个吸收态：

$$
(1,0,0),\qquad (0,1,0),\qquad (0,0,1),
$$

也就是只剩一种 species。另一类是内部共存点

$$
\mathbf s^*=(a^*,b^*,c^*)
=
\frac{1}{k_A+k_B+k_C}(k_B,k_C,k_A).
$$

这个公式要记住，因为它已经体现出循环竞争的“间接性”：某个 species 的稳态占比，不是简单由它自己的速率单独决定，而是和整条竞争环上的相对速率一起决定。

第五步，作者进一步指出 Markovian mean-field 系统还有一个守恒量

$$
\mathcal R(t)=a^{k_B}b^{k_C}c^{k_A}.
$$

这意味着 deterministic dynamics 不会自动走向灭绝，而是在共存点周围形成中性闭轨道。`Figure 1(a)` 画的正是这件事：灰色随机轨迹在三角相图里顺时针绕圈，红色粗线给出最外层的 deterministic orbit。每个角点都对应某一个 species 的 fixation。

第六步，这里出现了这一小节最关键的转折：如果只看 mean-field 方程，系统本来不会 fixation；真正导致长期 fixation 的，是有限群体里的 demographic fluctuations。一旦 $N<\infty$，随机 birth-death / replacement events 会让轨迹不再守恒地困在某一条闭轨道上，而是慢慢在轨道之间随机漂移，先碰到三角形边界，再最终掉到某个角点。于是：

- 两个 species 灭绝
- 一个 species fixation

所以这一节真正建立起来的是：`长期结局不是 deterministic orbit 给出的，而是 finite-N stochasticity 给出的。`

第七步，作者因此把后面整篇文章要比较的对象明确成 `fixation probability`。对于 species $i$，定义

$$
\phi_i=\lim_{t\to\infty}\mathrm{Prob}\{n_i(t)=N\}.
$$

这就是后面 LOW、non-Markovian correction、waiting-time fluctuation 这些讨论真正要落到的终极量。也就是说，文章最后不是在问“短期谁增长更快”，而是在问“长期谁最可能成为唯一幸存者”。

第八步，`Figure 1` 在这里的作用不是只做插图，而是提前把后面的主线可视化出来：

1. `Figure 1(a)` 给出标准 Markovian benchmark：闭轨道加有限-N 漂移，最后去某个角点。
2. `Figure 1(b)` 和 `Figure 1(c)` 先剧透了后文的 non-Markovian 结果：只改动第一条反应的 waiting-time law，三角相图中的外层轨道和最终 fixation 区域就会变。
3. `Figure 1(d)` 只是颜色图例，告诉你后面 fixation heatmap 里红、绿、蓝分别对应哪个胜者。

所以，`Figure 1` 不是“结果图先行”，而是把整篇文章的比较框架先摆在你面前：同一个 zRPS 模型，在不同 waiting-time law 下，最终朝哪个角点坍缩会发生系统性改变。

### What To Retain From This Subsection

如果这一节只记 6 件事，就记下面这些：

1. 这是一个 `well-mixed`、总人口固定的三物种 `zero-sum` 循环竞争模型。
2. 基本事件是 `predation with reproduction`，对应三条反应率 $k_A,k_B,k_C$。
3. 在 Markovian mean-field 极限下，系统 obeys 一组三变量 rate equations。
4. 内部共存点是
   $$
   \mathbf s^*=\frac{1}{k_A+k_B+k_C}(k_B,k_C,k_A).
   $$
5. deterministic dynamics 有守恒量
   $$
   \mathcal R(t)=a^{k_B}b^{k_C}c^{k_A},
   $$
   因而产生中性闭轨道，而不是自动 fixation。
6. 真正导致长期 fixation 的是 finite population 的 demographic fluctuations；后文所有 LOW 和 non-Markovian 结果，都在比较三者的 fixation probabilities $\phi_A,\phi_B,\phi_C$。

## 6. B. The Law Of The Weakest Under Markovian Dynamics

这一小节的角色非常清楚：先把经典 Markovian zRPS 的长期结局钉死，作为后面一切 non-Markovian 偏离的基准。也就是说，作者现在还没有开始讨论 memory，而是在先回答：如果 waiting times 就是最普通的指数分布，那么 large well-mixed population 的 fixation 规则到底是什么。

第一步，作者正式写出 `law of the weakest (LOW)` 的数学表述。若三条反应都 obey exponential waiting-time distributions，也就是系统是 Markovian，那么对于足够大的群体，species $i$ 和 $j$ 的 fixation probabilities 满足

$$
\phi_i>\phi_j
\quad \text{if} \quad
k_i<k_j.
$$

这条关系的意思很直接：反应率较低的 species，反而更容易最终占据整个群体。也就是说，经典 zRPS 的长期结局不是“最强者通吃”，而是“最弱者最可能通吃”。

第二步，作者强调 LOW 在大群体极限下会进一步变成一个 `zero-one law`。如果某一个 species 的速率严格最小，例如 $k_m<k_n,k_l$，那么当 $N$ 足够大时，

$$
\phi_m\to 1,\qquad
\phi_n,\phi_l\to 0.
$$

所以 LOW 不是一个轻微偏差，而是在大群体里会越来越接近确定性的选择规则：最弱 species 最终几乎必然 fixation，其余 species 几乎必然灭绝。

第三步，作者说明 LOW 不只是一个口号，而是在参数空间里给出一个很清楚的相图分区。因为 Markovian 情况下，最终谁最可能胜出，只取决于三条速率

$$
k_A,\qquad k_B,\qquad k_C
$$

的大小排序。于是参数空间会被简单的线性边界切开：在哪一块区域里 $A$ 最弱，$A$ 最可能胜出；在哪一块区域里 $B$ 最弱，$B$ 最可能胜出；$C$ 同理。如果有两个 species 的速率相同且都低于第三个，那么第三个最可能灭绝，而前两个会对称地分享生存概率。

第四步，作者接着解释 LOW 为什么会出现。这里要把上一小节的相空间图像接上来：deterministic mean-field dynamics 本来给出的是围绕共存点的闭轨道，而 finite-$N$ demographic fluctuations 会让真实随机轨迹在这些闭轨道之间慢慢漂移。当轨迹漂到最外层 orbit 时，系统就很容易碰到 simplex 的边界，并最终掉进某个角点，也就是某个 species fixation。

关键的几何事实是：利用共存点

$$
\mathbf s^*
$$

和守恒量

$$
\mathcal R(t)
$$

可以论证，这条最外层 orbit 离“最弱 species fixation”对应的边界最近。因此随机漂移最容易先从那一侧漏出去。于是 LOW 的相空间机制并不是“最弱 species 在单次对抗里更强”，而是：`随机轨迹在相空间里最容易从通向最弱 species fixation 的那一侧逃逸。`

第五步，作者最后补了一个重要边界条件：LOW 不是所有群体规模下都成立。如果 $N$ 很小，系统会进入另一套小群体规则，fixation probabilities 对初始条件更敏感，这时讨论的是所谓 `law of stay out`。但本文后面全部假设

$$
N\ge 10^2,
$$

所以小群体效应被主动排除。这样后面如果看到 LOW 被改写，就能更清楚地归因于 waiting-time memory，而不是归因于 small-$N$ noise structure。

### What To Retain From This Subsection

如果这一节只记 5 件事，就记下面这些：

1. 在 Markovian zRPS 里，指数 waiting times 对应经典 benchmark：`law of the weakest`。
2. LOW 的核心数学关系是
   $$
   k_i<k_j \Rightarrow \phi_i>\phi_j.
   $$
3. 在大群体极限下，LOW 会变成 zero-one law：最弱 species 的 fixation probability 趋近于 1。
4. LOW 的几何机制是：finite-$N$ 随机轨迹最容易从通向最弱 species fixation 的那一侧逃离最外层 orbit。
5. 这篇文章后面只研究大群体，因此如果 LOW 被改写，主要归因于 non-Markovian waiting times，而不是小群体效应。

## 7. C. RPS Under Exponential WTD

这一小节的作用不是再重复 LOW，而是把 `Markovian` 具体落到一个清楚的时间统计对象上。作者想先说清楚：在这篇文章里，“反应是 Markovian”到底是什么意思；只有这样，后面你才能明白 non-Markovian 改的是哪一层。

第一步，作者先把 Markovian 的时间结构写成 waiting-time distribution。对连续时间 Markov 过程来说，事件之间的等待时间 obey 指数分布：

$$
\psi_{\mathrm{ex}}(\tau)=\lambda e^{-\lambda \tau},
\qquad
\langle \tau\rangle = \lambda^{-1}.
$$

这里最重要的不是公式形式本身，而是：指数时钟只有一个参数 $\lambda$。这意味着一旦平均等待时间固定，整条 waiting-time law 就固定了；Markovian clock 没有额外的形状自由度。

第二步，作者把这条一般结论代回 zRPS 的三条反应里，于是三个反应的 event rate 分别是

$$
\lambda_A = N k_Aab,\qquad
\lambda_B = N k_Bbc,\qquad
\lambda_C = N k_Cac.
$$

这一步很关键，因为它把前面 `reaction rate` 的语言和这里 `waiting-time clock` 的语言接上了。在 Markovian 情况下，两者其实绑死在一起：谁的 $k_i$ 大，谁的平均 waiting time 就短。因此 LOW 之所以能只用 $k_A,k_B,k_C$ 排序，本质上是因为指数分布把“动力学强度”和“时间统计”压缩成了同一个参数。

第三步，作者接着列出指数分布的几个统计量：方差、coefficient of variation 和 median。这里最值得记住的是

$$
\mathrm{var}(\tau)=\lambda^{-2},\qquad
\mathrm{CV}(\tau)=1,\qquad
\bar\tau=\frac{\ln 2}{\lambda}.
$$

其中真正关键的是

$$
\mathrm{CV}(\tau)=1.
$$

因为这给了后面所有 non-Markovian waiting times 一个非常干净的基准：指数分布的相对波动强度固定为 1。只要某个 waiting-time law 的 $\mathrm{CV}>1$，就说明它比指数分布更宽、更不规则、更容易出现“平均值不代表典型事件”的情况。

第四步，作者随后说明后面的 non-Markovian 分析会怎样做控制变量。为了避免把问题搞得太复杂，他们不会一下子把三条反应都改掉，而是只改第一条反应

$$
A+B\to A+A,
$$

让它服从一个非指数 WTD，记为 $\psi_A(\tau)$；而另外两条反应继续保持 Markovian 的指数时钟。这样做的逻辑很干净：只改变一个 clock，就看 LOW 是否会被改写。

第五步，作者还说明为什么选 `power-law` 和 `gamma` 这两类 WTD。前者用来代表生态和生物系统里常见的 heavy-tailed waiting times；后者用来研究在平均值之外，distribution shape 本身，例如 skewness、median 和波动强度，会怎样影响竞争结局。这里他们特别强调关注

$$
\mathrm{CV}(\tau)>1
$$

的区间，因为指数分布的基准正好是 1，而显著偏离 LOW 最可能就发生在这种“比指数分布更宽”的 waiting-time law 上。

所以，这一小节真正完成的工作是：把指数 waiting time 立成一个时间统计基准。后面一旦 LOW 被改写，你就能明确知道，变的不是基础 zRPS 模型对象，而是其中某一条反应的时钟结构。

### What To Retain From This Subsection

如果这一节只记 5 件事，就记下面这些：

1. 这篇里 `Markovian` 的具体含义，就是反应 waiting time 服从指数分布。
2. 指数分布只有一个时间参数 $\lambda$，平均等待时间是 $\lambda^{-1}$。
3. 在 zRPS 里，
   $$
   \lambda_A=N k_Aab,\qquad
   \lambda_B=N k_Bbc,\qquad
   \lambda_C=N k_Cac.
   $$
4. 指数分布最关键的基准性质是
   $$
   \mathrm{CV}(\tau)=1.
   $$
5. 后面的 non-Markovian 比较采用“只改一条反应的 waiting-time law”的控制策略，并重点盯住 $\mathrm{CV}>1$ 时 LOW 如何被改写。

## 8. What Coefficient Of Variation Actually Means

`coefficient of variation`，通常记作 `CV`，就是“标准差除以平均值”：

$$
\mathrm{CV}(\tau)=\frac{\sqrt{\mathrm{var}(\tau)}}{\langle \tau\rangle}.
$$

它衡量的不是等待时间绝对有多大，而是：`相对于平均值，waiting time 本身有多不稳定。`

这和只看均值完全不是一回事。两个 waiting-time distributions 可以有相同的平均值，但如果一个分布很窄、几乎每次都差不多，另一个分布很宽、经常特别短或特别长，它们的动力学影响会非常不同。CV 就是用来量化这种“相对波动强度”的。

你可以把它这样理解：

- `CV` 小：waiting times 集中在均值附近，时钟比较稳定。
- `CV = 1`：这正是指数分布的基准情况。
- `CV > 1`：分布比指数分布更宽，等待时间更不规则，更容易出现 bursty 或长尾行为。
- `CV < 1`：分布比指数分布更窄，时钟更规则。

对这篇文章来说，CV 之所以重要，是因为作者要证明：

`改写 LOW 的，不只是平均 waiting time，而是 waiting-time law 的相对波动强度。`

如果两条反应的平均 waiting time 一样，但其中一条的 CV 更大，那么这条反应在动力学上就可能表现得完全不同。也正因此，后面 power-law 和 gamma WTD 的比较，不能只盯着均值，而必须盯着 CV、median 和分布形状。

## 9. II.A. RPS Survival Behavior With Power-Law WTD

![Figure 2: same mean, very different typical waiting times](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-03-figure-01.jpg)

这一小节真正要做的，不是马上给出最终相图，而是先把后面 power-law 结果的比较基准立起来。作者要先说明：如果只把第一条反应的时钟改成 heavy-tailed waiting-time law，那么应该怎样和经典指数时钟做公平比较，以及为什么单看平均 waiting time 已经不够了。

第一步，作者明确这节到底改了哪一部分。他们只把第一条反应

$$
A+B\to A+A
$$

的 interevent time 改成 power-law WTD，而另外两条反应仍保持 Markovian 的指数时钟。因此这一节研究的不是“整个系统完全非马尔可夫化”之后会怎样，而是：`只改 A 对 B 的时钟，survival / fixation 规则会怎样变。`

第二步，作者写出 power-law WTD 的具体形式：

$$
\psi_A(\tau_A)
=
\Lambda_A
\frac{\alpha_A}{(1+\Lambda_A\tau_A)^{\alpha_A+1}},
\qquad
\alpha_A>1,\ \Lambda_A>0.
$$

这个式子的重要点不只是形式上不是指数分布，而是它引入了 heavy tail。也就是说，和指数时钟相比，特别长的 waiting times 现在会更常见，这正是 non-Markovian memory 的一个时间统计表现。

第三步，作者接着列出这个 power-law WTD 的关键统计量：均值、方差、中位数以及

$$
\mathrm{CV}_A
=
\frac{\sqrt{\mathrm{var}(\tau_A)}}{\langle \tau_A\rangle}
=
\sqrt{\frac{\alpha_A}{\alpha_A-2}}.
$$

这一组公式不能只当成“把统计量列一下”，因为它们其实在告诉你 non-Markovian clock 到底比 Markovian clock 多出了什么结构。这里至少要看四层意思。

第一，均值

$$
\langle \tau_A\rangle=\frac{1}{\Lambda_A(\alpha_A-1)}
$$

告诉你为什么作者要求

$$
\alpha_A>1.
$$

只有在这个条件下，平均 waiting time 才是有限的，系统才谈得上和 Markovian benchmark 做“同均值比较”。

第二，方差

$$
\mathrm{var}(\tau_A)=\frac{\alpha_A\langle \tau_A\rangle^2}{\alpha_A-2}
$$

告诉你为什么

$$
\alpha_A=2
$$

是个关键门槛。当 $\alpha_A>2$ 时，方差有限；而当 $1<\alpha_A\le 2$ 时，均值虽然还有限，但方差已经发散。这说明 heavy tail 在这里不是轻微修饰，而是会把时间波动推到极端强的区间。

第三，中位数

$$
\bar\tau_A=\frac{2^{1/\alpha_A}-1}{\Lambda_A}
$$

告诉你：`平均 waiting time 不等于典型 waiting time。` 一旦分布有长尾，少数特别长的等待时间就可以把均值拉得很大，但多数事件实际发生得仍然可能更早。也就是说，后面作者反复强调的“mean 和 typical event 可以脱钩”，在这里已经通过 median 被量化出来了。

第四，

$$
\mathrm{CV}_A=\sqrt{\frac{\alpha_A}{\alpha_A-2}}
$$

告诉你 power-law 时钟的相对波动强度如何随 $\alpha_A$ 改变：

- 当 $\alpha_A\to\infty$ 时，$\mathrm{CV}_A\to 1$，回到指数分布基准。
- 当 $\alpha_A\to 2^+$ 时，$\mathrm{CV}_A\to\infty$，waiting-time fluctuation 会急剧放大。

所以 `Eq. (9)` 的真正作用是：把 “power-law WTD 不只是改了平均速度，而是改了整个时间不规则性” 这件事第一次定量写清楚。

换句话说，进入 power-law WTD 后，系统的时间结构就不再能只靠一个 rate 参数描述。现在至少有两层信息：

1. 平均多久发生一次事件。
2. 这些 waiting times 围绕均值到底有多宽、多不规则。

第四步，作者做了一个非常关键的比较选择：为了和 Markovian benchmark 公平比较，他们要求 power-law WTD 的平均 waiting time 与指数分布情况相同，也就是要求

$$
\langle\tau_A\rangle=\lambda_A^{-1},
\qquad
\lambda_A=Nk_Aab.
$$

这会导出参数约束

$$
\Lambda_A=\frac{\lambda_A}{\alpha_A-1}.
$$

这一步必须记住，因为它说明作者不是靠“改慢平均反应速度”来制造差异，而是固定平均时钟，只看 distribution shape 本身会不会改写 LOW。

第五步，在这个均值匹配规则下，作者马上指出 power-law 和指数时钟的真正差异。虽然两者的平均 waiting time 一样，但 power-law WTD 的 variance 更大；并且：

- 当 $\alpha_A\to\infty$ 时，
  $$
  \mathrm{CV}_A\to 1,
  $$
  也就是退回指数分布的 Markovian 基准。
- 当 $\alpha_A\to 2$ 时，
  $$
  \mathrm{CV}_A\to\infty,
  $$
  waiting-time fluctuation 会变得极端强。

所以这一节最核心的物理信息是：`真正被改变的不是均值，而是时间波动和尾部结构。`

第六步，作者据此提出一个比 LOW 更细的判断：对于 heavy-tailed WTD，survival / fixation behavior 不能再只靠 mean interevent time 来推断。原因是，平均等待时间大，并不等于典型事件真的来得慢。一个分布可以有很长的尾巴，从而把均值拉大；但它最常见、最典型的 waiting times 却依然很短。

这一步很重要，因为它直接动摇了 LOW 的基础：在 Markovian 情况下，平均速率就足以代表动力学快慢；而在 heavy-tailed non-Markovian 情况下，平均值已经不再能单独代表“典型动力学”。

第七步，`Figure 2` 就是为这件事服务的直觉图。虽然这一小节研究的是 power-law WTD，但作者在这里用 gamma WTD 画图，是为了更直观地说明一个一般事实：`相同均值，不代表相同典型等待时间。`

图里的红线是指数分布，蓝线是 gamma 分布。它们的均值相同，但 median 差很多。作者借这张图强调：

`如果某条反应的 mean waiting time 看起来很长，并不意味着它在动力学上就一定“更弱”；因为典型 waiting time 可能其实更短，事件可能更早、更密集地发生。`

因此，即使

$$
k_A<k_B,k_C,
$$

species $A$ 也不一定仍然是最可能存活的 species。换句话说，LOW 的判断规则在这里已经开始失稳。

### What To Retain From This Subsection

如果这一节只记 5 件事，就记下面这些：

1. 作者只把第一条反应的时钟改成 power-law WTD，其余反应保持指数时钟。
2. 他们采用了一个很关键的公平比较原则：固定平均 waiting time 不变。
3. 在这个比较下，真正被改变的是 waiting-time distribution 的形状，尤其是 tail、variance 和 CV。
4. 当 $\alpha_A\to\infty$ 时会回到 Markovian 基准；当 $\alpha_A$ 接近 2 时，waiting-time fluctuation 会显著增强。
5. 这一节最关键的结论不是谁赢，而是：`LOW 不能再只靠平均 waiting time 来判断，因为典型事件与平均事件已经可能脱钩。`

## 10. II.B. Generalized Rate Equations Under Power-Law WTD

![Figure 3a: coexistence point versus inverse shape parameter under power-law WTD](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-04-figure-01.jpg)

![Figure 3b: coexistence point versus $k_A$ under power-law WTD](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-04-figure-02.jpg)

这一小节真正的任务，是把前一节的直觉判断变成动力学方程。前面作者已经说明：一旦 waiting time 不是指数分布，LOW 不能再只靠平均 waiting time 来判断。现在他们要进一步回答：`这种 non-Markovian waiting time 到底怎样进入 mean-field dynamics？`

第一步，作者先把问题收得很窄：仍然只改第一条反应

$$
A+B\to A+A
$$

的时钟，让它 obey power-law WTD，而另外两条反应继续保持指数时钟。这样做的逻辑是：不是把整个系统都复杂化，而是只改一个 clock，看看这一条记忆效应能否单独改写整体竞争结构。

第二步，作者说明原来的 Markovian rate equations 已经不够用了。在指数时钟下，mean-field dynamics 可以直接写成局部、瞬时的速率方程；但一旦第一条反应有 memory，系统未来就不再只由当前状态决定，而会和过去的 waiting history 有关。因此，原来的瞬时反应项必须被 generalized equations 取代。

第三步，利用 continuous-time random walk 的 formalism，作者把 Markovian mean-field equations 改写成

$$
\dot a = abk_A\Theta(a,b,c)-ack_C,
$$

$$
\dot b = bck_B-abk_A\Theta(a,b,c),
$$

$$
\dot c = ack_C-bck_B.
$$

这组三式最关键的结构是：`只有第一条反应项被改写了。` 原来这条项是

$$
abk_A,
$$

现在变成了

$$
abk_A\Theta(a,b,c).
$$

所以 non-Markovianity 在 mean-field 层的表现，不是加一个额外噪声，而是把原来那条瞬时反应强度乘上一个状态依赖的 `memory kernel`。

第四步，作者进一步给出这个 power-law case 的 memory kernel

$$
\Theta_{\mathrm{PL}}(a,b,c)
=
\chi
\left\{
\left[
1-e^{(\alpha_A-1)\chi}\alpha_A E_{\alpha_A+1}\bigl((\alpha_A-1)\chi\bigr)
\right]^{-1}
-1
\right\},
$$

其中

$$
\chi=\frac{c(bk_B+ak_C)}{abk_A}.
$$

你现在不用去死记这个核的解析形式，但要抓住它的物理含义：第一条反应的有效通量，已经不再只由自己的 bare rate 决定，而是被整个系统当前组成状态

$$
(a,b,c)
$$

调制。也就是说，memory 已经把“单条反应的时钟”变成了“与整条竞争环耦合的有效反应项”。

第五步，作者继续保持前一节建立的公平比较原则：虽然第一条反应现在 obey power-law WTD，但仍要求它的平均 waiting time 与指数时钟 benchmark 相同，也就是继续使用

$$
\Lambda_A=\frac{\lambda_A}{\alpha_A-1},
\qquad
\lambda_A=Nk_Aab.
$$

这一步仍然非常关键，因为它保证这里观察到的动力学偏离，不是因为平均反应速度被改了，而是因为 waiting-time law 的 shape 和 memory 被改了。

第六步，作者随后用 generalized equations 去求新的 coexistence equilibrium。这里出现了这小节的第一个关键结论：即使保持同均值，只要第一条反应的时钟变成 power-law WTD，经典 Markovian 的共存点也会偏移。

最简单的情形是

$$
k_A=k_B=k_C=1.
$$

在 Markovian benchmark 下有

$$
a^*=b^*=c^*=\frac13.
$$

但在 finite $\alpha_A$ 的 power-law case 下，作者发现会变成

$$
a^*=b^*<c^*.
$$

这件事的意义非常大：`只改一条反应的 waiting-time law，就足以打破原来完全对称的共存结构。`

这也是 `Figure 3(a)` 和 `Figure 3(b)` 最该读的地方。它们不是在给你看“参数扫描很多”，而是在说明：共存点本身会随着 $\alpha_A$ 和 $k_A$ 系统性移动，而这种移动是由 non-Markovian time structure 驱动的。

第七步，为了进一步拿到解析理解，作者研究

$$
\alpha_A\gg 1
$$

的极限。这个极限很重要，因为它对应 power-law WTD 接近指数分布，因而能把 non-Markovian correction 当成对 Markovian benchmark 的可控小偏离。此时 memory kernel 可以近似成

$$
\Theta_{\mathrm{PL}}(a,b,c)
\simeq
\alpha_A\chi\,[1+(\alpha_A-1)\chi]^{-1}.
$$

这条近似最好不要只当成一个技术步骤，而要线性地看它在说什么。

第一，它把 memory kernel 的结构压缩成了“一个由 $\alpha_A$ 控制的有理函数”。这里

$$
\chi=\frac{c(bk_B+ak_C)}{abk_A}
$$

衡量的是：其余两条反应对第一条反应的相对竞争强度有多大。于是这个近似式告诉你，第一条反应的有效通量不再只是

$$
abk_A,
$$

而是会被一个同时依赖 `distribution shape` 和 `current population composition` 的因子重新缩放。

第二，这条式子把 Markovian 极限和 non-Markovian 偏离写得很清楚。当

$$
\alpha_A\to\infty,
$$

它会退回

$$
\Theta_{\mathrm{PL}}(a,b,c)\to 1,
$$

也就是恢复经典指数时钟下的 bare reaction term。有限的 $\alpha_A$ 则对应一个显式偏离。这里需要把含义拆开。

第一，在 Markovian benchmark 里，第一条反应的 mean-field 通量就是

$$
abk_A.
$$

第二，在 finite $\alpha_A$ 时，这条通量会变成

$$
abk_A\,\Theta_{\mathrm{PL}}(a,b,c),
$$

而此时通常

$$
\Theta_{\mathrm{PL}}(a,b,c)\neq 1.
$$

这意味着第一条反应的有效强度不再等于 bare rate，而是被 memory kernel 重整了。

第三，这个偏离不是一个固定常数偏移，因为

$$
\Theta_{\mathrm{PL}}(a,b,c)
$$

本身还依赖于当前组成状态

$$
(a,b,c).
$$

所以 finite $\alpha_A$ 的真正含义是：`memory 不只是把反应整体调快或调慢，而是把第一条反应改写成一个随系统状态共同变化的有效通量。`

所以这条近似第一次把“memory 会怎样改写反应项”写成了可以直接代入方程的解析形式。

这里的极限最好显式算一下，否则很容易误以为分子里有 $\alpha_A$，整个式子就会发散。实际上

$$
\Theta_{\mathrm{PL}}(a,b,c)
\simeq
\frac{\alpha_A\chi}{1+(\alpha_A-1)\chi}.
$$

把分母展开成

$$
1+(\alpha_A-1)\chi
=
\alpha_A\chi+(1-\chi),
$$

于是

$$
\Theta_{\mathrm{PL}}(a,b,c)
\simeq
\frac{\alpha_A\chi}{\alpha_A\chi+(1-\chi)}.
$$

现在就能直接看出：当

$$
\alpha_A\to\infty
$$

时，分子和分母的主导项都是

$$
\alpha_A\chi,
$$

常数项 $1-\chi$ 只是次主导修正，因此

$$
\Theta_{\mathrm{PL}}(a,b,c)\to
\frac{\alpha_A\chi}{\alpha_A\chi}
=1.
$$

也可以写成更标准的极限形式：把分子分母同时除以 $\alpha_A$，

$$
\Theta_{\mathrm{PL}}(a,b,c)
=
\frac{\chi}{\frac{1}{\alpha_A}+\left(1-\frac{1}{\alpha_A}\right)\chi}
\xrightarrow[\alpha_A\to\infty]{}
\frac{\chi}{\chi}
=1.
$$

所以这里趋于 1 的原因不是“$\alpha_A$ 消失了”，而是：`分子与分母以同阶速度增长，主导项相消，最后只剩 Markovian benchmark。`

第三，这条近似之所以关键，不是因为它“更好看”，而是因为它直接决定后面的 stationary condition 能不能真正解开。这里所谓 stationary condition，就是把 generalized rate equations 的右端同时设为 0，去解

$$
a^*,\qquad b^*,\qquad c^*.
$$

如果保留原始的 memory kernel [Eq. (12)]，这些方程里会混入 exponential integral，结构过于复杂，很难直接看出共存点怎样依赖 $\alpha_A$ 和 $k_A$。用这条近似替换之后，kernel 退化成了有理形式，stationary equations 也随之变成可处理的代数方程。

这样作者才能在

$$
k_A:k_B:k_C=k:1:1
$$

这个切片上显式解出新的共存点

$$
\{a^*,b^*,c^*\},
$$

并进一步从

$$
a^*=b^*=c^*=\frac13
$$

这个条件里抽出临界值

$$
k^*(\alpha_A).
$$

所以这条近似真正提供的信息不是“kernel 现在可计算了”这么空泛，而是：

`它把 memory 的影响具体传递成了两类显式结果：共存点的位置偏移，以及 LOW 分界线的位置偏移。`

第八步，在

$$
k_A:k_B:k_C=k:1:1
$$

这个最干净的切片上，作者得到新的共存点

$$
\{a^*,b^*,c^*\}
=
\frac{\{2(\alpha_A-1),\,2(\alpha_A-1),\,k(2\alpha_A-1)\}}
{4(\alpha_A-1)+k(2\alpha_A-1)}.
$$

这条式子比形式更重要的是它表达的事实：共存点的位置现在由 bare rate $k$ 和 waiting-time shape 参数 $\alpha_A$ 共同决定，而不再只由 bare rates 决定。

第九步，作者接着从这条式子里抽出一个最有解释力的量：临界值

$$
k^*(\alpha_A)\simeq 1-\frac{1}{2\alpha_A-1}.
$$

这条式子是这一小节最值得记住的结果之一。它告诉你：LOW 的分界线不再是经典 Markovian 的

$$
k=1,
$$

而是被 memory 推到了

$$
k=k^*(\alpha_A)<1.
$$

这里需要再往前展开一步。经典 Markovian zRPS 里，只要

$$
k<1,
$$

就意味着 $A$ 的 bare rate 最低，因此 $A$ 既是“最弱者”，也是 LOW 预测下最可能 fixation 的 species。但现在分界线已经从

$$
k=1
$$

移动到了

$$
k=k^*(\alpha_A)<1.
$$

因此会出现一个新的参数窗口：

$$
k^*(\alpha_A)<k<1.
$$

在这个窗口里，按 bare rate 排序看，$A$ 仍然是最弱者；但按真正的 non-Markovian dynamics 看，$A$ 已经不再处在“最可能 fixation”的那一侧。换句话说，memory 改变的不是 fixation probability 的细小数值，而是 LOW 本身的判别阈值。于是 bare-rate 意义上的“最弱者”这个标签，已经不再自动等于最终赢家。

第十步，作者最后把这个 equilibrium shift 和 fixation 结局连起来。只要 generalized equations 仍然产生围绕共存点的闭轨道，那么就可以沿用前面 Markovian 相空间的逻辑：看外层 orbit 更靠近哪条边，就推断哪个 species 更容易 fixation / extinction。于是，通过共存点的位置和临界值 $k^*(\alpha_A)$，作者就能预测 survival behavior 何时偏离 LOW。

### What To Retain From This Subsection

如果这一节只记 5 件事，就记下面这些：

1. power-law non-Markovianity 在 mean-field 层表现为一条带 `memory kernel` 的 generalized rate equation。
2. 被改写的不是整个系统，而是第一条反应项
   $$
   abk_A \to abk_A\Theta(a,b,c).
   $$
3. 这个 kernel 依赖整体状态，因此 memory 会把单条反应的有效强度和整条竞争环耦合起来。
4. 即使固定平均 waiting time 不变，共存点也会偏移，说明 distribution shape 本身就足以改写长期动力学。
5. 临界值
   $$
   k^*(\alpha_A)\simeq 1-\frac{1}{2\alpha_A-1}
   $$
   表明 LOW 的分界线被 memory 推动了；bare rate 上的“最弱者”不再自动等于最终最可能的幸存者。

## 11. II.E. Fixation Heatmaps For The Power-Law WTD

![Figure 4a: fixation heatmap when only the first reaction has a power-law WTD](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-05-figure-01.jpg)

![Figure 4b: fixation heatmap when all reactions have power-law WTDs, with $\alpha_B=\alpha_C=10$](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-05-figure-02.jpg)

![Figure 4c: fixation heatmap when all reactions have power-law WTDs, with $\alpha_B=\alpha_C=1.5$](../../pdfs/2026-04-13/non-markovian-rock-paper-scissors-games.mineru/hybrid_auto/images/page-05-figure-03.jpg)

这一小节的任务，是把前面关于 `threshold shift` 和 `equilibrium shift` 的分析，真正变成整个参数空间上的 survival phase diagram。前面几节已经说明：power-law waiting time 会移动共存点，也会把 LOW 的分界线从 $k=1$ 推到 $k=k^*(\alpha_A)$。heatmap 这一节要回答的是：`这些偏移在整个 $\alpha_A$-$k_A$ 平面上到底长什么样，最后谁真正赢？`

第一步，先读懂 heatmap 本身在画什么。图中的每个点都对应一组三元 fixation probability

$$
(\phi_A,\phi_B,\phi_C),
$$

横轴是第一条反应 waiting-time law 的 shape 参数

$$
\alpha_A,
$$

纵轴是第一条反应的 bare rate

$$
k_A.
$$

颜色采用 Figure 1(d) 的 RGB 编码：

- 红色表示 $A$ 主导；
- 绿色表示 $B$ 主导；
- 蓝色表示 $C$ 主导；
- 青色表示 $B$ 与 $C$ 共享较大 fixation probability，而 $A$ 基本不赢；
- 白色表示三者胜率接近，各约 $1/3$。

所以这组图不是在画轨道，也不是在画共存点，而是在画：`参数一变，最终哪一个 species 最可能成为唯一幸存者。`

第二步，作者先给出 Markovian benchmark 作参照。若三条反应都 obey 指数 WTD，且

$$
k_B=k_C=1,
$$

那么 LOW 的预测非常简单：

- 当 $k_A<1$ 时，$A$ 最弱，图上应该是红色；
- 当 $k_A>1$ 时，$A$ 不再最弱，$B$ 和 $C$ 分享主导权，图上应该是青色；
- 分界线就在
  $$
  k_A=1.
  $$

所以后面读 heatmap 时，最重要的问题就是：`真实边界还在 k_A=1 吗，还是已经被 memory 推走了？`

第三步，Figure 4(a) 给出的，是最纯净的 non-Markovian perturbation：只有第一条反应有 power-law WTD，其余两条仍保持指数时钟。这张图主要由两大片区域组成：

- 红区：
  $$
  \phi_A\approx 1,\qquad \phi_B\approx\phi_C\approx 0;
  $$
- 青区：
  $$
  \phi_A\approx 0,\qquad \phi_B\approx\phi_C\approx \frac12.
  $$

这说明 heatmap 仍然保留了一个“谁赢、谁不赢”的基本双相结构，但与 Markovian benchmark 不同的是，红区和青区之间的分界线不再固定在

$$
k_A=1,
$$

而是随 $\alpha_A$ 系统性移动。这正是前面

$$
k^*(\alpha_A)
$$

的图像版本：LOW 的分界线已经从一条常数线变成了一条由 waiting-time shape 控制的曲线。

第四步，Figure 4(a) 里最重要的新现象，是当

$$
\alpha_A\to 1
$$

时出现了一个额外的蓝色相。这是 LOW 完全没有预测到的区域，其含义是

$$
\phi_C\approx 1,\qquad \phi_A\approx\phi_B\approx 0.
$$

也就是说，在某些强 non-Markovian 条件下，最后几乎总是 species $C$ fixation。

第五步，这个蓝色相为什么会出现，是这一节最关键的机制解释。作者指出：当 $\alpha_A$ 接近 1 时，第一条反应的 power-law WTD 会让 median 远小于 mean。换句话说，虽然按平均 waiting time 看，这条反应未必显得特别快，但按典型事件看，

$$
A+B\to A+A
$$

往往发生得非常早。结果就是：

1. $A$ 会快速消耗 $B$；
2. $B$ 是 $C$ 的 predator；
3. 一旦 $B$ 被迅速削弱，$C$ 就几乎失去主要压制；
4. 最终 $C$ 反而被释放出来并完成 fixation。

所以蓝色相在物理上的意思是：`typical reaction time 与 mean reaction time 的强脱钩，会通过循环竞争链条把最终赢家从 A/B-C 对称结构，推到 C 独占。`

第六步，作者还把这个图像和前面的 generalized equations 对上了。随着

$$
\alpha_A\to 1,
$$

memory kernel 会变得很大，

$$
\Theta_{\mathrm{PL}}\gg 1,
$$

从而导致 generalized equations 预测

$$
c^*\to 1,\qquad a^*,b^*\to 0.
$$

所以 heatmap 里的蓝色相，不是孤立数值现象，而是在验证前面 mean-field memory-kernel 分析得到的 equilibrium shift。

第七步，Figure 4(b) 的作用不是给一个完全新故事，而是做稳健性检验。在这幅图里，三条反应都采用 power-law WTD，但作者取

$$
\alpha_B=\alpha_C=10,
$$

这意味着后两条反应已经很接近指数时钟。因此 Figure 4(b) 和 Figure 4(a) 的图像非常相似。它说明：`Figure 4(a)` 中看到的相图重排，确实主要由第一条反应的 non-Markovianity 控制，而不是某种偶然的数值实现细节。

第八步，Figure 4(c) 则进一步说明：如果另外两条反应也具有显著 non-Markovian timing，整个 survival phase diagram 还会被进一步重画。在这里作者取

$$
\alpha_B=\alpha_C=1.5,
$$

于是后两条反应也都比指数分布更宽、更不规则。结果是，红区和青区的分界被推到了

$$
k_A>1
$$

的区域。这意味着：即使按 bare rate 看 $A$ 已经不弱了，$A$ 仍可能 fixation。换句话说，`最终 survival diagram 不是由 bare rates 单独决定，而是由整条竞争环上所有反应的 waiting-time statistics 共同决定。`

### What To Retain From This Subsection

如果这一节只记 6 件事，就记下面这些：

1. fixation heatmap 画的是整个参数平面上
   $$
   (\phi_A,\phi_B,\phi_C)
   $$
   的主导结构，而不是单条轨迹。
2. Markovian benchmark 的分界线是
   $$
   k_A=1.
   $$
3. Figure 4(a) 证明这条分界线在 non-Markovian power-law 情况下会变成随 $\alpha_A$ 变化的曲线。
4. 当 $\alpha_A\to 1$ 时，会出现 LOW 没预测到的蓝色相，即 $C$ 几乎必然 fixation。
5. 这个蓝色相的机制是：A 的典型事件比均值暗示的更快，A 迅速消耗 B，从而间接释放了 C。
6. Figure 4(c) 进一步说明：如果整条竞争环上多条反应都带有 non-Markovian timing，整个 survival phase diagram 会被进一步重画。
