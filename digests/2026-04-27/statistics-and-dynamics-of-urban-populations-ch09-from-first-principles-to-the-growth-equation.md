---
title: "Statistics and Dynamics of Urban Populations, Chapter 9: From first principles to the growth equation"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-27"
topics: ["urban growth", "migration", "bottom-up model", "gravity model", "Levy noise", "generalized central limit theorem", "stochastic growth equation"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/09-from-first-principles-to-the-growth-equation.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 9：From First Principles to the Growth Equation

## 精读笔记

---

## 一、这一章在全书动力学线里的位置

Chapter 9 是前面几章的汇合点。

Chapter 6 说明，很多经典 city growth models 是从 Zipf's law 出发的：模型是否有效，常常取决于它能不能生成一个 Pareto/Zipf stationary distribution。Chapter 7 把 migration 加入模型，说明城市不是孤立增长，而是通过人口流动耦合在一起。Chapter 8 则补了 generalized central limit theorem，说明如果 migration shocks 有 heavy tail，那么许多 shocks 加总以后不会变成 Gaussian，而会变成 Levy stable noise。

Chapter 9 的任务是把这些线索合成一个 bottom-up growth equation。它不再从“怎样生成 Zipf”开始，而是从人口守恒和迁移流数据开始，逐步推出城市人口的 stochastic equation。

这一章的主线可以写成：

$$
\begin{aligned}
&\text{Zipf-first modeling is insufficient}\\
&\rightarrow \text{decompose city growth}\\
&\rightarrow \text{out-of-system growth is Gaussian}\\
&\rightarrow \text{interurban migration is a directed weighted graph}\\
&\rightarrow \text{flows are size-dependent but very noisy}\\
&\rightarrow \text{net migration shocks are heavy-tailed}\\
&\rightarrow \text{generalized CLT gives Levy noise}\\
&\rightarrow \text{final growth equation}.
\end{aligned}
$$

最终得到的核心方程是：

$$
\frac{\partial S_i}{\partial t}
=
\eta_i S_i
+
D S_i^\beta\zeta_i.
$$

这一章要解释的是：这个式子里的每一项从哪里来，为什么第一项是 Gaussian multiplicative noise，为什么第二项是 Levy-type migration noise，以及为什么 migration noise 的幅度是 $S_i^\beta$ 而不是简单的 $S_i$。

### 1.1 本章符号口径

Chapter 9 是全书符号最容易混淆的一章，因为它同时包含 graph、gravity model、generalized CLT 和最终 stochastic equation。

$S_i$ 表示城市 $i$ 的 population size。没有下标的 $S$ 只在概念解释里表示代表性城市规模。

$J_{i\to j}$ 表示从城市 $i$ 到城市 $j$ 的 total migration flow。$I_{ji}=J_{i\to j}/S_i$ 表示从 $i$ 到 $j$ 的 per-capita migration rate。这里第二个下标对应 origin city，这是原文记号里最容易读反的地方。

$N(i)$ 表示城市 $i$ 的 migration neighbor set，$\mathcal{N}(i)=|N(i)|$ 表示 neighbor number。$\mathcal{N}(i)$ 来自二值化后的 support graph，只数“有多少个迁移联系”，不数每条边上的迁移人数。

$\mu,\nu,\sigma$ 只在 gravity model 中使用：$\mu$ 是 origin-size exponent，$\nu$ 是 destination-size exponent，$\sigma$ 是 distance exponent。这里的 $\mu$ 不是 Chapter 10 中 generic fractional equation 的 Levy index。

$\alpha$ 表示 pairwise net migration shock 的 tail exponent，也是 Levy stable index。这个 $\alpha$ 继承自 Chapter 8 的 generalized CLT。

$\gamma$ 表示 neighbor number 对城市规模的 scaling exponent，即 $\mathcal{N}(i)\propto S_i^\gamma$。它不是 Chapter 6 的 growth factor $\gamma_i(t)$。

$\beta$ 表示最终 migration shock amplitude 的 size exponent：

$$
\beta=\nu+\frac{\gamma}{\alpha}.
$$

它不是 Chapter 8 stable law 的 skewness parameter。

$\eta_i$ 是 Gaussian out-of-system growth noise，$\zeta_i$ 是 city-level Levy migration noise。$\zeta_i$ 不是单条 pairwise flow 的 residual，而是许多 $X_{ij}$ 经过 generalized CLT 聚合后的 normalized shock。

---

## 二、为什么不能继续从 Zipf's law 出发

这一节是全章的动机。作者先批评一种常见建模路径：先把 Zipf's law 当成城市系统的核心事实，再构造一个能生成 Zipf 的增长模型。

这个路径的问题有两层。

第一，Zipf's law 本身不是稳定的 universal law。Chapter 3 已经说明，Zipf exponent 会随国家、时期、城市定义和拟合方法改变。因此，能生成 Zipf 不能作为模型正确性的充分证据。

第二，Zipf's law 描述的是 stationary population distribution，而不是 temporal dynamics。它回答的是：

$$
\text{城市规模在某一时刻如何分布?}
$$

但它没有回答：

$$
\text{一个城市为什么会在一段时间里突然增长、停滞、衰落或被另一个城市超过?}
$$

作者认为，真正缺失的是一个同时解释两类现象的模型：

$$
\text{stationary hierarchy}
\quad
\text{and}
\quad
\text{city-level temporal instability}.
$$

这就是 Chapter 9 所说的 paradigm shift。城市增长模型不能只为了复现 Zipf's law，而要从更基本的人口流动机制出发。

---

## 三、Eq. 9.1：把城市增长拆成两个来源

这一节开始建立 bottom-up equation。作者先不做复杂假设，只写人口变化的会计恒等式。

对城市 $i$，人口规模记为：

$$
S_i.
$$

它的增长可以分成两大部分。

第一部分是 out-of-system growth：

$$
\text{natural growth}
+
\text{migrations out of the city system}.
$$

第二部分是 interurban migrations：

$$
\text{migrations within the city system}.
$$

作者写成：

$$
\partial_t S_i
=
\underbrace{
\text{Natural growth + Migrations out of }\{S_i\}
}_{\text{out-of-system growth}}
+
\underbrace{
\text{Migrations within }\{S_i\}
}_{\text{interurban migrations}}.
\tag{9.1}
$$

这里的 $\{S_i\}$ 是被纳入研究的城市系统，例如一个国家内的一组 metropolitan areas。

为什么要这样拆？因为不同来源的统计性质不同。

out-of-system growth 包括出生、死亡、国际迁移、以及城市和 hinterland 之间的交换。它不是城市系统内部的重新分配。

interurban migrations 则是在城市系统内部发生的人口流动。一个城市的流入往往对应另一个城市的流出，因此它天然具有 network structure。

所以 Eq. 9.1 不是一个经验模型，而是一个组织框架。它先把增长问题分成两个可以分别测量的对象：

$$
\partial_t S_i
=
\text{external-like growth}
+
\text{internal redistribution}.
$$

下一步，作者分别研究这两项的统计形式。

---

## 四、out-of-system growth：为什么写成 Gaussian multiplicative noise

这一节回答 Eq. 9.1 的第一项如何建模。

作者把 out-of-system growth 定义为两类来源的合并：

$$
\text{births and deaths}
+
\text{migration outside the selected city system}.
$$

这里的 outside 包括国际迁移，也包括和 hinterland 的交换。hinterland 可以理解为没有进入 $\{S_i\}$ 这组 metropolitan areas 的小城市、乡镇、乡村或外部区域。

作者认为，在当代成熟城市系统中，这部分通常不是主导项。以美国 2013-2017 年为例，跨 metropolitan areas 的迁移超过 900 万人，而国外迁入约 130 万，来自美国其余区域约 150 万。也就是说，城市系统内部迁移更大。

但这并不意味着 out-of-system growth 可以直接删掉。它仍然提供城市自身的 baseline growth。因此作者把它写成：

$$
\eta_i S_i.
$$

这里 $\eta_i$ 是 city-specific growth rate noise。它乘以 $S_i$，因为这部分增长仍然是比例式的：

$$
\text{same growth rate}
\Rightarrow
\text{larger city gets larger absolute change}.
$$

经验上，这个 growth rate 近似服从 normal law。

![Fig. 9.1 France out-of-system growth](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-03-figure-01.jpg)

![Fig. 9.1 US out-of-system growth](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-03-figure-02.jpg)

Fig. 9.1 的作用是支撑这个建模选择。France 和 US 的 out-of-system growth histogram 都围绕 0 附近集中，并用 normal law 做近似。US panel 的分布更宽，France panel 更尖，但作者的建模结论是相同的：这一项可以用 Gaussian Langevin noise 表示。

这一步和后面的 migration noise 形成对比：

$$
\text{out-of-system growth}
\rightarrow
\text{Gaussian noise},
$$

而

$$
\text{interurban migration}
\rightarrow
\text{heavy-tailed Levy noise}.
$$

这也是全章的第一条关键分工：不是所有噪声都一样。不同增长来源有不同的统计分布。

---

## 五、为什么 mature city system 需要 interurban migration model

作者接着把这个分解和 Haran-Vining 的观点联系起来。

如果一个城市系统还处在 developing stage，出生显著超过死亡，rural-to-urban migration 也很强，那么 out-of-system growth 会很重要。此时城市系统仍然在从外部大量吸收人口，Simon-style growth model 仍有解释力。

但在 mature city system 中，出生和死亡接近，hinterland inflow 也较低。此时城市增长更像是：

$$
\text{people move between cities}
\quad
\text{rather than}
\quad
\text{new people enter the city system}.
$$

这会改变模型问题。我们不能只问：

$$
\text{新增人口如何选择城市?}
$$

而要问：

$$
\text{城市之间的迁移网络如何产生城市增长冲击?}
$$

因此下一节转向 interurban migration graph。

---

## 六、把 interurban migration 写成 directed weighted graph

这一节回答 Eq. 9.1 第二项如何被数据化。

作者使用四个国家的 migration datasets：

$$
\text{US 2012-2017},
\quad
\text{France 2003-2008},
\quad
\text{UK 2012-2016},
\quad
\text{Canada 2012-2016}.
$$

城市是 graph vertices。城市 $i$ 到城市 $j$ 的迁移流记为：

$$
J_{i\to j}.
$$

这个 graph 是 directed，因为 $i\to j$ 和 $j\to i$ 是不同方向；也是 weighted，因为 edge weight 是迁移人数。

但后面会同时用到这个网络的两个层次。

第一个层次是 weighted directed flow network。这里每条边的权重就是实际迁移人数：

$$
J_{i\to j}.
$$

这个层次保留了方向和大小。后面讨论 pairwise migration rate、net flow、heavy-tailed shock 时，用的就是这个加权信息。

第二个层次是 binary support network。这里不关心一条边上有多少人迁移，只关心这条迁移联系是否存在。可以定义：

$$
A_{i\to j}
=
\mathbf{1}\{J_{i\to j}>0\}.
$$

如果 $A_{i\to j}=1$，说明从 $i$ 到 $j$ 至少观察到一条迁移联系；如果 $A_{i\to j}=0$，说明这个方向上没有观察到迁移联系。

neighbor number $\mathcal{N}(i)$ 用的是第二个层次，也就是二值化后的 support，而不是 edge weight。换句话说，$\mathcal{N}(i)$ 数的是“城市 $i$ 和多少个城市发生迁移联系”，不是“迁移了多少人”。

如果至少有一个人从 $i$ 移到 $j$，或者从 $j$ 移到 $i$，就说两座城市是 neighbors。

由于 graph 有方向，作者区分两个概念。

in-neighbors of city $i$：

$$
\text{cities from which people move into }i.
$$

out-neighbors of city $i$：

$$
\text{cities to which people move out of }i.
$$

记为：

$$
\mathcal{N}_{in}(i),
\qquad
\mathcal{N}_{out}(i).
$$

Fig. 9.2 展示 $\mathcal{N}_{in}(i)$ 和 $\mathcal{N}_{out}(i)$ 的关系。

![Fig. 9.2 France in-neighbors vs out-neighbors](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-05-figure-01.jpg)

![Fig. 9.2 US in-neighbors vs out-neighbors](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-05-figure-02.jpg)

图中的虚线是 $y=x$。France 和 US 的点云大体围绕这条线，说明一个城市有多少 out-neighbors，通常也有相近数量的 in-neighbors。这个结果并不是说每条边上的流量相等，而是说城市的迁移联系数在入向和出向上大致平衡。

Table 9.1 用归一化差异进一步支持这个判断：

$$
\frac{
\mathcal{N}_{out}(i)-\mathcal{N}_{in}(i)
}{
\max(\mathcal{N}_{out}(i),\mathcal{N}_{in}(i))
}.
$$

| Dataset | Mean | Variance |
|---|---:|---:|
| France | 4% | 5% |
| US | 0.3% | 5% |

mean 接近 0，说明入向邻居数和出向邻居数没有系统性偏离。于是作者定义平均 neighbor number：

$$
\mathcal{N}(i)
=
\frac{
\mathcal{N}_{out}(i)+\mathcal{N}_{in}(i)
}{2}.
\tag{9.2}
$$

这一步的作用是把 directed graph 的两个 degree 合并成一个 effective number of migration partners。后面要对 $j\in N(i)$ 求和，所以必须知道城市 $i$ 大概连接多少个迁移邻居。

---

## 七、Eq. 9.3：城市越大，migration neighbors 越多，但不是线性增长

有了 $\mathcal{N}(i)$，下一步要看它如何随城市规模变化。

直觉上，大城市应该有更多 migration connections。作者把这个关系写成 power law：

$$
\mathcal{N}(i)
\propto
S_i^\gamma.
\tag{9.3}
$$

Fig. 9.3 给出 France 和 US 的拟合。

![Fig. 9.3 France neighbor scaling](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-05-figure-03.jpg)

![Fig. 9.3 US neighbor scaling](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-05-figure-04.jpg)

France 的估计是：

$$
\gamma\simeq0.55,
$$

US 的估计是：

$$
\gamma\simeq0.34.
$$

UK 和 Canada 的 dataset 较小，且二值化后的 migration support graph 几乎 fully connected，因此作者取：

$$
\gamma=0.
$$

这里需要展开，否则 $\gamma=0$ 很容易被误读成“UK 和 Canada 的大城市并不会连接更多城市”。作者的意思更技术一些。

$\gamma$ 衡量的是 neighbor number 对城市规模的 scaling elasticity：

$$
\mathcal{N}(i)
\propto
S_i^\gamma.
$$

如果二值化后的 migration support graph 还没有饱和，那么小城市通常只和少数城市有迁移联系，大城市会和更多城市有迁移联系，这时可以从 $\mathcal{N}(i)$ 和 $S_i$ 的 log-log slope 估计 $\gamma$。

但 support graph fully connected 的情况不同。设一个国家样本里共有 $L$ 个城市。对任意城市 $i$，它最多只能连接 $L-1$ 个其他城市：

$$
\mathcal{N}(i)
\le
L-1.
$$

如果二值化后的 support graph 几乎 fully connected，那么大多数城市的 $\mathcal{N}(i)$ 都已经接近这个上限。此时 neighbor number 不再随 $S_i$ 明显变化，而是被样本边界卡住：

$$
\mathcal{N}(i)
\approx
L-1
\quad
\text{for most cities}.
$$

这相当于把 $\mathcal{N}(i)$ 当成常数。常数可以写成：

$$
\mathcal{N}(i)
\propto
S_i^0.
$$

所以作者取 $\gamma=0$。它不是一个强机制结论，而是一个数据处理上的近似：在 UK 和 Canada 的小样本、近饱和 support network 里，neighbor number 的规模依赖无法可靠识别，因此暂时不让这一项贡献额外的 size exponent。

$\gamma<1$ 的物理意义很重要。它说明 migration neighbor number 随人口增加而增加，但增加是 sublinear 的。

如果 $\gamma=1$，城市规模翻倍，迁移邻居数也翻倍。如果 $\gamma<1$，城市规模翻倍，迁移邻居数增加不到一倍。这意味着大城市确实更 connected，但连接数不会和人口规模同比例增长。

这个 scaling 会在后面直接进入 final exponent：

$$
\beta
=
\nu+\frac{\gamma}{\alpha}.
$$

原因是：城市 $i$ 的 net migration 是对 $\mathcal{N}(i)$ 个 heavy-tailed shocks 求和，而 heavy-tailed sum 的尺度是：

$$
\mathcal{N}(i)^{1/\alpha}.
$$

所以 $\mathcal{N}(i)\propto S_i^\gamma$ 会给 migration amplitude 带来额外的：

$$
S_i^{\gamma/\alpha}.
$$

---

## 八、Eq. 9.4：一般的人口平衡方程

现在作者把 out-of-system growth 和 interurban migration graph 合并起来，得到：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right).
\tag{9.4}
$$

这条方程逐项读。

第一项：

$$
\eta_iS_i
$$

是 out-of-system growth。$\eta_i$ 是 growth rate，所以它乘以当前城市规模 $S_i$。

第二项：

$$
\sum_{j\in N(i)}J_{j\to i}
$$

是所有邻居城市流入 $i$ 的人口。

第三项：

$$
\sum_{j\in N(i)}J_{i\to j}
$$

是从 $i$ 流出到所有邻居城市的人口。

所以 migration contribution 是：

$$
\text{incoming flows}
-
\text{outgoing flows}.
$$

Eq. 9.4 和 Chapter 7 的 Bouchaud-Mezard equation 很接近。区别是：这里作者不先假设一个简单 mean-field migration term，而是保留真实 pairwise flows $J_{i\to j}$，然后再从数据中简化它。

如果每一对城市都精确满足：

$$
J_{i\to j}=J_{j\to i},
$$

那么 migration sum 为 0，Eq. 9.4 退化成：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i.
$$

这就是 continuous Gibrat model，会导向 lognormal population distribution。

但真实数据的关键不是平均迁移流是否接近平衡，而是 pairwise fluctuations 是否巨大。作者后面会证明：即使 average flow and counterflow 平衡，实际 net migration shocks 仍然是 heavy-tailed，而且足以改变城市增长方程的噪声类型。

---

## 九、先测试 gravity model：迁移流是否主要由城市规模和距离解释

这一节回答一个建模选择：在 Eq. 9.4 里，$J_{i\to j}$ 应该用什么形式近似？

人类迁移和交通流常用 gravity model：

$$
J_{i\to j}
=
I_0
\frac{
S_i^\mu S_j^\nu
}{
d_{ij}^\sigma
}.
\tag{9.5}
$$

这里：

$$
S_i
$$

是 origin city population；

$$
S_j
$$

是 destination city population；

$$
d_{ij}
$$

是地理距离；

$$
\mu,\nu,\sigma
$$

是需要拟合的 exponents；

$$
I_0
$$

是 prefactor。

这个模型的直觉是：

$$
\text{large origin}
\rightarrow
\text{more people available to leave},
$$

$$
\text{large destination}
\rightarrow
\text{more attractive destination},
$$

$$
\text{longer distance}
\rightarrow
\text{migration friction}.
$$

作者的目标不是证明 gravity model 最好，而是判断哪些因素必须保留。于是他们比较两个模型。

full gravity model：

$$
J_{i\to j}
=
I_0
\frac{S_i^\mu S_j^\nu}{d_{ij}^\sigma}.
$$

distance-free model：

$$
J_{i\to j}
=
I_0S_i^\mu S_j^\nu.
$$

Table 9.2 给出 log-linear regression 的结果：

| Dataset | $I_0$ | $\mu$ | $\nu$ | $\sigma$ | $R^2$ |
|---|---:|---:|---:|---:|---:|
| US flows, distance included | $1.6\cdot10^{-2}$ | 0.46 | 0.44 | 0.53 | 0.42 |
| US flows, no distance | $3.8\cdot10^{-3}$ | 0.38 | 0.37 | / | 0.34 |
| France flows, distance included | $3.7\cdot10^{-3}$ | 0.49 | 0.49 | 0.54 | 0.45 |
| France flows, no distance | $4.3\cdot10^{-4}$ | 0.45 | 0.45 | / | 0.38 |

结果有三点。

第一，France 和 US 的 $\mu,\nu,\sigma$ 很接近。$\mu$ 和 $\nu$ 都在 0.4-0.5 附近，$\sigma$ 在 0.5 附近。

第二，distance 确实提高了 $R^2$，但提高幅度不大。US 从 0.34 到 0.42，France 从 0.38 到 0.45。

第三，即使加入 distance，$R^2$ 也只有 0.4 左右。这说明 migration flows 的 dispersion 很大，城市规模和距离只能解释其中一部分。

作者由此做出一个建模选择：distance 不是完全无关，但它不是最关键的 first-order factor。为了得到更 parsimonious 和更 universal 的模型，可以把 distance 和其他未观测因素一起吸收到 noise 里。

这一步非常重要。它不是说：

$$
\text{distance has no effect}.
$$

而是说：

$$
\text{distance effect is treated as part of flow noise}.
$$

于是 migration flow 的平均结构保留 population dependence，而剩余巨大波动交给随机变量处理。

---

## 十、minimal migration model：从平均流量到 average detailed balance

这一节开始推 Eq. 9.6-Eq. 9.8。目标是把 gravity model 简化成一个 symmetric average flow structure。

先写平均迁移流：

$$
\langle J_{i\to j}\rangle
=
I_0S_i^\mu S_j^\nu.
$$

这里的 $\langle\cdot\rangle$ 表示对 flow noise 的平均。也就是说，$I_0S_i^\mu S_j^\nu$ 不是每一条边的实际流量，而是给定 origin/destination sizes 后的平均趋势。

为了研究 flow direction，作者定义 per-capita migration rate。需要注意记号方向：$I_{ji}$ 表示从 $i$ 到 $j$ 的 per-capita rate：

$$
I_{ji}
=
\frac{J_{i\to j}}{S_i}.
$$

也就是说，第二个下标对应 origin city，分母是 origin population。

在平均意义下：

$$
\langle I_{ji}\rangle
=
\frac{\langle J_{i\to j}\rangle}{S_i}
=
I_0S_i^{\mu-1}S_j^\nu.
$$

同理，从 $j$ 到 $i$ 的 per-capita rate 是：

$$
\langle I_{ij}\rangle
=
\frac{\langle J_{j\to i}\rangle}{S_j}
=
I_0S_j^{\mu-1}S_i^\nu.
$$

取二者比值：

$$
\frac{I_{ij}}{I_{ji}}
=
\frac{
I_0S_j^{\mu-1}S_i^\nu
}{
I_0S_i^{\mu-1}S_j^\nu
}.
$$

消去 $I_0$ 后：

$$
\frac{I_{ij}}{I_{ji}}
=
S_i^{\nu-\mu+1}
S_j^{\mu-1-\nu}.
$$

把它写成 population ratio：

$$
\frac{I_{ij}}{I_{ji}}
=
\left(
\frac{S_i}{S_j}
\right)^{1-\mu+\nu}.
\tag{9.6}
$$

Eq. 9.6 的作用是把一个 migration-rate asymmetry 问题转成一个 scaling exponent 问题。

Fig. 9.4 左侧 panels 显示：

$$
\frac{I_{ij}}{I_{ji}}
\quad
\text{versus}
\quad
\frac{S_i}{S_j}
$$

近似是 exponent 1 的 power law。

![Fig. 9.4 France rate ratio](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-08-figure-01.jpg)

![Fig. 9.4 US rate ratio](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-08-figure-03.jpg)

经验上：

$$
1-\mu+\nu
\simeq
1.
$$

因此：

$$
\mu\simeq\nu.
$$

这一步带来一个重要结论。若 $\mu=\nu$，则平均 flow 变成：

$$
\langle J_{i\to j}\rangle
=
I_0S_i^\nu S_j^\nu.
\tag{9.7}
$$

这个式子关于 $i$ 和 $j$ 对称。因此：

$$
\langle J_{i\to j}\rangle
=
\langle J_{j\to i}\rangle.
$$

这就是 average detailed balance。它的意思不是每一对城市实际流量相等，而是：

$$
\text{conditioned on city sizes, mean flow and mean counterflow balance}.
$$

进一步，per-capita rate 的平均形式变成：

$$
\langle I_{ij}\rangle
=
I_0S_i^\nu S_j^{\nu-1}.
\tag{9.8}
$$

这里 $I_{ij}$ 是从 $j$ 到 $i$ 的 per-capita rate，所以分母是 $S_j$：

$$
\langle I_{ij}\rangle
=
\frac{\langle J_{j\to i}\rangle}{S_j}
=
\frac{I_0S_j^\nu S_i^\nu}{S_j}
=
I_0S_i^\nu S_j^{\nu-1}.
$$

作者估计得到：

$$
\nu\simeq0.4
$$

in France and US，但误差很大。这一点会在后面变得重要：平均结构是相对清楚的，但围绕平均结构的 fluctuations 很大。

---

## 十一、为什么 average detailed balance 仍然不够

上一节得到 average detailed balance：

$$
\langle J_{i\to j}\rangle
=
\langle J_{j\to i}\rangle.
$$

如果只停在这里，很容易误解为 migration term 可以忽略。因为平均流入和平均流出相等，似乎：

$$
\sum_j(J_{j\to i}-J_{i\to j})
\approx
0.
$$

但作者强调：这只在 average 上成立，真实 fluctuations 非常大。（**这里能否联系上熵产生的不等式？**）

换句话说，migration 的核心不是 mean，而是 deviation from mean。城市增长真正受到冲击的部分是：

$$
\text{actual flow}
-
\text{average flow}.
$$

这也是 Chapter 9 的关键转折：模型不是用 mean migration flow 决定城市命运，而是用 heavy-tailed migration fluctuations 解释城市动态的不稳定性。

---

## 十二、Eq. 9.9：把 migration rate 写成平均结构乘以噪声

为了表示这些大波动，作者写：

$$
I_{ij}
=
I_0S_i^\nu S_j^{\nu-1}x_{ij}.
\tag{9.9}
$$

这里 $x_{ij}$ 是随机变量，满足：

$$
\mathbb{E}(x_{ij})=1.
$$

它把所有没有被平均结构解释的因素都吸收进去，包括：

$$
\text{distance},
\quad
\text{regional context},
\quad
\text{institutional effects},
\quad
\text{unobserved social/economic factors},
\quad
\text{measurement-level heterogeneity}.
$$

所以 Eq. 9.9 的逻辑是：

$$
\text{migration rate}
=
\text{population-based mean trend}
\times
\text{random multiplier}.
$$

这里的 $x_{ij}$ 可以被直觉地看成 residual，但它和普通 regression residual 的角色不同。

在普通回归里，residual 常常被当成模型没有解释掉的小误差。模型的主要内容在 fitted mean 里，residual 最好是无结构的、均值接近 0、方差有限，并且不会改变主要结论。

这里不是这样。作者先用 $I_0S_i^\nu S_j^{\nu-1}$ 抓住 pairwise migration rate 的平均规模关系，然后把真实流量相对这个平均关系的偏离写进 $x_{ij}$。因此 $x_{ij}$ 表示的是：

$$
x_{ij}
=
\frac{
\text{actual migration rate}
}{
\text{population-based mean migration rate}
}.
$$

如果 $x_{ij}\approx1$，说明这一对城市的迁移流接近平均结构；如果 $x_{ij}\gg1$，说明这一对城市之间存在远大于平均趋势的迁移联系；如果 $x_{ij}\ll1$，说明这对城市虽然按人口规模预测应有迁移流，但实际联系很弱。

所以 $x_{ij}$ 不是可以被忽略的噪声尾巴。它正是后面 heavy-tail 进入模型的入口。城市 $i$ 的 total net migration 不是由一个 residual 决定，而是由很多 pairwise fluctuations 加总：

$$
\sum_{j\in N(i)}
\left(
J_{j\to i}
-
J_{i\to j}
\right).
$$

如果这些 pairwise fluctuations 的分布很宽，少数特别大的 $x_{ij}$ 或 pairwise net flows 就可能主导这个 sum。这样，residual 不再只是拟合误差，而会变成城市层面的 heavy-tailed net migration shock。

---

## 十三、定义 $X_{ij}$：把 pairwise net migration 变成可加随机变量

为了把 Eq. 9.4 的 migration sum 化简，作者定义：

$$
X_{ij}
=
\frac{
J_{j\to i}-J_{i\to j}
}{
I_0S_i^\nu
}.
$$

这个定义的目的，是把城市 $i$ 的 size-dependent prefactor $I_0S_i^\nu$ 提出来。

从定义直接得到：

$$
J_{j\to i}-J_{i\to j}
=
I_0S_i^\nu X_{ij}.
$$

对所有 migration neighbors 求和：

$$
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right)
=
I_0S_i^\nu
\sum_{j\in N(i)}X_{ij}.
\tag{9.10}
$$

这一步非常关键。它把 migration contribution 拆成两部分。

第一部分：

$$
I_0S_i^\nu
$$

是城市 $i$ 自身规模带来的平均迁移强度尺度。

第二部分：

$$
\sum_{j\in N(i)}X_{ij}
$$

是来自所有邻居的 net migration shocks 加总。

接下来问题就变成：这个 sum 服从什么分布？

---

## 十四、Fig. 9.5：$X_{ij}$ 的右尾是 heavy-tailed

作者观察 $X_{ij}$ 的经验分布，尤其是右尾：

$$
X_{ij}^+
\quad
\text{where}
\quad
X_{ij}>0.
$$

Fig. 9.5 显示这些正向 net migration shocks 的 density 具有 power-law tail：

$$
\rho(X)
\sim
X^{-1-\alpha},
\qquad
\alpha<2.
$$

![Fig. 9.5 France right-tail density of positive net migration shocks](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-09-figure-01.jpg)

这张图的作用不是只说“尾部厚”，而是为 Chapter 8 的 generalized CLT 提供触发条件。只要：

$$
\alpha<2,
$$

variance diverges，ordinary CLT 的 Gaussian limit 就不再适用。

这意味着 migration sum：

$$
\sum_{j\in N(i)}X_{ij}
$$

不能用：

$$
\sqrt{\mathcal{N}(i)}
\times
\text{Gaussian noise}
$$

来表示，而应该用：

$$
\mathcal{N}(i)^{1/\alpha}
\times
\text{Levy stable noise}.
$$

这就是 Chapter 8 在 Chapter 9 中的具体用法。

---

## 十五、Eq. 9.11：用 generalized CLT 得到 Levy migration noise

假设 $X_{ij}$ 之间的相关性可以忽略，Chapter 8 的 generalized CLT 给出：

$$
\zeta_i
=
\frac{1}{
|N(i)|^{1/\alpha}
}
\sum_{j\in N(i)}X_{ij}.
\tag{9.11}
$$

这一步可以拆开读。

第一，$|N(i)|$ 是城市 $i$ 的 migration neighbors 数量。记：

$$
n_i
=
|N(i)|.
$$

那么 Eq. 9.10 里的随机部分就是 $n_i$ 个 pairwise net shocks 的和：

$$
\sum_{j\in N(i)}X_{ij}.
$$

第二，如果这些 $X_{ij}$ 是 finite-variance random variables，普通 CLT 会告诉我们：$n_i$ 个 shocks 加总后的典型波动尺度是 $\sqrt{n_i}$。原因是 variance 可以相加：

$$
\operatorname{Var}\left(
\sum_{j=1}^{n_i}X_{ij}
\right)
\sim
n_i,
\qquad
\text{standard deviation}
\sim
n_i^{1/2}.
$$

这时合理的标准化是除以 $n_i^{1/2}$，标准化后的变量会趋向 Gaussian。

第三，Fig. 9.5 给出的经验事实不是 finite variance，而是 heavy tail：

$$
\rho(X)
\sim
X^{-1-\alpha},
\qquad
\alpha<2.
$$

当 $\alpha<2$ 时，variance 不再是稳定的尺度量。加总的波动不再由大量小 shocks 平均出来，而可能由少数极大的 pairwise shocks 主导。因此标准化尺度从普通 CLT 的 $n_i^{1/2}$ 变成 generalized CLT 的 $n_i^{1/\alpha}$。

第四，Eq. 9.11 正是在做这个标准化：

$$
\zeta_i
=
\frac{
\text{sum of pairwise net shocks around city }i
}{
\text{heavy-tail aggregation scale}
}
=
\frac{
\sum_{j\in N(i)}X_{ij}
}{
n_i^{1/\alpha}
}.
$$

所以 $\zeta_i$ 不是某一条 pairwise flow 的噪声，而是城市 $i$ 周围所有 pairwise shocks 加总后、按 generalized CLT 重新缩放得到的 city-level migration noise。generalized CLT 说，在相关性可以忽略、tail exponent 相同的近似下，这个 normalized aggregate shock follows a Levy stable law $L_\alpha$。

这句话的结构要反过来读。Eq. 9.11 等价于：

$$
\sum_{j\in N(i)}X_{ij}
=
|N(i)|^{1/\alpha}\zeta_i.
$$

这就是 heavy-tailed sum 的 scaling。

ordinary CLT 会给：

$$
\sum_{j=1}^{n}X_j
\sim
n^{1/2}\eta.
$$

generalized CLT 给：

$$
\sum_{j=1}^{n}X_j
\sim
n^{1/\alpha}\zeta_\alpha.
$$

因为这里：

$$
\alpha<2,
$$

所以：

$$
\frac{1}{\alpha}
>
\frac{1}{2}.
$$

也就是说，migration shocks 的 aggregate fluctuation 随 neighbor number 增长得比 Gaussian case 更快。

Fig. 9.4 右侧 panels 对比了 renormalized migration flows $\zeta_i$ 的 empirical cumulative tail、Levy stable law 和 normal law。

![Fig. 9.4 France renormalized migration shock tail](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-08-figure-02.jpg)

![Fig. 9.4 US renormalized migration shock tail](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/09-from-first-principles-to-the-growth-equation.mineru/hybrid_auto/images/page-08-figure-04.jpg)

图中 normal law 的 tail 下降得太快，无法描述 empirical tail；Levy stable law 更接近经验曲线。这个证据支撑了本章的核心建模选择：

$$
\text{interurban migration noise is not Gaussian}.
$$

Table 9.3 给出 $\alpha$ 的估计：

| Dataset | MLE | Kolmogorov-Smirnov | Log-moments | Hill |
|---|---:|---:|---:|---:|
| France 2003-2008 | $1.43\pm0.07$ | $1.2<\alpha<1.8$ | 1.3 | $1.4\pm0.3$ |
| US 2013-2017 | $1.76\pm0.07$ | $1.7<\alpha<1.8$ | 1.6 | Inconclusive |
| UK 2012-2016 | $1.32\pm0.26$ | Inconclusive | 1.0 | $1.2\pm0.8$ |
| Canada 2012-2016 | $1.69\pm0.12$ | Inconclusive | 1.9 | $1.4\pm0.6$ |

这些估计不完全一致，但共同点是：

$$
\alpha<2.
$$

这就是模型需要 Levy noise 的关键经验条件。

---

## 十六、Eq. 9.12-Eq. 9.13：把 migration sum 代回 growth equation

现在把 Eq. 9.10 和 Eq. 9.11 代回 Eq. 9.4。

Eq. 9.4 是：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right).
$$

Eq. 9.10 给出：

$$
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right)
=
I_0S_i^\nu
\sum_{j\in N(i)}X_{ij}.
$$

Eq. 9.11 给出：

$$
\sum_{j\in N(i)}X_{ij}
=
|N(i)|^{1/\alpha}\zeta_i.
$$

因此：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
D S_i^\nu
|N(i)|^{1/\alpha}\zeta_i.
\tag{9.12}
$$

这里 $D\propto I_0$，把 prefactor absorb 进一个常数。

接下来用 Eq. 9.3。这里 $|N(i)|$ 是城市 $i$ 的 migration neighbor number，也就是前面的 $\mathcal{N}(i)$：

$$
|N(i)|
\propto
S_i^\gamma.
$$

于是：

$$
|N(i)|^{1/\alpha}
\propto
\left(S_i^\gamma\right)^{1/\alpha}
=
S_i^{\gamma/\alpha}.
$$

代回 Eq. 9.12：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
D S_i^\nu
S_i^{\gamma/\alpha}
\zeta_i.
\tag{9.13}
$$

合并幂次：

$$
S_i^\nu S_i^{\gamma/\alpha}
=
S_i^{\nu+\gamma/\alpha}.
$$

所以 migration noise amplitude 的 size exponent 是：

$$
\beta
=
\nu+\frac{\gamma}{\alpha}.
$$

这一步是全章最重要的推导之一。最终 exponent $\beta$ 不是直接拟合出来的纯经验参数，而是由三类机制共同决定：

$$
\nu:
\text{pairwise migration flow 对城市规模的依赖},
$$

$$
\gamma:
\text{migration neighbor number 对城市规模的依赖},
$$

$$
\alpha:
\text{migration shock tail thickness}.
$$

---

## 十七、Eq. 9.14：最终的 city growth equation

作者把 Eq. 9.13 写成紧凑形式：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
D S_i^\beta\zeta_i.
\tag{9.14}
$$

其中：

$$
\beta
=
\nu+\frac{\gamma}{\alpha}.
$$

这条方程有两个噪声项。

第一项：

$$
\eta_iS_i
$$

是 out-of-system growth noise。$\eta_i$ 是 Gaussian noise，有平均增长率 $r$ 和 dispersion $\sigma$。它对应出生死亡、外部迁移和 hinterland exchange 的合并效果。

第二项：

$$
D S_i^\beta\zeta_i
$$

是 interurban migration noise。$\zeta_i$ 是 Levy stable noise，来自许多 pairwise net migration shocks 的 generalized-CLT aggregation。

这两个项都具有 multiplicative structure，但含义不同。

$\eta_iS_i$ 是 standard proportional growth。它表示同样的外部增长率作用在更大城市上，会产生更大的 absolute change。

$D S_i^\beta\zeta_i$ 是 state-dependent migration shock amplitude。它不只是“城市越大，流动越大”，还包含大城市有更多 migration partners、且 migration shocks heavy-tailed 这两个机制。

如果 $\beta=1$，migration shock amplitude 与城市规模线性成比例；如果 $\beta<1$，migration shock amplitude 随城市规模 sublinear 增长。Table 9.4 的估计大多在 0.5-1 附近，说明 migration volatility 随城市规模增加，但不一定完全按比例增加。

---

## 十八、用 $\beta$ 的 measured value 检查模型

作者不仅从机制预测：

$$
\beta
=
\nu+\frac{\gamma}{\alpha},
$$

也直接对 total net migration 进行 log-linear regression：

$$
\left|
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right)
\right|
\propto
S_i^\beta.
$$

然后比较 predicted $\beta$ 和 measured $\beta$。

Table 9.4 给出：

| Dataset | $\gamma$ | $\nu$ | $\beta=\nu+\gamma/\alpha$ | $\beta$ measured |
|---|---:|---:|---:|---:|
| France 2003-2008 | $0.55\pm0.06$ | $0.4\pm0.3$ | $0.8\pm0.4$ | $0.79\pm0.07$ |
| US 2013-2017 | $0.34\pm0.05$ | $0.4\pm0.4$ | $0.6\pm0.5$ | $0.96\pm0.05$ |
| UK 2012-2016 | 0 | $0.7\pm0.3$ | $0.7\pm0.3$ | $0.51\pm0.05$ |
| Canada 2012-2016 | 0 | $0.5\pm0.4$ | $0.5\pm0.4$ | $0.78\pm0.06$ |

这里的 comparison 不是直接看 $\beta$ 的数值漂亮不漂亮，而是看两条独立路径是否给出相近结果。

第一条路径是 mechanism-based prediction。它先分别估计：

$$
\alpha,\quad \gamma,\quad \nu,
$$

再通过机制公式合成：

$$
\beta_{\text{pred}}
=
\nu+\frac{\gamma}{\alpha}.
$$

第二条路径是 direct measurement。它不拆机制，而是直接把 total net migration amplitude 对城市规模做 scaling fit：

$$
\left|
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right)
\right|
\propto
S_i^{\beta_{\text{measured}}}.
$$

如果 $\beta_{\text{pred}}$ 和 $\beta_{\text{measured}}$ 接近，说明前面的机制分解至少没有明显错位。France 的情况最清楚：预测值 $0.8\pm0.4$ 和直接测得的 $0.79\pm0.07$ 很接近。US 的点估计差得更明显，但 $\nu$ 的不确定性很大，所以作者仍然认为它没有直接推翻机制公式。

UK 和 Canada 的解释更弱一些。这里不应该简单说“噪声更大”，因为这容易和 Eq. 9.14 里的 stochastic migration noise 混在一起。更准确地说，是 $\beta_{\text{pred}}$ 的机制识别更不充分，估计不确定性更大。

原因有两个。

第一，UK 和 Canada 的 dataset 较小，并且二值化后的 migration support graph 近乎 fully connected。此时 neighbor-number scaling 无法可靠估计，作者只能取：

$$
\gamma=0.
$$

一旦取 $\gamma=0$，公式里的 neighbor-number contribution 被完全拿掉：

$$
\beta
=
\nu.
$$

也就是说，模型只能依靠 pairwise flow amplitude 的 size scaling，即 $\nu$，来解释总 migration shock 的规模依赖。原本 $\beta$ 有两部分来源：

$$
\beta
=
\underbrace{\nu}_{\text{pairwise flow amplitude}}
+
\underbrace{\frac{\gamma}{\alpha}}_{\text{number of partners plus heavy-tail aggregation}}.
$$

但在 UK 和 Canada 的处理里，第二项被设成 0，于是模型少检验了一条机制通道。

第二，support graph fully connected 不等于真实迁移机制没有网络结构，也不等于每条边的权重都一样。它只说明这个数据切片已经无法用“连接数量随城市规模增加”来区分城市。原本机制链是：

$$
\begin{aligned}
&\text{larger city}\\
&\rightarrow \text{more migration partners}\\
&\rightarrow \text{more heavy-tailed pairwise shocks to aggregate}\\
&\rightarrow \text{larger net migration amplitude}.
\end{aligned}
$$

但在 support graph 近 fully connected 的样本里，第二步已经饱和。每个城市都几乎连接到所有其他城市，所以城市之间的差异主要不再来自“有多少个 partners”，而来自“每条 pairwise flow 有多大”。这时 $\gamma=0$ 应该被读成一个饱和 support network 下的保守设定，而不是一个稳定的经验规律。

因此，France 和 US 的价值在于它们至少能分别估计 $\alpha,\gamma,\nu$，再检查合成出来的 $\beta$ 是否接近直接测量值。UK 和 Canada 的价值更多是提供补充样本，但由于 $\gamma$ 无法识别，它们对完整机制链的检验力度较弱。

这里的重点不是每个国家都精确命中，而是模型给出了一条可检验的机制链：

$$
\alpha,\gamma,\nu
\quad
\Rightarrow
\quad
\beta.
$$

这比直接拟合一个 $\beta$ 更强，因为它把 final growth equation 的 size exponent 分解成可观测的中间机制。

---

## 十九、Eq. 9.15：检查不同城市之间的 noise correlations

到目前为止，推导 Eq. 9.14 用了一个重要简化：不同城市的 noises 近似不相关。

作者承认这显然是现实的简化。比如如果人口从城市 $a$ 流向城市 $b$，那么 $a$ 和 $b$ 的 migration shocks 在真实系统里不可能完全独立。

但他们需要判断：作为 first approximation，能不能忽略这种 correlation？

数据日期太少，无法可靠估计 temporal correlations。因此作者采用标准 white-noise 假设：

$$
\langle\eta_i(t)\eta_j(t')\rangle
\propto
\delta(t-t'),
$$

并且对 $\zeta$ 也假设不同时间不相关。

可检查的是 same-time cross-city correlations。作者定义：

$$
\rho
=
\frac{
\langle\eta_i\eta_j\rangle_{i\neq j}
-
\langle\eta_i\rangle\langle\eta_j\rangle
}{
\langle\eta_i\rangle\langle\eta_j\rangle
}.
\tag{9.15}
$$

用样本形式写：

$$
\rho
=
\frac{
\sum_{i\neq j}(\eta_i\eta_j)/N
-
\left(\sum_i\eta_i/N\right)^2
}{
\left(\sum_i\eta_i/N\right)^2
}.
$$

这里 $N$ 是城市数。

France 的估计：

$$
\rho_\eta\simeq\frac{1}{100},
\qquad
\rho_\zeta\simeq\frac{1}{100}.
$$

US 的估计：

$$
\rho_\eta\simeq\frac{5}{1000},
\qquad
\rho_\zeta\simeq\frac{6}{100}.
$$

这些值都较低，因此作者认为 first approach 中可以忽略 cross-city correlations。

这一步的作用是为 decoupled city equations 提供经验辩护。也就是说，Eq. 9.14 可以先被看成每个城市一条方程：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
DS_i^\beta\zeta_i,
$$

而不是一个必须显式写出所有城市联合噪声协方差矩阵的高维系统。

---

## 二十、Itô 还是 Stratonovich：为什么作者倾向 Itô

作者最后指出，Eq. 9.14 中两个噪声都是 multiplicative：

$$
\eta_iS_i,
\qquad
DS_i^\beta\zeta_i.
$$

因此从 Chapter 5 的角度看，stochastic prescription 是一个真实问题。对 multiplicative noise，不同 prescription 会导致不同的 drift correction。

作者认为这里 Itô convention 更合适。理由是：人口 $S_i(t)$ 是在时间 $t$ 的状态，而 interurban migration terms 是在下一段时间 $t+dt$ 中发生或统计出来的。也就是说，noise increment 不应该用时间步中点的已经受冲击状态来解释，而更像用冲击发生前的状态 $S_i(t)$ 来乘以随机增量。

用直观语言说：

$$
\text{migration shock during }[t,t+dt]
\quad
\text{acts on population observed at }t.
$$

这对应 Itô 的 left-point interpretation。

这和 Chapter 7 的 Bouchaud-Mezard Stratonovich 写法不同。Chapter 7 更像连续 exchange process 中的 state-dependent diffusion；Chapter 9 则强调迁移数据是在离散时间段内统计的 flows，因此使用 pre-shock population 更自然。

---

## 二十一、这一章的核心贡献：Gaussian noise 被 Levy migration noise 取代

作者最后总结：Eq. 9.14 是 large urban populations 的 growth equation。

它和 Gibrat-style model 的根本差别是，城市增长不再只有：

$$
\eta_iS_i.
$$

而是：

$$
\eta_iS_i
+
DS_i^\beta\zeta_i.
$$

第一项仍然是 Gaussian proportional growth；第二项是 heavy-tailed migration shock。

这个改变是 quantitative 的，因为它改变了 noise distribution、scaling exponent 和 variance structure。

但它也是 qualitative 的，因为 heavy-tailed noise 会改变城市动态的叙事。ordinary Gaussian noise 表示很多小冲击的平均结果；Levy noise 表示少数巨大冲击可以主导结果。

用 Chapter 8 的语言：

$$
X_{N+1}
\sim
S_N
$$

在 heavy-tail 情况下是可能的。翻译成城市语言就是：

$$
\text{a single migration wave can be comparable to a city's typical population change}.
$$

因此，一个城市的命运不一定由持续的小增长率累积决定，也可能被一次或少数几次大规模迁移波显著改变。

这正是作者所说的 paradigm shift：

$$
\text{from Zipf-generating growth models}
\rightarrow
\text{migration-shock-driven growth dynamics}.
$$

---

## 二十二、和前面章节的关系

Chapter 6 的重点是：哪些 stochastic growth mechanisms 能生成 power-law 或 Zipf-like distribution。那些模型常常从 stationary distribution 出发，机制解释相对薄。

Chapter 7 加入 migration，说明 redistribution 可以 regularize multiplicative growth，并产生 stationary power-law。但 Bouchaud-Mezard model 仍然高度抽象，migration term 不是从真实 pairwise flow distribution 推出来的。

Chapter 8 提供 generalized CLT，说明 broad distribution 的 sums 会走向 Levy stable laws，而不是 Gaussian。

Chapter 9 把这三条线合起来：

$$
\begin{aligned}
&\text{migration data}\\
&\rightarrow \text{heavy-tailed pairwise net shocks}\\
&\rightarrow \text{generalized CLT}\\
&\rightarrow \text{Levy noise in urban growth equation}.
\end{aligned}
$$

所以 Chapter 9 是从“模型为了生成 Zipf”转向“模型从 migration flows 推导”的关键章节。

---

## 二十三、本章最重要的记忆点

第一，作者不再把 Zipf's law 当作模型的出发点，而是从人口变化的 bottom-up decomposition 出发。

第二，城市增长被拆成两类：

$$
\text{out-of-system growth}
\quad
\text{and}
\quad
\text{interurban migrations}.
$$

第三，out-of-system growth 近似 Gaussian，并写成：

$$
\eta_iS_i.
$$

第四，interurban migration 是 directed weighted graph 上的 net flow：

$$
\sum_{j\in N(i)}
(J_{j\to i}-J_{i\to j}).
$$

第五，migration neighbor number 随城市规模 sublinearly 增长：

$$
N(i)\propto S_i^\gamma.
$$

第六，gravity model 显示 population dependence 是核心，distance 可以作为 second-order correction 被吸收到 noise 中。

第七，平均 flow and counterflow 满足 average detailed balance：

$$
\langle J_{i\to j}\rangle
=
\langle J_{j\to i}\rangle,
$$

但实际 pairwise fluctuations 很大。

第八，net migration shock $X_{ij}$ 有 heavy tail：

$$
\rho(X)\sim X^{-1-\alpha},
\qquad
\alpha<2.
$$

第九，generalized CLT 把 many-neighbor migration sum 变成 Levy stable noise：

$$
\sum_{j\in N(i)}X_{ij}
=
|N(i)|^{1/\alpha}\zeta_i.
$$

第十，最终增长方程是：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
DS_i^\beta\zeta_i,
\qquad
\beta=\nu+\frac{\gamma}{\alpha}.
$$

这条式子的核心含义是：城市增长同时受到 Gaussian out-of-system growth 和 heavy-tailed interurban migration shocks 控制。后者让城市动态不再只是平滑的 Gibrat-style proportional growth，而包含 rare but large migration waves。
