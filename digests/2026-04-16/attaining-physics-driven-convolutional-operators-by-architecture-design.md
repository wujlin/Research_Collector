---
title: "Attaining Physics-Driven Convolutional Operators by Architecture Design"
authors: "Zhenhua Xiong, Pengyang Zhao"
venue: "Communications Physics (2026)"
date_read: "2026-04-16"
topics: ["物理约束", "卷积算子", "Scientific ML", "架构设计"]
---

# Attaining Physics-Driven Convolutional Operators by Architecture Design

## 精读笔记

---

## 一、问题背景与动机

### 1.1 算子学习的核心需求

偏微分方程 (PDE) 是物理建模的基础语言。对于工程应用而言，需要的不是对**单个** PDE 实例的求解，而是对**一族** PDE 的统一求解能力——同一控制方程在不同微观结构、不同初始条件、不同材料参数下的解。数学上，这等价于学习一个**非线性算子**：从输入函数空间（如微观结构场、初始条件场）到输出函数空间（如位移场、应力场）的无穷维到无穷维映射。

### 1.2 现有算子学习方法的局限

**DeepONet**（Lu et al., 2021）基于 Chen & Chen 的算子通用逼近定理，将算子表示为 branch net（编码输入函数）与 trunk net（编码评估位置）的向量内积。然而 branch net 依赖输入函数的特定离散化形式，未能严格实现网格无关性。

**FNO**（Li et al., 2021）利用卷积定理将空间积分变换为 Fourier 域的逐点乘法，高效捕捉全局特征。但存在两个根本弱点：

- **Gibbs 现象**：全局谱变换在处理尖锐界面不连续性时，高频截断导致振荡伪影
- **谱偏差 (spectral bias)**：MLP 骨干网络对高频特征收敛困难

两类方法的共同瓶颈在于：它们依赖**连续空间中算子的解析表示**，而深度学习中许多关键的高效操作（池化、LSTM 门控）本质上是离散的，无法自然嵌入这一连续框架。作者用一个精妙类比概括这一现象：通用逼近定理是算子学习的"热力学论证"（证明可行性），但"动力学路径"（实现高效训练的架构设计）仍需探索。

### 1.3 本文的切入点

能否借鉴图像处理领域已经成熟的架构设计，构建一个**完全由物理驱动**、不需要任何标注数据的卷积算子？

这一思路的合理性基于两个观察：

1. 全卷积网络 (FCN) 天然支持任意输入尺寸、保留空间信息，适合做像素级的 image-to-image 映射
2. 有限差分法 (FDM) 的微分算子可以被精确编码为**固定卷积核**，与 FCN 的卷积操作天然兼容

---

## 二、方法：物理驱动卷积算子 (PDCO)

### 2.1 整体框架

![Fig. 1a — PDCO 训练流程](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-23-figure-01.jpg)

PDCO 的训练回路如上图所示：随机采样的微观结构或初始状态作为输入 → PDCO 网络前向推理 → 输出场通过**固定 FDM 卷积核**计算空间/时间导数 → 代入 PDE 残差构造物理损失 → 反向传播更新网络参数。整个过程**不需要任何标注数据**。

![Fig. 1b — PDCO 推理能力：物理预测与物理推断](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-23-figure-02.jpg)

训练完成后，PDCO 可作为代理模型进行两类推理：
- **Physics-based prediction**（浅橙色区域）：对训练分布内的新初始条件做预测
- **Physics-based inference**（浅蓝色区域）：对训练分布外的配置做外推（如更多激励源、更长时间）

### 2.2 架构设计：时间无关 vs 时间相关

PDCO 根据 PDE 类型采用两种骨干网络：

| PDE 类型 | 骨干网络 | 核心思想 |
|---------|---------|---------|
| 时间无关（如 Eshelby 夹杂问题） | **U-Net** | encoder 逐层下采样提取多尺度特征 + decoder 上采样恢复空间分辨率 + skip connection 保留高频细节 |
| 时间相关（如弹性波、Allen-Cahn） | **ConvLSTM** | 卷积层提取空间特征 + LSTM 门控（输入门、遗忘门、输出门）建模时间依赖 + 自回归递推时间步 |

#### U-Net（时间无关 PDE）

U-Net 的 encoder 路径通过卷积 + 池化逐步提取从低频（宏观应力分布）到高频（界面梯度）的多尺度特征，decoder 路径通过上采样 + skip connection 恢复像素级精度。数学表达：

**Encoder**（第 \(k\) 层）：

$$\mathbf{z}_k^e = \sigma(\mathbf{W}_k^e * \mathbf{y}_{k-1}^e + \mathbf{b}_{k-1}^e), \quad \mathbf{y}_k^e = \mathcal{P}(\mathbf{z}_k^e)$$

**Decoder**（第 \(k\) 层）：

$$\mathbf{z}_k^d = \mathcal{U}(\mathbf{y}_{k+1}^d), \quad \mathbf{y}_k^d = \sigma(\mathbf{W}_k^d * [\mathbf{z}_k^d \oplus \mathbf{z}_k^e] + \mathbf{b}_k^d)$$

其中 \(\mathcal{P}\) 为池化下采样，\(\mathcal{U}\) 为上采样，\(\oplus\) 为通道拼接。skip connection \(\mathbf{z}_k^e\) 将浅层高分辨率特征直接传递给 decoder，避免信息瓶颈。

与传统 MLP 方法将物理参数作为损失函数中的固定系数不同，U-Net 将微观结构场与弹性参数作为**多通道图像输入**，将求解过程转化为 image-to-image 的映射问题。

#### ConvLSTM（时间相关 PDE）

ConvLSTM 将连续时间演化离散化为等距时间步 \(\{0, \Delta t, 2\Delta t, \ldots\}\)，采用**自回归递推**机制：在每个时间步 \(t\)，当前场 \(u^t\)、隐藏状态 \(\mathbf{h}^t\)、细胞状态 \(\mathbf{C}^t\) 共同预测下一步 \(u^{t+1}\)，同时更新状态变量。

门控机制定义为：

$$\mathbf{i}^t = \sigma(\mathbf{W}^i * [u^t, \mathbf{h}^{t-1}] + \mathbf{b}^i), \quad \mathbf{f}^t = \sigma(\mathbf{W}^f * [u^t, \mathbf{h}^{t-1}] + \mathbf{b}^f)$$

$$\mathbf{C}^t = \mathbf{f}^t \times \mathbf{C}^{t-1} + \mathbf{i}^t \times \tanh(\mathbf{W}^c * [u^t, \mathbf{h}^{t-1}] + \mathbf{b}^c)$$

$$\mathbf{h}^t = \mathbf{o}^t \times \tanh(\mathbf{C}^t)$$

这一设计的关键优势：将空间离散化与时间积分分离处理，与传统数值求解器（如时间步进法）的思路一致，但全部嵌入 FCN 架构中。固定步长 \(\Delta t\) 的自回归策略确保了长时间推理的数值稳定性。

### 2.3 物理驱动损失函数

PDCO 的核心创新之一是**完全无标注数据训练**。其物理损失的构建依赖三个关键组件：

#### (a) FDM 卷积核：替代自动微分

FCN 处理的是像素化图像输入，缺乏严格的物理坐标定义，因此无法使用自动微分计算导数。本文采用四阶精度中心差分格式构造固定卷积核：

$$W_x = \frac{1}{12h}\begin{bmatrix} 0&0&0&0&0\\ 0&0&0&0&0\\ 1&-8&0&8&-1\\ 0&0&0&0&0\\ 0&0&0&0&0 \end{bmatrix}, \quad W_y = \frac{1}{12h}\begin{bmatrix} 0&0&1&0&0\\ 0&0&-8&0&0\\ 0&0&0&0&0\\ 0&0&8&0&0\\ 0&0&-1&0&0 \end{bmatrix}$$

$$W_{\text{Laplace}} = \frac{1}{12h^2}\begin{bmatrix} 0&0&-1&0&0\\ 0&0&16&0&0\\ -1&16&-60&16&-1\\ 0&0&16&0&0\\ 0&0&-1&0&0 \end{bmatrix}$$

这些固定卷积核的计算资源消耗仅取决于离散网格分辨率，**与网络架构复杂度无关**。对比 MLP 的自动微分需要存储整个计算图进行反向传播，FDM 核在高阶微分方程中展现出显著的数值稳定性优势。

#### (b) 物理驱动的边界填充算法

- **Dirichlet 边界条件**：将已知边界函数值直接编码到网络输出层，形成硬约束
- **Neumann 边界条件**：基于有限差分格式的外推方案，利用内部节点梯度信息动态生成边界虚拟节点值

#### (c) 损失函数策略

- **时间无关问题**（Eshelby 夹杂）：基于变分原理，最小化系统总弹性能——自然满足平衡态约束而无需显式计算强形式中的高阶导数
- **时间相关问题**（弹性波、Allen-Cahn）：基于 PDE 残差的 MSE——在每个时间步施加控制方程约束

---

## 三、实验验证

### 3.1 Eshelby 夹杂问题（时间无关 PDE）

**问题定义**：非均匀材料中含椭球夹杂体的弹性力学问题。控制方程：

$$[C_{ijkl}(\mathbf{x})(u_{k,l}(\mathbf{x}) - \epsilon_{kl}^*(\mathbf{x}))]_{,j} = 0$$

其中 \(C_{ijkl}(\mathbf{x})\) 为空间变化的弹性刚度张量，\(\epsilon_{kl}^*\) 为本征应变场。

**训练设置**：

- 输入：3 个弹性常数场 + 1 个序参量场（4 通道），\(256 \times 256\) 分辨率
- 训练集：10,000 个随机生成的含 1-3 个椭球夹杂体的微观结构
- 骨干：五层级联 U-Net

**定量验证**：

![Fig. 2 — 圆形夹杂体应力场对比](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-24-figure-01.jpg)

在标准圆形夹杂体基准上，PDCO 预测的应力场 \(\sigma_{xx}, \sigma_{yy}, \sigma_{xy}\) 与 MLP 参考解的全场相对误差仅为 **0.02%**。最大偏差集中在夹杂体/基体界面附近——这与高对比度界面处导数表征的复杂性直接相关。

**分布外泛化**：

![Fig. 3 — 多夹杂体外推预测](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-25-figure-01.jpg)

PDCO 成功泛化至训练集之外的构型：
- 4 个夹杂体（训练集最多 3 个）：MSE = \(3.2 \times 10^{-4}\)
- 不同弹性模量的夹杂体：MSE = \(3.3 \times 10^{-4}\)
- 混合几何形状 + 不同弹性性质：MSE = \(4.5 \times 10^{-4}\)

这种分布外泛化能力归因于 PDCO 捕获了底层算子的**内禀性质**（如 Eq. 2 的旋转不变性），而非仅仅记忆训练分布。

### 3.2 弹性波传播（时间相关 PDE）

**问题定义**：各向异性弹性波在多层非均匀介质中的传播，涉及宏观波传播与微观结构异质性引发的散射/反射现象的共存。

**训练设置**：

- 四层梯度模量分布（衰减系数 0.8），周期边界条件
- 输入：随机分布振动源产生的初始位移场，\(128 \times 128\) 分辨率
- 时间步 \(\Delta t = 0.005s\)，训练至 \(t = 0.5s\)
- 骨干：ConvLSTM

**定量结果**：

![Fig. 4 — 弹性波传播位移场对比](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-26-figure-01.jpg)

PDCO 预测的 \(u_x, u_y\) 位移分量 MSE 为 \(1.05 \times 10^{-4}\)，与有限差分法 (FDM) 参考解的 \(6.65 \times 10^{-3}\) 形成显著对比。波的传播过程、界面反射与散射现象均被准确捕获。

**时间外推能力**：PDCO 在训练时域 \(t \leq 0.5s\) 之外，成功预测了总时长延长 50% 的波场（至 \(t = 0.75s\)），MSE 仅为 \(8.86 \times 10^{-4}\)。这种双重外推能力（激励源数量 + 时间域）是纯数据驱动方法难以具备的。

### 3.3 Allen-Cahn 方程（相场演化）

**问题定义**：

$$\partial \eta / \partial t - c_1^2 \Delta \eta + c_2(\eta^3 - \eta) = 0$$

描述非守恒序参量的微观结构演化，涉及微观尺度扩散界面宽度与宏观尺度相域几何演化的耦合。

**训练设置**：

- 初始条件：\([-0.5, 0.5]\) 均匀分布的连续场，10,000 个样本
- 材料参数 \((c_1, c_2) = (0.01, 1)\)，\(\Delta t = 0.01s\)
- 训练至 \(t = 3s\)（300 个时间步）

**定量结果**：训练时域内 MSE 始终保持在 **0.1%** 以下。

**时间外推**：仅在 \(t < 2s\) 上训练，模型稳定外推至 \(t = 5s\)——**2.5 倍训练时域**。Allen-Cahn 动力学的非线性性质使得长程外推尤为困难，PDCO 的成功表明其架构有效利用了短期训练来推断长期动力学。

### 3.4 热力学与物理一致性验证

![Fig. 8a — 弹性波系统 Lagrangian 演化](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-30-figure-01.jpg)

![Fig. 8b — Allen-Cahn 系统自由能演化](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-30-figure-02.jpg)

超越空间精度的验证——两个时间相关系统的基本动力学描述符：

- **弹性波**（守恒系统）：全局 Lagrangian \(\mathcal{L}_{sys}(t) = \mathcal{K}(t) - \mathcal{U}(t)\) 在训练域和外推域均保持振荡模式和相位保真度，无非物理发散
- **Allen-Cahn**（耗散系统）：总自由能严格单调递减至稳态平衡，即使在渐近域存在微小数值偏差，也**未出现非物理的能量增长**

这些结果证明物理驱动损失函数有效正则化了解路径，确保模型在训练时域之外依然遵循基本物理定律。

### 3.5 计算效率对比

![Table 1 — 模型定量对比](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-22-table-01.jpg)

| 模型 | 参数量 | 内存占用 | 训练时间 | MSE |
|------|-------|---------|---------|-----|
| **PDCO** | **0.03M** | **508 MiB** | **5040s** | **1.30 × 10⁻¹⁰** |
| MLP | 117.46M | 2728 MiB | 14342s | 1.76 × 10⁻⁷ |
| DeepONet | 0.75M | 1196 MiB | 8760s | 5.07 × 10⁻⁵ |
| FNO | 12.60M | 1070 MiB | 14571s | 1.05 × 10⁻⁷ |

PDCO 以**比 MLP 少近 4 个数量级的参数**（0.03M vs 117.46M）达到了比 MLP 高 **3 个数量级**的精度（10⁻¹⁰ vs 10⁻⁷），训练时间缩短约 3 倍。

![Fig. 9a — 训练效率对比](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-31-figure-01.jpg)

![Fig. 9b — 单次预测推理时间对比](../../pdfs/2026-04-16/attaining-physics-driven-convolutional-operators-by-architecture-design.mineru/hybrid_auto/images/page-31-figure-02.jpg)

物理驱动的 PDCO 跳过了昂贵的数据生成阶段，实现了显著更低的总训练开销。单次推理速度方面，PDCO 相较 MLP 快约 **4-5 个数量级**。

---

## 四、方法论分析

### 4.1 为什么卷积架构比 MLP 更适合算子学习？

| 维度 | MLP / DeepONet / FNO | PDCO (FCN) |
|-----|----------------------|------------|
| 导数计算 | 自动微分（需存储完整计算图） | FDM 固定卷积核（仅依赖网格分辨率） |
| 空间信息 | 展平为向量，丢失拓扑结构 | 保留二维空间相关性 |
| 多尺度能力 | 单一尺度或全局谱变换 | encoder-decoder + skip connection 显式多尺度 |
| 高阶微分 | 需多输出策略缓解数值不稳定 | 组合卷积核直接计算任意阶导数 |
| 边界条件 | 软约束（惩罚项） | 硬约束（虚拟节点填充） |
| 参数效率 | 全连接层参数爆炸 | 权值共享 + 局部感受野 |

### 4.2 FDM 卷积核的理论优势

从 Taylor 展开严格导出的四阶精度差分格式被编码为 \(5 \times 5\) 固定卷积核。这一设计有三重优势：

1. **精度可控**：差分阶数由卷积核大小决定，可根据精度需求灵活调整
2. **资源可预测**：计算量仅取决于 \(O(N^2 \cdot k^2)\)（\(N\) 为网格尺寸，\(k\) 为核大小），与网络深度无关
3. **数值稳定性**：在高阶 PDE（如四阶弹性方程）中避免了自动微分链式法则的梯度放大问题

### 4.3 物理驱动 vs 数据驱动的根本差异

PDCO 的"无标注训练"不是简单地移除标签，而是将物理定律**结构性地嵌入**训练流程：

- 训练时随机采样初始/边界条件，无需预先求解 PDE 生成标注数据
- 物理损失作为正则化器，强制模型沿物理合法路径优化
- 外推时遵循物理约束（能量守恒/耗散），而非简单的模式外推

---

## 五、局限性与讨论

1. **网格依赖性**：PDCO 在固定网格上构建，未实现严格的网格无关性（mesh-independence）。作者将其定位为"在典型工程网格分辨率范围内对连续算子的高效逼近"，而非严格的无穷维算子。

2. **时间离散化固定步长**：ConvLSTM 的时间步 \(\Delta t\) 在训练和推理中固定，引入时间域的离散化依赖。作者论证这一选择对长时间推理的数值稳定性至关重要。

3. **二维限制**：所有实验均在 2D 域上进行，三维扩展的计算开销和架构调整有待探索。

4. **问题范围**：目前仅验证了周期边界条件和相对规则的几何域，对复杂不规则域的适用性有待考察。

---

## 六、核心贡献总结

1. **架构创新**：将 U-Net + ConvLSTM 的图像处理架构系统性地迁移至 PDE 算子学习，通过 FDM 卷积核实现物理约束与卷积操作的无缝对接
2. **无标注训练范式**：完全物理驱动的损失函数消除了对昂贵标注数据的依赖，将训练成本降低至数据驱动方法的 47%-75%
3. **物理推断能力**：在三个代表性 PDE 系统上展示了超越训练分布的外推能力（空间构型外推 + 时间域外推），且满足热力学一致性
4. **极致参数效率**：0.03M 参数实现 10⁻¹⁰ 量级 MSE，比同类方法少 1-4 个数量级参数的同时精度提高 3-5 个数量级

---

## 七、延伸思考

- **与 PINN 的关系**：PDCO 可视为 PINN 的"图像版本"——将 MLP 的逐点函数学习替换为 FCN 的全场图像映射，本质上是同一物理驱动理念在不同架构下的实现。FDM 卷积核扮演了自动微分在 PINN 中的角色。
- **与 Neural Operator 的互补性**：PDCO 牺牲了严格的网格无关性，换取了实用场景下的极致参数效率和物理外推能力。对于需要在固定工程网格上高效求解的应用场景（如微观力学、材料设计），这一权衡是合理的。
- **潜在扩展方向**：(1) 三维扩展需引入 3D 卷积核和更高效的多尺度架构；(2) 与自适应网格方法结合可能突破网格依赖性限制；(3) ConvLSTM 的时间步长自适应可能进一步提升时间外推能力。
