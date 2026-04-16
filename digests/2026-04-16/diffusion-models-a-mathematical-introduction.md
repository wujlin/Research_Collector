---
title: "Diffusion Models: A Mathematical Introduction"
authors: "Sepehr Maleki, Negar Pourmoazemi"
venue: "arXiv (2025)"
date_read: "2026-04-16"
topics: ["扩散模型", "SDE", "Fokker-Planck", "score matching", "DDPM"]
---

# Diffusion Models: A Mathematical Introduction

## 精读笔记

---

## 一、定位与全局结构

### 1.1 本文定位

这是一篇面向研究者和学生的**数学导论型综述**，从高斯分布基本性质出发，以统一的记号和完整的中间步骤，从第一原理推导扩散模型的全部核心组件。与很多偏实践的教程不同，本文的重点在于**透明的代数推导**——每一个"为什么"都有显式的公式支撑。

### 1.2 全局线索

本文的逻辑链条可概括为：

$$
\text{高斯基础} \xrightarrow{\text{构造}} \text{前向扩散} \xrightarrow{\text{Bayes}} \text{真后验} \xrightarrow{\text{ELBO}} \text{训练目标} \xrightarrow{\text{加速}} \text{DDIM / 潜空间} \xrightarrow{\text{连续}} \text{概率流ODE} \xrightarrow{\text{统一}} \text{Flow Matching} \xrightarrow{\text{控制}} \text{引导生成}
$$

### 1.3 核心记号

| 符号 | 含义 |
|------|------|
| $\alpha_t := 1 - \beta_t$ | 前向保信号比例 |
| $\bar{\alpha}_t := \prod_{i=1}^{t} \alpha_i$ | 累积信号保留率 |
| $\mathrm{SNR}_t := \bar{\alpha}_t / (1 - \bar{\alpha}_t)$ | 信噪比 |
| $\tilde{\beta}_t := \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t$ | 真后验方差 |
| $\hat{\epsilon}_\theta(\mathbf{x}_t, t)$ | 噪声预测网络 |
| $s_t(\mathbf{x}) := \nabla_{\mathbf{x}} \log p_t(\mathbf{x})$ | score function |

---

## 二、高斯预备知识

本文的推导策略是：**先固定高斯的五个核心工具，后面所有推导不过是反复调用**。

### 2.1 各向同性高斯密度

![各向同性高斯密度公式](../../pdfs/2026-04-16/diffusion-models-a-mathematical-introduction.mineru/hybrid_auto/images/page-06-equation-04.jpg)

$$
p(\mathbf{x}) = \frac{1}{(2\pi\sigma^2)^{d/2}} \exp\left(-\frac{1}{2\sigma^2}\|\mathbf{x} - \boldsymbol{\mu}\|_2^2\right)
$$

当协方差 $\boldsymbol{\Sigma} = \sigma^2 \mathbf{I}$ 时，Mahalanobis 距离退化为欧氏距离的 $1/\sigma^2$ 倍。这个化简是后续所有"高斯配方"的起点。

### 2.2 二次型期望（Trace Trick）

**Proposition 2.4** 给出核心恒等式：若 $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}_p, \boldsymbol{\Sigma}_p)$，则

$$
\mathbb{E}_p\left[(\mathbf{x} - \boldsymbol{\mu}_p)^\top \mathbf{A} (\mathbf{x} - \boldsymbol{\mu}_p)\right] = \mathrm{tr}(\mathbf{A}\boldsymbol{\Sigma}_p)
$$

**证明思路**：令 $\mathbf{z} := \mathbf{x} - \boldsymbol{\mu}_p$，利用 trace trick $\mathbf{v}^\top \mathbf{A} \mathbf{u} = \mathrm{tr}(\mathbf{A}\mathbf{u}\mathbf{v}^\top)$，将标量二次型提升为矩阵迹，再交换期望和迹运算，得到 $\mathrm{tr}(\mathbf{A}\mathbb{E}[\mathbf{z}\mathbf{z}^\top]) = \mathrm{tr}(\mathbf{A}\boldsymbol{\Sigma}_p)$。

这个恒等式将在 KL 散度推导和 ELBO 分解中反复出现。

### 2.3 重参数化

**核心命题**：若 $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_d)$，则 $\mathbf{x} = \boldsymbol{\mu} + \mathbf{A}\mathbf{z} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{A}\mathbf{A}^\top)$。

各向同性特例 $\mathbf{A} = \sigma\mathbf{I}$ 给出：$\mathbf{x} = \boldsymbol{\mu} + \sigma\mathbf{z} \sim \mathcal{N}(\boldsymbol{\mu}, \sigma^2\mathbf{I}_d)$。

这是扩散模型中"从 $\mathbf{x}_0$ 一步跳到 $\mathbf{x}_t$"的数学基础——前向过程的闭式采样完全依赖于此。

### 2.4 两个高斯的乘积

**Proposition 2.11**：两个高斯密度的逐点乘积仍（正比于）高斯，参数为

$$
\boldsymbol{\Sigma} = (\boldsymbol{\Sigma}_p^{-1} + \boldsymbol{\Sigma}_q^{-1})^{-1}, \qquad \boldsymbol{\mu} = \boldsymbol{\Sigma}(\boldsymbol{\Sigma}_p^{-1}\boldsymbol{\mu}_p + \boldsymbol{\Sigma}_q^{-1}\boldsymbol{\mu}_q)
$$

**证明思路**：将两个高斯写成自然参数（精度矩阵）形式，合并指数中的二次项和线性项，通过 completing the square（Lemma 2.10）识别出新的高斯参数。

物理直觉：**精度相加，均值取精度加权平均**。这正是 Bayesian 融合两个信息源的标准操作——DDPM 后验推导的关键。

### 2.5 高斯 KL 散度

**Proposition 2.13**：

![KL散度闭式表达](../../pdfs/2026-04-16/diffusion-models-a-mathematical-introduction.mineru/hybrid_auto/images/page-12-equation-01.jpg)

$$
\mathrm{KL}(P \| Q) = \frac{1}{2}\left[\mathrm{tr}(\boldsymbol{\Sigma}_Q^{-1}\boldsymbol{\Sigma}_P) + (\boldsymbol{\mu}_Q - \boldsymbol{\mu}_P)^\top\boldsymbol{\Sigma}_Q^{-1}(\boldsymbol{\mu}_Q - \boldsymbol{\mu}_P) - d + \log\frac{\det(\boldsymbol{\Sigma}_Q)}{\det(\boldsymbol{\Sigma}_P)}\right]
$$

**证明**分三步：

1. 写出 $\log p(\mathbf{x}) - \log q(\mathbf{x})$，$(2\pi)^{d/2}$ 项消去
2. 对第一个二次型取期望，用 trace trick 得 $\mathrm{tr}(\boldsymbol{\Sigma}_P^{-1}\boldsymbol{\Sigma}_P) = d$
3. 对第二个二次型，展开 $\mathbf{x} - \boldsymbol{\mu}_Q = (\mathbf{x} - \boldsymbol{\mu}_P) + (\boldsymbol{\mu}_P - \boldsymbol{\mu}_Q)$，交叉项因 $\mathbb{E}[\mathbf{x} - \boldsymbol{\mu}_P] = \mathbf{0}$ 消失

**各向同性等方差**的特殊情况进一步简化为纯均值差的 $\ell_2$ 损失：$\mathrm{KL}(P\|Q) = \frac{1}{2\sigma^2}\|\boldsymbol{\mu}_P - \boldsymbol{\mu}_Q\|_2^2$。DDPM 的噪声预测目标正是从这个特殊情况推出的。

---

## 三、前向扩散过程

### 3.1 单步转移

前向过程定义为 Markov 链：

$$
q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) = \mathcal{N}\left(\mathbf{x}_t; \sqrt{\alpha_t}\,\mathbf{x}_{t-1},\; \beta_t\mathbf{I}\right)
$$

其中 $\beta_t \in (0,1)$ 按递增调度 $\beta_1 < \beta_2 < \cdots < \beta_T$，$\alpha_t := 1 - \beta_t$。

设计意图：每一步将信号缩小 $\sqrt{\alpha_t}$ 倍，同时注入方差 $\beta_t$ 的噪声。当 $T$ 足够大时，$\bar{\alpha}_T \to 0$，终态趋近标准高斯。

### 3.2 闭式边缘分布（跳步公式）

**核心推导**：利用重参数化，$\mathbf{x}_t = \sqrt{\alpha_t}\mathbf{x}_{t-1} + \sqrt{1-\alpha_t}\boldsymbol{\epsilon}$，逐步递归代入：

$$
\mathbf{x}_t = \sqrt{\alpha_t\alpha_{t-1}}\,\mathbf{x}_{t-2} + \underbrace{\sqrt{\alpha_t(1-\alpha_{t-1})}\boldsymbol{\epsilon} + \sqrt{1-\alpha_t}\boldsymbol{\epsilon}}_{\text{两个独立高斯之和}}
$$

两个独立高斯的和仍为高斯，方差相加：$\alpha_t(1-\alpha_{t-1}) + (1-\alpha_t) = 1 - \alpha_t\alpha_{t-1}$。

![前向过程归纳法](../../pdfs/2026-04-16/diffusion-models-a-mathematical-introduction.mineru/hybrid_auto/images/page-15-equation-02.jpg)

由归纳法得到闭式结果：

$$
q(\mathbf{x}_t \mid \mathbf{x}_0) = \mathcal{N}\left(\sqrt{\bar{\alpha}_t}\,\mathbf{x}_0,\; (1-\bar{\alpha}_t)\mathbf{I}\right), \qquad \mathbf{x}_t = \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon}
$$

这意味着**不需要逐步执行 $T$ 步前向过程**，只需一次采样即可从 $\mathbf{x}_0$ 生成任意时刻的含噪样本——这是训练效率的关键。

---

## 四、反向过程与 DDPM 后验

### 4.1 真后验的推导

生成的核心问题：给定 $\mathbf{x}_t$，如何回到 $\mathbf{x}_{t-1}$？由 Bayes 定理：

$$
q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0) = \frac{q(\mathbf{x}_t \mid \mathbf{x}_{t-1})\, q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}{q(\mathbf{x}_t \mid \mathbf{x}_0)}
$$

三个因子都是已知的高斯。将其写成指数形式，关键步骤是**收集关于 $\mathbf{x}_{t-1}$ 的二次项和线性项**：

![后验推导——配方](../../pdfs/2026-04-16/diffusion-models-a-mathematical-introduction.mineru/hybrid_auto/images/page-17-equation-05.jpg)

定义精度 $A := \frac{\alpha_t}{\beta_t} + \frac{1}{1-\bar{\alpha}_{t-1}}$ 和线性项 $\mathbf{b} := \frac{\sqrt{\alpha_t}}{\beta_t}\mathbf{x}_t + \frac{\sqrt{\bar{\alpha}_{t-1}}}{1-\bar{\alpha}_{t-1}}\mathbf{x}_0$，完成配方后得到：

**后验均值**（$\mathbf{x}_0$-形式）：

$$
\hat{\boldsymbol{\mu}}(\mathbf{x}_t, \mathbf{x}_0) = \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}\,\mathbf{x}_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\,\beta_t}{1-\bar{\alpha}_t}\,\mathbf{x}_0
$$

**后验方差**：

$$
\tilde{\beta}_t := A^{-1} = \frac{\beta_t(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}
$$

化简关键：利用 $\bar{\alpha}_t = \alpha_t\bar{\alpha}_{t-1}$ 得到 $1 - \bar{\alpha}_t = (1-\bar{\alpha}_{t-1}) + \bar{\alpha}_{t-1}\beta_t$，分母的通分使得 $A^{-1}$ 整洁地表达为 $\tilde{\beta}_t$。

### 4.2 ε-形式的后验均值

利用前向闭式 $\mathbf{x}_0 = \frac{1}{\sqrt{\bar{\alpha}_t}}(\mathbf{x}_t - \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon})$ 代入后验均值：

$$
\hat{\boldsymbol{\mu}}(\mathbf{x}_t, \mathbf{x}_0) = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\boldsymbol{\epsilon}\right)
$$

这个形式直接暗示了实践中的参数化方案：用神经网络预测噪声 $\hat{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_t, t)$，然后代入上式作为逆过程的均值。

---

## 五、变分目标与噪声预测损失

### 5.1 ELBO 推导

目标：最大化 $\log p_\theta(\mathbf{x}_0)$（等价于最小化 $\mathrm{KL}(q(\mathbf{x}_0)\|p_\theta(\mathbf{x}_0))$）。

由于 $\log p_\theta(\mathbf{x}_0)$ 不可计算，引入前向过程 $q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)$ 作为变分分布，得到变分上界（VB）：

$$
-\log p_\theta(\mathbf{x}_0) \leq \mathbb{E}_{q(\mathbf{x}_{0:T})}\log\frac{q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)}{p_\theta(\mathbf{x}_{0:T})}
$$

展开后经三步关键化简：

1. **Markov 分解**：将 $q$ 和 $p_\theta$ 都写成单步条件概率的乘积
2. **Bayes 翻转**：将 $q(\mathbf{x}_t \mid \mathbf{x}_{t-1})$ 改写为 $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0) \cdot q(\mathbf{x}_t \mid \mathbf{x}_0) / q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)$
3. **伸缩和消项**：$\sum_{t=2}^{T} \log\frac{q(\mathbf{x}_t \mid \mathbf{x}_0)}{q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}$ 伸缩为 $\log\frac{q(\mathbf{x}_T \mid \mathbf{x}_0)}{q(\mathbf{x}_1 \mid \mathbf{x}_0)}$

最终结果分为三项：

| 项 | 含义 | 处理 |
|----|------|------|
| $\mathrm{KL}(q(\mathbf{x}_T\mid\mathbf{x}_0) \| p_\theta(\mathbf{x}_T))$ | 终态匹配 | 当 $T$ 大时近似 $0$ |
| $-\mathbb{E}\log p_\theta(\mathbf{x}_0\mid\mathbf{x}_1)$ | 解码项 | 实践中常忽略 |
| $\sum_{t=2}^{T}\mathrm{KL}\{q(\mathbf{x}_{t-1}\mid\mathbf{x}_t,\mathbf{x}_0) \| p_\theta(\mathbf{x}_{t-1}\mid\mathbf{x}_t)\}$ | **核心训练项** | 两个高斯之间的 KL |

### 5.2 化简为噪声预测目标

对核心训练项，令 $\sigma_t^2 = \tilde{\beta}_t$（方差匹配），则两个等方差各向同性高斯的 KL 退化为均值差的 $\ell_2$ 范数：

$$
\mathrm{KL}\{q(\mathbf{x}_{t-1}\mid\mathbf{x}_t,\mathbf{x}_0) \| p_\theta(\mathbf{x}_{t-1}\mid\mathbf{x}_t)\} = \frac{1}{2\tilde{\beta}_t}\left\|\hat{\boldsymbol{\mu}}_t^{\mathrm{true}} - \boldsymbol{\mu}_\theta(\mathbf{x}_t, t)\right\|_2^2
$$

将 ε-参数化代入（真后验均值和学习均值都用 $\frac{1}{\sqrt{\alpha_t}}(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\cdot)$ 的形式），均值差中 $\mathbf{x}_t$ 相消，得到：

$$
\mathrm{VB} = \sum_{t=2}^{T} \frac{\beta_t}{2(1-\beta_t)(1-\bar{\alpha}_{t-1})} \left\|\boldsymbol{\epsilon}_t - \hat{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_t, t)\right\|_2^2
$$

实践中丢弃时间依赖的权重因子（Ho et al., 2020），得到简化损失：

$$
\mathcal{L}_{\text{simple}} = \mathbb{E}_{t,\mathbf{x}_0,\boldsymbol{\epsilon}}\left[\|\boldsymbol{\epsilon} - \hat{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_t, t)\|_2^2\right], \qquad \mathbf{x}_t = \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon}
$$

---

## 六、DDIM 与加速采样

### 6.1 DDIM 的核心思想

DDPM 采样需要 $T$ 步（通常 1000 步），非常慢。DDIM 的关键洞察：**不需要保持前向联合分布，只需保持边缘分布 $q(\mathbf{x}_t \mid \mathbf{x}_0)$ 不变**。

DDIM 定义了一族新的逆向条件分布，含一个自由参数 $\sigma_t^2$：

$$
q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0) = \mathcal{N}\left(\sqrt{\bar{\alpha}_{t-1}}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_{t-1}-\sigma_t^2}\cdot\frac{\mathbf{x}_t - \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0}{\sqrt{1-\bar{\alpha}_t}},\; \sigma_t^2\mathbf{I}\right)
$$

**Proposition 4.1** 证明：对任意 $\sigma_t^2 \in [0, 1-\bar{\alpha}_{t-1}]$，这族逆向条件分布保持正确的边缘分布。

**证明方法**：反向归纳。基础情况 $t=T$ 已给定。归纳步：对 $q(\mathbf{x}_{t-1}\mid\mathbf{x}_0) = \int q(\mathbf{x}_{t-1}\mid\mathbf{x}_t,\mathbf{x}_0)q(\mathbf{x}_t\mid\mathbf{x}_0)\,d\mathbf{x}_t$，用全期望和全方差定律：

- 均值：$\mathbb{E}[\mathbf{x}_{t-1}\mid\mathbf{x}_0] = \sqrt{\bar{\alpha}_{t-1}}\,\mathbf{x}_0$（噪声项期望为零）
- 方差：$\sigma_t^2\mathbf{I} + (1-\bar{\alpha}_{t-1}-\sigma_t^2)\mathbf{I} = (1-\bar{\alpha}_{t-1})\mathbf{I}$

$\sigma_t^2$ **恰好消去**！这是 DDIM 自由度成立的数学原因。

### 6.2 两个极端

| 选择 | 效果 | 名称 |
|------|------|------|
| $\sigma_t^2 = \tilde{\beta}_t$ | 恢复 DDPM 随机采样 | DDPM |
| $\sigma_t^2 = 0$ | 纯确定性采样 | DDIM ($\eta=0$) |

确定性情况下，更新规则退化为：

$$
\mathbf{x}_{t-1} = \sqrt{\bar{\alpha}_{t-1}}\,\hat{\mathbf{x}}_0(\mathbf{x}_t, t) + \sqrt{1-\bar{\alpha}_{t-1}}\,\hat{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_t, t)
$$

此时可以在**任意子网格** $\{\tau_k\}$ 上执行采样，通常只需 10–50 步。

### 6.3 DDGAN：对抗式加速

思路不同：不用 KL 散度匹配逆向转移，而是用判别器区分真实对 $(\mathbf{x}_{t-1}, \mathbf{x}_t) \sim q_t^{\mathrm{pair}}$ 与生成对 $(\hat{\mathbf{x}}_{t-1}, \mathbf{x}_t)$。

**Proposition 4.3** 证明：在最优判别器 $D_t^* = \frac{q_t^{\mathrm{pair}}}{q_t^{\mathrm{pair}} + p_t^\theta}$ 下，生成器目标可写为 Jensen-Shannon 散度，其全局最小值恰在 $p_t^\theta = q_t^{\mathrm{pair}}$ 时取到。

### 6.4 潜空间扩散（Stable Diffusion）

核心：用预训练的编码器-解码器对 $(E, D)$ 将数据映射到低维潜空间，在潜空间中执行扩散。

$$
\mathbf{z}_0 := E(\mathbf{x}_0), \qquad \hat{\mathbf{x}}_0 = D(\hat{\mathbf{z}}_0)
$$

所有数学结构——前向闭式边缘、真后验、逆过程参数化——在 $\mathbf{x} \mapsto \mathbf{z}$ 替换后完全保持。潜空间维度 $d = hwc \ll HWC$ 带来大幅加速，且不改变底层数学。

---

## 七、连续时间视角：SDE、Fokker-Planck 与概率流 ODE

这是本文将离散扩散模型与连续分析工具对接的关键章节。

### 7.1 连续前向 SDE

DDPM 的连续时间极限是方差保持（VP）SDE：

$$
d\mathbf{X}_t = -\frac{1}{2}\beta(t)\mathbf{X}_t\,dt + \sqrt{\beta(t)}\,d\mathbf{W}_t
$$

其中 $\mathbf{f}(\mathbf{x},t) = -\frac{1}{2}\beta(t)\mathbf{x}$（线性漂移），$g(t) = \sqrt{\beta(t)}$（扩散系数）。

### 7.2 连续性方程（Liouville 方程）

**Definition 5.1**：若密度族 $\{p_t\}$ 与速度场 $\mathbf{v}$ 满足

$$
\partial_t p_t = -\nabla_{\mathbf{x}} \cdot (p_t\,\mathbf{v})
$$

则称 $(p_t, \mathbf{v})$ 满足连续性方程——这是概率守恒的表述。

**Lemma 5.2**（Liouville 输运）：ODE $\dot{\mathbf{X}}_t = \mathbf{v}(\mathbf{X}_t, t)$ 的解的分布满足上述连续性方程。

**证明**：对光滑测试函数 $\varphi$，链式法则给出 $\frac{d}{dt}\varphi(\mathbf{X}_t) = \nabla\varphi^\top \mathbf{v}$。取期望、对 $\mathbf{x}$ 分部积分，将梯度从 $\varphi$ 转移到 $p_t\mathbf{v}$ 上，由测试函数的任意性得到 PDE。

### 7.3 Fokker-Planck 方程

**Lemma 5.3**：SDE $d\mathbf{X}_t = \mathbf{f}\,dt + g(t)\,d\mathbf{W}_t$ 的密度满足

$$
\partial_t p_t = -\nabla \cdot (\mathbf{f}\,p_t) + \frac{g(t)^2}{2}\Delta p_t
$$

**证明**：对 Itô 公式应用于 $\varphi(\mathbf{X}_t)$，得到

$$
d\varphi = \nabla\varphi^\top\mathbf{f}\,dt + \frac{g^2}{2}\mathrm{Tr}(\nabla^2\varphi)\,dt + \nabla\varphi^\top g\,d\mathbf{W}_t
$$

取期望消去鞅项，然后对两个积分项分别分部积分，将微分算子从 $\varphi$ 转移到 $p_t$。

### 7.4 概率流 ODE（Theorem 5.4）

这是全文最重要的定理之一。

**定义速度场**：

$$
\mathbf{v}(\mathbf{x}, t) := \mathbf{f}(\mathbf{x}, t) - \frac{g(t)^2}{2}\nabla_{\mathbf{x}}\log p_t(\mathbf{x})
$$

**结论**：ODE $\dot{\mathbf{Y}}_t = \mathbf{v}(\mathbf{Y}_t, t)$ 与原始 SDE 具有**相同的时间边缘分布** $p_t$。

**证明核心**：利用恒等式 $\Delta p_t = \nabla \cdot (p_t \nabla \log p_t)$，将 Fokker-Planck 中的扩散项（二阶 Laplacian）改写为保守输运项：

$$
\partial_t p_t = -\nabla \cdot \left(\mathbf{f}\,p_t - \frac{g^2}{2}p_t\nabla\log p_t\right) = -\nabla \cdot (p_t\,\mathbf{v})
$$

这恰好是以 $\mathbf{v}$ 为速度的连续性方程。由 Lemma 5.2，ODE 的边缘分布满足相同方程和初始条件，因此边缘分布一致。

**VP 特化**：代入 $\mathbf{f} = -\frac{1}{2}\beta(t)\mathbf{x}$，$g^2 = \beta(t)$，得到

$$
\dot{\mathbf{x}} = -\frac{\beta(t)}{2}\left(\mathbf{x} + \nabla_{\mathbf{x}}\log p_t(\mathbf{x})\right)
$$

用学习到的 score 近似 $\nabla\log p_t \approx -\hat{\boldsymbol{\epsilon}}_\theta/\sqrt{1-\bar{\alpha}_t}$，就得到 DDIM 的概率流 ODE。

---

## 八、Flow Matching

### 8.1 从 SDE 到 ODE 的范式转换

Flow matching 的核心思想：既然概率流 ODE 已经能产生正确的边缘分布，不如**直接学习速度场**，完全绕过随机过程。

### 8.2 随机插值与目标速度

**Definition 5.6**：给定端点 $\mathbf{X}_0 \sim p_0$、$\mathbf{X}_T \sim p_T$ 和耦合 $\pi$，定义随机插值

$$
\mathbf{X}_t := \psi_t(\mathbf{X}_0, \mathbf{X}_T)
$$

满足 $\psi_0 = \mathbf{X}_0$, $\psi_T = \mathbf{X}_T$。

**边缘目标速度**（Definition 5.7）：

$$
\mathbf{u}_t(\mathbf{x}) := \mathbb{E}\left[\dot{\psi}_t(\mathbf{X}_0, \mathbf{X}_T) \mid \mathbf{X}_t = \mathbf{x}\right]
$$

**Proposition 5.8** 证明 $p_t$ 满足以 $\mathbf{u}_t$ 为速度的连续性方程——因此 ODE $\dot{\mathbf{Y}}_t = \mathbf{u}_t(\mathbf{Y}_t)$ 精确传输 $p_t$。

### 8.3 CFM 与 MFM 的等价性

两种训练目标：

| 目标 | 公式 | 特点 |
|------|------|------|
| **CFM**（条件） | $\mathcal{L}_{\mathrm{CFM}} = \mathbb{E}\|\mathbf{v}_\theta(\mathbf{Z}_t, t) - \dot{\psi}_t(\mathbf{X}_0, \mathbf{X}_T)\|_2^2$ | 不需要知道 $\mathbf{u}_t$ |
| **MFM**（边缘） | $\mathcal{L}_{\mathrm{MFM}} = \mathbb{E}\|\mathbf{v}_\theta(\mathbf{X}_t, t) - \mathbf{u}_t(\mathbf{X}_t)\|_2^2$ | 需要 $\mathbf{u}_t$ 的解析形式 |

**Theorem 5.9**：二者共享同一组全局最小点，且最优预测器为 $\mathbf{v}^*(\mathbf{x},t) = \mathbf{u}_t(\mathbf{x}) = \mathbb{E}[\mathbf{U}_t \mid \mathbf{Z}_t = \mathbf{x}]$。

**证明**：由 $L^2$ 正交原理 + 全方差公式，$\mathcal{L}_{\mathrm{CFM}} = \mathcal{L}_{\mathrm{MFM}} + C$，常数 $C$ 与 $\theta$ 无关。

实践中 CFM 更具吸引力——$\dot{\psi}_t$ 可以直接从采样的端点计算，而不需要处理边缘速度中难以处理的后验 $\pi(\mathbf{x}_0, \mathbf{x}_T \mid \mathbf{X}_t = \mathbf{x})$。

![CFM vs MFM 示意](../../pdfs/2026-04-16/diffusion-models-a-mathematical-introduction.mineru/hybrid_auto/images/page-37-figure-01.jpg)

### 8.4 直线插值与整流流

最简单也最常用的选择：**直线路径** $\psi_t = (1-\rho(t))\mathbf{X}_0 + \rho(t)\mathbf{Z}$。

此时 CFM 目标为 $\dot{\rho}(t)(\mathbf{Z} - \mathbf{X}_0)$。

**Proposition 5.11**（直线边缘速度）：利用 Tweedie 恒等式，

$$
\mathbf{u}_t(\mathbf{x}) = -\frac{\dot{\rho}(t)}{1-\rho(t)}\left(\mathbf{x} + \rho(t)\nabla_{\mathbf{x}}\log p_t(\mathbf{x})\right)
$$

**Tweedie 恒等式**（Lemma 5.10）是推导中的关键引理：若 $\mathbf{Y} = \mathbf{U} + \sigma\mathbf{Z}$，则

$$
\mathbb{E}[\mathbf{U} \mid \mathbf{Y} = \mathbf{y}] = \mathbf{y} + \sigma^2\nabla_{\mathbf{y}}\log p_{\mathbf{Y}}(\mathbf{y})
$$

这与 score function 直接挂钩：score 编码了对"去噪后信号"的最优估计。

**整流（Rectification）**：速度场中的标量因子 $\kappa(t) = \dot{\rho}/(1-\rho)$ 在 $\rho \to 1$ 时会发散。**Lemma 5.12** 证明：用正函数 $\kappa(t)$ 乘以速度场不改变状态空间轨迹，只改变参数化速度。因此可以定义整流速度：

$$
\widetilde{\mathbf{u}}_t(\mathbf{x}) = -\left(\mathbf{x} + \rho(t)\nabla_{\mathbf{x}}\log p_t(\mathbf{x})\right) = -\left(\mathbf{x} - \boldsymbol{\epsilon}^*(\mathbf{x},t)\right)
$$

### 8.5 DDIM 就是整流流

**Theorem 5.16** 建立了精确联系：DDIM 的确定性更新

$$
\mathbf{x}_{\tau_{k-1}} = \sqrt{\bar{\alpha}_{\tau_{k-1}}}\,\hat{\mathbf{x}}_0(\mathbf{x}_{\tau_k}, \tau_k) + \sqrt{1-\bar{\alpha}_{\tau_{k-1}}}\,\hat{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_{\tau_k}, \tau_k)
$$

正是整流 ODE $\frac{d}{ds}\mathbf{x} = -(\mathbf{x} - \hat{\epsilon}_\theta)$ 沿直线特征线的**精确单步积分**。

物理图像：DDIM 不是在"近似"某个 ODE，它就**是**整流流 ODE 在 $\bar{\alpha}$ 网格上的精确解。

### 8.6 ε-预测与整流速度的等价性

**Proposition 5.19** 证明：训练 $\hat{\epsilon}_\theta$ 使得 $\mathbb{E}\|\hat{\epsilon}_\theta - \boldsymbol{\epsilon}\|^2$ 最小，等价于学习整流速度 $\widetilde{\mathbf{u}}_t^{\theta}(\mathbf{x}) = -(\mathbf{x} - \hat{\epsilon}_\theta(\mathbf{x},t))$。二者通过可逆线性映射联系，且任何正的时间加权 $w(t)$ 不改变最优预测器（Lemma 5.18）。

---

## 九、引导生成

### 9.1 分类器引导（Classifier-Based Guidance）

给定辅助分类器 $p_\phi(y \mid \mathbf{x}_t, t)$，目标后验为

$$
p(\mathbf{x}_t \mid y) \propto p_\theta(\mathbf{x}_t)\,p_\phi(y \mid \mathbf{x}_t, t)
$$

取对数梯度，得到 score 的加法分解：

$$
\nabla_{\mathbf{x}_t}\log p(\mathbf{x}_t \mid y) = \underbrace{\nabla_{\mathbf{x}_t}\log p_\theta(\mathbf{x}_t)}_{\text{无条件 score}} + \underbrace{\nabla_{\mathbf{x}_t}\log p_\phi(y \mid \mathbf{x}_t, t)}_{\text{分类器梯度}}
$$

在 DDPM 离散框架中，这对应于**均值偏移**：

$$
\tilde{\mu}_\theta(\mathbf{x}_t, t \mid y) = \mu_\theta(\mathbf{x}_t, t) + \lambda\sigma_t^2\nabla_{\mathbf{x}_t}\log p_\phi(y \mid \mathbf{x}_t, t)
$$

其中 $\lambda$ 控制引导强度，$\sigma_t^2$ 确保偏移量与逆步方差匹配。

### 9.2 无分类器引导（Classifier-Free Guidance）

不需要外部分类器。训练时随机丢弃条件 $\mathbf{c}$，使模型同时学会条件与无条件预测。采样时混合：

$$
\hat{\boldsymbol{\epsilon}}_\lambda(\mathbf{x}_t, t, \mathbf{c}) = \hat{\boldsymbol{\epsilon}}_{\mathrm{uncond}} + \lambda\left(\hat{\boldsymbol{\epsilon}}_{\mathrm{cond}} - \hat{\boldsymbol{\epsilon}}_{\mathrm{uncond}}\right)
$$

**Score 形式**的等价表达：

$$
s_t^{(\lambda)}(\mathbf{x}) = (1-\lambda)\,s_t^{\mathrm{uncond}}(\mathbf{x}) + \lambda\,s_t^{\mathrm{cond}}(\mathbf{x})
$$

- $\lambda = 0$：纯无条件生成
- $\lambda = 1$：标准条件生成
- $\lambda > 1$：外推，增强条件一致性（代价是多样性下降）

**Lemma 6.2** 给出直觉：在噪声预测器关于条件嵌入局部线性的假设下，$\Delta\hat{\epsilon} := \hat{\epsilon}_{\mathrm{cond}} - \hat{\epsilon}_{\mathrm{uncond}}$ 相当于一个学到的"条件方向"，混合系数 $\lambda$ 控制沿该方向的步长。

### 9.3 时变引导调度

![引导调度公式](../../pdfs/2026-04-16/diffusion-models-a-mathematical-introduction.mineru/hybrid_auto/images/page-49-equation-01.jpg)

常数 $\lambda$ 在不同噪声水平下可能过强或过弱。一种实用的参数化方案：

$$
\lambda_t = \lambda_{\max}\,\sigma(a\ell_t + b), \qquad \ell_t := \log\mathrm{SNR}_t
$$

其中 $\sigma$ 是 sigmoid 函数。直觉：**早期（低 SNR）用小引导避免与噪声对抗，后期（高 SNR）用大引导锐化条件属性**。

### 9.4 引导蒸馏

**Definition 6.3**：学生模型通过匹配教师的 $\hat{\mathbf{x}}_0$ 预测来蒸馏引导行为：

$$
\mathcal{L}_{\mathrm{distill}} = \sum_k \mathbb{E}\left[\|\hat{\mathbf{x}}_0^{\mathrm{S}}(\mathbf{x}_{\tau_k}) - \hat{\mathbf{x}}_0^{\mathrm{T}}(\mathbf{x}_{\tau_k})\|_2^2\right]
$$

**Proposition 6.4** 证明：若学生在网格 $\{\tau_k\}$ 上精确匹配教师的 $\hat{\mathbf{x}}_0$，则 DDIM 采样下二者的轨迹完全一致——因为 DDIM 的端点公式（Theorem 5.16）是 $\hat{\mathbf{x}}_0$ 和 $\hat{\epsilon}$ 的确定性函数，归纳即得。

---

## 十、全文定理/命题索引与证明策略

| 结果 | 核心工具 | 证明策略 |
|------|----------|----------|
| 闭式边缘 $q(\mathbf{x}_t\mid\mathbf{x}_0)$ | 重参数化 + 高斯和 | 归纳法，方差逐步合并 |
| 真后验 $q(\mathbf{x}_{t-1}\mid\mathbf{x}_t,\mathbf{x}_0)$ | 高斯乘积 | Bayes + completing the square |
| 变分上界 → 噪声损失 | 高斯 KL 闭式 | 伸缩和 + 等方差 KL 化简 |
| DDIM 保持边缘 | 全方差公式 | 反向归纳，$\sigma_t^2$ 消去 |
| 概率流 ODE | $\Delta p = \nabla\cdot(p\nabla\log p)$ | Fokker-Planck → 连续性方程 |
| CFM = MFM | $L^2$ 正交原理 | 全方差分解 |
| DDIM = 整流流 | 直线特征线 | 精确积分 + 端点公式 |
| 分类器引导 | score 加法性 | $\log(ab)' = (\log a)' + (\log b)'$ |
| CFG | 线性插值 | 局部线性化 + 均值偏移 |

---

## 十一、个人评价与延伸方向

### 11.1 本文优点

1. **记号一致性极强**：全文围绕 $(\alpha_t, \bar{\alpha}_t, \tilde{\beta}_t)$ 展开，避免了不同论文记号混乱的问题
2. **中间步骤不省略**：从 completing the square 到伸缩和的每一步都有显式展示
3. **统一视角**：Flow Matching 不是作为独立范式引入，而是作为概率流 ODE 的直接推论，再通过 Theorem 5.16 与 DDIM 建立精确等价

### 11.2 局限

1. 缺乏 score matching 训练的显式推导（denoising score matching、sliced score matching 等）
2. 未涉及 SDE 反向（Anderson 反向 SDE）的完整推导
3. 连续时间讨论集中在 VP（方差保持），未系统处理 VE（方差爆炸）和 sub-VP 变体
4. 没有实验或数值示例

### 11.3 延伸阅读

- **Score-based SDE 框架**：Song et al., ICLR 2021 [12]——Anderson 反向 SDE 的完整推导
- **EDM（Elucidating Design Space）**：Karras et al., NeurIPS 2022 [4]——统一预条件和采样器设计
- **Consistency Models**：Song et al., ICML 2023——直接学习从噪声到数据的单步映射
- **Rectified Flow**：Liu et al., ICLR 2023——本文 §5.3 的直接理论来源
