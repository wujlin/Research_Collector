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

## 1. 问题定义：最小做功的概率质量逆转

### 1.1 物理直觉

考虑一个多体随机系统：它有一个"结构化"的目标状态（如图像分布 $p_{\text{data}}$）和一个"无序"的参考状态（如高斯噪声 $p_{\text{ref}}$）。系统的**自然弛豫**（natural relaxation）方向是从结构走向无序——这正是扩散过程（diffusion）所做的事。核心问题是：

> **能否找到一个最小做功的随机过程，将这一弛豫过程逆转？**

这个问题同时出现在非平衡统计力学（non-equilibrium statistical mechanics）和随机控制（stochastic control）中。

### 1.2 数学形式化

设 $\mathbf{x}_t \in \mathbb{R}^d$ 遵循受控 Itô SDE：

$$d\mathbf{x}_t = \mathbf{u}_t \, dt + \sqrt{2D} \, d\mathbf{B}_t$$

其中 $\mathbf{u}_t$ 是控制输入，$D > 0$ 是扩散系数。边界条件为 $\mathbf{x}_0 \sim p_{\text{ref}}$，$\mathbf{x}_1 \sim p_{\text{data}}$。最优控制问题表述为：

$$\min_{\mathbf{u}_t} \; \mathbb{E}_{\mathbb{P}_\mathbf{u}} \left[ \int_0^1 \nu(\mathbf{x}_t) \, dt + \frac{\gamma}{2} \int_0^1 \|\mathbf{u}_t\|^2 \, dt \right]$$

其中：
- $\nu(\mathbf{x}) \geq 0$：**空间代价函数**（spatial cost function），惩罚物理上不合法或不安全的状态
- $\gamma > 0$：控制代价权重
- 目标函数同时包含**轨迹级的空间惩罚**和**控制能耗**

这一形式化的关键洞察在于：它不仅关心端点分布的匹配（如 flow matching、score-based diffusion），更关心**整条轨迹的最优性**——每一步的做功和路径的空间可行性都被显式考虑。

### 1.3 与现有方法的本质区别

| 方法 | 优化对象 | 轨迹最优性 | 空间约束 |
|------|----------|------------|----------|
| Score matching | 逆向漂移场 | 无 | 无 |
| Flow matching | 边际分布匹配 | 无 | 无 |
| Schrödinger bridge | KL-正则化端点传输 | 弱（熵正则化） | 无 |
| **本文 (HJB matching)** | **路径空间代价泛函** | **是（变分最优）** | **是（ν(x) 几何先验）** |

---

## 2. 对偶变分原理：从控制到标量势

### 2.1 Lemma 2.1 — Kantorovich 对偶

通过引入 Lagrange 乘子 $U(t, \mathbf{x})$ 约束 Fokker-Planck 方程，对控制变量 $\mathbf{u}$ 做逐点极小化，可以得到：

- **最优控制**：$\mathbf{u}^*(t, \mathbf{x}) = -\frac{1}{\gamma} \nabla U(t, \mathbf{x})$
- **HJB 约束**：$\frac{\partial U}{\partial t} + D\Delta U - \frac{1}{2\gamma}\|\nabla U\|^2 + \nu(\mathbf{x}) = 0$
- **对偶目标**：$\max_{U_0, U_1} \left\{ \int U(0,\mathbf{x}) p_{\text{ref}}(\mathbf{x}) d\mathbf{x} - \int U(1,\mathbf{x}) p_{\text{data}}(\mathbf{x}) d\mathbf{x} \right\}$

物理含义：**最优控制是一个标量势函数的梯度**。这将高维向量场学习降维为标量场学习，极大提高了可解释性和参数效率。

### 2.2 循环依赖困境

然而直接求解上述对偶问题存在本质困难：对偶目标中的积分需要在 $p_{\text{data}}$ 上求期望，但从 $p_{\text{ref}}$ 出发采样得到 $p_{\text{data}}$ 恰恰需要事先知道生成过程——这形成了**循环依赖**（circular dependency）。

---

## 3. 时间反转对偶：正向训练 ↔ 逆向生成

### 3.1 Theorem 2.2 — 前向-后向 HJB 对偶

这是本文的核心定理。定义正向势函数 $W(s, \mathbf{x}) := -U(1-s, \mathbf{x})$，即对逆向势函数做时间反转和取负。则：

**(1) 正向 HJB 方程**：

$$\frac{\partial W}{\partial s} - D\Delta W - \frac{1}{2\gamma}\|\nabla W\|^2 + \nu(\mathbf{x}) = 0$$

注意与逆向 HJB 的区别：扩散项 $D\Delta W$ 的符号反转了——从"逆向抛物"变为"正向抛物"。

**(2) 正向传输过程**：受控 SDE

$$d\mathbf{y}_s = \mathbf{v}^*(s, \mathbf{y}_s) \, ds + \sqrt{2D} \, d\mathbf{B}_s, \quad \mathbf{y}_0 \sim p_{\text{data}}$$

其中 $\mathbf{v}^* = -\frac{1}{\gamma}\nabla W + 2D\nabla \log q$ 将 $p_{\text{data}}$ 传输到 $p_{\text{ref}}$。

**(3) 最优性**：$\mathbf{v}^*$ 最小化正向控制代价泛函。

### 3.2 物理解读：控制场的双重分解

最优正向控制场分解为两个具有清晰物理角色的分量：

- $-\frac{1}{\gamma}\nabla W$：**目标导向分量**（value function gradient），沿累积代价下降方向驱动传输
- $2D\nabla \log q$：**密度感知修正**（score correction），确保与 Fokker-Planck 演化的一致性

关键优势：两个分量都编码在单一标量势 $W$ 中，无需独立估计 score。

### 3.3 方法论突破

时间反转对偶打破了循环依赖：

- **训练阶段**：从 $p_{\text{data}}$（已有数据）出发，沿正向扩散 $p_{\text{data}} \to p_{\text{ref}}$ 采样轨迹——这是容易模拟的
- **生成阶段**：利用学到的 $W$，从 $p_{\text{ref}}$ 出发逆转，沿 $\nabla W$ 驱动生成

![方法总览示意图](../../pdfs/2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.mineru/hybrid_auto/images/page-03-figure-01.jpg)

**Figure 1 在论文逻辑中的角色**：这是全文的方法架构图。图中清晰展示了前向-后向 HJB 对偶的完整闭环：右上角为最优传输的对偶变分形式，其 KKT 条件给出逆向 HJB（红色方框）；通过时间反转 $W(s,\mathbf{x}) := -U(1-s,\mathbf{x})$ 得到正向 HJB（粉色区域）；正向 HJB 的解可通过 Feynman-Kac 路径积分（右下方框）在非受控正向轨迹上估计；学到的 $W$ 再通过时间反转还原 $U$，驱动上方的受控生成过程。图的底部弧线是非受控的正向扩散，箭头方向标注了训练（$p_{\text{data}} \to p_{\text{ref}}$）和生成（$p_{\text{ref}} \to p_{\text{data}}$）的流向。

---

## 4. Cole-Hopf 变换与 Feynman-Kac 表示

### 4.1 非线性 → 线性：Cole-Hopf 变换

HJB 方程是非线性的（包含 $\|\nabla W\|^2$ 项）。经典的 Cole-Hopf 变换 $W = \frac{1}{\beta} \log Z$（其中 $\beta = \frac{1}{2D\gamma}$）将其线性化为：

$$\frac{\partial Z}{\partial t} = D\Delta Z - \beta\nu Z$$

这是一个带空间变化**吸收率** $\beta\nu(\mathbf{x})$ 的扩散方程。物理直觉：

- 吸收项 $\beta\nu Z$ 指数级抑制了经过高代价区域的路径贡献
- 低代价走廊中的路径贡献被放大
- 这正是路径空间上的**自由能**（free energy）结构

### 4.2 Feynman-Kac 路径积分

线性 PDE 的解有闭合的路径积分表示：

$$Z(t, \mathbf{x}) = \mathbb{E}_{\mathbb{P}_0}\left[Z(0, \mathbf{x}_0) \exp\left(-\beta \int_0^t \nu(\mathbf{x}_s) \, ds\right) \;\middle|\; \mathbf{x}_t = \mathbf{x}\right]$$

这意味着 $Z$（进而 $W$）可以通过在正向轨迹上的蒙特卡洛平均来估计——不需要逆向模拟。

### 4.3 实用参考过程：Ornstein-Uhlenbeck

纯布朗运动采样效率低。实践中用 OU 过程作为参考：

$$d\mathbf{x}_s = -\theta \mathbf{x}_s \, ds + \sqrt{2D} \, d\mathbf{B}_s, \quad \mathbf{x}_0 \sim p_{\text{data}}$$

OU 过程具有解析转移核，允许在任意时间点条件采样，无需存储完整轨迹。

### 4.4 风险敏感控制与方差控制

对值函数做 Taylor 展开揭示：

$$U(t, \mathbf{x}) = \mathbb{E}[C | \mathbf{x}_t = \mathbf{x}] - \frac{\beta}{2}\text{Var}[C | \mathbf{x}_t = \mathbf{x}] + \mathcal{O}(\beta^2)$$

其中 $C$ 是轨迹总代价。参数 $\gamma$ 通过 $\beta = 1/(2D\gamma)$ 调控这一权衡：
- 大 $\gamma$：风险中性（risk-neutral），容忍高方差轨迹
- 小 $\gamma$：风险规避（risk-averse），集中于低方差、确定性更强的路径

方差控制从随机最优控制的结构中自然涌现，无需额外正则化。

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
