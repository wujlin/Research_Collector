---
title: "Generative Optimal Transport via Forward-Backward HJB Matching"
authors: "Haiqian Yang, Vishaal Krishnan, Sumit Sinha, L. Mahadevan"
venue: "arXiv (2026)"
date_read: "2026-04-16"
topics: ["最优传输", "HJB方程", "flow matching", "生成模型"]
---

# Generative Optimal Transport via Forward-Backward HJB Matching — 精读笔记

> **一句话总结**：本文将生成模型问题严格还原为随机最优控制（stochastic optimal control），通过建立前向-后向 HJB 方程的时间反转对偶（time-reversal duality），将难以求解的逆向控制问题转化为沿正向扩散轨迹的 Feynman-Kac 路径积分估计，从而在无需 score estimation 或逆向 SDE 模拟的情况下学习一个标量势函数（scalar potential）来驱动最优生成传输。

---

## 1. INTRODUCTION

### 1.1 这篇文章到底在问什么

原文开头先把问题放在一个很物理的框架里来看。它关心的不是“怎样从噪声采样到数据”这么一句常见的生成模型表述，而是一个更强的问题：

**如果一个随机系统会自然地从结构化状态弛豫到无序参考态，那么反过来把它从无序态推回结构化目标态时，最小做功的随机过程是什么？**

这里有三个关键词需要先钉住。

第一，作者把生成过程看成一个**受控随机动力学问题**。系统本身带扩散和涨落，所以轨迹不是确定的；但我们可以通过控制漂移，把概率质量从参考分布推向目标分布。

第二，作者强调的不是只有端点分布，而是**整条轨迹**。他们关心的不是“起点和终点对不对”，而是：在中间每一步，系统有没有走进高代价区域，控制做功是不是尽量小，整条路径是不是物理上合理。

第三，作者把这个问题同时放在两条传统里：

- 非平衡统计力学：系统自然弛豫到无序，逆转这个弛豫需要做功；
- 随机最优控制：在带噪动力学里，怎样以最小总代价把分布从起点运到终点。

所以这篇文章的起点，不是“再做一个生成模型”，而是：

**生成本身就是一个受控的概率输运问题，而最自然的问题是寻找最优输运路径。**

### 1.2 为什么作者觉得现有生成方法还不够

接下来文章不是简单回顾文献，而是把现有方法按“它们到底优化了什么”重新摆了一遍。

第一类是 score-based / score-matching 路线。它们擅长做的是：学习一个逆向漂移场，让系统能够从噪声逐步回到数据分布。但作者这里的批评不是说这条路不行，而是说：它主要是在学习**局部逆向向量场**，并没有把“整条轨迹的全局代价最小”直接写进目标。

第二类是 flow matching。它做的是：先指定一条随时间变化的中间分布路径，然后学习一个速度场，使得系统在每一个时间切片上都能把样本推到对应的那一层分布。它主要检查的是：

- 在时间 $t$，样本分布是不是到了应该到的位置；
- 在时间 $t+\Delta t$，分布是不是又被推到了下一层目标边际。

所以它的监督对象首先是**每个时间切片上的边际分布**，而不是整条随机轨迹的总代价。这也是为什么它在分布层面看起来很干净：你不需要先处理整条路径的全局 action，也不需要显式追踪某条路径累计付出了多少代价；只要让每个时间片上的样本流向正确的目标边际，训练就能成立。

也正因为这样，它通常比直接解完整的随机最优控制问题更容易训练。你学的是“这一时刻局部应该往哪里流”，而不是“一整条连续时间轨迹怎样同时兼顾做功最小、空间约束最小和终点匹配”。所以在作者看来，flow matching 虽然在分布演化层面很自然，但它优化的仍然是“各个时刻的局部输运方向”，而不是“整条随机路径的动作代价和空间代价如何同时最优”。

第三类是 Schrödinger bridge。它已经比前两类更接近作者想要的东西，因为它确实在做带噪的分布输运，也和随机控制、最优传输、路径测度联系很深。原文这里进一步区分的是问题的起点。

Schrödinger bridge 的标准起点通常是：给定起点分布和终点分布，在所有能把前者送到后者的随机路径测度里，寻找那个**相对于某个参考扩散过程最不意外、也就是 KL 代价最小**的过程。这样一来，问题的主角首先是：

- 起点和终点这两个边界分布；
- 以及在这两个端点约束下，整条路径测度相对参考过程的熵正则化代价。

所以从这个视角看，Schrödinger bridge 关心的是：**在满足端点约束的前提下，哪条随机输运路径最接近一个给定的自然参考过程。**

而这篇文章想把问题写得更原始一些。它不是先从“相对某个参考过程的 KL 最小”出发，再把这个量解释成一种路径代价；它是从第一行就直接写下连续时间轨迹上的 running cost：

- 经过高代价区域要付出多少空间代价；
- 施加控制要付出多少做功代价；
- 这两类代价沿整条轨迹如何累积。

在这篇文章里，主角首先不是“相对参考过程的熵正则化偏离”，而是：

**整条连续时间轨迹本身到底花了多少代价。**

所以两者的差别不是谁更高级，而是问题起点不同：

- Schrödinger bridge 更自然地从**端点约束 + 相对熵正则化**出发；
- 这篇文章更自然地从**连续时间随机最优控制的路径代价泛函**出发。

作者想强调的是：如果你的核心关切是“最小做功”和“路径几何可行性”，那么把连续时间 running cost 直接放在原始问题里，会比事后再从熵正则化角度去解释更直接。

作者觉得“不够”的地方，不是这些方法不能生成样本，而是：

- 它们不一定显式优化一条连续时间路径上的总代价；
- 它们不一定显式纳入空间约束或几何代价；
- 它们不一定把“最小做功”当成问题本身的中心。

**现有方法大多在学“如何把分布搬过去”，而作者想问的是“如何以最小轨迹代价把分布搬过去”。**

### 1.3 作者把这个问题写成了什么数学对象

在这个目标下，原文引入的不是离散时间生成链，而是一个受控 Itô 随机微分方程：

$$
d\mathbf{x}_t = \mathbf{u}_t\,dt + \sqrt{2D}\,d\mathbf{B}_t.
$$

这里：

- $\mathbf{x}_t$ 是系统状态；
- $\mathbf{u}_t$ 是控制输入；
- $D$ 是扩散系数；
- $\mathbf{B}_t$ 是 Brownian motion。

边界条件是：

- 初始分布来自无序参考态 $p_{\mathrm{ref}}$；
- 终点分布要到达结构化目标态 $p_{\mathrm{data}}$。

然后作者给这个受控过程配上了一个路径代价泛函：

$$
\min_{\mathbf{u}_t}\;
\mathbb E_{\mathbb P_{\mathbf u}}
\left[
\int_0^1 \nu(\mathbf{x}_t)\,dt
+
\frac{\gamma}{2}\int_0^1 \|\mathbf{u}_t\|^2\,dt
\right].
$$

这两项必须分开理解。

第一项 $\int_0^1 \nu(\mathbf{x}_t)\,dt$ 是**空间代价**。它说的是：某些区域物理上不合理、工程上不安全、或者几何上不希望经过，那么轨迹经过那里就要付出代价。

第二项 $\frac{\gamma}{2}\int_0^1 \|\mathbf{u}_t\|^2\,dt$ 是**控制做功代价**。它说的是：想把系统从自然弛豫方向硬拉回目标态，需要施加控制；控制越大，代价越高。

这个数学问题的含义是：

**在满足起点和终点分布约束的前提下，找到一条随机控制策略，使系统既少做功，又尽量避开高代价区域。**

这也是这篇文章和普通“把噪声变成样本”的生成表述最不一样的地方。这里从第一行开始，主角就是**路径最优性**，不是只看最终样本。

### 1.4 这篇文章的核心想法是什么

到这里，原文开始引入本文的新意。它没有直接去学习一个高维向量场，也没有直接在 backward process 上做 hard control，而是先把原始控制问题改写成它的对偶形式。线索分成三步。

为避免混用两套时间坐标，下面先固定一个说法：把目标数据分布所在的一端统一叫作**数据端**，把参考分布所在的一端统一叫作**参考端**。在 backward 时钟 $t\in[0,1]$ 里，系统从参考端走到数据端；在 forward 时钟 $s=1-t$ 里，系统从数据端走回参考端。

第一步，原始问题表面上是在所有可能的控制策略 $\mathbf{u}_t$ 里做最优化。也就是说，你直接操纵的对象看起来是一个随时间和空间变化的向量场：在每个时刻、每个位置，到底要把系统往哪个方向推。

第二步，这里说的“对偶形式”，不是另一个无关的新问题，而是**把同一个最优控制问题换一种变量来写**。原始写法里，你要同时处理两样东西：

- 控制场 $\mathbf{u}_t$；
- 在这个控制下随时间演化的概率密度 $\rho(t,\mathbf{x})$。

而且这两样东西还不能随便选，它们必须一起满足 Fokker-Planck 方程，也就是“控制怎么推着整团概率质量往前走”的动力学约束。直接在这两个对象上同时做优化，会很笨重。

对偶化做的事情是：引入一个标量函数 $U(t,\mathbf{x})$ 作为 Lagrange 乘子，把 Fokker-Planck 约束先乘上这个函数，再和原始路径代价一起写进同一个积分里。这样一来，动力学约束就不再是“额外写在旁边、必须另外满足的一条方程”，而是直接变成优化目标的一部分。于是原来那个“同时优化控制场和概率密度、并且还要单独检查它们是否满足动力学约束”的问题，就可以改写成一个更统一的变分问题。再往下对控制场做极小化之后，主角就从“任意向量控制场”变成了一个标量 value function。这个标量函数记录的是：**如果系统此刻位于 $(t,\mathbf{x})$，那么从现在到数据端，完成整个输运任务所需的最小剩余代价是多少。**

这里要特别分清 past 和 future 在这个函数里的角色。原始路径代价当然是沿整条轨迹累计的，但一旦走到当前时刻 $t$，更早那段路径上已经付出的代价就变成了既定常数，不会再被当前控制改变；真正还会被当前决策影响的，只剩从现在到数据端这段 future cost。也就是说，当前控制不是回头去重算过去，而是在利用 $U(t,\mathbf{x})$ 这种 `cost-to-go` 对象，把“从这一点往后最少还要付出多少代价”压缩进当前决策里。

第三步，一旦把问题写成这种对偶形式，控制场就不再需要被单独学习了。这里的 HJB 是 **Hamilton-Jacobi-Bellman** 的缩写，它描述的是：如果系统现在位于某个状态，那么从现在到数据端的最小剩余代价满足什么偏微分方程。这个理论里最核心的对象就是 value function，也就是上面说的“最小剩余代价函数”。

原始代价里，控制 $\mathbf{u}_t$ 一方面要付出二次做功代价，另一方面又会通过 $\mathbf{u}\cdot \nabla U$ 这一项影响 value function 的变化。于是，对控制变量做极小化时，你实际上是在每个时空点上最小化一个标准的凸二次函数：

$$
\frac{\gamma}{2}\|\mathbf{u}\|^2+\mathbf{u}\cdot \nabla U.
$$

对这个二次函数求极小值，一阶条件是
$$
\gamma\,\mathbf{u}+\nabla U=0,
$$
于是最优控制自然写成

$$
\mathbf{u}^*(t,\mathbf{x})=-\frac{1}{\gamma}\nabla U(t,\mathbf{x}).
$$

需要学习的不是一个任意的向量函数，而是一个标量势 $W(t,\mathbf{x})$，再由它的梯度来定义最优控制方向。

这样做有两个立刻的好处。

第一，表示更紧。高维向量场学习被压成了标量势学习，结构更清楚，也更接近最优控制和 Hamilton-Jacobi-Bellman 理论的经典形式。

第二，物理意义更强。因为一旦最优控制是某个势函数的梯度，整个生成过程就不再只是“一个学出来的 drift”，而更像“沿着 value landscape 做最优输运”。

但这里马上会出现作者自己强调的难点。下面分成三步。

第一步，backward problem 对应的正是我们真正想要的生成过程：从参考分布出发，在控制下逐步走到目标分布。表面上看，这正是应该直接求解的方向。

第二步，一旦你真的沿这个方向往下写，很多关键量都会开始依赖“在最优控制下，系统实际会经过哪些轨迹”。例如，你想计算某个值函数的期望、想评估某个路径代价，或者想知道某个控制是否真的把概率质量送到了目标分布附近，这些问题最后都会要求你已经能够从那个 backward controlled process 里采样。

第三步，问题恰好卡在这里：这个 backward controlled process 本身正是你还没有求出来的对象。你想评估它，需要先能运行它；但你想运行它，又得先知道它。这就形成了一个闭环：

- 为了算最优 backward control，你需要知道最优轨迹长什么样；
- 为了知道最优轨迹长什么样，你又需要先有最优 backward control。

这就是这里说的“循环依赖”。后面要解决的，不是一个普通数值难题，而是这个结构性的闭环。

### 1.5 作者如何打破这个循环依赖

这正是原文 introduction 最后要引出的核心机制：

**把难解的 backward optimal control 问题，通过时间反转对偶，改写成一个 forward-in-time 的 HJB 问题。**

下面按四步展开。

第一步，真正的生成任务发生在 backward 方向。系统从参考分布出发，在控制作用下逐步走向目标数据分布；这正是我们最终想运行的过程。

第二步，困难也恰好出在这个方向上。因为 backward controlled process 还没有被构造出来，所以你既不知道它的典型轨迹长什么样，也不能直接从它采样。这样一来，凡是依赖“沿最优生成轨迹求期望”的量，都会立刻卡住。

第三步，forward 方向则不同。作者把时间反过来看：如果系统从数据分布出发，往参考分布弛豫，那么这就是一个自然扩散过程。这个过程不需要额外猜测最优控制，也不需要先知道目标轨迹；它本身就是可模拟、可采样、可在路径上做 Monte Carlo 平均的对象。

第四步，时间反转对偶的作用，不只是“把 forward 解拿回 backward 用”，而是把**同一个控制问题放到两个不同时间坐标下重读**。下面分三层。

第一层，backward value function $U(t,\mathbf{x})$ 记录的是：如果系统在反向生成时刻位于 $(t,\mathbf{x})$，那么从现在到数据端还要付出多少最小剩余代价。它天然是一个“朝数据端看”的量。

第二层，如果把时间改写成 $s=1-t$，再定义一个新的标量函数 $W(s,\mathbf{x})=-U(1-s,\mathbf{x})$，那么你并没有换掉问题本身，只是把同一族时空点改用 forward 时钟来标记。这样一来，原来那个“从参考分布往数据分布推”的 backward control 问题，就被重新表述成一个 forward HJB 问题。

这里不是又发明了一个新目标，而是把同一个“最小剩余代价”函数，改写成了 forward 时间下满足的偏微分方程。第一，先固定当前 forward 时刻 $s$ 和当前位置 $\mathbf{x}$。第二，从这一刻开始，系统会继续沿着 forward 弛豫往前走，直到到达 $s=1$，也就是参考端。第三，在这段剩余时间里，轨迹会继续累积空间代价和控制代价；不同的后续走法，会对应不同的总代价。第四，$W(s,\mathbf{x})$ 记录的就是：在所有允许的后续演化里，从当前这点出发、一直走到参考端为止，最少还需要付出多少总代价。因为这个 forward 方向本身对应自然扩散，所以这个 forward HJB 约束的是一个可以沿真实前向轨迹去估计的 value function，而不是一个必须先知道生成过程才能评估的对象。

第三层，这样做之所以有用，是因为 forward 方向本身是可采样的。你可以真的从数据分布出发，沿着弛豫过程模拟轨迹，并在这些轨迹上估计 forward value function $W$。而一旦 $W$ 学到了，backward control 又只依赖它的梯度；于是再通过时间反转关系和后面的 Anderson-type reverse formula，就能把 $W$ 重新翻译回生成时需要的 backward drift。

所以作者的策略不是“直接学逆过程”，而是：

1. 先构造从数据到参考的 forward relaxation；
2. 在这个 forward 过程中学习标量 value function；
3. 再通过时间反转对偶，把这个 value function 变回生成时需要的 backward control。

接下来会用到：

- HJB 方程；
- Cole-Hopf 变换；
- Feynman-Kac 表示；
- path-space free energy。

但 introduction 在这里已经把整篇文章的主线交代清楚了：

**训练时走正向、生成时走反向；正向之所以可学，是因为它是自然弛豫；反向之所以可得，是因为前后两个 HJB 通过时间反转对偶联系起来。**

### 1.6 原文在引言里想 claim 的贡献

如果把 introduction 收成作者自己的 claim，大致就是四点。

第一，他们不是从 score 或 drift 回归出发，而是从**随机最优控制 + 动态最优传输**出发，给生成问题一个更物理、更变分的起点。

第二，他们提出了一个**前向-后向 HJB 对偶**。这让 backward control 的学习可以转移到 tractable 的 forward trajectories 上完成。

第三，他们引入了显式的**空间代价函数** $\nu(\mathbf{x})$。这意味着生成路径不只受端点约束，还会被中间路径的几何和可行性塑形；原文甚至用类似 Fermat 原理的语言去解释这种“折射式”输运几何。

第四，他们把整个框架解释成一种**path-space free energy** 视角下的生成建模。这篇文章不是单纯想做更好的 sampler，而是想把：

- stochastic control
- optimal transport
- Schrödinger bridge
- non-equilibrium statistical mechanics

放进同一个解释框架里。

---

## 2. FORWARD-BACKWARD HJB MATCHING

### 2.1 原文这一节的线性顺序

原文 `Section 2` 的顺序很清楚，下面按这条线展开：

1. 先重新写出受控 SDE 和随机控制目标，也就是 `Eq. (1)` 和 `Eq. (2)`；  
2. 再给出 `Lemma 2.1`，把问题从“控制场优化”改写成“标量势函数满足的 HJB 对偶问题”；  
3. 然后指出：如果直接从这个 backward generative formulation 往下做，会遇到循环依赖；  
4. 再给出 `Theorem 2.2`，把 backward problem 改写成 forward-time 的 HJB matching；  
5. 最后才进入 `b. Feynman-Kac estimation of the forward potential`，解释为什么 forward value function 可以沿可采样的正向轨迹估计。

下面的整理就严格按这个顺序走，不再把 `Lemma 2.1`、`Theorem 2.2`、`Feynman-Kac` 拆到几个互相断开的大节里。

### 2.2 a. 从受控 SDE 到随机控制问题

原文这一节开头先把生成问题重新写回受控 SDE：

原文 Eq. (1)：

$$
d\mathbf{x}_t = \mathbf{u}_t\,dt + \sqrt{2D}\,d\mathbf{B}_t.
$$

边界条件是：

- 起点在参考端，$\mathbf{x}_0 \sim p_{\mathrm{ref}}$；
- 终点在数据端，$\mathbf{x}_1 \sim p_{\mathrm{data}}$。

然后作者把真正要解的随机控制问题写成

原文 Eq. (2)：

$$
\min_{\mathbf{u}_t}\;
\mathbb E_{\mathbb P_{\mathbf u}}
\left[
\int_0^1 \nu(\mathbf{x}_t)\,dt
+
\frac{\gamma}{2}\int_0^1 \|\mathbf{u}_t\|^2\,dt
\right].
$$

原文先把问题重新钉死为“在固定端点分布约束下，最小化整条随机轨迹上的空间代价和控制做功代价”。

为什么要这么做？因为直接学习控制场有两个困难。

1. 控制场 $\mathbf{u}(t,\mathbf{x})$ 本身是定义在“时间 $\times$ 状态空间”上的高维向量函数。  
   这意味着：对每一个时刻、每一个位置，你都要决定一个完整的推动方向。  
   所以如果直接把它当成主角去学习，模型表面上要拟合的是一整张随时间变化的向量场，而不是一个更紧凑的标量对象。  
   这就是“重”的意思：参数化对象本身维度高、结构复杂。  
   这也是“不透明”的意思：即使学到了一个控制场，你也很难直接读出“为什么这里要往这个方向推、它对应的剩余任务代价是什么”。  
2. 控制场和概率密度 $\rho(t,\mathbf{x})$ 不是分开选的；它们必须一起满足动力学约束。

这里的动力学约束就是 Fokker-Planck 方程：

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\mathbf{u}\rho) = D\Delta\rho.
$$

这条方程的意思是：如果你给系统施加某个控制场 $\mathbf{u}$，那么整团概率质量 $\rho(t,\mathbf{x})$ 会按这条连续性方程演化。原始最优控制问题不是“只优化控制”，而是：

- 一边优化路径代价；
- 一边要求密度演化始终 obey 这条 Fokker-Planck 约束。

作者这一节要做的，就是把这个“控制场 + 概率密度 + 动力学约束”的问题，改写成一个以标量势函数为主角的对偶问题。

### 2.3 Lemma 2.1 的主线：为什么会冒出一个标量函数

这里的关键动作只有一个：引入一个标量函数 $U(t,\mathbf{x})$ 作为 Lagrange 乘子，把 Fokker-Planck 约束写进同一个优化泛函里。

这里的直觉是：

- 原来 Fokker-Planck 是一个必须额外满足的条件；
- 现在用 $U(t,\mathbf{x})$ 去乘这条约束；
- 再把它和原始路径代价放进同一个积分；
- 于是“代价最小”和“动力学必须成立”就被放进了同一个变分问题里。

对应的 Lagrangian 写成：

$$
\mathcal{L}[\mathbf{u}, \rho, U]
=
\int_0^1\!\!\int
\left[
\nu(\mathbf{x})+\frac{\gamma}{2}\|\mathbf{u}\|^2
\right]\rho\,d\mathbf{x}\,dt
\;+\;
\int_0^1\!\!\int
U
\left[
\frac{\partial \rho}{\partial t}
+\nabla\cdot(\mathbf{u}\rho)
-D\Delta \rho
\right]
d\mathbf{x}\,dt.
$$

到这里为止，$U$ 还只是一个乘子函数。它的作用只是：把“密度必须满足 Fokker-Planck”这件事显式写进优化目标。

#### 2.3.1 变分三步：从 Lagrangian 到最优控制

下面按原文的三步展开 Lemma 2.1。

第一步，先处理乘子项里那三类带导数的部分：时间导数项、散度项和 Laplace 项。原文一句话说“做分部积分，把导数从 $\rho$ 转到 $U$ 上”，中间具体是下面三步。

1. 对时间导数项
   $$
   \int_0^1\!\!\int U\,\frac{\partial \rho}{\partial t}\,d\mathbf{x}\,dt
   $$
   做时间方向的分部积分。这样会留下两个边界项，同时把时间导数从 $\rho$ 挪到 $U$ 上：
   $$
   \int U(1,\mathbf{x})\rho_1(\mathbf{x})\,d\mathbf{x}
   -
   \int U(0,\mathbf{x})\rho_0(\mathbf{x})\,d\mathbf{x}
   -
   \int_0^1\!\!\int \rho\,\frac{\partial U}{\partial t}\,d\mathbf{x}\,dt.
   $$

2. 对散度项
   $$
   \int_0^1\!\!\int U\,\nabla\cdot(\mathbf{u}\rho)\,d\mathbf{x}\,dt
   $$
   做空间分部积分。忽略无穷远处的边界通量以后，散度从 $\mathbf{u}\rho$ 挪到 $U$ 上，于是得到
   $$
   -\int_0^1\!\!\int \rho\,\mathbf{u}\cdot \nabla U\,d\mathbf{x}\,dt.
   $$

3. 对扩散项
   $$
   -D\int_0^1\!\!\int U\,\Delta \rho\,d\mathbf{x}\,dt
   $$
   做两次空间分部积分。结果等价于把 Laplacian 从 $\rho$ 挪到 $U$ 上，所以得到
   $$
   -D\int_0^1\!\!\int \rho\,\Delta U\,d\mathbf{x}\,dt.
   $$

把这三部分和原来的代价项重新合并，就得到：

$$
\mathcal{L}
=
\int U(0,\mathbf{x})\rho_0\,d\mathbf{x}
-\int U(1,\mathbf{x})\rho_1\,d\mathbf{x}
+\int_0^1\!\!\int
\left[
\nu
+\frac{\gamma}{2}\|\mathbf{u}\|^2
-\frac{\partial U}{\partial t}
-D\Delta U
+\mathbf{u}\cdot \nabla U
\right]\rho\,d\mathbf{x}\,dt.
$$

这里发生的结构变化是：

- 边界项里出现了 $U(0,\mathbf{x})$ 和 $U(1,\mathbf{x})$；
- 积分内部关于控制 $\mathbf{u}$ 的部分，已经只剩一个标准的凸二次函数。

第二步，对控制变量 $\mathbf{u}$ 做逐点极小化。固定某个时空点 $(t,\mathbf{x})$ 以后，需要最小化的是

$$
\frac{\gamma}{2}\|\mathbf{u}\|^2 + \mathbf{u}\cdot \nabla U.
$$

这就是一个非常标准的凸二次函数。对 $\mathbf{u}$ 求一阶条件：

$$
\gamma\,\mathbf{u}+\nabla U=0,
$$

于是得到逐点最优控制：

$$
\mathbf{u}^*(t,\mathbf{x})=-\frac{1}{\gamma}\nabla U(t,\mathbf{x}).
$$

这里给出整节最重要的结论之一：**最优控制不是一个需要单独学习的任意向量场，而是某个标量函数的空间梯度。**

第三步，把这个最优控制代回去。代回以后，二次项会化简成

$$
\frac{\gamma}{2}\|\mathbf{u}^*\|^2+\mathbf{u}^*\cdot\nabla U
=
-\frac{1}{2\gamma}\|\nabla U\|^2.
$$

于是被积函数内部只剩下

$$
\nu
-\frac{\partial U}{\partial t}
-D\Delta U
-\frac{1}{2\gamma}\|\nabla U\|^2.
$$

代回之后，Lagrangian 内部的时空积分变成

$$
\int_0^1\!\!\int
\left[
\nu
-\frac{\partial U}{\partial t}
-D\Delta U
-\frac{1}{2\gamma}\|\nabla U\|^2
\right]\rho\,d\mathbf{x}\,dt.
$$

现在关键点是：$\rho(t,\mathbf{x})$ 还不是一个已经固定好的函数；在对偶问题里，它仍然是一个非负密度。更准确地说，改变 $\rho$，就等于改变“哪些时空区域分到更多概率权重、哪些区域分到更少概率权重”。

于是就会出现下面这个判断：

1. 如果方括号里的系数在某些地方为负，那么优化会倾向于把更多概率质量堆到那些地方，从而继续压低目标值；  
2. 如果它在某些地方为正，那么那些地方会抬高代价；  
3. 真正稳定的最优点，不能依赖“把概率质量偷偷搬去某些局部区域”来继续改进目标。  

所以在最优解上，这个乘在 $\rho$ 前面的局部系数不能留下可被继续利用的空间方向；它必须在每个时空点都被钉死。也就是要求

$$
\nu
-\frac{\partial U}{\partial t}
-D\Delta U
-\frac{1}{2\gamma}\|\nabla U\|^2
=
0.
$$

这里的“整理”其实只做了一步移项：把时间导数项、扩散项和梯度平方项都移到左边，把即时空间代价 $\nu(\mathbf{x})$ 也并到同一边，于是局部系数为零这件事就被改写成标准的 HJB 形式：

$$
\frac{\partial U}{\partial t}
+D\Delta U
-\frac{1}{2\gamma}\|\nabla U\|^2
+\nu(\mathbf{x})
=0.
$$

这条方程之所以叫 HJB，不是因为它“看起来像某种标准公式”，而是因为这里的 $U(t,\mathbf{x})$ 本身就是一个 value function：它记录的是，如果系统现在位于 $(t,\mathbf{x})$，那么从现在到数据端还剩多少最小总代价。

一旦主角是“最小剩余代价函数”，问题就自动带上了 Bellman 的动态规划结构：从现在到终点的最优总代价，应该等于“先走一个极短时间步所付出的即时成本”加上“后面那段路径的最优剩余代价”。把这个连续时间极限写成偏微分方程，得到的正是 Hamilton-Jacobi-Bellman equation。

所以这条式子里的各项都不是随便拼起来的：

- $\partial_t U$ 描述 value function 随时间推进的变化；
- $D\Delta U$ 来自扩散噪声；
- $-\frac{1}{2\gamma}\|\nabla U\|^2$ 来自对控制做极小化后得到的 Hamiltonian 项；
- $\nu(\mathbf{x})$ 是当前位置的即时运行代价。

这条方程表达的是：**最优控制下的最小剩余代价函数必须满足的局部平衡关系。**

#### 2.3.2 Lemma 2.1 得到了什么

到这里，这一节得到三件事。

第一，最优控制可以写成

$$
\mathbf{u}^*(t,\mathbf{x})=-\frac{1}{\gamma}\nabla U(t,\mathbf{x}).
$$

第二，控制问题不再只看成“在所有向量场里找一个最优 $\mathbf{u}$”，而是改写成“寻找一个满足 HJB 方程的标量函数 $U$”。

第三，对偶目标里留下的是边界项：

原文 Eq. (3) 的目标部分：

$$
\max_{U_0,U_1}
\left\{
\int U(0,\mathbf{x})\,p_{\text{ref}}(\mathbf{x})\,d\mathbf{x}
-\int U(1,\mathbf{x})\,p_{\text{data}}(\mathbf{x})\,d\mathbf{x}
\right\}.
$$

这一步按顺序读。

1. 原来的时空积分部分，在最优解上已经被 HJB 方程逐点消掉了；  
2. 所以整个对偶目标里最后留下的，不再是“沿整条路径累计的代价”，而是两个端点上的边界项；  
3. 第一项
   $$
   \int U(0,\mathbf{x})\,p_{\text{ref}}(\mathbf{x})\,d\mathbf{x}
   $$
   表示：在参考端的初始分布上，对 value function 的起点值做平均；  
4. 第二项
   $$
   \int U(1,\mathbf{x})\,p_{\text{data}}(\mathbf{x})\,d\mathbf{x}
   $$
   表示：在数据端的终点分布上，对 value function 的终点值做平均；  
5. 两者相减的含义是：在所有满足 HJB 约束的候选标量函数里，找一个最能区分“参考端”和“数据端”代价差异的势函数。

所以这里的对偶目标不是又加了一个新的训练损失，而是在说：**一旦内部时空代价已经通过 HJB 被编码进 $U$，最终优化只需要比较这个势函数在两端分布上的平均值。**

而同一个原文 Eq. (3) 还要求 $U$ 同时满足上面那条 HJB 约束。

所以“对偶变分原理：从控制到标量势”这句话，现在可以读成更具体的版本：

- 原问题的主角本来是控制场 $\mathbf{u}$；
- 做完对偶化以后，主角变成了标量 value function $U$；
- 而控制场只是它的梯度结果。

### 2.4 为什么 direct generative formulation 还不可算

到这里虽然已经把问题从“控制场学习”改写成了“标量势学习”，但困难还没有消失。

原因是：这个对偶目标最终仍然要在数据端和参考端的分布上取期望。尤其是涉及数据端的那些量，本质上仍然和“最优 backward 生成过程到底会经过哪些轨迹”绑在一起。

这就带来下一步的核心困难：如果你直接从 backward problem 出发，很多你想算的量都会依赖一个你还没构造出来的最优生成过程。问题结构本身带着循环依赖。

这正是下一节要解决的事。

### 2.5 Theorem 2.2 — 前向-后向 HJB 对偶

这是本文的核心定理。定义正向势函数 $W(s, \mathbf{x}) := -U(1-s, \mathbf{x})$，即对逆向势函数做时间反转和取负。则：

**(1) 正向 HJB 方程**：

原文 Eq. (4)：

$$
\frac{\partial W}{\partial s} - D\Delta W - \frac{1}{2\gamma}\|\nabla W\|^2 + \nu(\mathbf{x}) = 0
$$

注意与逆向 HJB 的区别：扩散项 $D\Delta W$ 的符号反转了——从"逆向抛物"变为"正向抛物"。

**(2) 正向传输过程**：受控 SDE

$$d\mathbf{y}_s = \mathbf{v}^*(s, \mathbf{y}_s) \, ds + \sqrt{2D} \, d\mathbf{B}_s, \quad \mathbf{y}_0 \sim p_{\text{data}}$$

其中 $\mathbf{v}^*$ 的完整形式为 $\mathbf{v}^* = -\frac{1}{\gamma}\nabla W + 2D\nabla \log q$，它将 $p_{\text{data}}$ 传输到 $p_{\text{ref}}$。下面详细推导 $\mathbf{v}^*$ 中各项的来源。

**Step 1 — 时间反转 SDE 的标准形式（Anderson, 1982）**。设正向过程 $d\mathbf{x}_t = \mathbf{b}(t,\mathbf{x}_t)\,dt + \sqrt{2D}\,d\mathbf{B}_t$，其边际密度为 $\rho(t,\cdot)$。Anderson 定理指出，定义逆向时间 $s = 1 - t$，则逆向过程满足：

$$d\mathbf{x}_s = \left[-\mathbf{b}(1-s,\mathbf{x}_s) + 2D\nabla\log\rho(1-s,\mathbf{x}_s)\right]ds + \sqrt{2D}\,d\tilde{\mathbf{B}}_s$$

其中 $\tilde{\mathbf{B}}_s$ 是逆向 Brownian motion。关键观察：时间反转除了翻转漂移 $\mathbf{b}$ 的符号外，还额外引入了一个 **score 修正项** $2D\nabla\log\rho$——这正是 $\nabla\log q$ 项的物理来源。

**Step 2 — 定义正向势函数并代入**。原始逆向过程（生成过程）的最优漂移为 $\mathbf{u}^*(t,\mathbf{x}) = -\frac{1}{\gamma}\nabla U(t,\mathbf{x})$。对该受控 SDE 做 Anderson 时间反转（$s = 1-t$），正向漂移为：

$$\mathbf{v}^*(s,\mathbf{x}) = -\mathbf{u}^*(1-s,\mathbf{x}) + 2D\nabla\log q(s,\mathbf{x})$$

其中 $q(s,\mathbf{x})$ 是正向过程的边际密度。代入 $\mathbf{u}^* = -\frac{1}{\gamma}\nabla U$：

$$\mathbf{v}^*(s,\mathbf{x}) = \frac{1}{\gamma}\nabla U(1-s,\mathbf{x}) + 2D\nabla\log q(s,\mathbf{x})$$

**Step 3 — 利用 $W$ 的定义化简**。由 $W(s,\mathbf{x}) := -U(1-s,\mathbf{x})$，得 $\nabla U(1-s,\mathbf{x}) = -\nabla W(s,\mathbf{x})$，代入上式：

$$\boxed{\mathbf{v}^*(s,\mathbf{x}) = -\frac{1}{\gamma}\nabla W(s,\mathbf{x}) + 2D\nabla\log q(s,\mathbf{x})}$$

至此 $\mathbf{v}^*$ 的两项来源完全明确。

**(3) 最优性**：$\mathbf{v}^*$ 不是一个随手写出来的 forward 漂移场，而是正向问题里的最优控制。

这里的意思需要按三步读：

1. 现在我们已经把原来的 backward generative problem 改写成了一个 forward-in-time 的控制问题；  
2. 在这个 forward 问题里，系统从数据端出发，沿着可采样的弛豫方向走向参考端，同时也要支付同一类空间代价和控制做功代价；  
3. Theorem 2.2 说的“最优性”就是：在所有可能的 forward 控制场里，$\mathbf{v}^*$ 恰好是那个让这条正向控制代价泛函达到最小的解。

所以这里不是又额外定义了一个和 backward 无关的新优化问题，而是在说：

- backward 一侧决定我们想要的生成过程；
- 但由于时间反转对偶，同一个最优传输任务也可以在 forward 一侧被等价地重写；
- 而 $\mathbf{v}^*$ 正是这个等价 forward 问题里的最优控制。

一旦你能在 forward 方向上求出这个最优控制，就等于间接求到了原来难以直接处理的 backward 生成控制。

#### 2.5.1 控制场的双重分解

最优正向控制场分解为两个具有清晰物理角色的分量：

- $-\frac{1}{\gamma}\nabla W$：**目标导向分量**（value function gradient），沿累积代价下降方向驱动传输——直接继承自逆向最优控制 $\mathbf{u}^*$ 的时间翻转
- $2D\nabla \log q$：**密度感知修正**（score correction），由 Anderson 时间反转公式自然产生，确保正向过程的漂移与 Fokker-Planck 演化的一致性

这一点分三层。

1. 第一项 $-\frac{1}{\gamma}\nabla W$ 当然直接来自 $W$ 的梯度，这一点是显式的。  
2. 第二项 $2D\nabla \log q$ 表面上看像是另一个独立对象，因为它依赖正向边际密度 $q(s,\mathbf{x})$。  
3. 但在这篇框架里，$q$ 不是额外假设的一份外部密度，也不是再单独训练一个 score network 去拟合出来的；它就是由同一个 forward 最优控制问题所诱导出来的边际密度。换句话说，一旦 $W$ 确定，正向 HJB、对应的 forward 过程以及它的边际演化就一起被钉死了，$\nabla \log q$ 只是这个同一最优传输结构里随之出现的密度梯度项。

所以这里“无需独立估计 score”的意思不是说 score 项消失了，而是说：

- 你不需要像 score-based diffusion 那样，再额外训练一个专门输出 $\nabla \log q$ 的模型；  
- 在这篇方法里，需要学习的主角只有标量势 $W$；  
- score correction 是从同一个 forward controlled process 里伴随出现的，而不是一套独立参数化对象。

#### 2.5.2 Figure 1：为什么这一步能把训练和生成接起来

Figure 1 按图里的箭头顺序来读。

第一步，看图的上半部分。这里画的是我们想要的 **controlled generative process**：从右边的参考端 $p_{\text{ref}}$ 出发，在控制作用下走到左边的数据端 $p_{\text{data}}$。这对应的就是原来的 backward generation 目标，也是文章一开始写下的随机最优控制问题。

第二步，看图右上角的黑框。作者先把这个最优传输问题写成一个对偶变分问题，并由 KKT 条件得到逆向 HJB。原来直接写成“控制场优化”的问题，先被改写成“标量势函数 $U$ 满足的方程”。

第三步，看图中间的红色和粉色框。这里发生的是时间反转：

- 红色框是 reverse HJB，主角是 $U$；
- 粉色框是 forward HJB，主角是 $W(s,\mathbf{x}) := -U(1-s,\mathbf{x})$。

这一变换的作用不是换记号，而是把原来那个难以直接采样的 backward 问题，改写成一个可以沿正向时间求解的 value-function 问题。

第四步，看图下半部分。这里作者故意把 **训练阶段** 放在 forward 方向上来做：

- 起点放在左边的数据端 $p_{\text{data}}$；
- 让系统沿正向弛豫走向右边的参考端 $p_{\text{ref}}$；
- 底部那条粗弧线表示非受控的正向扩散轨迹；
- 右下角黑框说明：在这些正向、可采样的轨迹上，可以用 Feynman-Kac 路径平均去估计 forward potential，也就是 $W$。

所以训练阶段做的不是“直接学逆过程”，而是：

1. 从已有数据分布出发；
2. 沿容易模拟的正向弛豫采样轨迹；
3. 在这些轨迹上估计标量势 $W$。

第五步，再回到生成阶段。图中从右下黑框往上，再往左的箭头表示：

- 一旦 $W$ 学到了；
- 就可以通过时间反转关系把它转回逆向势函数 $U$；
- 再由梯度给出用于生成的 backward control；
- 最后从参考端 $p_{\text{ref}}$ 出发，受控地走到数据端 $p_{\text{data}}$。

所以这张图说明的是：**训练和生成之所以能接起来，不是因为作者直接学到了 backward drift，而是因为他先在可采样的 forward 方向学到了 $W$，再通过时间反转把这个结果带回生成方向。**

![方法总览示意图](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-03-figure-01.jpg)

Figure 1 画出的是一个闭环：

- **上半圈**：参考端 $\to$ 数据端，是我们想要的生成；
- **右半圈**：backward optimal control 先被改写成 reverse HJB，再通过时间反转变成 forward HJB；
- **下半圈**：数据端 $\to$ 参考端，是可采样、可训练的正向弛豫；
- **左半圈**：学到的 $W$ 再被送回上方，变成生成时需要的 backward control。

原文说时间反转对偶“打破循环依赖”，图 1 画出来的就是这个意思：**原来你想直接求的 backward generative control 太难；现在先在 forward 方向把 value function 学出来，再把它带回 backward 方向。**

### 2.6 b. Feynman-Kac estimation of the forward potential

这一小节依次完成四件事：

1. 用 Cole-Hopf 变换把非线性的 forward HJB 改写成线性的 PDE；  
2. 用 Feynman-Kac 公式把这个线性 PDE 改写成正向轨迹上的条件路径平均；  
3. 说明实践里为什么不用纯 Brownian 轨迹，而改用带漂移的 Langevin / OU 参考过程；  
4. 说明一旦训练时改用了这类参考过程，生成时就必须把对应的漂移修正补回 backward drift。  

#### 2.6.1 Eq. (5)：先把 forward HJB 线性化

前面已经得到 forward HJB，它的难点在于含有非线性的梯度平方项 $\|\nabla W\|^2$。  
作者这里做的第一步不是直接求解，而是先做一个变量替换：

$$
W=\frac{1}{\beta}\log Z,
\qquad
\beta=\frac{1}{2D\gamma}.
$$

这就是 Cole-Hopf 变换。它的作用不是换一个更好看的记号，而是把“梯度平方的非线性方程”变成“线性的扩散-吸收方程”。

这里最好把代入过程显式写出来。forward HJB 是

$$
\frac{\partial W}{\partial s}
-D\Delta W
-\frac{1}{2\gamma}\|\nabla W\|^2
+\nu(\mathbf{x})
=0.
$$

现在把

$$
W=\frac{1}{\beta}\log Z
$$

逐项代进去。

第一，时间导数变成

$$
\frac{\partial W}{\partial s}
=
\frac{1}{\beta}\frac{1}{Z}\frac{\partial Z}{\partial s}.
$$

第二，梯度平方项变成

$$
\|\nabla W\|^2
=
\frac{1}{\beta^2}\frac{\|\nabla Z\|^2}{Z^2}.
$$

第三，Laplacian 项会展开成两部分：

$$
\Delta W
=
\frac{1}{\beta}
\left(
\frac{\Delta Z}{Z}
-\frac{\|\nabla Z\|^2}{Z^2}
\right).
$$

关键点就在这里：$\Delta W$ 里本来就已经带着一个

$$
-\frac{\|\nabla Z\|^2}{Z^2}
$$

项。再乘上前面的 $-D$ 之后，它会贡献一个正的梯度平方项；而原方程里的

$$
-\frac{1}{2\gamma}\|\nabla W\|^2
$$

则会贡献一个负的梯度平方项。由于

$$
\beta=\frac{1}{2D\gamma},
$$

这里把系数明确写出来。来自 $-D\Delta W$ 的那一部分，梯度平方项前面的系数是

$$
\frac{D}{\beta},
$$

而来自

$$
-\frac{1}{2\gamma}\|\nabla W\|^2
$$

的那一部分，梯度平方项前面的系数是

$$
\frac{1}{2\gamma\beta^2}.
$$

现在把

$$
\beta=\frac{1}{2D\gamma}
$$

代进去，第一项变成

$$
\frac{D}{\beta}=D\cdot 2D\gamma = 2D^2\gamma,
$$

第二项变成

$$
\frac{1}{2\gamma\beta^2}
=
\frac{1}{2\gamma}\cdot (2D\gamma)^2
=
\frac{1}{2\gamma}\cdot 4D^2\gamma^2
=
2D^2\gamma.
$$

所以这两项大小完全一样，只是符号相反，于是梯度平方项被彻底消掉。

消掉之后，原方程里剩下的就只剩三类项：

- 时间导数项 $\partial_s Z$；
- 线性扩散项 $D\Delta Z$；
- 线性吸收项 $-\beta \nu Z$。

所以方程里不再含有任何关于 $\|\nabla Z\|^2$ 的非线性项，而是变成原文 `Eq. (5)`：

$$
\frac{\partial Z}{\partial s}=D\Delta Z-\beta \nu Z.
$$

这条方程现在更容易读：

- $D\Delta Z$ 是普通扩散；
- $-\beta \nu Z$ 是吸收项；
- 吸收率由空间代价 $\nu(\mathbf{x})$ 决定。

所以 `Eq. (5)` 的物理意思可以再拆成两步。

第一，后面在 Feynman-Kac 表示里，每一条 forward 路径都会带一个权重因子

$$
\exp\left(-\beta\int_0^t \nu(\mathbf{x}_s)\,ds\right).
$$

这说明路径真正被计入 $Z$ 时，不是简单地“一条路径算一次”，而是要先看它沿路累计了多少空间代价。

第二，如果一条路径经常穿过高代价区域，那么

$$
\int_0^t \nu(\mathbf{x}_s)\,ds
$$

就会更大，于是前面的指数权重就会更小；相反，如果一条路径大部分时间都待在低代价区域，这个累计代价就较小，它的指数权重也就不会被明显压低。

所以这里真正发生的是：**高代价路径在路径平均里会被自动降权，低代价路径会保留更大的权重。**

#### 2.6.2 Eq. (6)：线性 PDE 于是可以写成路径平均

一旦变成 `Eq. (5)` 这种线性扩散-吸收方程，作者就可以调用 Feynman-Kac 公式，把 PDE 的解重写成路径平均。原文 `Eq. (6)` 是：

$$
Z(t,\mathbf{x})=\mathbb{E}_{\mathbb{P}_0}\left[
Z(0,\mathbf{x}_0)
\exp\left(-\beta\int_0^t \nu(\mathbf{x}_s)\,ds\right)
\;\middle|\;
\mathbf{x}_t=\mathbf{x}
\right].
$$

这条式子分成三层看：

1. 在参考测度 $\mathbb{P}_0$ 下，先采一条正向轨迹；  
2. 对这条轨迹，把沿路累计的空间代价
   $$
   \int_0^t \nu(\mathbf{x}_s)\,ds
   $$
   指数加权；  
3. 然后对所有满足终点条件 $\mathbf{x}_t=\mathbf{x}$ 的轨迹做条件平均。

所以 `Eq. (6)` 带来的突破是：

**你不必先显式解出 PDE，再去得到 $W$；你可以直接通过正向轨迹上的 Monte Carlo 平均来估计 $Z$，再由 $W=\frac{1}{\beta}\log Z$ 还原出 value function。**

#### 2.6.3 Eq. (7)：为什么实践中不直接用纯 Brownian 轨迹

到这里，一个自然问题就出现了：  
既然 `Eq. (6)` 里参考测度 $\mathbb{P}_0$ 对应的是纯 Brownian motion，为什么不直接按它采样？

作者的回答是：**当数据分布离参考分布很远时，纯 Brownian 轨迹太低效。**

原因很直接：

- 纯 Brownian motion 只会盲目扩散；
- 而训练时有用的，是那些能把数据端逐渐带向参考端的 forward 轨迹；
- Feynman-Kac 估计本质上是在做一类带权路径平均：每条轨迹先按
  $e^{-\beta\int_0^t \nu(\mathbf{x}_s)\,ds}$ 赋权，再把这些权重做平均；
- 如果大量采到的轨迹都在无关区域乱飘，它们通常只会贡献非常小的权重；
- 这样一来，真正有用的贡献就只来自少数恰好走到低代价区域的轨迹；
- 样本之间的贡献会变得极不均匀，于是 Monte Carlo 平均就会强烈依赖“有没有碰巧采到那几条高权重路径”；
- 这就是为什么纯 Brownian 参考过程下，Feynman-Kac 估计的方差会很大。

所以原文 `Eq. (7)` 改用一个带漂移的参考过程：

$$
d\mathbf{x}_s=-\nabla V(\mathbf{x}_s)\,ds+\sqrt{2D}\,d\mathbf{B}_s,
\qquad
\mathbf{x}_0\sim p_{\text{data}}.
$$

这一步先把参考过程从“无漂移的纯 Brownian motion”换成了“带回复漂移的扩散过程”。  
只要漂移项能写成某个势函数的负梯度 $-\nabla V(\mathbf{x})$，这种过程就属于 Langevin 过程。  
论文实验里又进一步选了一个最简单、最标准的特例：令势函数 $V(\mathbf{x})$ 是二次函数。  
这时回复漂移就会变成线性的 $-\lambda \mathbf{x}$，对应的参考过程正是 Ornstein-Uhlenbeck（OU）过程。  
这样做的实际好处是：

- forward 轨迹更容易从数据端自然弛豫到参考端；
- 路径采样更稳定；
- 条件采样和数值实现也更方便。

所以 `Eq. (7)` 不是在改原问题，而是在改**训练时使用的参考轨迹生成方式**。

#### 2.6.4 Eq. (8)：为什么换了 forward 参考过程，生成时就必须补回一项漂移

这里是原文这一小节最容易折叠的一步。

如果训练时 forward 轨迹用的不是纯 Brownian，而是带漂移的 Langevin 过程，那么你学到的 $W$ 对应的，其实已经不是“纯 Brownian 参考下的值函数估计”，而是“在这个 drifted reference process 上做出来的估计”。

这意味着：  
**到了 backward 生成阶段，你不能只保留最优控制梯度，还必须把 forward 参考过程里原本那份漂移反转回来。**

原文 `Eq. (8)` 正是这一点：

$$
d\mathbf{x}_t=
\left(
\nabla V(\mathbf{x}_t)-\frac{1}{\gamma}\nabla U(t,\mathbf{x}_t)
\right)dt
+\sqrt{2D}\,d\mathbf{B}_t.
$$

这条式子里的两项要分开读：

- $\nabla V(\mathbf{x}_t)$：补回并反转 training-time reference drift；  
- $-\frac{1}{\gamma}\nabla U(t,\mathbf{x}_t)$：来自最优控制的生成驱动。

所以 `Eq. (8)` 的逻辑不是“又多出来一项漂移”，而是：

1. 训练时为了让 forward 路径更好采样，作者改用了 drifted reference process；  
2. 一旦这么做，forward 与 backward 的对应关系就不再是纯 Brownian 版本；  
3. 因此生成时必须显式把那份参考漂移反转回来，才能和训练时的 Feynman-Kac 估计保持一致。

#### 2.6.5 这一小节最后完成了什么

按原文顺序读完 `Eq. (5)–(8)`，这一小节完成的是一整条闭环：

1. 先把非线性的 forward HJB 变成线性的 PDE；  
2. 再把线性 PDE 变成 forward 轨迹上的路径平均；  
3. 再把训练时可采样的 forward 参考过程换成 Langevin / OU；  
4. 最后把这个训练选择在 backward 生成方程里补回来。

这四步连起来，$W$ 的角色才真正闭合起来：

1. 在 $Eq.\,(4)$ 里，$W$ 先被定义成 forward 问题的 value function，也就是“从当前位置走到参考端还剩多少最小代价”的标量势。  
2. 在 $Eq.\,(5)$ 里，Cole-Hopf 变换把关于 $W$ 的非线性 HJB 方程改写成关于 $Z$ 的线性 PDE，所以 $W$ 不再只是抽象定义，而是可以通过 $W=\frac{1}{\beta}\log Z$ 从一个可解对象恢复出来。  
3. 在 $Eq.\,(6)$ 和 $Eq.\,(7)$ 里，$Z$ 又被写成 forward 参考轨迹上的 Feynman-Kac 路径平均；这一步说明 $W$ 可以直接靠正向采样轨迹来训练，而不需要先显式求出 backward generative process。  
4. 在 $Eq.\,(8)$ 里，学到的 $W$ 再通过时间反转关系回到 backward 生成方程中，变成生成时真正需要的控制项梯度。  

所以这里真正完成的是：先把 $W$ 定义成最优控制里的 value function，再把它改写成可沿正向轨迹估计的对象，最后再把同一个 $W$ 无缝送回逆向生成过程。

#### 2.6.6 风险敏感控制与方差控制

这一小节要说明的是：为什么这套方法学到的 value function 不只关心“平均代价”，还会自动对“代价波动”敏感。

第一步，先回到前面的 Feynman-Kac 权重。  
在这套框架里，一条轨迹不是只按总代价 $C$ 线性计分，而是按指数权重进入平均：

$$
\exp(-\beta C).
$$

这意味着高代价轨迹会被指数压低，低代价轨迹会被保留更大的权重。  
所以这里的 value function 从一开始就不是“总代价的普通平均”，而更接近“总代价的指数加权统计量”。

第二步，对这种指数统计量做小 $\beta$ 展开。  
这里真正用到的不是普通 Taylor 展开，而是对数矩母函数的累积量展开。  
先把 forward 侧的量写清楚：

$$
Z(s,\mathbf{x})
=
\mathbb{E}\!\left[e^{-\beta C}\mid \mathbf{x}_s=\mathbf{x}\right],
\qquad
W(s,\mathbf{x})=\frac{1}{\beta}\log Z(s,\mathbf{x}).
$$

于是

$$
W(s,\mathbf{x})
=
\frac{1}{\beta}\log \mathbb{E}\!\left[e^{-\beta C}\mid \mathbf{x}_s=\mathbf{x}\right].
$$

当 $\beta$ 很小时，可以把它看成随机变量 $C$ 的对数矩母函数在 $\lambda=-\beta$ 处的展开：

$$
\log \mathbb{E}[e^{-\beta C}]
=
-\beta\,\mathbb{E}[C]
+\frac{\beta^2}{2}\operatorname{Var}(C)
+\mathcal{O}(\beta^3).
$$

两边再除以 $\beta$，就得到

$$
W(s,\mathbf{x})
=
-\mathbb{E}[C\mid \mathbf{x}_s=\mathbf{x}]
+\frac{\beta}{2}\operatorname{Var}[C\mid \mathbf{x}_s=\mathbf{x}]
+\mathcal{O}(\beta^2).
$$

第三步，把它翻回 backward value function。  
前面已经有时间反转关系

$$
W(s,\mathbf{x})=-U(1-s,\mathbf{x}).
$$

所以同一条展开式如果改写成 backward 侧的 value function $U$，符号就会整体反过来，得到

$$
U(t,\mathbf{x})
=
\mathbb{E}[C\mid \mathbf{x}_t=\mathbf{x}]
-\frac{\beta}{2}\operatorname{Var}[C\mid \mathbf{x}_t=\mathbf{x}]
+\mathcal{O}(\beta^2),
$$

其中 $C$ 是轨迹总代价。  
所以这里之所以能写成“期望项减去方差修正项”，本质上是因为 $U$ 来自 $\log \mathbb{E}[e^{-\beta C}]$ 的小 $\beta$ 累积量展开，而不是普通的线性平均。

这条式子可以直接读成：

- 第一项 $\mathbb{E}[C\mid \mathbf{x}_t=\mathbf{x}]$ 是条件平均总代价；
- 第二项 $-\frac{\beta}{2}\operatorname{Var}[C\mid \mathbf{x}_t=\mathbf{x}]$ 是对代价波动的修正；
- 更高阶项 $\mathcal{O}(\beta^2)$ 则包含更细的高阶累积量。

所以 $U$ 不是只在问“平均上哪条路径最省”，还在问“这条路径的总代价是否稳定”。

第三步，为什么方差项会带负号。  
因为这里的指数权重是 $\exp(-\beta C)$：  
总代价越大，权重下降越快；  
而总代价波动越大，说明偶尔会出现很差的高代价轨迹，这些轨迹会被指数权重额外惩罚。  
因此在小 $\beta$ 展开里，方差会作为一个额外扣分项出现。

第四步，这就是“风险敏感控制”的含义。  
如果一个控制策略虽然平均代价不高，但偶尔会产生非常大的代价波动，那么它在这里不会被当成和稳定策略同样好。  
也就是说，这套 value function 天然会偏好：

- 平均代价较低的路径；
- 在此基础上，代价波动也较小的路径。

第五步，参数 $\gamma$ 通过

$$
\beta=\frac{1}{2D\gamma}
$$

和前面的指数加权强度连在一起，因此它控制的就是“平均代价”和“代价波动”之间的 trade-off：

- 大 $\gamma$：更接近风险中性，只看平均代价；  
- 小 $\gamma$：更偏风险规避，更压制高方差路径。

因此：

- 大 $\gamma$ 对应小 $\beta$，指数加权更弱，模型更接近只看平均代价的风险中性控制；
- 小 $\gamma$ 对应大 $\beta$，指数加权更强，模型会更明显地压制高波动路径。

所以这里的“方差控制”不是训练时额外叠加的启发式技巧，而是已经被写进这套随机最优控制和 Feynman-Kac 加权结构里了。

---

## 3. LEARNING GENERATIVE SCALAR POTENTIAL

这一节回答的问题很具体：前面已经证明了存在一个 forward value function $W(s,\mathbf{x})$，而且它通过时间反转决定 backward 生成控制；现在要解决的是，**怎样把这个标量势真正训练出来，并把它变成一个可执行的生成算法。**

原文的顺序是：

1. 先选一条训练时真正会采样的 forward OU 轨迹；  
2. 再把 Feynman-Kac 表示改写成沿这些轨迹的监督目标；  
3. 再把监督目标拆成全局、一阶局部和边界三类损失；  
4. 最后说明训练完的 $W_\theta$ 怎样回到 backward controlled diffusion 中生成样本。

### 3.1 Eq. (9)：先把训练用的 forward 轨迹具体化成 OU 过程

`Section 2` 里已经说明：训练阶段真正能稳定采样的，是从数据端朝参考端弛豫的 forward reference process。  
到这一节，作者把这个参考过程固定成一个最简单的特例：Ornstein-Uhlenbeck（OU）过程。

原文写成离散时间就是

$$
\mathbf{x}_{k+1} = (1-\theta \Delta s)\mathbf{x}_k + \sqrt{2D\Delta s}\,\xi_k,
\qquad
\xi_k \sim \mathcal{N}(0,I).
\tag{9}
$$

这条式子可以分成两部分读：

- $(1-\theta \Delta s)\mathbf{x}_k$ 是线性回复项，表示状态会被逐步拉回参考端；
- $\sqrt{2D\Delta s}\,\xi_k$ 是扩散噪声，表示这条 forward 轨迹仍然带随机波动。

它对应的连续时间形式是

$$
d\mathbf{x}_s = -\theta \mathbf{x}_s\,ds + \sqrt{2D}\,d\mathbf{B}_s,
\qquad
\mathbf{x}_0 \sim p_{\mathrm{data}}.
$$

所以这一步的作用不是再发明一个新模型，而是把训练时真正要采样的 forward reference process 具体钉死成一个 tractable 的 OU 过程。

### 3.2 a. 轨迹监督：怎样把 Feynman-Kac 表示变成训练目标

接下来作者要做的是：把 `Section 2` 里的

$$
Z(s,\mathbf{x}) = \mathbb{E}\!\left[e^{-\beta C}\mid \mathbf{x}_s=\mathbf{x}\right]
$$

变成一个神经网络可以直接拟合的监督信号。

神经网络的主角是标量势 $W_\theta(s,\mathbf{x})$，而不是控制向量场。  
按照 Cole-Hopf 变换，

$$
Z_\theta(s,\mathbf{x}) = \exp(\beta W_\theta(s,\mathbf{x})).
$$

所以训练的真正目标，不是直接回归 drift，而是让网络输出的 $W_\theta$ 与 Feynman-Kac 给出的 $Z$ 一致。

### 3.3 Eq. (10)–(12)：三类损失分别在约束什么

#### 3.3.1 Eq. (10)：单条 forward 轨迹给出的 Feynman-Kac 贡献

对第 $i$ 条 forward OU 轨迹

$$
\left\{\mathbf{x}^{(i)}_k\right\}_{k=0}^K,
\qquad
s_k = k\Delta s,
$$

原文先定义单条轨迹在中间点 $(s_k,\mathbf{x}^{(i)}_k)$ 上给出的 Feynman-Kac 贡献：

$$
Z_{\mathrm{FK}}^{(i)}(s_k,\mathbf{x}^{(i)}_k)
:=
\exp\!\left(
-\beta \sum_{j=0}^{k-1}\nu_\phi(\mathbf{x}^{(i)}_j)\Delta s
\right)
\exp\!\left(\beta W_\theta(0,\mathbf{x}^{(i)}_0)\right).
\tag{10}
$$

这条式子的逻辑是：

1. 先从当前时刻 $s_k$ 沿轨迹往回看，累计这一路上已经走过的空间代价；  
2. 再把这些累计代价放进指数权重里；  
3. 最后乘上起点处的边界项 $\exp(\beta W_\theta(0,\mathbf{x}^{(i)}_0))$。

所以 $Z_{\mathrm{FK}}^{(i)}$ 不是“模型预测值”，而是：**给定一条 forward 样本路径后，这条路径为 Feynman-Kac 表示贡献的单轨迹估计量。**

#### 3.3.2 Eq. (11)：全局 Feynman-Kac 回归损失

有了单条路径贡献之后，第一类损失就是让网络给出的

$$
\exp(\beta W_\theta(s_k,\mathbf{x}^{(i)}_k))
$$

去拟合这些轨迹监督量：

$$
\mathcal{L}_{\mathrm{FK}}
:=
\frac{1}{NK}\sum_{i,k}
\left(
\exp\!\left(\beta W_\theta(s_k,\mathbf{x}^{(i)}_k)\right)
-Z_{\mathrm{FK}}^{(i)}(s_k,\mathbf{x}^{(i)}_k)
\right)^2.
\tag{11}
$$

这一项的作用最直接：  
它强迫网络学到的 $W_\theta$ 在整条 forward 轨迹尺度上，与 Feynman-Kac 路径积分的全局 cost-to-go 保持一致。

#### 3.3.3 Eq. (12)：局部一步一致性损失

接着又加了一个局部一阶损失：

$$
\mathcal{L}_{\mathrm{FK-local}}
:=
\frac{1}{NK}\sum_{i,k}
\left(
\exp\!\left(\beta W_\theta(s_{k+1},\mathbf{x}^{(i)}_{k+1})\right)
-e^{-\beta \nu_\phi(\mathbf{x}^{(i)}_k)\Delta s}
\exp\!\left(\beta W_\theta(s_k,\mathbf{x}^{(i)}_k)\right)
\right)^2.
\tag{12}
$$

这一步在做的事情是：

- 不再看整段从起点累积到当前时刻的全局一致性；
- 而是只检查相邻两个时间点之间，$Z=\exp(\beta W_\theta)$ 的传播是否符合一个离散的一步半群关系。

这里的“半群”说的是：对线性 PDE 的解，先推进一步、再推进一步，应该等价于直接推进两步。  
缩到一个离散时间步 $\Delta s$ 上，它最基本的局部版本就是：

$$
Z(s_{k+1},\mathbf{x}_{k+1})
\approx
e^{-\beta \nu_\phi(\mathbf{x}^{(i)}_k)\Delta s}\,
Z(s_k,\mathbf{x}^{(i)}_k).
$$

这条关系可以按三步读：

1. 从 $s_k$ 到 $s_{k+1}$ 只走一个小时间步；  
2. 这一步里先付出局部空间代价 $\nu_\phi(\mathbf{x}^{(i)}_k)\Delta s$，所以会带来一个权重因子 $e^{-\beta \nu_\phi(\mathbf{x}^{(i)}_k)\Delta s}$；  
3. 走完这一步之后，新的 $Z$ 应该等于“旧的 $Z$ 乘上这一步的局部传播因子”。

所以这一项的作用不是重复全局 Feynman-Kac，而是补上一条更局部的时间一致性约束，让网络在相邻时间层之间也能学得稳定。

### 3.4 Eq. (13)–(14)：为什么还需要一个 dual boundary loss

如果只有前面两项，网络确实会被轨迹积分监督；但它还没有被明确要求去满足 Lemma 2.1 的边界方向性。  
所以原文又加入了第三类损失：

$$
\mathcal{L}_{\mathrm{dual}}
:=
\frac{1}{N}\sum_{i=1}^{N}W_\theta(\mathbf{x}^{(i)}_K)
-\frac{1}{N}\sum_{i=1}^{N}W_\theta(\mathbf{x}^{(i)}_0).
\tag{13}
$$

这里两端分别对应：

- $\mathbf{x}^{(i)}_0$：forward 过程的起点，也就是数据端；
- $\mathbf{x}^{(i)}_K$：forward 过程的终点，也就是参考端。

这一项监督的是势函数在两端的相对高低关系，也就是 Kantorovich 对偶在边界上的方向性要求。  
这一点可以分成三步理解：

1. 在 forward 训练里，轨迹是从数据端出发，最后走到参考端；  
2. 对偶问题要求这个标量势在两端不能任意平移或翻转，而必须保留“数据端较高、参考端较低”的相对方向；  
3. 只有这样，后面把 $W_\theta$ 带回 backward 生成方程时，它的梯度才会给出正确的生成方向，而不会把概率流推反。

所以这里的 boundary loss，不是在学习新的局部动力学；它是在把整条 transport 的方向性钉死在两个端点上。

把三项合起来，就得到总损失：

$$
\mathcal{L}_{\mathrm{total}}(\theta)
:=
\lambda_{\mathrm{FK}}\mathcal{L}_{\mathrm{FK}}
+\lambda_{\mathrm{FK-local}}\mathcal{L}_{\mathrm{FK-local}}
+\lambda_{\mathrm{dual}}\mathcal{L}_{\mathrm{dual}}.
\tag{14}
$$

这三项不是平行罗列，而是三层约束：

- $\mathcal{L}_{\mathrm{FK}}$：保证全局路径积分一致性；
- $\mathcal{L}_{\mathrm{FK-local}}$：保证局部一步传播一致性；
- $\mathcal{L}_{\mathrm{dual}}$：保证两端边界方向性正确。

### 3.5 Algorithm 1：训练循环到底在做什么

这套训练循环可以按下面的顺序理解：

1. 先从数据集中取一批样本，作为 forward 过程的起点 $\mathbf{x}_0$。  
   这一步确定的是：这一轮训练要从哪些数据端状态出发。

2. 再从每个起点出发，用 $Eq.\,(9)$ 的 OU 过程采样一条 forward 轨迹。  
   这一步得到的是一串带时间标签的状态点
   $\{(s_k,\mathbf{x}_k)\}_{k=0}^K$，
   它们描述了样本如何从数据端逐步弛豫向参考端。

3. 然后把这些轨迹点送进网络，计算每个时间点上的标量势
   $W_\theta(s_k,\mathbf{x}_k)$。  
   到这一步为止，网络只是对每个时空点输出一个数，还没有直接学任何 drift。

4. 接着用 $Eq.\,(10)$，从每条 forward 轨迹构造单轨迹的 Feynman-Kac 监督量
   $Z_{\mathrm{FK}}^{(i)}(s_k,\mathbf{x}^{(i)}_k)$。  
   这一步把“沿轨迹累计的空间代价”和“起点边界值”合成一个监督目标。

5. 有了网络输出和轨迹监督量之后，再分别计算三类损失：
   - $Eq.\,(11)$ 的 $\mathcal{L}_{\mathrm{FK}}$，检查全局路径积分一致性；  
   - $Eq.\,(12)$ 的 $\mathcal{L}_{\mathrm{FK-local}}$，检查相邻时间步之间的一步传播一致性；  
   - $Eq.\,(13)$ 的 $\mathcal{L}_{\mathrm{dual}}$，检查数据端和参考端的边界方向性。

6. 最后按 $Eq.\,(14)$ 把三类损失加权求和，得到
   $\mathcal{L}_{\mathrm{total}}(\theta)$，再对参数 $\theta$ 做一次梯度更新。

所以这套训练循环真正学的不是 backward SDE 本身，而是：  
**一个在 forward 轨迹上被全局路径监督、局部时间一致性和边界方向性三重约束共同钉住的标量势 $W_\theta$。**

### 3.6 b. Eq. (15)：训练好的 $W_\theta$ 怎样回到生成过程

训练完成后，真正生成样本时就不再从数据端出发，而是回到 reference end，从那里启动 backward controlled diffusion。

原文把采样过程写成 Euler-Maruyama 离散化：

$$
\mathbf{x}_{k+1}
=
\mathbf{x}_k
+\Delta s\left(
\theta \mathbf{x}_k
+\frac{1}{\gamma}\nabla W_\theta(1-s_k,\mathbf{x}_k)
\right)
+\sqrt{2D\Delta s}\,\xi_k,
\qquad
\xi_k\sim \mathcal{N}(0,I).
\tag{15}
$$

这条式子也要分开读：

- $\theta \mathbf{x}_k$：反转 OU reference drift；
- $\frac{1}{\gamma}\nabla W_\theta(1-s_k,\mathbf{x}_k)$：训练得到的最优控制梯度；
- $\sqrt{2D\Delta s}\,\xi_k$：扩散噪声。

所以 `Section 3` 真正完成的是一整条可执行链：

1. 先用 forward OU 轨迹把 HJB 标量势训练出来；  
2. 再用这个学到的 $W_\theta$ 作为 backward drift 的核心控制项；  
3. 最后从 reference end 出发，把样本真正生成到数据端。  

也正因为这样，这篇文章的方法主角始终不是一个单独训练的 score network，而是这一个通过 trajectory supervision 学出来、最后又回到生成方程里的 scalar potential $W_\theta$。

---

## 4. RESULTS

这一节原文是按三条线来展示结果的：

1. 先看 HJB 标量势能否在 forward Feynman-Kac 轨迹监督下被稳定学出来；  
2. 再看学到的势函数能否真正把参考端样本送到数据端，也就是生成性能本身；  
3. 最后再看空间代价 $\nu(\mathbf{x})$ 能否像几何介质一样塑造最优路径。

所以 `Section 4` 不是一组杂散 demo，而是在依次验证：
- 势函数是否学得出来；
- 学到的势函数是否真的能驱动生成；
- 空间代价是否真的进入了路径几何。

### 4.1 a. Feynman-Kac 轨迹监督下的 HJB 势函数学习

第一组结果用三个标准 2D 基准数据集来验证：
- 4 Gaussians
- 2 Moons
- Swiss Roll

实验设置保持一致：
- 参考分布是各向同性高斯 $p_{\mathrm{ref}}\sim\mathcal{N}(0,I)$；
- 空间代价先固定为均匀场 $\nu(\mathbf{x})=1$；
- 势函数 $W(t,\mathbf{x})$ 用 10 层 MLP 参数化；
- forward 轨迹来自 OU 过程，参数 $D=0.05$、$\beta=0.1$、$T=128$；
- 训练目标使用 $Eq.\,(14)$ 的总损失。

这一组实验先回答最基础的问题：  
**只靠正向 OU 轨迹上的 Feynman-Kac 监督，能不能把一个有几何结构的 HJB 势函数学出来。**

![4 Gaussians 值函数与生成过程](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-01.jpg)

![2 Moons 值函数与生成过程](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-02.jpg)

![Swiss Roll 值函数与生成过程](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-03.jpg)

Figure 2 的上半部分给出的就是这个问题的正面证据。  
随着训练推进，$W(t,\mathbf{x})$ 逐渐长出和目标数据几何相匹配的 basin 结构：

- 在 4 Gaussians 上，后期势函数形成四个对称势阱，对应四个簇；
- 在 2 Moons 上，势函数形成两条弧形谷，追踪半月结构；
- 在 Swiss Roll 上，势函数形成螺旋通道，和流形几何对齐。

所以这里最重要的观察不是“图像好看”，而是：
**这些几何结构并不是从逆向 SDE 或 score network 里直接喂出来的，而是纯粹从正向轨迹监督中涌现出来的。**

![4 Gaussians 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-04.jpg)

![2 Moons 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-05.jpg)

![Swiss Roll 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-06.jpg)

Figure 2 的下半部分再补上训练稳定性这一层：  
三个数据集上的 $\mathcal{L}_{\mathrm{total}}$ 都单调下降，说明这套 trajectory supervision 不只是概念上成立，而且在不同拓扑几何下都能稳定训练。

### 4.2 b. Action-minimizing ground states：Figure 2 真正证明了什么

原文在同一组 2D 结果之后，紧接着强调了第二层含义：  
Figure 2 不只是“把值函数学出来了”，它还说明**学到的势函数确实在驱动一条最小代价的生成路径。**

这层含义可以按下面的顺序来读。

第一步，先看 Figure 2 上半部分学出来的 basin 结构。  
这些 basin 不是孤立的热力图纹理，而是在定义一张真正的 cost-to-go 地形：  
对 backward controlled diffusion 来说，哪些区域更容易继续朝目标数据流形推进，哪些区域代价更高，都会体现在这张势函数地形里。

第二步，再看 Figure 2 中间那排从参考端出发的粒子演化。  
如果学到的 $W$ 只是一个“看起来像目标分布”的静态函数，而没有真正进入动力学，那么这些粒子不会稳定地沿着 basin 被引导到目标结构上。  
原文给出的结果正相反：粒子确实会沿着势函数地形被逐步吸向目标流形，最后聚集到 4 Gaussians、2 Moons、Swiss Roll 各自的目标几何上。

第三步，把这两层合起来，才得到更强的结论：  
Figure 2 说明学到的 value function 并不只是“能拟合一张势能图”，而是真的在 backward 生成过程中承担了控制角色。  
也就是说，$W$ 提供的不是装饰性的几何信息，而是实际驱动 transport 的最优控制结构。

第四步，再看为什么这点重要。  
这三组数据的几何差别很大：

- 4 Gaussians 是离散多簇结构；
- 2 Moons 是非凸弧形结构；
- Swiss Roll 是卷曲流形结构。

如果方法依赖某种只适合特定拓扑的手工机制，它不太可能在这三种目标上都保持同样的输运效果。  
而 Figure 2 展示的是：同一套 forward-backward HJB 对偶、同一种 learned value function 机制，可以在这三类完全不同的目标几何上都把参考端样本稳定送到数据端。

所以这一部分真正验证的是两件事：

1. 势函数 $W$ 确实能从正向轨迹监督里学出来；  
2. 学出来的 $W$ 不是静态描述量，而是真正能承担 generative transport 的控制对象。

### 4.3 c. Geometry of refraction and Fermat’s principle for stochastics

前两组结果已经说明两件事：
- 标量势函数 $W$ 可以学出来；
- 学到的 $W$ 确实能驱动从参考端到数据端的生成输运。

Figure 3 继续往前追问一个更具体的问题：  
**如果只改空间代价 $\nu(\mathbf{x})$，而把起点分布、终点分布、网络结构、训练算法和参考动力学都保持不变，那么最优路径的几何会不会跟着系统性改变。**

所以这一组实验的关键不在“又做了一个 2D demo”，而在于它把变量控制得很干净：
- 左侧源分布固定为一个高斯团；
- 右侧目标分布固定为另一个高斯团；
- 学习框架仍然是同一套 forward-backward HJB matching；
- 唯一被主动改动的，就是中间区域的空间代价场 $\nu(\mathbf{x})$。

这样一来，后面看到的路径弯折、聚焦或绕开，就不能再归因于数据几何本身，而只能归因于 $\nu(\mathbf{x})$ 对最优代价地形的改变。

![非受控扩散（无学习控制）](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-01.jpg)

Figure 3(a) 先给出最外层的对照基线：  
如果根本没有学到的控制，粒子只按非受控扩散自然弥散。它们会向四周散开，但不会自发形成一条有方向的集中通道，更不会稳定地从左侧源团输运到右侧目标团。

这一张图先钉死了一件事：  
后面 Figure 3(b)(c)(d) 里看到的“路径像光线那样被引导”，不是扩散噪声自己长出来的，而必须来自学到的控制与空间代价的共同作用。

![平坦代价场的受控传输](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-02.jpg)

Figure 3(b) 再给出受控情形下的基线：  
现在控制已经学出来了，但把空间代价场设成平坦常数，也就是任意位置经过的代价都差不多。

这时最优路径几何退回到最普通的直线型输运。原因很简单：
- 目标仍然是把粒子从左侧送到右侧；
- 但空间上没有任何区域被额外奖励，也没有任何区域被额外惩罚；
- 因而最省总代价的路线就是最直接的路线。

所以 Figure 3(b) 可以理解成“均匀介质”下的基线传播图像。后面所有弯折，都是相对于这张平坦基线发生的。

![凹面代价：会聚透镜效应](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-04.jpg)

Figure 3(c) 开始只改 $\nu(\mathbf{x})$。  
这里把中间区域变成一个低代价凹槽，也就是说：和周围相比，穿过中心附近更“便宜”。

这会带来三步连锁反应：
1. 经过中心的累计空间代价变小；  
2. 因而在总体目标里，穿过中心的路径比绕远路的路径更划算；  
3. backward controlled diffusion 于是会把更多粒子拉向中轴区域。

宏观上看，就会出现一种会聚透镜效应：  
原本在平坦代价场里大致直线前进的路径，现在被进一步吸向中心，形成更窄、更集中的输运束。

![凸面代价：发散透镜效应](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-05.jpg)

Figure 3(d) 则把中间区域改成高代价凸峰，也就是：中心附近反而更“贵”。

于是同样的逻辑会反过来工作：
1. 直接穿过中心会积累更多空间代价；  
2. 即使直线距离更短，这条路线在总代价上也不再占优；  
3. 最优控制就会主动把粒子从中心两侧分流出去。

宏观上看，这对应一种发散透镜效应：  
路径不再向中轴聚拢，而是被中间的高代价区域推开，绕着中心障碍走。

到这里，Figure 3(a) 到 3(d) 其实形成了一条很清楚的因果链：
- 没有控制时，只会无结构弥散；
- 有控制但代价场平坦时，得到直线型基线输运；
- 中间区域更便宜时，路径会向中心会聚；
- 中间区域更昂贵时，路径会绕开中心发散。

![三种代价场的损失曲线对比](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-03.jpg)

Figure 3(e) 最后给出三种配置下的训练损失曲线。  
它补的是稳定性这一层：前面看到的聚焦和发散，不是少数随机轨迹的偶然偏折，而是在不同空间代价场下都能稳定学出来的整体几何行为。

原文把这一组结果和 Fermat 原理联系起来，真正想说的是：
- 在经典光学里，介质的折射率分布会改变光线选择哪条路；
- 在这里，空间代价 $\nu(\mathbf{x})$ 改变的是随机输运路径的总代价地形；
- 一旦总代价地形变了，最优路径的几何也会随之改变。

所以 Figure 3 验证的不是简单的“模型还能生成”，而是更强的一层：

**空间代价函数 $\nu(\mathbf{x})$ 不是目标函数里的装饰项。它会先进入 HJB 势函数，再通过学到的控制场进入实际生成路径，从而系统性地改变输运几何。**

## 5. Appendix D：高维扩展（MNIST）

前面的 `Section 4 Results` 都停留在 2D 几何上。  
这些结果已经说明：
- HJB 标量势函数可以学出来；
- 学到的势函数可以驱动生成输运；
- 空间代价 $\nu(\mathbf{x})$ 会系统性改变路径几何。

但一个自然追问马上会出现：  
**如果状态空间不再是 2D 平面，而是高维图像空间，这套“学势函数而不是直接学向量场”的方法还会不会维持基本结构。**

附录 D 的角色就在这里。它不是另起一个全新的主结果，而是在更难的高维 setting 里检查一件更基础的事：  
**学到的势函数在高维数据上，是否仍然表现出连贯的 cost-to-go 结构，而不是在训练样本附近做局部插值。**

作者把测试对象换成 MNIST 手写数字数据集。这里的状态空间不再是平面点，而是 $28\times 28=784$ 维的像素向量。参考端仍然取高斯噪声 $p_{\mathrm{ref}}=\mathcal N(0,I)$，空间代价场则固定成最简单的均匀形式 $\nu(\mathbf{x})=1$。这意味着附录 D 不再去研究复杂几何先验，而是把注意力集中在“高维可训练性”本身。

这一节还有一个和 2D 实验不同的技术点：  
作者没有显式存整条 forward OU 轨迹，而是利用 OU 过程的闭式条件分布，直接在任意时间采样扰动状态 $\mathbf{x}_t$。这样做的目的不是改理论，而是节省高维训练中的内存和轨迹存储成本。

在参数化上，2D 里的 MLP 也被换成了更适合图像的卷积 U-Net：
- encoder channels 为 `[32, 64, 128, 256]`；
- 归一化使用 GroupNorm；
- 保留 skip connections；
- 时间嵌入使用 Gaussian Fourier features。

所以附录 D 的问题可以压成一句：

**在高维图像空间里，沿着 forward OU 扰动轨迹去学习 $W_\theta(t,\mathbf{x})$，这个势函数还会不会长出和 2D 情形相同的“沿生成方向传播的 cost-to-go 结构”。**

![MNIST 初始化势函数](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-15-figure-01.jpg)

Figure 4(a) 先看初始化阶段。  
这时把尚未训练好的势函数 $W(t,\mathbf{x}(s))$ 画在一组测试轨迹上，几乎看不到任何有组织的结构。换句话说，在训练开始时，网络还没有学会把“当前状态在输运过程中处于什么位置”编码成一个连贯的剩余代价值。

![MNIST 训练后势函数](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-15-figure-02.jpg)

Figure 4(b) 再看训练 $200$ 个 epochs 之后。  
这时沿着 held-out 测试轨迹，会出现一个很明显的传播脉冲：随着轨迹向生成方向推进，$W$ 沿轨迹呈现出有组织的移动峰值。

这张图真正重要的地方有两层：
1. 这说明高维情形下学到的 $W$ 仍然不是静态噪声图，而是在沿轨迹编码一种 cost-to-go 结构；  
2. 这些轨迹是测试轨迹，不是训练时直接见过的样本，因此这个结构更像是全局一致的势函数行为，而不是对训练点的局部记忆。

也就是说，附录 D 想保住的不是“高维生成质量已经很好”，而是更基础的一点：  
**即使到了 784 维，Feynman-Kac 框架学到的仍然是一个沿输运方向有组织传播的值函数。**

![MNIST 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-15-figure-03.jpg)

Figure 4(c) 最后给出训练损失的收敛曲线。  
它补的是优化稳定性这一层：前面看到的传播脉冲不是偶然出现的视觉 artifact，而是伴随着整体训练目标的稳定下降一起长出来的。

所以附录 D 最稳妥的结论不是：
- “方法已经在高维 image generation 上达到最优结果”，
- 也不是“MNIST 上已经完整验证了生成质量指标”。

它真正说明的是：

**即使状态空间上升到 784 维像素空间，这套 HJB 标量势学习仍然保持了三件事：可训练、结构一致、并且能在测试轨迹上呈现出连贯的 cost-to-go 传播形态。**

换句话说，附录 D 在整篇文章里的作用，是把前面 2D 结果里的核心主张往高维再推一步：
- 学到的对象仍然是势函数，而不是无结构的黑箱回归；
- 这个势函数在高维上仍保留了值函数应有的方向性结构；
- 但文章在这里还没有进一步证明它已经在高维图像生成质量上超越现有方法。

---

## 6. 核心结论与贡献

### 6.1 理论贡献

这篇文章的理论贡献，最好不要只看成“又提出了一个生成算法”，而要看成它把三个原本分散的问题接成了一条线。

第一步，它先处理的是最核心的结构难点：  
真正想求的是从参考端到数据端的 backward optimal control，但这个方向天然带有循环依赖，因为很多量都需要在“已经知道最优生成轨迹”的前提下才能写出来。`Theorem 2.2` 的前向-后向 HJB 对偶，真正完成的就是把这个难题改写成一个可以沿 forward 弛豫轨迹求解的等价问题。也就是说，文章不是把 backward 问题近似掉了，而是把它等价地搬到了一个 tractable 的方向上。

第二步，它给值函数补上了明确的物理含义。通过 Cole-Hopf 变换和 Feynman-Kac 表示，原本抽象的 HJB 势函数不再只是“一个满足 PDE 的数学对象”，而可以读成路径加权平均所定义的路径空间自由能。这样一来，$W$ 既是最优控制里的 value function，又是对整条 forward 路径代价分布的压缩表达。

第三步，这篇文章把几条常见但通常分开讲的理论语言放到了同一个变分骨架里：
- 随机最优控制给出原始问题；
- Kantorovich 对偶给出变分重写；
- HJB 给出值函数 PDE；
- Cole-Hopf 和 Feynman-Kac 把 PDE 变成可采样对象；
- Schrödinger bridge 和非平衡统计物理则给出更大的背景语境。

所以这一节最稳妥的总结不是“证明了一个对偶定理”，而是：

**它把生成输运问题从 backward control、value function、路径自由能到可采样训练信号，第一次写成了一条闭合的理论链。**

### 6.2 方法论贡献

如果说理论部分回答的是“为什么这件事可做”，那么方法部分回答的就是“作者到底把学习对象和训练信号换成了什么”。

最关键的改变，是把原来直接学习高维控制向量场的问题，改写成学习一个标量势函数的问题。因为最优控制满足 $\mathbf{u}^*=-\frac{1}{\gamma}\nabla U$，所以真正需要拟合的主角不再是任意向量场，而是一个 value function。这样做带来两个直接后果：
- 搜索空间从“所有可能的向量场”收紧到“由某个标量势生成的梯度场”；
- 学到的对象也更容易解释，因为它本身表示的是剩余最小代价，而不是单纯的局部推动方向。

第二个方法论变化，是训练信号的来源被彻底改写了。文章没有沿着 score-based diffusion 那条线去估计 `score`，也没有直接在 backward SDE 上做监督，而是把所有训练信号都放在了 forward 参考轨迹上。这样一来，训练阶段真正用到的是：
- 全局 Feynman-Kac 轨迹监督；
- 局部一步半群一致性；
- 以及对偶边界条件。

也就是说，模型学到的不是“如何直接模仿一个逆向漂移”，而是“哪个标量势函数同时满足 forward PDE、路径平均和边界结构”。

第三个方法论亮点，是空间代价函数 $\nu(\mathbf{x})$ 被保留下来，作为一个可以直接设计的几何先验。Figure 3 已经说明，这个量不是装饰项：一旦改变 $\nu(\mathbf{x})$ 的空间分布，最优路径几何就会系统性改变。所以这篇方法天然给受约束生成留出了接口：
- 想让路径避开某些区域，就把那些区域设成高代价；
- 想让路径穿过某些区域，就把那些区域设成低代价。

所以方法上的最强信息不是“又提出了一种训练损失”，而是：

**作者把生成学习的主角，从直接拟合逆向向量场，改成了沿正向轨迹学习一个既可解释、又能回到生成控制的标量势函数。**

### 6.3 局限与展望

这篇文章的局限也很清楚，而且都和它最有特色的设计正相关。

首先，Cole-Hopf 和 Feynman-Kac 虽然把非线性 HJB 变成了可估计对象，但代价是把训练变成了一种路径重加权问题。有限采样下，这里会同时出现两类误差：
- 线性化和离散化带来的系统偏差；
- 指数重加权带来的方差膨胀。

这也是为什么文章虽然在理论上很干净，但在实践上仍然会面对 Monte Carlo 方差控制的问题。

第二，高维可扩展性目前还只验证到了“值函数结构仍然能学出来”这一步。MNIST 附录已经说明这套方法在 784 维像素空间里仍然可训练、并能在测试轨迹上产生连贯的 cost-to-go 脉冲；但这还不是严格意义上的高维生成 benchmark。文章目前没有在 FID、IS 等标准指标上和主流 score-based 或 flow matching 方法做系统对比，所以关于大规模高维生成质量的结论仍然要保守。

第三，这个框架天然还在往两个方向打开。一个方向是更物理的：把单粒子扩散推广到多粒子相互作用系统，例如分子动力学、活性物质或更一般的相互作用随机系统。另一个方向是更方法学的：把空间代价函数 $\nu(\mathbf{x})$ 当成外加几何先验，用来对预训练生成模型做受约束微调，让生成路径自动避开危险区域、或更偏好某些允许区域。

所以这一节更合适的总结不是“这篇还有一些缺点”，而是：

**它已经把理论结构搭得很完整，但真正决定这条路线能不能继续走远的，将是两个问题：高维下的方差控制，以及空间先验在更复杂生成模型中的可操作性。**

---

## 7. 关键公式速查

| 编号 | 公式 | 意义 |
|------|------|------|
| (1) | $d\mathbf{x}_t = \mathbf{u}_t dt + \sqrt{2D} d\mathbf{B}_t$ | 受控 Itô SDE |
| (2) | $\min_\mathbf{u} \mathbb{E}[\int \nu + \frac{\gamma}{2}\|\mathbf{u}\|^2]$ | 最优控制目标 |
| (3) | 对偶变分问题 + HJB 约束 | Kantorovich 对偶 |
| (4) | $\partial_s W - D\Delta W - \frac{1}{2\gamma}\|\nabla W\|^2 + \nu = 0$ | 正向 HJB |
| (5) | $\partial_t Z = D\Delta Z - \beta\nu Z$ | Cole-Hopf 线性化 PDE |
| (6) | $Z$ 的 Feynman-Kac 路径积分表示 | 无需逆向模拟的估计 |
| (14) | $\mathcal{L}_{\text{total}} = \lambda_{\text{FK}}\mathcal{L}_{\text{FK}} + \lambda_{\text{FK-local}}\mathcal{L}_{\text{FK-local}} + \lambda_{\text{dual}}\mathcal{L}_{\text{dual}}$ | 训练总损失 |
| (15) | 逆向 Euler-Maruyama 采样公式 | 生成过程 |

---

## 8. 个人评论

**优点**：
- 理论上非常完整，从变分原理出发推到可训练的算法，每一步都有物理对应和数学保证
- $\nu(\mathbf{x})$ 的引入为"受约束生成"开辟了新范式，Fermat 原理类比既优美又精确
- 标量势学习 vs 向量场学习是一个值得关注的设计选择，可能在物理约束系统中有独特优势

**关注点**：
- Feynman-Kac 估计的方差在高维下如何增长？指数级的 reweighting 可能导致采样效率问题
- 与 adjoint matching (Domingo-Enrich et al., 2024) 的实质区别需要更清晰的对比——两者都通过标量势的梯度定义最优控制
- MNIST 实验仅展示了值函数结构，未展示生成样本质量，缺乏与 flow matching / score-based 方法的定量对比
