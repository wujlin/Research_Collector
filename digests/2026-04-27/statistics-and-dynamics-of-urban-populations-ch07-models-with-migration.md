---
title: "Statistics and Dynamics of Urban Populations, Chapter 7: Models with migration"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-27"
topics: ["urban growth", "migration", "master equation", "Bouchaud-Mezard model", "mean-field", "Zipf's law", "power-law"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/07-models-with-migration.mineru/hybrid_auto/07-models-with-migration.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 7：Models With Migration

## 精读笔记

---

## 一、这一章在全书动力学线里的位置

Chapter 6 讨论的是 growth models。那些模型关心的是：如果城市人口按比例随机增长，什么条件下会出现 power-law 或 Zipf-like distribution。

但 Chapter 6 的大多数模型没有回答一个更基础的问题：城市增长的 population 从哪里来？

人口来源只有两类：

1. natural growth：出生减死亡；
2. migration：人口在城市系统内部或外部之间移动。

这一章的核心转向是：城市不是互相隔离地随机增长，而是通过 migration 发生相互作用。只要 migration 进入模型，城市增长就不再只是每个城市自己的 multiplicative noise，而变成一个 coupled system：

$$
\text{city growth}
=
\text{internal growth}
+
\text{incoming migration}
-
\text{outgoing migration}.
$$

这也改变了前面关于 Zipf law 的问题。之前的模型常常问：

$$
\text{什么样的随机增长机制能生成 Zipf?}
$$

这一章更接近在问：

$$
\text{如果城市之间真的有人口流动，Zipf 还会自然出现吗?}
$$

作者给出的答案比较谨慎。migration 可以作为一种 regularization，让 Gibrat-like random growth 产生 stationary power-law；但它也会破坏 Simon/Yule 的纯 power-law，并且真实 migration interaction 未必满足模型为了得到 Zipf 所需要的简单 mean-field 假设。

所以这一章的主线可以写成：

$$
\text{Yule-Simon lacks migration}
\rightarrow
\text{interurban migration bends Zipf}
\rightarrow
\text{master equation with utility-driven flows}
\rightarrow
\text{migration as diffusion/redistribution}
\rightarrow
\text{Bouchaud-Mezard stationary power-law}
\rightarrow
\text{mobility controls heterogeneity}.
$$

### 1.1 本章符号口径

这一章有两类模型：前半部分是 size distribution 的 master equation，后半部分是城市之间的 migration flow equation。因此同一个字母在不同模型里可能是局部符号。

$s$ 表示 size class，$P(s,t)$ 表示一个城市处在 size class $s$ 的概率或频率。这里的 $s$ 不是具体城市编号。

$\alpha$ 和 $\beta$ 在 Haran-Vining / modified Yule-Simon 模型里是事件概率参数：$\alpha$ 控制新城市生成，$\beta$ 控制事件是否属于 interurban migration。这里的 $\beta$ 不是 Chapter 9-10 的 migration amplitude exponent。

$J_{ij}$ 表示从城市 $i$ 到城市 $j$ 的 total flow；$I_{ij}$ 表示从 $i$ 到 $j$ 的 per-capita migration intensity。在本章 Bouchaud-Mezard 部分，两个下标的方向按“origin $\to$ destination”读。

$\nu_{ij}(t)$ 是 Haag-type utility model 里的 mobility factor，表示城市对之间的基础可达性或迁移摩擦。它不是 Chapter 9 gravity model 里的 destination-size exponent $\nu$。

$S_i(t)$ 表示城市 $i$ 的 population size，$w_i=S_i/\bar S$ 表示相对平均城市规模。后面 stationary distribution $\rho(w)\sim w^{-1-\mu}$ 里的 $\mu$ 是 Pareto tail exponent，不是 Chapter 10 的 Levy index。

这一章只有一张图，Fig. 7.1。它不是装饰图，而是把 Eq. 7.8 的结构画成了三个部分：internal random growth、incoming migration、outgoing migration。

---

## 二、为什么 migration 必须进入城市增长模型

Yule-Simon 模型隐含了一个历史背景：城市系统还在从外部吸收人口。这个外部可以是 rural population，也可以是自然增长带来的新增人口。这样一来，城市增长主要表现为：

$$
\text{new individuals enter the urban system}
\rightarrow
\text{preferentially attach to existing cities}.
$$

在这种设定里，城市之间的 migration 不是核心机制。新增人口主要来自系统外部，或者来自 births exceeding deaths。

Haran 和 Vining 的关键判断是：这个背景并不总成立。到了自然增长接近零、城市化已经较成熟、农村人口池不再巨大时，城市增长的主要来源就可能不是“系统外部新增人口”，而是城市之间的再分配：

$$
\text{dominant growth source}
=
\text{interurban migration}.
$$

这一步很重要。因为 migration 不是简单加人口。migration 是一边增加、一边减少：

$$
\text{one city gains}
\quad
\Longleftrightarrow
\quad
\text{another city loses}.
$$

所以 migration 会把城市系统从 pure growth process 改成 redistribution process。它不只是让某个城市变大，也同时改变别的城市的 size。这就是为什么引入 migration 后，原来的 pure Simon power-law 会发生弯曲。

---

## 三、Haran-Vining：modified Yule-Simon model

### 3.1 模型对象和符号

令

$$
P(s,t)
=
\text{时刻 }t\text{ 一个城市 size 为 }s\text{ 的概率}.
$$

这里的 $s$ 是城市人口 size class，不是某个具体城市编号。$P(s,t)$ 描述的是整个城市系统的 size distribution。

模型有两个关键概率：

$$
\alpha
=
\text{新城市出现的概率},
$$

$$
\beta
=
\text{一次事件是 interurban migration 的概率}.
$$

因此 $1-\beta$ 表示这次事件不是城市间迁移，而更接近 Simon 原模型里的“新增 individual 进入城市系统”。

还有一个归一化因子 $K(t)$。它的作用和 Simon 模型中的 $K(k)$ 类似：当选择某个 size class 时，选择概率要正比于 size，但所有概率加起来必须归一化。

Haran-Vining 的关键设定是：

1. 如果一个 newcomer 加入已有城市，目标城市为 size $s$ 的概率正比于 $sP(s,t)$。
2. 如果发生 interurban migration，离开城市的概率也正比于 origin city size，进入城市的概率也正比于 destination city size。

这意味着 migration 事件同时有两个 preferential components：

$$
\text{origin selection}
\propto
sP(s,t),
$$

$$
\text{destination selection}
\propto
s'P(s',t).
$$

大城市不仅更容易吸引迁入，也因为人口多而更可能产生迁出。

### 3.2 Eq. 7.1：为什么多出一个二阶差分结构

对 $s>1$，分布演化为

$$
\begin{aligned}
P(s,t+1)
&=
P(s,t)
+(1-\beta)K(t)\left[(s-1)P(s-1,t)-sP(s,t)\right]\\
&\quad
+\beta K(t)
\left[
(s-1)P(s-1,t)
-2sP(s,t)
+(s+1)P(s+1,t)
\right].
\end{aligned}
\tag{7.1}
$$

这条式子最好拆成三层。

第一层是原来的存量：

$$
P(s,t).
$$

这是时刻 $t$ 已经处在 size $s$ 的城市比例。

第二层是非迁移增长，也就是 Simon-like growth：

$$
(1-\beta)K(t)\left[(s-1)P(s-1,t)-sP(s,t)\right].
$$

这里有一个流入项：

$$
(s-1)P(s-1,t).
$$

它表示：原来 size 为 $s-1$ 的城市，如果获得一个新增 individual，就会进入 size $s$。

还有一个流出项：

$$
-sP(s,t).
$$

它表示：原来 size 为 $s$ 的城市，如果获得一个新增 individual，就会变成 size $s+1$，于是离开 size $s$ 这个 class。

前面的 $1-\beta$ 表示这类事件不是 interurban migration，而是外部新增或自然增长式的 Simon 事件。

第三层是 migration 造成的上下移动：

$$
\beta K(t)
\left[
(s-1)P(s-1,t)
-2sP(s,t)
+(s+1)P(s+1,t)
\right].
$$

这一项之所以像二阶差分，是因为 migration 会让一个城市既可能增加 1，也可能减少 1。

先看 migration-in：

$$
(s-1)P(s-1,t)-sP(s,t).
$$

这和 Simon-like growth 形式相同。原来 size $s-1$ 的城市收到迁入者后进入 $s$；原来 size $s$ 的城市收到迁入者后离开 $s$，进入 $s+1$。

再看 migration-out：

$$
(s+1)P(s+1,t)-sP(s,t).
$$

原来 size $s+1$ 的城市失去一个 migrant 后进入 $s$；原来 size $s$ 的城市失去一个 migrant 后离开 $s$，进入 $s-1$。

把 migration-in 和 migration-out 合在一起：

$$
\left[(s-1)P(s-1,t)-sP(s,t)\right]
+
\left[(s+1)P(s+1,t)-sP(s,t)\right].
$$

于是得到

$$
(s-1)P(s-1,t)-2sP(s,t)+(s+1)P(s+1,t).
$$

这就是 Eq. 7.1 中 migration term 的来源。它不是单向 preferential attachment，而是在 size axis 上同时允许向上和向下移动。因此 migration 在数学上把 Simon 模型从 pure birth process 改成了 birth-death / redistribution process。

### 3.3 Eq. 7.2：size 1 的边界条件

size $1$ 是特殊的，因为它是最小城市 size class，也是新城市出生的位置。边界条件写成

$$
\begin{aligned}
P(1,t+1)
&=
P(1,t)
+\alpha(1-\beta)
-(1-\beta)K(t)P(1,t)\\
&\quad
+\beta K(t)\left[2P(2,t)-2P(1,t)\right].
\end{aligned}
\tag{7.2}
$$

这里也可以逐项读。

第一项是原来的 size 1 存量：

$$
P(1,t).
$$

第二项是新城市出生：

$$
\alpha(1-\beta).
$$

它表示：当事件不是 interurban migration 时，有概率 $\alpha$ 生成一个新城市，而新城市从 size 1 开始。

第三项是 size 1 城市因获得新增 individual 而离开 size 1：

$$
-(1-\beta)K(t)P(1,t).
$$

如果 size 1 城市获得一个 newcomer，它就变成 size 2，因此从 $P(1,t)$ 中流出。

最后一项是 migration 对边界的影响：

$$
\beta K(t)\left[2P(2,t)-2P(1,t)\right].
$$

$2P(2,t)$ 表示 size 2 城市如果失去一个 migrant，就会变成 size 1，流入边界 class。$-2P(1,t)$ 表示 size 1 城市可以因为迁入变成 size 2，也可以因为迁出跌出 size 1 的城市状态，因此在边界处有额外流出。

这条边界式说明：一旦 migration 进入模型，最小城市 class 不只是新城市出生点，也是城市消失或跌出系统的敏感位置。

### 3.4 Eq. 7.3：没有 migration 时回到 Simon

当

$$
\beta=0,
$$

所有 migration terms 都消失，Eq. 7.1 回到 Simon process。此时 stationary distribution 是

$$
P(s,t\to\infty)
\sim
\frac{1}{s^\zeta},
\tag{7.3}
$$

其中

$$
\zeta=\frac{1}{1-\alpha}.
$$

这和 Chapter 6 的结论一致：没有 migration 时，模型靠 preferential attachment 和新城市出生生成 pure power-law。

但只要

$$
\beta>0,
$$

distribution 就不再是 pure power-law。原因是 migration term 在 size axis 上引入了向下跳转。城市 size 不再只沿着 $s\to s+1$ 单向增长，而是会在相邻 size classes 之间扩散：

$$
s-1
\leftrightarrow
s
\leftrightarrow
s+1.
$$

这会在 log-log rank-size 图上制造 curvature。Haran 和 Vining 的重要性正在这里：他们很早就指出，真实城市系统中 interurban migration 会破坏简单 Zipf law，因此不能把 Zipf 当作城市系统的自然默认结果。

---

## 四、Haag et al.：utility-driven master equation

### 4.1 从 size distribution 转到城市系统状态

Haran-Vining 仍然主要在 size distribution 上工作。Haag et al. 则把问题推进到整个城市系统的配置。

设系统有 $L$ 个城市和一个 hinterland $h$。城市人口配置写成向量

$$
\vec{s}
=
\{s_1,s_2,\ldots,s_L\}.
$$

这里的 hinterland $h$ 可以理解为城市系统之外的非城市腹地或外部人口池。它不是第 $L+1$ 个普通城市，而是一个外部 reservoir：人口可以从 hinterland 进入某个城市，也可以从某个城市流回 hinterland。

所以 $\vec{s}$ 只记录 $L$ 个城市的人口：

$$
s_i=\text{city }i\text{ 的 population}.
$$

hinterland $h$ 不放进 $\vec{s}$，因为模型主要关心城市系统内部的 configuration，而 $h$ 只是和城市系统交换人口的外部边界。

模型的目标不是只描述“有多少城市处在 size $s$”，而是描述整个向量 $\vec{s}$ 怎样随 migration 改变。

如果一个人从城市 $j$ 迁到城市 $i$，城市 $j$ 的人口减少 1，城市 $i$ 的人口增加 1。于是 migration 是 configuration space 上的跳转：

$$
\vec{s}
\longrightarrow
\vec{s}+\mathbf{e}_i-\mathbf{e}_j.
$$

这比只看 $P(s,t)$ 更细，因为它保留了“从哪里到哪里”的方向。

### 4.2 Eq. 7.4：迁移概率来自 mobility 和 utility difference

个体从城市 $j$ 迁到城市 $i$ 的概率写成

$$
p_{ij}(\vec{s})
=
\nu_{ij}(t)
\exp\left[
U_i(\vec{s})-U_j(\vec{s})
\right].
\tag{7.4}
$$

这里有两个因素。

第一，$\nu_{ij}(t)$ 是 mobility factor，并且满足

$$
\nu_{ij}=\nu_{ji}.
$$

它是对称的，表示城市对之间的基础可达性或迁移摩擦。比如距离、交通联系、制度障碍，都可以进入这类 mobility factor。对称性意味着：如果只看基础连接强度，从 $i$ 到 $j$ 和从 $j$ 到 $i$ 的通道强度相同。

第二，指数项

$$
\exp\left[U_i(\vec{s})-U_j(\vec{s})\right]
$$

表示 utility difference。$U_i$ 是城市 $i$ 的 attraction potential。若

$$
U_i>U_j,
$$

则从 $j$ 到 $i$ 的迁移概率被放大。若

$$
U_i<U_j,
$$

则迁移概率被压低。

所以 Eq. 7.4 的直觉是：

$$
\text{migration probability}
=
\text{mobility channel}
\times
\text{attraction advantage}.
$$

这和 gravity model 有相似味道，但这里的 attraction 不是直接写成人口规模，而是通过 utility potential 写出来。

### 4.3 Eq. 7.5：从个体迁移概率到城市间 transition rate

从城市 $j$ 到城市 $i$ 的总迁移率是

$$
W_{ij}(\vec{s})
=
s_jp_{ij}(\vec{s})
=
s_j\nu_{ij}(t)
\exp\left[
U_i(s_i+1)-U_j(s_j)
\right].
\tag{7.5}
$$

这一步的逻辑是：$p_{ij}$ 是单个个体的迁移概率，但城市 $j$ 里有 $s_j$ 个可能迁移的人。因此总 transition rate 要乘上 origin population：

$$
\text{total flow from }j\text{ to }i
=
\text{number of potential movers in }j
\times
\text{per-person probability}.
$$

所以

$$
W_{ij}=s_jp_{ij}.
$$

式子中 $U_i(s_i+1)$ 的含义是：如果一个人迁入城市 $i$，城市 $i$ 的 size 会从 $s_i$ 变成 $s_i+1$，因此 attraction potential 要在迁入后的状态上评估。$U_j(s_j)$ 则是 origin city 当前状态的 utility。

### 4.4 Eq. 7.6 和 Eq. 7.7：平均城市人口的演化

完整 master equation 应该描述

$$
P(\vec{s},t),
$$

也就是整个城市人口配置的概率分布。但 $\vec{s}$ 是 $L$ 维状态，完整 master equation 很复杂。Haag et al. 因此转向平均人口：

$$
\bar{s}_k(t)
=
\sum_{\vec{s}}s_kP(\vec{s},t).
\tag{7.6}
$$

这里 $k$ 不是随机变量，而是一个固定的城市编号。比如 $k=3$ 就表示“第三个城市”。随机变量是整个配置

$$
\vec{s}=(s_1,\ldots,s_L),
$$

因为系统可能处在很多不同人口配置中。对每一个可能配置 $\vec{s}$，城市 $k$ 的人口是该配置的第 $k$ 个分量 $s_k$。

所以 Eq. 7.6 的求和

$$
\sum_{\vec{s}}
$$

不是对城市编号求和，而是对所有可能的人口配置求和。每个配置用概率 $P(\vec{s},t)$ 加权，再取其中的 $s_k$。因此

$$
\bar{s}_k(t)
$$

表示“固定城市 $k$ 在时刻 $t$ 的期望人口”。

平均人口的演化写成

$$
\begin{aligned}
\frac{d\bar{s}_k(t)}{dt}
&=
\sum_{i=1}^{L}
\bar{s}_i\nu_{ki}
\exp(U_k-U_i)\\
&\quad
-
\sum_{i=1}^{L}
\bar{s}_k\nu_{ik}
\exp(U_i-U_k)
+W_{kh}-W_{hk}
+\delta_k\bar{s}_k.
\end{aligned}
\tag{7.7}
$$

这条式子是一个 accounting equation。它把城市 $k$ 的平均变化分成五部分。

第一部分是来自其他城市的 inflow：

$$
\sum_{i=1}^{L}
\bar{s}_i\nu_{ki}
\exp(U_k-U_i).
$$

从城市 $i$ 到城市 $k$ 的迁移率，等于 origin population $\bar{s}_i$ 乘以 mobility $\nu_{ki}$，再乘以 utility advantage $\exp(U_k-U_i)$。如果 $U_k$ 高于 $U_i$，城市 $k$ 的吸引力更强，inflow 增大。

第二部分是从城市 $k$ 到其他城市的 outflow：

$$
-
\sum_{i=1}^{L}
\bar{s}_k\nu_{ik}
\exp(U_i-U_k).
$$

这里 origin population 是 $\bar{s}_k$。如果其他城市 $i$ 的 utility 高于 $k$，则 $\exp(U_i-U_k)$ 较大，城市 $k$ 的人口流出更多。

第三部分是 hinterland 到城市 $k$：

$$
+W_{kh}.
$$

按照 $W_{ij}$ 表示从 $j$ 到 $i$ 的 transition rate，$W_{kh}$ 是从 hinterland $h$ 到 city $k$ 的流入。

第四部分是城市 $k$ 到 hinterland：

$$
-W_{hk}.
$$

这是从 city $k$ 到 hinterland $h$ 的流出。

第五部分是 natural growth：

$$
\delta_k\bar{s}_k.
$$

$\delta_k$ 是城市 $k$ 的 net growth rate，也就是 births minus deaths。

所以 Eq. 7.7 的结构是：

$$
\frac{d\bar{s}_k}{dt}
=
\text{intercity inflow}
-
\text{intercity outflow}
+
\text{hinterland inflow}
-
\text{hinterland outflow}
+
\text{natural growth}.
$$

这比 Zipf-style distribution model 更接近真实 demographic accounting。它不再把城市大小看成独立样本，而是直接建模城市之间的人口交换。

### 4.5 法国数据的含义

Haag et al. 用 1954-1982 年的法国城市系统估计这些参数，并做 projection。结果中 rank variation 较小，top 10 基本稳定，但 rank 和 population 并没有形成简单 Zipf relation。

这条经验结果和 Haran-Vining 的观点一致：一旦 migration 被显式纳入，城市 hierarchy 不一定表现为一条简单 power-law。migration 可能维持 rank stability，也可能造成局部弯曲和偏离，而不是自动生成纯 Zipf。

---

## 五、Bouchaud-Mezard：migration as diffusion with noise

### 5.1 为什么要换一条 regularization 路线

Chapter 6 的 Gabaix model 用 reflective lower barrier regularize Gibrat process。它的逻辑是：城市按 GBM 随机增长，但不能低于 $S_{\min}$，于是形成 stationary Pareto。

这一章给出另一种 regularization：

$$
\text{不要先规定一个 artificial lower barrier，}
\quad
\text{而是让城市之间发生 migration exchange}.
$$

如果一个城市太小，它可以通过 migration inflow 得到补充；如果一个城市太大，它会通过 outflow 被拉回平均水平。这样 migration 本身就可以扮演 regularizing force。

Bouchaud-Mezard 原本研究 wealth distribution。作者把它翻译到城市语境：城市 population 像 wealth 一样，既有内部随机增长，也有和其他 units 的交换。

### 5.2 Eq. 7.8：内部增长 + 净迁移

城市 $i$ 的人口满足

$$
\frac{dS_i}{dt}
=
\eta_i(t)S_i(t)
+
\sum_j
\left(
J_{ji}
-
J_{ij}
\right).
\tag{7.8}
$$

这里

$$
S_i(t)
=
\text{city }i\text{ 的 population}.
$$

第一项

$$
\eta_i(t)S_i(t)
$$

是 internal growth。它仍然是 Gibrat-style multiplicative growth：随机增长率 $\eta_i(t)$ 乘以当前规模 $S_i(t)$。

第二项

$$
\sum_j J_{ji}
$$

是 incoming migration。$J_{ji}$ 表示从城市 $j$ 到城市 $i$ 的 flow。

第三项

$$
-\sum_j J_{ij}
$$

是 outgoing migration。$J_{ij}$ 表示从城市 $i$ 到城市 $j$ 的 flow。

所以 Eq. 7.8 就是：

$$
\text{population change}
=
\text{internal stochastic growth}
+
\text{incoming flows}
-
\text{outgoing flows}.
$$

Fig. 7.1 正是在画这个结构。

![Fig. 7.1](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/07-models-with-migration.mineru/hybrid_auto/images/page-03-figure-01.jpg)

图中间是 internal growth $\eta_iS_i$，左边是 incoming migration $J_{ji}$，右边是 outgoing migration $J_{ij}$。它提醒我们：migration model 不是只在 Gibrat noise 外面加一个小修正，而是把城市增长改成了 flow-balance problem。

### 5.3 Eq. 7.9：flow proportional to origin city size

假设从城市 $i$ 到城市 $j$ 的 flow 与 origin city size 成比例：

$$
J_{ij}=I_{ij}S_i.
$$

这里 $I_{ij}$ 是从 $i$ 到 $j$ 的 per-capita mobility rate。城市 $i$ 人口越多，潜在迁出者越多，因此总 outflow 越大。

代入 Eq. 7.8：

$$
\frac{dS_i}{dt}
=
\eta_i(t)S_i(t)
+
\sum_j
\left[
I_{ji}S_j(t)
-
I_{ij}S_i(t)
\right].
\tag{7.9}
$$

这里的两项分别是：

$$
I_{ji}S_j(t)
=
\text{from }j\text{ to }i\text{ 的 inflow},
$$

$$
I_{ij}S_i(t)
=
\text{from }i\text{ to }j\text{ 的 outflow}.
$$

这个模型已经是一个 coupled stochastic system。每个城市的增长不只由自己的 $\eta_i$ 决定，也由所有其他城市的 migration flows 决定。

---

## 六、mean-field complete graph：所有城市以同一强度交换

### 6.1 为什么需要 mean-field 简化

一般的 $I_{ij}$ 很难求解。因为每个城市对之间都可以有不同 migration intensity，这会形成一个复杂网络。

Bouchaud-Mezard 先研究最简单的 complete graph mean-field case：

$$
I_{ij}=\frac{I}{N}.
$$

这里 $I_{ij}$ 是从城市 $i$ 到城市 $j$ 的 per-capita migration intensity。它有两个下标，是因为一般情况下每一对城市都可以有不同的迁移强度。

无下标的 $I$ 是 mean-field 简化后保留下来的系统级 exchange strength。它不是某一条具体边的迁移率，而是“一个城市和整个城市系统交换人口的总强度尺度”。

complete graph mean-field 的假设是：每个城市都和所有其他城市连接，而且所有连接完全一样。因此每条具体边只分到总交换强度的一小份：

$$
\text{pairwise intensity}
=
\frac{\text{total exchange scale}}{\text{number of possible destinations}}
=
\frac{I}{N}.
$$

这里 $N$ 是城市数量。除以 $N$ 的原因是为了让 large-$N$ limit 保持良好。如果每个城市都和 $N$ 个城市交换，而每条边强度不缩小，总交换量会随 $N$ 发散。

写成 $I/N$ 后，对城市 $i$ 来说，总 outflow intensity 近似为

$$
\sum_j I_{ij}
=
\sum_j \frac{I}{N}
\simeq
I.
$$

也就是说，每条边很弱，但边很多；合起来每个城市面对的总交换强度仍然是 $O(I)$。

### 6.2 Eq. 7.10：migration 变成向平均值回归的力

把

$$
I_{ij}=\frac{I}{N}
$$

代入 Eq. 7.9：

$$
\sum_j
\left[
I_{ji}S_j
-
I_{ij}S_i
\right]
=
\sum_j
\left[
\frac{I}{N}S_j
-
\frac{I}{N}S_i
\right].
$$

第一部分是

$$
\sum_j\frac{I}{N}S_j
=
I\frac{1}{N}\sum_jS_j
=
I\bar{S}.
$$

第二部分是

$$
\sum_j\frac{I}{N}S_i
=
\frac{I}{N}NS_i
=
IS_i.
$$

所以 migration term 变成

$$
I\bar{S}-IS_i
=
I(\bar{S}-S_i).
$$

于是得到

$$
\frac{dS_i}{dt}
=
I(\bar{S}-S_i)
+
\eta_i(t)S_i.
\tag{7.10}
$$

这里

$$
\bar{S}(t)
=
\frac{1}{N}\sum_iS_i(t).
$$

这条式子的物理含义很清楚。若

$$
S_i<\bar{S},
$$

则

$$
I(\bar{S}-S_i)>0,
$$

migration 给城市 $i$ 一个正向补充。若

$$
S_i>\bar{S},
$$

则

$$
I(\bar{S}-S_i)<0,
$$

migration 把城市 $i$ 往下拉。

所以 mean-field migration 是一个 homogenizing force。它不像 Gabaix model 那样用人工 lower barrier 防止城市跌到 0，而是通过 exchanges 把城市拉向平均规模。

### 6.3 Eq. 7.11：线性随机 ODE 的形式解

Eq. 7.10 可以写成

$$
\frac{dS_i}{dt}
=
\left[\eta_i(t)-I\right]S_i(t)
+
I\bar{S}(t).
$$

这是一个一阶线性非齐次 ODE。令

$$
A_i(t)=\eta_i(t)-I.
$$

则

$$
\frac{dS_i}{dt}
=
A_i(t)S_i(t)
+
I\bar{S}(t).
$$

线性 ODE 的形式解是

$$
S_i(t)
=
S_i(0)
\exp\left[
\int_0^tA_i(\tau)d\tau
\right]
+
\int_0^t
I\bar{S}(\tau)
\exp\left[
\int_\tau^tA_i(\tau')d\tau'
\right]
d\tau.
$$

代回 $A_i=\eta_i-I$：

$$
S_i(t)
=
S_i(0)
e^{\int_0^t[\eta_i(\tau)-I]d\tau}
+
I\int_0^t
d\tau\,
\bar{S}(\tau)
e^{\int_\tau^t[\eta_i(\tau')-I]d\tau'}.
\tag{7.11}
$$

第一项是初始人口在随机 multiplicative growth 和 migration leakage 下的延续。第二项是过去每个时刻 $\tau$ 从 mean-field source $I\bar{S}(\tau)$ 注入的人口，在 $\tau$ 到 $t$ 之间继续经历同样的随机增长和 leakage。

这一步不是最终解，因为 $\bar{S}(t)$ 仍然未知。它只是把单个城市方程写成了“给定平均场 $\bar{S}$ 时”的形式解。

---

## 七、self-averaging 与平均人口增长

### 7.1 Eq. 7.12：large-$N$ self-averaging 假设

为了继续求解，作者假设 large $N$ limit 下平均人口 self-averaging：

$$
\bar{S}
\simeq_{N\to\infty}
\langle\bar{S}\rangle.
\tag{7.12}
$$

这里 $\langle\cdot\rangle$ 表示对随机增长率 $\eta$ 的平均。

self-averaging 的意思是：当城市数量很大时，单个城市的随机波动会在平均值里相互抵消。因此实际样本平均 $\bar{S}$ 接近 ensemble average $\langle\bar{S}\rangle$。

这个假设把一个 coupled random system 简化成 mean-field deterministic equation。它不是一个城市机制，而是一个 large population approximation。

### 7.2 为什么指数平均会出现 $m+\sigma^2$

随机增长率 $\eta_i(t)$ 设为独立同分布 Gaussian noise，平均值为 $m$，方差强度为 $2\sigma^2$。

在 Eq. 7.11 里需要计算类似

$$
\left\langle
\exp\left[
\int_a^b\eta_i(\tau)d\tau
\right]
\right\rangle.
$$

如果

$$
X=\int_a^b\eta_i(\tau)d\tau
$$

是 Gaussian 变量，则

$$
\mathbb{E}[e^X]
=
\exp\left[
\mathbb{E}[X]
+
\frac{1}{2}\operatorname{Var}(X)
\right].
$$

这里

$$
\mathbb{E}[X]=m(b-a),
$$

而噪声方差强度为 $2\sigma^2$，所以

$$
\operatorname{Var}(X)=2\sigma^2(b-a).
$$

因此

$$
\mathbb{E}[e^X]
=
\exp\left[
m(b-a)+\sigma^2(b-a)
\right]
=
e^{(m+\sigma^2)(b-a)}.
$$

如果指数里还有 $-I$，就得到

$$
e^{(m+\sigma^2-I)(b-a)}.
$$

这就是 Eq. 7.13 中 $m+\sigma^2-I$ 的来源。$\sigma^2$ 不是 drift 本身，而是 multiplicative Gaussian noise 的 exponential moment 修正。

### 7.3 Eq. 7.13 到 Eq. 7.14：平均人口方程如何求解

对 Eq. 7.11 做 ensemble average，并使用 self-averaging，得到

$$
\bar{S}(t)
\simeq
\bar{S}(0)e^{(m+\sigma^2-I)t}
+
I\int_0^t
d\tau\,
\bar{S}(\tau)
e^{(m+\sigma^2-I)(t-\tau)}.
\tag{7.13}
$$

为了看清解，令

$$
a=m+\sigma^2-I.
$$

则 Eq. 7.13 写成

$$
\bar{S}(t)
=
\bar{S}(0)e^{at}
+
I\int_0^t
\bar{S}(\tau)e^{a(t-\tau)}d\tau.
$$

这是一个 Volterra integral equation。可以用 Laplace transform，也可以直接对 $t$ 求导。

对右边求导：

$$
\frac{d\bar{S}}{dt}
=
a\bar{S}(0)e^{at}
+
I\bar{S}(t)
+
aI\int_0^t
\bar{S}(\tau)e^{a(t-\tau)}d\tau.
$$

把第一项和最后一项合并：

$$
a\left[
\bar{S}(0)e^{at}
+
I\int_0^t
\bar{S}(\tau)e^{a(t-\tau)}d\tau
\right]
=
a\bar{S}(t).
$$

因此

$$
\frac{d\bar{S}}{dt}
=
a\bar{S}(t)
+
I\bar{S}(t)
=
(a+I)\bar{S}(t).
$$

代回 $a=m+\sigma^2-I$：

$$
\frac{d\bar{S}}{dt}
=
(m+\sigma^2)\bar{S}(t).
$$

所以

$$
\bar{S}(t)
=
\bar{S}(0)e^{(m+\sigma^2)t}.
\tag{7.14}
$$

这个结果有一个重要含义：mean-field migration 不改变系统总平均增长率。它只在城市之间重新分配人口。整体平均增长仍然由 internal multiplicative growth 的 mean 和 noise correction 决定。

---

## 八、归一化变量 $w_i$：从非平稳增长到 stationary distribution

### 8.1 为什么要除以平均人口

$S_i(t)$ 本身随时间指数增长，因此它不可能有 stationary distribution。为了研究城市之间的相对大小，需要定义

$$
w_i(t)
=
\frac{S_i(t)}{\bar{S}(t)}.
$$

如果 $w_i>1$，城市 $i$ 大于平均城市；如果 $w_i<1$，城市 $i$ 小于平均城市。

这个归一化把问题从

$$
\text{absolute population growth}
$$

转成

$$
\text{relative city size distribution}.
$$

Zipf/Pareto 问的本质上也是相对分布尾部，而不是总人口指数增长本身。

### 8.2 Eq. 7.15：归一化变量的 Langevin equation

从

$$
w_i=\frac{S_i}{\bar{S}}
$$

出发。为了看清楚求导，先把它写成乘积形式：

$$
w_i
=
S_i\bar{S}^{-1}.
$$

对时间求导，用 product rule：

$$
\frac{dw_i}{dt}
=
\frac{dS_i}{dt}\bar{S}^{-1}
+
S_i\frac{d}{dt}\left(\bar{S}^{-1}\right).
$$

现在处理第二项。因为

$$
\frac{d}{dt}\left(\bar{S}^{-1}\right)
=
-\bar{S}^{-2}\frac{d\bar{S}}{dt},
$$

所以

$$
\frac{dw_i}{dt}
=
\frac{1}{\bar{S}}\frac{dS_i}{dt}
-
\frac{S_i}{\bar{S}^2}\frac{d\bar{S}}{dt}.
$$

这里的负号来自 $\bar{S}^{-1}$ 的导数。直观上，如果 $S_i$ 不变但平均城市规模 $\bar{S}$ 增大，那么城市 $i$ 的相对规模 $w_i=S_i/\bar{S}$ 会下降。

因为

$$
\frac{S_i}{\bar{S}}=w_i,
$$

所以第二项可以改写为

$$
\frac{S_i}{\bar{S}^2}\frac{d\bar{S}}{dt}
=
\frac{S_i}{\bar{S}}
\frac{1}{\bar{S}}
\frac{d\bar{S}}{dt}
=
w_i
\frac{1}{\bar{S}}
\frac{d\bar{S}}{dt}.
$$

于是

$$
\frac{dw_i}{dt}
=
\frac{1}{\bar{S}}\frac{dS_i}{dt}
-
w_i\frac{1}{\bar{S}}\frac{d\bar{S}}{dt}.
$$

代入 Eq. 7.10：

$$
\frac{dS_i}{dt}
=
I(\bar{S}-S_i)
+
\eta_i(t)S_i.
$$

两边除以 $\bar{S}$：

$$
\frac{1}{\bar{S}}\frac{dS_i}{dt}
=
\frac{I(\bar{S}-S_i)}{\bar{S}}
+
\eta_i(t)\frac{S_i}{\bar{S}}.
$$

先处理 migration 项：

$$
\frac{I(\bar{S}-S_i)}{\bar{S}}
=
I\left(
\frac{\bar{S}}{\bar{S}}
-
\frac{S_i}{\bar{S}}
\right).
$$

因为

$$
\frac{\bar{S}}{\bar{S}}=1,
\qquad
\frac{S_i}{\bar{S}}=w_i,
$$

所以

$$
\frac{I(\bar{S}-S_i)}{\bar{S}}
=
I(1-w_i).
$$

再处理 internal growth 项：

$$
\eta_i(t)\frac{S_i}{\bar{S}}
=
\eta_i(t)w_i.
$$

因此

$$
\frac{1}{\bar{S}}\frac{dS_i}{dt}
=
I(1-w_i)
+
\eta_i(t)w_i.
$$

再由 Eq. 7.14：

$$
\frac{1}{\bar{S}}\frac{d\bar{S}}{dt}
=
m+\sigma^2.
$$

所以

$$
\frac{dw_i}{dt}
=
I(1-w_i)
+
\eta_i(t)w_i
-
(m+\sigma^2)w_i.
$$

令

$$
\delta\eta_i(t)=\eta_i(t)-m,
$$

得到

$$
\frac{dw_i}{dt}
=
I(1-w_i)
-
\sigma^2w_i
+
w_i\delta\eta_i(t).
$$

因此可以写成

$$
\frac{dw_i}{dt}
=
f(w_i)
+
g(w_i)\delta\eta_i(t),
\tag{7.15}
$$

其中

$$
f(w)=I(1-w)-\sigma^2w,
\qquad
g(w)=w.
$$

这一步非常关键，因为它把原来随总人口一起增长的 $S_i$ 动力学，改写成了相对规模 $w_i$ 的动力学。$w_i$ 的含义是：

$$
w_i=1
\quad
\Longleftrightarrow
\quad
\text{city }i\text{ 正好等于平均城市规模}.
$$

因此 $f(w)$ 可以直接读成相对规模空间里的 deterministic drift：

$$
f(w)=I(1-w)-\sigma^2w.
$$

第一部分是 migration homogenization：

$$
I(1-w).
$$

如果

$$
w<1,
$$

说明城市小于平均规模，于是

$$
I(1-w)>0.
$$

migration 给它一个向上的相对增长趋势。直观上，小城市会从平均场收到净流入。

如果

$$
w>1,
$$

说明城市大于平均规模，于是

$$
I(1-w)<0.
$$

migration 给它一个向下的相对增长趋势。直观上，大城市会有净流出，或者至少被平均场拉回。

所以 $I(1-w)$ 是一个 mean-reverting force：它把 $w$ 往 $1$ 拉。

第二部分是 noise-induced correction：

$$
-\sigma^2w.
$$

它不是某个额外的迁移机制，而是来自归一化步骤。因为 $\bar{S}(t)$ 的平均增长率不是 $m$，而是

$$
m+\sigma^2.
$$

这里的 $\sigma^2$ 来自 multiplicative Gaussian noise 的 exponential moment correction。把 $S_i$ 除以 $\bar{S}$ 时，我们要从单个城市增长里减去整体平均增长：

$$
\eta_i(t)w_i-(m+\sigma^2)w_i.
$$

再把

$$
\eta_i(t)=m+\delta\eta_i(t)
$$

代入，就得到

$$
\eta_i(t)w_i-(m+\sigma^2)w_i
=
\delta\eta_i(t)w_i-\sigma^2w_i.
$$

所以 $-\sigma^2w$ 是归一化到相对规模之后出现的 deterministic correction。它表示：由于整体平均人口受到 multiplicative noise 的 Jensen correction 而增长得更快，单个城市的相对规模需要扣掉这部分整体增长。

最后看噪声项：

$$
g(w)\delta\eta_i(t)=w\delta\eta_i(t).
$$

这里的关键是不要把 $\delta\eta_i(t)$ 理解成“直接加到城市规模上的人口冲击”。它是增长率冲击，也就是城市 $i$ 的瞬时增长率相对于平均增长率的偏离。原来的城市规模方程里，随机增长项是

$$
\eta_i(t)S_i(t).
$$

也就是说，噪声先作用在 growth rate 上，再乘以当前城市规模 $S_i(t)$。当我们改用相对规模

$$
w_i(t)=\frac{S_i(t)}{\bar{S}(t)}
$$

之后，同一个增长率冲击就变成

$$
\delta\eta_i(t)w_i(t).
$$

所以在标准写法

$$
\frac{dw}{dt}=f(w)+g(w)\delta\eta(t)
$$

里，噪声振幅函数必须是

$$
g(w)=w.
$$

这就是 multiplicative noise 的含义：随机项不是以固定幅度加到 $w$ 上，而是先给一个增长率冲击，再由当前规模 $w$ 把它转换成规模变化。

如果两个城市受到同样大小的正向增长率冲击 $\delta\eta_i(t)>0$，较大的城市因为 $w$ 更大，$w\delta\eta_i(t)$ 也更大，所以相对规模的上升幅度更大；较小的城市因为 $w$ 更小，同样的增长率冲击转化出来的规模变化也更小。反过来，负向冲击也是按当前 $w$ 的大小放大或缩小。

因此，$g(w)=w$ 不是一个任意设定，而是从“噪声作用在增长率上”推出的。它把城市增长中的随机性写成 proportional fluctuation：规模越大，绝对随机波动越大；但冲击本身仍然是增长率层面的随机性。

---

## 九、Fokker-Planck equation 和 stationary distribution

### 9.1 Eq. 7.16：为什么要指定 Stratonovich

Eq. 7.15 中噪声项是

$$
g(w)\delta\eta(t)=w\delta\eta(t).
$$

它依赖当前状态 $w$，因此是 multiplicative noise。Chapter 5 已经说明：multiplicative noise 的 Fokker-Planck equation 会依赖 stochastic prescription。

Bouchaud-Mezard 使用 Stratonovich prescription。于是 $\rho(w,t)$ 的 Fokker-Planck equation 写成

$$
\frac{\partial\rho}{\partial t}
=
-
\frac{\partial}{\partial w}[f\rho]
+
\sigma^2
\frac{\partial}{\partial w}
\left[
g\frac{\partial}{\partial w}(g\rho)
\right].
\tag{7.16}
$$

这里第一项是 drift flux：

$$
-\partial_w[f\rho].
$$

第二项是 multiplicative diffusion：

$$
\sigma^2\partial_w\left[g\partial_w(g\rho)\right].
$$

它不是简单的 $\partial_w^2[g^2\rho]$ 写法，而是 Stratonovich 下的结构。对本模型来说

$$
g(w)=w.
$$

把它代入 diffusion operator，可以看出这个结构具体在做什么。先看括号内部：

$$
g\rho=w\rho.
$$

对它求导：

$$
\partial_w(g\rho)
=
\partial_w(w\rho)
=
\rho+w\partial_w\rho.
$$

再乘外面的 $g=w$：

$$
g\partial_w(g\rho)
=
w(\rho+w\partial_w\rho)
=
w\rho+w^2\partial_w\rho.
$$

最后再取一次 $\partial_w$：

$$
\partial_w[g\partial_w(g\rho)]
=
\partial_w(w\rho+w^2\partial_w\rho)
=
\rho+3w\partial_w\rho+w^2\partial_w^2\rho.
$$

所以在这个模型里，Stratonovich diffusion 项实际展开为

$$
\sigma^2\partial_w[g\partial_w(g\rho)]
=
\sigma^2(\rho+3w\partial_w\rho+w^2\partial_w^2\rho).
$$

这个结果和简单写成

$$
\sigma^2\partial_w^2(w^2\rho)
$$

不同。后者展开为

$$
\sigma^2(2\rho+4w\partial_w\rho+w^2\partial_w^2\rho).
$$

两者的最高阶二阶导项都是 $\sigma^2w^2\partial_w^2\rho$，因为局部扩散强度都随 $w^2$ 增大。但一阶导项和零阶项不同。这些差异正是 stochastic prescription 的差异：当噪声振幅依赖状态变量 $w$ 时，如何解释“在一个很小时间步内用哪个 $w$ 来乘噪声”会改变极限方程。

Stratonovich 写法的物理含义是：噪声振幅在小时间步内部连续随状态变化，扩散通量要按

$$
-\sigma^2g\partial_w(g\rho)
$$

来读。先出现的 $g\rho$ 表示 density 被局部噪声振幅加权；$\partial_w(g\rho)$ 表示这种加权密度的空间梯度；外面的 $g$ 再把这个梯度转成状态依赖的 diffusion flux。因此 $g=w$ 时，大城市不仅有更强的扩散强度，而且扩散算子本身也携带了由 $w$ 的变化带来的额外导数项。

### 9.2 从零通量条件推 Eq. 7.17

稳态要求

$$
\frac{\partial\rho}{\partial t}=0.
$$

若取无通量稳态，Fokker-Planck flux 为零：

$$
f(w)\rho
-
\sigma^2g(w)\frac{\partial}{\partial w}[g(w)\rho]
=0.
$$

代入

$$
f(w)=I(1-w)-\sigma^2w,
\qquad
g(w)=w,
$$

得到

$$
\left[I(1-w)-\sigma^2w\right]\rho
=
\sigma^2w\frac{d}{dw}[w\rho].
$$

令

$$
y(w)=w\rho(w).
$$

则

$$
\rho(w)=\frac{y(w)}{w}.
$$

代入上式：

$$
\left[I(1-w)-\sigma^2w\right]\frac{y}{w}
=
\sigma^2w\frac{dy}{dw}.
$$

两边除以 $\sigma^2w y$：

$$
\frac{1}{y}\frac{dy}{dw}
=
\frac{I(1-w)-\sigma^2w}{\sigma^2w^2}.
$$

右边展开：

$$
\frac{I(1-w)-\sigma^2w}{\sigma^2w^2}
=
\frac{I}{\sigma^2w^2}
-
\frac{I}{\sigma^2w}
-
\frac{1}{w}.
$$

因此

$$
\frac{d\log y}{dw}
=
\frac{I}{\sigma^2w^2}
-
\left(1+\frac{I}{\sigma^2}\right)\frac{1}{w}.
$$

对 $w$ 积分：

$$
\log y
=
-
\frac{I}{\sigma^2w}
-
\left(1+\frac{I}{\sigma^2}\right)\log w
+
C.
$$

指数化：

$$
y(w)
=
C
\exp\left[
-\frac{I}{\sigma^2w}
\right]
w^{-\left(1+I/\sigma^2\right)}.
$$

因为

$$
\rho(w)=\frac{y(w)}{w},
$$

所以

$$
\rho(w)
=
C
\frac{
\exp\left[-I/(\sigma^2w)\right]
}{
w^{2+I/\sigma^2}
}.
$$

令

$$
\mu=1+\frac{I}{\sigma^2},
$$

则

$$
2+\frac{I}{\sigma^2}
=
1+\mu,
$$

并且

$$
\frac{I}{\sigma^2}
=
\mu-1.
$$

因此

$$
\rho(w)
=
C_\rho
\frac{
\exp\left[-\frac{\mu-1}{w}\right]
}{
w^{1+\mu}
}.
\tag{7.17}
$$

这里 $C_\rho$ 是 normalization constant。笔记不用 $\mathcal{N}$ 表示它，是为了避免和 Chapter 9 的 neighbor number $\mathcal{N}(i)$ 混淆。

书中 Eq. 7.18 把 exponent 写成 migration coupling 和 internal growth noise 的比值。为了避免和 pairwise flow $J_{ij}$ 混淆，这里统一用前面 mean-field notation 的 $I$ 表示 migration coupling：

$$
\mu
=
1+\frac{I}{\sigma^2}.
\tag{7.18}
$$

如果原书在这一行使用 $J$，它和这里的 $I$ 是同一类 exchange intensity。为了读公式，关键不是字母，而是比例：

$$
\text{tail exponent}
\quad
\mu
=
1+
\frac{\text{migration coupling}}{\text{internal growth noise}}.
$$

这里有一个容易混淆的点：$\mu$ 不是 density 里 $w$ 的完整幂指数。Eq. 7.17 的 large-size density tail 是

$$
\rho(w)\sim w^{-1-\mu}.
$$

所以 density exponent 是 $1+\mu$。但在 Pareto 分布或 city-size literature 中，人们常把 cumulative tail 写成

$$
P(W>w)\sim w^{-\mu}.
$$

因为

$$
\int_w^\infty u^{-1-\mu}\,du
\propto
w^{-\mu}.
$$

因此，书中说的 exponent $\mu$ 更接近 Pareto tail exponent，也就是 cumulative tail exponent；而 density 本身多出一个 $+1$。

这样 Eq. 7.18 的含义就更清楚了。迁移耦合 $I$ 越强，$\mu$ 越大，cumulative tail

$$
P(W>w)\sim w^{-\mu}
$$

下降得越快，大城市极端值越少。内部随机增长噪声 $\sigma^2$ 越强，$\mu$ 越小，tail 越厚，极端大城市越容易出现。

也就是说，$I/\sigma^2$ 是一个竞争比值。分子 $I$ 代表城市之间的 exchange 或 migration smoothing：它把过大的城市往平均拉，把过小的城市往平均补。分母 $\sigma^2$ 代表每个城市内部 multiplicative growth 的不确定性：它会不断把城市规模随机放大或缩小。Eq. 7.18 说，城市规模分布的尾部厚度由这两股力量的相对强弱决定，而不是由某个单独参数决定。

### 9.3 Eq. 7.17 的物理含义

Eq. 7.17 有两个因子：

$$
\rho(w)
\propto
\exp\left[-\frac{\mu-1}{w}\right]
w^{-1-\mu}.
$$

先读变量本身。这里

$$
w=\frac{S}{\bar{S}}
$$

不是城市绝对人口，而是城市相对平均规模。如果 $w=1$，说明这个城市等于系统平均城市规模；如果 $w\gg1$，说明它是远大于平均值的大城市；如果 $w\ll1$，说明它是远小于平均值的小城市。

Eq. 7.17 说的是：在长期稳态中，随机抽取一个城市，它的相对规模 $w$ 会服从什么分布。这个分布的形状由两个因子共同决定。

第一，$w^{-1-\mu}$ 给出 large-$w$ tail。因为当

$$
w\to\infty,
$$

指数项满足

$$
\exp\left[-\frac{\mu-1}{w}\right]\to1.
$$

所以大城市尾部为

$$
\rho(w)\sim w^{-1-\mu}.
$$

这部分来自 multiplicative growth。只要增长是比例式的，已经大的城市在受到正向随机冲击时会获得更大的绝对增量；长期累积后，分布就容易产生 fat tail。这里的 power-law tail 表示：虽然极大城市少，但它们不是按 Gaussian 或 exponential 那样快速消失，而是以幂律方式缓慢衰减。

第二，指数项

$$
\exp\left[-\frac{\mu-1}{w}\right]
$$

控制小 $w$。当

$$
w\to0,
$$

指数里的 $-(\mu-1)/w$ 趋向 $-\infty$，因此

$$
\rho(w)\to0.
$$

这句话不能读成“城市绝对不能接近 0”。模型里没有设置一个硬性的 lower boundary。更准确地说，migration regularization 让稳态分布在 $w=0$ 附近出现 soft cutoff：非常小的相对规模不是不可能，而是概率密度被指数项强烈压低。

原因来自 migration drift。如果只有 multiplicative noise，小城市一旦连续遭遇负向冲击，就可能越来越接近 0。加入 migration 后，当

$$
w<1
$$

时，migration 项

$$
I(1-w)>0
$$

会给小城市一个向上拉回平均值的力。这个正 drift 不会像 reflective barrier 那样把城市硬反弹回去，但会持续削弱 $w\to0$ 附近的概率堆积。因此，小 $w$ 区域不是单纯由 power law 控制，而是被

$$
\exp\left[-\frac{\mu-1}{w}\right]
$$

快速压低。这个因子可以看成 migration 对小城市灭失风险的软保护。

所以 Bouchaud-Mezard 分布同时有两个特征：

$$
\text{small }w\text{ cutoff}
+
\text{large }w\text{ Pareto tail}.
$$

这和 Gabaix 的 lower barrier 很不同。Gabaix 用 reflective lower boundary 人为阻止城市跌破 $S_{\min}$；Bouchaud-Mezard 用 migration exchange 产生一个软的下端 regularization。

从机制上看，Eq. 7.17 可以读成一个平衡结果：

$$
\text{multiplicative noise creates dispersion}
\quad
\text{while}
\quad
\text{migration exchange restores average scale}.
$$

大城市尾部由前者主导，所以出现 Pareto tail；小城市端由后者主导，所以不会堆积到 $w=0$。这就是 Bouchaud-Mezard 模型比单纯 Gibrat growth 多出来的解释力：它不是只说“随机增长会产生不平等”，而是进一步说明 migration coupling 如何决定不平等的厚度。

### 9.4 mobility 如何控制 heterogeneity

由

$$
\mu=1+\frac{I}{\sigma^2}
$$

可以直接读出 migration 和 noise 的竞争。

如果 migration coupling $I$ 很小，但非零，则

$$
\mu\gtrsim1.
$$

此时 tail exponent $1+\mu$ 介于 2 附近，分布很厚。它有有限平均值

$$
\langle w\rangle=1,
$$

但当

$$
1<\mu<2,
$$

方差发散。这表示城市相对规模仍然有巨大波动，少数城市可以远大于平均值。

如果 migration coupling $I$ 增大，则

$$
\mu
=
1+\frac{I}{\sigma^2}
$$

也增大，Pareto tail 变薄。物理含义是：mobility 越强，城市之间交换越频繁，migration 越能把过大的城市拉回平均、把过小的城市补上，因此 city-size heterogeneity 下降。

反过来，如果 internal random growth noise $\sigma^2$ 增大，则

$$
\frac{I}{\sigma^2}
$$

变小，$\mu$ 下降，尾部变厚。噪声越强，城市之间的随机放大越强，migration homogenization 越难压住极端大城市。

所以这一节给出的机制解释是：

$$
\text{Pareto exponent}
=
\text{migration smoothing strength}
/
\text{multiplicative noise strength}.
$$

---

## 十、Solomon-Richmond：更一般的 redistribution equation

### 10.1 Eq. 7.19：generalized Lotka-Volterra 形式

Solomon 和 Richmond 提出类似 Eq. 7.10 的广义形式：

$$
\frac{dS_i}{dt}
=
\left[
\eta_i
+
c_i(\{S_i\},t)
\right]S_i
+
a_i\sum_jb_jS_j.
\tag{7.19}
$$

这条式子可以分成三部分。

第一部分是 multiplicative noise：

$$
\eta_iS_i.
$$

这里 $\eta_i$ 是 Gaussian noise，均值为 0，方差为 $\sigma_i^2$。

第二部分是 arbitrary growth term：

$$
c_i(\{S_i\},t)S_i.
$$

$c_i$ 可以依赖整个城市系统状态，也可以随时间变化。它代表城市 $i$ 的系统性增长或衰退条件。

第三部分是 redistribution：

$$
a_i\sum_jb_jS_j.
$$

其中

$$
U(t)=\sum_jb_jS_j
$$

可以看成一个加权总资源池。$b_jS_j$ 表示城市 $j$ 对这个资源池的贡献，$a_i$ 表示城市 $i$ 从资源池中获得的份额强度。因此 $a_ib_j$ 可以读作从 $j$ 到 $i$ 的 redistribution fraction。

### 10.2 Eq. 7.20：为什么要让 $c_i$ 相同

如果 $c_i$ 任意不同，系统会产生越来越强的不平等。特别是，若某些城市的 $c_i$ 很负，它们会长期衰退，甚至消失。

为了得到可解析的稳态分布，Solomon-Richmond 考虑所有城市共享同一个 $c$：

$$
c_i(S_1,S_2,\ldots,S_N,t)
=
c(S_1,S_2,\ldots,S_N,t).
\tag{7.20}
$$

这意味着城市之间的差异主要来自 $\eta_i$、$a_i$、$b_i$ 和 $\sigma_i$，而不是每个城市拥有完全不同的 deterministic growth environment。

在这个条件下，可以研究归一化变量

$$
x_i=\frac{S_i}{U(t)},
$$

其中

$$
U(t)=\sum_jb_jS_j.
$$

和 Bouchaud-Mezard 的 $w_i=S_i/\bar{S}$ 一样，这里的 $x_i$ 也是相对规模变量。目标不是解释总规模增长，而是解释各城市在总系统中的相对份额。

### 10.3 Eq. 7.21 和 Eq. 7.22：robust Pareto tail

在 constant $\sigma_i$ 和 $a_i$ 的条件下，归一化变量 $x_i$ 的分布为

$$
P(x_i)
\sim
\frac{1}{x_i^{1+\alpha_i}}
\exp\left[
-\frac{2a_i}{x_i\sigma_i^2}
\right].
\tag{7.21}
$$

指数为

$$
\alpha_i
=
1+\frac{2a}{\sigma_i^2},
\tag{7.22}
$$

其中

$$
a=\sum_i b_ia_i.
$$

这和 Bouchaud-Mezard 的 Eq. 7.17 结构一致：

$$
\text{small-size exponential cutoff}
+
\text{large-size power-law tail}.
$$

当 $x_i$ 很大时，

$$
\exp\left[
-\frac{2a_i}{x_i\sigma_i^2}
\right]\to1,
$$

于是

$$
P(x_i)\sim x_i^{-1-\alpha_i}.
$$

当 $x_i$ 很小时，指数项会强烈压低概率，防止相对规模趋近 0。

这说明 Bouchaud-Mezard 的 mean-field result 不是一个脆弱结论。即使把 redistribution 写得更一般，只要有 multiplicative noise 和某种系统性 redistribution，仍然容易得到 Pareto-like tail。

---

## 十一、这一章对城市增长问题的结论

这一章给 Chapter 6 的 growth models 加上了来源机制。核心结论可以压成三条。

第一，migration 会破坏 pure Simon power-law。Haran-Vining 模型表明，一旦城市之间允许人口双向流动，size distribution 不再只是单向 preferential attachment 的结果，log-log 图会出现 curvature。

第二，migration 可以作为 Gibrat process 的 regularization。Bouchaud-Mezard 模型表明，内部随机增长会制造不平等，而城市间 exchange 会把城市拉向平均值。二者竞争后，可以产生 stationary Pareto distribution。

第三，Pareto exponent 不再只是数学边界条件的结果，而可以由 migration strength 和 growth noise 的相对大小决定：

$$
\mu
=
1+
\frac{\text{migration coupling}}{\text{growth noise strength}}.
$$

这比 Gabaix 的 reflective barrier 更有城市机制含义：城市不会因为碰到某个抽象下界而反弹，而是因为城市之间存在实际的人口交换。

但作者也保留了警惕。Bouchaud-Mezard 的完整图假设所有城市以同样强度交换：

$$
I_{ij}=\frac{I}{N}.
$$

这个假设未必真实。真实 migration 显然会依赖距离、交通网络、区域边界、经济联系和历史路径。因此，这一章的模型不是最终答案，而是把一个更经验化的问题推到前台：

$$
\text{真实 migration network 的结构会怎样改变城市增长方程?}
$$

这也自然引向下一章和后续章节：如果迁移不是均匀扩散，而是有距离、网络和 rare events，那么城市增长可能不再由 Brownian noise 主导，而要考虑更重尾、更突发的动力学。
