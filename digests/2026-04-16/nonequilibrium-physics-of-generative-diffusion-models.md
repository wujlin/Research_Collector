---
title: "Nonequilibrium Physics of Generative Diffusion Models"
authors: "Zhendong Yu, Haiping Huang"
venue: "Phys. Rev. E 111, 014111 (2025)"
date_read: "2026-04-16"
topics: ["非平衡动力学", "涨落定理", "扩散生成模型", "熵产生"]
---

# Nonequilibrium Physics of Generative Diffusion Models —— 精读笔记

## 1. 问题定义与研究动机

生成扩散模型（Generative Diffusion Models, GDMs）是当前最活跃的生成式 AI 方向之一，其物理根基是非平衡统计力学中的 Langevin 动力学。其核心流程分两步：**正向扩散**（forward diffusion）将真实数据样本（如图像）逐步加噪为高斯白噪声；**反向生成**（reverse generative process）从白噪声出发，由对数似然的梯度（即 score function）驱动，将噪声逆转恢复为符合真实数据分布的样本。

尽管 GDMs 在工程上取得了巨大成功（DALL-E、Sora 等），但对其内在物理机制的完整理解仍然缺乏。此前的物理研究主要集中在对称性破缺、Bayes 最优去噪、平衡统计力学重构、路径积分表示等方面，但这些角度各自独立，缺少统一图景。

**本文的核心目标**：在一个解析可处理的高斯混合数据模型（Gaussian Mixture Model）上，用非平衡统计物理的完整工具箱——路径积分（path integral）、涨落定理（fluctuation theorem）、熵产生（entropy production）、自由能（free energy）、Franz-Parisi 势（Franz-Parisi potential）——来剖析 GDMs 的正向与反向动力学，统一非平衡热力学、统计推断和几何分析三个视角。

**三项主要贡献**：

1. 从熵产生的角度分析反向生成过程，推导并验证正向和反向过程的涨落定理；
2. 将去噪过程映射为统计推断问题，推导广义自由能，统一此前不同方法得到的分化转变（speciation transition）结果，并揭示新的对称性相图；
3. 用 Franz-Parisi 势从几何角度刻画反向过程中的坍缩转变（collapse transition），不依赖经验分布假设。

![图1：二维高斯混合数据的扩散过程示意图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-02-figure-01.jpg)

**图 1 的角色**：展示二维高斯混合数据从 $t=0$ 到 $t=3$ 的正向扩散过程（蓝色轨迹，数据→噪声）和从 $t=3$ 返回 $t=0$ 的反向生成过程（绿色轨迹，噪声→数据），为全文搭建直觉。正向过程中两个分离的数据簇逐渐混合为单一高斯分布，反向过程则从无结构的噪声中重新"分化"出两个数据簇。

---

## 2. 正向扩散的非平衡物理

### 2.1 Ornstein-Uhlenbeck 过程

正向扩散采用标准的 Ornstein-Uhlenbeck（OU）过程：

$$\dot{\mathbf{X}} = -\mathbf{X} + \sqrt{2}\,\boldsymbol{\xi}$$

其中 $\mathbf{X} \in \mathbb{R}^d$ 为状态变量，$\boldsymbol{\xi}$ 为标准高斯白噪声。给定初始条件 $\mathbf{X}_0$，解为：

$$\mathbf{X}_t = e^{-t}\mathbf{X}_0 + \sqrt{1 - e^{-2t}}\,\mathbf{Z}_t$$

其中 $\mathbf{Z}_t$ 为标准高斯随机变量。当 $t \to \infty$，$\mathbf{X}_t$ 趋向标准正态分布，信号被完全淹没。

数据分布选取为两类等权高斯混合（symmetric Gaussian mixture）：

$$p(\mathbf{X}_0) = \frac{1}{2}\mathcal{N}(\boldsymbol{\mu}, \mathbf{I}_d) + \frac{1}{2}\mathcal{N}(-\boldsymbol{\mu}, \mathbf{I}_d)$$

经过前向扩散后，任意时刻 $t$ 的状态分布仍保持高斯混合形式 $p(\mathbf{X}_t, t) = \frac{1}{2}\mathcal{N}(\boldsymbol{\mu}_t, \mathbf{I}_d) + \frac{1}{2}\mathcal{N}(-\boldsymbol{\mu}_t, \mathbf{I}_d)$，其中均值衰减为 $\boldsymbol{\mu}_t = \boldsymbol{\mu}e^{-t}$。这一解析可控的模型是全文推导的基础。

### 2.2 路径积分框架

这一小节从方程 `(6)` 一直铺到方程 `(16)`。如果直接跳到最后那个结果式，Wiener 过程、$\lambda$-离散化和 Jacobian 修正项都会悬空。下面按原文顺序展开。

#### 第一步：先把白噪声改写成 Wiener 过程

原文先定义 Wiener 过程

$$
\mathbf{W}(t)=\int_{t_0}^{t}dt'\,\boldsymbol{\xi}(t')=\int_{t_0}^{t} d\mathbf{W}. \tag{6}
$$

白噪声 $\boldsymbol{\xi}(t)$ 本身太奇异，不能像普通函数那样逐点操作；Wiener 过程 $\mathbf{W}(t)$ 是它的积分对象，后面的随机积分和离散化都围绕 $d\mathbf{W}$ 来写：

- $\boldsymbol{\xi}(t)$ 是白噪声
- $d\mathbf{W}$ 是 Wiener 增量
- SDE 后面真正被离散化的，不是“噪声函数本身”，而是这个 Wiener 增量

#### 第二步：为什么要引入 $\lambda$-离散化

接着说明，随机积分

$$
\int d\mathbf{W}\, f(\mathbf{X}_t,t)
$$

不是普通积分，它依赖你在每个小时间步里用区间左端、右端还是中点来取函数值。因此作者先写了两种最经典的方案：

- Ito：$\lambda = 0$
- Stratonovich：$\lambda = \tfrac12$

更一般地，时间区间 $[t_k,t_{k+1}]$ 上的取样点写成

$$
\tau=(1-\lambda)t_k+\lambda t_{k+1}.
$$

原文称其为 general discretization scheme。它不是新的物理参数，而是把不同随机微积分约定统一到同一个记号里；后面路径概率里的 $\lambda$ 项都来自这里。

#### 第三步：把 SDE 改写成单步更新公式

原文把前向 SDE 先写成一般形式

$$
d\mathbf{X}_t = f(\mathbf{X}_t,t)\,dt + \sqrt{2}\,d\mathbf{W}, \tag{9}
$$

对于本文的 OU 过程，最后再代入

$$
f(\mathbf{X}_t,t)=-\mathbf{X}_t.
$$

在一般的 $\lambda$-离散化下，单步更新变成

$$
\frac{\mathbf{X}_{t+dt}-\mathbf{X}_t}{dt}
=
f\!\left((1-\lambda)\mathbf{X}_t+\lambda\mathbf{X}_{t+dt},\, t+\lambda dt\right)
+ \boldsymbol{\eta}_t, \tag{10}
$$

其中

$$
\eta_{i,t}\sim \mathcal{N}(0,2/dt).
$$

这里的 $\boldsymbol{\eta}_t$ 不是新的动力学变量，而是把每一步的 Wiener 增量重新写成一个高斯随机变量之后得到的离散噪声。原文后面就是要先写出 $\boldsymbol{\eta}_t$ 的概率密度，再把它变换成 $\mathbf{X}_{t+dt}$ 的概率密度。

#### 第四步：单步传播子为什么要乘 Jacobian

原文下一步的核心公式是

$$
P(\mathbf{X}_{t'} , t' \mid \mathbf{X}_t , t)
=
P(\boldsymbol{\eta}_t)
\left|
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t'}}
\right|. \tag{11}
$$

这里最容易让人疑惑的是：为什么可以把噪声变量 $\boldsymbol{\eta}_t$ 的概率密度，直接变成下一时刻状态 $\mathbf{X}_{t'}$ 的概率密度？

关键不在“它们都是随机变量”，而在于：一旦当前状态 $\mathbf{X}_t$ 被固定，方程 `(10)` 就把 $\boldsymbol{\eta}_t$ 和 $\mathbf{X}_{t+dt}$ 之间建立成了局部可逆的映射。把 `(10)` 移项可得

$$
\boldsymbol{\eta}_t
=
\frac{\mathbf{X}_{t+dt}-\mathbf{X}_t}{dt}
-
f\!\left((1-\lambda)\mathbf{X}_t+\lambda \mathbf{X}_{t+dt},\, t+\lambda dt\right).
$$

因此，在“给定当前状态 $\mathbf{X}_t$”这个条件下，$\boldsymbol{\eta}_t$ 就是 $\mathbf{X}_{t+dt}$ 的一个确定函数。这里做的不是任意随机对象之间的替换，而是在单步更新公式定义出的局部映射上做密度变换。

更具体地说，当前条件分布要计算的是

$$
P(\mathbf{X}_{t+dt}\mid \mathbf{X}_t).
$$

这里 $\mathbf{X}_t$ 已经是固定参数，因此“随机性”完全来自 $\boldsymbol{\eta}_t$。而一旦 $\mathbf{X}_t$ 固定，每个可能的噪声值 $\boldsymbol{\eta}_t$ 都会对应一个可能的下一时刻状态 $\mathbf{X}_{t+dt}$，反过来也成立。对这个映射求导得到

$$
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t+dt}}
=
\frac{1}{dt}I-\lambda \frac{\partial f}{\partial \mathbf{X}}.
$$

当 $dt$ 很小时，主导项是 $\frac{1}{dt}I$，因此这个映射在局部上是可逆的。于是就可以使用普通的概率密度换元公式。

守恒的不是“密度值”，而是小体积元上的概率质量：

$$
P(\boldsymbol{\eta}_t \in d\eta)
=
P(\mathbf{X}_{t+dt}\in d\mathbf{X}').
$$

因此

$$
p_{\mathbf{X}'}(\mathbf{X}')\,d\mathbf{X}'
=
p_{\eta}(\eta)\,d\eta,
$$

而体积元之间满足

$$
d\eta
=
\left|
\det \frac{\partial \eta}{\partial \mathbf{X}'}
\right| d\mathbf{X}'.
$$

所以最后自然得到

$$
p_{\mathbf{X}'}(\mathbf{X}')
=
p_\eta(\eta)
\left|
\det \frac{\partial \eta}{\partial \mathbf{X}'}
\right|.
$$

原文的 `(11)` 正是在多维情况下把这条换元公式应用到

$$
\mathbf{X}'=\mathbf{X}_{t'}
$$

和

$$
\eta=\boldsymbol{\eta}_t
$$

上。

真正容易写出来的是噪声变量 $\boldsymbol{\eta}_t$ 的分布，因为它是高斯的；但我们最后需要的是“给定当前状态 $\mathbf{X}_t$，下一时刻状态 $\mathbf{X}_{t'}$ 的分布”。因此必须做变量替换，而变量替换就必须乘 Jacobian。

逻辑顺序是：

1. 单步更新公式 `(10)` 把 $\mathbf{X}_{t+dt}$ 和 $\boldsymbol{\eta}_t$ 一一对应起来
2. 已知 $\boldsymbol{\eta}_t$ 是高斯分布
3. 用概率密度变换把它改写成 $\mathbf{X}_{t+dt}$ 的短时传播子

所以 Jacobian 不是技术细节，而是从“噪声的概率”走到“状态的概率”的必要一步。

#### 第五步：为什么 Jacobian 会给出一个额外的 $\lambda \nabla\!\cdot f$ 项

原文随后计算

$$
\left|
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t+dt}}
\right|
\propto e^{-\lambda \nabla\cdot f\,dt}. \tag{12}
$$

“体积元变化”指的是多维换元中的局部体积伸缩。

设想在 $\mathbf{X}_{t+dt}$ 空间里取一个非常小的小立方体，体积记为 $d\mathbf{X}'$。通过前面的映射

$$
\boldsymbol{\eta}_t = g(\mathbf{X}_{t+dt};\mathbf{X}_t),
$$

这个小立方体会被映到 $\boldsymbol{\eta}_t$ 空间里的一个很小的平行多面体，体积记为 $d\eta$。所谓“体积元变化”，就是在比较这两个很小区域的体积是否一样：

- 如果映射只是刚体平移，体积不变；
- 如果映射在某些方向上拉伸、在某些方向上压缩，体积就会改变；
- Jacobian 行列式测量的正是这个局部体积放大或缩小的倍数。

所以

$$
\left|
\det\frac{\partial \eta}{\partial \mathbf{X}'}
\right|
$$

不是凭空来的校正项，而是在回答：

`同样一块小区域，在状态空间和噪声空间里分别占多大体积？`

现在回到这篇文章的具体映射。前面已经得到

$$
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t+dt}}
=
\frac{1}{dt}I-\lambda \frac{\partial f}{\partial \mathbf{X}}.
$$

把 $\frac{1}{dt}$ 提出来：

$$
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t+dt}}
=
\frac{1}{dt}
\left(
I-\lambda dt \frac{\partial f}{\partial \mathbf{X}}
\right).
$$

因此 Jacobian 行列式可以写成

$$
\left|
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t+dt}}
\right|
=
\left(\frac{1}{dt}\right)^d
\det\!\left(
I-\lambda dt \frac{\partial f}{\partial \mathbf{X}}
\right).
$$

前面的 $(1/dt)^d$ 只是一个与路径形状无关的整体常数，后面真正留下动力学信息的是第二项。对小 $dt$，使用矩阵近似

$$
\det(I+\varepsilon A)\approx 1+\varepsilon\,\mathrm{Tr}(A),
$$

就得到

$$
\det\!\left(
I-\lambda dt \frac{\partial f}{\partial \mathbf{X}}
\right)
\approx
1-\lambda dt\,\mathrm{Tr}\!\left(\frac{\partial f}{\partial \mathbf{X}}\right).
$$

而

$$
\mathrm{Tr}\!\left(\frac{\partial f}{\partial \mathbf{X}}\right)=\nabla\cdot f,
$$

也就是漂移场的散度。因此

$$
\left|
\frac{\partial \boldsymbol{\eta}_t}{\partial \mathbf{X}_{t+dt}}
\right|
\propto
1-\lambda dt\,\nabla\cdot f
\approx
e^{-\lambda \nabla\cdot f\,dt}.
$$

这时就能看清楚原文为什么会出现那个指数修正项了。它反映的是：漂移场 $f$ 会改变状态空间中小体积元的大小；在变量替换时，Jacobian 正是用来记录这种局部体积变化的。散度

$$
\nabla\cdot f
$$

测量的正是这种局部体积变化率。

因此，这里最重要的不是单纯记住结果

$$
e^{-\lambda \nabla\cdot f\,dt},
$$

而是理解它背后的几何意义：

`噪声变量和状态变量之间的映射，不只是改变了变量名称，也改变了状态空间中小体积元的大小；在变量替换时，Jacobian 正是用来记录这种局部体积变化的，而散度项就是这种变化在短时间步上的痕迹。`

#### 第六步：得到单步传播子

把高斯噪声分布和 Jacobian 合起来，原文得到 infinitesimal propagator

$$
P(\mathbf{X}_{t+dt}, t+dt \mid \mathbf{X}_t, t)
\propto
e^{-\lambda \nabla\cdot f\,dt}
\exp\!\left[
-\frac{\left|\dot{\mathbf{X}}_t-f(\mathbf{X}_t,t)\right|^2}{4}\,dt
\right]. \tag{13}
$$

它可以读成：

- 第一部分来自 Jacobian
- 第二部分来自高斯噪声的二次型

如果你只熟悉普通扩散核，那么这里多出来的那项正是随机积分约定留下的修正。

#### 第七步：从单步传播子乘到整条路径概率

接着原文用 Markov 链性质，把整条轨迹的条件概率写成各个短时传播子的乘积：

$$
P(X([T]) \mid \mathbf{X}_0)
=
\prod_{t'} P(\mathbf{X}_{t'}, t' \mid \mathbf{X}_t, t). \tag{14}
$$

把上一条短时传播子代进去，再取连续极限，就得到

$$
P(X([T]) \mid \mathbf{X}_0)
\propto
\exp\!\left[
\int_0^T
\left(
-\lambda \nabla\cdot f
-\frac{|\dot{\mathbf{X}}_t-f(\mathbf{X}_t,t)|^2}{4}
\right)
\overset{\lambda}{\odot}dt
\right].
$$

这就是一般漂移 $f$ 下的路径概率公式。原文中间还提到另一条等价路线：利用 Dirac delta 泛函

$$
\delta(\mathbf{X}(t)-\mathbf{X}_\xi(t)) = \delta(\mathbf{O}[\mathbf{X}(t)]) \det \frac{\delta \mathbf{O}}{\delta \mathbf{X}} \tag{15}
$$

也能导出同样结果。但就阅读主线来说，到这里已经够了：整条路径概率就是由“每一步的高斯噪声代价”加上“每一步的 Jacobian 修正”累乘起来的。

#### 第八步：最后才把一般公式专门代回 OU 过程

前面一直保留一般漂移 $f$，是为了让路径积分结构写得最清楚。到了方程 `(16)`，作者才把

$$
f=-\mathbf{X}
$$

代回去，于是得到前向 OU 过程的条件轨迹概率：

$$
P(X([T])|\mathbf{X}_0)
\propto
\exp\left(
-\int_0^T
\left[
\frac{1}{4}(\dot{\mathbf{X}}+\mathbf{X})^2
-\lambda d
\right]
\overset{\lambda}{\odot}dt
\right). \tag{16}
$$

现在这个式子里的每一部分都能对上来源：

- $(\dot{\mathbf{X}}+\mathbf{X})^2/4$ 来自高斯噪声的二次代价
- $-\lambda d$ 来自 Jacobian 修正，因为对于 OU 漂移 $f=-\mathbf{X}$，有
  $$
  \nabla\cdot f = -d
  $$
- 整个时间积分就是路径的 action
- 被积函数就是 Lagrangian

方程 `(16)` 是原文从 `(6)` 到 `(15)` 逐步推进后的终点。后面做涨落定理时，用到的就是这条前向路径 action 及其在时间反转下的变化。

### 2.3 正向过程的涨落定理

有了方程 `(16)` 的前向路径概率之后，原文下一步才进入涨落定理。这里的核心问题是：同一条轨迹如果倒过来走，它在正向动力学和反向时间方向下的路径权重会差多少。

**时间反转路径的定义。** 给定一条前向轨迹 $\{X_t\}_{0 \leq t \leq T}$，定义其时间反转路径 $\tilde{X}$ 为 $\tilde{\mathbf{X}}_s = \mathbf{X}_{T-s}$（$0 \leq s \leq T$），即沿相同的空间位置序列但以相反的时间顺序经过。反转路径的速度满足 $\dot{\tilde{\mathbf{X}}}_s = -\dot{\mathbf{X}}_{T-s}$。

**计算条件路径概率之比。** 在 Stratonovich（$\lambda = 1/2$）格式下，前向路径的作用量密度为 $\frac{1}{4}(\dot{\mathbf{X}} + \mathbf{X})^2$。将时间反转路径 $\tilde{X}$ 代入**同一正向动力学**的作用量，速度取反而位置不变，作用量密度变为 $\frac{1}{4}(-\dot{\mathbf{X}} + \mathbf{X})^2$。取二者之差：

$$\ln\frac{P[X|\mathbf{X}_0]}{P[\tilde{X}|\mathbf{X}_T]} = -\int_0^T \frac{(\dot{\mathbf{X}}+\mathbf{X})^2 - (-\dot{\mathbf{X}}+\mathbf{X})^2}{4}\,dt$$

展开平方差：$(\dot{\mathbf{X}}+\mathbf{X})^2 - (-\dot{\mathbf{X}}+\mathbf{X})^2 = (\dot{\mathbf{X}}^2 + 2\dot{\mathbf{X}}\cdot\mathbf{X} + \mathbf{X}^2) - (\dot{\mathbf{X}}^2 - 2\dot{\mathbf{X}}\cdot\mathbf{X} + \mathbf{X}^2) = 4\dot{\mathbf{X}}\cdot\mathbf{X}$，因此：

$$\ln\frac{P[X|\mathbf{X}_0]}{P[\tilde{X}|\mathbf{X}_T]} = -\int_0^T \dot{\mathbf{X}}\cdot\mathbf{X}\,dt$$

这恰好等于环境熵变（在过阻尼系统中，$-\dot{\mathbf{X}}\cdot\mathbf{X}$ 对应外力乘以位移的热耗散率）：

$$\Delta S_E = \int_0^T dt\, \stackrel{1/2}{\odot}\,[-\dot{\mathbf{X}} \cdot \mathbf{X}]$$

物理含义：在过阻尼系统中，总机械力与位移的乘积等于向环境的热耗散，这与 Stratonovich 中点格式下的计算结果一致（结果与 $\lambda$ 无关）。

系统熵变定义为始末状态概率之比的对数：

$$\Delta S = \ln\left[\frac{p(\mathbf{X}(0), 0)}{p(\mathbf{X}(T), T)}\right]$$

前面的环境熵变

$$
\Delta S_E
$$

来自路径权重之比，描述的是这条轨迹在演化过程中向环境耗散了多少热。系统熵变

$$
\Delta S
$$

则不是从路径 action 里读出来的，而是从**轨迹起点和终点分别落在多大概率密度的位置上**读出来的。

原文这里采用的是随机热力学里的 `trajectory-dependent system entropy` 定义：在任意时刻 $t$，沿着一条具体轨迹看到系统处在状态 $\mathbf{X}_t$，就把这条轨迹当下的系统熵定义成

$$
S_{\mathrm{sys}}(t) = -\ln p(\mathbf{X}_t,t).
$$

这一定义的意思是：

- 如果系统此刻落在一个概率密度很高的位置，那么 $p(\mathbf{X}_t,t)$ 大，$-\ln p(\mathbf{X}_t,t)$ 小；
- 如果系统此刻落在一个概率密度很低的位置，那么 $p(\mathbf{X}_t,t)$ 小，$-\ln p(\mathbf{X}_t,t)$ 大。

这里的系统熵不是“整个系综的 Shannon 熵”本身，而是：

`对一条具体轨迹来说，它当前落点在整体概率分布里有多稀有。`

一旦接受这个定义，系统熵变就只是终点减起点：

$$
\Delta S
=
S_{\mathrm{sys}}(T)-S_{\mathrm{sys}}(0)
=
\bigl[-\ln p(\mathbf{X}(T),T)\bigr]-\bigl[-\ln p(\mathbf{X}(0),0)\bigr].
$$

把两个负号合并，就得到

$$
\Delta S = \ln\left[\frac{p(\mathbf{X}(0), 0)}{p(\mathbf{X}(T), T)}\right].
$$

所以这个式子不是一个额外假设，而只是把

$$
S_{\mathrm{sys}}(t)=-\ln p(\mathbf{X}_t,t)
$$

在起点和终点各算一次，再做差。

这样再看它的物理含义就更清楚了：

- 如果轨迹最后落在一个比起点更不常见的位置，那么
  $$
  p(\mathbf{X}(T),T)<p(\mathbf{X}(0),0),
  $$
  因而 $\Delta S>0$；
- 如果轨迹最后落在一个更常见的位置，那么 $\Delta S<0$。

系统熵变衡量的是：这条轨迹把系统从“在当前分布里较常见的位置”带到了“较罕见的位置”，还是反过来。

在这篇文章里，起点和终点的分布都可以解析写出：起点来自原始高斯混合数据分布，终点来自经过前向扩散后时刻 $T$ 的高斯混合分布。因此原文可以把

$$
\Delta S
$$

进一步写成方程 `(21)` 里那个显式的对数比。

**路径概率比分解为 $\Delta S_E + \Delta S$。** 包含初始条件的完整路径概率为 $P[X([T])] = p(\mathbf{X}_0, 0)\cdot P[X|\mathbf{X}_0]$；时间反转路径的完整概率为 $P[\tilde{X}([T])] = p(\mathbf{X}_T, T)\cdot P[\tilde{X}|\mathbf{X}_T]$（反转路径从 $\tilde{\mathbf{X}}_0 = \mathbf{X}_T$ 出发）。取完整路径概率的对数比：

$$\ln\frac{P[X([T])]}{P[\tilde{X}([T])]} = \underbrace{\ln\frac{p(\mathbf{X}_0, 0)}{p(\mathbf{X}_T, T)}}_{=\,\Delta S} \;+\; \underbrace{\ln\frac{P[X|\mathbf{X}_0]}{P[\tilde{X}|\mathbf{X}_T]}}_{=\,\Delta S_E} = \Delta S + \Delta S_E = \Delta S_{\text{tot}}$$

因此总熵变 $\Delta S_{\text{tot}} = \Delta S_E + \Delta S$ 满足**详细涨落定理**（detailed fluctuation theorem）：

$$\frac{P[X([T])]}{P[\tilde{X}([T])]} = e^{\Delta S_{\text{tot}}}$$

$\Delta S_E$、$\Delta S$ 和 $\Delta S_{\text{tot}}$ 都不是单个固定常数，而是**路径依赖量**。一旦固定一条具体轨迹 $X([T])$，这条轨迹就有自己的

$$
\Delta S_E[X],\qquad \Delta S[X],\qquad \Delta S_{\text{tot}}[X].
$$

不同轨迹通常对应不同的总熵变，因此后面写

$$
\left\langle e^{-\Delta S_{\text{tot}}}\right\rangle
$$

时，真正的意思是：对所有可能轨迹，用各自的路径概率做权重，对

$$
e^{-\Delta S_{\text{tot}}[X]}
$$

做平均。

**从详细涨落定理推导积分涨落定理。** 对 $e^{-\Delta S_{\text{tot}}}$ 在所有前向轨迹上取系综平均：

$$\langle e^{-\Delta S_{\text{tot}}} \rangle = \int \mathcal{D}[X]\, P[X([T])]\, e^{-\Delta S_{\text{tot}}}$$

利用详细涨落定理 $e^{-\Delta S_{\text{tot}}} = P[\tilde{X}([T])]/P[X([T])]$ 代入，$P[X]$ 与分母对消：

$$= \int \mathcal{D}[X]\, P[\tilde{X}([T])]$$

由于对所有前向路径 $X$ 的求和与对所有反转路径 $\tilde{X}$ 的求和构成一一对应，且概率归一化 $\int \mathcal{D}[\tilde{X}]\,P[\tilde{X}] = 1$，故：

$$\langle e^{-\Delta S_{\text{tot}}} \rangle = 1$$

这就是**积分涨落定理**（integral fluctuation theorem）。

从这里到随机热力学第二定律，还要再走一步 Jensen 不等式。由于指数函数是凸函数，对任意随机变量 $Y$ 都有

$$
\langle e^{-Y}\rangle \ge e^{-\langle Y\rangle}.
$$

现在取

$$
Y=\Delta S_{\text{tot}},
$$

就得到

$$
\left\langle e^{-\Delta S_{\text{tot}}}\right\rangle
\ge
e^{-\langle \Delta S_{\text{tot}}\rangle}.
$$

但积分涨落定理已经给出左边正好等于 $1$，因此

$$
1 \ge e^{-\langle \Delta S_{\text{tot}}\rangle}.
$$

由于指数函数单调递增，这等价于

$$
0 \ge -\langle \Delta S_{\text{tot}}\rangle,
$$

也就是

$$
\langle \Delta S_{\text{tot}} \rangle \ge 0.
$$

这就是随机热力学第二定律。它的意思不是“每条轨迹的熵都一定增加”，而是：虽然个别轨迹可以出现负的总熵变，但所有轨迹按路径概率平均之后，总熵变不能为负。

![图2：正向OU过程的积分涨落定理数值验证](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-05-figure-01.jpg)

**图 2 的角色**：用一维 OU 过程的数值模拟验证积分涨落定理。随着用于计算系综平均的轨迹数增加，$\langle e^{-\Delta S_{\text{tot}}} \rangle$ 收敛至理论预测值 1，确认正向扩散过程严格满足涨落定理。

### 2.4 正向过程的熵分布统计

![图3(a)：正向过程系统熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-01.jpg)

![图3(b)：正向过程环境熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-02.jpg)

![图3(c)：正向过程总熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-03.jpg)

![图3(d)：正向过程 exp(-ΔS_tot) 直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-04.jpg)

**图 3 的角色**：从 10 000 条正向轨迹统计系统熵变 $\Delta S$、环境熵变 $\Delta S_E$、总熵变 $\Delta S_{\text{tot}}$ 及 $e^{-\Delta S_{\text{tot}}}$ 的分布。系统熵变以零为中心近似对称分布；环境熵变偏正值；总熵变以正值为主但存在负值涨落（个别轨迹熵减少）；$e^{-\Delta S_{\text{tot}}}$ 的分布在 1 附近聚集，与积分涨落定理一致。负熵轨迹的存在是涨落定理的本质体现——热力学第二定律是统计律而非绝对律。

### 2.5 系综熵产生率

这一节分成三层：

1. 先从 Fokker-Planck 方程写出概率流；
2. 再定义单条轨迹上的随机熵率和总熵产生率；
3. 最后对这些轨迹级对象做系综平均，得到

$$
\frac{dS(t)}{dt}=\pi-\phi.
$$

#### 第一步：Fokker-Planck 方程先告诉你概率密度怎样流动

对前向 OU 过程，原文先写 Fokker-Planck 方程

$$
\frac{\partial p(\mathbf{X}_t,t)}{\partial t}
=
-\nabla\cdot\!\big[f(\mathbf{X}_t,t)p(\mathbf{X}_t,t)\big]
+\sum_{i=1}^{d}\frac{\partial^2 p(\mathbf{X}_t,t)}{\partial X_i\partial X_i}
=
-\nabla\cdot \mathbf{J}. \tag{24}
$$

先看最后这个写法

$$
\partial_t p = -\nabla\cdot \mathbf{J},
$$

它把 FPE 写成了连续性方程：

- $p(\mathbf{X}_t,t)$ 是某个位置上的概率密度；
- $\mathbf{J}$ 是概率流；
- 概率密度随时间改变，不是因为概率凭空消失或产生，而是因为概率在状态空间里流进来或流出去。

因此，下面所有关于熵产生的讨论，实际上都会回到这个概率流

$$
\mathbf{J}=f(\mathbf{X}_t,t)p(\mathbf{X}_t,t)-\nabla p(\mathbf{X}_t,t).
$$

它有两部分来源：

- $f\,p$：漂移项推动概率云整体移动；
- $-\nabla p$：扩散项把高密度区域往低密度区域抹平。

#### 第二步：先定义轨迹级的随机熵，再求它的时间导数

接着重新引入随机熵

$$
\mathbb{S}(t)=-\ln p(\mathbf{X}_t,t). \tag{25}
$$

这和前面系统熵变的定义一致；前面用它比较起点和终点，这里把它看成一条轨迹上的时间函数，再直接对时间求导。

对

$$
\mathbb{S}(t)=-\ln p(\mathbf{X}_t,t)
$$

用链式法则求导，原文得到

$$
\dot{\mathbb{S}}(t)
=
- \frac {\partial_ {t} p (\mathbf {X} _ {t} , t)}{p (\mathbf {X} _ {t} , t)}
- \frac {\nabla p (\mathbf {X} _ {t} , t)}{p (\mathbf {X} _ {t} , t)} \cdot \dot {\mathbf {X}}. \tag{26a}
$$

这只是普通链式法则：第一项来自概率密度本身显式随时间变化，第二项来自轨迹点 $\mathbf{X}_t$ 在状态空间里移动。

然后原文把

$$
\nabla p = f p - \mathbf{J}
$$

代进去，于是

$$
\dot{\mathbb{S}}(t)
=
- \frac {\partial_ {t} p (\mathbf {X} _ {t} , t)}{p (\mathbf {X} _ {t} , t)}
- f(\mathbf{X}_t,t)\cdot \dot {\mathbf {X}}
+ \frac {\mathbf {J} \cdot \dot {\mathbf {X}}}{p (\mathbf {X} _ {t} , t)}. \tag{26b}
$$

先把这条式子和随机熵的原始定义对齐：

$$
\dot{\mathbb{S}}(t)
=
-\frac{d}{dt}\ln p(\mathbf{X}_t,t)
=
-\partial_t \ln p(\mathbf{X}_t,t)
-\dot{\mathbf{X}}\cdot \nabla \ln p(\mathbf{X}_t,t).
$$

因此，系统熵率本来就有两部分来源：

- 第一部分是**你停在当前位置不动时，周围的概率密度场本身还在随时间改变**；
- 第二部分是**轨迹在状态空间里移动，因而跨过了不同的概率密度等值面**。

`(26b)` 只是把第二部分继续拆开了。利用

$$
\frac{\mathbf{J}}{p}=f-\nabla \ln p,
$$

可以把后两项合在一起：

$$
- f(\mathbf{X}_t,t)\cdot \dot{\mathbf{X}}
+ \frac {\mathbf {J} \cdot \dot {\mathbf {X}}}{p (\mathbf {X} _ {t} , t)}
=
-\dot{\mathbf{X}}\cdot \nabla \ln p(\mathbf{X}_t,t).
$$

所以三项和熵的关系应该这样读：

- 第一项
  $$
  -\partial_t \ln p(\mathbf{X}_t,t)
  $$
  表示**在当前位置固定不动时，轨迹落点的“稀有程度”怎样随时间改变**。如果某个位置的概率密度随时间下降，那么待在同一个位置也会变得更稀有，于是随机熵上升。

- 第二项
  $$
  -f(\mathbf{X}_t,t)\cdot \dot{\mathbf{X}}
  $$
  是从“沿概率梯度移动”这部分里拆出来的漂移做功项。原文把
  $$
  f(\mathbf{X}_t,t)\cdot \dot{\mathbf{X}}
  $$
  识别成环境熵率
  $$
  \dot{\mathbb{S}}_E(t)=f(\mathbf{X}_t,t)\cdot \dot{\mathbf{X}}.
  $$
  因此，`(26b)` 里真正出现的第二项是
  $$
  -\dot{\mathbb{S}}_E(t).
  $$

- 第三项
  $$
  \frac {\mathbf {J} \cdot \dot {\mathbf {X}}}{p (\mathbf {X} _ {t} , t)}
  $$
  不是另一个独立的热力学源项，而是**在把漂移做功单独拿出去之后，保留下来的概率流修正项**。它告诉你：轨迹当前的运动方向和局部概率流
  $$
  \mathbf{J}/p
  $$
  是对齐还是相反，从而决定“运动带来的系统熵变化”剩下多少。

原文特别指出，

$$
f(\mathbf{X}_t,t)\cdot \dot{\mathbf{X}}
$$

就是单位温度下的热耗散率，也就是环境熵率

$$
\dot{\mathbb{S}}_E(t)=f(\mathbf{X}_t,t)\cdot \dot{\mathbf{X}}.
$$

于是，总熵产生率定义为

$$
\dot{\mathbb{S}}_{\mathrm{tot}}(t)
=
\dot{\mathbb{S}}_E(t)+\dot{\mathbb{S}}(t),
$$

因此，在 `(26b)` 里把第二项和 $\dot{\mathbb{S}}_E(t)$ 相加时，漂移做功项正好被抵消，只剩下第一项和第三项。代回后得到原文的

$$
\dot{\mathbb{S}}_{\mathrm{tot}}(t)
=
- \frac {\partial_ {t} p (\mathbf {X} _ {t} , t)}{p (\mathbf {X} _ {t} , t)}
+ \frac {\mathbf {J} \cdot \dot {\mathbf {X}}}{p (\mathbf {X} _ {t} , t)}. \tag{27}
$$

到这里讨论的对象仍然是**单条轨迹上的随机量**。不同轨迹一般有不同的

$$
\dot{\mathbb{S}}(t),\quad
\dot{\mathbb{S}}_E(t),\quad
\dot{\mathbb{S}}_{\mathrm{tot}}(t).
$$

#### 第三步：再从轨迹级随机熵率转到系综平均熵

原文下一步才进入 “ensemble entropy production rate”。这里不再盯一条具体轨迹，而是看整个概率分布本身的 Shannon 熵：

$$
S(t)\equiv \langle \mathbb{S}(t)\rangle
=
-\int p(\mathbf{X}_t,t)\ln p(\mathbf{X}_t,t)\,d\mathbf{X}_t. \tag{28}
$$

这里的 $S(t)$ 已经不是单条轨迹上的随机熵，而是整个分布的系综熵。

#### 第四步：为什么 Eq. (29) 会变成“对数梯度乘概率流”

现在对 `(28)` 直接求导：

$$
\frac{dS(t)}{dt}
=
\frac{d}{dt}\left(
-\int p(\mathbf{X}_t,t)\ln p(\mathbf{X}_t,t)\,d\mathbf{X}_t
\right).
$$

先把时间导数放进积分：

$$
\frac{dS(t)}{dt}
=
-\int \partial_t\!\big(p\ln p\big)\,d\mathbf{X}_t.
$$

对被积函数用乘法求导：

$$
\partial_t(p\ln p)
=
(\partial_t p)\ln p + p\,\partial_t(\ln p)
=
(\partial_t p)\ln p + \partial_t p
=
(\partial_t p)(\ln p + 1).
$$

因此

$$
\frac{dS(t)}{dt}
=
-\int (\partial_t p)(\ln p + 1)\,d\mathbf{X}_t
=
-\int (\partial_t p)\ln p\,d\mathbf{X}_t
-\int \partial_t p\,d\mathbf{X}_t.
$$

第二项可以去掉，因为总概率守恒：

$$
\int \partial_t p\, d\mathbf{X}_t = 0
$$

于是只剩

$$
\frac{dS(t)}{dt}
=
-\int (\partial_t p)\ln p\,d\mathbf{X}_t.
$$

再代入 FPE 的连续性方程

$$
\partial_t p = -\nabla\cdot \mathbf{J},
$$

得到

$$
\frac{dS(t)}{dt}
=
\int (\nabla\cdot \mathbf{J})\ln p\,d\mathbf{X}_t.
$$

现在做分部积分。若边界处概率流消失，则边界项为零，于是

$$
\int (\nabla\cdot \mathbf{J})\ln p\,d\mathbf{X}_t
=
-\int \mathbf{J}\cdot \nabla \ln p\,d\mathbf{X}_t.
$$

把向量形式按分量写开，就是

$$
\frac{d S (t)}{d t}
=
- \int \sum_ {i = 1} ^ {d} \frac {\partial \ln p \left(\mathbf {X} _ {t} , t\right)}{\partial X _ {i}} J _ {i} \, d \mathbf {X} _ {t}. \tag {29}
$$

它把“熵的变化率”改写成了“概率流沿着对数密度梯度移动”的形式：

- 如果概率流正朝着让分布更平的方向走，熵会增加；
- 如果概率流朝着更集中、更有序的方向走，熵可能下降。

#### 第五步：为什么 Eq. (30) 能拆成 $\pi-\phi$

再利用

$$
J_i = f_i p - p\frac{\partial \ln p}{\partial X_i},
$$

把

$$
\frac{\partial \ln p}{\partial X_i}
$$

写成

$$
\frac{\partial \ln p}{\partial X_i}
=
f_i-\frac{J_i}{p}.
$$

代回 `(29)`，就得到

$$
\frac {d S (t)}{d t}
=
\int \sum_ {i = 1} ^ {d}
\left[
- f _ {i} J _ {i}
+ \frac {J _ {i} ^ {2}}{p \left(\mathbf {X} _ {t} , t\right)}
\right]
d \mathbf {X} _ {t}. \tag {30a}
$$

原文把这两项分别命名为

$$
\pi \equiv \sum_i \int \frac{J_i^2}{p(\mathbf{X}_t,t)}\,d\mathbf{X}_t \ge 0,
$$

以及

$$
\phi \equiv \sum_i \int f_i(\mathbf{X}_t,t)J_i\,d\mathbf{X}_t,
$$

于是

$$
\frac{dS(t)}{dt}=\pi-\phi. \tag{30b}
$$

这里三者分别是：

- $S(t)$：系统分布 $p(\mathbf{X}_t,t)$ 的**系综熵**；
- $\phi$：系统与环境之间的**熵通量**；
- $\pi$：**总熵产生率**，也就是不可逆耗散率。

两项分别表示：

- $\pi$ 是**熵产生率**。它之所以一定非负，是因为被积函数
  $$
  \frac{J_i^2}{p}
  $$
  是平方项再除以正的概率密度。因此 $\pi$ 测量的是不可逆概率流本身带来的耗散。

- $\phi$ 是**熵通量**。它表示系统和环境之间通过漂移项交换了多少熵。它可以为正，也可以为负，所以它不是纯耗散量，而是“系统与环境之间的熵交换”。

#### 第六步：平衡态、非平衡稳态和这条分解各自对应什么

最后分三种情形：

1. **平衡态**
   
   $$
   \pi=\phi=0.
   $$
   没有概率流，熵不再变化，也没有持续耗散。

2. **一般非平衡演化**
   
   $$
   \frac{dS}{dt}=\pi-\phi
   $$
   两项都可能非零，系统熵随时间变化。

3. **非平衡稳态**
   
   $$
   \frac{dS}{dt}=0,\qquad \pi=\phi\neq 0.
   $$
   系统分布已经不再变化，因此系综熵 $S(t)$ 恒定；但熵通量 $\phi$ 和总熵产生率 $\pi$ 仍然非零。这表示系统仍持续向环境交换熵，并且总熵仍持续增加，只是系统自身的系综熵变化率恰好为零。

**系综熵不变，不等于总熵产生率为零。**

如果一个系统处在非平衡稳态，分布形状可以保持不变，但内部仍然可能有持续循环流和持续的熵产生。

#### 这和你前面几篇“熵产生”文章的脉络怎么接

这一节给出的是**全可观测、Markov、连续扩散系统**里最标准的熵产生结构：

- 路径级上，有
  
  $$
  \Delta S_E,\ \Delta S,\ \Delta S_{\mathrm{tot}}
  $$
- 系综级上，有
  
  $$
  \frac{dS}{dt}=\pi-\phi.
  $$

你前面读过的几篇文章，实际上都是在这个框架上往外推广：

- 在 [fluctuating-entropy-production-on-the-coarse-grained-level.md](/Users/jinlin/Desktop/Project/Research_Collector/digests/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level.md:12) 里，问题变成：当系统只能被粗粒化观测时，路径级熵产生怎样还能被重建、局域化，并且保留 fluctuation structure。

- 在 [learning-stochastic-thermodynamics-directly-from-correlation-and-trajectory-fluc.md](/Users/jinlin/Desktop/Project/Research_Collector/library/bridges/translation_layers/fokker_planck_master/learning-stochastic-thermodynamics-directly-from-correlation-and-trajectory-fluc.md:95) 里，重点变成：如何直接从轨迹统计里恢复 `probability velocity`、`temporal score`、`diffusion field` 这些局域对象，再把熵产生写成这些对象的组合。

- 在你今天这篇和 Sagawa 那篇自回归生成模型工作里，问题又进一步变成：当可观测过程不是简单的 Markov diffusion，而是带记忆、带隐藏状态的生成过程时，熵产生该怎样重新定义和计算。

这篇的 `(24)-(30)` 可以当成你整条熵产生主线里的“基准坐标系”：

- 它先告诉你，在最标准的 Markov 扩散设定里，熵产生和概率流之间是什么关系；
- 后面的 coarse-graining、hidden driving、non-Markovian、autoregressive 扩展，本质上都是在问：这套结构在更复杂可见性条件下还能保留多少、要怎样改写。

---

## 3. 反向生成动力学的非平衡分析

这一部分内部其实是一条连续的链：

1. 先从前向扩散推出反向生成 SDE；
2. 再把反向漂移重写成势能 / 广义自由能的梯度流；
3. 然后读取这个势能景观怎样从单阱变成双阱，从而出现分化转变；
4. 接着检查反向过程本身是否仍满足涨落定理和熵产生结构；
5. 最后再从 Franz-Parisi 势的角度刻画更晚发生的坍缩转变。

### 3.1 从前向扩散到反向生成 SDE

前向过程的短时转移核是

$$
P(\mathbf{X}_{t+dt}\mid \mathbf{X}_t)
\propto
\exp\!\left(
-\frac{|\mathbf{X}_{t+dt}-\mathbf{X}_t-f\,dt|^2}{4\,dt}
\right).
$$

要得到反向动力学，先把条件分布反过来写：

$$
P(\mathbf{X}_t\mid \mathbf{X}_{t+dt})
=
\frac{P(\mathbf{X}_{t+dt}\mid \mathbf{X}_t)\,p(\mathbf{X}_t,t)}
{p(\mathbf{X}_{t+dt},t+dt)}.
$$

令

$$
\Delta\mathbf{X}=\mathbf{X}_{t+dt}-\mathbf{X}_t,
$$

则对数条件分布可以写成

$$
\ln P(\mathbf{X}_t\mid \mathbf{X}_{t+dt})
=
-\frac{|\Delta\mathbf{X}-f\,dt|^2}{4\,dt}
+\ln p(\mathbf{X}_t,t)
-\ln p(\mathbf{X}_{t+dt},t+dt)+C.
$$

接下来只需要处理后两个对数概率项。把

$$
\ln p(\mathbf{X}_t,t)
=
\ln p(\mathbf{X}_{t+dt}-\Delta\mathbf{X},t)
$$

在 $\mathbf{X}_{t+dt}$ 附近 Taylor 展开，并把

$$
\ln p(\mathbf{X}_{t+dt},t+dt)
$$

也在小时间步下展开，就得到

$$
\ln p(\mathbf{X}_t,t)-\ln p(\mathbf{X}_{t+dt},t+dt)
\approx
-\Delta\mathbf{X}\cdot \nabla\ln p(\mathbf{X}_{t+dt},t)+O(dt).
$$

把这一项代回去，所有和 $\Delta\mathbf{X}$ 有关的部分变成

$$
-\frac{|\Delta\mathbf{X}-f\,dt|^2}{4\,dt}
-\Delta\mathbf{X}\cdot \nabla\ln p.
$$

展开并配方：

$$
-\frac{|\Delta\mathbf{X}|^2}{4\,dt}
+\frac{1}{2}\Delta\mathbf{X}\cdot f
-\Delta\mathbf{X}\cdot \nabla\ln p
\approx
-\frac{1}{4\,dt}
\left|
\Delta\mathbf{X}-(f-2\nabla\ln p)\,dt
\right|^2.
$$

因此，反向短时转移核仍是高斯的，但漂移从 $f$ 变成了

$$
f-2\nabla\ln p.
$$

这就给出反向生成 SDE：

$$
d\mathbf{X}_t
=
\left[f(\mathbf{X}_t,t)-2\nabla\ln p(\mathbf{X}_t,t)\right]dt
+\sqrt{2}\,d\bar{\mathbf{W}}_t.
$$

这里的附加项

$$
-2\nabla\ln p(\mathbf{X}_t,t)
$$

就是 score correction。前向过程把分布摊平；反向过程要把轨迹推回高密度区域，因此必须沿着 $\nabla\ln p$ 的方向补上一项逆向驱动力。

对本文的一般高斯混合模型，score 有解析表达式

$$
\nabla\ln p(\mathbf{X}_t,t)
=
\frac{
\tanh\!\left(
\dfrac{\mathbf{X}_t\cdot \boldsymbol{\mu}_t}
{1-e^{-2t}+e^{-2t}\sigma^2}
\right)\boldsymbol{\mu}_t e^{-t}
-\mathbf{X}_t
}
{1-e^{-2t}+e^{-2t}\sigma^2},
$$

在单位方差 $\sigma^2=1$ 时退化为

$$
\nabla\ln p(\mathbf{X}_t,t)
=
\tanh(\boldsymbol{\mu}_t^\top \mathbf{X}_t)\,\boldsymbol{\mu}_t-\mathbf{X}_t.
$$

实际训练扩散模型时，score 通常由网络 $s_\theta(\mathbf{X}_t,t)$ 拟合：

$$
\mathcal{L}(\theta)
=
\mathbb{E}_{\mathbf{X}_t\sim p(\mathbf{X}_t,t)}
\left[
\|s_\theta(\mathbf{X}_t,t)-\nabla\ln p(\mathbf{X}_t,t)\|^2
\right].
$$

本文的优势在于，所选高斯混合模型足够简单，score 可以解析写出，因此后面关于相变、自由能和熵产生的讨论都不需要再经过数值拟合。

### 3.2 从反向漂移到广义自由能

把反向时间记成

$$
s=T-t,
$$

则反向 SDE 的漂移项

$$
2\nabla\ln p(\tilde{\mathbf{X}}_s,T-s)-f(\tilde{\mathbf{X}}_s,T-s)
$$

可以写成某个势能的负梯度。作者在这里定义

$$
-\nabla U(\tilde{\mathbf{X}}_s,T-s)
=
2\nabla\ln p(\tilde{\mathbf{X}}_s,T-s)-f(\tilde{\mathbf{X}}_s,T-s),
$$

于是反向 SDE 被改写成标准 Langevin 形式

$$
d\tilde{\mathbf{X}}_s
=
-\nabla U(\tilde{\mathbf{X}}_s,T-s)\,ds
+\sqrt{2}\,d\mathbf{W}.
$$

这里突然出现的 $U$ 不是另加的新对象，而是把反向漂移场重新表达成势能景观之后得到的势函数。这样做的目的，是把反向生成过程从“一个带 score 的随机微分方程”改写成“粒子在时变势能景观里的 Langevin 运动”。

更一般地，原文先在任意方差的高斯混合模型上写出 score；再把它代回上面的定义，得到势能。这里的“单位方差情形”指的是：原始数据分布里的两个高斯混合分量都取

$$
\sigma^2=1.
$$

在这个特殊情形下，score 和势能都能写成更简洁的解析形式。对应的势能为

$$
U(\mathbf{X}_t,t)
=
\frac{1}{2}|\mathbf{X}_t|^2
-2\ln\cosh(\mathbf{X}_t\cdot \boldsymbol{\mu}_t).
$$

这里最好不要直接说“第一项只来自 $f$”，因为最终的

$$
\frac{1}{2}|\mathbf{X}_t|^2
$$

是两部分合并后的结果。原文先给出一般形式

$$
U(\mathbf{X}_t,t)=-2\ln p(\mathbf{X}_t,t)+\int f(\mathbf{Z},t)\,d\mathbf{Z}.
$$

对 OU 漂移

$$
f(\mathbf{X}_t,t)=-\mathbf{X}_t,
$$

第二项积分给出

$$
\int f\,d\mathbf{X}=\int (-\mathbf{X})\cdot d\mathbf{X}
=
-\frac{1}{2}|\mathbf{X}|^2.
$$

另一方面，在单位方差高斯混合下，

$$
p(\mathbf{X}_t,t)\propto
e^{-|\mathbf{X}_t|^2/2}\cosh(\mathbf{X}_t\cdot \boldsymbol{\mu}_t),
$$

因此

$$
-2\ln p(\mathbf{X}_t,t)
=
|\mathbf{X}_t|^2
-2\ln\cosh(\mathbf{X}_t\cdot \boldsymbol{\mu}_t)
+\text{const}.
$$

把这两部分相加：

$$
U
=
\left[
|\mathbf{X}_t|^2
-2\ln\cosh(\mathbf{X}_t\cdot \boldsymbol{\mu}_t)
\right]
-\frac{1}{2}|\mathbf{X}_t|^2
+\text{const}
=
\frac{1}{2}|\mathbf{X}_t|^2
-2\ln\cosh(\mathbf{X}_t\cdot \boldsymbol{\mu}_t)
+\text{const}.
$$

所以更准确地说：

- 二次项
  $$
  \frac{1}{2}|\mathbf{X}_t|^2
  $$
  反映的是 OU 恢复力对应的二次约束，但它在最终表达式里是通过漂移积分项和 $-2\ln p$ 里的高斯因子合并后留下的结果；
- 双阱修正项
  $$
  -2\ln\cosh(\mathbf{X}_t\cdot \boldsymbol{\mu}_t)
  $$
  则来自混合分布结构带来的 score 非线性。

接下来，原文把同一个反向动力学翻译成一个统计推断问题。顺序是：先用 `(45)` 把含噪分布写成前向高斯核与数据先验的卷积，再用 `(46)` 把 score 写成后验平均残差，最后才在 `(47)` 里写出后验分布本身。

前向 OU 过程告诉我们：给定原始样本 $\mathbf{X}_0$，时刻 $t$ 的含噪状态是一个高斯核

$$
P(\mathbf{X}_t\mid \mathbf{X}_0,t)
=
\mathcal N(e^{-t}\mathbf{X}_0,\Sigma_t \mathbf I_d),
\qquad
\Sigma_t=1-e^{-2t}.
$$

因此，边际分布 $p(\mathbf{X}_t,t)$ 就是把这个高斯核对数据先验 $p(\mathbf{X}_0)$ 做卷积：

$$
p(\mathbf{X}_t,t)
=
\int
\mathcal N(\mathbf{X}_t; e^{-t}\mathbf{X}_0,\Sigma_t \mathbf I_d)\,
p(\mathbf{X}_0)\,d\mathbf{X}_0. \tag{45}
$$

这一步的意思很具体：时刻 $t$ 的分布不是凭空出现的，而是“原始数据分布经过高斯模糊之后”的结果。

接着对这个卷积形式求 score。把梯度直接打到被积函数上，并利用高斯核的导数

$$
\nabla_{\mathbf{X}_t}
\ln \mathcal N(\mathbf{X}_t; e^{-t}\mathbf{X}_0,\Sigma_t \mathbf I_d)
=
-\Sigma_t^{-1}(\mathbf{X}_t-e^{-t}\mathbf{X}_0),
$$

就得到

$$
\begin{aligned}
\nabla\ln p(\mathbf{X}_t,t)
=\Sigma_t^{-1}
\Bigg[
\frac{
\int d\mathbf{X}_0\,
p(\mathbf{X}_0)\,
\mathcal N(\mathbf{X}_t; e^{-t}\mathbf{X}_0,\Sigma_t \mathbf I_d)\,
e^{-t}\mathbf{X}_0
}{
\int d\mathbf{X}_0\,
p(\mathbf{X}_0)\,
\mathcal N(\mathbf{X}_t; e^{-t}\mathbf{X}_0,\Sigma_t \mathbf I_d)
}
-\mathbf{X}_t
\Bigg].
\end{aligned}
\tag{46}
$$

分子除以分母，正好就是“在给定当前 $\mathbf{X}_t$ 的条件下，对 $e^{-t}\mathbf{X}_0$ 的后验平均”。所以 `(46)` 可以更紧地写成

$$
\nabla\ln p(\mathbf{X}_t,t)
=
\Sigma_t^{-1}
\left[
\langle e^{-t}\mathbf{X}_0\rangle_{\mathbf{X}_t}
-\mathbf{X}_t
\right].
$$

这一步是整条逻辑的关键：score 不是一个孤立出现的向量场，而是“当前含噪点 $\mathbf{X}_t$ 相对于后验去噪估计 $\langle e^{-t}\mathbf{X}_0\rangle_{\mathbf{X}_t}$ 还有多少残差”。

也正因为 `(46)` 把 score 写成了后验平均，原文才顺势把反向生成解释成统计推断。给定当前含噪状态 $\mathbf{X}_t$，原始数据 $\mathbf{X}_0$ 的后验由 Bayes 公式给出：

$$
P(\mathbf{X}_0\mid \mathbf{X}_t,t)
=
\frac{P(\mathbf{X}_t\mid \mathbf{X}_0,t)\,p(\mathbf{X}_0)}
{p(\mathbf{X}_t,t)}. \tag{47}
$$

把高斯转移核代进去，并忽略只依赖于 $\mathbf{X}_t$ 的归一化常数，就得到

$$
P(\mathbf{X}_0\mid \mathbf{X}_t,t)
\propto
\exp[-\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)],
$$

其中

$$
\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)
=
\frac{1}{2}
(\mathbf{X}_t-e^{-t}\mathbf{X}_0)^\top
\Sigma_t^{-1}
(\mathbf{X}_t-e^{-t}\mathbf{X}_0)
-\ln p(\mathbf{X}_0).
$$

这条 Hamiltonian 里有两部分：

- 第一项是高斯似然对应的二次失配代价，衡量“这个候选原始样本 $\mathbf{X}_0$ 经过前向扩散后，和当前观测 $\mathbf{X}_t$ 相差多远”；
- 第二项 $-\ln p(\mathbf{X}_0)$ 是先验代价，衡量这个候选原始样本本身在数据分布里有多不典型。

因此，这一段的逻辑顺序是：

1. `(45)` 先把含噪分布写成“前向高斯核和数据先验的卷积”；
2. `(46)` 再说明 score 等于一个后验平均残差；
3. `(47)` 最后把这个后验显式写出来，于是反向生成被重写成“给定当前含噪观测，对原始样本做 Bayesian inference”。

定义配分函数

$$
Z(\mathbf{X}_t,t)=\int d\mathbf{X}_0\,e^{-\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)},
$$

自由能定义为

$$
F(\mathbf{X}_t,t)=-\frac{1}{\beta}\ln Z(\mathbf{X}_t,t),
\qquad
\beta=\Sigma_t^{-1}.
$$

由于

$$
Z(\mathbf{X}_t,t)
=(2\pi\Sigma_t)^{d/2}p(\mathbf{X}_t,t),
$$

可得

$$
F
=
-\Sigma_t\left[
\ln p(\mathbf{X}_t,t)
+\frac{d}{2}\ln(2\pi\Sigma_t)
\right].
$$

对 $\mathbf{X}_t$ 求梯度，得到

$$
\nabla F
=
-\Sigma_t\,\nabla\ln p(\mathbf{X}_t,t)
=
-\frac{1}{\beta}\nabla\ln p(\mathbf{X}_t,t).
$$

这说明普通自由能 $F$ 只抓住了 score 那一部分驱动力，因为

$$
\nabla(2\beta F)=-2\nabla\ln p(\mathbf{X}_t,t).
$$

而反向 SDE 的完整漂移是

$$
2\nabla\ln p(\mathbf{X}_t,t)-f(\mathbf{X}_t,t).
$$

所以如果想把整条反向动力学都写成某个标量函数的负梯度形式，就不能只用 $F$，还要把漂移场 $f$ 对应的那一部分也并进去。原文因此定义广义自由能

$$
\tilde F = 2\beta F + \int f\,d\tilde{\mathbf{X}}_s,
$$

因为

$$
\nabla\!\left(\int f\,d\tilde{\mathbf{X}}_s\right)=f,
$$

所以立刻有

$$
\nabla \tilde F
=
\nabla(2\beta F)+\nabla\!\left(\int f\,d\tilde{\mathbf{X}}_s\right)
=
-2\nabla\ln p+f,
$$

从而

$$
-\nabla \tilde F
=
2\nabla\ln p-f.
$$

这正好等于反向 SDE 里的完整驱动力。这样定义 $\tilde F$，不是额外引入一个新量，而是为了让“广义自由能的负梯度”与“反向生成动力学的漂移”完全对齐。

对 OU 漂移 $f=-\mathbf{X}$，这个积分项可以直接算成

$$
\int f\,d\mathbf{X}=-\frac{1}{2}|\mathbf{X}|^2,
$$

因此

$$
\tilde F
=
2\beta F-\frac{1}{2}|\mathbf{X}_t|^2
=
\frac{1}{2}|\mathbf{X}_t|^2-2\ln\cosh(\mathbf{X}_t\cdot\boldsymbol{\mu}_t)
=
U.
$$

所以在 OU 情形下，前面从反向漂移直接定义出来的势能 $U$，和这里从统计推断出发构造出来的广义自由能 $\tilde F$，其实是同一个对象。前者强调它是反向 Langevin 动力学的势能景观，后者强调它来自自由能与漂移场的组合；两条路最后汇到同一个函数上。

### 3.3 从单阱到双阱：分化转变与相图

![图4：势能随时间的演化（μ=1，一维）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-01.jpg)

![图4续：t=0.35 时势能接近临界](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-02.jpg)

![图4续：t=0.1 时势能呈双阱](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-03.jpg)

有了势能 $U(\mathbf{X}_t,t)$ 之后，下一件事就是看这个景观怎样随时间改变。图 4 给出的正是一维例子：

- 在较大时间处，势能还是单阱；
- 到临界时间附近，原点附近开始变平；
- 再往后，单阱分裂成双阱。

这里先要说明为什么盯着原点 $X=0$ 看就够了。对于对称的双峰数据，势能 $U(X,t)$ 关于原点是偶函数，因此原点始终是最自然的候选中心点。问题不在于原点会不会移动，而在于原点附近的曲率会不会变号：

- 如果原点处曲率为正，原点就是局部极小值，势能景观仍然是单阱；
- 如果原点处曲率降到零，原点附近开始变平，系统正好到达单阱失稳的临界点；
- 如果原点处曲率变成负值，原点变成局部极大值，左右两侧才会分裂出新的极小值，景观从单阱变成双阱。

所以所谓 speciation transition，不是凭直觉判断“图像开始分叉”，而是用原点处二阶导数变号来精确定义。临界时间 $t_S$ 就由“原点处凸性消失”这个条件给出：

$$
\left.\frac{\partial^2 U}{\partial X^2}\right|_{X=0}(t_S)=0.
$$

把单位方差情形下的势能

$$
U(X,t)=\frac{1}{2}X^2-2\ln\cosh(\mu_t X),
\qquad
\mu_t=\mu e^{-t},
$$

代进去，先对 $X$ 求一次导数：

$$
\frac{\partial U}{\partial X}
=
X-2\mu_t\tanh(\mu_t X),
$$

再求二阶导数：

$$
\frac{\partial^2 U}{\partial X^2}
=
1-2\mu_t^2\,\operatorname{sech}^2(\mu_t X).
$$

在原点 $X=0$ 处有 $\operatorname{sech}^2(0)=1$，所以

$$
\left.\frac{\partial^2 U}{\partial X^2}\right|_{X=0}
=
1-2\mu_t^2.
$$

令它等于零，就得到临界条件

$$
\mu^2 e^{-2t_S}=\frac{1}{2}.
$$

这就是本文所谓的 speciation transition。它的含义不是“样本已经生成完成”，而是：从这个时刻开始，原点不再是稳定的唯一吸引中心，轨迹第一次可以稳定地向左右两个数据簇分开演化。

对一般均值 $\mu$ 和方差 $\sigma^2$，临界时间推广为

$$
t_S
=
\frac{1}{2}
\ln\!\left(
\mu^2+\sqrt{\sigma^4-2\sigma^2+\mu^4+1}
\right).
$$

![图5：一维情形的对称性破缺相图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-04.jpg)

Figure 5 不是数值模拟扫出来的经验图，而是把前面得到的两个解析判据放到 $(\mu,\sigma)$ 平面里之后得到的相图。顺序要按这两条判据来读。

第一条判据决定“会不会发生分化转变”。前面已经得到，一维任意均值和方差下的分化时间是

$$
t_S
=
\frac{1}{2}
\ln\!\left(
\mu^2+\sqrt{\sigma^4-2\sigma^2+\mu^4+1}
\right).
$$

如果这个 $t_S$ 没有正实解，或者等于零，说明在实际反向生成开始之前，原点处的曲率还没有来得及变号，势能始终保持单阱，于是不会发生簇级分化。这就给出了图 5 里绿色区域和棕色区域之间的那条弯曲边界。把 $t_S=0$ 代进去，可以把它改写成更直观的显式形式：

$$
\mu^2+\sqrt{\sigma^4-2\sigma^2+\mu^4+1}=1
\quad \Longleftrightarrow \quad
\mu^2=\sigma^2-\frac{\sigma^4}{2}.
$$

这条曲线以下、同时又不触发第二条判据时，会进入稳定对称性破缺相；这条曲线以上，则保持对称性未破缺。

第二条判据决定“即使双阱出现了，它是不是稳定的”。原文在 Appendix B 里检查了大振幅极限下的势能斜率，发现当

$$
t_{USB}=\frac{1}{2}\ln(\sigma^2-1)
$$

变成非负时，双阱外侧的斜率会翻成正号，势能在大振幅处不再把轨迹拉回，而是变成向外逃逸的上坡。把 $t_{USB}=0$ 代进去，就得到图 5 里那条水平边界：

$$
\sigma^2=2
\qquad
(\text{即 } \sigma=\sqrt{2}).
$$

这条水平线以上，就是原文所说的 `unstable symmetry breaking`：局部上可能已经出现双阱，但整个势能轮廓在远处失稳，生成轨迹会逃向无穷远，采样失败。

所以图 5 要这样读：

1. 先看水平线 $\sigma=\sqrt{2}$。这条线以上，不管 $\mu$ 多大，都会进入不稳定对称性破缺相，因为大振幅斜率已经翻正。
2. 再看水平线以下的区域。这时大振幅还稳定，真正决定是否分化的是那条由 $t_S=0$ 给出的弯曲边界。
3. 弯曲边界左上方的绿色区域是 `no symmetry breaking`：原点始终稳定，势能保持单阱。
4. 弯曲边界右下方的棕色区域是 `symmetry breaking`：原点先失稳，再长出稳定双阱，轨迹可以正常分化到两个数据簇。
5. 最上方的红色区域是 `unstable symmetry breaking`：双阱结构即使局部出现，也会被远处的不稳定斜率破坏。

因此，Figure 5 的核心结论不是“参数空间有三种颜色”，而是：这一维高斯混合模型里，生成是否成功需要同时满足两件事，

1. 原点必须先失稳，才能发生簇级分化；
2. 双阱在大振幅处还必须保持稳定，生成轨迹才不会逃逸。

![图6(a)：稳定对称性破缺（μ=1, σ=0.8）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-11-figure-01.jpg)

![图6(b)：对称性未破缺（μ=0.4, σ=1）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-11-figure-04.jpg)

![图6(c)：不稳定对称性破缺（μ=4, σ=1.5）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-11-figure-07.jpg)

图 6 就是在给 Figure 5 的三块区域各挑一个代表点：

1. $(\mu,\sigma)=(1,0.8)$：先穿过 $t_S$，又始终不触发 $t_{USB}$，所以形成稳定双阱；
2. $(\mu,\sigma)=(0.4,1)$：始终没有正的 $t_S$，所以保持单阱；
3. $(\mu,\sigma)=(4,1.5)$：虽然会发生局部分化，但因为 $\sigma>\sqrt2$，最终会触发不稳定对称性破缺，势能外侧翻成向外逃逸的上坡。

这样，Section III 里的相变分析就和前面的动力学景观直接接上了：不是抽象说“有相变”，而是先有两条解析判据，再有三块参数区域，最后才在 Figure 6 里看到对应的势能形状。

### 3.4 反向过程的涨落定理

这一节把正向过程在 `2.2` 和 `2.3` 里做过的那套路径积分构造，重新对反向生成动力学做一遍。顺序和前面一样：

1. 先写反向 SDE；
2. 再把它离散化成单步更新；
3. 用噪声分布做变量替换，得到单步转移核；
4. 把单步转移核连乘成整条路径的权重；
5. 再把“同一条几何路径的反向走法”写出来，与正向走法做概率比；
6. 最后定义环境熵变、系统熵变和总熵变，推出积分涨落定理。

原文先给出已经推导好的反向生成 SDE：

$$
d\tilde{\mathbf{X}}_s
=
\left[
2\tanh(\boldsymbol{\mu}_{T-s}^\top \tilde{\mathbf{X}}_s)\boldsymbol{\mu}_{T-s}
-\tilde{\mathbf{X}}_s
\right]ds
+\sqrt{2}\,d\mathbf{W},
$$

它和前面的反向 SDE 是同一个动力学，只是把时间变量换成了随生成过程递增的

$$
s=T-t.
$$

这样写的好处是：生成轨迹现在和正向扩散一样，都是沿着“时间从 0 累积到 $T$”的方向来写，后面做路径积分时更方便。接下来原文对这条 SDE 使用与前面完全相同的 $\lambda$-离散化：

$$
\frac {\tilde {\mathbf {X}} _ {s + d s} - \tilde {\mathbf {X}} _ {s}}{d s}
=
\left[
2 \tanh  \left(\boldsymbol {\mu} _ {T - s - \lambda d s} ^ {\top} \{\lambda \tilde {\mathbf {X}} _ {s + d s} + (1 - \lambda) \tilde {\mathbf {X}} _ {s} \}\right) \boldsymbol {\mu} _ {T - s - \lambda d s}
-
(\lambda \tilde {\mathbf {X}} _ {s + d s} + (1 - \lambda) \tilde {\mathbf {X}} _ {s})
\right]
+
\sqrt {2} \boldsymbol {\eta} _ {s},
\tag{54}
$$

其中

$$
\boldsymbol{\eta}_s\sim\mathcal N\!\left(0,\frac{1}{ds}\mathbf I_d\right).
$$

这一步的意思和前向过程完全一样：固定当前点 $\tilde{\mathbf X}_s$ 之后，下一步状态 $\tilde{\mathbf X}_{s+ds}$ 与噪声 $\boldsymbol{\eta}_s$ 之间建立了局部一一对应关系，因此可以再次用噪声高斯分布来构造单步转移核。原文得到

$$
\begin{aligned}
P \left(\tilde {\mathbf {X}} _ {s + d s} \mid \tilde {\mathbf {X}} _ {s}\right)
&=
P \left(\sqrt {2} \boldsymbol {\eta}\right)
\left| \frac {\partial \sqrt {2} \boldsymbol {\eta}}{\partial \tilde {\mathbf {X}} _ {s + d s}} \right| \\
&\propto
\exp \Bigg[
- \frac {\left(\dot {\tilde {\mathbf {X}}} _ {s} - 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}} _ {s}\right) \boldsymbol {\mu} _ {T - s} + \tilde {\mathbf {X}} _ {s}\right) ^ {2} d s}{4}
- \lambda \nabla \cdot \left(2 \tanh \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}} _ {s}\right) \boldsymbol {\mu} _ {T - s} - \tilde {\mathbf {X}} _ {s}\right)
\Bigg].
\end{aligned}
\tag{55}
$$

这里的两部分和前向过程逐项对应：

- 第一项来自噪声高斯分布，给出轨迹偏离确定性漂移的代价；
- 第二项来自 Jacobian，记录漂移场对局部体积元的压缩或膨胀。

再把这些单步转移核沿时间方向连乘，就得到整条反向生成轨迹 $\tilde X([T])$ 的条件路径权重：

$$
\begin{aligned}
P \left(\tilde {X} ([ T ]) \mid \tilde {\mathbf {X}} _ {0}\right)
&=
\prod_ {s} P \left(\tilde {\mathbf {X}} _ {s + d s} \mid \tilde {\mathbf {X}} _ {s}\right) \\
&\propto
\exp\!\Bigg\{
- \int_ {0} ^ {T} d s \overset {\lambda} {\odot}
\left[
\frac {\left(\dot {\mathbf {x}} - 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {x}}\right) \boldsymbol {\mu} _ {T - s} + \tilde {\mathbf {x}}\right) ^ {2}}{4}
+ \lambda \nabla \cdot \left( 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {x}}\right) \boldsymbol {\mu} _ {T - s} - \tilde {\mathbf {x}} \right)
\right]
\Bigg\}.
\end{aligned}
\tag{56}
$$

原文再把指数里的积分记成路径作用量 $\mathcal A(\tilde X([T]))$，写成

$$
\begin{aligned}
P (\tilde {X} ([ T ]) \mid \tilde {\mathbf {X}} _ {0})
=
\mathcal {N} \exp \left[ - \mathcal {A} (\tilde {X} ([ T ])) \right],
\qquad
\mathcal {A} (\tilde {X} ([ T ]))
=
\int_ {0} ^ {T} d s \stackrel {\lambda} {\odot}
\left[
\frac {\left(\dot {\tilde {\mathbf {X}}} - 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}}\right) \boldsymbol {\mu} _ {T - s} + \tilde {\mathbf {X}}\right) ^ {2}}{4}
+ \lambda \nabla \cdot [ 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}}\right) \boldsymbol {\mu} _ {T - s} - \tilde {\mathbf {X}} ]
\right].
\end{aligned}
\tag{57–58}
$$

到这里为止，和正向过程的结构完全一致，只是漂移场从线性的 OU 力变成了带 $\tanh$ 的非线性生成漂移。

下一步原文要构造的不是另一条独立轨迹，而是**同一条几何路径的反向走法**。记

$$
\tilde X([T])
$$

为按生成时间 $s$ 从 $0$ 走到 $T$ 的轨迹，再记

$$
X([T])
$$

为把这条同样的路径反过来走一遍得到的轨迹。两者满足

$$
\mathbf X(t)=\tilde{\mathbf X}(s),
\qquad
s=T-t,
\qquad
\dot{\mathbf X}(t)=-\dot{\tilde{\mathbf X}}(s).
$$

因此，路径作用量里所有与速度有关的项都会发生

$$
\dot{\tilde{\mathbf X}}\longrightarrow -\dot{\tilde{\mathbf X}}
$$

同时，时间反演把离散化中“左端点 / 右端点”的角色对调，所以 $\lambda$-约定也相应变成 $1-\lambda$。原文因此写出这条反向走法的路径权重：

$$
\begin{aligned}
P (X ([ T ]) \mid \mathbf {X} _ {0})
=
\mathcal {N} \exp [ - \mathcal {A} (X ([ T ])) ],
\qquad
\mathcal {A} (X ([ T ]))
=
\int_ {0} ^ {T} d s \stackrel {1 - \lambda} {\odot}
\left[
\frac {\left(- \dot {\tilde {\mathbf {X}}} - 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}}\right) \boldsymbol {\mu} _ {T - s} + \tilde {\mathbf {X}}\right) ^ {2}}{4}
+ \lambda \nabla \cdot \left( 2 \tanh  \left(\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}}\right) \boldsymbol {\mu} _ {T - s} - \tilde {\mathbf {X}} \right)
\right].
\end{aligned}
\tag{59–60}
$$

有了这两条路径权重之后，环境熵变就仍然按“正向走法与反向走法的条件路径概率之比”来定义：

$$
\Delta S _ {E}
=
\ln \left[ \frac {P (\tilde {X} ([ T ]) \mid \tilde {\mathbf {X}} _ {0})}{P (X ([ T ]) \mid \mathbf {X} _ {0})} \right].
\tag{61a}
$$

把上面的两个作用量相减，原文得到

$$
\Delta S _ {E}
=
\int_ {0} ^ {T} d s \stackrel {\frac {1}{2}} {\odot}
\left[
\dot {\tilde {\mathbf {X}}} \cdot \left(2 \tanh (\boldsymbol {\mu} _ {T - s} ^ {\top} \tilde {\mathbf {X}}) \boldsymbol {\mu} _ {T - s} - \tilde {\mathbf {X}} \right)
\right].
\tag{61b}
$$

这一步的物理意义和正向过程没有变化：环境熵变来自轨迹沿着反向漂移场运动时向环境释放或吸收的热。

系统熵变仍然只看始末两端状态在分布中的相对稀有程度：

$$
\Delta S
=
\ln \left[ \frac {p (\tilde {\mathbf {X}} _ {0})}{p (\tilde {\mathbf {X}} _ {T})} \right].
\tag{62a}
$$

在这篇双峰高斯模型里，作者把它显式写成

$$
\Delta S
=
\ln \left[
\frac {\exp \left(- \frac {(\tilde {\mathbf {X}} _ {0} - \boldsymbol {\mu} e ^ {- T}) ^ {2}}{2}\right) + \exp \left(- \frac {(\tilde {\mathbf {X}} _ {0} + \boldsymbol {\mu} e ^ {- T}) ^ {2}}{2}\right)}
{\exp \left(- \frac {(\tilde {\mathbf {X}} _ {T} - \boldsymbol {\mu}) ^ {2}}{2}\right) + \exp \left(- \frac {(\tilde {\mathbf {X}} _ {T} + \boldsymbol {\mu}) ^ {2}}{2}\right)}
\right].
\tag{62b}
$$

总熵变就是这两部分之和：

$$
\Delta S _ {t o t}
=
\Delta S _ {E} + \Delta S
=
\ln \left[ \frac {P \left[ \tilde {X} ([ T ]) \right]}{P [ X ([ T ]) ]} \right].
\tag{63}
$$

这里最后一个等式说明：把环境熵变的条件路径概率比和系统熵变的端点分布比合在一起，恰好得到**完整轨迹概率**的对数比。

然后和正向过程一样，对 $e^{-\Delta S_{\mathrm{tot}}}$ 做路径平均：

$$
\begin{aligned}
\left\langle e ^ {- \Delta S _ {t o t}} \right\rangle
&=
\int P \left[ \tilde {X} ([ T ]) \right] e ^ {- \Delta S _ {t o t}} d \tilde {X} ([ T ]) \\
&=
\int P [ X ([ T ]) ] d X ([ T ]) \\
&=
1.
\end{aligned}
\tag{64}
$$

![图7：反向生成过程的积分涨落定理数值验证](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-14-figure-01.jpg)

因此，反向生成动力学虽然已经是强非线性的去噪过程，但它在路径级上仍然满足和正向扩散同样的积分涨落定理。图 7 的数值结果就是在验证这一点：对越来越多条反向生成轨迹做平均时，$\langle e^{-\Delta S_{\mathrm{tot}}}\rangle$ 收敛到理论值 1。

### 3.5 反向过程的熵分布与熵产生率

![图8(a)：反向过程系统熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-15-figure-01.jpg)

![图8(d)：反向过程 exp(-ΔS_tot) 直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-15-figure-04.jpg)

图 8 表明，反向过程里的系统熵变和总熵变都更偏向正值。直观地说，轨迹正在从“高噪声、低结构”的状态走向“低噪声、有结构”的状态，因此系统内部的有序性在上升；但环境熵增加得更多，所以总熵仍然满足第二定律。

再往下，原文比较正向和反向两套系综熵产生率。关键事实是：

- 正向和反向共享相同的边际分布 $p(\mathbf{X}_t,t)$；
- 两者的概率流大小相同、方向相反：
  $$
  \mathbf{J}^*=-\mathbf{J}.
  $$

因此，正向和反向的熵产生率相同：

$$
\pi^*=\pi,
$$

但熵通量不同，因为两者的漂移场不同。

![图9：正向OU过程的熵产生率和熵通量](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-16-figure-01.jpg)

![图10：反向生成过程的熵产生率和熵通量](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-16-figure-02.jpg)

这两张图最好按“先看前向基线，再看反向生成”来读。

先看图 9。它给的是前向 OU 过程的基线行为：

1. 熵产生率 $\pi(t)$ 单调下降并最终趋近于零；
2. 系综熵变化率 $\dot S(t)$ 先下降，再回升到零；
3. 这对应的是普通扩散弛豫：系统逐步靠近平衡，所有热力学速率量最终都消失。

有了这个基线，再看图 10 里的反向生成过程，读图顺序应该是：

1. 熵产生率 $\pi^*(t)$ 仍然保持非负；
2. 熵通量 $\phi^*(t)$ 一开始是负的，说明系统最初并不是在向环境排出熵，而是在把噪声态重新拉回有结构的数据流形；
3. 随着时间推进，$\phi^*(t)$ 会穿过零点并变成正值；原文特别指出，这个符号翻转发生在早于分化转变时刻 $t_S$ 的某个时刻；
4. 系综熵变化率 $\dot S^*(t)$ 在早期先是正的，但在接近 $t_S$ 之前就开始下降；
5. 当 $t$ 继续逼近 0，也就是轨迹接近真实样本时，$\dot S^*(t)$ 会急剧下降，而 $\phi^*(t)$ 同时快速上升。

这样读下来，图 9 和图 10 传达的不是一个抽象结论，而是一条时间顺序很明确的热力学叙事：

- 前向过程是普通弛豫，所有速率最后都衰减到零；
- 反向过程一开始先把系统从无结构噪声态拉回；
- 在达到分化转变附近之前，熵通量已经发生符号翻转，说明生成轨迹不再只是从噪声中回拉，而是开始把结构真正推向可分的数据簇；
- 到更接近 $t=0$ 的阶段，生成过程进一步加速收缩到目标数据空间。

这一段正好把前面的势能分叉图像和这里的热力学量接起来：势能景观的分裂给出“结构何时开始可分”的几何条件，而图 10 里的熵通量与系综熵变化率则告诉你，这个结构化过程在热力学上是如何逐步展开的。

### 3.6 Franz-Parisi 势与坍缩转变

前面的分化转变回答的是：反向轨迹什么时候开始在不同数据簇之间分裂。这里要回答的是另一个更细的问题：当轨迹已经选中某个簇之后，它什么时候会进一步收缩到某一个具体样本上。

原文把这个问题重新翻译成统计推断。`Eq. (47)` 已经告诉我们：给定当前含噪状态 $\mathbf{X}_t$，原始样本 $\mathbf{X}_0$ 的后验可以写成

$$
P(\mathbf{X}_0\mid \mathbf{X}_t,t)\propto \exp[-\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)].
$$

现在再选一个参考构型 $\mathbf{X}_0'$。接下来问的不是“哪一个 $\mathbf{X}_0$ 后验概率最大”，而是：

- 如果把候选样本 $\mathbf{X}_0$ 限制在距离参考构型 $\mathbf{X}_0'$ 为 $q$ 的壳层上，
- 这个限制要付出多大的自由能代价？

这里之所以要引入“自由能代价”，是因为“最大后验点在哪里”只告诉你一个最优位置，却看不出整个后验几何是否已经变窄、碎裂，或者即将坍缩到单个样本。为了看这种几何结构，原文不再只盯着一个后验最大点，而是把所有满足距离约束

$$
d(\mathbf{X}_0,\mathbf{X}_0')=q
$$

的候选样本整体拿出来看：这一整层样本一共还剩多少统计权重？

这时最自然的对象就是受限配分函数

$$
Z(\mathbf{X}_t,\mathbf{X}_0',q).
$$

它衡量的是：在当前含噪状态 $\mathbf{X}_t$ 和参考构型 $\mathbf{X}_0'$ 给定时，距离为 $q$ 的那一层候选样本整体上有多“可行”。

- 如果这一层上仍然有很多与 $\mathbf{X}_t$ 相容的候选点，$Z$ 就大；
- 如果这一层上几乎没有与 $\mathbf{X}_t$ 相容的候选点，$Z$ 就小。

于是

$$
-\log Z
$$

就成了这个距离壳层的自由能代价：它不是在问“最好那个点是谁”，而是在问“把候选样本整体限制在这个距离壳层上，到底容易还是困难”。也正因为它同时综合了“这一层上的相容程度”和“这一层上还有多少候选点”，它才能用来刻画后验几何何时从宽阔盆地变成碎片化结构，并最终坍缩到单个样本。

原文于是定义受限 Boltzmann 测度

$$
p(\mathbf{X}_0\mid \mathbf{X}_t,\mathbf{X}_0',q)
=
\frac{1}{Z(\mathbf{X}_t,\mathbf{X}_0',q)}
\exp[-\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)]
\delta[q-d(\mathbf{X}_0,\mathbf{X}_0')].
\tag{70}
$$

这里每一项都各司其职：

- $\exp[-\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)]$：保证候选样本和当前含噪状态 $\mathbf{X}_t$ 相容；
- $\delta[q-d(\mathbf{X}_0,\mathbf{X}_0')]$：把候选样本限制在距离参考构型为 $q$ 的壳层上；
- $Z(\mathbf{X}_t,\mathbf{X}_0',q)$：这个壳层上的受限配分函数。

所以 $Z(\mathbf{X}_t,\mathbf{X}_0',q)$ 的含义是：在给定 $\mathbf{X}_t$ 和参考构型 $\mathbf{X}_0'$ 的条件下，距离为 $q$ 的那一层候选样本总共有多大的统计权重。

接着提到，也可以把这个硬约束改写成一个带耦合场 $\epsilon$ 的软约束，从而定义约束自由能

$$
F(\epsilon)
=
- \left\langle
\int d\mathbf{X}_0'
p(\mathbf{X}_0'\mid \mathbf{X}_t)
\ln
\int d\mathbf{X}_0
\exp\!\big[
-\mathcal{H}(\mathbf{X}_0\mid \mathbf{X}_t,t)
+\epsilon\,d(\mathbf{X}_0,\mathbf{X}_0')
\big]
\right\rangle_{\mathbf{X}_t},
\tag{71}
$$

这里先要说明为什么要从硬约束跳到软约束。`Eq. (70)` 直接固定了

$$
d(\mathbf{X}_0,\mathbf{X}_0')=q,
$$

这在概念上最直接，但在计算上不方便，因为 delta 函数把积分强行压在一个精确的壳层上。原文于是先引入耦合场 $\epsilon$，把“严格固定距离”改写成“对不同距离赋予不同权重”：

- 如果某个候选样本和参考构型距离更大，项 $\epsilon\,d(\mathbf{X}_0,\mathbf{X}_0')$ 就会改变它在 Boltzmann 权重里的相对重要性；
- 因而 $\epsilon$ 扮演的是“距离的共轭场”，就像统计物理里外场控制磁化强度那样，它不直接固定距离，但会推动系统偏向某一类典型距离。

所以 `Eq. (71)` 里的 $F(\epsilon)$ 描述的是：当我们用耦合场 $\epsilon$ 去偏置距离分布时，整个系统的自由能如何变化。

然后通过 Legendre 变换定义 Franz-Parisi 势

$$
V(q)=\min_{\epsilon}\,[F(\epsilon)+\epsilon q].
\tag{72}
$$

这一步也不能只当成一个公式替换。它真正做的是把描述方式从“用共轭场 $\epsilon$ 控制距离”切换成“直接把典型距离 $q$ 当作自变量”。

在 `Eq. (71)` 的表述里，自变量是 $\epsilon$；系统在这个外场下会自己选出一个典型距离。这个典型距离满足

$$
\frac{\partial F}{\partial \epsilon}=-q.
$$

也就是说：

- 先指定耦合场 $\epsilon$，
- 系统再响应出一个典型距离 $q$。

但 Franz-Parisi 势真正想回答的问题恰好反过来：

- 如果我先指定距离 $q$，
- 那么维持这个距离要付出多大的自由能代价？

这正是 Legendre 变换存在的理由。它把“场变量” $\epsilon$ 换成了与之共轭的“几何变量” $q$。因此

$$
V(q)=\min_{\epsilon}[F(\epsilon)+\epsilon q]
$$

的含义是：在所有能够产生典型距离 $q$ 的耦合场里，选出那个最匹配的 $\epsilon$，并把对应的自由能代价记成 $V(q)$。

所以 Franz-Parisi 势

$$
V(q,t)
$$

要读成：在当前含噪状态 $\mathbf{X}_t$ 给定的情况下，如果要求候选原始样本和参考构型的典型距离就是 $q$，那么系统为维持这个几何约束所需要支付的平均自由能代价是多少。

接下来原文转到一维可直接计算的例子。这里最清楚的写法不是把 Hamiltonian 一次性完全展开，而是先保留“似然项 + 先验项”的结构：

$$
\mathcal H(X_0\mid X_t,t)
=
\frac{(X_t-e^{-t}X_0)^2}{2(1-e^{-2t})}
-\ln p_0(X_0),
\tag{73}
$$

其中

$$
p_0(X_0)
=
\frac{1}{2}\mathcal N(X_0;\mu,\sigma^2)
+
\frac{1}{2}\mathcal N(X_0;-\mu,\sigma^2).
$$

这样读最直接：

- 第一项是前向高斯核给出的失配代价，衡量“这个候选原始样本 $X_0$ 扩散到时刻 $t$ 之后，能否解释当前观测 $X_t$”；
- 第二项是数据先验代价，衡量“这个候选原始样本本身在双峰数据分布里是否典型”。

如果把 $p_0(X_0)$ 在这一维双峰高斯模型里完全展开，就回到原文的显式形式：

$$
-\ln p_0(X_0)
=
- \ln \left[
\frac {1}{2 \sqrt {2 \pi \sigma^ {2}}} \exp \left(- \frac {(X _ {0} - \mu) ^ {2}}{2 \sigma^ {2}}\right)
+ \frac {1}{2 \sqrt {2 \pi \sigma^ {2}}} \exp \left(- \frac {(X _ {0} + \mu) ^ {2}}{2 \sigma^ {2}}\right)
\right].
$$

然后把这个 Hamiltonian 代回受限配分函数：

$$
Z \left(X _ {t}, X _ {0} ^ {\prime}, q, t\right)
=
\int
\exp \left(- \mathcal {H} \left(X _ {0} \mid X _ {t}, t\right)\right)
\delta \left(q - \left(X _ {0} - X _ {0} ^ {\prime}\right) ^ {2}\right)
d X _ {0}.
\tag{74}
$$

于是 Franz-Parisi 势的平均定义变成

$$
V (q, t)
=
- \left\langle
\int p \left(X _ {0} ^ {\prime} \mid X _ {t}, t\right)
\ln Z \left(X _ {t}, X _ {0} ^ {\prime}, q, t\right)
d X _ {0} ^ {\prime}
\right\rangle_ {X _ {t}}.
\tag{75}
$$

这一步其实有两层平均，不能只把公式抄下来。

第一层是

$$
\int p(X_0'\mid X_t,t)\,\ln Z(X_t,X_0',q,t)\,dX_0'.
$$

它的意思是：先把当前含噪状态 $X_t$ 固定住，再对所有可能的参考构型 $X_0'$ 做平均。因为同一个 $X_t$ 往往不只对应一个候选原始样本，所以这里不是挑一个参考构型，而是按照后验分布

$$
p(X_0'\mid X_t,t)
$$

去平均不同参考构型带来的约束自由能。

第二层是外面的

$$
\langle \cdots \rangle_{X_t}.
$$

它表示：上面那个“给定 $X_t$ 时的平均自由能代价”，还要再对当前含噪状态 $X_t$ 做一遍平均。这样得到的 $V(q,t)$ 才不依赖某一个特定噪声 realization，而是给出时刻 $t$ 的典型几何结构。

这里还有一个容易跳过的点：为什么平均的是

$$
\ln Z
$$

而不是直接平均

$$
Z
$$

本身？最直接的原因其实是：对一个**固定**的背景 $(X_t,X_0')$ 来说，受限自由能本来就定义成

$$
F_{\mathrm{restr}}(X_t,X_0',q)=-\ln Z(X_t,X_0',q).
$$

也就是说，$-\ln Z$ 不是额外多出来的写法，而就是“这个具体 realization 下的自由能”。既然现在有很多不同的 $X_t$ 和 $X_0'$ realization，原文要做的自然就是：

1. 先对每个 realization 分别算出它自己的自由能 $-\ln Z$；
2. 再对这些自由能做平均。

这就得到

$$
-\langle \ln Z\rangle
$$

而不是先把所有 realization 的配分函数混在一起平均，再去取对数：

$$
-\ln \langle Z\rangle.
$$

这两者的顺序不一样，物理意义也不一样：

- $-\langle \ln Z\rangle$：先固定一个具体的 $X_t$，看在这个背景下后验几何的自由能代价，再对不同背景做平均；
- $-\ln\langle Z\rangle$：先把不同背景下的配分函数混在一起，再统一取对数。

这篇文章要保留的正是前一种结构，因为当前状态 $X_t$ 在这里扮演的是一个时变的 quenched disorder。作者关心的是：**对每一个具体的含噪背景，受限后验几何长什么样；然后再把这些几何代价平均起来。** 如果直接用 $-\ln\langle Z\rangle$，不同 $X_t$ 的后验结构会先被混合，后面想读出碎片化或坍缩，就会被明显抹平。

为了把 `(74)` 真正算出来，原文利用了一维 delta 函数恒等式

$$
\delta \left(q - \left(X _ {0} - X _ {0} ^ {\prime}\right) ^ {2}\right)
=
\frac {1}{2 \sqrt {q}}
\left[
\delta \left(X _ {0} - X _ {0} ^ {\prime} - \sqrt {q}\right)
+ \delta \left(X _ {0} - X _ {0} ^ {\prime} + \sqrt {q}\right)
\right].
\tag{76}
$$

它的意思很简单：在一维里，距离平方等于 $q$ 的点只有两个，分别是

$$
X_0=X_0'+\sqrt q,
\qquad
X_0=X_0'-\sqrt q.
$$

所以原来的积分立刻塌成两项求和：

$$
\begin{aligned}
Z \left(X _ {t}, X _ {0} ^ {\prime}, q, t\right)
&=
\int
\exp \left(- \mathcal {H} \left(X _ {0} \mid X _ {t}, t\right)\right)
\delta \left(q - \left(X _ {0} - X _ {0} ^ {\prime}\right) ^ {2}\right)
d X _ {0} \\
&=
\frac {1}{2 \sqrt {q}} \exp \bigl (- \mathcal H (X _ {0} ^ {\prime} + \sqrt {q} \mid X _ {t}, t) \bigr)
+ \frac {1}{2 \sqrt {q}} \exp \bigl (- \mathcal H (X _ {0} ^ {\prime} - \sqrt {q} \mid X _ {t}, t) \bigr).
\end{aligned}
\tag{77}
$$

接下来要做的是对参考构型 $X_0'$ 和当前含噪状态 $X_t$ 做平均。原文先写出它们的联合分布：

$$
\begin{aligned}
p \left(X _ {0} ^ {\prime}, X _ {t}, t\right)
&=
p \left(X _ {t}, t \mid X _ {0} ^ {\prime}\right) p \left(X _ {0} ^ {\prime}\right) \\
&=
\frac {\exp \left(- \frac {\left(X _ {t} - X _ {0} ^ {\prime} e ^ {- t}\right) ^ {2}}{2 \left(1 - e ^ {- 2 t}\right)}\right)}{\sqrt {2 \pi \left(1 - e ^ {- 2 t}\right)}}
\left(
\frac {1}{2 \sqrt {2 \pi \sigma^ {2}}} \exp \left(- \frac {\left(X _ {0} ^ {\prime} - \mu\right) ^ {2}}{2 \sigma^ {2}}\right)
+ \frac {1}{2 \sqrt {2 \pi \sigma^ {2}}} \exp \left(- \frac {\left(X _ {0} ^ {\prime} + \mu\right) ^ {2}}{2 \sigma^ {2}}\right)
\right).
\end{aligned}
\tag{78}
$$

有了这个联合分布之后，Monte Carlo 估计可以按三步来理解。

第一步，先采样

$$
(X_0',X_t)\sim p(X_0',X_t,t).
$$

这里不能把 $X_0'$ 和 $X_t$ 分开独立采样，因为两者本来就通过前向扩散耦合在一起。联合分布保留的正是“这个参考样本经过加噪之后，当前含噪状态出现的概率有多大”。

第二步，对每一对具体样本

$$
(X_{0,\ell}',X_{t,\ell})
$$

都用 `Eq. (77)` 计算一个具体的受限配分函数

$$
Z(X_{t,\ell},X_{0,\ell}',q,t).
$$

这一步的意思是：先把背景固定住，再问在这个具体背景下，距离为 $q$ 的壳层还剩多少统计权重。

第三步，把每一组背景对应的自由能代价

$$
-\ln Z(X_{t,\ell},X_{0,\ell}',q,t)
$$

在很多组样本上做平均。这样得到的平均值，就是 Franz-Parisi 势的数值估计。原文把它写成

$$
V (q, t) = - \frac {1}{\mathcal {T}} \sum_ {\ell = 1} ^ {\mathcal {T}} \ln Z \left(X _ {t, \ell}, X _ {0, \ell} ^ {\prime}, q, t\right).
\tag{79}
$$

Figure 11 展示的是 $V(q,t)$ 及其一阶、二阶导数。按原图的排版顺序，可以把它读成一个 $3\times 3$ 的 panel 矩阵：三列对应三个时间点 $t=0.42,\ 0.015,\ 0.01$，三行依次对应 $V(q,t)$、$\partial_q V(q,t)$ 和 $\partial_q^2 V(q,t)$。

<p>
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-01.jpg" width="32%" />
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-02.jpg" width="32%" />
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-03.jpg" width="32%" />
</p>
<p>
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-04.jpg" width="32%" />
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-05.jpg" width="32%" />
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-06.jpg" width="32%" />
</p>
<p>
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-07.jpg" width="32%" />
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-08.jpg" width="32%" />
  <img src="../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-18-figure-09.jpg" width="32%" />
</p>

读这张图时，先把三行的角色分开：

1. 第一行的 $V(q,t)$ 直接回答：如果把候选原始样本限制在离参考构型 $X_0'$ 距离为 $q$ 的壳层上，要付出多大的平均自由能代价。曲线越平，表示允许的距离范围越宽；曲线越陡，表示只有更窄的一段距离仍然有明显统计权重。
2. 第二行的 $\partial_q V(q,t)$ 用来找驻点和斜率变化。它穿过零点时，对应 $V(q,t)$ 的局部极值；它如果先快速下降再回升，说明曲线已经不再是简单的单调凸形。
3. 第三行的 $\partial_q^2 V(q,t)$ 用来找拐点。它等于零的位置，就是曲率改变符号的位置；这些点出现之后，$V(q,t)$ 的几何结构才开始真正变复杂。

然后按时间从大到小逐列读。

1. 第一列是 $t=0.42$，几乎正好贴着前面求出来的分化时间 $t_S=0.42622$。这时第一行的 $V(q,t)$ 已经不再是简单的单阱曲线：它先上升，在小 $q$ 处形成一个肩部，然后再下降到更宽的低谷。第二行里，$\partial_q V(q,t)$ 先从正值迅速下降，穿过零点后再回升，说明曲线已经出现局部极值。第三行里，$\partial_q^2 V(q,t)$ 在小 $q$ 区域由负向接近零，说明曲率结构刚开始发生变化。原文把这一步读成动态玻璃转变的开端：后验几何不再只是一个宽而平滑的盆地。
2. 第二列是 $t=0.015$。这时第一行的 $V(q,t)$ 整体变得更陡，表示一旦离参考构型太远，自由能代价会上升得更快。换句话说，后验允许的距离范围已经明显收窄。第二行里，$\partial_q V(q,t)$ 虽然仍然只有一段明显的下凹区，但这段结构被压到了更靠近小 $q$ 的范围。第三行里，$\partial_q^2 V(q,t)$ 的非平凡变化也集中在更小的 $q$ 区域。这说明后验几何的复杂结构正在向参考构型附近收缩：远离参考构型的大部分壳层已经不再重要。
3. 第三列是 $t=0.01$，更接近反向过程的终点。第一行里，$V(q,t)$ 对 $q$ 的增长几乎是整体陡升的，表示只要和参考构型拉开距离，代价就迅速变大。第二行的最低点继续向小 $q$ 区域集中。第三行的曲率变化也更加局域化。作者对这一列的解释是：随着 $t\to 0$，会出现更多拐点，推断空间逐渐碎片化，反向轨迹不再只是在某个簇附近波动，而是进一步锁定到某一个具体样本。

所以 Figure 11 在这篇文章里的作用，不是再讲一次簇级分化，而是把更晚发生的样本级坍缩单独抓出来：

1. `speciation transition` 回答的是：轨迹什么时候开始在两个数据簇之间分开。
2. Franz-Parisi 势回答的是：在已经选中某个簇之后，后验几何什么时候开始收窄、碎片化，并最终把轨迹锁定到单个样本。

这样一来，Section III 的逻辑才算完整闭合：

- 反向 SDE 给出动力学；
- 势能 / 广义自由能给出生成景观；
- 分化转变说明轨迹何时开始在簇之间分开；
- Franz-Parisi 势进一步说明轨迹何时从“选中一个簇”收缩到“锁定一个样本”。

---

## 7. 核心结论与总结

### 7.1 统一图景

本文为生成扩散模型建立了一幅完整的物理图景，从非平衡到平衡层层递进：

| 物理概念 | 在 GDM 中的对应 |
|---------|---------------|
| OU 过程 / Langevin 动力学 | 正向扩散 / 反向生成 |
| 路径积分与作用量 | 轨迹概率 |
| 涨落定理 | 正向与反向过程均满足 |
| 熵产生率 & 熵通量 | 刻画生成过程中序的涌现 |
| 势能 / 自由能 | 反向动力学的驱动力景观 |
| 自发对称性破缺 | 分化转变——数据簇的"选择" |
| 淬火无序 & 统计推断 | 时变状态 $\mathbf{X}_t$ 作为 quenched disorder |
| Franz-Parisi 势 | 构型空间碎片化 → 坍缩转变 |

### 7.2 核心物理洞察

1. **涨落定理是生成扩散模型的基本物理定律**：无论正向加噪还是反向去噪，均严格满足详细涨落定理和积分涨落定理，随机热力学第二定律成立。

2. **反向生成 = 最小化广义自由能**：score function 是自由能的梯度（差一个预因子），反向 Langevin 动力学在势能/自由能景观中下坡运动，生成样本对应自由能最小值。

3. **分化转变 = 自发对称性破缺**：在反向过程中，自由能景观从单阱变为双阱（或多阱），类比铁磁 Ising 模型降温时的相变。临界时间 $t_S$ 由势能凸性消失条件精确确定。

4. **坍缩转变 = 玻璃转变**：Franz-Parisi 势的拐点标志推断空间碎片化，反向轨迹被锁定到单个数据样本。这是一个不依赖经验分布假设的几何化判据。

5. **三相相图的发现**：在任意均值和方差的参数空间中，存在稳定对称性破缺、对称性未破缺和不稳定对称性破缺三种相，其中不稳定相导致生成采样失败——这是本文首次揭示的新结果。

6. **熵通量的符号变化是序涌现的热力学标志**：反向过程中 $\phi^*$ 从负变正的转折点标记了数据结构开始从噪声中涌现的时刻。

### 7.3 局限性与未来方向

- 所有结果建立在高斯混合数据模型上，虽然高维公式已被推导，但具体数值展示仅限一维。
- Franz-Parisi 势的高维计算留待未来工作——高维情形下将涌现新的序参量（order parameters）。
- 未考虑实际算法设计中的神经网络训练误差对物理图景的影响。
- 不稳定对称性破缺相在高维生成过程中是否仍然存在，有待进一步研究。

---

## 附录：关键公式速查

| 名称 | 公式 |
|-----|------|
| 正向 OU SDE | $\dot{\mathbf{X}} = -\mathbf{X} + \sqrt{2}\boldsymbol{\xi}$ |
| 状态分布 | $p(\mathbf{X}_t, t) = \frac{1}{2}\mathcal{N}(\boldsymbol{\mu}e^{-t}, \mathbf{I}_d) + \frac{1}{2}\mathcal{N}(-\boldsymbol{\mu}e^{-t}, \mathbf{I}_d)$ |
| Score function | $\nabla\ln p = \tanh(\boldsymbol{\mu}_t^\top \mathbf{X}_t)\boldsymbol{\mu}_t - \mathbf{X}_t$ |
| 反向 SDE | $\dot{\mathbf{X}} = \mathbf{X} - 2\tanh(\boldsymbol{\mu}_t^\top \mathbf{X}_t)\boldsymbol{\mu}_t + \sqrt{2}\boldsymbol{\xi}$ |
| 势能 | $U = \frac{1}{2}\mathbf{X}_t^2 - 2\ln\cosh(\mathbf{X}_t \cdot \boldsymbol{\mu}_t)$ |
| 分化转变时间（一般情形） | $t_S = \frac{1}{2}\ln(\mu^2 + \sqrt{\sigma^4 - 2\sigma^2 + \mu^4 + 1})$ |
| 不稳定对称性破缺阈值 | $t_{USB} = \frac{1}{2}\ln(\sigma^2 - 1)$ |
| 积分涨落定理 | $\langle e^{-\Delta S_{\text{tot}}} \rangle = 1$ |
| 熵产生率分解 | $\dot{S} = \pi - \phi$ |
