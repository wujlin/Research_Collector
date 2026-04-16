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

为了建立涨落定理，需要写出轨迹的路径概率。论文从随机微积分的 $\lambda$-离散化方案出发（$\lambda = 0$ 对应 Ito 格式，$\lambda = 1/2$ 对应 Stratonovich 格式），推导出正向 OU 过程的条件轨迹概率：

$$P(X([T])|\mathbf{X}_0) \propto \exp\left(-\int_0^T \left[\frac{1}{4}(\dot{\mathbf{X}} + \mathbf{X})^2 - \lambda d\right] \stackrel{\lambda}{\odot} dt\right)$$

指数中的被积函数即物理中的 Lagrangian $\mathcal{L}$，整个指数为路径的作用量（action）。最大概率路径由 Euler-Lagrange 方程决定。

关键技术要点在于 Jacobian 行列式的计算：从噪声 $\boldsymbol{\eta}_t$ 到下一时刻状态 $\mathbf{X}_{t+dt}$ 的概率密度变换需要精确处理离散化方案带来的修正项 $e^{-\lambda \nabla \cdot f\, dt}$。

### 2.3 正向过程的涨落定理

将同一条轨迹分别在正向和时间反转方向上计算路径概率之比，可以得到环境熵变（environmental entropy change）：

$$\Delta S_E = \int_0^T dt\, \stackrel{1/2}{\odot}\,[-\dot{\mathbf{X}} \cdot \mathbf{X}]$$

物理含义：在过阻尼系统中，总机械力与位移的乘积等于向环境的热耗散，这与 Stratonovich 中点格式下的计算结果一致（结果与 $\lambda$ 无关）。

系统熵变定义为始末状态概率之比的对数：

$$\Delta S = \ln\left[\frac{p(\mathbf{X}(0), 0)}{p(\mathbf{X}(T), T)}\right]$$

总熵变 $\Delta S_{\text{tot}} = \Delta S_E + \Delta S$ 满足**详细涨落定理**（detailed fluctuation theorem）：

$$\frac{P[X([T])]}{P[\tilde{X}([T])]} = e^{\Delta S_{\text{tot}}}$$

由此推导出**积分涨落定理**（integral fluctuation theorem）$\langle e^{-\Delta S_{\text{tot}}} \rangle = 1$，再由指数函数的凸性（Jensen 不等式）给出**随机热力学第二定律** $\langle \Delta S_{\text{tot}} \rangle \geq 0$。

![图2：正向OU过程的积分涨落定理数值验证](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-05-figure-01.jpg)

**图 2 的角色**：用一维 OU 过程的数值模拟验证积分涨落定理。随着用于计算系综平均的轨迹数增加，$\langle e^{-\Delta S_{\text{tot}}} \rangle$ 收敛至理论预测值 1，确认正向扩散过程严格满足涨落定理。

### 2.4 正向过程的熵分布统计

![图3(a)：正向过程系统熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-01.jpg)

![图3(b)：正向过程环境熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-02.jpg)

![图3(c)：正向过程总熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-03.jpg)

![图3(d)：正向过程 exp(-ΔS_tot) 直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-06-figure-04.jpg)

**图 3 的角色**：从 10 000 条正向轨迹统计系统熵变 $\Delta S$、环境熵变 $\Delta S_E$、总熵变 $\Delta S_{\text{tot}}$ 及 $e^{-\Delta S_{\text{tot}}}$ 的分布。系统熵变以零为中心近似对称分布；环境熵变偏正值；总熵变以正值为主但存在负值涨落（个别轨迹熵减少）；$e^{-\Delta S_{\text{tot}}}$ 的分布在 1 附近聚集，与积分涨落定理一致。负熵轨迹的存在是涨落定理的本质体现——热力学第二定律是统计律而非绝对律。

### 2.5 系综熵产生率

从 Fokker-Planck 方程（FPE）出发，定义概率流（probability current）$\mathbf{J} = f(\mathbf{X}_t, t)p(\mathbf{X}_t, t) - \nabla p(\mathbf{X}_t, t)$，可以将系综熵变化率分解为：

$$\frac{dS(t)}{dt} = \pi - \phi$$

其中：
- **熵产生率**（entropy production rate）$\pi = \sum_i \int \frac{J_i^2}{p(\mathbf{X}_t, t)} d\mathbf{X}_t \geq 0$，衡量总（系统+环境）熵增长的速率；
- **熵通量**（entropy flux）$\phi = \sum_i \int f_i(\mathbf{X}_t, t) J_i\, d\mathbf{X}_t$，衡量从环境流入或流出系统的熵。

关键性质：平衡态时 $\pi = \phi = 0$；非平衡稳态时 $\pi = \phi \neq 0$，系统熵恒定但持续耗散。

---

## 3. 反向生成动力学的非平衡分析

### 3.1 反向 SDE 的推导

从 Bayes 公式出发，将正向传播核 $P(\mathbf{X}_{t+dt}|\mathbf{X}_t)$ 和概率比 $p(\mathbf{X}_t)/p(\mathbf{X}_{t+dt})$ 结合，可推导出反向生成 SDE：

$$\dot{\mathbf{X}} = f(\mathbf{X}_t, t) - 2\nabla\ln p(\mathbf{X}_t, t) + \sqrt{2}\,\boldsymbol{\xi}$$

关键驱动力是 $-2\nabla\ln p(\mathbf{X}_t, t)$，其中 $\nabla\ln p(\mathbf{X}_t, t)$ 即 score function。在高斯混合模型中，score function 有解析形式：

$$\nabla\ln p(\mathbf{X}_t, t) = \tanh(\boldsymbol{\mu}_t^\top \mathbf{X}_t)\,\boldsymbol{\mu}_t - \mathbf{X}_t$$

这是一个关于 $\mathbf{X}_t$ 的非线性函数，非线性来自 $\tanh$ 项——它编码了数据的双峰结构。当 $\boldsymbol{\mu}_t^\top \mathbf{X}_t \approx 0$（时间较大、信号微弱时），$\tanh \approx 0$，驱动力近似线性；当 $\boldsymbol{\mu}_t^\top \mathbf{X}_t$ 较大时（时间较小、信号清晰），$\tanh \approx \pm 1$，强烈的非线性将轨迹推向两个数据簇中的一个。

### 3.2 Score function 的学习

在实际应用中，score function 通常由神经网络拟合，最小化：

$$\mathcal{L}(\theta) = \mathbb{E}_{\mathbf{X}_t \sim p(\mathbf{X}_t, t)}\left[\|s_\theta(\mathbf{X}_t, t) - \nabla\ln p(\mathbf{X}_t, t)\|^2\right]$$

一个重要简化是 $\nabla\ln p(\mathbf{X}_t, t)$ 在期望意义下可以用条件概率 $\nabla\ln P(\mathbf{X}_t|\mathbf{X}_0)$ 替代，后者仅依赖高斯转移核，形式简单：$\nabla\ln P(\mathbf{X}_t|\mathbf{X}_0) = -\frac{1}{\sqrt{1-e^{-2t}}}\mathbf{Z}_t$。本文的模型优势在于 score function 完全解析可知，无需训练神经网络。

---

## 4. 势能、自由能与相变分析

### 4.1 反向动力学的势能

令 $s = T - t$（使反向时间递增），反向 SDE 可改写为标准 Langevin 形式：

$$d\tilde{\mathbf{X}}_s = -\nabla U(\tilde{\mathbf{X}}_s, T-s)\,ds + \sqrt{2}\,d\mathbf{W}$$

其中势能（potential energy）$U$ 有解析表达式：

$$U = \frac{1}{2}\mathbf{X}_t^2 - 2\ln\left[\cosh(\mathbf{X}_t \cdot \boldsymbol{\mu}e^{-t})\right]$$

第一项 $\frac{1}{2}\mathbf{X}_t^2$ 是正向 OU 过程的恢复力贡献；第二项 $-2\ln\cosh(\cdot)$ 来自 score function 中的 $\tanh$ 非线性，编码数据分布的双峰结构。

### 4.2 自发对称性破缺——分化转变

![图4：势能随时间的演化（μ=1，一维）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-01.jpg)

![图4续：t=0.35 时势能接近临界](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-02.jpg)

![图4续：t=0.1 时势能呈双阱](../../../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-03.jpg)

**图 4 的角色**：以一维情形展示反向生成过程中势能 $U(X_t, t)$ 随时间的演化。$t=1$ 时势能为单阱（单一最小值在 $X=0$）；$t \approx 0.35$ 时处于临界点附近，单阱开始变平；$t=0.1$ 时势能发展为双阱结构，原点变为局部极大值，两个新的最小值分别出现在 $X > 0$ 和 $X < 0$ 处。这一过程类比铁磁 Ising 模型降温时的自发对称性破缺。

分化转变时间（speciation transition time）$t_S$ 由势能在原点处凸性消失的条件决定：

$$\left.\frac{\partial^2 U}{\partial X^2}\right|_{X=0}(t_S) = 0 \quad \Longrightarrow \quad \mu^2 e^{-2t_S} = \frac{1}{2}$$

对于单位方差的高斯混合。这与 Biroli 等人通过重叠参数动力学（overlap dynamics）得到的分化转变时间完全一致，但推导方式更加直观——势能凸性的定性改变。

### 4.3 统计推断映射与自由能

去噪过程可以被精确映射为一个统计推断问题：给定当前含噪观测 $\mathbf{X}_t$，推断原始数据 $\mathbf{X}_0$ 的后验概率：

$$P(\mathbf{X}_0|\mathbf{X}_t, t) \propto \exp\left[-\mathcal{H}(\mathbf{X}_0|\mathbf{X}_t, t)\right]$$

其中 Hamiltonian 为：

$$\mathcal{H}(\mathbf{X}_0|\mathbf{X}_t, t) = \frac{1}{2}(\mathbf{X}_t - \mathbf{X}_0 e^{-t})^\top \Sigma^{-1} (\mathbf{X}_t - \mathbf{X}_0 e^{-t}) - \ln p(\mathbf{X}_0)$$

反向动力学中的时变状态 $\mathbf{X}_t$ 扮演了传统自旋玻璃理论（spin glass theory）中**淬火无序**（quenched disorder）的角色——它由正向过程产生，在推断过程中是固定的外部参数。

等效逆温度为 $\beta = \Sigma_t^{-1} = (1-e^{-2t})^{-1}$。当 $t$ 从大（近似高温、$\beta$ 小）减小到接近 $0$（低温、$\beta$ 大）时，系统经历从无序到有序的相变。

定义自由能 $F(\mathbf{X}_t, t) = -\frac{1}{\beta}\ln Z(\mathbf{X}_t, t)$，论文证明其梯度恰好等于负的 score function（差一个预因子）：

$$\nabla F = -\frac{1}{\beta}\nabla\ln p$$

因此自由能的解析形式为：

$$F = -\frac{1}{\beta}\ln\cosh(\mathbf{X}_t \cdot \boldsymbol{\mu}_t) + \frac{1}{2\beta}\mathbf{X}_t^2$$

进一步定义**广义自由能**（generalized free energy）$\tilde{F} = 2\beta F + \int f\, d\tilde{\mathbf{X}}_s$，论文证明它恰好等于前面推导的势能 $U$。这意味着：

> **反向生成过程可以理解为在动态状态空间中最小化广义自由能，生成的样本遵循最小自由能原则。**

### 4.4 一般化相图——任意均值与方差

对于一般的数据均值 $\mu$ 和方差 $\sigma^2$，分化转变时间为：

$$t_S = \frac{1}{2}\ln\left(\mu^2 + \sqrt{\sigma^4 - 2\sigma^2 + \mu^4 + 1}\right)$$

![图5：一维情形的对称性破缺相图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-10-figure-04.jpg)

**图 5 的角色**：在 $(\mu, \sigma)$ 参数空间中展示三种对称性行为的相图。这是本文首次揭示的完整相图，包含三个相：

1. **稳定对称性破缺相**（Symmetry breaking，棕色区域）：势能发展出稳定双阱，反向过程能成功生成数据。
2. **对称性未破缺相**（No symmetry breaking / Symmetry un-breaking，绿色区域）：势能始终保持单阱，分化转变不发生。
3. **不稳定对称性破缺相**（Unstable symmetry breaking，红色区域）：势能先出现双阱，但随后不稳定化为倒 U 形，生成采样失败。

两条相界线：$\mu^2 + \sqrt{\sigma^4 - 2\sigma^2 + \mu^4 + 1} = 1$ 分隔对称破缺与未破缺相；$t_{USB} = \frac{1}{2}\ln(\sigma^2 - 1)$ 分隔稳定与不稳定破缺相，后者与 $\mu$ 无关，仅取决于方差。

![图6(a)：稳定对称性破缺（μ=1, σ=0.8）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-11-figure-01.jpg)

![图6(b)：对称性未破缺（μ=0.4, σ=1）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-11-figure-04.jpg)

![图6(c)：不稳定对称性破缺（μ=4, σ=1.5）](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-11-figure-07.jpg)

**图 6 的角色**：用三组典型参数展示三种相的势能演化过程。(a) 稳定对称性破缺：势能从单阱平滑过渡为稳定双阱。(b) 对称性未破缺：势能始终保持单阱，$t_S$ 无正实数解。(c) 不稳定对称性破缺：势能先出现双阱，但在某个时刻 $t_{USB}$ 之后，势能在 $|X| \to \infty$ 处的斜率变号，双阱结构被摧毁为倒 U 形，Langevin 动力学中的粒子向无穷远处逃逸，生成采样彻底失败。

---

## 5. 反向过程的涨落定理与熵产生

### 5.1 反向过程的路径概率

对于反向生成 SDE $d\tilde{\mathbf{X}}_s = [2\tanh(\boldsymbol{\mu}_{T-s}^\top \tilde{\mathbf{X}}_s)\boldsymbol{\mu}_{T-s} - \tilde{\mathbf{X}}_s]ds + \sqrt{2}d\mathbf{W}$，论文同样用 $\lambda$-离散化方案推导了条件轨迹概率的路径积分表示，得到作用量：

$$\mathcal{A}(\tilde{X}([T])) = \int_0^T ds\,\stackrel{\lambda}{\odot}\left[\frac{(\dot{\tilde{\mathbf{X}}} - 2\tanh(\boldsymbol{\mu}_{T-s}^\top \tilde{\mathbf{X}})\boldsymbol{\mu}_{T-s} + \tilde{\mathbf{X}})^2}{4} + \lambda\nabla\cdot[2\tanh(\boldsymbol{\mu}_{T-s}^\top \tilde{\mathbf{X}})\boldsymbol{\mu}_{T-s} - \tilde{\mathbf{X}}]\right]$$

与正向过程的关键区别：反向 SDE 的漂移力（drift）包含非线性 $\tanh$ 项，Jacobian 修正项也相应变得更复杂。

### 5.2 反向过程的涨落定理

仿照正向过程的推导，在反向过程上建立前向/后向路径概率之比，得到环境熵变和系统熵变，二者之和满足详细涨落定理与积分涨落定理：

$$\langle e^{-\Delta S_{\text{tot}}} \rangle = 1$$

![图7：反向生成过程的积分涨落定理数值验证](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-14-figure-01.jpg)

**图 7 的角色**：用反向 SDE 的数值模拟验证积分涨落定理。与正向过程类似，随着轨迹数增大，$\langle e^{-\Delta S_{\text{tot}}} \rangle$ 收敛至 1。这证明了反向生成过程——虽然漂移力更复杂且含非线性——仍然严格服从随机热力学的基本定律。

### 5.3 反向过程的熵分布统计

![图8(a)：反向过程系统熵变直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-15-figure-01.jpg)

![图8(d)：反向过程 exp(-ΔS_tot) 直方图](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-15-figure-04.jpg)

**图 8 的角色**：从 10 000 条反向轨迹统计熵变分布。与正向过程相比，反向过程的系统熵变和总熵变均**偏向正值**（分布峰值右移），反映生成过程中"有序结构从噪声中涌现"这一物理事实——系统从高熵（噪声）状态向低熵（有结构数据）演化，但由于环境熵增大更多，总熵仍然增加。

### 5.4 系综熵产生率的时间演化

正向和反向过程共享相同的状态概率分布 $p(\mathbf{X}_t, t)$（论文在附录 C 中给出了严格证明：将 $p(\tilde{\mathbf{X}}_s, T-s)$ 代入反向 FPE，可化简为正向 FPE 的完全相同形式）。两个过程的概率流大小相等、方向相反：$\mathbf{J}^* = -\mathbf{J}$（附录 D 证明）。

**推论**：正向和反向过程具有相同的熵产生率 $\pi = \pi^*$，但熵通量不同（因为漂移力不同）。

![图9：正向OU过程的熵产生率和熵通量](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-16-figure-01.jpg)

**图 9 的角色**：展示正向 OU 过程（$\mu=1, \sigma^2=0.4$, 时间从 0 到 3）的熵产生率 $\pi(t)$、熵通量 $\phi(t)$ 和系统熵变率 $\dot{S}(t)$ 的时间演化。$\pi(t)$ 从初始高值单调递减至零（系统趋向平衡）；$\dot{S}(t)$ 先减小后增加趋零（先失序后稳定）；$\phi(t)$ 单调递减。

![图10：反向生成过程的熵产生率和熵通量](../../pdfs/2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.mineru/hybrid_auto/images/page-16-figure-02.jpg)

**图 10 的角色**：展示反向生成过程（时间从 3 递减至 0）的 $\pi^*(t)$、$\phi^*(t)$ 和 $\dot{S}^*(t)$。这是全文物理含义最丰富的一张图。关键观察：

1. 熵通量 $\phi^*(t)$ 先为负值（环境向系统输入"序"），在 $t_S$ 之前变为正值（系统开始向环境排出"序"），表明生成过程中系统结构的涌现；
2. 系统熵变率 $\dot{S}^*(t)$ 在 $t_S$ 附近开始急剧下降，在 $t \to 0$ 时剧烈减小——这对应于生成样本被锁定到一个具体的数据簇时的熵急剧下降；
3. 绿色虚线标注分化转变时间 $t_S \approx 0.387$，紫色虚线标注 $\phi^*(t)$ 取最小值的时刻 $t^*$。$t^* > t_S$，说明熵通量的极端负值出现在分化转变之后，物理上对应"决定去哪个簇"之后紧接着发生的最剧烈的序生成过程。

---

## 6. 玻璃转变与 Franz-Parisi 势

### 6.1 从统计推断到构型空间几何

此前的工作指出，在反向过程中比 $t_S$ 更晚（$t < t_S$）的时刻，会发生**坍缩转变**（collapse transition）：轨迹凝聚到数据分布的单个样本上。先前的分析依赖于对时变状态 $\mathbf{X}_t$ 的经验分布假设（用 $n$ 个数据点近似）。

本文采用不同的进路：从统计推断的角度出发，不需要经验分布假设，而是使用 **Franz-Parisi 势**（Franz-Parisi potential）——自旋玻璃理论中刻画玻璃态能量景观几何结构的强大工具。

### 6.2 Franz-Parisi 势的构造

选择一个平衡参考构型 $\mathbf{X}_0'$，定义受限 Boltzmann 测度：

$$p(\mathbf{X}_0|\mathbf{X}_t, \mathbf{X}_0') = \frac{1}{Z(\mathbf{X}_t, \mathbf{X}_0', q)}\exp[-\mathcal{H}(\mathbf{X}_0|\mathbf{X}_t, t)]\,\delta[q - d(\mathbf{X}_0, \mathbf{X}_0')]$$

其中 $q = d(\mathbf{X}_0, \mathbf{X}_0')$ 是两个构型之间的欧几里得距离。Franz-Parisi 势定义为受限自由能对 $\mathbf{X}_0'$ 和 $\mathbf{X}_t$（作为淬火无序）的平均：

$$V(q, t) = -\langle \ln Z(\mathbf{X}_t, \mathbf{X}_0', q, t) \rangle$$

物理含义：$V(q)$ 描述了推断空间中，与参考构型距离为 $q$ 的构型的自由能代价。

### 6.3 一维实例与玻璃转变信号

在一维情形下，利用 Dirac delta 函数的性质和联合分布 $p(X_0', X_t, t)$ 的解析形式，Franz-Parisi 势可以通过 Monte-Carlo 方法高效计算。

论文指出（图 11）：
- 当 $t$ 从正向起始点 $T$ 向 $0$ 减小时，$V(q, t)$ 的形状发生定性变化；
- 在某个时刻，$V(q)$ 的二阶导出现零点（inflection point），标志着**动态玻璃转变**（dynamical glass transition）——遍历性（ergodicity）开始破缺；
- 当 $t$ 进一步接近 $0$ 时，更多的拐点出现，反映推断空间的碎片化——给定当前 $X_t$ 值，可推断的数据空间被分割为多个不连通区域；
- 这意味着反向轨迹将**坍缩**到单个数据样本上。

当第二最小值与第一最小值等高时，发生**静态玻璃转变**（static glass transition），对应复杂度（complexity）为零。

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
