---
title: "Predictor-Driven Diffusion for Spatiotemporal Generation"
authors: "Yuki Yasuda, Tobias Bischoff"
venue: "arXiv (2026)"
date_read: "2026-04-16"
topics: ["时空生成", "条件扩散", "天气预测", "自回归"]
---

# Predictor-Driven Diffusion for Spatiotemporal Generation

## 精读笔记

---

## 一、问题背景与动机

### 1.1 时空生成的多尺度困境

自然界与工程系统中普遍存在**多尺度空间结构（multiscale spatial structure）**：天气模式受云形成等小尺度过程调控（Bony et al., 2015），湍流场中不同波数的 Fourier 模式跨越数个数量级。在这类系统中，小尺度空间涨落会影响大尺度演化，但同时精确解析所有尺度在计算上往往不可行。

这带来一个根本性的建模矛盾：
- **保留全部尺度**：计算代价高昂，对高维时空场尤为严重
- **丢弃小尺度**：简单的低通滤波会丢失小尺度对大尺度的统计反馈，导致大尺度动力学预测出错

### 1.2 标准扩散模型的局限

扩散模型（Ho et al., 2020; Song et al., 2021）在生成任务中取得了巨大成功，其去噪过程看似具有从粗到细的特征（Rissanen et al., 2023）。然而，标准扩散模型对**所有 Fourier 模式施加均匀衰减**——中间状态按噪声水平而非空间分辨率排列。这意味着：

1. 多尺度层次仅**隐式**地从信噪比差异中浮现，而非被**显式**利用
2. 前向过程不构成严格的空间粗粒化（coarse-graining）
3. 无法直接支持不同空间分辨率下的仿真

### 1.3 重正化群（RG）扩散的进展与未解问题

物理学中的**重正化群（Renormalization Group, RG）** 通过逐步积掉小尺度自由度来构建多尺度层次（Wilson, 1971）。近年来，Cotler & Rezchikov (2023) 将 RG 与扩散模型结合，引入尺度依赖的 Laplacian 阻尼和噪声，使前向过程对应空间粗粒化、逆过程对应超分辨率。然而，已有的 RG 扩散模型**仅处理静态数据**（如图像）。

将 RG 扩散扩展到时空动力学面临一个关键困难：如果沿物理时间轴 $t$ 做粗粒化（平滑），就会将未来信息混入当下，**违反因果性（causality）**。

> **本文的核心提问：如何在显式保留空间多尺度层次的同时，保证时间方向上的因果性？**

### 1.4 本文方案一句话概括

学习一个在物理时间 $t$ 方向上做前向预测的 predictor，用它定义时空轨迹上的路径概率密度；这个密度的 score 可通过自动微分计算，从而支持沿扩散尺度 $\lambda$ 方向的逆向采样。一个网络同时统一**仿真（simulation）、无条件生成（generation）和超分辨率（super-resolution）** 三个任务。

---

## 二、RG 粗粒化作为扩散过程

### 2.1 前向过程：Laplacian 阻尼 + 噪声

论文采用 Carosso (2020) 的 RG 随机扩散形式化。对矢量场 $u_\lambda := u_\lambda(x,t)$，前向过程为：

$$\partial_\lambda u_\lambda = \alpha \nabla_x^2 u_\lambda + \beta \eta_\lambda \tag{1}$$

其中 $\alpha, \beta > 0$ 为常数，$\nabla_x^2$ 是空间 Laplacian，$\eta_\lambda$ 为时空白噪声。关键是**扩散尺度 $\lambda$**（而非物理时间 $t$）充当前向过程的"时间"参数。

在 Fourier 空间，波数为 $k$ 的模式以 $\exp(-\alpha \|k\|^2 \lambda)$ 的速率衰减——高波数（小尺度）模式衰减远快于低波数（大尺度）模式。随着 $\lambda$ 增大，$u_\lambda$ 变得越来越粗糙，截止波数约为 $k_{\mathrm{cut}} \sim 1/\sqrt{\alpha\lambda}$。

**噪声项不可省略**：没有噪声（$\beta = 0$），Laplacian 只做确定性平滑，简单地抹掉小尺度成分。有噪声时，对应的 Fokker–Planck 方程表明前向过程将场分布与 Gaussian 核做卷积——等价于对小尺度自由度的**边缘化（marginalization）**。这保留了被消除成分对大尺度成分的统计影响，区别于简单的低通滤波。

### 2.2 闭式解与条件密度

前向过程在每个 $\lambda$ 处有闭式解：

$$u_\lambda = \mathcal{C}_\lambda u_0 + \sqrt{\Sigma_\lambda}\,\epsilon \tag{3}$$

其中 $\mathcal{C}_\lambda := e^{\lambda\alpha\nabla_x^2}$ 是粗粒化算子，$\Sigma_\lambda$ 是由前向扩散导出的空间协方差矩阵，$\epsilon$ 是标准 Gaussian 噪声。在 Fourier 空间，两者均为对角阵：

$$\widetilde{\mathcal{C}}_\lambda(k) = e^{-\alpha\|k\|^2\lambda}, \quad \widetilde{\Sigma}_\lambda(k) = \frac{\beta^2(1 - e^{-2\alpha\|k\|^2\lambda})}{2\alpha\|k\|^2}$$

给定原始场 $u_0$，粗粒化场 $u_\lambda$ 服从 Gaussian 条件密度，且不同时间步之间独立——因为粗粒化仅作用于空间 $x$，不涉及时间 $t$，**因果性自动保持**。

### 2.3 逆过程：超分辨率

RG 前向过程的逆过程为（Anderson, 1982; Song et al., 2021）：

$$\partial_\lambda u_\lambda = \alpha\nabla_x^2 u_\lambda - \beta^2 \nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t) + \beta\eta_\lambda \tag{2}$$

从大 $\lambda$ 向小 $\lambda$ 积分，依次恢复小尺度成分——这在物理上对应**超分辨率**。与标准扩散不同，这里的中间状态有清晰的物理含义：每个 $\lambda$ 对应一个特定空间分辨率下的动力学。

---

## 三、核心框架：Predictor-Driven Diffusion

### 3.1 两轴结构

本文的核心设计思想是将**物理时间 $t$**（因果演化）与**扩散尺度 $\lambda$**（空间层次）视为两个独立的轴。

![Figure 1 — 框架示意图](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-02-figure-01.jpg)

*Figure 1 — 框架示意图。横轴为扩散尺度 $\lambda$（粗粒化程度），纵轴为物理时间 $t$。蓝色框：在固定 $\lambda$ 下沿 $t$ 方向做前向仿真；红色框：沿 $\lambda$ 方向做逆向积分，实现从噪声生成和超分辨率。一个 predictor 通过最小化路径密度间的 KL 散度训练，同时支持仿真、生成、超分辨率三个任务。*

- **沿 $t$ 轴**（蓝色箭头）：predictor 在任意固定 $\lambda$ 下模拟时间演化，仅使用过去信息，保证因果性
- **沿 $\lambda$ 轴**（红色箭头）：逆向 $\lambda$ 积分实现空间分辨率从粗到细的恢复

### 3.2 随机控制方程与路径概率

在每个固定的扩散尺度 $\lambda$，物理时间方向的演化用随机微分方程建模：

$$\partial_t u_\lambda = f_\lambda^\theta(u_\lambda) + \sigma_\lambda \xi \tag{6}$$

其中 $f_\lambda^\theta$ 是神经 predictor（漂移项），$\xi$ 为时空白噪声，$\sigma_\lambda$ 为噪声幅度。

**随机性的物理来源**：空间粗粒化消除了小尺度成分，时间增量 $\partial_t u_\lambda$ 自然继承了这些被消除自由度的涨落。噪声幅度 $\sigma_\lambda$ 可以从前向 RG 扩散的解析解估计。

在 Itô 约定下，上述 SDE 诱导出一个**可解析的路径概率密度（path density）**（Onsager & Machlup, 1953）：

$$p_\lambda(\{u_\lambda\}_t) = \frac{r_\lambda}{Z_\lambda}\exp\left[-\int_{\mathrm{x,t}} \frac{\|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2}{2\sigma_\lambda^2}\right] \tag{7}$$

这个路径积分形式有两个关键性质：
1. **可微**：对数密度关于 $u_\lambda$ 的梯度可通过自动微分计算，直接给出 path score $\nabla_{u_\lambda}\ln p_\lambda$
2. **归一化常数 $Z_\lambda$ 与 $f_\lambda^\theta$ 无关**：$Z_\lambda$ 仅依赖 $\sigma_\lambda$、$\Delta t$ 和网格维度，简化了训练

### 3.3 训练目标：路径密度间的 KL 散度

训练 predictor $f_\lambda^\theta$ 的目标是最小化数据路径密度 $q_\lambda$ 与 predictor 诱导的代理路径密度 $p_\lambda$ 之间的 KL 散度：

$$D_{\mathrm{KL}}(q_\lambda \| p_\lambda) = \frac{1}{2\sigma_\lambda^2}\mathbb{E}_{q_\lambda}\left[\int_{\mathrm{x,t}} \|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2\right] + \mathrm{const.} \tag{8}$$

因为 $Z_\lambda$ 不依赖 $\theta$，所有与 $\theta$ 无关的项被吸收进常数。最终的训练损失对 $\lambda \in [0,1]$ 取均匀平均：

$$\mathcal{L}(\theta) = \mathbb{E}_{\lambda\sim\mathcal{U}(0,1), q_\lambda}\left[\frac{1}{2\sigma_\lambda^2}\int_{\mathrm{x,t}} \|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2\right] \tag{9}$$

**最终效果：训练简化为在不同粗粒化尺度上对时间导数的加权回归。** 一个网络以 $\lambda$ 为额外输入，跨所有尺度训练。

### 3.4 Predictor 学到了什么

在存在真实细分辨率动力学 $\partial_t u_0 = f_0^{\mathrm{true}}(u_0)$ 的理想化情况下，最小化 $\mathcal{L}(\theta)$ 得到的最优漂移为：

$$f_\lambda^*(u_\lambda) \approx \mathbb{E}[\mathcal{C}_\lambda f_0^{\mathrm{true}}(u_0) \mid u_\lambda] \tag{10}$$

这个条件期望揭示了关键的**算子顺序**：先在细分辨率场上（包含所有小尺度成分）求得真实漂移，然后做粗粒化。这保留了小尺度动力学对大尺度演化的贡献。相反，如果先粗粒化再求漂移（$f_0^{\mathrm{true}}(\mathcal{C}_\lambda u_0)$），就会丢失这些跨尺度耦合——这正是简单低通滤波方法失败的原因。

---

## 四、推断：仿真与生成的统一

### 4.1 仿真模式

固定扩散尺度 $\lambda$，给定粗粒化的初始条件，沿物理时间 $t$ 积分控制方程 (6)。确定性评估时设 $\sigma_\lambda = 0$。该模式下不需要计算 path score，只需一次前向传播。

### 4.2 生成模式

利用逆向 $\lambda$ 方程：

$$\partial_\lambda u_\lambda = \alpha\nabla_x^2 u_\lambda - \beta^2 s_\lambda + \beta\eta_\lambda \tag{11}$$

其中 $s_\lambda := \nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t)$ 是 path score。训练完成后 $p_\lambda \approx q_\lambda$，逆向 $\lambda$ 采样生成的时空场近似服从数据分布 $q_0 (= q_\mathrm{d})$。

**关键优势**：path score 直接从 predictor 定义的路径密度 (7) 通过自动微分计算，**无需训练额外的 score 网络**。同时，这避免了通过物理时间 rollout 进行反向传播。

### 4.3 超分辨率模式

超分辨率只是生成模式的一个特例：从某个 $\lambda > 0$ 处的粗粒化仿真路径出发，通过逆向 $\lambda$ 积分恢复到 $\lambda = 0$，重建细尺度结构。

### 4.4 三种模式的统一

|  模式  | 固定轴 | 积分方向 | 输入 |
|--------|--------|----------|------|
| 仿真 | $\lambda$ | $t$ 前向 | 初始条件 |
| 生成 | — | $\lambda$ 逆向 | Gaussian 噪声 |
| 超分辨率 | — | $\lambda$ 逆向 | 粗粒化路径 |

三种模式共享同一个 predictor 网络，无需重新训练。

---

## 五、训练与采样的实现细节

### 5.1 训练流程（Algorithm 1）

1. 从训练数据采样时空路径 $\{u_0\}_t$
2. 采样 $\lambda \sim \mathcal{U}(0,1)$ 和 $\epsilon \sim \mathcal{N}(0, I)$
3. 解析计算粗粒化场：$u_\lambda = \mathcal{C}_\lambda u_0 + \sqrt{\Sigma_\lambda}\,\epsilon$
4. 计算局部时间导数上的回归损失
5. 更新网络参数

训练**不涉及时间方向上的 rollout**——损失仅在每个时间步的局部导数上计算。这与 DDPM 的逐步去噪训练在计算开销上相当。

### 5.2 噪声幅度 $\sigma_\lambda$ 的设定

通过匹配代理模型与数据分布的条件协方差，得到：

$$\sigma_\lambda^2 = \frac{1}{\Delta t \cdot D}\mathrm{tr}(\Sigma_\lambda) \tag{58}$$

这表明 $\sigma_\lambda$ 表征了粗粒化噪声的典型尺度。当 $\lambda \to 0$ 时 $\Sigma_\lambda \to 0$，$\sigma_\lambda \to 0$——动力学回归确定性。为数值稳定性，$\Sigma_\lambda$ 被下界限制在最小非零扩散尺度处。

### 5.3 逆向 $\lambda$ 采样的数值技巧

逆向 $\lambda$ 积分中，Laplacian 项 $\alpha\nabla_x^2 u_\lambda$ 变为反扩散（amplification），高波数模式被放大。论文采用**指数时间差分（ETD）方案**处理这种刚性问题：

$$\widetilde{u}_{\lambda-\Delta\lambda}(k,t) = e^{\alpha\|k\|^2\Delta\lambda}\widetilde{u}_\lambda(k,t) + \varphi(\alpha\|k\|^2\Delta\lambda)\beta^2\widetilde{s}_\lambda(k,t)\Delta\lambda + \beta\widetilde{\eta}_\lambda(k,t)\Delta\lambda$$

其中 $\varphi(z) = (e^z - 1)/z$。此外配合 predictor-corrector 采样（Langevin 校正步），进一步提高生成质量。

---

## 六、实验验证

### 6.1 实验设置

论文在两个代表性混沌系统上验证框架：

| 系统 | 空间维度 | 通道 | 空间网格 | 时间步 | 训练样本 |
|------|---------|------|---------|--------|---------|
| Lorenz-96 | 1D | 2 (X, Y) | 128 | 64 | 3,000 |
| Kolmogorov flow | 2D | 1 (涡度 $\zeta$) | 40×40 | 40 | 6,000 |

**Lorenz-96 模型**是一维周期域上的理想化大气模型，包含慢变量 $X$（大尺度）和快变量 $Y$（小尺度），时间尺度分离约一个数量级。**Kolmogorov flow** 是二维不可压驱动流，广泛用于湍流研究和 ML 基准。

网络架构为 U-Net（Saharia et al., 2022a），输入当前状态和前 4 个时间步，输出时间导数的有限差分近似。$\lambda$ 通过 FiLM 条件化注入网络。基线模型为使用相同架构的 DDPM。

### 6.2 仿真结果

![Figure 2 — Lorenz-96 仿真结果](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-05-figure-01.jpg)

*Figure 2 — Lorenz-96 模型的仿真结果。上排：细分辨率 $\lambda = 0$；下排：粗粒化 $\lambda = 0.2$。左：慢变量 X；右：快变量 Y。每个面板左侧为时空演化图，右侧为时间平均空间功率谱密度（PSD）。代理模型准确再现了物理仿真的时空模式和谱统计特性。*

![Figure 3 — Kolmogorov flow 仿真结果](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-05-figure-02.jpg)

*Figure 3 — Kolmogorov flow 的仿真结果。上排：$\lambda = 0$；下排：$\lambda = 0.2$。左：第 6 时间步的涡度场快照；右：时间平均 PSD。粗粒化移除了小尺度结构但保留了大尺度动力学。*

在 $\lambda = 0$ 处与 DDPM 基线对比（Table 1）：

| 指标 | Predictor-Driven | DDPM (Baseline) |
|------|-----------------|-----------------|
| L96 $L^2$ error | **0.503** (±0.011) | 0.557 (±0.031) |
| KF $L^2$ error | **0.691** (±0.057) | 0.861 (±0.023) |
| L96 谱误差 | **0.120** (±0.014) | 0.226 (±0.077) |
| KF 谱误差 | 0.182 (±0.029) | **0.139** (±0.021) |

两种方法的精度相当，但本文方法额外支持在任意 $\lambda > 0$ 下仿真——这是 DDPM 无法做到的。

### 6.3 无条件生成结果

用同一个训练好的网络，从 Gaussian 噪声出发沿 $\lambda$ 逆向积分，生成时空样本：

| 指标 | Predictor-Driven | DDPM (Baseline) |
|------|-----------------|-----------------|
| L96 谱误差 | 0.343 (±0.028) | **0.267** (±0.020) |
| KF 谱误差 | **0.457** (±0.025) | 0.615 (±0.121) |

生成质量与专门训练的 DDPM 基线相当，验证了 predictor 定义的路径密度确实为扩散式生成提供了可用的 score。

### 6.4 超分辨率结果

![Figure 4 — 超分辨率结果](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-06-figure-01.jpg)

*Figure 4 — 超分辨率结果。上：Lorenz-96；下：Kolmogorov flow，均展示第 6 时间步。左：$\lambda = 0$ 处的超分辨率输出；中：$\lambda = 0.2$ 处的低分辨率输入；右：PSD 对比。逆向 $\lambda$ 积分成功恢复了低分辨率输入中缺失的小尺度结构。*

| 指标 | 超分辨率 (SR) | 低分辨率 (LR at $\lambda=0.2$) |
|------|-------------|-------------------------------|
| L96 谱误差 | **0.345** (±0.027) | 0.873 (±0.005) |
| KF 谱误差 | **0.303** (±0.011) | 0.743 (±0.005) |

超分辨率大幅降低了谱误差，恢复的细结构谱统计与无条件生成相当。

---

## 七、消融实验与进一步分析

### 7.1 输入时间步数的影响

在 $\lambda = 0$ 处，Lorenz-96 系统是 Markov 的，使用单步输入即可准确预测。但在 $\lambda = 0.2$ 处，粗粒化破坏了 Markov 性——单步输入无法捕获大尺度变异性，产生单调模式。随着输入窗口从 5 步增加到 15 步，谱误差从约 0.6 降至约 0.3。

这与 **Mori–Zwanzig 投影算子理论**一致：当小尺度成分被消除时，它们对大尺度动力学的反馈必须通过大尺度变量的历史来表征，从而打破 Markov 性。

### 7.2 噪声注入的必要性

当训练时不注入噪声（$\epsilon \equiv 0$），即用确定性粗粒化数据训练：

- **仿真**：$\lambda \approx 0$ 时仍然稳定，但 $\lambda$ 增大时数值不稳定
- **生成**：完全失败，生成的样本呈噪声状
- **超分辨率**：同样失败

这验证了 RG 理论的预测：噪声通过概率分布的卷积实现了对被消除小尺度自由度的**统计积分**，是逆向过程能够重建小尺度结构的前提。

### 7.3 架构鲁棒性

用 FNO（Fourier Neural Operator）替换 U-Net，在仿真、生成和超分辨率上均获得可比的结果，表明框架对网络架构不敏感。

---

## 八、与相关工作的定位

| 方法类别 | 代表工作 | 与本文的区别 |
|---------|---------|------------|
| 标准扩散/流匹配 | Ho et al., Song et al. | 沿扩散时间建模 score/drift；中间状态无明确物理含义 |
| RG 扩散 | Cotler & Rezchikov, 2023 | 仅处理静态数据，未考虑时间演化 |
| Neural ODE/SDE | Chen et al., 2018; Kidger et al., 2021 | 固定分辨率，无显式扩散尺度 $\lambda$ |
| 条件扩散预测 | Price et al., 2025 (GenCast) | predictor 和 super-resolver 分开训练 |
| 能量模型 | Gao et al., 2021 | 目标为静态数据分布 |
| **本文** | — | 物理时间 $t$ 的漂移 + 扩散尺度 $\lambda$ 的 RG 层次，单网络统一三任务 |

本文的独特贡献在于将 $t$ 和 $\lambda$ 作为两个独立轴，通过路径积分将时间演化的 predictor 与空间多尺度的 RG 扩散桥接起来。

---

## 九、局限性与未来方向

### 9.1 作者自述局限

1. 框架面向受物理方程支配的时空场；对缺乏显式控制方程的通用视频数据，适用性未经探索
2. 初始密度 $r_\lambda$ 被视为经验给定，适用于平稳系统但需扩展到瞬态设定
3. 仅在 1D Lorenz-96 和 2D Kolmogorov flow 上验证；向更高分辨率和 3D 数据的可扩展性未经测试
4. 生成和超分辨率比仿真代价更高，因为每个逆向 $\lambda$ 步都需计算 path score
5. 粗粒化参数 $\alpha, \beta$ 可能需要系统特定的调优

### 9.2 进一步优化方向

- **$\lambda$ 依赖的阻尼和噪声调度**：借鉴 Sheshmani et al. (2025) 的优化策略提升效率
- **减少逆向 $\lambda$ 步数**：通过采样器或噪声调度优化降低生成成本
- **学习初始密度 $r_\lambda$**：当前通过线性外推处理时间边界，显式建模 $r_\lambda$ 可能提升非平稳场景的性能
- **向真实地球系统扩展**：论文第一作者来自 JAMSTEC（日本海洋研究开发机构），框架天然适合气候模拟的降尺度应用

---

## 十、核心结论

1. **空间 RG + 时间路径积分 = 因果且多尺度的生成框架**：通过将空间粗粒化（$\lambda$ 轴）与因果时间演化（$t$ 轴）解耦，避免了时间方向粗粒化带来的因果性问题。

2. **训练目标等价于加权时间导数回归**：KL 散度的极小化归结为一个简单的回归损失，无需训练 score 网络或做时间方向 rollout。

3. **Predictor 隐式编码了跨尺度耦合**：最优漂移的条件期望形式（先算细分辨率漂移再粗粒化）保证了小尺度对大尺度的统计影响被正确保留。

4. **三任务统一**：仿真（沿 $t$）、生成（沿 $\lambda$ 逆向）、超分辨率（从中间 $\lambda$ 开始逆向）共享一个网络，仅通过改变输入和积分方向切换任务。

5. **噪声不可省略**：噪声实现了 RG 意义上的统计积分，是逆向过程能够重建小尺度结构的理论和实验前提。

---

## 关键术语索引

| 中文 | 英文 | 简述 |
|------|------|------|
| 扩散尺度 | Diffusion scale $\lambda$ | 参数化空间粗粒化程度的连续变量 |
| 粗粒化算子 | Coarse-graining operator $\mathcal{C}_\lambda$ | $e^{\lambda\alpha\nabla_x^2}$，在 Fourier 空间为逐模式指数衰减 |
| 路径密度 | Path density $p_\lambda$ | predictor 在物理时间上诱导的轨迹概率分布 |
| 路径分数 | Path score $s_\lambda$ | $\nabla_{u_\lambda}\ln p_\lambda$，用于逆向 $\lambda$ 采样 |
| KL 散度 | KL divergence | 数据路径密度与代理路径密度间的差异度量 |
| 重正化群 | Renormalization Group (RG) | 通过逐步积掉小尺度自由度构建多尺度层次的物理方法 |
| Mori–Zwanzig 形式 | Mori–Zwanzig formalism | 说明粗粒化破坏 Markov 性，需要历史记忆的理论框架 |
| 指数时间差分 | Exponential Time Differencing (ETD) | 处理刚性 ODE/SDE 的数值方法，用于逆向 $\lambda$ 积分 |
| 超分辨率 | Super-resolution | 从低分辨率（大 $\lambda$）场恢复高分辨率（$\lambda=0$）场 |
| 功率谱密度 | Power Spectral Density (PSD) | 衡量不同空间频率能量分布的统计量 |
