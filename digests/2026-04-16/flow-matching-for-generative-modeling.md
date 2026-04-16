---
title: "Flow Matching for Generative Modeling"
authors: "Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel"
venue: "ICLR 2023"
date_read: "2026-04-16"
topics: ["flow matching", "连续正则化流", "最优传输", "生成模型"]
---

# Flow Matching for Generative Modeling

## 精读笔记

---

## 一、问题背景与动机

### 1.1 作者与论文定位

本文第一作者 **Yaron Lipman** 来自 Meta AI（FAIR）与 Weizmann Institute of Science，是计算几何与深度生成模型领域的领军人物。合作者 **Ricky T. Q. Chen** 是 Neural ODE 的提出者之一，**Heli Ben-Hamu** 和 **Maximilian Nickel** 同在 Meta AI，分别专注于流形上的概率路径匹配和图表示学习。

本文发表于 ICLR 2023，是 **Flow Matching** 范式的奠基性工作。它为训练连续正则化流（Continuous Normalizing Flows, CNFs）提供了一种**无需模拟（simulation-free）** 的高效方法，并在此框架下统一了扩散模型路径和最优传输路径，彻底改变了生成模型的训练方式。

### 1.2 核心问题：CNF 的训练瓶颈

**连续正则化流（CNF）** 是一类用神经网络参数化的时间连续向量场（vector field），通过 ODE 将简单先验分布（如标准高斯）推向复杂数据分布。CNF 的表达能力极强——理论上能建模任意概率路径——但传统训练方法面临严重瓶颈：

| 训练方法 | 核心困难 |
|---------|---------|
| 最大似然（Maximum Likelihood） | 需要昂贵的前向/反向 ODE 模拟 |
| Moser Flow (Rozen et al., 2021) | 涉及高维不可解积分 |
| 概率路径匹配 (Ben-Hamu et al., 2022) | 随机小批量下梯度有偏 |

唯一能大规模训练的方法是**扩散模型（Diffusion Models）**，但它被限制在由随机微分方程（SDE）定义的扩散概率路径上，采样路径弯曲、训练迭代次数巨大。

本文的核心提问是：**能否设计一种通用的、无需 ODE 模拟的 CNF 训练目标，使其不受扩散过程的限制，并能利用更高效的概率路径（如最优传输路径）？**

### 1.3 主要贡献

1. 提出 **Flow Matching（FM）** 目标：直接回归生成目标概率路径的向量场
2. 证明 **条件流匹配（Conditional Flow Matching, CFM）** 与 FM 在梯度上等价，使训练变得可解
3. 定义一族通用的**高斯条件概率路径**，将扩散路径纳入为特例
4. 引入**最优传输（OT）条件路径**：直线轨迹、更快训练、更高效采样
5. 在 ImageNet 上实现了 CNF 在似然和样本质量上的 SOTA 表现

---

## 二、预备知识：连续正则化流

### 2.1 核心数学对象

本文围绕两个核心对象展开：

**概率密度路径（probability density path）** $p: [0,1] \times \mathbb{R}^d \to \mathbb{R}_{>0}$，是一个随时间变化的概率密度函数，满足 $\int p_t(x) dx = 1$。

**时间依赖的向量场（time-dependent vector field）** $v: [0,1] \times \mathbb{R}^d \to \mathbb{R}^d$，定义了数据空间中每个点在每个时刻的"速度"。

### 2.2 从向量场到流

给定向量场 $v_t$，可以通过求解常微分方程（ODE）构造一个时间依赖的微分同胚映射，称为**流（flow）** $\phi: [0,1] \times \mathbb{R}^d \to \mathbb{R}^d$：

$$\frac{d}{dt} \phi_t(x) = v_t(\phi_t(x)), \quad \phi_0(x) = x$$

这个 ODE 的含义是：粒子从初始位置 $x$ 出发，在向量场 $v_t$ 的驱动下，沿轨迹 $\phi_t(x)$ 运动。$\phi_t$ 是一个可逆映射（微分同胚），将 $t=0$ 时的分布推到 $t$ 时刻的分布。

### 2.3 推前方程（Push-forward）

CNF 通过**推前方程（push-forward equation）** 将简单先验 $p_0$（如标准高斯噪声）变换为复杂分布 $p_1$：

$$p_t = [\phi_t]_* p_0$$

推前算子的定义为：

$$[\phi_t]_* p_0(x) = p_0(\phi_t^{-1}(x)) \det\left[\frac{\partial \phi_t^{-1}}{\partial x}(x)\right]$$

这就是经典的**变量替换公式（change of variables）**：新分布在点 $x$ 处的密度等于原分布在逆映射点 $\phi_t^{-1}(x)$ 处的密度，乘以 Jacobian 行列式（补偿体积变化）。

如果向量场 $v_t$ 的流 $\phi_t$ 满足上述推前方程，则称 $v_t$ **生成（generates）** 概率密度路径 $p_t$。判断向量场是否生成某概率路径的工具是**连续性方程（continuity equation）**：

$$\frac{d}{dt} p_t(x) + \text{div}(p_t(x) v_t(x)) = 0$$

这是流体力学中的质量守恒方程：概率密度的时间变化率等于概率通量的负散度。

### 2.4 CNF 的参数化

Chen et al. (2018) 提出用神经网络 $v_t(x; \theta)$ 参数化向量场，其中 $\theta$ 是可学习参数。这就得到了 CNF：一个从噪声到数据的连续时间生成模型。训练好后，从 $p_0 = \mathcal{N}(0, I)$ 采样 $x_0$，再用 ODE 求解器积分到 $t=1$，即可得到数据样本 $\phi_1(x_0)$。

---

## 三、Flow Matching 目标

### 3.1 直觉与定义

假设存在一条"目标"概率路径 $p_t(x)$，满足 $p_0 = \mathcal{N}(0, I)$（标准高斯），$p_1 \approx q$（数据分布），并且存在向量场 $u_t(x)$ 生成这条路径。**Flow Matching（FM）** 目标就是让神经网络 $v_t(x; \theta)$ 回归这个目标向量场：

$$\mathcal{L}_{\text{FM}}(\theta) = \mathbb{E}_{t, p_t(x)} \|v_t(x) - u_t(x)\|^2$$

其中 $t \sim \mathcal{U}[0,1]$，$x \sim p_t(x)$。直觉上，FM 损失让学到的向量场在每个时刻、每个空间点都尽量接近目标向量场。当损失为零时，CNF 就能精确生成 $p_t$。

### 3.2 不可解性

FM 目标虽然简洁，但**直接使用是不可解的**：我们既不知道合适的边际概率路径 $p_t$ 的解析形式，也不知道生成它的向量场 $u_t$。需要找到一种方式来构造它们。

---

## 四、从条件构造到边际：核心理论

### 4.1 条件概率路径的混合

本文的关键思路是：用**条件概率路径的混合**来构造边际概率路径。

给定一个数据样本 $x_1$，定义**条件概率路径** $p_t(x|x_1)$，满足：
- $t=0$ 时：$p_0(x|x_1) = p(x) = \mathcal{N}(x|0, I)$（所有条件路径从相同的噪声分布出发）
- $t=1$ 时：$p_1(x|x_1) = \mathcal{N}(x|x_1, \sigma^2 I)$（集中在数据点 $x_1$ 附近）

对所有数据样本 $x_1 \sim q(x_1)$ 取边际化（marginalization），得到**边际概率路径**：

$$p_t(x) = \int p_t(x|x_1) q(x_1) dx_1$$

在 $t=1$ 时，边际分布 $p_1(x) = \int p_1(x|x_1) q(x_1) dx_1 \approx q(x)$，即近似数据分布。

### 4.2 边际向量场的构造

类似地，定义**边际向量场**为条件向量场的加权平均：

$$u_t(x) = \int u_t(x|x_1) \frac{p_t(x|x_1) q(x_1)}{p_t(x)} dx_1$$

其中 $u_t(\cdot|x_1)$ 是生成条件概率路径 $p_t(\cdot|x_1)$ 的条件向量场。权重 $\frac{p_t(x|x_1) q(x_1)}{p_t(x)}$ 是后验分布 $q(x_1|x, t)$——给定当前位置 $x$ 和时间 $t$，数据点 $x_1$ 的后验概率。

**定理 1**（边际向量场生成边际概率路径）：给定条件向量场 $u_t(x|x_1)$ 生成条件概率路径 $p_t(x|x_1)$，则上述定义的边际向量场 $u_t$ 生成边际概率路径 $p_t$，即两者满足连续性方程。

证明的核心思路是验证连续性方程：

$$\frac{d}{dt} p_t(x) = \int \left(\frac{d}{dt} p_t(x|x_1)\right) q(x_1) dx_1 = -\int \text{div}(u_t(x|x_1) p_t(x|x_1)) q(x_1) dx_1$$

第二个等号利用了每个条件向量场各自满足连续性方程。交换积分和散度算子后得到 $-\text{div}(u_t(x) p_t(x))$，正是边际连续性方程。

这个定理建立了**条件→边际的桥梁**：将不可解的边际向量场分解为无穷多个简单的、仅依赖单个数据点的条件向量场。

### 4.3 条件流匹配（Conditional Flow Matching）

虽然定理 1 给出了边际向量场的形式，但由于积分不可解，我们仍然无法直接计算 FM 损失。本文的第二个关键突破是提出**条件流匹配（CFM）**目标：

$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{t, q(x_1), p_t(x|x_1)} \|v_t(x) - u_t(x|x_1)\|^2$$

与 FM 目标的区别在于：
- FM：从**边际分布** $p_t(x)$ 采样 $x$，回归**边际向量场** $u_t(x)$
- CFM：先从数据分布采 $x_1 \sim q(x_1)$，再从**条件分布** $p_t(x|x_1)$ 采 $x$，回归**条件向量场** $u_t(x|x_1)$

CFM 目标完全可解：只需能从 $p_t(x|x_1)$ 采样并计算 $u_t(x|x_1)$，这些对于简单的条件路径都是容易的。

**定理 2**（FM 与 CFM 梯度等价）：假设 $p_t(x) > 0$ 对所有 $x \in \mathbb{R}^d$ 和 $t \in [0,1]$ 成立，则 $\mathcal{L}_{\text{CFM}}$ 与 $\mathcal{L}_{\text{FM}}$ 相差一个与 $\theta$ 无关的常数。因此 $\nabla_\theta \mathcal{L}_{\text{FM}}(\theta) = \nabla_\theta \mathcal{L}_{\text{CFM}}(\theta)$。

**证明要点**：将 FM 和 CFM 损失的二次范数展开为三项：
$$\|v_t(x) - u_t(x)\|^2 = \|v_t(x)\|^2 - 2\langle v_t(x), u_t(x)\rangle + \|u_t(x)\|^2$$

关键步骤是证明两个目标中依赖 $\theta$ 的项（前两项）相等：

1. **$\|v_t\|^2$ 项**：利用 $p_t(x) = \int p_t(x|x_1)q(x_1)dx_1$ 和 Fubini 定理交换积分序，得到 $\mathbb{E}_{p_t(x)} \|v_t(x)\|^2 = \mathbb{E}_{q(x_1), p_t(x|x_1)} \|v_t(x)\|^2$。

2. **交叉项**：将边际向量场的定义代入，利用 $u_t(x) = \int u_t(x|x_1) \frac{p_t(x|x_1)q(x_1)}{p_t(x)} dx_1$，消去 $p_t(x)$ 后再次交换积分序，得到 $\mathbb{E}_{p_t(x)} \langle v_t(x), u_t(x)\rangle = \mathbb{E}_{q(x_1), p_t(x|x_1)} \langle v_t(x), u_t(x|x_1)\rangle$。

3. 第三项 $\|u_t\|^2$ 与 $\theta$ 无关，对梯度无影响。

这意味着我们可以**完全绕开边际概率路径和边际向量场**，仅通过设计简单的条件路径和条件向量场来训练 CNF。

---

## 五、高斯条件概率路径

### 5.1 一般高斯路径

本文考虑一族通用的**高斯条件概率路径**：

$$p_t(x|x_1) = \mathcal{N}(x|\mu_t(x_1), \sigma_t(x_1)^2 I)$$

其中 $\mu_t$ 是时间依赖的均值，$\sigma_t$ 是时间依赖的标准差，满足边界条件：
- $t=0$：$\mu_0(x_1) = 0$，$\sigma_0(x_1) = 1$ → $p_0(x|x_1) = \mathcal{N}(0, I)$（标准高斯）
- $t=1$：$\mu_1(x_1) = x_1$，$\sigma_1(x_1) = \sigma_{\min}$ → $p_1(x|x_1) = \mathcal{N}(x_1, \sigma_{\min}^2 I)$（集中在数据点）

### 5.2 条件流映射

对于高斯路径，存在一个自然的仿射变换将标准高斯推到 $p_t(x|x_1)$：

$$\psi_t(x) = \sigma_t(x_1) x + \mu_t(x_1)$$

当 $x \sim \mathcal{N}(0, I)$ 时，$\psi_t(x) \sim \mathcal{N}(\mu_t(x_1), \sigma_t(x_1)^2 I) = p_t(\cdot|x_1)$。即 $[\psi_t]_* p(x) = p_t(x|x_1)$。

### 5.3 条件向量场的闭式解

**定理 3**：对于高斯条件概率路径，$\psi_t$ 所定义的唯一条件向量场为：

$$u_t(x|x_1) = \frac{\sigma_t'(x_1)}{\sigma_t(x_1)}(x - \mu_t(x_1)) + \mu_t'(x_1)$$

**推导**：从 $\psi_t(x) = \sigma_t x + \mu_t$（省略对 $x_1$ 的依赖），取时间导数：

$$\frac{d}{dt}\psi_t(x) = \sigma_t' x + \mu_t'$$

根据流的定义 $\frac{d}{dt}\psi_t(x) = u_t(\psi_t(x)|x_1)$，令 $y = \psi_t(x)$，则 $x = \psi_t^{-1}(y) = \frac{y - \mu_t}{\sigma_t}$，代入得：

$$u_t(y|x_1) = \sigma_t' \cdot \frac{y - \mu_t}{\sigma_t} + \mu_t' = \frac{\sigma_t'}{\sigma_t}(y - \mu_t) + \mu_t'$$

将条件流代入 CFM 损失，并用 $x_0 \sim p(x_0) = \mathcal{N}(0, I)$ 重参数化：

$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{t, q(x_1), p(x_0)} \left\|v_t(\psi_t(x_0)) - \frac{d}{dt}\psi_t(x_0)\right\|^2$$

训练时只需：(1) 从数据中采 $x_1$，从标准高斯中采 $x_0$；(2) 计算 $\psi_t(x_0)$（插值点）和 $\frac{d}{dt}\psi_t(x_0)$（目标速度）；(3) 让网络在插值点处预测目标速度。

---

## 六、特例一：扩散条件向量场

### 6.1 方差爆炸（Variance Exploding, VE）路径

VE 扩散的反向（噪声→数据）条件概率路径为：

$$p_t(x|x_1) = \mathcal{N}(x|x_1, \sigma_{1-t}^2 I)$$

其中 $\sigma_t$ 是递增函数，$\sigma_0 = 0$，$\sigma_1 \gg 1$。对应 $\mu_t(x_1) = x_1$，$\sigma_t(x_1) = \sigma_{1-t}$。代入定理 3：

$$u_t(x|x_1) = -\frac{\sigma_{1-t}'}{\sigma_{1-t}}(x - x_1)$$

### 6.2 方差保持（Variance Preserving, VP）路径

VP 扩散的反向条件概率路径为：

$$p_t(x|x_1) = \mathcal{N}(x|\alpha_{1-t} x_1, (1 - \alpha_{1-t}^2) I)$$

其中 $\alpha_t = e^{-\frac{1}{2}T(t)}$，$T(t) = \int_0^t \beta(s) ds$。对应 $\mu_t(x_1) = \alpha_{1-t} x_1$，$\sigma_t(x_1) = \sqrt{1 - \alpha_{1-t}^2}$。代入定理 3：

$$u_t(x|x_1) = \frac{\alpha_{1-t}'}{1 - \alpha_{1-t}^2}(\alpha_{1-t} x - x_1)$$

这个条件向量场与 Song et al. (2020b) 推导的 Probability Flow ODE 完全一致（附录 D 详细验证）。

### 6.3 FM 作为扩散模型的替代训练方式

即使使用扩散路径，FM 目标也比 Score Matching 提供更稳定的训练。原因在于：

- Score Matching 的回归目标是 $\nabla \log p_t(x|x_1) = -\frac{x - \mu_t}{\sigma_t^2}$，在 $\sigma_t \to 0$ 时发散
- FM 的回归目标是 $u_t(x|x_1) = \frac{\sigma_t'}{\sigma_t}(x - \mu_t) + \mu_t'$，行为更温和

此外，扩散路径的一个技术缺陷是：在有限时间内无法精确到达纯噪声分布（$p_0$ 只是近似高斯），而 FM 框架可以直接设定 $\mu_t$ 和 $\sigma_t$ 的边界条件，完全控制路径的起止。

---

## 七、特例二：最优传输条件向量场

### 7.1 线性插值路径

一个更自然的选择是让均值和标准差随时间**线性变化**：

$$\mu_t(x_1) = t x_1, \quad \sigma_t(x_1) = 1 - (1 - \sigma_{\min})t$$

代入定理 3，得到 OT 条件向量场：

$$u_t(x|x_1) = \frac{x_1 - (1 - \sigma_{\min})x}{1 - (1 - \sigma_{\min})t}$$

对应的条件流为：

$$\psi_t(x) = (1 - (1 - \sigma_{\min})t) x + t x_1$$

CFM 损失简化为：

$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{t, q(x_1), p(x_0)} \left\|v_t(\psi_t(x_0)) - (x_1 - (1 - \sigma_{\min}) x_0)\right\|^2$$

注意回归目标 $x_1 - (1 - \sigma_{\min}) x_0$ **不依赖时间 $t$**！这使得回归任务极为简单。

### 7.2 为什么叫"最优传输"？

条件流 $\psi_t(x) = (1-t)x + t \cdot \psi(x)$（忽略 $\sigma_{\min}$ 修正项）正是两个高斯分布 $p_0(x|x_1) = \mathcal{N}(0, I)$ 和 $p_1(x|x_1) = \mathcal{N}(x_1, \sigma_{\min}^2 I)$ 之间的 **Wasserstein-2 最优传输位移映射（OT displacement map）**。McCann (1997) 定义的 OT 插值概率路径为：

$$p_t = [(1-t)\text{id} + t\psi]_* p_0$$

其中 $\psi$ 是将 $p_0$ 推到 $p_1$ 的 OT 映射。对于标准高斯到均值为 $x_1$ 的高斯，OT 位移映射恰好是上述仿射变换。

### 7.3 OT 路径 vs. 扩散路径：几何直觉

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-05-figure-10.jpg)
![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-05-figure-11.jpg)

**Figure 3**（扩散 vs. OT 轨迹）：左图为扩散路径的采样轨迹，右图为 OT 路径。扩散路径的粒子轨迹弯曲且可能"过冲（overshoot）"——先走过数据点再折返；OT 路径保证粒子沿**直线**运动且**匀速**前进。这种几何差异直接影响 ODE 求解器的效率：直线轨迹所需的函数评估次数（NFE）更少。

### 7.4 条件向量场的方向恒定性

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-05-figure-05.jpg)

**Figure 2 上半部分**（扩散条件 Score Function）：扩散路径的条件得分函数 $\nabla \log p_t(x|x_1)$ 随时间 $t$ 变化剧烈——$t=0$ 时在全空间均匀指向 $x_1$（幅度大），$t=1$ 时退化为集中在 $x_1$ 附近的尖锐梯度。蓝色表示大幅值，红色表示小幅值。

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-05-figure-09.jpg)

**Figure 2 下半部分**（OT 条件向量场）：OT 条件向量场 $u_t(x|x_1)$ 的**方向在时间上恒定**，仅幅值变化。数学上，向量场可分解为 $u_t(x|x_1) = g(t) h(x|x_1)$，时间和空间因子分离。这使得神经网络的回归任务更简单——网络不需要学习复杂的时间依赖的方向变化。

### 7.5 关于边际向量场的说明

需要强调的是：**条件流是最优传输，但边际向量场并不一定是最优传输解**。将无数个条件 OT 映射的边际化结果并不等价于整体 OT 问题的解。尽管如此，由于每个条件流都是直线，边际向量场仍然保持相对简单的结构。

---

## 八、实验验证

### 8.1 2D 直觉实验

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-06-figure-01.jpg)

**Figure 4**（2D 棋盘格实验）：(左) 不同目标训练的 CNF 的粒子轨迹。OT 路径在更早的时间点就出现了棋盘格模式，而 FM 比 Score Matching 训练更稳定。(右) FM-OT 的低成本采样效率更高——用 midpoint 方案只需很少的步数即可生成高质量样本。

### 8.2 ImageNet 密度建模与样本质量

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-07-table-01.jpg)

**Table 1**（定量比较）：使用相同的 U-Net 架构（来自 Dhariwal & Nichol, 2021）和相同超参数，在 CIFAR-10 和 ImageNet 32/64/128 上比较不同训练方法。FM-OT 在所有数据集上的 NLL（似然）、FID（样本质量）和 NFE（采样效率）三项指标上一致优于 DDPM、Score Matching 和 ScoreFlow。

关键数据点（ImageNet 64×64）：

| 方法 | NLL (BPD)↓ | FID↓ | NFE↓ |
|-----|-----------|------|------|
| DDPM | 3.32 | 17.36 | 264 |
| Score Matching | 3.40 | 19.74 | 441 |
| FM w/ Diffusion | 3.33 | 16.88 | 187 |
| **FM w/ OT** | **3.31** | **14.45** | **138** |

FM-OT 的 NFE（138）仅为 DDPM（264）的 52%，且 FID 降低了 17%。

### 8.3 采样路径可视化

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-07-figure-01.jpg)
![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-07-figure-02.jpg)
![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-07-figure-03.jpg)

**Figure 6**（ImageNet 64×64 采样路径）：从相同的初始噪声出发，三种模型的采样路径对比。上：Score Matching w/ Diffusion；中：Flow Matching w/ Diffusion；下：Flow Matching w/ OT。OT 路径的噪声大致线性消除——图像结构在中间时间点就清晰可见；扩散路径则到最后阶段才显现图像。

### 8.4 训练速度

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-07-figure-04.jpg)

**Figure 5**（训练过程中的 FID 曲线，ImageNet 64×64）：FM-OT 的 FID 下降最快且最终值最低。对比训练总量：Dhariwal & Nichol (2021) 在 ImageNet-128 上用 4.36M 迭代（batch size 256），FM 仅用 500K 迭代（batch size 1.5K），图像吞吐量减少 33%。

### 8.5 采样效率

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-08-figure-01.jpg)

**Figure 7 左**（ODE 数值误差 vs. NFE，ImageNet 32×32）：使用固定步长求解器，FM-OT 只需约 60% 的函数评估次数就能达到与扩散模型相同的数值精度。

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-08-figure-02.jpg)
![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-08-figure-03.jpg)
![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-08-figure-04.jpg)

**Figure 7 右**（FID vs. NFE）：FM-OT 在极低 NFE 下仍能保持可接受的 FID，在样本质量与计算成本之间提供了最优的权衡。

### 8.6 条件图像生成

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/page-08-table-01.jpg)

**Table 2**（图像超分辨率，64×64→256×256）：FM-OT 在 FID（3.4）和 IS（200.8）上大幅优于 SR3（5.2 / 180.1），PSNR 和 SSIM 略低但 FID/IS 是更好的生成质量指标。

### 8.7 ImageNet 生成样本

![](../../pdfs/2026-04-16/flow-matching-for-generative-modeling.mineru/hybrid_auto/images/c428b8f1466a4a1d46bd2c295be04dad93e8e9f74296f6afe88ec8ed17827c91.jpg)

**Figure 1**（非条件 ImageNet-128 样本）：FM-OT 训练的 CNF 生成的无条件 ImageNet 128×128 样本。图像多样性高，纹理和结构细节清晰，展示了 FM 框架在大规模图像生成任务上的能力。

---

## 九、与扩散模型的深层关系

### 9.1 Score Matching 是 FM 的特例

扩散模型通过 denoising score matching 训练得分函数 $s_t(x) \approx \nabla \log p_t(x)$，然后用 Probability Flow ODE 采样：

$$u_t(x) = f_t - \frac{g_t^2}{2} \nabla \log p_t$$

其中 $f_t$ 是漂移，$g_t$ 是扩散系数。本文附录 D 证明，当 FM 使用 VP/VE 扩散路径时，条件向量场 $u_t(x|x_1)$ 恰好等于 Probability Flow ODE 的条件向量场。因此**扩散模型的 Score Matching 训练可被视为 Flow Matching 的一个特例**。

### 9.2 FM 的概念优势

FM 框架的核心优势在于**直接与概率路径和向量场打交道**，绕开了随机微分方程的构造：

- 不需要推导前向/反向 SDE
- 不需要选择噪声调度函数 $\beta(t)$ 来隐式定义概率路径
- 可以自由设计任意 $\mu_t$ 和 $\sigma_t$，甚至非高斯路径
- 天然支持有限时间构造（$t \in [0,1]$），无需截断近似

---

## 十、并行工作与后续影响

本文与 **Rectified Flow**（Liu et al., 2022）和 **Stochastic Interpolants**（Albergo & Vanden-Eijnden, 2022）几乎同时独立提出了类似的条件目标。三者共同开创了基于 flow matching 的生成模型训练范式。

FM 框架的后续影响极为深远：Stable Diffusion 3、FLUX、Meta 的 Movie Gen 等工业级模型均采用了 Flow Matching 训练。该框架还被扩展到流形上的生成（Riemannian Flow Matching）、蛋白质设计（FrameFlow）、语音合成（Voicebox）等领域。

---

## 十一、总结与个人评价

### 核心贡献的三层递进

1. **技术层**：FM/CFM 目标提供了无需 ODE 模拟、无偏梯度的 CNF 训练方法
2. **概念层**：将扩散模型从"SDE 的附属品"解放出来，直接在概率路径空间中设计生成过程
3. **实用层**：OT 路径的直线轨迹带来训练加速（~2×）和采样加速（NFE 降低 40-50%）

### 局限与开放问题

- 条件 OT ≠ 边际 OT：边际向量场不保证是全局最优传输解
- 高斯路径的限制：非各向同性高斯或非高斯核的扩展仍有待探索
- 似然计算仍需 ODE：虽然训练无需模拟，但精确的 $\log p_1(x)$ 计算仍依赖反向 ODE 积分

### 进一步阅读建议

- **Rectified Flow** (Liu et al., 2022)：从 rectified flow 角度理解 OT 路径的"拉直"效应
- **Stochastic Interpolants** (Albergo & Vanden-Eijnden, 2022)：更数学化的统一框架
- **Minibatch OT** (Tong et al., 2024)：通过小批量 OT 耦合改善边际向量场
- **Flow Matching on Manifolds** (Chen & Lipman, 2024)：扩展到黎曼流形
