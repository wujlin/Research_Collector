---
title: "A Primer on Variational Inference for Physics-Informed Deep Generative Modelling"
authors: "Alex Glyn-Davies, Arnaud Vadeboncoeur, O. Deniz Akyildiz, Ieva Kazlauskaite, Mark Girolami"
venue: "arXiv (2024)"
date_read: "2026-04-16"
topics: ["变分推断", "ELBO", "physics-informed", "生成模型", "逆问题"]
---

# A Primer on Variational Inference for Physics-Informed Deep Generative Modelling

## Core Answer

这篇文章要回答的核心问题是：**如何用变分推断 (Variational Inference, VI) 系统性地构建具有不确定性量化 (Uncertainty Quantification, UQ) 能力的物理约束深度生成模型？**

作者的回答分两层：

1. **方法论层**：VI 的核心是把统计推断转化为优化问题——通过最小化变分近似 $q_\phi(\mathbf{z})$ 与真实后验 $p(\mathbf{z}|\mathbf{y})$ 之间的 KL 散度，等价于最大化 Evidence Lower Bound (ELBO)。深度学习为这个框架提供了灵活的参数化手段（神经网络作为编码器/解码器），而物理约束则通过正向模型嵌入或 PDE 残差似然来注入。
2. **应用层**：根据物理约束的嵌入方式不同，文献中形成了两大技术路线——基于正向模型 (forward-model-based) 和基于残差 (residual-based) 的方法。前者将已知正向映射直接嵌入生成模型的似然函数或解码器中；后者通过 PDE 残差构造"虚拟观测量 (virtual observable)"，即使没有标注数据也能训练概率代理模型。

## 0. Reading Frame

1. 这篇文章是 **tutorial + review**，目标读者是想用 VI 解决物理问题但缺乏系统推导的科学计算研究者。
2. 它的价值不在于提出新方法，而在于用**统一符号体系**串联起散落在不同文献中的 physics-informed VI 方法。
3. 你最需要带走的是：(a) ELBO 在 Bayes VI 与生成模型两种视角下的推导差异；(b) 物理约束通过正向模型 vs. 残差两种方式进入变分目标函数的具体机制；(c) 不同方法对数据需求的分级（有监督 → 少数据 → 无数据）。

---

## 1. 三空间框架：参数 → 解 → 观测

![三空间框架图](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-02-figure-01.jpg)

论文唯一的 Figure 刻画了物理推断的三个核心空间：

| 空间 | 符号 | 含义 |
|------|------|------|
| 参数空间 (parameter space) | $\mathcal{Z}$ | 物理系统的设定参数，如扩散系数场、边界条件 |
| 解空间 (solution space) | $\mathcal{U}$ | PDE 解场，如温度场、速度场 |
| 观测空间 (observation space) | $\mathcal{Y}$ | 传感器实际观测到的数据 |

三个空间由两个映射连接：
- **正向模型 (forward model)** $F^\dagger: \mathcal{Z}_h \to \mathcal{U}_h$，从参数到解
- **观测模型 (observation model)** $H^\dagger: \mathcal{U}_h \to \mathcal{Y}$，从解到观测

正向问题是沿箭头方向走（$\mathcal{Z} \to \mathcal{U} \to \mathcal{Y}$），逆向问题则是逆箭头（$\mathcal{Y} \to \mathcal{U}$ 或 $\mathcal{Y} \to \mathcal{Z}$）。整篇文章的所有方法都可以在这张图上定位。

---

## 2. 正向问题：PDE 与加权残差方法

### 2.1 PDE 离散化的统一视角：加权残差方法 (Weighted Residual Method, WRM)

论文选择了一个聪明的切入点：不直接讨论有限元或 PINNs 的具体实现，而是用 WRM 统一所有空间离散化方法。核心步骤：

1. 定义残差函数 $R(u, z, f, x)$——PDE 方程移项后的剩余量
2. 选择一组测试函数 $\{v_i\}$，对残差做加权积分得到残差向量 $\mathbf{r}$
3. 数值求解 PDE = 找到使 $\mathbf{r} \approx 0$ 的 $u_h$

不同的测试函数/试探函数选择产生不同的方法：

| 方法 | 试探函数 $u_h$ | 测试函数 $v_i$ |
|------|----------------|----------------|
| 有限元 (FEM) | 分片线性帽函数展开 | 同试探函数 (Bubnov-Galerkin) |
| PINNs | 神经网络 $T_L \circ \cdots \circ T_0(x)$ | Dirac-delta 配点函数 |
| 谱方法 (Spectral) | 全局基函数展开 | 视具体方案而定 |

这种统一视角的实用价值在于：**构建 VI 推断方案时可以与具体离散化方法解耦**——残差 $\mathbf{r}$ 的计算方式可以自由切换，而不影响变分目标函数的推导。

### 2.2 解与参数的有限维表示

解场和参数场通过基函数展开离散化为有限维向量：

$$u_h(x) = \sum_{i=1}^{N_u} [\mathbf{u}]_i \phi_i(x), \quad z_h(x) = \sum_{i=1}^{N_z} [\mathbf{z}]_i \psi_i(x)$$

后续所有推断方案都在系数向量 $\mathbf{u}, \mathbf{z}$ 上操作，而非直接在函数空间上。

---

## 3. 逆向问题：从点估计到贝叶斯

### 3.1 点估计反演 (Point Estimate Inversion)

最基本的反演是优化问题，包含数据拟合项和正则化项：

$$\mathbf{z}^\star = \arg\min_{\mathbf{z}} \frac{1}{2}\|\mathbf{y} - (H^\dagger \circ F^\dagger \circ \pi_z)(\mathbf{z})\|^2 + \frac{\beta}{2}\|\pi_z(\mathbf{z})\|^2$$

这是经典的 Tikhonov 正则化。另一种思路是用物理残差做正则化：

$$\mathbf{z}^\star = \arg\min_{\mathbf{z}} \min_{\mathbf{u}} \|\mathbf{y} - (H^\dagger \circ \pi_u)(\mathbf{u})\|^2 + \beta \|\mathbf{r}(\pi_u(\mathbf{u}); \pi_z(\mathbf{z}))\|^2$$

后者的优势在于将物理知识直接编码为约束，但 $\beta$ 需要手动调节。

### 3.2 贝叶斯逆问题 (Bayesian Inverse Problems, BIPs)

当需要不确定性量化时，贝叶斯框架提供了原则性方法：

$$p(\mathbf{z}|\mathbf{y}) = \frac{p(\mathbf{y}|\mathbf{z})p(\mathbf{z})}{p(\mathbf{y})}$$

关键对应关系：

| 贝叶斯成分 | 物理含义 | 对应点估计中的角色 |
|-----------|---------|------------------|
| 似然 $p(\mathbf{y}\|\mathbf{z})$ | 正向模型 + 噪声模型 | 数据拟合项 |
| 先验 $p(\mathbf{z})$ | 参数的先验知识 | 正则化项 |
| 后验 $p(\mathbf{z}\|\mathbf{y})$ | 给定数据后参数的完整分布 | 点估计是其 MAP |
| 证据 $p(\mathbf{y})$ | 归一化常数（通常不可解析计算） | — |

证据 $p(\mathbf{y}) = \int p(\mathbf{y}|\mathbf{z})p(\mathbf{z})d\mathbf{z}$ 的不可计算性，正是 VI 和 MCMC 存在的根本原因。

---

## 4. 变分推断的核心推导

这是本文最核心的理论部分。论文从两个不同视角推导了 ELBO，清晰地区分了 **Bayes VI** 和**生成模型 VI** 的差异。

### 4.1 Bayes VI：直接最小化后验 KL

目标是让变分近似 $q_\phi(\mathbf{z})$ 尽可能逼近真实后验 $p(\mathbf{z}|\mathbf{y})$。展开 KL 散度并应用 Bayes 定理：

![KL展开第一步](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-06-equation-01.jpg)

![KL展开结果](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-06-equation-02.jpg)

由于 $\log p(\mathbf{y})$ 不依赖于变分参数 $\phi$，最小化 KL 等价于最小化：

![Bayes VI 目标函数](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-06-equation-03.jpg)

$$J(\phi; \mathbf{y}) := \mathbb{E}_{q_\phi(\mathbf{z})}[-\log p(\mathbf{y}|\mathbf{z})] + D_\text{KL}(q_\phi(\mathbf{z}) \| p(\mathbf{z}))$$

这个目标函数有两个直观成分：
- **负对数似然期望**（数据拟合）：鼓励 $q_\phi$ 集中在能解释数据的参数区域
- **KL 正则化**（先验约束）：防止 $q_\phi$ 偏离先验太远

关键优势：**避开了不可计算的证据 $p(\mathbf{y})$**。

### 4.2 生成模型 VI：ELBO 作为对数证据的下界

当生成模型本身的参数 $\theta$ 也需要学习时（如 VAE），目标是最大化对数边际似然 $\log p_\theta(\mathbf{y})$。通过 Jensen 不等式：

![ELBO 推导 via Jensen 不等式](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-07-equation-01.jpg)

$$\log p_\theta(\mathbf{y}) \geq \mathbb{E}_{q_\phi(\mathbf{z})}[\log p_\theta(\mathbf{y}|\mathbf{z})] - D_\text{KL}(q_\phi(\mathbf{z}) \| p(\mathbf{z})) =: \mathcal{L}(\mathbf{y}; \phi, \theta)$$

### 4.3 两种推导的本质区别

| | Bayes VI (Eq.12) | 生成模型 VI / ELBO (Eq.14) |
|---|---|---|
| 优化变量 | 仅 $\phi$（变分参数） | $\phi$ 和 $\theta$（变分 + 生成模型参数） |
| $\log p(\mathbf{y})$ 的角色 | 不依赖优化变量，是常数 | 依赖 $\theta$，ELBO 只是下界 |
| 优化效果 | 直接最小化后验 KL（精确等价） | 同时拟合生成模型 + 近似后验 |
| 适用场景 | 似然已知，只需近似后验 | 似然本身需要学习（如 VAE） |

这个区分经常被忽略，但在物理问题中至关重要：当正向模型已知时用 Bayes VI；当正向模型需要学习时用 ELBO 框架。

---

## 5. 深度学习参数化：VAE 与 Normalizing Flows

### 5.1 变分自编码器 (Variational Autoencoder, VAE)

VAE 是 ELBO 框架的标准深度学习实现，由两个神经网络组成：

- **编码器 (Encoder)** $q_\phi(\mathbf{z}|\mathbf{y}) = \mathcal{N}(\mathbf{z}; m_\phi(\mathbf{y}), C_\phi(\mathbf{y}))$：将数据映射为潜变量的分布
- **解码器 (Decoder)** $p_\theta(\mathbf{y}|\mathbf{z}) = \mathcal{N}(\mathbf{y}; G_\theta(\mathbf{z}), C_\eta)$：从潜变量生成数据

对 $N$ 个数据点的 ELBO 分解为：

![VAE ELBO 分解](../../pdfs/2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.mineru/hybrid_auto/images/page-07-equation-02.jpg)

$$\log p_\theta(\mathbf{y}^{(1:N)}) \geq \sum_{n=1}^{N} \underbrace{\mathbb{E}_{q_\phi(\mathbf{z}|\mathbf{y}^{(n)})}[\log p_\theta(\mathbf{y}^{(n)}|\mathbf{z})]}_{\text{重构误差}} - \underbrace{D_\text{KL}(q_\phi(\mathbf{z}|\mathbf{y}^{(n)}) \| p(\mathbf{z}))}_{\text{正则化}}$$

### 5.2 重参数化技巧 (Reparameterisation Trick)

训练 VAE 需要对 ELBO 关于 $\phi$ 求梯度，但采样操作 $\mathbf{z} \sim q_\phi(\mathbf{z}|\mathbf{y})$ 不可微。解决方案：

$$\epsilon \sim \mathcal{N}(0, \mathrm{I}), \quad \mathbf{z} = m_\phi(\mathbf{y}) + L_\phi(\mathbf{y}) \odot \epsilon$$

将随机性从参数分离出来，使得梯度可以通过 $m_\phi, L_\phi$ 反向传播。

### 5.3 Normalizing Flows

Normalizing Flows 通过一系列可逆变换 $f_\phi$ 将简单分布（标准高斯）映射为复杂分布：

$$\mathbf{z} = f_\phi(\mathbf{w}), \quad q_\phi(\mathbf{z}) = p(\mathbf{w}) \left|\det \frac{\partial f_\phi^{-1}}{\partial \mathbf{z}}\right|$$

与 VAE 相比：
- 优势：可逆变换，密度可精确计算
- 限制：潜变量维度必须等于数据维度，无法进行降维

条件 Normalizing Flows 可以学习条件分布 $q_\phi(\mathbf{z}|\mathbf{y})$，在物理逆问题中特别有用。

---

## 6. 物理约束的嵌入方式

论文将文献中的方法按物理约束嵌入方式分为两大类，这是全文最有综述价值的部分。

### 6.1 路线一：基于正向模型的方法 (Forward-Model-Based)

**核心思想**：假设正向模型 $G^\dagger$ 可以评估，将其直接嵌入概率生成模型的似然函数中。

#### 6.1.1 有监督 VAE 获取校准后验

**场景**：有正向模型的输入-输出配对数据 $\mathcal{D} = \{(\mathbf{z}^{(n)}, \mathbf{y}^{(n)})\}$。

有监督设置允许使用 **forward KL** $D_\text{KL}(p(\mathbf{z}|\mathbf{y}) \| q_\phi(\mathbf{z}|\mathbf{y}))$——这是 mean-seeking 的，比 VAE 标准使用的 reverse KL（mode-seeking）在逆问题中更合适。对数据分布取平均后，优化目标简化为：

$$\mathbb{E}_{p(\mathbf{y})}[D_\text{KL}(p(\mathbf{z}|\mathbf{y}) \| q_\phi(\mathbf{z}|\mathbf{y}))] = \mathbb{E}_{p(\mathbf{z},\mathbf{y})}[-\log q_\phi(\mathbf{z}|\mathbf{y})]$$

两种具体实现：
- **Conditional Normalizing Flow** [Siahkoohi et al.]：$q_\phi(\mathbf{z}|\mathbf{y})$ 用条件 NF 参数化，训练后通过 $f_{\phi^\star}(\mathbf{w}; \mathbf{y})$ 从标准高斯采样即可得到后验样本
- **物理解码器 VAE** [Goh et al.]：用已知正向模型 $G^\dagger$ 替代 VAE 解码器，结合 Jensen-Shannon 散度在 forward/reverse KL 之间插值

#### 6.1.2 动力学潜空间 (Dynamical Latent Space)

**场景**：时间序列数据 $\mathbf{y}_{1:N}$，潜空间应遵循物理动力学。

[$\varphi$-DVAE, Glyn-Davies et al.] 的核心设计：
- 引入辅助变量 $\mathbf{x}_n$ 作为潜在高斯状态空间模型的伪观测
- 潜变量动力学由物理正向模型驱动：$p(\mathbf{u}_n|\mathbf{u}_{n-1}) = \mathcal{N}(\Psi^\dagger(\mathbf{u}_{n-1}; \mathbf{z}), \sigma_\mathbf{u}^2 \mathrm{I})$
- 变分后验按时间步分解，利用 Kalman Filtering 精确计算 $p(\mathbf{u}_{1:N}|\mathbf{x}_{1:N})$

#### 6.1.3 深度生成先验 (Deep Generative Prior, DGP)

**场景**：参数空间高维，需要正则化。如果有参数的直接观测，可以训练生成模型来学习参数先验。

核心操作：引入低维辅助潜变量 $\mathbf{w}$，训练生成器 $f_\theta: \mathbf{w} \to \mathbf{z}$。反演时在低维 $\mathbf{w}$ 空间优化，天然实现降维正则化。

两种使用方式：
- **点估计** [Lopez-Alvis et al.]：$\mathbf{w}^\star = \arg\min \|G^\dagger \circ f_{\theta^\star}(\mathbf{w}) - \mathbf{y}\|^2 + \beta(\|\mathbf{w}\| - \mu_\chi)^2$
- **贝叶斯** [Xia et al., VI-DGP]：对辅助后验 $p(\mathbf{w}|\mathbf{y})$ 做 VI 近似，然后将样本推过生成器得到参数后验样本

### 6.2 路线二：基于残差的方法 (Residual-Based)

**核心思想**：不需要完整的正向模型求解器，而是通过 PDE 残差构造似然函数。

#### 6.2.1 无数据推断 (Data-Free Inference)

**场景**：没有观测数据，纯粹从物理方程出发学习概率代理模型。

[Zhu et al.] 的关键构造——将 PDE 残差定义为概率似然：

$$p_\beta(\mathbf{u}|\mathbf{z}) \propto \exp(-\beta \|\mathbf{r}(\pi_u(\mathbf{u}), \pi_z(\mathbf{z}))\|_2^2)$$

当 $u_h$ 精确满足 PDE 时残差为零，概率最大。$\beta$ 控制物理约束的"硬度"。

[Vadeboncoeur et al.] 进一步引入**虚拟观测量 (virtual observable)** $\hat{\mathbf{r}} = \mathbf{r} + \epsilon_r$，构建同时学习正向映射和逆映射的双向框架：

$$J(\phi, \theta) = \mathbb{E}_{q_\phi(\mathbf{u}|\mathbf{z})p(\mathbf{z})} \log \frac{p(\hat{\mathbf{r}}=0|\mathbf{u},\mathbf{z}) p_\theta(\mathbf{z}|\mathbf{u}) p(\mathbf{u})}{q_\phi(\mathbf{u}|\mathbf{z}) p(\mathbf{z})}$$

这个目标函数的精妙之处在于：$q_\phi(\mathbf{u}|\mathbf{z})$ 学正向映射的不确定性，$p_\theta(\mathbf{z}|\mathbf{u})$ 学逆映射，两者在同一个 ELBO 中联合优化。

#### 6.2.2 少数据体制 (Small-Data Regime)

**场景**：有少量观测数据 + 已知 PDE 形式。

将似然构造为物理残差与数据的乘积测度：

$$p(\hat{\mathbf{r}}, \mathbf{y}|\mathbf{u}, \mathbf{z}) = p(\hat{\mathbf{r}}=0|\mathbf{u}, \mathbf{z}) \cdot p(\mathbf{y}|\mathbf{u}, \mathbf{z})$$

物理与数据之间的平衡由各自的噪声方差自然决定，不需要手动调节权重。

[Tait & Damoulas] 的方法特别有意思：将正向代理模型 $F_\theta$ 嵌入变分近似的似然中，当物理约束趋于精确（$\epsilon \to 0$）时，优化退化为约束优化问题：

$$\min_{\theta,\phi} \mathbb{E}_{q_\phi(\mathbf{z})}[-\log p(\mathbf{y}|\mathbf{u}=F_\theta(\mathbf{z}))] + D_\text{KL}(q_\phi(\mathbf{z}) \| p(\mathbf{z})) \quad \text{s.t.} \quad \|\mathbf{r}\|_2^2 = 0$$

其他变体包括：
- **PI-VAE** [Zhong & Meidani]：处理随机 PDE 的 VAE 方法
- **PI-GAN** [Yang et al.]：用 GAN 替代 VAE 的生成对抗框架
- **NFF** [Guo et al.]：normalizing field flows，对传感器位置无关的方法

---

## 7. 方法全景对比

| 方法 | 物理嵌入方式 | 数据需求 | 变分近似 | 学习对象 |
|------|-------------|---------|---------|---------|
| Supervised CNF [60] | 正向模型生成训练数据 | 有监督 | Conditional NF | 逆映射后验 |
| 物理解码器 VAE [20] | 正向模型做解码器 | 有监督 | 高斯编码器 | 逆映射后验 |
| $\varphi$-DVAE [19] | 动力学嵌入潜空间 | 时序数据 | 分解式 | 动力学参数后验 |
| DGP 点估计 [40] | 生成先验 + 正向模型 | 参数观测 + 少数据 | — | 点估计 |
| VI-DGP [72] | 生成先验 + 正向模型 | 参数观测 + 少数据 | 辅助变量 VI | 参数后验 |
| 物理残差代理 [79] | PDE 残差似然 | 无数据 | Normalizing Flow | 正向概率代理 |
| 双向 VI [67,68] | 虚拟观测 + 残差 | 无数据 | $q_\phi(\mathbf{u}\|\mathbf{z})$ | 正向+逆向同时 |
| 物理+数据混合 [26] | 残差 + 数据似然 | 少数据 | 均场近似 | 解和参数后验 |
| PDE 约束 VAE [64] | 刚度矩阵信息化协方差 | 少数据 | $q_\phi(\mathbf{u}\|\mathbf{z})q_\phi(\mathbf{z})$ | 正向代理 + 参数后验 |

---

## 8. 不确定性量化的角色

贯穿全文的一条暗线是：**物理问题为什么特别需要 UQ？**

1. **逆问题的 ill-posedness**：当观测稀疏或有噪声时，多组参数可能产生相同的观测。贝叶斯后验自然地捕捉这种不确定性。
2. **代理模型的近似误差**：神经网络代理模型不可能精确等价于原始 PDE 求解器，VI 框架让代理模型能"说出自己不确定的地方"。
3. **多查询场景 (multi-query)**：UQ 方法（如 Monte Carlo）本身就需要多次正向求解。传统数值方法的计算代价使得 UQ 不可行，而 VI 代理模型在训练后可以廉价地进行推断。
4. **数据-物理权衡**：在少数据场景中，物理残差和数据似然的相对权重本质上反映了对两种信息来源的信任程度，VI 框架通过概率建模自然地处理这种权衡。

---

## 9. 核心结论与开放问题

### 结论

1. **VI 在物理推断中的核心价值**：在计算效率与 UQ 精度之间取得了 MCMC 无法达到的平衡。
2. **物理约束的嵌入灵活性**：无论是通过正向模型、PDE 残差还是深度生成先验，VI 框架都能自然地容纳物理知识。
3. **从有监督到无数据的连续谱**：不同方法适用于不同的数据可用性场景，而 VI 框架提供了统一的推导基础。

### 开放问题

1. **VI 不确定性的校准性 (calibration)**：VI 产生的不确定性估计在实践中可能不准确，这既是实际挑战也是理论难题。
2. **代理模型 vs. 经典求解器的性价比**：训练代理模型的成本是否真的低于直接使用数值方法，取决于具体问题。
3. **KL 散度的适定性**：对函数空间上的 KL 散度，可能出现不适定的问题。Wasserstein 距离、Sliced Wasserstein 度量、最大平均差异 (MMD) 等替代散度正在被探索。
4. **先验学习**：如何从数据中学习更好的物理先验，是一个活跃的研究方向。

---

## 10. 个人评注

这篇文章作为 tutorial/review 的定位非常准确。它最大的贡献不是新方法，而是用统一的符号系统（参数-解-观测三空间 + WRM 残差 + ELBO 推导）把近年来零散的 physics-informed VI 工作串联成一个有逻辑的体系。对于想进入这个领域的研究者，我建议的阅读路径是：

1. 先吃透 Section 2.3 的两种 ELBO 推导（Bayes VI vs. 生成模型 VI），理解它们的本质区别
2. 然后根据自己的问题类型（正向/逆向，有数据/无数据）定位到 Section 3 的对应方法
3. 最后关注 Discussion 中关于 KL 散度替代和先验学习的指引
