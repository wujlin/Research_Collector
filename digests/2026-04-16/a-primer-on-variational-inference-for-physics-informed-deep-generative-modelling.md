---
title: "A Primer on Variational Inference for Physics-Informed Deep Generative Modelling"
authors: "Alex Glyn-Davies, Arnaud Vadeboncoeur, O. Deniz Akyildiz, Ieva Kazlauskaite, Mark Girolami"
venue: "arXiv (2024)"
date_read: "2026-04-16"
topics: ["变分推断", "ELBO", "physics-informed", "生成模型", "逆问题"]
---

# A Primer on Variational Inference for Physics-Informed Deep Generative Modelling

## 1. Introduction

引言真正要回答的问题是：如果研究对象是受物理规律约束的系统，为什么变分推断会成为一条自然的方法主线。作者没有一上来写 ELBO，而是先把物理建模、逆问题和不确定性量化放回同一条问题链里。

### 1.1 文章先把自己的角色说清楚

这篇文章不是提出一个单独的新模型，而是一篇 tutorial + review。它要做的事情，是把 physics-informed deep generative modelling 中最常见的几类 VI 思路，放回统一的数学框架里重新组织。因此引言的任务也不是“先给结论”，而是先搭一条阅读顺序：为什么先讲 forward problem，再讲 inverse problem，再讲 VI，最后才去综述具体方法。

### 1.2 第一层背景：forward problem 为什么会把人推向代理模型和不确定性量化

作者先从 forward problem 讲起。这里的对象主要是 PDE 驱动的物理模型。热传导、流体速度场、电势分布这类问题，本质上都在描述某些物理量如何随时间和空间变化。于是 forward problem 从来不只是“给定参数求一个解”，它还总是连着初始条件、边界条件、几何区域和材料参数等一整套物理设定。

这一层里最重要的不是“PDE 很常见”，而是 forward solver 的计算瓶颈。单次求解也许可以承受，但一旦进入 multi-query 场景，问题就变了。这里的 multi-query 指的是：你不是只求一次解，而是要在很多不同参数下反复求解同一个模型。之所以会这样，往往是因为你不只想得到一个单一答案，还想知道答案对参数扰动、观测噪声或模型不确定性到底有多敏感。

作者这里提到的 uncertainty quantification，最直接的意思就是：**不只问“解是多少”，还问“这个解有多不确定”。** 例如，参数如果有误差，最终温度场会波动多大；观测如果带噪，反推出的材料参数会有多不稳定；模型如果只见过有限数据，它对新输入到底有多自信。也就是说，不确定性量化关心的是结果周围那一圈“不确定的范围”，而不是只给一个点值答案。

这就是代理模型会进入这条脉络的原因。这里的 surrogate model，不是另一个物理模型，而是一个**更便宜的近似替身**：原来每次都要调用昂贵的 PDE 求解器，现在先学一个“参数到解”的近似映射，以后需要重复查询时，就尽量由这个替身模型来回答。作者在引言里点了两类代表：
- Gaussian process 这类经典代理模型，天然就能同时给出预测和不确定性；
- DeepONet、FNO 这类学习型算子虽然很适合做 PDE 的近似求解器，但不像 GP 那样天然带有内建的不确定性量化。

所以引言在这一层先建立的是：**forward problem 不是单纯的数值求解问题，而是会自然长出“需要一个便宜替身模型”和“需要知道结果有多不确定”这两种需求的问题。**

### 1.3 第二层背景：inverse problem 为什么会把人推向后验推断

然后作者把视角从正向求解切到 inverse problem。这里问的已经不是“参数给定时系统怎样演化”，而是“给定观测以后，究竟是哪组参数产生了这些数据”。

这一步里最核心的事实是：inverse problem 往往不是一个“把结果直接倒回去”的干净问题。原因很简单，观测通常比完整物理状态要少得多。你真正看到的往往只是少数传感器读数、有限时间点的数据、或者带噪的间接测量，而你想恢复的却可能是一整个参数场、边界条件，甚至隐藏在 PDE 里的物理系数。于是从观测回到参数时，信息天然是不够的。

作者用的术语是 ill-posedness。这里最好把它拆开理解：  
- **没有唯一性**：很多不同的参数配置都可能解释同一组观测；  
- **没有稳定性**：观测里哪怕只有一点小噪声，反推出的参数也可能发生很大变化。  

所以问题不在于“数学上不能写反函数”，而在于：即使形式上能反推，得到的结果也可能不唯一、不稳定、而且对噪声极其敏感。正因为这样，inverse problem 不能只靠把 forward model 倒过来，而必须额外引入某种约束或先验，来排除那些虽然能解释数据、但并不合理的参数配置。

于是 inverse problem 自然分出两条经典路线：
- 点估计方法通过正则化挑出一个代表性解；
- 贝叶斯方法把目标改成恢复参数的后验分布，从而把不确定性本身纳入推断对象。

这两条路线的差别也最好讲清楚。点估计方法的思路是：既然可能有很多可行解，那就再加一个偏好原则，例如偏好更平滑、更小、或者更符合物理结构的参数，然后从所有可行解里挑一个最合适的代表。贝叶斯方法则走得更远一些：它不只挑一个答案，而是承认“可能有很多参数都能解释这些数据”，然后把这种不确定性整体写成一个后验分布。

因此，引言的第二层推进其实是在说：**forward problem 把你带到代理模型和不确定性量化，inverse problem 则进一步把你带到“必须处理后验分布”的推断问题。**

### 1.4 第三层背景：VI 为什么会在这里自然出现

VI 正是在这个背景下被引入的。这里需要先把问题重新说清楚：一旦你在 inverse problem 里采用贝叶斯视角，目标就不再是找一个单点答案，而是恢复一个后验分布。可是真正困难的地方恰恰在这里。困难不是“后验”这个概念本身，而是它通常不能直接写成一个可计算的闭式表达。为了真正评估这个后验，你往往要处理高维积分；而这些积分里的似然项，又常常依赖一个非线性的 forward solver。只要 forward solver 背后还连着昂贵的 PDE 数值求解，整个后验推断的计算成本就会被层层放大。因此，“要后验分布”这件事在物理问题里并不是概念上难，而是计算上难。

作者在引言里先点出的，就是这层张力：物理问题经常必须做不确定性量化，但后验分布本身又往往难算。MCMC 当然是一条原则性路线，因为它直接面向后验采样；但在物理问题里，它的代价通常会被迅速放大。原因不只是“采样慢”，而是每一次接受率评估、每一次链的推进，背后都可能连着一次昂贵的 forward model 求解。只要 forward model 本身已经很贵，MCMC 的总体成本就会进一步膨胀。

VI 的吸引力正是在这里出现的。它不是直接去“精确算出后验”，而是换一个角度：先选一个可处理的近似分布族，再通过优化让这个近似分布尽可能靠近真实后验。也就是说，原来那个难以直接处理的后验推断问题，被改写成了一个可优化的问题。作者在引言里强调的，不是“VI 一定最准确”，而是它在这里提供了一种现实可用的折中：你牺牲一部分后验逼近精度，换来可扩展的计算代价和仍然可用的不确定性描述。

但作者随后又强调，VI 在物理问题里的价值还不只在于“它比 MCMC 便宜”。更关键的一点是：物理问题通常自带很强的依赖结构。参数怎样决定解，解怎样经过观测模型变成数据，噪声在哪里进入，残差又处在什么位置，这些关系在物理问题里往往不是随意拼起来的，而是由 forward model、观测机制和物理约束本身决定的。

这里说的 conditional dependence structure，最好不要只当成一个抽象术语。更直接地说，它是在问：**如果把整个问题写成一个概率模型，哪些变量应该显式保留，哪些变量可以被消掉，哪些关系要作为约束留下来。** 比如：
- 有的建模方式会把解场当成显式随机变量保留下来，于是参数先生成解，解再生成观测；
- 有的建模方式会把解场通过 forward solver 隐式消掉，于是参数和观测之间直接由一个复合映射相连；
- 有的建模方式会把 PDE 残差作为单独对象保留下来，当成额外约束；
- 有的建模方式则把这些约束吸收到似然、先验或者生成结构里。

这些选择看起来像“建模风格不同”，但作者真正想说的是：它们对应的是不同的依赖结构，也因此对应不同的 VI 形式。也就是说，physics-informed VI 方法之所以会长成很多分支，不是因为大家在随意造变体，而是因为不同物理问题本来就要求你以不同方式组织“参数、解、观测、噪声、残差”这些变量之间的关系。

VI 在这里的好处，就体现在它允许你把这层结构显式写进推断框架里。你不必被迫采用一种统一但未必合适的后验表示，而是可以根据问题本身的物理结构，去设计近似后验、生成模型和约束项的组织方式。

所以这一层真正建立起来的判断是：VI 之所以会在这里自然出现，不只是因为后验难算。它同时回答了两个要求：
- 一方面，它把难算的后验推断改写成可优化的问题；
- 另一方面，它允许你把物理系统内部真实存在的依赖结构显式保留下来。

### 1.5 引言最后才交代全文结构

在这些背景都铺好之后，作者最后才交代文章路线。`Section 2.1` 讲 forward problems，`Section 2.2` 讲 inverse problems 的优化与贝叶斯视角，`Section 2.3` 正式推导 VI。`Section 3` 再回到 physics-based generative modelling 文献，把现有方法分成两条路线：一条基于 forward model，另一条基于加权残差或 PDE 残差。

所以这篇引言真正建立起来的主线不是“VI 很有用”这种抽象判断，而是一条更清楚的问题链：forward problem 先把你带到代理模型和不确定性量化的需求，inverse problem 再把你推到后验推断；而一旦你既要可计算、又要不确定性量化、还要把物理依赖结构写进模型，VI 就成了一个自然的组织框架。

---

## 2. Physics and Inference

原文的 `Section 2` 不是直接进入公式推导，而是先把整篇文章后面要反复用到的对象和路线钉死。它做的事情可以压成一句话：**先把物理推断里最基本的三个对象分清楚，再依次说明 forward problem、inverse problem 和 variational inference 分别在处理什么。**

这一节还有一个容易被忽略的限定：作者从一开始就说明，这篇文章只讨论**离散化之后的有限维表示**。也就是说，后面真正进入推断和优化的，不是无限维函数本身，而是它们在某个离散化方案下得到的有限维参数化表示。这个限定很重要，因为它解释了为什么后面的 VI、VAE 和 normalizing flow 都是在向量空间里操作，而不是直接在函数空间里操作。

### 2.1 三空间框架：参数 → 解 → 观测

![三空间框架图](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-02-figure-01.jpg)

作者先给出 Figure 1，不是为了补一张概念图，而是为了先把后面所有方法都要落回去的三类对象分清楚。论文把物理推断中的核心量压成三个空间：

| 空间 | 符号 | 含义 |
|------|------|------|
| 参数空间 (parameter space) | $\mathcal{Z}$ | 物理系统的设定参数，如扩散系数场、边界条件 |
| 解空间 (solution space) | $\mathcal{U}$ | PDE 解场，如温度场、速度场 |
| 观测空间 (observation space) | $\mathcal{Y}$ | 传感器实际观测到的数据 |

这三类对象之间通过两个映射连接：
- **正向模型 (forward model)** $F^\dagger: \mathcal{Z}_h \to \mathcal{U}_h$，从参数到解
- **观测模型 (observation model)** $H^\dagger: \mathcal{U}_h \to \mathcal{Y}$，从解到观测

所以正向问题是沿箭头方向走：从参数到解，再从解到观测；逆向问题则是在反方向上做推断：从观测回到解，或者从观测回到参数。整篇文章里后面出现的点估计、贝叶斯逆问题、VI、VAE 和 physics-informed generative model，本质上都可以重新定位回这张图。

这一小节里还埋了一个后面会持续使用的符号约定：下标 $h$ 表示离散化尺度。因此 $z_h$ 和 $u_h$ 不是连续函数本身，而是它们离散化之后的有限维表示。作者之所以先讲这件事，是因为后面的推断目标、似然函数和变分分布，都是建立在这些离散化后的对象上。

---

### 2.2 正向问题：PDE 与加权残差方法

把三空间框架钉死之后，原文先进入 `Section 2.1 Forward Problems`。这里的重点不是再重复“PDE 很重要”，而是说明：如果要把物理问题接进推断框架，首先必须把正向模型写成一个统一的数值离散化对象。

这里真正要解决的第一个问题是：什么叫 `forward problem`。在这篇文章里，它指的不是抽象的“正向求解”，而是很具体的一件事：当参数、边界条件和源项都给定时，系统会演化出什么样的解。例如给定扩散系数、边界温度和热源分布之后，温度场到底是什么；给定介质参数和边界电势之后，电势分布又会是什么。也就是说，forward problem 关心的是：**从物理设定出发，推出解场。**

但一旦把 forward problem 写成 PDE，就会立刻碰到一个数值上的障碍：解场 $u(x)$ 和参数场 $z(x)$ 都是连续函数，理论上带有无穷多个自由度，计算机不可能直接操作这样的对象。所以作者接下来的思路是，先不急着谈具体离散化方法，而是先问：如果某个候选函数不是真正的解，那么它到底“错”在哪里。这个“错”的量就是残差。把候选函数代回原方程，如果原方程没有被精确满足，剩下来的那部分就是残差。于是数值求解可以改写成：**不要直接找精确解，而是找一个函数，让它对原方程的违背尽可能小。**

接下来，作者又把这个想法往前推进一步。原始 PDE 是逐点成立的强条件，也就是你要求方程在每个位置都严格成立；但数值计算里，更自然的做法是把这个逐点条件改写成一组积分条件：先选一组测试函数，再把残差和这些测试函数相乘后积分。这就得到加权残差方法。再往前走一步，通过分部积分，就得到弱形式。弱形式的关键不是“要求更弱所以更随便”，而是它把原来对解的高阶光滑性要求放宽了，让很多更适合计算的近似函数也能被接受。到了最后，再选一组基函数，把连续函数压成有限维系数向量，forward problem 才真正变成了后面推断和优化可以处理的对象。

#### 2.2.1 PDE 离散化的统一视角：加权残差方法 (Weighted Residual Method, WRM)

作者先选了一个最标准的例子：Poisson 问题。它对应稳态扩散类物理系统，例如热传导、电势、地下水流。原文先写出边值问题本身：

$$
\nabla \cdot (z(x)\nabla u(x)) = f(x), \qquad x\in \Omega
$$

$$
u(x)=0, \qquad x\in \partial \Omega
$$

这里最好先把每个量的角色讲清楚：
- $u(x)$ 是待求的解场；
- $z(x)$ 是控制介质性质的参数场，例如扩散系数；
- $f(x)$ 是源项；
- $\Omega$ 是物理区域；
- $\partial \Omega$ 是区域边界。

这一步的关键不是“Poisson 方程长什么样”，而是：此时的 $u$ 还是一个连续函数，也就是无限维对象，所以这个问题还不能直接交给计算机。于是作者接着做第二步，把“方程要成立”改写成“残差应该为零”。

原文的残差函数定义是：

$$
R(u,z,f,x)=\nabla \cdot (z(x)\nabla u(x)) - f(x).
$$

如果某个函数 $u$ 真的是 PDE 的精确解，那么对每个 $x$ 都应该有 $R(u,z,f,x)=0$。这样一来，求解 PDE 就可以重新理解成：**找到一个近似函数，使它的残差尽量小。**

接下来作者才引入 weighted residual method。做法是：不要逐点要求残差严格为零，而是选择一组测试函数 $\{v_i\}$，把残差与它们相乘后积分，得到一组加权残差：

$$
r_i = \int_\Omega v_i(x)\,R(u,z,f,x)\,dx
= \int_\Omega v_i(x)\big(\nabla \cdot (z(x)\nabla u(x)) - f(x)\big)\,dx.
$$

这里的逻辑是：原来 PDE 是一个逐点成立的条件，现在被改写成一组积分条件。只要这些加权残差 $r_i$ 都接近零，就说明这个近似解在测试函数张成的意义下已经足够接近真实解了。

原文接着再做一步，把上式通过分部积分改写成弱形式：

$$
r_i
= \int_{\partial\Omega} v_i(x)\,(z(x)\nabla u(x))\cdot \hat n(x)\,dx
- \int_\Omega \nabla v_i(x)\cdot (z(x)\nabla u(x))\,dx
- \int_\Omega v_i(x)\,f(x)\,dx.
$$

这里最关键的不是“又做了一次代数变形”，而是：前面加权残差里最难处理的那一项是

$$
\int_\Omega v_i(x)\,\nabla \cdot (z(x)\nabla u(x))\,dx.
$$

如果保持这个写法不动，那么你实际上还在要求候选解 $u$ 至少足够光滑，能够承受一次散度算子；换句话说，二阶微分结构还压在 $u$ 身上。分部积分做的就是把这个负担重新分配。它把上面的积分改写成两部分：

$$
\int_{\partial\Omega} v_i(x)\,(z(x)\nabla u(x))\cdot \hat n(x)\,dx
\;-\;
\int_\Omega \nabla v_i(x)\cdot (z(x)\nabla u(x))\,dx.
$$

这时可以更清楚地看见导数是怎么“转移”的：
- 原来是散度 $\nabla \cdot (z\nabla u)$ 直接作用在解 $u$ 上；
- 分部积分之后，内部积分里出现的是 $\nabla v_i$，也就是导数改为作用在测试函数上；
- 解 $u$ 在内部项里只通过一阶梯度 $\nabla u$ 出现，不再直接承受那层更强的二阶微分要求。

这就是弱形式真正“弱”在哪里：不是条件变随便了，而是对候选解的光滑性要求变弱了。原来必须能逐点满足强形式 PDE 的函数，现在只要能让这些积分关系成立，就可以进入计算框架。因此，很多本来不够光滑、无法逐点解释二阶导数的近似函数，在弱形式里仍然是合法的。

边界项的出现也有明确含义。它记录的是通量 $(z\nabla u)\cdot \hat n$ 在边界上的贡献。在具体离散化里，如果边界条件和测试函数的选择合适，这一项常常会被显式处理，甚至直接消失；但它在理论上必须先保留下来，因为它正是从“体内散度”变成“边界通量 + 内部梯度配对”时自然冒出来的项。

所以这一整步真正建立的是下面这条逻辑：
- 强形式里，PDE 要逐点成立；
- 加权残差把它改成积分条件；
- 分部积分再把内部的高阶导数压力从 $u$ 身上挪开；
- 于是问题进入一个对数值近似更友好的弱形式框架。

到这里，原文真正建立起来的是一条更完整的链：
- 先有连续的 PDE 边值问题；
- 再把它改写成残差为零的问题；
- 再把残差改写成一组加权积分条件；
- 再通过分部积分得到弱形式。

这样后面无论是有限元、谱方法还是 PINNs，都可以被重新看成：**在不同的函数表示和测试函数选择下，让这些加权残差尽量小。**

到这里，原文其实已经把各种数值方法压进了同一个骨架里。真正需要选的只有两样东西：
- 你准备用什么形式来表示近似解 $u_h$；
- 你准备用什么测试函数 $v_i$ 去“检查”残差到底在哪些意义下应该接近零。

不同方法的差别，主要就落在这两处选择上：

| 方法 | 试探函数 $u_h$ | 测试函数 $v_i$ |
|------|----------------|----------------|
| 有限元 (FEM) | 分片线性帽函数展开 | 同试探函数 (Bubnov-Galerkin) |
| PINNs | 神经网络 $T_L \circ \cdots \circ T_0(x)$ | Dirac-delta 配点函数 |
| 谱方法 (Spectral) | 全局基函数展开 | 视具体方案而定 |

有限元的思路最直接：先用一组局部基函数把解场展开出来，再用同一组函数去测试残差。更具体地说，如果测试函数就是这组基函数里的每一个 $v_i$，那么你要求的是对应的加权残差

$$
r_i=\int_\Omega v_i(x)\,R(u,z,f,x)\,dx
$$

都等于零，或者在数值上足够接近零。所谓“残差对这个有限维函数空间整体上正交”，说的就是这件事：残差分别和这个空间里的每一个测试方向配对时，积分结果都消失。这里的 `Bubnov-Galerkin` 不是额外的物理假设，只是在说：试探函数和测试函数取自同一个空间。

PINNs 的写法表面上和有限元很不一样，因为近似解不再是基函数线性组合，而是一个神经网络 $T_L \circ \cdots \circ T_0(x)$。但如果放回 WRM 视角，它做的事情仍然可以理解成“选了一种特殊测试函数”：Dirac-delta 配点函数。这样一来，积分条件就退化成在若干配点上直接检查残差是否接近零。换句话说，PINNs 不是跳出了弱形式框架，而是把“如何测试残差”这一步改成了配点式检查。

谱方法又是另一种选择。它不用局部帽函数，也不用神经网络，而是直接用全局基函数来表示解。这样做通常在解本身足够光滑时很高效，因为少量全局模态就可能给出很高精度。它的测试函数怎么选，要看具体谱 Galerkin、collocation 或其他变体，所以原文在表里只写“视具体方案而定”。

这样逐个看下来，原文真正想建立的判断就清楚了：这些方法看起来形式差别很大，但在更抽象的层面上，它们都只是对同一个弱形式框架做了不同的“表示选择 + 测试选择”。

这一步对后面 VI 的作用也就变得更明确了。后面要把物理约束写进概率模型和推断目标时，真正重要的不是你此刻用的是 FEM、谱方法还是 PINNs，而是：物理系统最终都可以被压成某种残差向量 $\mathbf{r}$ 的结构。这样后面的统计建模和变分推断，就可以围绕“残差怎样进入似然、先验或生成结构”来写，而不必在推导层面被某一种特定离散化方法绑死。

#### 2.2.2 解与参数的有限维表示

有了前面的 WRM 视角，作者最后才回到真正要用于推断的有限维表示。解场和参数场都要通过某种基函数展开离散化成向量：

$$u_h(x) = \sum_{i=1}^{N_u} [\mathbf{u}]_i \phi_i(x), \quad z_h(x) = \sum_{i=1}^{N_z} [\mathbf{z}]_i \psi_i(x)$$

这一步的作用是把“函数”真正变成“参数向量”。从现在开始，后面的推断与优化不再直接在连续函数空间里做，而是在系数向量 $\mathbf{u}$ 和 $\mathbf{z}$ 上做。也正因为如此，后面出现的似然函数、后验分布、ELBO 和神经网络参数化，才都能写成有限维的概率模型与优化问题。

所以这一节如果按原文顺序压成一句话，就是：**先用 Poisson 问题说明什么叫 forward model，再用残差和弱形式统一各种数值离散化，最后把连续函数压成有限维系数向量，为后面的统计推断做准备。**

---

### 2.3 逆向问题：从点估计到贝叶斯

有了从参数到解、从解到观测的正向链条之后，原文才转到 `Section 2.2 Inverse Problems`。这一步的关键，不是简单把箭头反过来，而是把“从观测回推参数”这件事拆成两种不同的问题表述：点估计和贝叶斯逆问题。

#### 2.3.1 点估计反演 (Point Estimate Inversion)

最基本的反演是优化问题，包含数据拟合项和正则化项：

$$\mathbf{z}^\star = \arg\min_{\mathbf{z}} \frac{1}{2}\|\mathbf{y} - (H^\dagger \circ F^\dagger \circ \pi_z)(\mathbf{z})\|^2 + \frac{\beta}{2}\|\pi_z(\mathbf{z})\|^2$$

这是经典的 Tikhonov 正则化。另一种思路是用物理残差做正则化：

$$\mathbf{z}^\star = \arg\min_{\mathbf{z}} \min_{\mathbf{u}} \|\mathbf{y} - (H^\dagger \circ \pi_u)(\mathbf{u})\|^2 + \beta \|\mathbf{r}(\pi_u(\mathbf{u}); \pi_z(\mathbf{z}))\|^2$$

后者的优势在于将物理知识直接编码为约束，但 $\beta$ 需要手动调节。

#### 2.3.2 贝叶斯逆问题 (Bayesian Inverse Problems, BIPs)

当需要不确定性量化时，贝叶斯框架提供了原则性方法：

$$p(\mathbf{z}|\mathbf{y}) = \frac{p(\mathbf{y}|\mathbf{z})p(\mathbf{z})}{p(\mathbf{y})}$$

关键对应关系：

| 贝叶斯成分 | 物理含义 | 对应点估计中的角色 |
|-----------|---------|------------------|
| 似然 $p(\mathbf{y}\|\mathbf{z})$ | 正向模型 + 噪声模型 | 数据拟合项 |
| 先验 $p(\mathbf{z})$ | 参数的先验知识 | 正则化项 |
| 后验 $p(\mathbf{z}\|\mathbf{y})$ | 给定数据后参数的完整分布 | 点估计是其 MAP |
| 证据 $p(\mathbf{y})$ | 归一化常数（通常不可解析计算） | — |

这里真正卡住推断的，不是 Bayes 公式写不出来，而是分母里的证据

$$
p(\mathbf{y}) = \int p(\mathbf{y}|\mathbf{z})p(\mathbf{z})\,d\mathbf{z}
$$

往往算不出来。它要求你把所有可能参数 $\mathbf{z}$ 下的似然和先验乘积都积分一遍；一旦参数维度高、forward model 非线性、单次 PDE 求解又很贵，这个积分就会立刻变成整个问题最难的部分。

这一步一旦算不出来，后验

$$
p(\mathbf{z}|\mathbf{y}) = \frac{p(\mathbf{y}|\mathbf{z})p(\mathbf{z})}{p(\mathbf{y})}
$$

虽然在形式上已经写下来了，但在计算上还没有真正落地。也正因为这个归一化常数难算，后面才会自然分出两条经典路线：
- MCMC：不去显式算证据，而是想办法直接从后验分布采样；
- VI：不去直接得到真实后验，而是选一个可处理的近似分布族，再把后验推断改写成优化问题。

所以更准确地说，证据的不可计算性不是一个附带技术细节，而正是后面 MCMC 和 VI 这两整套推断方法存在的出发点。

---

### 2.4 变分推断：从 Bayes VI 到生成模型 ELBO

原文的 `Section 2.3 Variational Inference` 是按一条很清楚的线推进的。它先不给 ELBO，而是先把 VI 的抽象目标写出来；然后说明如果目标只是近似一个已知后验，就得到 Bayes VI；再说明如果连生成模型本身的参数也要一起学习，ELBO 会以另一种方式出现。也就是说，这一节的顺序不是“先给一个统一公式，再分情况解释”，而是：

- 先说 VI 在最抽象层面上到底是什么；
- 再说第一种情形：后验形式已知，但难算；
- 最后说第二种情形：连生成模型参数也要一起学。

#### 2.4.1 先给最抽象的 VI 目标

在最一般的层面上，VI 做的事情很简单：不直接在全部概率分布里找答案，而是先选一个可处理的分布族 $\mathcal{Q}(Z)$，再在这个较小的类里找最优近似。原文先把这件事写成

$$
q^\star(\mathbf{z}) \in \arg\min_{q\in \mathcal{Q}(Z)} J(q(\mathbf{z});\mathbf{y}),
\tag{9}
$$

其中 $\mathcal{Q}(Z)\subseteq \mathcal{P}(Z)$ 是你允许自己搜索的变分分布族。真正进入计算时，这个分布族通常还会再参数化成 $q_\phi(\mathbf{z})$，于是“在所有分布里找最优”就变成“在参数 $\phi$ 上做优化”。所以这一行的作用不是给出具体损失，而是先把整件事的框架钉死：**VI 的核心不是显式求积分，而是把推断问题改写成分布族上的优化问题。**

到这里，原文其实只完成了第一步：把推断问题写成“在一个可处理的分布族里做优化”。但这还不够，因为式子里最关键的部分还没有定下来：你到底想让这个近似分布去逼近什么，或者说，什么样的误差才算“近似得好”。

这正是目标函数 $J$ 要回答的问题。它不是一个随手选的损失，而是在决定：你准备把哪一种统计任务改写成优化问题。不同的选择，会把 VI 带到不同方向：
- 如果真实后验已经由先验和似然明确定义出来了，那么最自然的目标就是直接逼近这个后验本身；
- 如果连生成模型参数也要一起学习，那么更自然的目标就不再是“精确逼近一个已知后验”，而是“最大化模型对数据的边际解释能力”，这时 ELBO 就会作为对数证据的下界出现。

所以后面出现的 Bayes VI 和 generative-model ELBO，并不是两种彼此无关的方法，而是对同一个抽象 VI 框架做出的两种具体化：前者回答“后验已知但难算时怎么办”，后者回答“连生成模型本身也要学习时怎么办”。

这里的本质区别最好直接说清楚。两者虽然最后都能写出 ELBO 形式，但它们并不是在做同一件事：

- **Bayes VI** 的前提是：先验和似然已经给定，所以真实后验 $p(\mathbf{z}|\mathbf{y})$ 在概念上已经被定义好了。这里的 ELBO 只是把“近似一个已知但难算的后验”改写成可优化问题。也就是说，模型本身是固定的，真正要学的是近似后验。
- **generative-model VI** 的前提则更强：不仅后验难算，而且生成模型本身也还带着待学习参数。于是这里的 ELBO 不再只是“逼近一个固定后验”的技巧，而是在同时做两件事：一边学习模型参数，一边学习当前模型下的后验近似。

所以如果压成一句话，那么区别就在于：**Bayes VI 是在固定模型里近似后验；generative-model VI 是一边学模型、一边学后验。**

#### 2.4.2 Bayes VI：后验已定义，但难以直接计算

第一种情形是：模型已经给定，先验 $p(\mathbf{z})$ 和似然 $p(\mathbf{y}|\mathbf{z})$ 都已经写好了，因此真实后验

$$
p(\mathbf{z}|\mathbf{y})
$$

在概念上是明确定义的；问题只是它太难直接计算。于是最自然的想法就是：不要再发明一个新目标，而是直接让变分近似 $q_\phi(\mathbf{z})$ 去逼近真实后验本身。原文这里选择的距离就是 KL 散度：

$$
D_{\mathrm{KL}}(q(\mathbf{z})\|p(\mathbf{z}))
=
\mathbb{E}_{q(\mathbf{z})}
\left[
\log \frac{q(\mathbf{z})}{p(\mathbf{z})}
\right].
\tag{10}
$$

在 Bayes VI 里，真正要最小化的是

$$
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p(\mathbf{z}|\mathbf{y})\bigr).
$$

原文接着把 Bayes 定理代进去：

$$
p(\mathbf{z}|\mathbf{y})=\frac{p(\mathbf{y}|\mathbf{z})p(\mathbf{z})}{p(\mathbf{y})},
$$

于是

$$
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p(\mathbf{z}|\mathbf{y})\bigr)
=
\log p(\mathbf{y})
-\mathbb{E}_{q_\phi(\mathbf{z})}\bigl[\log p(\mathbf{y}|\mathbf{z})\bigr]
+\mathbb{E}_{q_\phi(\mathbf{z})}
\left[
\log \frac{q_\phi(\mathbf{z})}{p(\mathbf{z})}
\right].
\tag{11}
$$

这一步最关键的地方在于：$\log p(\mathbf{y})$ 虽然难算，但它和变分参数 $\phi$ 无关，所以在优化时它只是一个常数。于是最小化后验 KL，就等价于最小化

$$
J(\phi;\mathbf{y})
:=
\mathbb{E}_{q_\phi(\mathbf{z})}\bigl[-\log p(\mathbf{y}|\mathbf{z})\bigr]
+
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p(\mathbf{z})\bigr).
\tag{12}
$$

这时 Bayes VI 的结构就完全清楚了：

- 第一项是数据拟合项：如果某些参数 $\mathbf{z}$ 能更好解释观测 $\mathbf{y}$，那么它们会得到更低代价；
- 第二项是先验正则项：它防止 $q_\phi$ 脱离先验太远。

所以 Bayes VI 这一支真正做的是：**后验虽然难算，但仍然把“逼近真实后验”本身作为目标。**

#### 2.4.3 生成模型视角：为什么 ELBO 会再次出现

第二种情形比前一种更复杂。现在不只是后验要近似，连生成模型本身也带着待学习参数 $\theta$。也就是说，联合分布已经写成

$$
p_\theta(\mathbf{z},\mathbf{y}),
$$

你真正想做的是学习这个模型，使它能给观测数据更高的边际似然

$$
p_\theta(\mathbf{y})=\int p_\theta(\mathbf{z},\mathbf{y})\,d\mathbf{z}.
$$

此时最大的问题是：$\log p_\theta(\mathbf{y})$ 现在不再是一个和优化无关的常数，因为它本身依赖模型参数 $\theta$。所以前面 Bayes VI 那种“把证据视为常数扔掉”的做法，不能原封不动照搬。

原文先把 Bayes VI 的推导式重新整理成

$$
\log p_\theta(\mathbf{y})
=
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p_\theta(\mathbf{z}|\mathbf{y})\bigr)
+
\mathbb{E}_{q_\phi(\mathbf{z})}\bigl[\log p_\theta(\mathbf{y}|\mathbf{z})\bigr]
-
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p(\mathbf{z})\bigr).
\tag{13}
$$

这时前面那个后验 KL 不再只是“一个可以忽略的常数差”，因为它里面也有 $\theta$。但它始终非负，因此原文直接把它去掉，得到对数边际似然的一个下界：

$$
\log p_\theta(\mathbf{y})
\ge
\mathbb{E}_{q_\phi(\mathbf{z})}\bigl[\log p_\theta(\mathbf{y}|\mathbf{z})\bigr]
-
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p(\mathbf{z})\bigr)
=:
\mathcal{L}(\phi,\theta;\mathbf{y}).
\tag{14}
$$

这就是 ELBO。它和上面 Bayes VI 的目标在形式上长得一样，但逻辑地位已经变了：这里它不再与真实后验 KL 的最小化精确等价，而只是对 $\log p_\theta(\mathbf{y})$ 的一个可优化下界。

原文接着又补了一条常见推导路径：不用先写后验 KL，而是直接从边际似然出发，对

$$
\log \int p_\theta(\mathbf{z},\mathbf{y})\,d\mathbf{z}
$$

插入 $q_\phi(\mathbf{z})$，再用 Jensen 不等式，就能得到

$$
\log p_\theta(\mathbf{y})
=
\log
\mathbb{E}_{q_\phi(\mathbf{z})}
\left[
\frac{p_\theta(\mathbf{z},\mathbf{y})}{q_\phi(\mathbf{z})}
\right]
\ge
\mathbb{E}_{q_\phi(\mathbf{z})}
\left[
\log \frac{p_\theta(\mathbf{z},\mathbf{y})}{q_\phi(\mathbf{z})}
\right],
\tag{15-16}
$$

最后同样落到

$$
\mathcal{L}(\phi,\theta;\mathbf{y})
=
\mathbb{E}_{q_\phi(\mathbf{z})}\bigl[\log p_\theta(\mathbf{y}|\mathbf{z})\bigr]
-
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z})\|p(\mathbf{z})\bigr).
\tag{17}
$$

所以在 generative-model 这条线上，ELBO 的角色是：**用一个可优化的下界去同时学习生成模型参数 $\theta$ 和变分近似参数 $\phi$。**

#### 2.4.4 为什么这两条线不能混成一个“统一公式”

这两部分最容易让人混淆，因为最后都写出了很像的两项式目标：

$$
\mathbb{E}_{q}[-\log p(\mathbf{y}|\mathbf{z})]
+
D_{\mathrm{KL}}(q\|p(\mathbf{z})).
$$

但原文真正强调的是：**形式相似，不代表逻辑完全一样。**

在 Bayes VI 里：
- 模型已经给定；
- 只优化 $\phi$；
- $\log p(\mathbf{y})$ 对优化来说是常数；
- 因而最小化目标与最小化真实后验 KL 是精确等价的。

在 generative-model VI 里：
- 生成模型参数 $\theta$ 也要一起学；
- $\log p_\theta(\mathbf{y})$ 会随 $\theta$ 变化；
- 所以 ELBO 只是边际似然的下界；
- 优化它是在同时学习生成模型和近似后验。

把这一区分放回物理问题里，最直接的判断办法其实是先问：**在你的问题里，到底什么已经固定好了，什么还没有固定？**

第一种情况是：物理正向模型已经给定了。也就是说，参数 $\mathbf{z}$ 怎样映射到观测 $\mathbf{y}$，这条链本身已经由 PDE、数值求解器和噪声模型写清楚了。此时真正未知的，不是生成机制本身，而只是“给定数据以后，参数的后验分布长什么样”。在这种设定下，你要做的核心任务就是近似一个已经定义好的后验，因此更接近 Bayes VI 的语境。

第二种情况是：连生成结构本身也还没有固定。比如正向映射的一部分需要由神经网络学习，或者整个隐变量生成模型 $p_\theta(\mathbf{z},\mathbf{y})$ 都带着待估参数 $\theta$。这时问题就不再只是“后验难算”，而是“模型本身也要一起学”。因此优化目标自然会转成提高边际似然 $\log p_\theta(\mathbf{y})$，而你手里真正可用的是它的下界，也就是 generative-model ELBO 的语境。

所以这里的分界点不是“有没有潜变量”，也不是“是不是用了神经网络”，而是：**你是在一个已经给定的物理-统计模型里近似后验，还是在一边学习生成模型、一边学习近似后验。**

---

### 2.5 深度学习参数化：VAE 与 Normalizing Flows

原文在 `Section 2.3` 里并没有停在抽象 ELBO 上，而是立刻把这套形式接到现代深度学习参数化上。这样做的目的，是把前面那套变分目标和后面 physics-informed generative modelling 文献里的具体模型接口接起来。

#### 2.5.1 变分自编码器 (Variational Autoencoder, VAE)

VAE 是 ELBO 框架的标准深度学习实现，由两个神经网络组成：

- **编码器 (Encoder)** $q_\phi(\mathbf{z}|\mathbf{y}) = \mathcal{N}(\mathbf{z}; m_\phi(\mathbf{y}), C_\phi(\mathbf{y}))$：将数据映射为潜变量的分布
- **解码器 (Decoder)** $p_\theta(\mathbf{y}|\mathbf{z}) = \mathcal{N}(\mathbf{y}; G_\theta(\mathbf{z}), C_\eta)$：从潜变量生成数据

对 $N$ 个数据点，假设各数据点独立，ELBO 分解为逐样本的加和：

$$
\log p_\theta(\mathbf{y}^{(1:N)}) \geq \sum_{n=1}^{N} \underbrace{\mathbb{E}_{q_\phi(\mathbf{z}|\mathbf{y}^{(n)})}[\log p_\theta(\mathbf{y}^{(n)}|\mathbf{z})]}_{\text{reconstruction error}} - \underbrace{D_\text{KL}(q_\phi(\mathbf{z}|\mathbf{y}^{(n)}) \| p(\mathbf{z}))}_{\text{regularisation}}.
$$

这条式子最容易被压扁成一句“VAE 就是重构项加 KL 项”，但原文这里其实在区分两种完全不同的作用。

先看第一项，也就是 `reconstruction error`。名字虽然叫“重构误差”，但它在公式里其实写成的是

$$
\mathbb{E}_{q_\phi(\mathbf{z}|\mathbf{y}^{(n)})}[\log p_\theta(\mathbf{y}^{(n)}|\mathbf{z})].
$$

它真正问的是：如果先用编码器 $q_\phi(\mathbf{z}|\mathbf{y}^{(n)})$ 把数据点 $\mathbf{y}^{(n)}$ 映到潜变量分布，再从这个潜变量分布里取样，那么解码器 $p_\theta(\mathbf{y}^{(n)}|\mathbf{z})$ 能不能把原来的数据点解释回来。这个量越大，说明潜变量 $\mathbf{z}$ 越能保留与数据重建有关的信息；如果它太小，就说明编码器把数据压进潜空间之后丢掉了太多内容，解码器已经很难把原始样本恢复出来。

再看第二项，也就是 `regularisation`：

$$
D_\text{KL}(q_\phi(\mathbf{z}|\mathbf{y}^{(n)}) \| p(\mathbf{z})).
$$

它不再关心“能不能把这一个样本重建好”，而是在问：针对这个样本学出来的后验近似，是否偏离预先指定的潜变量先验太远。这个项的作用是把不同样本对应的潜变量分布约束在一个共同的潜空间几何里，而不是让编码器为每个样本都随意开辟一个彼此毫无关系的局部编码区域。换句话说，它在管的是**潜空间是否保持规整、可采样、可泛化**。

这两项必须同时出现，原因也正好对应 VAE 的两个目标：
- 如果只保留第一项，模型会一味追求把训练样本重建好，潜变量分布很容易变得杂乱无章；
- 如果只保留第二项，潜空间虽然会贴近先验，但编码器和解码器就可能学不到足够的样本信息。

所以原文这里真正想让读者看到的是：`Eq. (18)` 不是简单把一个损失拆成两块，而是在明确区分
- 数据内容是否被保留下来；
- 潜空间结构是否被约束住。

前者对应 reconstruction，后者对应 regularisation；VAE 正是靠这两股力量的平衡，才同时得到“可重建的数据表示”和“可采样的潜空间结构”。

#### 2.5.2 重参数化技巧 (Reparameterisation Trick)

训练 VAE 时，真正要优化的是 ELBO 对变分参数 $\phi$ 的梯度。但这里马上会遇到一个计算上的卡点：ELBO 里面有对

$$
\mathbf{z}\sim q_\phi(\mathbf{z}|\mathbf{y})
$$

的采样，而这个采样步骤本身不是一个普通的可微函数。也就是说，如果你把“先根据 $q_\phi$ 采一个 $\mathbf{z}$，再把它送进解码器”当成黑箱流程，那么随机采样这一步会把梯度链条截断，反向传播就很难直接穿过去。

重参数化技巧做的事情，就是把这一步重新写成“先采一个和参数无关的标准噪声，再用可微变换把它变成目标样本”。原文这里对应的是高斯后验近似，所以先取

$$
\epsilon \sim \mathcal{N}(0,\mathrm{I}),
$$

然后再定义

$$
\mathbf{z}=m_\phi(\mathbf{y})+L_\phi(\mathbf{y})\odot \epsilon.
$$

这样写以后，随机性就不再直接绑在参数 $\phi$ 上，而是全部放进了外部噪声变量 $\epsilon$ 里。对当前数据点 $\mathbf{y}$ 来说，真正带参数的部分只剩下
- 均值函数 $m_\phi(\mathbf{y})$；
- 协方差因子或尺度项 $L_\phi(\mathbf{y})$。

这时从计算图角度看，$\mathbf{z}$ 已经变成了一个关于 $m_\phi(\mathbf{y})$、$L_\phi(\mathbf{y})$ 和噪声 $\epsilon$ 的显式可微函数。训练时你仍然会先采样，但采样发生在参数无关的 $\epsilon$ 上；一旦 $\epsilon$ 固定，后面的

$$
\mathbf{z}=m_\phi(\mathbf{y})+L_\phi(\mathbf{y})\odot \epsilon
$$

就是普通的可微映射，因此梯度就能沿着

$$
\mathbf{z}\rightarrow m_\phi(\mathbf{y}),\,L_\phi(\mathbf{y})
$$

这条路径反向传播回去。

所以这一步真正解决的不是“如何重新定义高斯分布”，而是：**如何把原来卡在随机采样上的梯度问题，改写成一个参数外部采噪声、参数内部做可微变换的问题。**

#### 2.5.3 Normalizing Flows

Normalizing Flows 的出发点和 VAE 很不一样。它不是先假设一个简单的变分分布，再用编码器去输出均值和协方差；它的思路是：先从一个最简单、最容易采样的基础分布开始，例如标准高斯 $p(\mathbf{w})$，然后用一系列可逆变换把这个简单分布一步步推成复杂目标分布。

原文把这件事写成

$$
\mathbf{z}=f_\phi(\mathbf{w}),
\qquad
q_\phi(\mathbf{z})=p(\mathbf{w})\left|\det \frac{\partial f_\phi^{-1}}{\partial \mathbf{z}}\right|.
$$

这两行里最重要的是“可逆”这件事。因为 $f_\phi$ 可逆，所以你不仅能从 $\mathbf{w}$ 正向生成 $\mathbf{z}$，还能从 $\mathbf{z}$ 反过来找回对应的 $\mathbf{w}=f_\phi^{-1}(\mathbf{z})$。密度公式里的 Jacobian 行列式，记录的正是这个可逆变换在局部把体积拉伸或压缩了多少。也就是说，flow 不只是给你一个采样过程，还同时给你一个精确的密度变换公式。原文想强调的优势就来自这里：**因为变换是可逆的，密度 $q_\phi(\mathbf{z})$ 可以被精确写出来，而不只是近似估计。**

这也解释了它相对 VAE 的优点。VAE 里我们通常能从编码器和解码器采样，但变分分布和生成分布的表达能力往往受高斯假设限制；而 flow 可以通过一串可逆映射，把一个简单分布逐步扭曲成非常复杂的形状，同时密度仍然是可计算的。

但这个优点也带来限制。因为整个变换必须可逆，所以输入和输出的维度必须一致。换句话说，你不能把一个高维变量通过可逆映射真正压缩成一个更低维潜变量；一旦维度变了，双向一一对应关系就不存在了。这就是为什么原文会特别指出：Normalizing Flows 很擅长表达复杂分布，但它们不天然适合做降维式潜空间学习。

最后原文才回到物理逆问题里最相关的版本：条件 Normalizing Flows。这里学习的不是无条件分布 $q_\phi(\mathbf{z})$，而是条件后验近似

$$
q_\phi(\mathbf{z}|\mathbf{y}).
$$

这时观测 $\mathbf{y}$ 进入 flow 结构里，起到“条件化”作用。直观上，这表示：面对不同的观测数据，flow 会把同一个简单基础噪声分布扭曲成不同的后验分布。也正因为它既能采样、又能精确写密度，条件 NF 在物理逆问题里就特别适合做后验近似：你既能从近似后验中抽样看不确定性，又能把它放回变分目标里做严格优化。

这里可以把逻辑再拆得更细一点。条件化之前，flow 做的是：从一个固定的简单基础分布出发，例如标准高斯噪声，然后通过可逆映射把它变成一个复杂分布。条件化之后，简单基础分布本身并没有变，变的是这条可逆映射会随着观测 $\mathbf{y}$ 改变。也就是说，面对不同的观测数据，模型不会重新换一个新的噪声源，而是让“同一份基础噪声”经过不同的、由 $\mathbf{y}$ 控制的扭曲方式，最后生成不同的后验分布形状。

这样做有两个直接结果。第一，它仍然保留了 flow 的采样优势：你想看后验不确定性时，只需要先从简单噪声分布里采样，再通过条件 flow 把这些样本推到参数空间，就能得到近似后验样本。第二，它也保留了 flow 的密度优势：因为这条变换仍然是可逆的，所以每个样本对应的条件密度 $q_\phi(\mathbf{z}|\mathbf{y})$ 仍然可以用 Jacobian 精确写出来，而不是只能做黑箱采样。

这正好对应逆问题里最想同时得到的两样东西：
- 一方面，你希望能从后验里抽样，看看给定观测之后参数还有哪些不确定性；
- 另一方面，你又希望这个近似后验的密度本身是可计算的，这样它才能被放回 KL 散度、ELBO 或其他变分目标里，作为一个真正可优化的对象。

所以条件 NF 在物理逆问题里的价值，不只是“它能生成复杂后验”，而是：**它把后验近似同时做成了一个可采样对象和一个可计算密度对象。** 前者让你能做不确定性分析，后者让你能把它稳当地纳入变分推断框架。

---

## 3. Physics-Informed Generative Models

论文将文献中的方法按物理约束嵌入方式分为两大类，这是全文最有综述价值的部分。

### 3.1 路线一：基于正向模型的方法 (Forward-Model-Based)

这一类方法共享同一个前提：**正向物理模型仍然可以调用。** 它也许很贵，但至少对给定参数 $\mathbf{z}$，你还能把它送进真实物理求解器 $G^\dagger$，得到相应的观测输出 $\mathbf{y}$。一旦这个前提成立，最自然的做法就是把正向模型直接嵌进概率生成结构里，让似然项本身就带着真实物理映射。

因此，这一整节的主线不是“如何完全替代物理模型”，而是：**在正向模型仍可评估的前提下，怎样学习一个从观测到参数的概率逆映射。** 原文接下来按 `Eq. (19)–(26)` 依次给出三种代表路线：
- 先是有监督情形下如何直接学习校准后的后验；
- 再是时间序列里怎样把动力学结构压进潜空间；
- 最后是参数空间很高维时，怎样先学一个深度生成先验，再在低维辅助空间里做反演。

#### 3.1.1 有监督 VAE 获取校准后验

第一种情形最直接：你手里已经有输入-输出配对数据

$$
\mathcal{D}=\{(\mathbf{z}^{(n)},\mathbf{y}^{(n)})\}_{n=1}^N.
$$

也就是说，每个观测 $\mathbf{y}$ 都对应一组已知参数 $\mathbf{z}$。在这种有监督设定下，原文强调可以直接用 **forward KL**

$$
D_{\mathrm{KL}}\bigl(p(\mathbf{z}|\mathbf{y})\|q_\phi(\mathbf{z}|\mathbf{y})\bigr)
$$

来训练后验近似。它和 VAE 里常见的 reverse KL 不一样：forward KL 是 mean-seeking 的，更倾向于覆盖真实后验的整个高概率区域，因此对逆问题里“需要校准不确定性”的场景更自然。

这里最容易误解的一点是：即使你手里有很多输入-输出配对样本 $(\mathbf{z}^{(n)},\mathbf{y}^{(n)})$，也不等于你已经知道了每一个具体观测 $\mathbf{y}$ 对应的真实后验 $p(\mathbf{z}|\mathbf{y})$。样本对只能告诉你 joint distribution 里出现了哪些组合，但后验是一个条件分布对象：它要求你知道“在固定这一个观测 $\mathbf{y}$ 之后，参数 $\mathbf{z}$ 的完整概率密度到底长什么样”。这件事通常仍然需要对贝叶斯公式做条件化和归一化，而这些正是逆问题里最难显式写出的部分。

所以这里的困难不是“没有数据”，而是：**有 joint samples，不等于有单个观测条件下的完整后验密度。** 原文接下来的关键一步，就是不再试图逐点恢复每一个 $\mathbf{y}$ 下的真实后验，而是把这个 forward KL 先对数据分布取平均。这样一来，目标就能改写成只依赖 joint samples 的形式：

$$
\mathbb{E}_{p(\mathbf{y})}
\left[
D_{\mathrm{KL}}\bigl(p(\mathbf{z}|\mathbf{y})\|q_\phi(\mathbf{z}|\mathbf{y})\bigr)
\right]
=
\mathbb{E}_{p(\mathbf{z},\mathbf{y})}
\left[
-\log q_\phi(\mathbf{z}|\mathbf{y})
\right].
\tag{19}
$$

这一步最好按三层来读。第一层，先把左边的 averaged forward KL 展开：

$$
\mathbb{E}_{p(\mathbf{y})}
\left[
D_{\mathrm{KL}}\bigl(p(\mathbf{z}|\mathbf{y})\|q_\phi(\mathbf{z}|\mathbf{y})\bigr)
\right]
=
\mathbb{E}_{p(\mathbf{y})}
\left[
\mathbb{E}_{p(\mathbf{z}|\mathbf{y})}
\left[
\log p(\mathbf{z}|\mathbf{y})-\log q_\phi(\mathbf{z}|\mathbf{y})
\right]
\right].
$$

第二层，把这两个嵌套期望合并成 joint distribution 下的期望：

$$
=
\mathbb{E}_{p(\mathbf{z},\mathbf{y})}
\left[
\log p(\mathbf{z}|\mathbf{y})-\log q_\phi(\mathbf{z}|\mathbf{y})
\right].
$$

第三层，注意这里第一项

$$
\mathbb{E}_{p(\mathbf{z},\mathbf{y})}\bigl[\log p(\mathbf{z}|\mathbf{y})\bigr]
$$

虽然一般也算不出来，但它和变分参数 $\phi$ 无关，所以在优化时只是一个常数。也就是说，从“关于 $\phi$ 的优化目标”来看，上式等价于最小化

$$
\mathbb{E}_{p(\mathbf{z},\mathbf{y})}
\left[
-\log q_\phi(\mathbf{z}|\mathbf{y})
\right].
$$

所以更严格地说，`Eq. (19)` 代表的是：**平均 forward KL 对 $\phi$ 的优化，可以等价地改写成 joint samples 下的监督负对数似然目标。** 原文把那个与 $\phi$ 无关的常数项压掉了，因此最后写成了现在这个更紧凑的形式。

这一步的意义很大。它说明：虽然你不能逐点计算每个 $\mathbf{y}$ 下的真实后验，但只要能从 joint distribution 里拿到样本对 $(\mathbf{z},\mathbf{y})$，就可以把训练目标改写成一个可直接对数据做平均的监督损失。

原文接着给出第一种具体实现：[60] 用 **conditional normalizing flow** 来参数化 $q_\phi(\mathbf{z}|\mathbf{y})$。这一步最好顺着 `Eq. (19)` 往下推，而不要把 `Eq. (20)` 当成一个突然冒出来的 flow loss。真正的逻辑顺序是四步。

第一步，先把监督目标钉死。前面已经说明，训练时真正要最小化的是

$$
\mathbb{E}_{p(\mathbf{z},\mathbf{y})}
\left[
-\log q_\phi(\mathbf{z}|\mathbf{y})
\right].
$$

所以这里最关键的问题不是“网络长什么样”，而是：**怎样把条件密度 $q_\phi(\mathbf{z}|\mathbf{y})$ 写成一个既能采样、又能精确计算密度的对象。**

第二步，先回答训练样本从哪里来。因为这里属于 forward-model-based learning，所以 joint samples 不是从真实后验里拿，而是直接由已知物理 forward model 合成。具体地说，先从参数先验采样

$$
\mathbf{z}^{(n)}\sim p(\mathbf{z}),
$$

再通过真实正向模型 $G^\dagger$ 和噪声模型生成观测：

$$
\mathbf{y}^{(n)}\sim \mathcal{N}(G^\dagger(\mathbf{z}^{(n)}),\sigma^2\mathrm{I}).
$$

这样得到的样本对 $(\mathbf{z}^{(n)},\mathbf{y}^{(n)})$ 就来自 joint distribution $p(\mathbf{z},\mathbf{y})$，正好可以直接放进上面的 averaged forward-KL 监督目标里。

第三步，才轮到条件 flow 的参数化。这里的思路是：对每个给定观测 $\mathbf{y}$，都用一个依赖于 $\mathbf{y}$ 的可逆映射，把复杂的后验参数分布拉回一个简单的标准高斯变量 $\mathbf{w}$。也就是说，模型假设

$$
\mathbf{z}=f_\phi(\mathbf{w};\mathbf{y}),
\qquad
\mathbf{w}\sim \mathcal{N}(0,\mathrm{I}).
$$

一旦这样写，条件密度 $q_\phi(\mathbf{z}|\mathbf{y})$ 就不再是抽象的“近似后验”，而能通过换元公式精确写成

$$
q_\phi(\mathbf{z}|\mathbf{y})
=
\mathcal{N}(f_\phi^{-1}(\mathbf{z};\mathbf{y});0,\mathrm{I})
\left|
\det \partial_{\mathbf{z}} f_\phi^{-1}(\mathbf{z};\mathbf{y})
\right|.
$$

第四步，把这个具体的条件密度代回 `Eq. (19)`。这时负对数密度会自动拆成两部分。先看高斯项：因为基础分布是标准高斯，所以

$$
-\log \mathcal{N}(f_\phi^{-1}(\mathbf{z};\mathbf{y});0,\mathrm{I})
$$

会给出一个二次能量项

$$
\frac{1}{2}\|f_\phi^{-1}(\mathbf{z};\mathbf{y})\|_2^2.
$$

再看换元带来的 Jacobian 项：它记录的是这个可逆映射在局部把体积拉伸或压缩了多少，所以会给出

$$
-\log \det \left| \partial_{\mathbf{z}} f_\phi^{-1}(\mathbf{z};\mathbf{y}) \right|.
$$

于是，`Eq. (19)` 里的监督负对数似然就被具体化成“二次能量 + Jacobian 修正”的 joint expectation，最后得到原文的训练目标：

$$
\phi^\star=\arg\min_\phi J(\phi;\mathbf{y}),
\qquad
J(\phi;\mathbf{y})
=
\mathbb{E}_{p(\mathbf{z},\mathbf{y})}
\left[
\frac{1}{2}\|f_\phi^{-1}(\mathbf{z};\mathbf{y})\|_2^2
-\log \det \left| \partial_{\mathbf{z}} f_\phi^{-1}(\mathbf{z};\mathbf{y}) \right|
\right].
\tag{20}
$$

所以 `Eq. (20)` 真正表达的是：**先用真实 forward model 造 joint samples，再用 conditional flow 给后验近似选一个可逆参数化，最后把这个参数化代回 `Eq. (19)`。** 它的逻辑顺序是：

$$
p(\mathbf{z},\mathbf{y})\ \text{可采样}
\;\longrightarrow\;
q_\phi(\mathbf{z}|\mathbf{y})\ \text{用条件 flow 表示}
\;\longrightarrow\;
-\log q_\phi(\mathbf{z}|\mathbf{y})\ \text{化成二次项 + Jacobian 项}
\;\longrightarrow\;
J(\phi;\mathbf{y}).
$$

这其实就是 `Eq. (19)` 在条件 NF 参数化下的具体化：第一项来自把样本拉回标准高斯后的二次能量，第二项来自可逆变换的 Jacobian 修正。训练完成后，对一个新的观测 $\mathbf{y}$，你只需要采样

$$
\mathbf{w}\sim \mathcal{N}(0,\mathrm{I}),
$$

再通过训练好的条件 flow 推过去：

$$
\mathbf{z}=f_{\phi^\star}(\mathbf{w};\mathbf{y}),
$$

就能得到近似后验样本。

原文紧接着又给出第二种代表思路：[20] 把 VAE 的解码器直接换成已知物理 forward model。这里的逻辑和前一个方法不一样，所以也最好顺着原文的次序一层一层读。

第一步，先看它和 conditional NF 的分工差别。前一个方法是：**直接为后验近似 $q_\phi(\mathbf{z}|\mathbf{y})$ 选一个足够灵活的条件可逆分布族，然后用监督样本去拟合它。** 这里则换了一种思路：**不把主要精力放在“后验近似族够不够灵活”上，而是先把生成模型本身做得更物理。** 具体做法就是把 VAE 里原本可学习的 decoder，直接替换成已知的物理 forward model。

第二步，先把这个“物理化的生成模型”写出来。作者假设观测是由真实 forward model $G^\dagger$ 加上噪声产生的，因此数据模型写成

$$
\mathbf{y}\sim \mathcal{N}(G^\dagger(\mathbf{z})+m_\epsilon,C_\epsilon),
$$

这条式子的意思是：给定参数 $\mathbf{z}$ 之后，观测均值不再由一个任意神经网络 decoder 给出，而是直接由物理模型 $G^\dagger(\mathbf{z})$ 给出；噪声的偏置和协方差则由 $m_\epsilon$、$C_\epsilon$ 控制。这样一来，物理规律不是事后加进去的 regularizer，而是一开始就放在生成结构里。

第三步，再看后验近似怎么选。这里编码器仍然输出一个高斯近似后验：

$$
q_\phi(\mathbf{z}|\mathbf{y})=\mathcal{N}(m_\phi(\mathbf{y}),C_\phi(\mathbf{y})).
$$

所以这条路线不是像 flow 那样靠可逆映射去构造一个复杂条件密度，而是保留了 VAE 式的 encoder 结构，只不过 decoder 这一侧已经被真实物理模型接管了。

第四步，原文接着解释为什么这里还要引入一个比普通 reverse KL 更细的目标。原因是：如果只用单一一种 KL，优化往往会偏向某一侧的极端行为。这里最好把前面那句缩写判断重新拆开。所谓 **forward KL 更偏平均、mode-covering**，说的是：当真实后验 $p(\mathbf{z}|\mathbf{y})$ 在多个区域都有概率质量时，最小化

$$
D_{\mathrm{KL}}(p\|q)
$$

会强迫近似分布 $q$ 在这些区域都给出足够概率；因为只要某个真实高概率区域被 $q$ 漏掉，惩罚就会很大，所以它倾向把多个 mode 都一起覆盖进去。相反，**reverse KL 更偏 mode-seeking**，说的是：最小化

$$
D_{\mathrm{KL}}(q\|p)
$$

时，惩罚主要来自“$q$ 把概率放到了 $p$ 很小的地方”。于是最省事的做法往往不是把所有 mode 都顾到，而是先集中到一个最容易解释、最安全的高概率区域里。也就是说：

- forward KL 更担心“真实后验里的质量被漏掉”；
- reverse KL 更担心“近似后验把质量放错地方”。

作者正是想在这两种倾向之间保留一个可调折中，于是引入加权 Jensen-Shannon divergence：

$$
\mathrm{JS}_\alpha(q\|p)
=
\alpha D_{\mathrm{KL}}(q\|(1-\alpha)q+\alpha p)
+(1-\alpha)D_{\mathrm{KL}}(p\|(1-\alpha)q+\alpha p).
\tag{21}
$$

这条式子可以这样读：它不是直接拿 $q$ 和 $p$ 硬碰硬，而是先构造一个中间混合分布 $(1-\alpha)q+\alpha p$，再分别测量 $q$ 和 $p$ 到这个中间分布的偏离。$\alpha$ 决定的是：这个中间分布更靠近哪一边，以及最终目标更偏向哪一侧。

第五步，才把这个加权 JS 和标准 reverse KL 组合成最终训练目标：

$$
\phi^\star
=
\arg\min_\phi J(\phi;\alpha,\mathbf{y}),
\qquad
J(\phi;\alpha,\mathbf{y})
=
\frac{1}{\alpha}\mathrm{JS}_\alpha\bigl(q_\phi(\mathbf{z}|\mathbf{y})\|p(\mathbf{z}|\mathbf{y})\bigr)
+
D_{\mathrm{KL}}\bigl(q_\phi(\mathbf{z}|\mathbf{y})\|p(\mathbf{z}|\mathbf{y})\bigr).
\tag{22}
$$

这里的逻辑不是“又多加了一项损失”，而是：作者想同时保留两件事。一件事是 reverse KL 带来的稳定变分训练框架；另一件事是利用加权 JS，在 forward-KL 和 reverse-KL 之间保留一条可调通道。于是 $\alpha$ 的作用也不再只是一个技巧超参数，而是在调节数据拟合和正则化之间的平衡。原文给出的判断是：这种插值式目标有助于避免后验方差被推到过小或过大的极端。

最后一步，作者再补了一个实际上的让步：如果真实的物理 forward model 太贵，连把它直接塞进 decoder 都承受不起，那么可以再用一个 surrogate decoder 去近似这条物理映射。这样做虽然退回到“物理模型 + 代理模型”的折中结构，但整体思路不变：**decoder 这一侧仍然尽量保持物理一致，而不是完全交给一个黑箱生成器。**

#### 3.1.2 动力学潜空间 (Dynamical Latent Space)

第二条路线把问题推进到时间序列。现在观测不再是单个 $\mathbf{y}$，而是一段时间索引数据

$$
\mathbf{y}_{1:N}=\{\mathbf{y}_n\}_{n=1}^N.
$$

如果仍然只用一个静态 latent code 去解释整段序列，那么模型能表达的是“这一串数据大致属于哪一类”，却很难表达“这串数据是怎样一步一步演化出来的”。也就是说，单个全局 latent 适合压缩整段序列的整体信息，却不适合显式承载动力学。于是原文转向 **dynamical latent space**：不是只给整段序列配一个隐变量，而是让潜空间本身沿时间 obey 某种物理演化规律。

这一步的核心做法，是在真实观测和真正的潜在动力学之间插入一层中间变量。在 [19] 里，作者引入辅助变量 $\mathbf{x}_n$，把它当成 latent Gaussian state-space model 的伪观测。这样模型里就有了三层对象：

1. 最外层是真正观测到的数据 $\mathbf{y}_{1:N}$；
2. 中间层是伪观测 $\mathbf{x}_{1:N}$，它负责承接“观测空间”和“动力学空间”之间的映射；
3. 最内层是 latent state $\mathbf{u}_{1:N}$，它才真正 obey 物理 one-step operator。

这样分层之后，作者就能把“如何重建观测”和“如何 obey 动力学”拆开处理。观测重建这一层由 probabilistic decoder 负责：从 $\mathbf{x}_n$ 重建 $\mathbf{y}_n$。动力学这一层则由一条显式的状态转移来负责。这里的 **one-step operator** 可以先按最朴素的方式理解：如果你已经知道系统在上一个时刻的状态，那么物理模型会告诉你“下一小步最应该走到哪里”。也就是说，它不是在问整条轨迹最终长什么样，而是在问：

- 给定当前状态；
- 再给定控制动力学的参数 $\mathbf{z}$；
- 下一时刻的状态均值应该被推进到哪里。

这就是 “one-step” 这个名字的来历：它只负责 **从一步到下一步** 的局部推进。在连续动力学里，你可以把它理解成“把微分方程沿一个小时间步积分一次”；在离散动力学里，你可以把它理解成“上一时刻状态经过一次演化更新后得到的下一时刻状态”。原文把这条局部推进规则记成 $\Psi^\dagger$，于是 latent state 不是随意跳动，而是要围绕这条物理一步推进规律演化。对应的 latent dynamics 写成

$$
p(\mathbf{u}_n|\mathbf{u}_{n-1})
=
\mathcal{N}(\Psi^\dagger(\mathbf{u}_{n-1};\mathbf{z}),\sigma_{\mathbf{u}}^2\mathrm{I}).
$$

这条式子最好再按两层来读。第一层，均值

$$
\Psi^\dagger(\mathbf{u}_{n-1};\mathbf{z})
$$

给出的就是“如果完全按照物理一步推进规则走，下一时刻最应该到哪里”。第二层，协方差

$$
\sigma_{\mathbf{u}}^2\mathrm{I}
$$

表示模型并不强迫 $\mathbf{u}_n$ 严格等于这个物理解，而是允许它围绕这条物理推进做有限的随机波动。这样一来，动力学结构就不是被软性地当成一个事后惩罚项，而是直接写进了 latent 状态转移本身。

在这个结构下，真正关键的就变成：变分后验到底怎么分解。原文这里没有把所有隐变量都交给一个大而全的 encoder，而是故意保留一部分精确结构，写成

$$
q(\mathbf{u}_{1:N},\mathbf{x}_{1:N},\mathbf{z}|\mathbf{y}_{1:N})
\propto
p(\mathbf{u}_{1:N}|\mathbf{x}_{1:N})
\,q_\phi(\mathbf{x}_{1:N}|\mathbf{y}_{1:N})
\,q_\vartheta(\mathbf{z}).
\tag{23}
$$

这条分解的逻辑可以按三步读。第一步，把伪观测 $\mathbf{x}_{1:N}$ 的编码工作交给 amortized encoder $q_\phi(\mathbf{x}_{1:N}|\mathbf{y}_{1:N})$。第二步，把全局参数 $\mathbf{z}$ 的不确定性单独交给 $q_\vartheta(\mathbf{z})$。第三步，也是最关键的一步：把 $\mathbf{u}_{1:N}$ 这一层留给

$$
p(\mathbf{u}_{1:N}|\mathbf{x}_{1:N})
$$

这个精确可处理的后验，而不是再用一个神经网络去硬近似它。原文的判断很明确：**能精确处理的那部分，就不要再额外引入近似误差。** 这里 $p(\mathbf{u}_{1:N}|\mathbf{x}_{1:N})$ 属于线性高斯状态空间模型的精确后验，因此可以直接用 Kalman filtering / smoothing 来算。

在这种“部分神经网络、部分精确推断”的分工下，原文得到的 ELBO 是

$$
\begin{aligned}
J(\theta,\phi,\vartheta;\mathbf{y}_{1:N})
=\;&
\sum_n
\mathbb{E}_{q_\phi(\mathbf{x}_n|\mathbf{y}_n)}
\left[
\log \frac{p_\theta(\mathbf{y}_n|\mathbf{x}_n)}{q_\phi(\mathbf{x}_n|\mathbf{y}_n)}
\right] \\
&+
\mathbb{E}_{q_\phi(\mathbf{x}_{1:N}|\mathbf{y}_{1:N})q_\vartheta(\mathbf{z})}
\bigl[\log p(\mathbf{x}_{1:N}|\mathbf{z})\bigr]
-
D_{\mathrm{KL}}\bigl(q_\vartheta(\mathbf{z})\|p(\mathbf{z})\bigr).
\end{aligned}
\tag{24}
$$

这条 ELBO 最好不要只看成“三项并列”，而要按它们各自守住哪一层结构来读。

第一项

$$
\sum_n
\mathbb{E}_{q_\phi(\mathbf{x}_n|\mathbf{y}_n)}
\left[
\log \frac{p_\theta(\mathbf{y}_n|\mathbf{x}_n)}{q_\phi(\mathbf{x}_n|\mathbf{y}_n)}
\right]
$$

管的是“观测 $\leftrightarrow$ 伪观测”这层：它要求编码器给出的 $\mathbf{x}_n$ 仍然足以重建真实观测 $\mathbf{y}_n$。第二项

$$
\mathbb{E}_{q_\phi(\mathbf{x}_{1:N}|\mathbf{y}_{1:N})q_\vartheta(\mathbf{z})}
\bigl[\log p(\mathbf{x}_{1:N}|\mathbf{z})\bigr]
$$

管的是整段时间序列的动力学一致性：给定全局参数 $\mathbf{z}$ 以后，这一整段伪观测轨迹 $\mathbf{x}_{1:N}$ 是否真的像某条由 latent dynamics 生成出来的序列。第三项

$$
-D_{\mathrm{KL}}\bigl(q_\vartheta(\mathbf{z})\|p(\mathbf{z})\bigr)
$$

则继续扮演全局参数正则化的角色，防止 $\mathbf{z}$ 的后验近似脱离先验太远。

所以这一小节真正展示的，不是“把时间序列塞进 VAE”这么简单，而是：**一旦数据本身带有演化结构，forward-model-based learning 就可以从“把单个 forward model 放进似然”进一步走到“把 physical one-step operator 直接嵌进潜空间动力学”。** 原文最后还提到另一种相关思路：[39] 通过把 latent embeddings 约束到非欧几里得流形上，也是在做同一件事：让潜空间本身更像真实动力学发生的几何空间，而不只是一个任意的欧氏编码容器。

#### 3.1.3 深度生成先验 (Deep Generative Prior, DGP)

第三条路线处理的是另一个常见难点：**参数空间本身太高维。** 即使 forward model 可评估，直接在高维参数 $\mathbf{z}$ 上做反演也往往非常不稳定。这时最自然的第一反应通常是：“那我是不是应该换一个更强的推断算法？” 例如，把后验近似做得更灵活，或者把优化过程设计得更复杂。原文这里故意没有先走这条路，而是先回到更前面的一步：**也许真正的问题，不在‘推断器不够强’，而在‘先验表示本身就太难处理’。**

这句话可以按三层来理解。第一层，如果高维参数空间本身非常复杂，那么无论你后面用点估计、MCMC 还是 VI，推断都得在一个很难正则化、很难搜索的空间里进行。也就是说，推断算法是在“坏坐标系”里工作。第二层，如果你手里本来就有参数样本，或者至少能单独训练一个生成模型去拟合这些参数的分布，那么你其实有机会先学到这个高维参数空间的几何结构：哪些区域是典型的、哪些方向是常见变化、哪些组合本来就不合理。第三层，一旦这层几何先验先学好了，后面的反演问题就不必再直接在原始高维参数空间里硬做，而可以先转到一个更规整的低维 latent 空间里进行。

这就是“先改先验表示”真正的意思：不是先去发明一种更复杂的后验近似器，而是先把高维参数先验本身改写成一个更容易操作的生成表示。所谓 **deep generative prior**，就是用一个深度生成模型来承载这种“参数空间几何已经被预先学好”的先验结构。

具体做法是引入一个更低维的**辅助潜变量** $\mathbf{w}$，再用生成器

$$
f_\theta:\mathbf{w}\mapsto \mathbf{z}
$$

去产生高维参数。这里的 $\mathbf{w}$ 对应的是 **DGP 引入的辅助潜空间**，它和上一小节里承载时间演化的动力学空间不是一回事。上一小节的 latent state $\mathbf{u}_{1:N}$ 负责描述“系统怎样随时间推进”；这里的 $\mathbf{w}$ 则负责描述“高维参数 $\mathbf{z}$ 可以由哪种更低维、更规整的生成坐标来表示”。这样一来，原来的参数先验不再直接放在高维 $\mathbf{z}$ 空间里，而是间接通过辅助潜空间 $\mathbf{w}$ 和生成器来表示。它的核心收益就是：后面做反演时，你可以在辅助潜空间 $\mathbf{w}$ 里工作，相当于把“参数高维、难以正则化”的问题，换成“先验几何已经由生成模型学好”的问题。

原文先给出点估计版本 [40]。在这里，训练好的生成器 $f_{\theta^\star}$ 被当成固定先验结构，真正优化的是低维 latent $\mathbf{w}$：

$$
J(\mathbf{w};\mathbf{y},\theta^\star)
=
\|G^\dagger\circ f_{\theta^\star}(\mathbf{w})-\mathbf{y}\|^2
+
\beta(\|\mathbf{w}\|-\mu_\chi)^2.
\tag{25}
$$

第一项是数据拟合：先把 $\mathbf{w}$ 推成参数 $\mathbf{z}=f_{\theta^\star}(\mathbf{w})$，再过真实 forward model 去匹配观测。第二项则是在辅助潜空间 $\mathbf{w}$ 里的正则化，这里可以更具体地读。它惩罚的是

$$
(\|\mathbf{w}\|-\mu_\chi)^2,
$$

也就是：如果 $\mathbf{w}$ 的模长偏离某个典型半径 $\mu_\chi$ 太远，代价就会上升。换句话说，这个正则项并不是简单地把 $\mathbf{w}$ 往原点压，也不是只要求它“越小越好”；它更像是在辅助潜空间里画出一个以原点为中心、半径约为 $\mu_\chi$ 的高概率环带（在更高维里可以理解成球壳）。优化时，$\mathbf{w}$ 会被鼓励留在这类训练先验分布最常见的区域附近，而不是跑到生成器几乎没见过的异常区域里。这样做的作用是：反演虽然仍然在追数据拟合，但不会为了匹配观测而把 latent code 拉到一个对生成器来说非常不典型的位置。最后求得的不是直接的参数点估计，而是先求

$$
\mathbf{w}^\star=\arg\min_\mathbf{w} J(\mathbf{w};\mathbf{y},\theta^\star),
$$

再通过生成器得到

$$
\mathbf{z}^\star=f_{\theta^\star}(\mathbf{w}^\star).
$$

原文接着又给出贝叶斯版本 [72]。这里不再只求一个最优 $\mathbf{w}^\star$，而是对辅助后验 $p(\mathbf{w}|\mathbf{y})$ 做 VI 近似：

$$
\phi^\star=\arg\min_\phi J(\phi;\mathbf{y},\theta^\star),
\qquad
J(\phi;\mathbf{y},\theta^\star)
=
\mathbb{E}_{q_\phi(\mathbf{w})}\bigl[-\log p(\mathbf{y}|\mathbf{w})\bigr]
+
\mathrm{KL}\bigl(q_\phi(\mathbf{w})\|p(\mathbf{w})\bigr),
\tag{26}
$$

其中

$$
p(\mathbf{y}|\mathbf{w})
:=
p(\mathbf{y}|\mathbf{z}=f_{\theta^\star}(\mathbf{w}))
$$

是由训练好的生成器和真实 forward model 共同诱导出来的似然。训练完以后，你先从辅助后验采样

$$
\mathbf{w}^{(i)}\sim q_{\phi^\star}(\mathbf{w}),
$$

再推过生成器

$$
\mathbf{z}^{(i)}=f_{\theta^\star}(\mathbf{w}^{(i)}),
$$

就得到参数后验样本。

所以这一小节真正展示的是：forward-model-based learning 不只是“把物理 forward model 写进似然”，还可以进一步把 **高维参数先验本身** 学成一个生成结构。这样反演就不必直接在高维参数空间里挣扎，而是改在一个更低维、更规整的辅助 latent 空间里进行。

### 3.2 路线二：基于残差的方法 (Residual-Based)

前一条路线默认你至少还能调用真实的 forward model，因此可以用它合成监督样本、构造物理解码器，或者把 one-step operator 直接嵌进 latent dynamics。`Residual-based learning` 的出发点更弱：这里不再要求你手里有一个可频繁调用的完整求解器，真正直接可用的只有 PDE 本身的结构。于是问题就变成：**能不能不用先把方程解出来，而是直接拿“残差应该接近零”这件事来构造概率模型？**

原文 `3.2` 的主线正是沿着这个想法推进：

1. 先在无数据情形下，把残差直接变成一种概率似然；
2. 再用这条残差似然去训练正向概率 surrogate；
3. 然后进一步引入虚拟观测，把正向映射和逆向映射放进同一个变分框架；
4. 最后再讨论如果手里还有少量真实观测，物理残差和数据似然该怎样并在一起。

#### 3.2.1 无数据推断 (Data-Free Inference)

这里的场景是：没有真实观测数据，或者至少训练时不依赖真实观测数据；你最可靠的信息来源就是 PDE 本身。

[Zhu et al.] 的关键构造是：既然“满足 PDE”这件事可以通过残差来判断，那么最自然的第一步，就是直接把残差写成一种条件概率：

$$
p_\beta(\mathbf{u}|\mathbf{z})
\propto
\exp\left(
-\beta \left\|\mathbf{r}\bigl(\pi_u(\mathbf{u}), \pi_z(\mathbf{z})\bigr)\right\|_2^2
\right).
\tag{27}
$$

这条式子最好按两层来读。第一层，残差

$$
\mathbf{r}\bigl(\pi_u(\mathbf{u}), \pi_z(\mathbf{z})\bigr)
$$

衡量的是：把候选解 $\mathbf{u}$ 和参数 $\mathbf{z}$ 代回离散化后的物理系统时，还剩多少不满足。第二层，指数形式把这件事变成了概率权重：残差越小，概率越大；如果残差精确为零，那么这个候选解在物理上最自洽，因此权重最大。这里的 $\beta$ 控制的就是物理约束的“硬度”：$\beta$ 越大，模型越接近“只接受几乎严格满足 PDE 的候选解”。

原文接着再走一步：既然已经有了由残差定义出来的条件分布，就可以不再把 PDE 只当成一个硬约束求解器，而是把它当成变分推断的目标分布。于是 [79] 写出

$$
\phi^\star
=
\underset{\phi}{\arg\min}\;
D_{\mathrm{KL}}
\left(
q_\phi(\mathbf{u}|\mathbf{z})p(\mathbf{z})
\;\middle\|\;
p_\beta(\mathbf{u}|\mathbf{z})p(\mathbf{z})
\right).
\tag{28}
$$

这一步的意思是：你现在不再直接求一个确定性的数值解，而是训练一个概率 surrogate

$$
q_\phi(\mathbf{u}|\mathbf{z}),
$$

让它尽量贴近那个“由物理残差诱导出来的条件分布” $p_\beta(\mathbf{u}|\mathbf{z})$。这样学到的就不只是一个点预测器，而是一个带不确定性的正向代理模型。原文在这里还特别强调：$\beta$ 不能只被看成一个惩罚强度，它还关系到 surrogate 的不确定性是否校准。

[Vadeboncoeur et al.] 接着又往前走一步：如果想同时学正向映射和逆向映射，那么只用 `Eq. (27)` 还不够，因为它只定义了“给定参数时，哪些解更物理”。于是作者引入一个 **虚拟观测量**：

$$
\hat{\mathbf{r}}
=
\mathbf{r}\bigl(\pi_u(\mathbf{u}), \pi_z(\mathbf{z})\bigr)
+\boldsymbol{\epsilon}_r,
\qquad
\boldsymbol{\epsilon}_r\sim \mathcal{N}(0,\sigma_r^2\mathrm{I}).
\tag{29}
$$

这一步真正做的，是把“残差应该接近零”这条物理要求，改写成一个标准的观测模型。也就是说，现在不再只是说“残差越小越好”，而是说：**我们把零残差当成一个虚拟观测目标，并允许它带一点高斯噪声。** 一旦这样写，物理约束就和普通数据观测一样，可以自然进入 ELBO。

在这个设定下，原文构造的联合模型和变分分解可以写成

$$
p_\theta(\hat{\mathbf{r}},\mathbf{u},\mathbf{z})
=
p(\hat{\mathbf{r}}|\mathbf{u},\mathbf{z})\,p_\theta(\mathbf{z}|\mathbf{u})\,p(\mathbf{u}),
$$

$$
q_\phi(\mathbf{u},\mathbf{z})
=
q_\phi(\mathbf{u}|\mathbf{z})\,p(\mathbf{z}).
$$

这组因子分解不是随意写的。它背后的分工是：
- $q_\phi(\mathbf{u}|\mathbf{z})$ 负责学习正向不确定性映射，也就是“给定参数时，解分布长什么样”；
- $p_\theta(\mathbf{z}|\mathbf{u})$ 负责学习逆向映射，也就是“给定解时，参数分布长什么样”；
- $p(\hat{\mathbf{r}}|\mathbf{u},\mathbf{z})$ 则把物理残差统一写进概率模型。

接下来最关键的一步，是说明这个目标为什么会自然变成一个 ELBO。这里最好按四步读。

第一步，既然现在“数据”不再是真实观测，而是虚拟观测 $\hat{\mathbf{r}}=0$，那么最自然要最大化的对象就是它的对数边际似然：

$$
\log p_\theta(\hat{\mathbf{r}}=0).
$$

第二步，把隐藏变量 $\mathbf{u},\mathbf{z}$ 积分掉：

$$
\log p_\theta(\hat{\mathbf{r}}=0)
=
\log \int p_\theta(\hat{\mathbf{r}}=0,\mathbf{u},\mathbf{z})\,d\mathbf{u}\,d\mathbf{z}.
$$

第三步，像标准 VI 一样，在积分里乘上再除以变分分布 $q_\phi(\mathbf{u},\mathbf{z})$，把它改写成

$$
\log p_\theta(\hat{\mathbf{r}}=0)
=
\log
\mathbb{E}_{q_\phi(\mathbf{u},\mathbf{z})}
\left[
\frac{p_\theta(\hat{\mathbf{r}}=0,\mathbf{u},\mathbf{z})}{q_\phi(\mathbf{u},\mathbf{z})}
\right].
$$

第四步，对外面的对数应用 Jensen 不等式，就得到一个下界，也就是 ELBO。再把前面已经选好的联合模型和变分分解代进去，才得到

$$
\phi^\star,\theta^\star
=
\underset{\phi,\theta}{\arg\max}\;J(\phi,\theta),
\qquad
J(\phi,\theta)
=
\mathbb{E}_{q_\phi(\mathbf{u}|\mathbf{z})p(\mathbf{z})}
\log
\frac{
p(\hat{\mathbf{r}}=0|\mathbf{u},\mathbf{z})\,
p_\theta(\mathbf{z}|\mathbf{u})\,
p(\mathbf{u})
}{
q_\phi(\mathbf{u}|\mathbf{z})\,p(\mathbf{z})
}.
\tag{30}
$$

这条 ELBO 最好按条件概率的语义逐项来读。先看分子里的第一项

$$
p(\hat{\mathbf{r}}=0|\mathbf{u},\mathbf{z})
$$

它问的不是一句抽象的“物理上对不对”，而是更具体的事：**如果当前这组候选解 $\mathbf{u}$ 和参数 $\mathbf{z}$ 真的成立，那么把它们代回 PDE 以后，得到的残差是否足够小，小到可以被解释成“零残差加一点高斯噪声”**。也就是说，这一项真正衡量的是：当前候选的解-参数组合离“满足物理方程”还有多远。

再看第二项

$$
p_\theta(\mathbf{z}|\mathbf{u})
$$

它问的是另一件具体的事：**如果你已经看到候选解 $\mathbf{u}$，那么哪一些参数 $\mathbf{z}$ 更像是能生成这条解的原因。** 这一项于是把“由解反推参数”的方向显式带进了同一个概率模型里，不再只是单向地从参数推出解。

分子里剩下的

$$
p(\mathbf{u})
$$

则提供了解空间本身的先验权重。它在问的是：**即使暂时不看残差和逆向映射，哪些候选解 $\mathbf{u}$ 本身就在先验上更常见，哪些则本来就不太合理。**

最后再看分母中的

$$
q_\phi(\mathbf{u}|\mathbf{z})
$$

它继续承担正向 surrogate 的角色，也就是：给定参数 $\mathbf{z}$ 以后，模型当前认为解 $\mathbf{u}$ 会怎样分布。于是这条 ELBO 的比值结构可以顺着读成：

- 分子在说：什么样的 $\mathbf{u},\mathbf{z}$ 组合既满足物理残差约束，又能支持由解反推参数，同时在解空间先验上也站得住；
- 分母在说：当前正向 surrogate 实际给这组 $\mathbf{u},\mathbf{z}$ 组合分配了多少概率。

所以这个目标不是简单地把几项硬拼在一起，而是在问：为了让“零残差”这个虚拟观测最有可能出现，模型应该怎样同时选择

- 正向不确定性映射 $q_\phi(\mathbf{u}|\mathbf{z})$，
- 逆向恢复映射 $p_\theta(\mathbf{z}|\mathbf{u})$，
- 与物理残差一致的解-参数组合，
- 以及这些组合在先验上是否本来就合理。

所以 Eq. (30) 的关键意义不只是“又写了一个 ELBO”，而是：**正向 UQ surrogate、逆向参数恢复，以及物理残差约束，第一次被放进了同一个变分框架里联合训练。**

#### 3.2.2 少数据体制 (Small-Data Regime)

到这里，原文已经完成了 data-free 情形：即使没有真实观测，也可以只靠“残差应该接近零”这条物理要求来训练概率 surrogate。下一步自然就是 small-data regime：如果你手里还有少量真实观测，那么物理残差和数据似然该怎样并在一起？

原文给出的第一步做法，是把两者直接写成乘积似然：

$$
p(\hat{\mathbf{r}}, \mathbf{y}|\mathbf{u}, \mathbf{z})
=
p(\hat{\mathbf{r}}=0|\mathbf{u}, \mathbf{z}) \cdot p(\mathbf{y}|\mathbf{u}, \mathbf{z}).
$$

这条式子最重要的意思是：物理残差和真实数据不再是两个互相竞争的 loss term，而是同一个概率模型里的两个观测通道。它们之间的平衡由各自噪声方差自然决定，而不需要另外再手工发明一组权重。

原文接着举的 [Tait & Damoulas] 方法，可以按一条更清楚的线来读。

第一步，先保留上一节已经出现过的想法：不用真实 forward solver 的精确后验，而是先训练一个正向代理模型

$$
\mathbf{u}=F_\theta(\mathbf{z}).
$$

它的意思是：给定参数 $\mathbf{z}$，先由代理模型预测对应的解 $\mathbf{u}$。

第二步，再把少量真实观测 $\mathbf{y}$ 接到这条代理链上。这样一来，数据拟合项不再直接写成“观测由原始 PDE 精确解生成”，而是写成

$$
p(\mathbf{y}\mid \mathbf{u}=F_\theta(\mathbf{z})).
$$

也就是说：当前参数 $\mathbf{z}$ 先经过代理模型变成候选解，再由这个候选解去解释真实观测。

第三步，再在参数端保留一个变分分布 $q_\phi(\mathbf{z})$。这样优化目标里自然会出现两部分：

- 一部分是数据拟合项  
  $$
  \mathbb{E}_{q_\phi(\mathbf{z})}\big[-\log p(\mathbf{y}\mid \mathbf{u}=F_\theta(\mathbf{z}))\big],
  $$
  它在问：如果参数按照当前的近似后验来取样，那么经过代理模型以后，是否还能把观测解释回来；

- 另一部分是正则化项  
  $$
  D_{\mathrm{KL}}(q_\phi(\mathbf{z})\|p(\mathbf{z})),
  $$
  它在约束：近似后验不要随意跑离先验太远。

第四步，再把物理残差放回来。这里最关键的是：残差一开始并不是硬约束，而是软约束。也就是说，模型先允许

$$
\|\mathbf{r}\|_2^2
$$

只是在概率上被压小，而不是立刻强制等于零。

第五步，原文讨论的是这个软约束的极限情形：当残差噪声尺度趋于零，也就是

$$
\epsilon \to 0,
$$

“残差应该接近零”这件事就不再只是一个软惩罚，而会收紧成一个真正的可行性条件。于是优化问题退化成

$$
\min_{\theta,\phi}
\mathbb{E}_{q_\phi(\mathbf{z})}\big[-\log p(\mathbf{y}\mid \mathbf{u}=F_\theta(\mathbf{z}))\big]
+
D_\mathrm{KL}\big(q_\phi(\mathbf{z}) \| p(\mathbf{z})\big)
\qquad
\text{s.t.}
\qquad
\|\mathbf{r}\|_2^2 = 0.
$$

这条式子最好也拆开读：

- 目标函数的第一项说的是：在所有满足物理约束的候选参数里，哪一些通过代理模型以后最能解释真实观测；
- 第二项说的是：这些候选参数的变分分布不要偏离先验太远；
- 约束项说的是：被接受的候选解必须真的把 PDE 残差压到零。

所以这里真正发生的不是“又给 ELBO 多加了一个 penalty”，而是：**物理残差在严格极限下从软约束变成了硬约束，数据拟合和先验正则则在这组可行解里继续做贝叶斯式权衡。**

原文最后列的几个变体，也最好不要只当作方法名，而要看成同一思路的不同实现：

- **PI-VAE** [Zhong & Meidani]：把这套思路放到随机 PDE 上，用 VAE 形式处理解和参数的不确定性；
- **PI-GAN** [Yang et al.]：保留“物理约束嵌入生成模型”这条主线，但把 VAE 的生成框架换成 GAN；
- **NFF** [Guo et al.]：用 normalizing field flows 去学习和传感器位置无关的场分布表示，让生成模型更适合处理观测布局变化的问题。

所以这一小节真正想说明的不是“又有几篇相关工作”，而是：一旦把残差、数据和先验都放进同一个概率模型里，后面可以接 VAE、GAN、flow 等不同生成框架；变化的是实现形式，不变的是“物理约束 + 观测数据 + 变分推断”这一条主线。

---

## 4. 方法全景对比

把前面的方法放在一起看，真正的分界线不是模型名字，而是三件事：

- 物理知识是通过正向模型、动力学结构、生成先验还是残差进入的；
- 手里到底有多少数据；
- 最后要学的是后验、正向 surrogate，还是两者一起。

顺着这三条线，全文的方法可以按更清楚的五类来读。

第一类，是**有监督条件下直接学习逆向后验**。这里最典型的是 Supervised CNF [60] 和物理解码器 VAE [20]。这一路线最好按三步来理解。

第一步，先假设训练数据是充足的。也就是说，你不只是拿到少量真实观测，而是可以反复从先验采样参数 $\mathbf{z}$，再通过真实正向模型生成对应观测 $\mathbf{y}$，从而得到大量监督样本对 $(\mathbf{z},\mathbf{y})$。

第二步，在有了这些监督样本对以后，任务就不再是“先解一个 forward problem 再慢慢倒推”，而是直接变成一个条件分布学习问题：面对一个观测 $\mathbf{y}$，怎样直接输出参数后验近似 $q_\phi(\mathbf{z}|\mathbf{y})$。

第三步，Supervised CNF 和物理解码器 VAE 的区别，主要不在任务本身，而在“这个后验近似用什么分布族表示”和“物理模型嵌在哪里”。

- **Supervised CNF [60]**：后验近似由 conditional normalizing flow 表示。它的重点是给 $q_\phi(\mathbf{z}|\mathbf{y})$ 一个足够灵活、又能精确写密度的分布族；真实正向模型主要用来生成监督训练对，本身并不深嵌进 decoder 结构里。  
- **物理解码器 VAE [20]**：这里的 **encoder** 指的是从观测 $\mathbf{y}$ 到后验近似 $q_\phi(\mathbf{z}|\mathbf{y})$ 这一段，也就是“看到数据以后，怎样把参数后验编码出来”；作者让它仍然保持为较简单的高斯形式。这里的 **decoder** 指的是从参数 $\mathbf{z}$ 回到观测 $\mathbf{y}$ 的生成路径，也就是 $p_\theta(\mathbf{y}|\mathbf{z})$。和普通 VAE 不同，这个 decoder 的均值不是随意用神经网络来回归，而是直接由真实 forward model 给出。因此模型的生成路径本身就带着更强的物理结构，而不是只在数据生成阶段借用一次 forward solver。

所以这一类方法的共同点可以收成一句：**数据是充足的，主任务是逆问题，学习对象是参数后验；差别主要在于后验分布族怎么选，以及物理正向模型是只用于生成监督数据，还是直接写进生成结构里。**

第二类，是**把时间演化本身嵌进潜空间**。这里代表是 $\varphi$-DVAE [19]。这一路线最好不要只理解成“给序列也加一个 VAE”，而要看它为什么要把潜空间改成动力学潜空间。

第一步，作者先承认一个限制：如果你只给整段时序观测一个静态 latent code，那么这个 latent 更像是在压缩“整段序列长什么样”，却不容易显式表达“系统是怎样一步一步演化到这里的”。

第二步，于是模型不再只保留观测 $\mathbf{y}_{1:N}$ 和一个单独 latent，而是在两者之间插入中间层。更具体地说，它把结构拆成：

- 真实观测 $\mathbf{y}_{1:N}$；
- 伪观测层 $\mathbf{x}_{1:N}$；
- 真正 obey one-step physical operator 的动力学 latent state $\mathbf{u}_{1:N}$。

第三步，这样做的重点不是把层次搞复杂，而是让时间推进这件事本身显式出现：latent state 不再是随意跳动的隐变量，而是要围绕 one-step operator 做一步一步的局部演化。于是模型关心的就不再只是“哪个参数最可能解释这组观测”，而是“哪一组动力学参数和潜空间演化规律最能共同解释整段时序数据”。

所以第二类方法的核心不在“逆向后验学得更准”，而在：**把物理一步推进规律直接嵌进潜空间的状态转移里。** 因而它学习的对象也从普通静态参数后验，变成了**动力学参数后验**以及与之配套的时序潜空间结构。

第三类，是**先重写先验表示，再做推断**。这就是 DGP 路线，也就是 DGP 点估计 [40] 和 VI-DGP [72]。它们共同的出发点是：如果原始高维参数空间太难处理，那么与其直接换推断算法，不如先学一个 deep generative prior，把参数几何压进一个更规整的辅助潜空间。

- **DGP 点估计 [40]**：先学生成先验，再在辅助潜变量上做确定性优化，最后得到一个点估计。  
- **VI-DGP [72]**：同样从生成先验出发，但不再只求一点，而是在辅助潜变量上做 VI，从而恢复参数后验。

所以这一类方法的共同点是：**物理知识通过“生成先验 + 正向模型”一起进入，重点不在直接学后验近似器，而在先把高维参数空间变成更好操作的表示。**

第四类，是**在没有真实数据时，直接把 PDE 残差当成概率对象**。这里有两层。

- **物理残差代理 [79]**：只学习正向概率 surrogate。它把“残差应该接近零”写成残差似然，然后用 Normalizing Flow 去近似由残差诱导出来的 $p_\beta(\mathbf{u}|\mathbf{z})$。这时学习对象是**正向概率代理**，还没有显式加入逆向参数恢复。  
- **双向 VI [67,68]**：再往前一步，把虚拟观测 $\hat{\mathbf{r}}=0$、正向 surrogate $q_\phi(\mathbf{u}|\mathbf{z})$ 和逆向映射 $p_\theta(\mathbf{z}|\mathbf{u})$ 一起放进同一个 ELBO。于是学的就不只是正向代理，而是**正向和逆向同时学习**。

所以这一类方法的共同点是：**即使没有真实观测，也试图只靠“物理残差应接近零”这条信息来驱动变分学习。**

第五类，是**少数据条件下，把物理残差和真实观测联合起来**。这里代表是物理+数据混合 [26] 和 PDE 约束 VAE [64]。它们共同处理的是这样一个场景：真实观测不多，单靠数据不够，单靠物理残差也不够，于是必须把两者放进同一个概率模型里。

- **物理+数据混合 [26]**：把残差似然和数据似然写成乘积观测模型，再在其中做均场近似，目标是同时恢复**解和参数的后验**。  
- **PDE 约束 VAE [64]**：把 PDE 离散结构更深地编码进近似分布本身，例如用刚度矩阵去信息化协方差结构。它学习的是**正向代理与参数后验**，但更强调近似分布内部也要带着 PDE 结构。

如果把这五类再压成一句总结，那么这篇 primer 里所有方法其实都在同一个坐标系里移动：

- 数据多的时候，重点是直接学逆向后验；
- 有时间结构时，重点是把动力学嵌进潜空间；
- 参数空间太坏时，重点是先学生成先验；
- 没有数据时，重点是把残差写成概率对象；
- 数据很少时，重点是把残差和观测联合起来。

因此这张“方法表”真正有用的地方，不是让人记住九个方法名，而是让人看清：**physics-informed VI 的变化，并不是随意堆模型，而是在不同数据条件和不同物理嵌入方式下，对“学什么对象、把物理放在哪里”这两个问题给出的不同回答。**

---

## 5. 不确定性量化的角色

贯穿全文的一条暗线是：**物理问题为什么特别需要不确定性量化（uncertainty quantification, UQ）？**

第一步，物理逆问题本身就天然带不确定性。前面已经反复出现过：观测通常是稀疏的、带噪的，而且只看到系统状态的一部分。于是很多不同的参数配置都可能解释同一组观测。也就是说，问题往往不是“唯一正确答案是什么”，而是“有多少种参数解释都还说得通”。这正是贝叶斯后验要捕捉的第一层内容。

第二步，即使先不谈观测噪声，数值近似本身也会再引入一层不确定性。文章里大量方法都会用到代理模型、生成模型或神经网络解算器，但这些对象都不可能与原始 PDE 求解器完全等价。它们只能给出近似。于是除了“参数本身有多不确定”之外，还会多出第二个问题：**当前模型自己的近似到底有多可靠。** 所以这里做 UQ，不只是为了表达逆问题的多解性，也是为了让近似模型能对自己的误差范围给出概率刻画。

第三步，这种不确定性在物理问题里还会被计算代价进一步放大。很多 UQ 方法本质上都需要重复做正向求解，例如 Monte Carlo 反复采样、再反复把每个样本送进 forward solver。如果每次都调用一次昂贵的 PDE 数值求解器，那么“不确定性量化”在计算上很快就会变得不可承受。也就是说，物理问题不是不想做 UQ，而是传统求解链路往往贵到做不起。文章里反复强调 VI 和代理模型的价值，也正是在这里：一旦近似后验和正向 surrogate 学好，后续采样和推断就会便宜很多。

第四步，到了少数据情形，UQ 的角色会再变得更微妙。此时模型往往一边依赖真实观测，一边依赖物理残差或先验结构。于是问题不再只是“答案有多不确定”，而是“我该更信数据，还是更信物理约束”。如果把这件事写成手工 loss 加权，权重通常很难选；但如果把它写进同一个概率模型里，那么这种权衡就会通过噪声方差、似然结构和后验分布自然体现出来。换句话说，这里做 UQ 的意义，不只是给一个误差条，而是把不同信息来源之间的信任分配也一起放进推断框架。

所以这一节真正想说的是：物理问题之所以特别需要 UQ，不是因为“大家习惯做贝叶斯”，而是因为这里同时存在四种不确定性来源：

- 逆问题本身的多解性；
- 代理模型和数值近似带来的模型误差；
- 多次正向求解导致的高计算成本；
- 少数据情形下数据与物理约束之间的信任权衡。

也正因为这四层问题叠在一起，文章才会把 VI 看成一个特别自然的工具：它既能给出后验近似，又能把这些不同来源的不确定性统一放进一个可优化、可计算的概率框架里。

---

## 6. 核心结论与开放问题

### 6.1 结论

如果把全文收成一条主线，那么这篇 primer 真正完成了三件事，而且这三件事是层层递进的。

第一层，它重新回答了一个最基础的问题：为什么在物理推断里，VI 会反复出现。前面已经看到，物理逆问题一方面天然需要后验分布来表达多解性和不确定性，另一方面又常常连一次正向求解都很贵。在这种背景下，MCMC 虽然概念上直接，但代价往往难以承受；VI 的价值就在于，它把原来难算的后验推断改写成可优化问题，因此在计算效率和不确定性刻画精度之间提供了一个现实可用的折中。

第二层，这篇文章说明的不是“VI 只能配一种物理模型”，而是：物理知识可以通过很多不同入口被嵌进同一个变分框架。前面已经依次看到，物理信息可以来自真实正向模型，可以来自 PDE 残差，可以来自动力学潜空间结构，也可以来自深度生成先验。也就是说，VI 在这里的真正强项不是某一个特定公式，而是它能容纳不同 conditional dependence structure，并把这些结构保留到近似后验和生成模型里。

第三层，全文把这些方法重新组织成了一条连续谱，而不是互不相干的技巧清单。从数据非常充足、可以直接监督学习后验，到几乎没有真实观测、只能依赖残差和虚拟观测；从单步静态反演，到时序潜空间动力学；从直接近似后验，到先重写先验表示再做推断，文章都在用同一套概率和变分语言来解释。因此这篇综述最重要的收束，不是“推荐哪一种模型”，而是说明：**physics-informed VI 的各种分支，本质上都是在不同数据条件和不同物理嵌入方式下，对同一个变分推断框架做具体化。**

### 6.2 开放问题

但文章的收束并不等于问题已经解决。恰恰相反，作者最后点出的开放问题，刚好说明这条路线接下来最难的地方在哪里。

第一，VI 给出的不确定性到底准不准，也就是 calibration 问题，仍然没有被真正解决。VI 可以廉价地产生后验近似，但近似后验的方差和尾部行为未必可靠。对于物理问题来说，这不是一个次要细节，因为一旦不确定性本身失真，后面所有基于风险、可信区间和实验设计的判断都会跟着偏掉。

第二，代理模型到底值不值得训练，不能抽象地下结论。文章虽然反复强调 VI 和 surrogate 的计算优势，但这并不自动意味着“训练一个代理模型总比直接跑经典求解器便宜”。如果问题维度不高、查询次数不多，或者训练代价本身极大，那么代理路线未必划算。所以这里真正要比较的不是方法标签，而是总成本：训练一次的代价、后续查询的频率，以及误差是否可接受。

第三，KL 散度本身在函数空间里并不总是一个稳定、好用的对象。前面所有 VI 推导都大量依赖 KL，但当随机对象变成函数、场或者无限维表示时，KL 的适定性会变得微妙，甚至可能失效。也正因为这一点，文章最后特别提到 Wasserstein 距离、Sliced Wasserstein 和最大平均差异（maximum mean discrepancy, MMD）等替代散度，说明这条路线的基础度量本身仍在被重新审视。

第四，先验学习依然是决定上限的关键。前面已经看到，无论是 deep generative prior 还是更一般的 physics-informed latent representation，很多方法之所以有效，靠的都是“先验几何写得够好”。但现实里真正困难的问题，恰恰经常缺少这种现成好先验。于是一个自然但尚未解决的问题就是：如何直接从数据中学出既物理合理、又足够灵活的先验结构。

所以这一节最后留下来的开放图景其实很清楚：VI 已经把物理推断里的很多计算和建模问题统一进来了，但校准、性价比、函数空间散度和先验学习这四个问题，决定了这条路线离真正成熟还差多远。

---

## 7. 个人评注

这篇文章作为 tutorial/review 的定位非常准确。它最大的贡献不是新方法，而是用统一的符号系统（参数-解-观测三空间 + WRM 残差 + ELBO 推导）把近年来零散的 physics-informed VI 工作串联成一个有逻辑的体系。对于想进入这个领域的研究者，我建议的阅读路径是：

1. 先吃透 Section 2.3 的两种 ELBO 推导（Bayes VI vs. 生成模型 VI）：前者是在固定模型里近似一个已定义好的后验，后者则是在学习生成模型的同时学习后验近似
2. 然后根据自己的问题类型（正向/逆向，有数据/无数据）定位到 Section 3 的对应方法
3. 最后关注 Discussion 中关于 KL 散度替代和先验学习的指引
