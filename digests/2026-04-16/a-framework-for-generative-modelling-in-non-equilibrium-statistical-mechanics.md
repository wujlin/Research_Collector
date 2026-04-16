---
title: "A Framework for the Use of Generative Modelling in Non-Equilibrium Statistical Mechanics"
authors: "Karl Friston, Maxwell Ramstead, Dalton Sakthivadivel"
venue: "Proc. R. Soc. A 482(2330), 2026"
date_read: "2026-04-16"
topics: ["自由能原理", "非平衡统计力学", "生成模型", "变分推断", "Lyapunov函数"]
---

# A Framework for the Use of Generative Modelling in Non-Equilibrium Statistical Mechanics

## 精读笔记

---

## 一、问题背景与动机

### 1.1 作者学术地位

本文第一作者 **Karl J. Friston** 是伦敦大学学院（UCL）Queen Square 神经学研究所教授，是**自由能原理（Free Energy Principle, FEP）** 的创始人和核心推动者。Friston 是神经影像学领域的奠基者之一，其开发的 SPM（Statistical Parametric Mapping）软件被全球神经科学界广泛使用。他长期位列全球被引用次数最多的神经科学家之首，其学术影响力跨越神经科学、理论物理、人工智能与哲学多个领域。合作者 **Maxwell Ramstead** 同在 UCL，专注于 FEP 的哲学与概念基础；**Dalton Sakthivadivel** 来自 CUNY 研究生中心数学系，负责 FEP 的数学形式化与动力系统分析。

### 1.2 核心问题：耦合开放系统的建模挑战

物理世界中的系统几乎都不是孤立的——它们通过能量、物质、信息的交换与环境耦合（coupling），形成**开放系统（open systems）** 或**非平衡系统（non-equilibrium systems）**。这类系统的典型特征包括：

- 持续的耗散（dissipation）与驱动（driving）
- 自组织（self-organisation）行为的涌现
- 形态发生（morphogenesis）等复杂动态

传统方法直接求解**随机动力系统（random dynamical systems）** 的耦合方程，但由于系统各部分之间可能存在高度非线性的耦合，这种方法往往面临计算不可处理性（intractability）的困难。

本文的核心提问是：**能否找到一种更简洁、更有解释力的数学框架，用生成模型（generative models）来表示和追踪子系统之间的依赖关系，从而替代对原始耦合动力学方程的直接求解？**

### 1.3 本文定位

本文并非 FEP 的首次提出，而是对 FEP 的一次**回归基础（back to basics）** 的系统阐述，重点强调：

1. FEP 在非平衡统计力学中的**一般性**（而非仅限于神经科学或认知科学）
2. 变分自由能（variational free energy）作为 Lyapunov 函数的技术基础
3. "推断（inference）"解释的**虚构性（as-if）** 特征——澄清地图与疆域（map vs. territory）的关系

---

## 二、生成模型表示子系统间的依赖关系

### 2.1 从统计学到物理学：生成模型的角色

在统计学中，**生成模型（generative model）** 是一个联合概率分布 $p(\eta, b, \mu)$，它编码了不同变量之间的关系——例如观测数据与其隐含原因之间的依赖。对于开放的、相互作用的物理系统，这种统计建模方法尤为贴切。

本文的关键洞见是：用**变分贝叶斯推断（variational Bayesian inference）** 的语言来建模物理对象如何反映其环境的性质——以及环境如何反映物理对象的性质——为科学建模提供了强大的工具。

### 2.2 Markov 毯（Markov Blanket）与特定划分（Particular Partition）

FEP 的形式化依赖于对联合系统状态空间的一个关键分割：

- **内部状态（internal states）** $\mu$：粒子/系统自身的状态
- **外部状态（external states）** $\eta$：环境的状态
- **毯状态（blanket states）** $B$：连接两者的边界变量，包含：
  - **感觉状态（sensory states）**：向系统传递关于环境的信号
  - **主动状态（active states）**：系统对环境的干预

关键条件是：在给定毯状态 $b$ 的情况下，内部状态 $\mu$ 与外部状态 $\eta$ **条件独立**。这种结构被称为 **Markov 毯**（源自 Judea Pearl 的图模型理论）。

这意味着：系统不能直接"看到"环境，只能通过 Markov 毯间接获取信息——一切关于外部世界的推断都必须通过这层边界完成。

### 2.3 依赖关系的信息论含义

存在一个映射函数 $\sigma$，使得 $\sigma(\hat{\mu}_b) = \hat{\eta}_b$（即内部状态的条件期望映射到外部状态的条件期望）。这意味着：

> **通过存在特定方式，系统的内部状态可以被解读为对环境统计属性的一个编码。**

系统在联合状态空间中"占据"某个位置，就等价于它对一个包含整个联合系统的生成模型做了推断。

---

## 三、变分自由能作为 Lyapunov 函数

### 3.1 从 SDE 到梯度流

考虑具有非平衡稳态密度（non-equilibrium steady state density, NESS）$p^*(x)$ 的随机微分方程（SDE）：

$$\mathrm{d}X_t = f(X_t)\,\mathrm{d}t + D(X_t)\,\mathrm{d}W_t$$

该 SDE 可以被分解为如下形式（Helmholtz 分解）：

$$\mathrm{d}X_t = -(Q(X_t) - \Gamma(X_t))\nabla_x \log p^*(X_t)\,\mathrm{d}t + D(X_t)\,\mathrm{d}W_t$$

其中：
- $\Gamma(x)$：正（半）定的耗散矩阵（dissipative），满足 $2\Gamma(x) = D(x)D^\top(x)$
- $Q(x)$：反对称的螺线管矩阵（solenoidal），描述概率流的保守/旋转部分
- $\nabla_x \log p^*(x)$：surprisal 的梯度

这一分解表明：**系统的动力学可以写成在 surprisal（即 $-\log p^*$）梯度上的下降流，只是被旋转场 $Q$ 和噪声所调制。**

### 3.2 引入变分自由能

定义变分自由能（variational free energy）：

$$F(\mu, b) = D_{\mathrm{KL}}(q(\eta; \sigma(\mu)) \| p(\eta \mid b)) - \log p(\mu, b)$$

关键不等式：

$$F(\mu, b) \geq -\log p(\mu, b)$$

等号成立的条件是 KL 散度（KL divergence）为零，即变分密度 $q$ 精确等于后验分布 $p(\eta \mid b)$。

这意味着：**变分自由能是 surprisal 的上界**，最小化自由能同时意味着最小化 surprisal 和最小化推断误差。

### 3.3 Lyapunov 函数的物理意义

变分自由能满足 Lyapunov 函数的定义——它沿（确定性）动力系统的轨迹单调递减，从而保证稳定性。这给我们以下等价描述：

$$\mathrm{d}\mu_t = -(Q - \Gamma)\nabla_\mu F(\mu, b) + \mathrm{d}W_t$$

也就是说，**Markov 毯系统的内部状态动力学可以等价地写成在变分自由能梯度上的下降流**。这一梯度流就是我们所说的"推断过程"——系统的动力学在数学上等价于变分推断。

**要义**：最可能的状态就是最不令人惊讶的状态（the most probable state is the least surprising one）。Surprisal 之所以能担任 Lyapunov 函数，根源在于 Freidlin–Wentzell 大偏差理论——对数概率衡量了系统所有涨落与最可能状态之间的距离。

---

## 四、FEP 的统计力学含义

### 4.1 存在即推断

FEP 反转了通常的因果推理方向：

- **传统思路**：物体因为稳定所以持续存在
- **FEP 思路**：物体因为持续存在（作为那种东西），所以稳定（作为那种东西）

换言之：一个粒子以某种方式存在于环境中，就意味着环境很可能以某种特定方式存在，使得这个粒子"成立"。如果系统的 surprisal 不可约地高，那么它占据的是"不像它自己"的状态——比如鱼离开了水——这在某种意义上意味着它已不再作为那种事物存在。

### 4.2 相干性度量

在"粒子因存在于环境中而建模其环境"这个假设下，自由能隐含地成为了一种**相干性度量（coherence measure）**：

- 如果粒子停止以某种特定方式建模其环境，那么它已经不再以那种方式存在
- 反之，如果粒子不再存在，它就会停止建模环境
- Surprisal 衡量的是：对一个携带模型的观察者来说，发现系统处于非系统典型状态有多"令人惊讶"

### 4.3 与 Jaynes 最大熵方法的类比

正如 Jaynes 提出的"做统计力学就是在做关于微观状态概率的推断"（given knowledge of macrostates），FEP 是**统计物理学作为建模过程**的自然表达。FEP 提供了一种约束：任何对物理事物的模型或映射都必须满足的先决条件。

---

## 五、经验验证：两个仿真实例

### 5.1 细胞形态发生（Cellular Morphogenesis）

**设置**：八个未分化细胞从同一位置出发，通过最小化变分自由能实现迁移和分化。

- 每个细胞的状态包括二维网格位置 $\psi_x$ 和四维信号表达谱 $\psi_c$
- 主动状态 $a_x, a_c$ 对应位置调制和化学信号分泌
- 细胞间通过指数衰减的胞外信号浓度场交互：$\lambda_i(\psi_x, \psi_c) = C\sum_j \psi_{cj} e^{|\psi_{xi} - \psi_{xj}|}$
- 目标形态编码了一个"头-身-尾"结构，不同部位对应不同细胞类型

**生成模型**：通过 softmax 函数让每个细胞推断自己在集合中的身份（identity），并将预期的感觉信号与实际感觉信号之间的预测误差 $\varepsilon_i = s_i - g(\psi)_i$ 作为驱动力。

**结果**：

![Figure 1a: 目标胞外信号梯度场](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-13-figure-01.jpg)

*Figure 1a — 目标胞外梯度场。不同颜色表示不同信号表达，星号标记细胞最终位置。该场编码了目标形态（头、身、尾）的空间信号分布。*

![Figure 1b: 目标信号的二进制编码](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-13-figure-02.jpg)

*Figure 1b — 目标信号在细胞中的二进制编码。可理解为遗传编码（genetic encoding）的类比，表位遗传动力学则被视为主动推断（active inference）。*

![Figure 1c: Softmax 身份推断矩阵](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-13-figure-03.jpg)

*Figure 1c — Softmax 函数返回的后验信念矩阵。每列代表一个细胞，每行代表集合中的一个位置。对角线附近的高亮表示每个细胞对自身身份有较强的信念。*

![Figure 2a: 细胞迁移轨迹](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-14-figure-01.jpg)

*Figure 2a — 细胞位置随时间的演化。颜色（红/黄/绿/蓝）标记细胞分化后的类型，梯度表示信号表达强度。细胞从初始位置（共位）逐渐迁移到目标形态对应的位置。*

![Figure 2b: 自由能随时间下降](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-14-figure-02.jpg)

*Figure 2b — 自由能随时间单调下降。这直接验证了 FEP 的核心预测：细胞在迁移和分化过程中持续最小化变分自由能。*

![Figure 3: 细胞最终空间分布](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-15-figure-01.jpg)

*Figure 3 — 各细胞的完整运动轨迹及最终位置（星号）。最终形态呈现清晰的"头-身-尾"结构，每个细胞通过推断自身身份并按预期行动，"知道自己在更大系统中的位置"。*

**小结**：每个细胞携带一个生成模型，该模型预测"如果我是正确类型的细胞，在正确的位置，我应该感受到什么信号"。系统通过自由能最小化实现自组织——这正是 FEP 作为建模框架的优势所在。

### 5.2 周期性放电细胞（Periodically-Firing Cells）

**设置**：一个由兴奋性细胞组成的环，通过间隙连接（gap junction）耦合。每个细胞的生成模型编码一个周期性目标波形 $s(\mu) = A\cos\mu$。

- 内部状态 $\mu$：细胞相位的估计
- 主动状态 $a$：离子通道门控等执行器
- 先验编码偏好：$p(a \mid \mu) \propto \exp\{-(a - A\cos\mu)^2 / 2\sigma_a^2\}$

与形态发生实例不同，此模型更具表达力——先验是振荡性的，自由能的最小值对应的是**极限环（limit cycle）** 而非不动点。

**关键对比**：论文同时模拟了两种动力学——基于 surprisal 梯度的流（flow on $\mathcal{L}$）和基于自由能梯度的流（flow on $F$）——并进行了直接比较。

![Figure 4: 内部状态相位演化](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-19-figure-01.jpg)

*Figure 4 — 极坐标螺旋图上的内部状态 $\mu_t$ 演化。蓝色：surprisal 梯度流 $\mathcal{L}$；红色：自由能梯度流 $F$。两者在所有时间尺度上显示出优异的一致性，验证了自由能梯度流对原始动力学的忠实近似。*

![Figure 5: 主动状态演化](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-20-figure-01.jpg)

*Figure 5 — 主动状态 $a_t$ 在两种流制下的演化对比。同样呈现高度一致性。*

![Figure 6: KL 散度随时间趋向零](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-20-figure-02.jpg)

*Figure 6 — 自由能流 $F$ 下 KL 散度 $D_{\mathrm{KL}}(q(\eta;\mu) \| p(\eta \mid s,a))$ 的样本均值（N=200）随时间迅速下降并趋向零。这意味着变分密度 $q$ 在推断过程中逐渐逼近真实后验——推断间隙（inference gap）被消除。*

![Figure 7: 两种流制下自由能的比较](../../pdfs/2026-04-16/a-framework-for-the-use-of-generative-modelling-in-non-equilibrium-statistical-mechanics.mineru/hybrid_auto/images/page-21-figure-01.jpg)

*Figure 7 — 自由能的样本均值比较（N=200）。红色（$F$ 流）比蓝色（$\mathcal{L}$ 流）下降更快、达到更低的最小值。这表明：通过加入精度加权预测误差（precision-weighted prediction error）驱动的 KL 项，自由能梯度流在收敛速度和最终精度上优于原始 surprisal 梯度流。*

**神经科学解释**：最小化变分自由能赋予振荡相位以"对环境中预期输入信号的后验信念"的解释，Kalman 式更新则对应为"最小化精度加权预测误差的增益调制"，而非仅仅是极限环上的一个位置。结合随机热力学的关系，还可以对维持这种"信念"的代价做出定量预测。

### 5.3 方法论反思：自上而下 vs. 自下而上

论文坦诚地指出了这两个仿真的方法论局限：

- **已做的（top-down）**：从生成模型和非平衡稳态出发，工程化地构建满足 FEP 的 Langevin 动力学，展示其推断解释
- **未做但理想的（bottom-up）**：从一个独立给定的物理动力学方程出发，(i) 导出其稳态密度和概率流，(ii) 验证是否存在满足分解 (2.1.1) 的 $Q$ 和 $\Gamma$，(iii) 推导出对应的自由能泛函和变分解释

这种"自上而下"的方法不是 FEP 普适性的独立经验检验，而是一个**精心构造的示例（worked example）**——展示了当所需的分解被假设存在时，FEP 形式化的实际样貌。论文的核心贡献在于表明：**只要分解 (2.1.1) 和 Markov 毯存在，就总是可以构造出相应的生成模型和变分密度族，使得物理动力学可以被写成自由能泛函上的下降。**

---

## 六、嵌套模型构建与 FEP 的一般方法论

### 6.1 从原理到模型的生成器

FEP 不是一个特定的模型，而是一个**原理**——类似最小作用量原理（principle of least action）或最大熵原理（maximum entropy principle），它是一台"生产模型的机器"。

应用 FEP 建模的实际步骤：
1. 观察某个"事物"的毯状态（blanket states）——内部状态不可直接观测
2. 推断最能解释观测到的动力学的生成模型
3. 由此获得内部动力学的完整（但不过度完整的）描述

### 6.2 嵌套结构

因为生成模型可以包含多个层次的 Markov 毯（例如细胞 → 组织 → 器官 → 有机体），FEP 天然支持**嵌套模型（nested models）** 的构建。这意味着：

- 在更高层次上，子系统本身被视为"粒子"，其内部状态又可以进一步分解
- 每一层都可以被解读为在追踪其"环境"（即同一层级的其他粒子）的统计性质
- 这与层次化贝叶斯推断（hierarchical Bayesian inference）的结构自然吻合

### 6.3 建模优势

相比直接求解随机动力系统的耦合方程，FEP 框架的优势在于：

| 方面 | 直接求解 SDE | FEP 框架 |
|------|-------------|----------|
| 可处理性 | 非线性耦合导致不可处理 | 自由能梯度是可处理的上界 |
| 解释力 | 动力学描述 | 推断过程的解释 |
| 模型构建 | 需要完整的耦合方程 | 只需指定生成模型和先验 |
| 嵌套结构 | 需要从头构建 | 自然支持层次化分解 |

---

## 七、"解释性虚构"（Explanatory Fiction）的哲学澄清

### 7.1 "如同"（as if）的地位

本文反复强调的核心哲学观点是：

> **说一个物理系统"执行推断"，是一种解释性虚构（explanatory fiction）。**

物理系统不需要真正"计算"其运动轨迹，就像我们不需要假设一个粒子"知道"牛顿定律才能遵循抛物线运动。FEP 提供的是一种 **"如同"描述（as-if description）**：

- 存在一个量（surprisal / 自由能）随系统动力学系统性地变化
- 这个量的最小化在数学上等价于推断（作为统计估计器）
- 但我们**不必须**假设系统本身在字面意义上执行推断

### 7.2 地图-疆域关系的澄清

对 FEP 的一个常见批评是它犯了**模型物化谬误（map-territory fallacy）**——即将科学模型（地图）的属性错误地归于被建模的物理系统（疆域）。本文以一个优雅的框架回应：

**FEP 是"那部分看起来像地图的疆域的地图"（a map of that part of the territory that behaves as if it were a map）。**

具体来说：
- **生成模型** $p(\eta, b, \mu)$：是科学家（建模者）构建的**科学模型**（地图），用于描述联合系统的特征性状态
- **变分密度** $q(\eta; \sigma(\mu))$：是系统内部状态**看起来像在参数化的**关于外部状态的概率密度
- **物理系统本身**：疆域，其动力学独立于我们的描述

这三者之间的关系是：
1. 生成模型是建模者的工具，不是粒子自身"持有"的
2. 变分密度是我们对"系统的内部子集看起来在做什么"的形式化表述
3. FEP 允许我们构建一个"地图"来描述"疆域中看起来像地图的部分"——而不需要声称疆域本身真的在使用地图

### 7.3 Wittgenstein 类比

论文将 FEP 与 Wittgenstein 在《逻辑哲学论》中的工作相类比：

- Wittgenstein 从语言内部划定了有意义命题的界限（什么可以被有意义地说出）
- FEP 从建模过程内部划定了可能的模型/映射关系的界限（什么可以算作对物理过程的模型）

> **任何与物理定律一致的建模过程都必须符合 FEP，因此 FEP 设定了从映射/建模技术内部出发的、关于什么可以算作模型的终极约束。**

### 7.4 "地图-疆域谬误的谬误"

论文进一步论证：声称 FEP 犯了地图-疆域谬误，本身就是一种谬误（the map-territory fallacy fallacy）。因为 FEP 恰恰**区分了**生成模型（我们的科学模型）和变分密度（系统"看起来持有"的信念），从未将两者混为一谈。

---

## 八、核心结论

1. **生成模型 + Markov 毯 → 变分自由能作为 Lyapunov 函数**：对于任何可以划分出 Markov 毯的耦合系统，其内部动力学都可以等价地写成变分自由能梯度上的下降流。这一数学事实使得我们可以用推断的语言来描述物理动力学，获得更高的可处理性和解释力。

2. **FEP 是原理而非模型**：它是生成模型的"元理论"——提供了构建科学模型的原则和约束，而非某个特定系统的具体模型。

3. **推断解释是"虚构的"但有用的**：系统不必须在字面意义上执行推断。这种"如同推断"的描述用更可处理的自由能梯度替代了可能高度非线性的耦合动力学——这是其方法论价值所在。

4. **不存在地图-疆域混淆**：通过仔细区分生成模型（科学家的地图）和变分密度（系统的"类地图"行为），FEP 框架避免了模型物化谬误。

5. **嵌套模型的构建能力**：FEP 使我们能够构建尊重子系统间已知关系的嵌套模型，这对复杂自组织系统的建模尤为重要。

6. **统计力学的新视角**：呼应 Jaynes 的最大熵方法，FEP 将统计物理学重新诠释为一种"制造模型"的过程，为非平衡统计力学提供了一个统一的建模框架。

---

## 九、个人评注与延伸思考

### 9.1 方法论上的诚实

本文难能可贵之处在于其方法论上的坦诚——论文在 §3.3 中明确承认两个仿真是"自上而下"的构造，而非 FEP 普适性的独立检验。真正有说服力的验证应该从一个独立建立的物理模型出发，"自下而上"地导出 FEP 结构。

### 9.2 与随机热力学的连接

论文多次引用了与随机热力学（stochastic thermodynamics）的联系（特别是 Parr et al., 2020），这暗示了一个更深的图景：自由能最小化不仅是推断的数学等价物，还可能与维持非平衡状态的热力学代价直接相关。

### 9.3 开放问题

- **"自下而上"验证**：能否从一个独立的、实验验证过的物理模型出发，严格导出 FEP 结构？
- **$Q$ 和 $\Gamma$ 的存在性条件**：在什么条件下，分解 (2.1.1) 中要求的 $Q(x)$ 和 $\Gamma(x)$ 确实存在？
- **计算复杂性**：对于高维系统，变分自由能的计算和梯度求解是否仍然可处理？
- **与深度学习的桥接**：变分自编码器（VAE）和 FEP 之间的形式关联能否被利用来构建更物理合理的生成模型？

---

## 关键术语索引

| 中文 | 英文 | 简述 |
|------|------|------|
| 自由能原理 | Free Energy Principle (FEP) | 耦合系统内部动力学可被描述为最小化变分自由能 |
| 生成模型 | Generative Model | 联合概率分布 $p(\eta, b, \mu)$，编码变量间依赖关系 |
| 变分自由能 | Variational Free Energy | Surprisal 的可处理上界，作为 Lyapunov 函数 |
| Markov 毯 | Markov Blanket | 使内部/外部状态条件独立的边界变量集 |
| 特定划分 | Particular Partition | 将系统状态空间划分为内部、外部、毯状态 |
| 变分密度 | Variational Density | 用内部状态参数化的关于外部状态的近似后验 |
| KL 散度 | KL Divergence | 度量变分密度与真实后验之间差异的信息论量 |
| Surprisal | Surprisal | $-\log p(\mu, b)$，自信息量 |
| Lyapunov 函数 | Lyapunov Function | 沿动力系统轨迹单调递减的函数，保证稳定性 |
| Helmholtz 分解 | Helmholtz Decomposition | 将漂移项分解为耗散和螺线管分量 |
| 非平衡稳态 | Non-Equilibrium Steady State (NESS) | 有持续概率流但密度不随时间变化的稳态 |
| 主动推断 | Active Inference | 通过行动使观测符合预测的推断框架 |
| 解释性虚构 | Explanatory Fiction | 推断解释的"如同"特征，非字面归属 |
| 地图-疆域谬误 | Map-Territory Fallacy | 将模型属性错误归于被建模系统的逻辑错误 |
