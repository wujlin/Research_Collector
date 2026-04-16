---
title: "Stochastic Thermodynamics for Autoregressive Generative Models"
authors: "Takahiro Sagawa"
venue: "arXiv (2026)"
date_read: "2026-04-16"
topics: ["随机热力学", "自回归模型", "非马尔可夫", "熵产生", "Transformer"]
---

# Stochastic Thermodynamics for Autoregressive Generative Models — 精读笔记

> **论文全称**：Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective  
> **作者**：Takahiro Sagawa（东京大学）  
> **日期**：2026-04-10  

---

## 0 一句话总结

本文为所有 **自回归生成模型**（Transformer / RNN / Kalman filter / SSM / Mamba）建立了统一的 **随机热力学（stochastic thermodynamics）** 框架：定义了非马尔可夫观测序列的 **熵产生（entropy production）**，证明其可从单条采样轨迹高效计算，并在 GPT-2 实验与 Kalman 滤波解析案例中进行了验证和分解。

---

## 1 问题定义：为什么需要非马尔可夫视角

### 1.1 随机热力学的经典局限

随机热力学（stochastic thermodynamics）以 **熵产生** $\mathcal{S}$ 作为量化不可逆性（irreversibility）的核心诊断量，其理论最完善的场景是 **马尔可夫过程**（Markovian processes）。经典的 Crooks 型时间反演（Crooks-type time reversal）为马尔可夫系统提供了清晰的前向/后向路径概率比：

$$
\sigma(y_{1:T}) = \sum_t \ln \frac{p_t(y_{t+1}|y_t)}{p_t(y_t|y_{t+1})}
$$

但当观测过程 $y_t$ 本身是 **非马尔可夫** 的——即当前状态的分布依赖于整段历史而非仅前一步——上述框架便不再直接适用。

### 1.2 自回归生成模型的统一结构

作者的关键洞察是：**所有主流自回归架构** 共享同一个抽象结构——**从确定性隐状态进行随机发射（stochastic emission from deterministic latent state）**：

1. **确定性记忆更新**：$h_t = \Phi_t(y_1, y_2, \ldots, y_t)$  
2. **随机发射**：$y_{t+1} \sim p_t(y_{t+1} | h_t)$

其中 $h_t$ 是对过去观测 $y_{1:t}$ 的有界大小压缩（bounded-size compression），而 $p_t$ 是发射核（emission kernel）。

> **核心约束**：$h_t$ 的维度/状态空间大小不随 $t$ 增长——它必须将不断增长的历史压缩到固定大小的表示中。

![Figure 1(a): 前向过程的因果结构——一般（非递归）情形](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-03-figure-01.jpg)

**图 1(a)**：前向过程的因果结构图。蓝色箭头 $f_t^\rightarrow$ 表示确定性映射（将所有过去观测映射为隐状态），绿色箭头 $p_t$ 表示随机发射。注意每个 $h_t$ 依赖于 **全部** 过去的 $y_1, \ldots, y_t$，这正是非马尔可夫性的来源。

### 1.3 五种架构的统一对照

![Table 1: 各架构与通用框架的对应关系](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-05-table-01.jpg)

| 模型 | 隐状态 $h_t$ | 确定性映射 | 发射核 | 递归？ |
|:---|:---|:---|:---|:---:|
| **Transformer** | 注意力上下文向量 | $\Phi(y_1, \ldots, y_t)$（全序列） | $\text{softmax}(W_{\text{out}} h_t)$ | ✗ |
| **RNN** | RNN 隐状态 | $\phi(h, y) = \tanh(W_h h + W_y y + b)$ | $\text{softmax}(W_{\text{out}} h_t + b_{\text{out}})$ | ✓ |
| **Kalman** | 一步预测 $\hat{x}_{t+1|t}$ | $\phi_t(h, y) = A_t[(I - K_t C_t)h + K_t y]$ | $\mathcal{N}(C_{t+1} h_t, S_{t+1})$ | ✓ |
| **SSM** | SSM 状态 | $\phi_t(h, y) = A_t h + B_t y$ | $\text{softmax}(W_{\text{out}} C_t h_t)$ | ✓ |
| **Mamba** | $(h_t, y_t)$ | $\phi'(h', y) = (A(y)h + B(y)y, \; y)$ | $\text{softmax}(W_{\text{out}} C(y_t) h_t)$ | ✓ |

**关键区别**：
- **Transformer** 是 **非递归** 的——$\Phi$ 访问完整历史，不能化简为 $(h_{t-1}, y_t)$ 的函数，联合过程 $(h_t, y_t)$ **也不是马尔可夫** 的。
- **RNN / Kalman / SSM / Mamba** 是 **递归** 的——$h_t = \phi_t(h_{t-1}, y_t)$，联合过程 $(h_t, y_t)$ 是马尔可夫的，但 $y_t$ 的边缘过程仍然是非马尔可夫的。

---

## 2 构建后向过程与定义熵产生

### 2.1 后向过程：同一机器反向运行

后向过程的构造遵循随机热力学中 Crooks 型协议反转（protocol reversal）的精神：**复用同一套发射核 $p_t$ 和确定性映射 $\Phi_t$，但以反转的时间顺序调用它们**。

具体地，给定前向序列 $y_{1:T}$，后向过程生成 $\tilde{y}_s = y_{T-s+1}$（即时间反转的序列），后向路径概率为：

$$
P_\leftarrow(y_{T:1}) = \prod_{t=1}^{T} p_t\!\left(y_t \;\big|\; g_{t+1}^\leftarrow(y_{T:t+1})\right)
$$

其中 $g_{t+1}^\leftarrow(y_{T:t+1}) \equiv \Phi_{t+1}(y_T, y_{T-1}, \ldots, y_{t+1})$ 是将 **未来序列** 反向输入同一确定性映射得到的隐状态。

![Figure 1(b): 后向过程的因果结构](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-03-figure-02.jpg)

**图 1(b)**：后向过程的因果结构。$g_t^\leftarrow$ 将未来观测映射为后向隐状态 $\tilde{h}_s$。即使对于 $\tilde{y}_s = y_{T-s+1}$ 这一特定实现，一般也 **不成立** $\tilde{h}_s = h_{T-s+1}$——因为同一函数 $\Phi_t$ 作用于反转序列会产生不同的隐状态。

### 2.2 递归情形的图示

![Figure 2(a): 递归前向过程](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-04-figure-01.jpg)

![Figure 2(b): 递归后向过程](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-04-figure-02.jpg)

**图 2**：递归情形下的前向/后向因果结构。蓝色箭头 $\phi_t$ 表示递归更新 $h_t = \phi_t(h_{t-1}, y_t)$，每个隐状态仅依赖前一步隐状态和当前观测——这使联合过程 $(h_t, y_t)$ 成为马尔可夫的。

### 2.3 熵产生的定义

**熵产生**（entropy production）定义为前向和后向路径测度之间的 KL 散度：

$$
\boxed{\mathcal{S}_y = D_{\text{KL}}\!\left(P_\rightarrow(y_{1:T}) \;\|\; P_\leftarrow(y_{T:1})\right) = \mathbb{E}_{P_\rightarrow}\!\left[\ln \frac{P_\rightarrow(y_{1:T})}{P_\leftarrow(y_{T:1})}\right] \geq 0}
$$

其中 **随机熵产生**（stochastic entropy production）为：

$$
\sigma(y_{1:T}) = \ln \frac{P_\rightarrow(y_{1:T})}{P_\leftarrow(y_{T:1})} = \sum_{t=0}^{T-1} \ln p_t(y_{t+1} | f_t^\rightarrow(y_{1:t})) - \sum_{t=1}^{T} \ln p_t(y_t | g_{t+1}^\leftarrow(y_{T:t+1}))
$$

**积分涨落定理**（integral fluctuation theorem）自动成立：$\mathbb{E}_{P_\rightarrow}[e^{-\sigma}] = 1$。

> **物理含义**：$\mathcal{S}_y$ 量化了观测序列 $y_{1:T}$ 在给定自回归模型下的 **时间不可逆性**（temporal irreversibility）。$\mathcal{S}_y = 0$ 当且仅当前向和后向路径概率处处相等。

### 2.4 马尔可夫极限的一致性

当 $y_t$ 本身是马尔可夫过程时（取 $h_t = y_t$），熵产生退化为经典 Crooks 公式：

$$
\mathcal{S}_y = \sum_{t=1}^{T-1} \mathbb{E}\left[\ln \frac{p_t(y_{t+1}|y_t)}{p_t(y_t|y_{t+1})}\right] + \text{边界项}
$$

若进一步假设局部细致平衡（local detailed balance），该项可解释为 $-\beta Q$（逆温度 × 吸收热量）。

---

## 3 计算可行性：为什么没有指数代价

### 3.1 一般非马尔可夫过程的困难

对于来自未知源的非马尔可夫过程，估计条件概率 $P_\rightarrow(y_{t+1} | y_{1:t})$ 需要观察大量共享相同前缀 $y_{1:t}$ 的轨迹——所需样本量随条件历史长度 **组合爆炸**。

### 3.2 自回归框架的结构优势

本框架绕过了这一困难，依赖三个结构性特征：

1. **确定性隐状态**：给定单条轨迹 $y_{1:T}$，所有隐状态 $h_0, h_1, \ldots, h_T$ **唯一确定**，无需随机边缘化。
2. **显式发射核**：$p_t(y_{t+1} | h_t)$ 是模型直接提供的可求值函数（如 Transformer 的 softmax 输出）。
3. **显式边界分布**：前向和后向的初始分布均为已知函数。

因此，每条轨迹的随机熵产生 $\sigma(y_{1:T})$ 只需 **两次前向传播**（一次正向、一次反向输入同一模型）：

$$
C_1 = 2 C_{\text{LL}}
$$

其中 $C_{\text{LL}}$ 是单次对数似然（log-likelihood）评估的代价。对 Transformer 为 $O(T^2)$，对 RNN/SSM/Mamba 为 $O(T)$。

Monte Carlo 估计器：

$$
\mathcal{S}_y \approx \frac{1}{N}\sum_{n=1}^{N} \sigma\!\left(y_{1:T}^{(n)}\right), \quad N = O\!\left(\text{Var}(\sigma) / \epsilon^2\right)
$$

### 3.3 时间粗粒化（temporal coarse-graining）

对语言模型，逐 token 反转（如 "book a is This"）因语法破坏而产生极大的熵产生，掩盖了语义层面的不可逆信号。

**块级反转**（block reversal）提供了更有解释力的替代方案：将序列按句子分块，反转块的顺序但保持块内 token 顺序不变：

$$
\text{token 反转}: (f, e, d, c, b, a); \quad \text{块反转}: (\underbrace{d,e,f}_{B_2}, \underbrace{a,b,c}_{B_1})
$$

对时间齐次模型（time-homogeneous，如 GPT-2），粗粒化随机熵产生定义为：

$$
\sigma'(y_{1:T}) = \ln P(y_{1:T}) - \ln P(\tilde{y}_{1:\tilde{T}}')
$$

即原始文本与块反转文本在 **同一模型** 下的对数似然之差。这仍满足涨落定理 $\mathbb{E}[e^{-\sigma'}] = 1$，且计算代价与 token 级相同。

---

## 4 GPT-2 概念验证实验

### 4.1 Monte Carlo 采样实验（Section 5.1）

**设置**：从 GPT-2（117M 参数）以温度 $\tau = 1$ 自回归采样 $T = 120$ 个 token 的序列，收集 $N \approx 500$ 条轨迹。

![Figure 3(a): Token 级熵产生分布](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-15-figure-01.jpg)

![Figure 3(b): Block 级熵产生分布](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-15-figure-02.jpg)

**图 3** 的关键发现：

| 度量 | 每 token 均值 | 解释 |
|:---|:---:|:---|
| $\sigma_{\text{token}} / T$ | **≈ 3.99** | Token 级反转：极高，因语法破坏 |
| $\sigma_{\text{block}} / T'$ | **≈ 0.469** | 块级反转：低一个数量级，更有解释力 |

**结论**：Token 级熵产生被语法破坏的 artifact 主导，而块级熵产生可能提取更具物理/语义意义的不可逆信号。

### 4.2 因果 vs. 非因果文本实验（Section 5.2）

用 Claude Opus 4.6 生成两组各 30 条文本：
- **因果文本**（causal）：句子描述时间有序的因果链（如"杯子滑落 → 摔碎 → 扫地"）
- **非因果文本**（non-causal）：独立事实陈述，顺序无关（如"小提琴用弓拉 → 长笛用气吹 → ..."）

![Figure 4(a): Token 级 — 因果 vs. 非因果](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-16-figure-01.jpg)

![Figure 4(b): Block 级 — 因果 vs. 非因果](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-16-figure-02.jpg)

**图 4** 的关键发现：

- **Token 级**（图 4a）：因果与非因果文本 **无显著差异**（$p = 0.78$），被语法 artifact 主导。
- **Block 级**（图 4b）：因果文本的 $\sigma_{\text{block}}/T$ **显著高于** 非因果文本（Mann-Whitney $U = 746$, $p = 4.5 \times 10^{-6}$, $r = 0.66$）。

> **物理直觉**：因果文本反转句子顺序后，"效果先于原因"会使反向路径概率大幅下降，导致更大的熵产生。非因果文本句子顺序无关紧要，反转后概率变化小。

---

## 5 Kalman 滤波解析案例

### 5.1 设置

考虑线性高斯系统：

$$
x_{t+1} = Ax_t + w_t, \quad y_t = Cx_t + v_t
$$

其中 $w_t \sim \mathcal{N}(0, Q)$, $v_t \sim \mathcal{N}(0, R)$。真实状态 $x_t$ **不出现在框架中**——Kalman 滤波器被视为一个 **生成模型**，隐状态 $h_t = \hat{x}_{t+1|t}$ 是一步预测估计。

在稳态 Kalman 滤波器的创新表示（innovation representation）下，前向路径概率为：

$$
P_\rightarrow(y_{1:T}) = \prod_{t=1}^{T} \mathcal{N}(e_t; 0, S), \quad e_t = y_t - C\hat{x}_{t|t-1}
$$

其中 $S = CPC^\top + R$ 是创新协方差，$e_t$ 是互相独立的高斯创新（innovation）。

### 5.2 创新反转矩阵（Innovation Reversal Matrix）

这是本文的优美数学贡献之一。定义：
- $\mathcal{H}$：块下三角脉冲响应矩阵，$\mathbf{y} = \mathcal{H}\mathbf{e}$
- $J$：时间反转置换矩阵，$J\mathbf{y} = (y_T^\top, \ldots, y_1^\top)^\top$

则后向创新 $\mathbf{e}^B = \mathcal{R}\mathbf{e}$，其中 **创新反转矩阵** 为：

$$
\boxed{\mathcal{R} \equiv \mathcal{H}^{-1} J \mathcal{H}}
$$

### 5.3 解析熵产生

$$
\boxed{\mathcal{S}_y = D_{\text{KL}}(P_\rightarrow \| P_\leftarrow) = \frac{1}{2}\left[\text{tr}\!\left((I_T \otimes S^{-1})\,\mathcal{R}\,(I_T \otimes S)\,\mathcal{R}^\top\right) - Tn_y\right]}
$$

等价地，用后向创新的协方差表示：

$$
\mathcal{S}_y = \frac{1}{2}\sum_{s=1}^{T}\left[\mathbb{E}_{P_\rightarrow}\!\left[(e_s^B)^\top S^{-1} e_s^B\right] - n_y\right]
$$

> **操作含义**：后向创新 $e_s^B$ 在前向测度下的协方差 $\Sigma_s^B$ 偏离 $S$ 的程度，累积起来就是总熵产生。

### 5.4 标量与多变量的渐近行为

- **标量情形**（$n_x = n_y = 1$）：任何平稳标量高斯过程都是时间可逆的，熵产生 $\mathcal{S}_y$ 在 $T \to \infty$ 时 **饱和** 到有限值（纯粹是初始条件的边界效应）。
- **多变量情形**（$n_y > 1$）：当交叉协方差矩阵不对称时，过程具有真正的时间不可逆性，$\mathcal{S}_y$ 随 $T$ **线性增长**。

### 5.5 数值验证

![Figure 5(a): 标量 Kalman — 解析 vs. Monte Carlo](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-23-figure-01.jpg)

![Figure 5(b): 多变量 Kalman — 解析 vs. Monte Carlo](../../pdfs/2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models-a-non-markovian-perspective.mineru/hybrid_auto/images/page-23-figure-02.jpg)

**图 5**：$N = 20{,}000$ 条轨迹的 Monte Carlo 估计（蓝色点 ± 标准误差）与解析表达式（黑色曲线）的对比。两者在 $T = 5, 10, \ldots, 50$ 的全部范围内高度吻合，验证了理论的正确性。

---

## 6 熵产生的回顾性分解（Retrospective Decomposition）

这是本文最深刻的理论结果之一。

### 6.1 逐步分解

利用贝叶斯回顾推断（Bayesian retrodiction），熵产生可精确分解为 **非负逐步贡献**：

$$
\boxed{\mathcal{S}_y = \sum_{t=1}^{T} \mathcal{D}_t, \quad \mathcal{D}_t \geq 0}
$$

其中：

$$
\mathcal{D}_t = \mathbb{E}_{y_{t+1:T}}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | y_{t+1:T}) \;\big\|\; p_t(y_t | g_{t+1}^\leftarrow(y_{T:t+1}))\right)\right]
$$

**含义**：$\mathcal{D}_t$ 衡量的是，在给定未来 $y_{t+1:T}$ 时，**贝叶斯回顾分布**（真正的后验 $P_\rightarrow(y_t | y_{t+1:T})$）与 **协议反转后向模型**（$p_t(y_t | g_{t+1}^\leftarrow)$）之间的差距。

> 一个直观的日常例子：  
> 前向："如果我不学习，妈妈就会生气。"  
> 贝叶斯回顾："如果妈妈生气了，那说明我没学习。"（大概率为真）  
> 协议反转后向："如果妈妈生气了，然后我就不学习了。"（在日常生活中大概率为假）  
> 两者的差距正是 $\mathcal{D}_t$，在这个例子中很大——高度不可逆。

### 6.2 压缩损失 + 模型失配

每个 $\mathcal{D}_t$ 可进一步精确分解为两个非负项：

$$
\boxed{\mathcal{D}_t = \underbrace{\mathcal{L}_t}_{\text{压缩损失}} + \underbrace{\mathcal{M}_t}_{\text{模型失配}}}
$$

**压缩损失**（compression loss）：

$$
\mathcal{L}_t = I_{P_\rightarrow}\!\left(y_t;\, y_{t+1:T} \;\big|\; g_{t+1}^\leftarrow\right) \geq 0
$$

即将完整未来 $y_{t+1:T}$ 压缩为有限维隐状态 $g_{t+1}^\leftarrow$ 时，关于 $y_t$ 的信息损失。这是后向模型有限记忆容量的代价。

**模型失配**（model mismatch）：

$$
\mathcal{M}_t = \mathbb{E}_{g_{t+1}^\leftarrow}\!\left[D_{\text{KL}}\!\left(P_\rightarrow(y_t | g_{t+1}^\leftarrow) \;\big\|\; p_t(y_t | g_{t+1}^\leftarrow)\right)\right] \geq 0
$$

即在已知后向隐状态 $g_{t+1}^\leftarrow$ 时，**真正的回顾分布** $P_\rightarrow(y_t | g_{t+1}^\leftarrow)$ 与 **直接复用的前向发射核** $p_t(y_t | g_{t+1}^\leftarrow)$ 之间的差距。

> **与变分推断的类比**：这一分解在形式上类似于 ELBO gap 分解（evidence lower bound），其中信息损失项和分布失配项分别出现。但起点完全不同：ELBO 分解来自似然下界，而本文的分解来自 **时间反演与熵产生**。

### 6.3 精炼第二定律（Refined Second Law）

结合压缩损失分解和互信息链式法则，得到熵产生的下界：

$$
\boxed{\mathcal{S}_y \geq \sum_{t=1}^{T}\left[I_{P_\rightarrow}\!\left(y_t;\, f_{t-1}^\rightarrow(y_{1:t-1})\right) - I_{P_\rightarrow}\!\left(y_t;\, g_{t+1}^\leftarrow(y_{T:t+1})\right)\right] \geq 0}
$$

**解读**：熵产生的下界由 **前向隐状态携带的预测信息** 与 **后向隐状态携带的回顾信息** 之间的差距决定。前向总结保留了关于 $y_t$ 的全部预测信息（因为它是充分统计量），而后向总结一般会丢失一些——这种不对称性正是不可逆性的来源之一。

---

## 7 核心结论与方法论意义

### 7.1 主要贡献总结

| 贡献 | 内容 |
|:---|:---|
| **统一框架** | 将 Transformer、RNN、Kalman、SSM、Mamba 纳入同一自回归生成模型类 |
| **熵产生定义** | 通过 Crooks 型时间反演定义非马尔可夫过程的 $\mathcal{S}_y$ |
| **计算可行性** | $O(T^2)$（Transformer）或 $O(T)$（递归模型）× $N$ 条轨迹，无指数代价 |
| **时间粗粒化** | 块级反转提取更有解释力的语义不可逆信号 |
| **GPT-2 验证** | 块级熵产生可区分因果 / 非因果文本 |
| **Kalman 解析解** | 创新反转矩阵 $\mathcal{R}$ 给出闭合表达式 |
| **回顾性分解** | $\mathcal{S}_y = \sum_t (\mathcal{L}_t + \mathcal{M}_t)$，精确分解为压缩损失与模型失配 |
| **精炼第二定律** | 熵产生 ≥ 前向/后向预测信息差 |

### 7.2 与扩散模型的关系

- 扩散模型（diffusion models）中的逆过程对应于 **贝叶斯回顾**（概率分布本身的时间反演），而非协议反转。
- 两者之间的差距恰好由熵产生衡量——这与本文的 $\mathcal{D}_t$ 分解中回顾分布 vs. 协议反转后向模型的差距完全一致。

### 7.3 重要的开放问题

1. **更大规模 LLM**：将框架应用于 GPT-4 等更大模型，但面临语义粗粒化的挑战（同一语义内容可由多种 token 序列表达）。
2. **有限时间权衡关系**：是否存在类似热力学不确定性关系（thermodynamic uncertainty relations）的速度-精度-不可逆性权衡？
3. **回顾性分解的估计**：$\mathcal{D}_t$、$\mathcal{L}_t$、$\mathcal{M}_t$ 的计算需要贝叶斯回顾分布 $P_\rightarrow(y_t | y_{t+1:T})$，目前不可直接从自回归模型获得，可能需要训练专门的逆向模型。
4. **因果推断**：区分真正的因果依赖、时间排序和话语结构惯例对熵产生的贡献。

---

## 8 个人评注

### 亮点
- **概念桥梁的优雅性**：将统计物理中熵产生的深刻概念与 AI 中最核心的 Transformer 架构连接起来，概念框架极其清晰。
- **"一石五鸟"的统一性**：Table 1 的五种架构对照令人赏心悦目，一个框架覆盖了从经典控制论到现代 LLM 的全部谱系。
- **可计算性的核心洞察**：确定性隐状态 + 显式发射核 = 可高效计算的非马尔可夫熵产生。这一观察本身就具有方法论价值。
- **块级粗粒化**：优雅地解决了 token 级反转的语法 artifact 问题，且保持了涨落定理的有效性。

### 局限
- GPT-2 实验仅为 proof-of-concept，序列长度 $T = 120$，模型规模有限。
- 因果/非因果文本由 LLM 生成，分类标准依赖于 prompt 而非形式化定义。
- 回顾性分解的各项（$\mathcal{L}_t$, $\mathcal{M}_t$）目前无法从模型直接计算。

### 可能的后续方向
- 对比不同训练阶段的 LLM 的熵产生变化，可能揭示训练过程中的不可逆性学习。
- 将粗粒化推广到语义级别（如使用句子嵌入而非 token 序列），构建"语义熵产生"。
- 探索熵产生与模型泛化能力、幻觉（hallucination）之间的关系。

---

## 附录：符号速查表

| 符号 | 含义 |
|:---|:---|
| $y_t$ | 观测变量（token 或测量值）|
| $h_t$ | 确定性隐状态（latent state）|
| $\Phi_t$ / $\phi_t$ | 确定性映射（一般/递归） |
| $p_t(y_{t+1} \| h_t)$ | 发射核（emission kernel）|
| $f_t^\rightarrow(y_{1:t})$ | 前向隐状态映射 |
| $g_{t+1}^\leftarrow(y_{T:t+1})$ | 后向隐状态映射 |
| $P_\rightarrow$, $P_\leftarrow$ | 前向/后向路径概率 |
| $\sigma(y_{1:T})$ | 随机熵产生（stochastic entropy production）|
| $\mathcal{S}_y$ | 熵产生（entropy production）= $\mathbb{E}[\sigma]$ |
| $\mathcal{D}_t$ | 逐步回顾性贡献 |
| $\mathcal{L}_t$ | 压缩损失（compression loss）|
| $\mathcal{M}_t$ | 模型失配（model mismatch）|
| $\mathcal{R}$ | 创新反转矩阵（innovation reversal matrix）|
| $S$ | 创新协方差（innovation covariance）|
| $K$ | Kalman 增益（Kalman gain）|
