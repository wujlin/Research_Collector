---
title: "Denoising Diffusion Probabilistic Models"
authors: "Jonathan Ho, Ajay Jain, Pieter Abbeel"
venue: "NeurIPS 2020"
date_read: "2026-04-16"
topics: ["DDPM", "去噪扩散", "变分下界", "score matching"]
---

# Denoising Diffusion Probabilistic Models

## 精读笔记

---

## 一、问题背景与动机

### 1.1 生成模型的发展脉络

2020 年之前，深度生成模型领域由以下几大范式主导：

- **GAN**（Generative Adversarial Networks）：样本质量极高，但训练不稳定（模式坍塌），且不提供似然估计
- **VAE**（Variational Autoencoders）：原理清晰、训练稳定，但生成样本通常较为模糊
- **Flow 模型**（Normalizing Flows）：精确似然计算，但架构设计受可逆约束限制
- **自回归模型**：精确似然、高质量样本，但采样速度极慢（逐像素生成）

**扩散概率模型**（diffusion probabilistic models）最早由 Sohl-Dickstein et al. (2015) 提出，灵感来源于非平衡热力学：通过逐步添加噪声破坏数据结构（前向扩散），再学习逐步去噪（反向过程）来生成样本。然而在 DDPM 之前，这类模型从未展示出与主流方法竞争的样本质量。

### 1.2 本文核心贡献

Jonathan Ho 等人在本文中解决了扩散模型"原理优美但效果不佳"的关键矛盾。核心贡献包括：

1. **首次证明扩散模型能生成高质量图像**，在 CIFAR10 上取得 FID 3.17（当时无条件生成 SOTA）
2. **发现 ε-prediction 参数化**，揭示扩散模型训练与多噪声尺度下的去噪 score matching 之间的等价关系
3. **提出简化训练目标** $L_{\text{simple}}$，去除变分下界中的权重系数，实质上让模型更关注困难的高噪声去噪任务
4. **渐进式有损压缩**解释——采样过程可视为广义的自回归解码

---

## 二、前向扩散过程（Forward Diffusion Process）

### 2.1 基本定义

扩散模型属于**隐变量模型**（latent variable model），数据分布建模为：

$$p_\theta(\mathbf{x}_0) := \int p_\theta(\mathbf{x}_{0:T}) \, d\mathbf{x}_{1:T}$$

其中隐变量 $\mathbf{x}_1, \ldots, \mathbf{x}_T$ 与数据 $\mathbf{x}_0$ 具有**相同维度**——这是扩散模型区别于 VAE（低维隐空间）的关键特征。

**前向过程**（forward process / diffusion process）是一条固定的 Markov 链，逐步向数据添加高斯噪声：

$$q(\mathbf{x}_{1:T} \mid \mathbf{x}_0) := \prod_{t=1}^{T} q(\mathbf{x}_t \mid \mathbf{x}_{t-1})$$

每一步的转移核为：

$$q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) := \mathcal{N}\left(\mathbf{x}_t;\, \sqrt{1 - \beta_t}\, \mathbf{x}_{t-1},\, \beta_t \mathbf{I}\right)$$

其中 $\beta_1, \ldots, \beta_T$ 是**噪声调度**（variance schedule），控制每一步添加多少噪声。注意均值中的 $\sqrt{1 - \beta_t}$ 缩放因子——它确保每一步在添加噪声的同时缩小信号，使得总方差不会无限增长。

![Figure 2: 有向图模型](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-01-figure-01.jpg)

*Figure 2 — DDPM 的有向图模型。上方实线箭头（从右到左）：反向去噪过程 $p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$，由神经网络参数化。下方虚线箭头（从右到左）：前向扩散过程 $q(\mathbf{x}_t \mid \mathbf{x}_{t-1})$，是固定的高斯噪声注入。最左侧灰色节点 $\mathbf{x}_T$ 接近纯噪声，最右侧 $\mathbf{x}_0$ 是干净数据。*

### 2.2 闭合形式采样：任意时刻的边际分布

前向过程的一个核心优势是：我们不需要逐步模拟 Markov 链就能直接从 $q(\mathbf{x}_t \mid \mathbf{x}_0)$ 采样。引入记号：

$$\alpha_t := 1 - \beta_t, \qquad \bar{\alpha}_t := \prod_{s=1}^{t} \alpha_s$$

则 $\mathbf{x}_t$ 关于 $\mathbf{x}_0$ 的边际分布为：

$$q(\mathbf{x}_t \mid \mathbf{x}_0) = \mathcal{N}\left(\mathbf{x}_t;\, \sqrt{\bar{\alpha}_t}\, \mathbf{x}_0,\, (1 - \bar{\alpha}_t) \mathbf{I}\right)$$

**推导过程**：这利用了高斯分布在线性变换下的闭合性。$\mathbf{x}_1 = \sqrt{\alpha_1}\, \mathbf{x}_0 + \sqrt{\beta_1}\, \boldsymbol{\epsilon}_1$，$\mathbf{x}_2 = \sqrt{\alpha_2}\, \mathbf{x}_1 + \sqrt{\beta_2}\, \boldsymbol{\epsilon}_2$。代入得 $\mathbf{x}_2 = \sqrt{\alpha_1 \alpha_2}\, \mathbf{x}_0 + \sqrt{1 - \alpha_1 \alpha_2}\, \boldsymbol{\epsilon}$（利用独立高斯之和的方差可加性）。归纳到 $t$ 步即得上式。

**等价的重参数化表示**：

$$\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\, \mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon}, \qquad \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

物理含义：$\mathbf{x}_t$ 是原始信号 $\mathbf{x}_0$（以 $\sqrt{\bar{\alpha}_t}$ 衰减）与纯噪声 $\boldsymbol{\epsilon}$（以 $\sqrt{1 - \bar{\alpha}_t}$ 放大）的线性混合。当 $t \to T$ 时，$\bar{\alpha}_T \to 0$，信号被完全淹没，$\mathbf{x}_T \approx \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$。

### 2.3 噪声调度的选择

本文采用**线性调度**：$\beta_1 = 10^{-4}$，$\beta_T = 0.02$，$T = 1000$。设计目标是：

- $\beta_t$ 足够小，使前向/反向过程在每步都近似高斯（Sohl-Dickstein et al. 的可逆性保证）
- $\bar{\alpha}_T$ 足够小，使终态接近标准正态（$D_{\mathrm{KL}}(q(\mathbf{x}_T \mid \mathbf{x}_0) \| \mathcal{N}(\mathbf{0}, \mathbf{I})) \approx 10^{-5}$ bits/dim）

---

## 三、反向去噪过程（Reverse Denoising Process）

### 3.1 反向过程的定义

**反向过程**（reverse process）是从纯噪声 $\mathbf{x}_T \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 出发，逐步去噪得到干净样本的参数化 Markov 链：

$$p_\theta(\mathbf{x}_{0:T}) := p(\mathbf{x}_T) \prod_{t=1}^{T} p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$$

每一步的转移核参数化为高斯分布：

$$p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t) := \mathcal{N}\left(\mathbf{x}_{t-1};\, \boldsymbol{\mu}_\theta(\mathbf{x}_t, t),\, \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t)\right)$$

为什么高斯参数化是合理的？当 $\beta_t$ 足够小时，可以证明真实的反向条件分布 $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$ 也近似高斯（Feller, 1949）。因此用高斯参数化 $p_\theta$ 不会损失表达能力。

### 3.2 方差的选择

作者将方差设为**不可学习的时间依赖常数**：$\boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t) = \sigma_t^2 \mathbf{I}$。实验中尝试了两种选择：

- $\sigma_t^2 = \beta_t$：对应 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 时的最优选择（上界）
- $\sigma_t^2 = \tilde{\beta}_t := \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t$：对应 $\mathbf{x}_0$ 为确定性点时的最优选择（下界）

两者是反向过程熵的上下界。实验表明两种选择效果相似。

### 3.3 前向过程后验（Forward Process Posterior）

当条件于 $\mathbf{x}_0$ 时，前向过程的后验 $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)$ 是**可解析计算的**高斯分布（利用 Bayes 定理和高斯的共轭性）：

$$q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0) = \mathcal{N}\left(\mathbf{x}_{t-1};\, \tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \mathbf{x}_0),\, \tilde{\beta}_t \mathbf{I}\right)$$

其中后验均值和后验方差分别为：

$$\tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \mathbf{x}_0) := \frac{\sqrt{\bar{\alpha}_{t-1}}\, \beta_t}{1 - \bar{\alpha}_t}\, \mathbf{x}_0 + \frac{\sqrt{\alpha_t}\,(1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t}\, \mathbf{x}_t$$

$$\tilde{\beta}_t := \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t}\, \beta_t$$

这个后验是训练目标的核心——我们希望学到的 $p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$ 去逼近 $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)$。

---

## 四、变分下界推导（ELBO Derivation）——逐步展开

### 4.1 起点：负对数似然的变分上界

训练目标是最大化数据对数似然 $\log p_\theta(\mathbf{x}_0)$。由于直接计算不可行（需要对所有隐变量积分），我们转而优化**负对数似然的变分上界**（即最小化 ELBO 的负值）：

$$\mathbb{E}\left[-\log p_\theta(\mathbf{x}_0)\right] \leq \mathbb{E}_q\left[-\log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)}\right] =: L$$

**这个不等式从何而来？** 利用 Jensen 不等式：

$$-\log p_\theta(\mathbf{x}_0) = -\log \int p_\theta(\mathbf{x}_{0:T})\, d\mathbf{x}_{1:T} = -\log \int q(\mathbf{x}_{1:T} \mid \mathbf{x}_0) \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)}\, d\mathbf{x}_{1:T}$$

$$\leq -\int q(\mathbf{x}_{1:T} \mid \mathbf{x}_0) \log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)}\, d\mathbf{x}_{1:T} = \mathbb{E}_q\left[-\log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)}\right]$$

### 4.2 展开联合分布

将 $L$ 中的联合分布展开为 Markov 链形式：

$$L = \mathbb{E}_q\left[-\log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T} \mid \mathbf{x}_0)}\right]$$

$$= \mathbb{E}_q\left[-\log \frac{p(\mathbf{x}_T) \prod_{t=1}^{T} p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{\prod_{t=1}^{T} q(\mathbf{x}_t \mid \mathbf{x}_{t-1})}\right]$$

$$= \mathbb{E}_q\left[-\log p(\mathbf{x}_T) - \sum_{t \geq 1} \log \frac{p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{q(\mathbf{x}_t \mid \mathbf{x}_{t-1})}\right]$$

### 4.3 分离 $t = 1$ 项

将 $t = 1$ 项从求和中分离出来：

$$L = \mathbb{E}_q\left[-\log p(\mathbf{x}_T) - \sum_{t > 1} \log \frac{p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{q(\mathbf{x}_t \mid \mathbf{x}_{t-1})} - \log \frac{p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)}{q(\mathbf{x}_1 \mid \mathbf{x}_0)}\right]$$

### 4.4 利用 Bayes 定理改写 $q(\mathbf{x}_t \mid \mathbf{x}_{t-1})$

对 $t > 1$ 的项，利用 Bayes 定理将 $q(\mathbf{x}_t \mid \mathbf{x}_{t-1})$ 改写为包含前向后验的形式：

$$q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) = q(\mathbf{x}_t \mid \mathbf{x}_{t-1}, \mathbf{x}_0) = \frac{q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)\, q(\mathbf{x}_t \mid \mathbf{x}_0)}{q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}$$

第一个等号成立因为前向过程是 Markov 的（条件于 $\mathbf{x}_{t-1}$ 后，$\mathbf{x}_t$ 与 $\mathbf{x}_0$ 独立）。代入得：

$$\frac{p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{q(\mathbf{x}_t \mid \mathbf{x}_{t-1})} = \frac{p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)} \cdot \frac{q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}{q(\mathbf{x}_t \mid \mathbf{x}_0)}$$

### 4.5 代入并合并比值项

将上式代入 $L$：

$$L = \mathbb{E}_q\left[-\log p(\mathbf{x}_T) - \sum_{t > 1} \log \frac{p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)} \cdot \frac{q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}{q(\mathbf{x}_t \mid \mathbf{x}_0)} - \log \frac{p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)}{q(\mathbf{x}_1 \mid \mathbf{x}_0)}\right]$$

观察 $\sum_{t>1}$ 中的 $\frac{q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}{q(\mathbf{x}_t \mid \mathbf{x}_0)}$ 项——这是一个**伸缩和**（telescoping product）：

$$\sum_{t=2}^{T} \log \frac{q(\mathbf{x}_{t-1} \mid \mathbf{x}_0)}{q(\mathbf{x}_t \mid \mathbf{x}_0)} = \log \frac{q(\mathbf{x}_1 \mid \mathbf{x}_0)}{q(\mathbf{x}_T \mid \mathbf{x}_0)}$$

将伸缩和与最后一项 $-\log \frac{p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)}{q(\mathbf{x}_1 \mid \mathbf{x}_0)}$ 中的 $q(\mathbf{x}_1 \mid \mathbf{x}_0)$ 合并，得到：

$$L = \mathbb{E}_q\left[-\log \frac{p(\mathbf{x}_T)}{q(\mathbf{x}_T \mid \mathbf{x}_0)} - \sum_{t > 1} \log \frac{p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)}{q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)} - \log p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)\right]$$

### 4.6 识别 KL 散度

利用 KL 散度的定义 $D_{\mathrm{KL}}(q \| p) = \mathbb{E}_q\left[\log \frac{q}{p}\right]$，将上式中的每项识别为 KL 散度或对数似然：

$$\boxed{L = \mathbb{E}_q\left[\underbrace{D_{\mathrm{KL}}\left(q(\mathbf{x}_T \mid \mathbf{x}_0) \,\|\, p(\mathbf{x}_T)\right)}_{L_T} + \sum_{t > 1} \underbrace{D_{\mathrm{KL}}\left(q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0) \,\|\, p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)\right)}_{L_{t-1}} - \underbrace{\log p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)}_{L_0}\right]}$$

### 4.7 三类损失项的含义

| 项 | 含义 | 是否需要训练 |
|---|------|------------|
| $L_T = D_{\mathrm{KL}}(q(\mathbf{x}_T \mid \mathbf{x}_0) \| p(\mathbf{x}_T))$ | 前向过程终态与先验的匹配度 | 否（$\beta_t$ 固定，$L_T \approx 10^{-5}$ 常数） |
| $L_{t-1} = D_{\mathrm{KL}}(q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0) \| p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t))$ | 反向过程每步与前向后验的匹配度 | 是（核心训练目标） |
| $L_0 = -\log p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)$ | 最后一步的重建质量 | 是（离散化解码器） |

关键优势：由于 $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)$ 和 $p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$ 都是高斯分布，$L_{t-1}$ 中的 KL 散度具有**解析闭合形式**——无需高方差的 Monte Carlo 估计。这是扩散模型相比一般 VAE 的重要优势。

---

## 五、$L_{t-1}$ 的展开与均值匹配

### 5.1 两个高斯之间的 KL 散度

对于两个具有相同方差 $\sigma_t^2 \mathbf{I}$ 的高斯分布，KL 散度退化为均值之间的均方误差：

$$L_{t-1} = \mathbb{E}_q\left[\frac{1}{2\sigma_t^2} \left\| \tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \mathbf{x}_0) - \boldsymbol{\mu}_\theta(\mathbf{x}_t, t) \right\|^2\right] + C$$

其中 $C$ 是与 $\theta$ 无关的常数。训练目标变为：**让网络预测的均值 $\boldsymbol{\mu}_\theta(\mathbf{x}_t, t)$ 逼近前向后验均值 $\tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \mathbf{x}_0)$**。

### 5.2 重参数化代入

利用重参数化 $\mathbf{x}_t(\mathbf{x}_0, \boldsymbol{\epsilon}) = \sqrt{\bar{\alpha}_t}\, \mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon}$（其中 $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$），从 $\mathbf{x}_t$ 反解 $\mathbf{x}_0$：

$$\mathbf{x}_0 = \frac{1}{\sqrt{\bar{\alpha}_t}}\left(\mathbf{x}_t - \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon}\right)$$

代入后验均值公式 $\tilde{\boldsymbol{\mu}}_t$：

$$\tilde{\boldsymbol{\mu}}_t = \frac{\sqrt{\bar{\alpha}_{t-1}}\, \beta_t}{1 - \bar{\alpha}_t}\, \mathbf{x}_0 + \frac{\sqrt{\alpha_t}(1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t}\, \mathbf{x}_t$$

将 $\mathbf{x}_0 = \frac{1}{\sqrt{\bar{\alpha}_t}}(\mathbf{x}_t - \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon})$ 代入上式的 $\mathbf{x}_0$ 项，经过代数化简（合并 $\mathbf{x}_t$ 的系数，利用 $\bar{\alpha}_t = \alpha_t \bar{\alpha}_{t-1}$），得到：

$$\tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \boldsymbol{\epsilon}) = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \boldsymbol{\epsilon}\right)$$

这个表达式极其重要——它告诉我们：**前向后验均值完全由当前噪声样本 $\mathbf{x}_t$ 和加入的噪声 $\boldsymbol{\epsilon}$ 决定**。

### 5.3 将 $L_{t-1}$ 表示为噪声预测误差

将上式代入 $L_{t-1}$，期望从对 $(\mathbf{x}_0, \mathbf{x}_t)$ 变为对 $(\mathbf{x}_0, \boldsymbol{\epsilon})$：

$$L_{t-1} - C = \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}}\left[\frac{1}{2\sigma_t^2}\left\| \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \boldsymbol{\epsilon}\right) - \boldsymbol{\mu}_\theta(\mathbf{x}_t, t) \right\|^2\right]$$

---

## 六、ε-prediction 参数化

### 6.1 从均值预测到噪声预测

第五节的结果表明 $\boldsymbol{\mu}_\theta$ 应该预测 $\frac{1}{\sqrt{\alpha_t}}(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \boldsymbol{\epsilon})$。由于 $\mathbf{x}_t$ 本身已作为网络输入可用，我们可以让网络去预测**噪声** $\boldsymbol{\epsilon}$，而非直接预测均值。定义参数化：

$$\boldsymbol{\mu}_\theta(\mathbf{x}_t, t) = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\right)$$

其中 $\boldsymbol{\epsilon}_\theta$ 是一个神经网络，接收噪声图像 $\mathbf{x}_t$ 和时间步 $t$，预测加入的噪声 $\boldsymbol{\epsilon}$。

### 6.2 化简后的损失函数

将 ε-prediction 参数化代入 $L_{t-1}$，大量系数抵消后得到：

$$L_{t-1} - C = \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}}\left[\frac{\beta_t^2}{2\sigma_t^2 \alpha_t (1 - \bar{\alpha}_t)} \left\| \boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta\left(\sqrt{\bar{\alpha}_t}\, \mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon},\, t\right) \right\|^2\right]$$

训练目标变得极其清晰：**网络 $\boldsymbol{\epsilon}_\theta$ 的任务是，给定不同噪声程度的图像 $\mathbf{x}_t$，预测加入的噪声 $\boldsymbol{\epsilon}$**。

### 6.3 采样过程

给定训练好的 $\boldsymbol{\epsilon}_\theta$，从 $p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$ 采样就是：

$$\mathbf{x}_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\right) + \sigma_t \mathbf{z}, \qquad \mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

从 $\mathbf{x}_T \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 出发，迭代 $T$ 步即可得到样本 $\mathbf{x}_0$。

![Algorithm 1 & 2: 训练与采样算法](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-03-table-01.jpg)

*Algorithm 1 (Training) 与 Algorithm 2 (Sampling) — 训练过程极为简洁：随机采样 $\mathbf{x}_0$、时间步 $t$、噪声 $\boldsymbol{\epsilon}$，然后对 $\|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\, \mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon},\, t)\|^2$ 做梯度下降。采样过程从纯噪声出发，逐步用网络预测的噪声去噪。*

---

## 七、简化训练目标 $L_{\text{simple}}$

### 7.1 去除权重系数

完整的变分下界中，$L_{t-1}$ 前面有一个时间步依赖的权重 $\frac{\beta_t^2}{2\sigma_t^2 \alpha_t (1 - \bar{\alpha}_t)}$。作者发现**去除这个权重**对样本质量有显著提升：

$$L_{\text{simple}}(\theta) := \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}}\left[\left\| \boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta\left(\sqrt{\bar{\alpha}_t}\, \mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\, \boldsymbol{\epsilon},\, t\right) \right\|^2\right]$$

其中 $t \sim \text{Uniform}(\{1, \ldots, T\})$。

### 7.2 为什么 $L_{\text{simple}}$ 效果更好？

原始权重 $\frac{\beta_t^2}{2\sigma_t^2 \alpha_t (1 - \bar{\alpha}_t)}$ 在小 $t$（低噪声）时权重较大，在大 $t$（高噪声）时权重较小。$L_{\text{simple}}$ 通过均匀采样 $t$ 实质上**下调了小 $t$ 项的权重**。

直觉解释：小 $t$ 时噪声很少，去噪任务"太简单"——网络只需要做微小的修正。大 $t$ 时去噪任务更困难、更有信息量。$L_{\text{simple}}$ 让网络把更多容量分配给困难的高噪声去噪任务，从而提升整体样本质量。

代价是：$L_{\text{simple}}$ 不再是负对数似然的严格上界，因此用它训练会牺牲一些对数似然性能（$\leq 3.75$ vs $\leq 3.70$ bits/dim），但样本质量大幅提升（FID 3.17 vs 13.51）。

### 7.3 $L_0$ 的处理

对于 $t = 1$，$L_{\text{simple}}$ 中的损失对应于 $L_0$，即最终重建项。论文使用**离散化高斯解码器**处理离散像素值：

$$p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1) = \prod_{i=1}^{D} \int_{\delta_-(x_0^i)}^{\delta_+(x_0^i)} \mathcal{N}(x;\, \mu_\theta^i(\mathbf{x}_1, 1),\, \sigma_1^2)\, dx$$

其中 $\delta_{\pm}$ 在边界处扩展到 $\pm\infty$，在内部取 $x_0^i \pm \frac{1}{255}$。这确保了变分下界是离散数据的无损编码长度。

---

## 八、与 Score Matching 的等价关系

### 8.1 去噪 Score Matching 回顾

**Score function** 定义为数据分布对数密度的梯度：$\nabla_{\mathbf{x}} \log p(\mathbf{x})$。Score matching 的目标是训练一个网络 $s_\theta(\mathbf{x})$ 来估计这个梯度。

**去噪 score matching**（Vincent, 2011）的关键结果是：对于被噪声 $\sigma$ 扰动的数据 $\tilde{\mathbf{x}} = \mathbf{x} + \sigma \boldsymbol{\epsilon}$，score function 为：

$$\nabla_{\tilde{\mathbf{x}}} \log q_\sigma(\tilde{\mathbf{x}} \mid \mathbf{x}) = -\frac{\boldsymbol{\epsilon}}{\sigma}$$

因此，训练网络预测噪声 $\boldsymbol{\epsilon}$ 等价于估计 score function（差一个缩放因子）。

**NCSN**（Song & Ermon, 2019）将此推广到多个噪声尺度 $\sigma_1 > \cdots > \sigma_L$，训练一个共享的 score 网络，采样时使用**退火 Langevin 动力学**（Annealed Langevin Dynamics）。

### 8.2 DDPM 视角下的等价关系

DDPM 损失项（Eq. 12）的形式为：

$$\mathbb{E}\left[\frac{\beta_t^2}{2\sigma_t^2 \alpha_t (1 - \bar{\alpha}_t)} \left\| \boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta\left(\mathbf{x}_t, t\right) \right\|^2\right]$$

这**恰好是**多噪声尺度去噪 score matching 的损失——其中时间步 $t$ 对应噪声尺度 $\sqrt{1 - \bar{\alpha}_t}$。

同时，采样过程：

$$\mathbf{x}_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\right) + \sigma_t \mathbf{z}$$

可以改写为（利用 $\boldsymbol{\epsilon}_\theta \propto -\nabla_{\mathbf{x}} \log p(\mathbf{x}_t)$）：

$$\mathbf{x}_{t-1} = \mathbf{x}_t + \frac{\beta_t}{2} \nabla_{\mathbf{x}_t} \log p(\mathbf{x}_t) + \sigma_t \mathbf{z}$$

这正是**Langevin 动力学**的离散化形式——$\boldsymbol{\epsilon}_\theta$ 可被视为学到的数据密度梯度。

### 8.3 等价关系的意义

| 视角 | 训练 | 采样 |
|------|------|------|
| **DDPM（变分推断）** | 最小化变分下界 $L$ | 反向 Markov 链 |
| **Score Matching** | 多尺度去噪 score matching | 退火 Langevin 动力学 |

两者在数学上**等价**，但各有优势：
- DDPM 提供了**严格的变分推断框架**，可以直接计算对数似然
- DDPM 的训练过程**直接优化采样器的质量**（通过变分推断训练 Langevin 采样器），而非像 NCSN 那样先训练 score network 再 post-hoc 设定采样系数

---

## 九、网络架构

作者使用 **U-Net** 骨干网络（基于 PixelCNN++ 的设计）：

- 残差块使用 **Group Normalization**（替代 Weight Normalization 以简化实现）
- 时间步 $t$ 通过 **Transformer 正弦位置编码**注入每个残差块
- 在 $16 \times 16$ 分辨率处使用 **Self-Attention**
- CIFAR10 模型：4 层分辨率（$32 \times 32$ 到 $4 \times 4$），35.7M 参数
- LSUN/CelebA-HQ 模型：6 层分辨率，114M 参数
- 训练使用 Adam 优化器，EMA 衰减系数 0.9999

---

## 十、实验结果

### 10.1 CIFAR10 样本质量

![Table 1 & Table 2: CIFAR10 结果与消融](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-04-table-01.jpg)

*Table 1 (左) — CIFAR10 定量结果。DDPM 使用 $L_{\text{simple}}$ 取得 IS=9.46, FID=3.17，是当时无条件生成的 SOTA。注意 FID 优于大部分条件生成模型（如 BigGAN 的 14.73）。Table 2 (右) — 消融实验：ε-prediction + $L_{\text{simple}}$ 的组合效果最佳。$\tilde{\mu}$-prediction 在简化目标下无法稳定训练，学习方差导致训练不稳定。*

关键发现：

- $L_{\text{simple}}$（简化目标）：FID 3.17，IS 9.46，NLL $\leq$ 3.75 bits/dim
- $L$（完整变分下界）：FID 13.51，IS 7.67，NLL $\leq$ 3.70 bits/dim
- 简化目标样本质量远优于完整变分下界，但对数似然略差

### 10.2 LSUN 256×256 样本

![Figure 3: LSUN Church 样本](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-05-figure-01.jpg)

*Figure 3 — LSUN Church 256×256 无条件生成样本。FID=7.89。样本展示了多样的建筑风格和光照条件。*

![Figure 4: LSUN Bedroom 样本](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-05-figure-02.jpg)

*Figure 4 — LSUN Bedroom 256×256 无条件生成样本（大模型）。FID=4.90。样本质量接近 ProgressiveGAN（FID 8.34），细节纹理丰富、空间布局合理。*

![Table 3: LSUN FID 对比](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-12-table-01.jpg)

*Table 3 — LSUN 256×256 FID 对比。DDPM 在 Bedroom 上接近 ProgressiveGAN，但与 StyleGAN/StyleGAN2 仍有差距。*

### 10.3 渐进式生成与有损压缩

#### 率失真曲线

![Figure 5: 率失真曲线](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-06-figure-01.jpg)

*Figure 5 — CIFAR10 测试集上的率失真曲线。横轴为反向过程步数（$T - t$），纵轴为 RMSE 失真。失真在低码率区域陡峭下降——大部分码率被分配给了不可察觉的细节。率 1.78 bits/dim + 失真 1.97 bits/dim = 无损码率 3.75 bits/dim，其中超过一半用于编码人眼不可察觉的失真（RMSE ≈ 0.95/255）。*

#### 渐进式生成过程

![Figure 6: CIFAR10 渐进生成](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-06-figure-04.jpg)

*Figure 6 — CIFAR10 渐进式生成（$\hat{\mathbf{x}}_0$ 随时间变化，从左到右）。大尺度特征（形状、颜色）首先出现，细节纹理最后添加——这与人类视觉的"从粗到细"处理方式一致。*

#### 条件于同一隐变量的随机采样

![Figure 7: 共享隐变量的条件采样](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-06-figure-05.jpg)

*Figure 7 — 条件于同一中间隐变量 $\mathbf{x}_t$ 的 CelebA-HQ 256×256 样本。从 $\mathbf{x}_{1000}$（纯噪声）分裂采样，各样本差异很大。但从 $\mathbf{x}_{250}$ 分裂，所有样本共享姿态、肤色、发型、表情等高级属性——说明隐变量 $\mathbf{x}_t$ 以层次化方式编码了语义信息。*

### 10.4 消融实验

Table 2 (右侧) 的消融揭示了关键设计选择：

| 参数化方式 | 训练目标 | IS | FID |
|-----------|---------|-----|-----|
| $\tilde{\mu}$-prediction | $L$, learned diagonal $\Sigma$ | 7.28 | 23.69 |
| $\tilde{\mu}$-prediction | $L$, fixed isotropic $\Sigma$ | 8.06 | 13.22 |
| $\tilde{\mu}$-prediction | $\|\tilde{\mu} - \mu_\theta\|^2$ (unweighted MSE) | 不稳定 | 不稳定 |
| $\epsilon$-prediction | $L$, learned diagonal $\Sigma$ | 不稳定 | 不稳定 |
| $\epsilon$-prediction | $L$, fixed isotropic $\Sigma$ | 7.67 | 13.51 |
| **$\epsilon$-prediction** | **$L_{\text{simple}}$** | **9.46** | **3.17** |

结论：
1. **学习方差不稳定**——固定方差更安全
2. **$\epsilon$-prediction 在 $L_{\text{simple}}$ 下远优于 $\tilde{\mu}$-prediction**——后者在去除权重后无法稳定训练
3. **$L_{\text{simple}}$ 是样本质量的关键**——代价是对数似然略差

### 10.5 插值

![Figure 8: CelebA-HQ 隐空间插值](../../pdfs/2026-04-16/denoising-diffusion-probabilistic-models.mineru/hybrid_auto/images/page-07-figure-02.jpg)

*Figure 8 — CelebA-HQ 256×256 隐空间插值（$t = 500$）。源图像经前向过程扩散到 $\mathbf{x}_t$，在隐空间线性插值后用反向过程重建。插值平滑地变化了姿态、肤色、发型和表情等属性，生成质量高、过渡自然。*

---

## 十一、与自回归解码的联系

作者提出了一个深刻的观察：变分下界 (Eq. 5) 可以改写为：

$$L = D_{\mathrm{KL}}(q(\mathbf{x}_T) \| p(\mathbf{x}_T)) + \mathbb{E}_q\left[\sum_{t \geq 1} D_{\mathrm{KL}}(q(\mathbf{x}_{t-1} \mid \mathbf{x}_t) \| p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t))\right] + H(\mathbf{x}_0)$$

如果将扩散过程设为逐维掩码（第 $t$ 步掩码第 $t$ 个坐标），则 $p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$ 退化为给定后续坐标预测第 $t$ 个坐标——这正是**自回归模型**。

因此，高斯扩散模型可以视为一种**广义自回归模型**，其"比特顺序"（bit ordering）不是逐坐标的，而是从粗到细的——这种顺序无法通过简单重排数据坐标来实现。$T = 1000$ 的扩散长度不受数据维度限制（CIFAR10 的维度为 $32 \times 32 \times 3 = 3072$），且高斯噪声可能比掩码噪声作为"擦除"机制更自然。

---

## 十二、与 NCSN 的具体差异

虽然 DDPM 与 NCSN 在数学上建立了等价关系，但实现细节上有重要差异：

| 方面 | DDPM | NCSN |
|------|------|------|
| 网络架构 | U-Net + Self-Attention | RefineNet + Dilated Conv |
| 时间条件化 | Sinusoidal embedding 注入每层 | 仅在归一化层或输出层 |
| 数据缩放 | 每步缩放 $\sqrt{1 - \beta_t}$，控制方差 | 不缩放，方差随噪声增长 |
| 先验匹配 | $D_{\mathrm{KL}}(q(\mathbf{x}_T \mid \mathbf{x}_0) \| \mathcal{N}(\mathbf{0}, \mathbf{I})) \approx 0$ | 不保证先验匹配 |
| 采样系数 | 从 $\beta_t$ 严格推导 | 手动设置 |
| 训练目标 | 直接优化采样器（变分推断） | Score network 训练后 post-hoc 采样 |

---

## 十三、核心结论

1. **扩散模型能生成高质量图像**：在 CIFAR10 上取得 FID 3.17，打破了"扩散模型样本质量差"的固有认知
2. **ε-prediction 是关键参数化**：将均值预测转化为噪声预测，既简化了训练目标又建立了与 score matching 的等价关系
3. **$L_{\text{simple}}$ 优于完整 ELBO**：去除权重系数实质上让网络更关注困难的去噪任务，以微小的对数似然代价换取显著的样本质量提升
4. **变分推断 = 去噪 score matching = Langevin 动力学**：三个看似不同的框架在 DDPM 中被统一
5. **渐进式生成**：采样过程自然地实现了从粗到细的生成，隐变量以层次化方式编码语义信息

---

## 十四、个人评注与延伸思考

### 14.1 历史地位

DDPM 是扩散模型从理论优美走向实用高效的**分水岭**。此后，DDIM（Song et al., 2021）解决了采样速度问题，Classifier-free Guidance（Ho & Salimans, 2022）引入了条件控制，Stable Diffusion 将扩散模型带入潜空间实现了工业级文生图——这些后续工作的数学基础均直接建立在 DDPM 之上。

### 14.2 开放问题（当时视角）

- **采样速度**：$T = 1000$ 步的迭代采样远慢于 GAN 的一次前向传播（后由 DDIM 和 DPM-Solver 解决）
- **方差学习**：固定方差是否最优？（后由 Improved DDPM, Nichol & Dhariwal 2021 解决，证明学习方差可以显著提升对数似然）
- **连续时间极限**：$T \to \infty$ 下扩散模型的理论性质？（后由 Score SDE, Song et al. 2021 统一为 SDE 框架）

### 14.3 与非平衡统计力学的关联

DDPM 的前向过程本质上是一个驱向平衡的扩散过程——数据的结构信息（非平衡态）被噪声逐步破坏，最终达到热力学平衡（$\mathcal{N}(\mathbf{0}, \mathbf{I})$）。反向过程则是在学习一个非平衡过程——从平衡态恢复结构。这与 Sohl-Dickstein et al. (2015) 论文标题中的"非平衡热力学"一脉相承，也与 Friston 自由能原理中的"通过最小化自由能维持非平衡稳态"形成有趣的概念呼应。

---

## 关键术语索引

| 中文 | 英文 | 简述 |
|------|------|------|
| 扩散概率模型 | Diffusion Probabilistic Model | 通过逐步去噪生成样本的隐变量模型 |
| 前向扩散 | Forward Process | 固定的高斯噪声注入 Markov 链 |
| 反向去噪 | Reverse Process | 参数化的去噪 Markov 链 |
| 噪声调度 | Variance Schedule | $\beta_1, \ldots, \beta_T$ 控制每步噪声量 |
| 变分下界 | Variational Lower Bound (ELBO) | 对数似然的可优化下界 |
| 前向后验 | Forward Process Posterior | $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)$，闭合形式高斯 |
| ε-prediction | ε-prediction | 网络预测噪声而非均值的参数化 |
| 简化目标 | $L_{\text{simple}}$ | 去除权重系数的均匀采样 MSE 损失 |
| Score function | Score function | 数据对数密度的梯度 $\nabla_{\mathbf{x}} \log p(\mathbf{x})$ |
| 去噪 score matching | Denoising Score Matching | 通过去噪估计 score function |
| Langevin 动力学 | Langevin Dynamics | 沿 score 方向的梯度噪声采样 |
| 渐进式生成 | Progressive Generation | 从粗到细的层次化生成过程 |
