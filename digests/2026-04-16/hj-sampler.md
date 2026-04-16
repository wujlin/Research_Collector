---
title: "HJ-sampler: Bayesian Sampler via Hamilton-Jacobi PDEs and Score-Based Generative Models"
authors: "Tingwei Meng, Zongren Zou, Jérôme Darbon, George Em Karniadakis"
venue: "arXiv (2024)"
date_read: "2026-04-16"
topics: ["Hamilton-Jacobi", "逆问题", "score-based", "贝叶斯采样"]
---

# HJ-sampler: 利用 Hamilton-Jacobi PDE 与 Score-Based 生成模型的贝叶斯采样器

## 精读笔记

---

## 一、问题背景与动机

### 1.1 作者学术背景

本文来自 Brown University 应用数学系。通讯作者 **George Em Karniadakis** 是 Brown 大学 Charles Pitts Robinson and John Palmer Barstow 讲席教授，是**物理信息神经网络（Physics-Informed Neural Networks, PINNs）** 的共同创始人之一。Karniadakis 长期深耕科学计算与不确定性量化（UQ）领域，在 Nature Reviews Physics、SIAM Review 等顶刊发表大量奠基性工作，是将深度学习与偏微分方程求解系统性融合的核心推动者。第一作者 Tingwei Meng 与合作者 Jérôme Darbon 在 Hamilton-Jacobi PDE 的高维求解方面有系列研究；Zongren Zou 则专注于 PINN 框架下的不确定性量化。

### 1.2 两个子领域的交汇

不确定性量化（UQ）中有两个高度活跃但相对独立的研究方向：

1. **贝叶斯推断**：将先验信息与观测数据严格结合，推断模型参数或状态的后验分布。核心挑战在于从高维后验分布中高效采样。
2. **生成模型**（特别是扩散模型 / Score-Based Generative Models）：从复杂数据分布中生成高质量样本。其成功依赖于随机过程与最优控制之间的深层联系。

本文的核心洞见：这两个方向可以在 **log 变换（Cole-Hopf 变换）** 的统一框架下联系起来。具体而言，随机过程逆问题的贝叶斯后验分布可以表示为一个 PDE，而这个 PDE 又与一个随机最优控制问题等价。

### 1.3 所解决的具体问题

给定一个由随机微分方程（SDE）$dY_t = b(Y_t, t)dt + \sqrt{\epsilon}\,dW_t$ 驱动的过程 $Y_t$，已知先验分布 $P_{\mathrm{prior}}(Y_0)$ 以及终端时刻的观测 $Y_T = y_{\mathrm{obs}}$，目标是从后验分布 $P(Y_t \mid Y_T = y_{\mathrm{obs}})$（$t \in [0, T)$）中采样。这是一类**随机过程的逆问题**：从终端观测反推全时间段的状态轨迹分布。

---

## 二、理论基础：Log 变换与线性-非线性系统的桥梁

### 2.1 抽象框架：线性系统与非线性系统

论文首先在抽象层面建立框架。引入一个一般线性算子 $\mathcal{A}_{\epsilon,t}$（可以是微分、差分、积分算子或其组合），构造一对线性方程：

$$\partial_t \mu = \mathcal{A}_{\epsilon,T-t}\,\mu, \qquad \partial_t \nu = \mathcal{A}_{\epsilon,t}^*\,\nu$$

其中 $\mathcal{A}_{\epsilon,t}^*$ 是 $\mathcal{A}_{\epsilon,t}$ 在 $L^2(\mathbb{R}^n)$ 上的伴随算子。下标 $\epsilon$ 反映随机性强度。

**Log 变换**建立 $(\mu, \nu)$ 与 $(\rho, S)$ 之间的非线性关系：

$$\rho(x,t) = \mu(x,T-t)\,\nu(x,t), \qquad S(x,t) = \epsilon\log\mu(x,T-t)$$

这把上述线性系统变换为一个耦合的非线性系统：

$$\partial_t S + \epsilon\, e^{-S/\epsilon}\,\mathcal{A}_{\epsilon,t}\,e^{S/\epsilon} = 0 \qquad \text{(广义 HJ 方程)}$$
$$\partial_t \rho + \rho\,e^{-S/\epsilon}\,\mathcal{A}_{\epsilon,t}\,e^{S/\epsilon} - e^{S/\epsilon}\,\mathcal{A}_{\epsilon,t}^*(\rho\,e^{-S/\epsilon}) = 0 \qquad \text{(广义 Fokker-Planck 方程)}$$

这一变换的意义在于：**线性系统（Kolmogorov 方程）本身容易求解，但其对应的非线性系统（HJ + Fokker-Planck）直接联系到最优控制与采样问题**。

![论文 Roadmap：黑色部分为已知结果，红色部分为本文贡献](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-02-figure-01.jpg)

### 2.2 已知联系：Log 变换与随机最优控制 / 最优输运

当 $\mathcal{A}_{\epsilon,t}$ 选为随机过程 $X_t$ 的**无穷小生成元（infinitesimal generator）** 时，线性系统的两个方程分别对应 Kolmogorov 后向方程（KBE）和前向方程（KFE）。log 变换则将其联系到随机最优控制和最优输运（SOT）问题——这在文献中已被广泛研究，被称为 **Cole-Hopf 变换**。

以标度布朗运动 $X_t = \sqrt{\epsilon}\,W_t$ 为例，生成元 $\mathcal{A}_{\epsilon,t} = \frac{\epsilon}{2}\Delta_x$，线性系统退化为两个热方程。非线性系统则变为经典的 Fokker-Planck + 粘性 HJ PDE：

$$\partial_t S + \tfrac{1}{2}\|\nabla_x S\|^2 + \tfrac{\epsilon}{2}\Delta_x S = 0$$

通过设定不同的初终条件，该 PDE 系统可联系到平均场博弈（MFG）、随机最优输运（SOT）以及 Schrödinger 桥问题。

![Log 变换在生成元情形下的结构示意，左侧为一般过程，右侧为布朗运动特例](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-03-figure-01.jpg)

### 2.3 本文核心贡献：Log 变换与贝叶斯推断的联系

**本文的理论新颖性在于选取 $\mathcal{A}_{\epsilon,T-t}$ 为随机过程 $Y_t$ 的生成元的伴随算子**，而非生成元本身。此时第一个线性方程描述 KFE，第二个描述 KBE。通过精心选取初始条件：

- $\mu$ 的初始条件设为 $Y_0$ 的先验密度 $P_{\mathrm{prior}}$
- $\nu$ 的初始条件设为 $\frac{\delta_z(\cdot)}{P(Y_T = z)}$（在观测点 $z$ 处的缩放 Dirac 质量）

由 KFE 性质，$\mu(\cdot, t)$ 演化为 $Y_t$ 的边际密度。对于 $\nu$，KBE 保证：

$$\nu(x, t) = \frac{P(Y_T = z \mid Y_{T-t} = x)}{P(Y_T = z)}$$

通过 log 变换，可以精确地得到：

$$\rho(x, t) = \mu(x, T-t)\,\nu(x, t) = P(Y_{T-t} = x \mid Y_T = z)$$

即 $\rho(\cdot, t)$ 恰好是给定终端观测 $Y_T = z$ 时，$Y_{T-t}$ 的**贝叶斯后验密度**。对应的非线性系统初终条件为：

$$\rho(x, 0) = \delta_{y_{\mathrm{obs}}}(x), \qquad S(x, T) = \epsilon\log P_{\mathrm{prior}}(x)$$

这意味着：HJ 方程的终端条件编码先验信息，Fokker-Planck 方程的初始条件编码观测数据，而 $\rho$ 从观测点处的 Dirac 质量演化到完整的后验分布。

![贝叶斯推断视角下的 log 变换：μ 从先验演化到数据分布，ρ 从 Dirac 质量演化到后验分布](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-06-figure-01.jpg)

上图清晰展示了三层演化关系：(1) 红色第一行：$\mu_t$ 从先验（右侧）沿 KFE 前向演化到数据分布（左侧）；(2) 蓝色第二行：$\nu_t$ 从缩放 Dirac 质量沿 KBE 演化到缩放似然；(3) 黑色第三行：$\rho_t = \mu_{T-t} \cdot \nu_t$ 从观测处的 Dirac 质量演化到后验分布。这三层的乘积关系正是 log 变换的几何含义。

---

## 三、从 HJB 解构造贝叶斯采样器：HJ-sampler

### 3.1 算法总体结构

基于第二节的理论联系，HJ-sampler 将贝叶斯后验采样转化为一个**两步法**：

**Step 1**：求解粘性 HJ PDE，确定最优控制 $\nabla_x S$

$$\partial_t S - b(x,T-t)\cdot\nabla_x S + \tfrac{1}{2}\|\nabla_x S\|^2 + \tfrac{\epsilon}{2}\Delta_x S - \epsilon\,\nabla_x\cdot b(x,T-t) = 0$$

终端条件 $S(x, T) = \epsilon\log P_{\mathrm{prior}}(x)$。

**Step 2**：从受控 SDE 中采样后验轨迹

$$dZ_\tau = \bigl(\nabla_x S(Z_\tau, \tau) - b(Z_\tau, T-\tau)\bigr)\,d\tau + \sqrt{\epsilon}\,dW_\tau, \qquad Z_0 = y_{\mathrm{obs}}$$

离散化后（Euler-Maruyama）：

$$Z_{k+1} = Z_k + \bigl(\nabla_x S(Z_k, \tau_k) - b(Z_k, T-\tau_k)\bigr)\Delta\tau + \sqrt{\epsilon\Delta\tau}\;\xi_k$$

$Z_k$ 即为 $Y_{T - k\Delta\tau} \mid Y_T = y_{\mathrm{obs}}$ 的后验样本近似。

这个两步法有一个关键的**结构优势**：Step 1 只依赖先验分布，不依赖观测数据 $y_{\mathrm{obs}}$，因此可以离线预计算。Step 2 依赖观测数据，但复用 Step 1 的结果。这意味着**更换观测值、观测时间、甚至时间离散化精度，都不需要重新计算控制函数**。

![SGM-HJ-sampler 算法示意：上方为训练阶段（Step 1），下方为推断阶段（Step 2）](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-08-figure-01.jpg)

![推断阶段：从观测点出发的受控轨迹演化到后验分布](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-08-figure-02.jpg)

上方两幅图直观展示了 SGM-HJ-sampler 的工作流程。训练阶段（Step 1）中，黑色曲线为从先验出发正向演化的样本路径，热力图为密度 $\mu_t$ 的演化，神经网络拟合 score function $\nabla\log P(Y_t)$。推断阶段（Step 2）中，所有轨迹从观测点 $y_{\mathrm{obs}}$ 出发，由学习到的控制引导，逐渐扩散到后验分布。

### 3.2 Riccati-HJ-sampler：当先验为高斯混合分布

当先验为高斯分布且 SDE 漂移项 $b(Y_t, t) = A(t)Y_t + \beta(t)$ 为线性时，HJ PDE 的 Hamiltonian 和初始条件都取二次形式，可通过 **Riccati ODE** 精确求解。

对单个高斯先验 $P_{\mathrm{prior}} \sim \mathcal{N}(\theta^P, \Sigma)$，HJ PDE 解为：

$$S(x, t) = -\tfrac{1}{2}(x - q(T-t))^T Q(T-t)^{-1}(x - q(T-t)) - r(T-t)$$

其中 $Q, q, r$ 满足 Riccati ODE 系统，初始条件由先验参数决定。控制函数为：

$$\nabla_x S(x, t) = -Q(T-t)^{-1}(x - q(T-t))$$

对**高斯混合先验** $P_{\mathrm{prior}} = \sum_j w_j P_{\mathrm{prior}}^j$，利用线性系统的叠加性质，解为 log-sum-exp 形式。每个分量独立求解 Riccati ODE，最终控制为加权组合。这一方法的计算成本与混合分量数成线性关系，非常高效。

### 3.3 SGM-HJ-sampler：利用 Score-Based 生成模型

对于更一般的情形（非线性漂移、非高斯先验），传统数值方法难以高效求解高维 HJ PDE。此时引入 **Score-Based Generative Model (SGM)** 作为 HJ PDE 的神经网络求解器。

核心观察：log 变换给出 $S(x, t) = \epsilon\log\mu(x, T-t)$，因此

$$\frac{1}{\epsilon}\nabla_x S(x, T-t) = \nabla_x \log P(Y_t = x) = \text{score function}$$

即 HJ PDE 的梯度解恰好是 $Y_t$ 的 score function。SGM 正是用神经网络 $s_W(x, t)$ 近似 score function 的方法。

**训练阶段**：从先验采样 $Y_0$，用 Euler-Maruyama 正向模拟 $Y_t$ 的轨迹，生成训练数据 $\{Y_{k,j}\}$。用隐式 score matching 损失函数训练神经网络：

$$\mathcal{L} = \sum_{k,j} \lambda_k \Bigl(\tfrac{1}{2}\|s_W(Y_{k,j}, t_k)\|^2 + \nabla_x \cdot s_W(Y_{k,j}, t_k)\Bigr)$$

高维情形下使用 sliced score matching 以提高可扩展性。

**推断阶段**：用学习到的 $s_W$ 替代 $\frac{1}{\epsilon}\nabla_x S$，采样受控 SDE：

$$Z_{k+1} = Z_k + \bigl(\epsilon\,s_W(Z_k, T-\tau_k) - b(Z_k, T-\tau_k)\bigr)\Delta\tau + \sqrt{\epsilon\Delta\tau}\;\eta_k, \quad Z_0 = y_{\mathrm{obs}}$$

---

## 四、与 Score-Based 扩散模型的统一与区别

### 4.1 统一框架

HJ-sampler 与标准扩散模型可以在 log 变换框架下统一理解。两者的区别仅在于 $\nu(\cdot, 0)$ 的选取：

| | $\mu(\cdot, 0)$ | $\mu(\cdot, T)$ | $\rho(\cdot, 0)$ | $\rho(\cdot, T)$ |
|---|---|---|---|---|
| **HJ-sampler** | 先验分布 | 数据分布 | 观测点 Dirac 质量 | 后验分布 |
| **扩散模型** | 数据分布 | 先验（噪声）分布 | $= \mu(\cdot, T)$ | $= \mu(\cdot, 0)$ |

扩散模型中 $\nu(\cdot, 0) \equiv 1$，对应无条件生成；HJ-sampler 中 $\nu(\cdot, 0) = \delta_{y_{\mathrm{obs}}}(\cdot)/P(Y_T = y_{\mathrm{obs}})$，对应以观测为条件的后验采样。

### 4.2 关键区别

尽管训练和推断阶段的公式形式相似，两者存在本质差异：

1. **过程关系不同**：扩散模型中 $Y_t$ 和 $Z_\tau$ 是前向-反向过程；HJ-sampler 中两者相差因子 $\nu$，不构成逆过程关系。
2. **初始分布不同**：扩散模型推断时从先验噪声采样；HJ-sampler 从观测点 $y_{\mathrm{obs}}$ 出发。
3. **加速技术不适用**：扩散模型中可用 ODE 求解器（如 DDIM、DPM-Solver）加速推断，因为前向和反向过程的边际分布匹配。HJ-sampler 中 $\nabla_x S \neq \epsilon\nabla_x\log\rho$，无法直接使用 ODE 替代 SDE 采样，也无法利用基于概率流 ODE 的加速技术。
4. **未来改进方向不同**：扩散模型聚焦于 SDE 设计、训练策略和推断加速；HJ-sampler 的改进方向在于将更多模型特定知识嵌入损失函数。

### 4.3 从扩散模型视角的等价解读

从扩散模型理论出发，SGM-HJ-sampler 也可理解为 SGM 的**条件采样变体**。标准反向 SDE

$$d\tilde{Y}_\tau = \bigl(\epsilon\,s_W(\tilde{Y}_\tau, T-\tau) - b(\tilde{Y}_\tau, T-\tau)\bigr)d\tau + \sqrt{\epsilon}\,dW_\tau, \quad \tilde{Y}_0 \stackrel{d}{=} Y_T$$

给出 $Y_t$ 的反向过程。若将 $\tilde{Y}_0$ 的分布从 $P(Y_T)$ 替换为 $\delta_{y_{\mathrm{obs}}}$，SDE 不变，则条件分布 $Z_\tau \mid Z_0 = y_{\mathrm{obs}}$ 恰好等于 $Y_{T-\tau} \mid Y_T = y_{\mathrm{obs}}$ 的后验分布。

---

## 五、数值实验

论文通过四组实验验证 HJ-sampler 的准确性、灵活性和可扩展性。

### 5.1 布朗运动验证（1D & 2D）

**设定**：标度布朗运动 $dY_t = \sqrt{\epsilon}\,dW_t$，先验为高斯或高斯混合分布，$\epsilon = 1, T = 1$。此问题有解析后验解，可作为 ground truth。

**定量结果**（Wasserstein-1 距离）：

| 方法 | $W_1$（均值 ± 标准差，1000 个随机 $y_{\mathrm{obs}}$） |
|---|---|
| analytic-HJ-sampler | 0.0024 ± 0.0006 |
| SGM-HJ-sampler | 0.0104 ± 0.0051 |

analytic-HJ-sampler 仅有 SDE 离散化误差，而 SGM-HJ-sampler 还包含神经网络近似误差。当 $\Delta\tau$ 从 0.01 减小到 0.001 时，SGM-HJ-sampler 的误差改善变缓，说明神经网络误差成为瓶颈。

**灵活性展示**：对高斯混合先验，同一个预训练神经网络在不同 $y_{\mathrm{obs}}$、不同观测时间 $s$、不同推断时间 $t$ 下均能产生高质量后验样本，无需重新训练。

### 5.2 Ornstein-Uhlenbeck 过程与模型不确定性

**第一种情形——一阶线性 ODE 系统的模型不确定性**：

ODE 系统 $dy_1/dt = y_2,\; dy_2/dt = -y_1 - y_2$ 加入白噪声成为 OU 过程。先验为二维高斯混合。Riccati-HJ-sampler 和 SGM-HJ-sampler 的后验样本高度吻合。

**第二种情形——二阶非线性 ODE 的模型误设（model misspecification）**：

精确 ODE 为 $u'' = -u + u^2 - u'$，被错误建模为 $\tilde{u}'' = -\tilde{u} - \tilde{u}'$。将误设的 ODE 加入白噪声以量化不确定性，$\epsilon$ 控制对误设模型的置信度。

![模型误设下的不确定性量化：不同 ε 对应不同的后验均值（虚线）和 2 标准差区间（阴影）](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-20-figure-09.jpg)

上图展示了模型误设的后果：仅用误设 ODE 反向推断（虚线 vs 实线）存在显著偏差。HJ-sampler 通过引入噪声 $\epsilon$ 来量化这种不确定性——$\epsilon$ 越大，后验分布越宽，反映更大的模型不确定性。

### 5.3 非线性 ODE 的模型误设

对非线性 ODE $dy/dt = f(t) + g(y)$，分别考虑：(a) $g(y) = 3y^2$ 误设为 $\tilde{g}(y) = y^2$（系数错误）；(b) $g(y) = 1.5y(1-y)$ 误设为 $\tilde{g}(y) = y^2$（形式错误）。SGM-HJ-sampler 在两种情形下均能有效捕捉模型不确定性，后验区间覆盖真实解。

### 5.4 高维问题（100 维）

推断定义在 $[0,1]$ 上的函数 $f_t$，在 $n = 100$ 个网格点上离散化为向量 $Y_t \in \mathbb{R}^{100}$。过程为标度布朗运动，先验为 8 阶正弦基函数的随机线性组合。SGM-HJ-sampler 使用 sliced score matching 训练。

![100 维问题结果：后验均值（红色十字）与 2 标准差区间（阴影）在不同时间快照的表现](../../pdfs/2026-04-16/hj-sampler-a-bayesian-sampler-for-inverse-problems-by-leveraging-hamilton-jacobi-pdes-and-score-based-generative-models.mineru/hybrid_auto/images/page-23-figure-01.jpg)

在 $t$ 接近 $T$ 时，后验紧密集中在观测值附近；随着 $t$ 远离 $T$，后验逐渐变宽且趋向先验。$t = 0$ 时，真实参考值（黑色线）落在 2 标准差区间内，验证了算法在高维情形下的有效性。

---

## 六、总结与评述

### 6.1 核心贡献

1. **理论层面**：揭示 log 变换（Cole-Hopf 变换）在 $\mathcal{A}_{\epsilon,T-t}$ 取为生成元伴随时与贝叶斯推断的新联系，将贝叶斯后验采样问题转化为 HJ PDE + 随机最优控制问题。
2. **算法层面**：提出 HJ-sampler 框架，包含 Riccati-HJ-sampler（解析方法，适用于线性-高斯情形）和 SGM-HJ-sampler（神经网络方法，适用于一般情形）两种变体。
3. **实践层面**：展示了该方法在模型不确定性量化、模型误设处理和高维问题上的有效性。

### 6.2 方法优势

- **先验与观测解耦**：Step 1 仅依赖先验，可离线预计算；Step 2 仅需设定观测初始条件，允许灵活更换观测值和观测时间。
- **轨迹采样**：直接生成后验样本路径，而非仅提供有限维度的样本点。
- **统一视角**：将贝叶斯推断、随机最优控制和扩散模型纳入同一理论框架。

### 6.3 局限与开放问题

1. **推断加速困难**：由于 $Y_t$ 和 $Z_\tau$ 不构成逆过程，无法直接借用扩散模型的 ODE 加速技术。
2. **部分观测问题**：当仅观测 $Y_T$ 的部分分量时，$\rho(\cdot, 0)$ 的采样（从条件分布中抽样）尚待进一步研究。
3. **扩展到一般随机过程**：理论框架适用于任何有良好无穷小生成元的过程（包括跳跃过程），但数值实现尚限于 SDE 情形。
4. **多次观测**：当前方法针对单次观测，多次序贯观测的扩展需要更新先验并重新求解 HJ PDE（可结合算子学习避免重训练）。

### 6.4 进一步思考方向

- 将神经网络作为动力学代理模型（NeuralODE/NeuralSDE），从数据驱动转向模型驱动的混合范式
- 利用 HJ-sampler 框架为扩散模型提供贝叶斯解释，探索条件生成与逆问题求解的跨领域迁移
- 探索 $\epsilon$ 作为置信度超参数的自适应选取策略，平衡模型偏差与不确定性

---
