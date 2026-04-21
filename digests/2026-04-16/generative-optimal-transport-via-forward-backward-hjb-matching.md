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

原文接着做的事情，不是简单回顾文献，而是把现有方法按“它们到底优化了什么”重新摆了一遍。

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

原文接着才会用到：

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

这句话分三层。

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

这一步最好把系数真正写出来。来自 $-D\Delta W$ 的那一部分，梯度平方项前面的系数是

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

所以 `Eq. (5)` 的物理意思是：  
**如果一条 forward 路径经常穿过高代价区域，它对 $Z$ 的贡献就会被指数压低；如果它主要待在低代价区域，它的贡献就会被保留下来。**

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
- 如果大量采到的轨迹都在无关区域乱飘，Feynman-Kac 估计的方差会很大。

所以原文 `Eq. (7)` 改用一个带漂移的参考过程：

$$
d\mathbf{x}_s=-\nabla V(\mathbf{x}_s)\,ds+\sqrt{2D}\,d\mathbf{B}_s,
\qquad
\mathbf{x}_0\sim p_{\text{data}}.
$$

这就是一个 Langevin 参考过程。论文实验里进一步把它具体化成 OU 过程。  
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

这里不是单独讲四条公式，而是在回答一个具体问题：

**为什么 $W$ 不只是一个理论上的标量势，而是一个可以沿正向轨迹训练出来、最后又能正确带回生成过程的对象。**

#### 2.6.6 风险敏感控制与方差控制

原文最后再补了一层物理解释：对 value function 做 Taylor 展开，可得到

$$
U(t,\mathbf{x})
=
\mathbb{E}[C\mid \mathbf{x}_t=\mathbf{x}]
-\frac{\beta}{2}\operatorname{Var}[C\mid \mathbf{x}_t=\mathbf{x}]
+\mathcal{O}(\beta^2),
$$

其中 $C$ 是轨迹总代价。  
这说明 $U$ 不只编码“期望代价”，还编码“代价波动”。

于是参数 $\gamma$ 通过

$$
\beta=\frac{1}{2D\gamma}
$$

控制了一个 trade-off：

- 大 $\gamma$：更接近风险中性，只看平均代价；  
- 小 $\gamma$：更偏风险规避，更压制高方差路径。

所以这篇文章最后顺手指出：  
**方差控制不是额外加的技巧，而是已经被写进这套随机最优控制结构里了。**

---

## 5. 算法设计

### 5.1 损失函数的三个分量

训练目标是学习标量势 $W_\theta(s, \mathbf{x})$（通过神经网络参数化），总损失：

$$\mathcal{L}_{\text{total}}(\theta) = \lambda_{\text{FK}} \mathcal{L}_{\text{FK}} + \lambda_{\text{FK-local}} \mathcal{L}_{\text{FK-local}} + \lambda_{\text{dual}} \mathcal{L}_{\text{dual}}$$

| 损失分量 | 物理意义 | 数学形式 |
|----------|----------|----------|
| $\mathcal{L}_{\text{FK}}$ | 全局 Feynman-Kac 一致性：学到的 $\exp(\beta W_\theta)$ 与轨迹积分目标的偏差 | 沿整条轨迹的累积代价回归 |
| $\mathcal{L}_{\text{FK-local}}$ | 局部时间一致性：相邻时间步的离散半群约束 | 单步传播的 $Z$ 值匹配 |
| $\mathcal{L}_{\text{dual}}$ | Kantorovich 对偶边界条件：势在数据端高、参考端低 | $W$ 在 $s=0$（数据端）和 $s=1$（噪声端）的期望差 |

三个分量各司其职：$\mathcal{L}_{\text{FK}}$ 保证全局路径积分正确性，$\mathcal{L}_{\text{FK-local}}$ 稳定逐步梯度传播，$\mathcal{L}_{\text{dual}}$ 确保概率流方向正确。

### 5.2 训练流程 (Algorithm 1)

1. 从数据集采样 $\mathbf{x}_0$
2. 用 OU 过程生成正向轨迹 $\{\mathbf{x}_k\}_{k=0}^K$
3. 在轨迹上计算 $W_\theta(s_k, \mathbf{x}_k)$
4. 由 Feynman-Kac 公式构造监督目标 $Z_{\text{FK}}$
5. 最小化 $\mathcal{L}_{\text{total}}$，更新 $\theta$

### 5.3 生成流程 (Algorithm 2)

从 $\mathbf{x}_0 \sim p_{\text{ref}}$ 出发，按 Euler-Maruyama 格式迭代：

$$\mathbf{x}_{k+1} = \mathbf{x}_k + \Delta s \left(\theta \mathbf{x}_k + \frac{1}{\gamma}\nabla W_\theta(1-s_k, \mathbf{x}_k)\right) + \sqrt{2D\Delta s} \, \xi_k$$

其中第一项 $\theta\mathbf{x}_k$ 反转 OU 漂移，第二项 $\nabla W_\theta$ 提供最优控制驱动。

---

## 6. 实验验证

### 6.1 2D 基准数据集上的值函数学习

在三个标准 2D 基准（4 Gaussians、2 Moons、Swiss Roll）上验证。网络为 10 层 MLP（64 hidden units, GeLU, sinusoidal time embeddings），OU 过程 $D=0.05$, $\beta=0.1$, $T=128$ 步。

![4 Gaussians 值函数与生成过程](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-01.jpg)

![2 Moons 值函数与生成过程](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-02.jpg)

![Swiss Roll 值函数与生成过程](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-03.jpg)

**Figure 2（上三图）在论文逻辑中的角色**：这组图是方法正确性的核心视觉证据。每个数据集显示两行：上行是学到的值函数 $W(t, \mathbf{x})$ 在 $t=0, 0.3, 0.7, 1.0$ 的热力图快照，下行是逆向受控扩散过程中粒子位置的演化。关键观察：

- **4 Gaussians**：$t=1$ 时值函数发展出四个对称势阱，精确对应四个高斯簇
- **2 Moons**：势函数形成两条弧形谷，追踪半月形弧
- **Swiss Roll**：势函数发展出螺旋通道，与流形对齐

这些结构**纯粹从正向轨迹监督中涌现**——没有逆向 SDE 模拟或 score 估计。

![4 Gaussians 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-04.jpg)

![2 Moons 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-05.jpg)

![Swiss Roll 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-07-figure-06.jpg)

**Figure 2（下三图）**：三个数据集上 $\mathcal{L}_{\text{total}}$ 的训练损失曲线，均呈单调下降，验证了 Feynman-Kac 轨迹监督在不同拓扑几何下的鲁棒性。

### 6.2 空间代价几何：随机 Fermat 原理

这是本文最具创新性的实验。通过设计不同的空间代价场 $\nu(\mathbf{x})$，展示其如何像**折射率**一样塑造最优传输路径。

![非受控扩散（无学习控制）](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-01.jpg)

**Figure 3(a)** — 非受控正向扩散：粒子从源（红点）到参考（蓝点）的无结构扩散，没有方向偏好，轨迹（绿线）弥散于整个空间。这是对照基线。

![平坦代价场的受控传输](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-02.jpg)

**Figure 3(b)** — 平坦 $\nu = \text{const}$：恢复直线传输几何，是均匀介质中的"直线传播"。

![凹面代价：会聚透镜效应](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-04.jpg)

**Figure 3(c)** — 凹面代价（中点低 $\nu$）：低代价区域形成势阱，将轨迹向中心汇聚——类比经典光学中的**会聚透镜**。

![凸面代价：发散透镜效应](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-05.jpg)

**Figure 3(d)** — 凸面代价（中点高 $\nu$）：高代价区域形成能量壁垒，迫使轨迹向外绕行——类比**发散透镜**。

![三种代价场的损失曲线对比](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-08-figure-03.jpg)

**Figure 3(e)** — 三种配置的损失收敛曲线，验证了在不同空间代价场下训练的鲁棒性。

**核心物理类比**：在经典光学中，Fermat 原理（最小光程原理）决定光线在折射率 $n(\mathbf{x})$ 空间变化的介质中沿测地线传播。本文中 $\nu(\mathbf{x})$ 完全类比 $n(\mathbf{x})$：
- 高 $\nu$ 区域 → 高折射率 → 光线（轨迹）向外偏折
- 低 $\nu$ 区域 → 低折射率势阱 → 光线（轨迹）向内汇聚

HJB 值函数 $W$ 编码了这些最小代价路径的自由能几何。

### 6.3 高维扩展：MNIST (784 维)

将框架扩展到 MNIST 手写数字数据集（$28 \times 28 = 784$ 维），值函数用卷积 U-Net 参数化（encoder channels [32, 64, 128, 256]，GroupNorm，skip connections，Gaussian Fourier time embeddings）。

![MNIST 初始化势函数](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-15-figure-01.jpg)

**Figure 4(a)** — 初始化阶段：$W(t, \mathbf{x}(s))$ 沿测试轨迹（不同颜色对应不同时间步 $s$）的分布无结构、无方向性。

![MNIST 训练后势函数](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-15-figure-02.jpg)

**Figure 4(b)** — 训练 200 epochs 后：每条轨迹上出现清晰的**传播脉冲**（propagating bump）——$W$ 沿生成路径形成移动的势峰，与 2D 实验中观察到的代价结构一致。这一结构出现在**未参与训练的测试轨迹上**，证明 Feynman-Kac 框架学到的是全局一致的值函数，而非训练样本的局部插值。

![MNIST 损失曲线](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-15-figure-03.jpg)

**Figure 4(c)** — 高维设置下的损失收敛，确认了 HJB 势函数的热力学可解释性在维度扩展后得以保持。

---

## 7. 核心结论与贡献

### 7.1 理论贡献

1. **前向-后向 HJB 对偶定理**（Theorem 2.2）：建立了逆向生成控制与正向扩散之间的严格数学等价，将不可解的逆向问题转化为可沿正向轨迹估计的问题
2. **路径空间自由能解释**：通过 Cole-Hopf + Feynman-Kac，值函数获得了路径空间自由能（path-space free energy）的明确物理含义
3. **统一框架**：将随机最优控制、Schrödinger bridge 理论、非平衡统计力学以及 Kantorovich 对偶统一于同一变分结构中

### 7.2 方法论贡献

1. **标量势学习**：将高维向量场估计降维为标量势学习，$\mathbf{u}^* = -\frac{1}{\gamma}\nabla U$ 天然保证了向量场的旋度为零（curl-free），提高了参数效率和可解释性
2. **无需 score estimation 或逆向 SDE**：所有训练信号来自正向扩散轨迹上的 Feynman-Kac 估计
3. **空间代价函数 $\nu(\mathbf{x})$ 作为几何先验**：为受约束生成（constrained generation）提供了自然接口——通过设计 $\nu$ 的空间分布即可引导轨迹避开或聚焦于特定状态空间区域

### 7.3 局限与展望

- **PDE 残差与方差**：Cole-Hopf 线性化在有限采样下的系统偏差和方差的定量分析仍是开放问题
- **高维可扩展性**：MNIST 实验仅为概念验证，尚未与 SOTA 生成模型在 FID/IS 等指标上对比
- **交互粒子系统**：扩展到多粒子相互作用场景（如分子动力学、活性物质）是重要的物理应用方向
- **预训练模型微调**：$\nu(\mathbf{x})$ 可用于对预训练生成模型进行空间约束微调，类似于物理先验引导的 fine-tuning

---

## 8. 关键公式速查

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

## 9. 个人评论

**优点**：
- 理论上非常完整，从变分原理出发推到可训练的算法，每一步都有物理对应和数学保证
- $\nu(\mathbf{x})$ 的引入为"受约束生成"开辟了新范式，Fermat 原理类比既优美又精确
- 标量势学习 vs 向量场学习是一个值得关注的设计选择，可能在物理约束系统中有独特优势

**关注点**：
- Feynman-Kac 估计的方差在高维下如何增长？指数级的 reweighting 可能导致采样效率问题
- 与 adjoint matching (Domingo-Enrich et al., 2024) 的实质区别需要更清晰的对比——两者都通过标量势的梯度定义最优控制
- MNIST 实验仅展示了值函数结构，未展示生成样本质量，缺乏与 flow matching / score-based 方法的定量对比
