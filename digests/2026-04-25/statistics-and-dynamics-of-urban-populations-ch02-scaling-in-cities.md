---
title: "Statistics and Dynamics of Urban Populations, Chapter 2: Why does population matter?"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-25"
topics: ["urban scaling", "城市人口", "scaling laws", "local exponent", "tomography plot", "城市定义"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/02-why-does-population-matter.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 2：Scaling in Cities

## 精读笔记

---

## 一、这一章真正要回答的问题

这一章表面上叫 **Why does population matter?**，但它真正要处理的问题不是“人口当然重要”这一类常识判断，而是一个更具体的建模问题：

**如果城市有大小差异，我们能不能用人口 $S$ 作为城市尺度变量，并用一个 scaling law 来比较不同城市的宏观量 $Y$？**

这个问题之所以重要，是因为城市之间差异极大。小镇可能只有几万人，megacity 可以超过一千万人。只说“大城市更多”“小城市更少”没有解释力。真正需要判断的是：当城市人口扩大时，某个城市量 $Y$ 是按同样比例扩大，还是扩大得更快，或者扩大得更慢。

因此，这一章的逻辑不是直接接受 urban scaling，而是先建立它的吸引力，再逐步拆解它的风险。作者的论证顺序可以压成一条线：

1. 人口是城市最自然的一阶尺度变量；
2. scaling law 把“城市大小差异”转化为指数 $\beta$ 的问题；
3. $\beta = 1$ 和 $\beta \neq 1$ 对城市机制的含义完全不同；
4. 但用 log-log 拟合估计 $\beta$ 很容易被噪声、城市定义和样本范围误导；
5. 因此，作者引入 probabilistic testing 和 local exponent / tomography plot 来检查 scaling 是否真的可靠。

这一章最值得记住的不是某个具体指数，而是作者给出的判断标准：**urban scaling 不是看到一条 log-log 直线就成立，而是要看指数是否稳健、是否能预测、是否不依赖拟合假设。**

---

## 二、为什么先从人口开始

作者先把城市研究放回一个一般系统问题里。研究一个复杂系统时，可以先问它的输入和输出关系：

$$
Y = f(X).
$$

这里 $X$ 和 $Y$ 不是微观个体状态，而是描述系统的宏观量。对城市来说，$X$ 可以有很多选择，例如面积、GDP、政治地位、基础设施规模。但作者认为，最自然的起点是人口 $S$。原因很直接：城市不是单纯占据空间的物体，而是由居民、活动、交互和基础设施组成的系统；没有居民的“城市”即使占据空间，也很难构成有意义的城市对象。

一旦把人口当作尺度变量，城市比较就变成：某个宏观量 $Y$ 怎样随 $S$ 变化。最朴素的基准是线性关系：

$$
f(\lambda X) = \lambda f(X).
$$

如果一个城市人口翻倍，某个量也正好翻倍，那么人均量 $Y/S$ 保持不变。此时城市大小本身没有改变这个量的生产方式，只是把同样的单位贡献复制了更多份。

这个线性基准很重要，因为它给后面的 scaling law 提供了参照。比如，如果大城市拥有更多专利，这本身并不说明大城市更创新；因为人口更多，本来就可能有更多专利。真正的问题是：专利数是否比人口增长得更快。如果专利人均值随人口上升，那才说明大城市规模可能带来了额外的交互效应。

所以本章第一步是把“城市比较”从原始总量比较，转成相对于人口尺度的比较。

---

## 三、scaling law 的承诺：用一个指数组织城市差异

进入 `Scaling in cities` 后，作者把城市 scaling 放到更宽的科学传统里。Scaling law 在生物学、聚合物物理、相变、湍流和复杂系统里都很重要，因为它通常提供两类信息。

第一，scaling 暗示 self-similarity。这里的 self-similarity 不是说大城市和小城市在地图形状上长得一样，也不是说大城市只是把小城市等比例放大。它说的是：当城市人口从 $S$ 增加到 $\lambda S$ 时，某些宏观量 $Y$ 的变化可以由一个稳定的尺度变换规则描述。如果这个规则存在，那么不同规模的城市虽然具体历史、地理和制度不同，但在某个统计关系上仍然可以互相比较。

对城市来说，这就是一个很强的假设。它等于说，大城市在某些方面可以被理解为小城市的 scaled-up version：不是逐条街道、逐个社区都相似，而是道路总长、GDP、专利数、剧院数量、能源消耗这类宏观量与人口之间存在稳定比例关系。这样一来，我们就可以用人口比 $S_2/S_1$ 把一个城市的量 $Y_1$ 推到另一个城市的量 $Y_2$。如果这个假设失败，说明城市之间的差异不能只靠人口尺度解释，还必须引入边界定义、历史路径、空间结构或制度条件。

第二，scaling exponent 可以提示机制。指数 $\beta$ 不只是拟合曲线的斜率，而是在问：城市规模增加时，单位人口贡献是否改变。如果 $\beta=1$，系统只是线性复制；人口翻倍，总量也翻倍。这个结果可以看作“无额外相互作用”的基准。如果 $\beta\neq 1$，就说明规模改变了单位人口的平均贡献，城市内部一定有某种非线性效应需要解释。

这种解释力在指数不能由简单量纲分析推出时尤其重要。比如面积和长度的关系可以由几何量纲给出，但专利、工资、犯罪、交通延误、基础设施长度这类城市量没有简单的几何维度决定它们怎样随人口增长。如果这些量稳定地表现出 $\beta>1$ 或 $\beta<1$，指数就变成机制线索：superlinear 可能指向交互密度、知识溢出或社会接触网络；sublinear 可能指向基础设施共享、空间压缩或规模经济。换句话说，非平凡 exponent 本身不是机制，但它告诉我们：这里可能存在单纯线性加总无法解释的组织原则、相互作用或约束。

城市 scaling 的基本形式是：

$$
Y = a S^\beta.
$$

这里 $Y$ 是城市宏观量，$S$ 是城市人口，$a$ 是 prefactor，$\beta$ 是 scaling exponent。这个式子最直接的含义体现在人均量上：

$$
\frac{Y}{S} \sim S^{\beta - 1}.
$$

因此，$\beta$ 的三种情况对应三种城市解释。

当 $\beta = 1$，$Y/S$ 与城市规模无关。这是线性情形，说明城市大小没有改变单位人口的平均贡献。

当 $\beta < 1$，$Y/S$ 随人口下降。这通常被解释为 decreasing returns 或规模经济。例如某些基础设施不需要随人口等比例增加，所以大城市在这类资源上可能更节省。

当 $\beta > 1$，$Y/S$ 随人口上升。这被解释为 increasing returns，常被用来讨论创新、工资、专利、犯罪等依赖交互密度的社会经济过程。

这就是 Bettencourt 等 urban scaling 工作的核心吸引力：它把城市复杂性压缩成一个可估计、可比较、可解释的指数。

---

## 四、scaling hypothesis 是强假设，不是默认事实

作者随后提醒，scaling hypothesis 其实很强。它假设人口是城市性质的主要决定变量，也就是说，相同人口规模的城市应当具有相似性质；不同人口规模的城市可以通过 $S$ 的比例关系互相预测。

这个假设有两个研究方式。

第一种是 vertical approach：跟踪同一座城市随时间演化，看 $Y(t)$ 怎样随 $S(t)$ 变化。这里研究的是城市自身的历史路径。

第二种是 horizontal approach：在同一时间收集许多城市的 $(S_i, Y_i)$，再做横截面 scaling。绝大多数 urban scaling 研究采用的是这种方式。

关键问题在于：这两种方式不一定等价。一个城市今天的人口和拥堵、基础设施、产业结构之间的关系，可能强烈依赖它过去的发展路径。作者举 congestion-induced traffic delays 的研究说明，某些城市量不仅依赖当前人口，还依赖整个系统历史。这样一来，简单的 $Y = aS^\beta$ 就可能失效。

所以这里的线性逻辑是：scaling 可以提供跨城市比较的语言，但它同时抹掉了城市历史、边界定义和路径依赖。它不是一个天然成立的城市定律，而是一个必须被检验的建模假设。

---

## 五、为什么 $\beta \neq 1$ 的判断如此关键

本章反复强调，判断 $\beta$ 是否显著不同于 1，比估计 $\beta$ 的小数点后几位更重要。

原因是 $\beta = 1$ 和 $\beta \neq 1$ 对应完全不同的城市图像。

如果 $\beta = 1$，那么人均量不随城市规模变化。城市大小只是复制了更多人口单位，没有产生额外的非线性效应。

如果 $\beta \neq 1$，那么城市规模改变了单位人口的贡献。此时城市内部的相互作用、基础设施共享、空间组织、交通成本或社会接触网络就必须进入解释。

这也是为什么 Bettencourt 的理论会试图解释 superlinear socio-economic quantities。例如工资、专利等社会经济量可能随人口以 $1+\delta$ 的指数增长，其中 $\delta$ 被联系到城市中个体路径的分形维数。这个解释很有吸引力，因为它把宏观 scaling exponent 接到了个体移动、交互和城市空间结构上。

但作者也指出，这类理论仍然偏 phenomenological。它能给出一种机制想象，却很难严格连接微观机制和集体涌现行为。换句话说，non-trivial $\beta$ 是一个机制线索，但不是机制本身。

---

## 六、直接 log-log 拟合的问题

通常估计 $\beta$ 的方法，是把 $Y$ 和 $S$ 画在 log-log 坐标里，用 ordinary least squares 找一条直线。因为

$$
\log Y = \log a + \beta \log S,
$$

所以幂律拟合在 log-log 图上变成线性拟合。

作者强调，这种方法只有在几个条件大致满足时才可靠：

1. 两个轴上都有足够多的数量级跨度；
2. 噪声不能太大；
3. 如果要证明非线性，$\beta$ 必须清楚地不同于 1。

城市数据经常不满足这些条件。美国城市 GDP 的例子很典型：非线性拟合得到 $\hat{\beta} \simeq 1.13$，而且 $R^2 = 0.98$ 很高。但这个结果并不自动说明 GDP 明确 superlinear。因为数据只有大约两个数量级的跨度，$\beta$ 又很接近 1，而且线性拟合同样不错。

这说明高 $R^2$ 不能证明非线性 scaling。特别是在 $\beta$ 接近 1 的灰区里，模型选择、噪声结构和城市边界定义都会影响结论。

作者还指出，城市定义本身会改变 scaling exponent。Arcaute 等人的研究表明，用不同 commuter threshold 和 density threshold 定义城市时，一些非线性量的 exponent 不仅会波动，甚至可能从大于 1 变成小于 1。这对 urban scaling 是根本挑战：如果一个指数依赖城市边界定义，它就很难被当作稳定机制指标。

因此，本章到这里完成了一个重要转折：**scaling law 很有解释力，但直接拟合得到的 $\hat{\beta}$ 很脆弱。**

---

## 七、公式链总览：作者怎样从 Eq. 2.3 推到 Eq. 2.21

`Scaling in cities` 这一节不是只提出一个幂律公式。它的公式链分成三段，每一段都在解决一个不同问题。

第一段是 Eq. 2.3 到 Eq. 2.8。这里作者先给出经典 scaling law，然后把它改写成概率模型。逻辑目标是：不要只问点是否落在一条 log-log 直线上，而要问城市量 $Y$ 在给定人口 $S$ 时的条件分布是否支持 $\beta \neq 1$。

第二段是 Eq. 2.9 到 Eq. 2.14。这里作者从“全体城市拟合一条线”转向“两座城市之间能否互相预测”。逻辑目标是：如果 scaling 真成立，任意两座城市之间的局部指数 $\beta_{\mathrm{loc}}$ 应该在大人口比下收敛到同一个 $\beta$。

第三段是 Eq. 2.15 到 Eq. 2.21。这里作者把 local exponent 变成 practical prediction tool。逻辑目标是：选出一个 benchmark city，计算 effective exponent，再看这个指数能把多少城市预测到合理误差范围内。

所以这一节的公式不是并列定义，而是一条检验链：

$$
\text{global power law}
\rightarrow
\text{probabilistic scaling}
\rightarrow
\text{pairwise local exponent}
\rightarrow
\text{benchmark prediction}.
$$

这条链最后要回答的不是“$\hat{\beta}$ 等于多少”，而是“这个 $\beta$ 是否稳定到可以用来解释和预测城市差异”。

---

## 八、Eq. 2.3 到 Eq. 2.8：从幂律拟合到概率模型

### 8.1 Eq. 2.3：经典 scaling law

城市 scaling 的起点是：

$$
Y = a S^\beta. \tag{2.3}
$$

这里 $S$ 是城市人口，$Y$ 是某个城市宏观量，$a$ 是 prefactor，$\beta$ 是 scaling exponent。这个式子做了一个强假设：城市之间的差异主要可以由人口尺度解释，剩余差异可以先看成波动。

它的解释力来自人均量：

$$
\frac{Y}{S} = a S^{\beta - 1}.
$$

如果 $\beta = 1$，人均量不随城市人口变。城市变大只是复制更多人口单位，没有额外规模效应。

如果 $\beta < 1$，人均量随人口下降。常见解释是基础设施或资源使用存在规模经济。例如道路、管网、某些公共设施不必随人口等比例增加。

如果 $\beta > 1$，人均量随人口上升。常见解释是城市交互、创新、工资、犯罪等社会经济过程会被人口密度和互动机会放大。

所以 Eq. 2.3 的关键不在于形式简单，而在于它把城市机制判断压缩到 $\beta$ 是否等于 1 上。

### 8.2 Fig. 2.4：为什么高 $R^2$ 不能证明非线性

![Fig. 2.4 — US GDP 的线性拟合和幂律拟合都很好](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-06-figure-01.jpg)

Fig. 2.4 是这一节的第一个反例。图中横轴是人口 $S$，纵轴是 GDP，都是 log scale。黑点是美国 MSA 数据，红线是 power-law fit，绿线是 linear fit。

红线给出 $\hat{\beta} \simeq 1.13$，看起来是 superlinear，而且 $R^2 = 0.98$。如果只看这个数，很容易得出“大城市 GDP 超线性增长”的结论。

但图里绿线也同样贴合数据，$R^2$ 也接近 0.98。这说明，数据范围和噪声水平不足以清楚区分 $\beta = 1$ 和 $\beta = 1.13$。作者用这张图说明：当 exponent 接近 1、样本只有有限数量级跨度时，log-log 直线和高 $R^2$ 不是可靠证据。

这张图把后面的统计检验引出来。因为问题不再是“能不能拟合出一条幂律”，而是“能不能拒绝线性假设”。

### 8.3 Eq. 2.4：把 scaling 放进条件期望

Leitao et al. 的思路是把 scaling 写成概率模型的均值结构：

$$
\mathbb{E}(y \mid x) = \alpha x^\beta. \tag{2.4}
$$

这里 $x$ 是城市人口，$y$ 是城市量。这个式子和 Eq. 2.3 看起来相似，但意义更严格。Eq. 2.3 像是在说数据点大致落在 $aS^\beta$ 附近；Eq. 2.4 则说，在给定人口 $x$ 后，城市量 $y$ 是一个随机变量，而它的条件均值满足幂律。

这一步很重要，因为城市数据本来就有大量波动。两个相同人口的城市不可能有完全相同 GDP、道路里程或剧院数量。把 $y$ 写成随机变量以后，波动不再只是拟合残差，而成为模型的一部分。

### 8.4 Eq. 2.5：期望值不是符号，而是由条件分布定义

Eq. 2.5 明确了条件期望的定义：

$$
\mathbb{E}(f(y) \mid x) = \int f(y) P(y \mid x)\,dy. \tag{2.5}
$$

这一步看似基础，但它把问题推进了一层：只给出均值 $\mathbb{E}(y \mid x)$ 还不够，因为真正决定 likelihood 的是整个条件分布 $P(y \mid x)$。

换句话说，scaling 检验不只需要一条均值曲线，还需要回答：在这条曲线周围，数据应该怎样波动？波动是 Gaussian、log-normal，还是更复杂？波动的方差是否随城市规模改变？

### 8.5 Eq. 2.6：Taylor's law 给波动结构加约束

作者随后引入方差和均值之间的关系：

$$
\mathbb{V}(y \mid x) = \gamma \mathbb{E}(y \mid x)^\delta. \tag{2.6}
$$

这个式子是 Taylor's law。它说城市量的波动强度不是常数，而是随均值改变。城市越大，$Y$ 的均值往往越大，绝对波动也可能越大；但这个波动增加得多快，需要由 $\delta$ 控制。

这一步的作用是把“噪声”结构化。没有 Eq. 2.6，所有偏离均值曲线的点都只是残差；有了 Eq. 2.6，模型就可以区分两种情况：某个城市偏离大，是因为 scaling law 失败，还是因为大城市本来就允许更大的条件方差。

### 8.6 Eq. 2.7：选择一个可计算的条件分布

为了真正计算 likelihood，作者需要指定 $P(y \mid x)$。一个选择是 Gaussian：

$$
P(y \mid x)
= \frac{1}{\sqrt{2\pi\sigma(x)^2}}
\exp\left[-\frac{(y-\mu(x))^2}{2\sigma(x)^2}\right]. \tag{2.7}
$$

其中 $\mu(x)=\alpha x^\beta$，$\sigma^2(x)=\gamma(\alpha x^\beta)^\delta$。这意味着均值由 scaling law 控制，方差由 Taylor's law 控制。

作者并不只考虑 Gaussian，也考虑 log-normal 等形式。这里的关键是：不同噪声模型会导致不同 $\beta$ 判断。也就是说，$\beta$ 是否显著不等于 1，不是独立于 fluctuation model 的纯数字问题。

### 8.7 Eq. 2.8：用 likelihood 同时估计指数和波动

给定 $P(y \mid x)$ 后，所有城市样本的 log-likelihood 写成：

$$
\ln \mathcal{L}
= \ln P(y_1,y_2,\dots,y_N \mid x_1,x_2,\dots,x_N)
= \sum_{i=1}^{N} \ln P(y_i \mid x_i). \tag{2.8}
$$

这个式子把统计检验落到可计算对象上。接下来可以最大化 $\mathcal{L}$ 来估计 $(\alpha,\beta,\gamma,\delta)$，也可以固定 $\beta=1$ 后重新计算 likelihood，再比较两个模型。

这一步的核心不是“更高级的拟合方法”，而是把 scaling 检验改成模型比较。作者要判断的是：允许 $\beta \neq 1$ 是否真的显著改善数据解释，还是只是多加一个参数后看起来更贴合。

Leitao et al. 的结果很谨慎。许多数据集上，候选概率模型本身会被数据拒绝。这说明问题不只是 $\beta$ 估计不稳，而是城市数据的生成和波动结构可能没有被这些简单模型捕捉。于是本章进入下一步：如果全局概率建模也不够令人满意，是否可以用更直接的 prediction test 来检查 scaling？

---

## 九、Eq. 2.9 到 Eq. 2.14：从全局拟合转向 pairwise local exponent

### 9.1 Eq. 2.9：scaling 的直接预测含义

作者先把 Eq. 2.3 改写成两个城市之间的预测关系：

$$
Y_2 = Y_1 \left(\frac{S_2}{S_1}\right)^\beta. \tag{2.9}
$$

这个式子把 scaling 的含义说得更实用。它不是问所有城市能否拟合一条线，而是问：如果我知道城市 1 的人口 $S_1$ 和城市量 $Y_1$，再知道城市 2 的人口 $S_2$，能否用人口比值预测 $Y_2$？

如果 scaling 真成立，城市 2 可以被看成城市 1 的 scaled-up 或 scaled-down version。这样，$\beta$ 就不只是描述性指数，而是预测指数。

### 9.2 Eq. 2.10：local exponent 是两座城市之间的斜率

反过来，如果 $Y_1,Y_2,S_1,S_2$ 都已知，可以问：哪一个指数会让 Eq. 2.9 对这两座城市刚好成立？答案是：

$$
\beta_{\mathrm{loc}}
= \frac{\log(Y_2/Y_1)}{\log(S_2/S_1)}. \tag{2.10}
$$

在 log-log 图上，$\beta_{\mathrm{loc}}$ 就是连接两个城市点的直线斜率。如果所有城市都落在同一条幂律上，那么任意城市对的 $\beta_{\mathrm{loc}}$ 都应该接近同一个 $\beta$。

这就是 tomography plot 的基础。作者不再只看一条全局拟合线，而是看所有城市对之间的局部斜率如何随人口比 $r=S_2/S_1$ 改变。

### 9.3 Eq. 2.11：乘法噪声下，人口比越大，噪声越不重要

作者先考虑乘法噪声：

$$
Y_2 = Y_1 \left(\frac{S_2}{S_1}\right)^\beta(1+\eta).
$$

代回 local exponent 得到：

$$
\beta_{\mathrm{loc}}
= \beta
+ \frac{\log(1+\eta)}{\log(S_2/S_1)}. \tag{2.11}
$$

这个式子解释了 tomography plot 为什么要以人口比 $r$ 为横轴。当 $r$ 很大时，$\log r$ 变大，噪声项被分母压低，$\beta_{\mathrm{loc}}$ 应该靠近真实 $\beta$。所以，如果 scaling 成立，local exponent 应该在大 $r$ 区域收敛。

反过来，如果 $r$ 很大时 $\beta_{\mathrm{loc}}$ 仍然不收敛，或者收敛到和全局拟合不一致的值，那就说明 simple scaling law 有问题。

### 9.4 Eq. 2.12：相似人口城市之间的比较最不稳定

如果两座城市人口很接近，可以写成 $S_2=S_1(1+\varepsilon)$，其中 $\varepsilon \ll 1$。此时：

$$
\beta_{\mathrm{loc}}
\simeq \beta + \frac{\log(1+\eta)}{\varepsilon}. \tag{2.12}
$$

这个式子说明，小人口差异会放大噪声。即使 $\eta$ 很小，只要 $\varepsilon$ 更小，$\beta_{\mathrm{loc}}$ 也可能变得很大、很负或非常波动。

因此，tomography plot 左侧通常会很散。这不是异常，而是公式预期。关键要看右侧：人口比足够大时，局部指数是否收敛。

### 9.5 Eq. 2.13 和 Eq. 2.14：加法噪声下也应当出现收敛

作者随后说明，这个收敛逻辑不依赖乘法噪声。若噪声是加法形式：

$$
Y_2 = Y_1\left(\frac{S_2}{S_1}\right)^\beta + \eta,
$$

则 local exponent 可以写成：

$$
\beta_{\mathrm{loc}}
= \beta
+ \frac{1}{\log r}
\log\left(1+\frac{\eta}{r^\beta Y_1}\right). \tag{2.13}
$$

当 $r$ 足够大时，噪声修正项近似为：

$$
\beta_{\mathrm{loc}}
\simeq \beta
+ \frac{1}{r^\beta \log r}\frac{\eta}{Y_1}. \tag{2.14}
$$

这说明，即使噪声不是乘法形式，只要 simple scaling law 是对的，大人口比下仍应看到 $\beta_{\mathrm{loc}}$ 向 $\beta$ 收敛。

因此，Eq. 2.11 到 Eq. 2.14 共同建立了一个判据：**local exponent 在小 $r$ 处可以乱，但在大 $r$ 处必须收敛。**

---

## 十、Eq. 2.15 到 Eq. 2.21：从 local exponent 到 benchmark prediction

### 10.1 Eq. 2.15：对每座城市计算 pairwise local exponent

作者接下来把两城公式推广到所有城市对。对固定城市 $i$ 和另一座城市 $j$：

$$
\beta_{\mathrm{loc}}(i,j)
= \frac{\log(Y_j/Y_i)}{\log r_{ij}}, \tag{2.15}
$$

其中 $r_{ij}=P_j/P_i$。这个式子把每座城市都变成一个候选参照点。问题变成：哪一座城市作为 reference 时，对其他城市的 scaling prediction 最稳定？

### 10.2 Eq. 2.16 和 Eq. 2.17：用平均值和方差寻找 benchmark city

对固定城市 $i$，作者计算它与所有其他城市的局部指数平均值：

$$
\left\langle \beta_{\mathrm{loc}}(i) \right\rangle
= \frac{1}{N-1}\sum_j \beta_{\mathrm{loc}}(i,j). \tag{2.16}
$$

然后计算这些局部指数的方差：

$$
\sigma^2(i)
= \left\langle \beta_{\mathrm{loc}}^2(i) \right\rangle
- \left\langle \beta_{\mathrm{loc}}(i) \right\rangle^2. \tag{2.17}
$$

如果某个城市 $i$ 的 $\sigma^2(i)$ 很小，说明以它为参照时，不同目标城市给出的 local exponent 波动较小。作者把方差最小的城市定义为 benchmark city，记作 $i_{\min}$。

这个定义很实用。全局拟合问的是“哪条线最贴近所有点”；benchmark city 问的是“如果我必须选一座城市作为标准城市，哪一座能最稳定地预测其他城市”。

### 10.3 Eq. 2.18：effective exponent 的预测式

对 benchmark city，局部指数平均值被称为 effective exponent：

$$
\beta_{\mathrm{eff}}
= \left\langle \beta_{\mathrm{loc}}(i_{\min}) \right\rangle.
$$

然后用它预测任意城市 $j$：

$$
Y(j)
= Y(i_{\min})
\left(\frac{S_j}{S_{i_{\min}}}\right)^{\beta_{\mathrm{eff}}}. \tag{2.18}
$$

这个式子和 Eq. 2.9 很像，但意义更明确。Eq. 2.9 假设我们已经知道一个理论 $\beta$；Eq. 2.18 则使用从 benchmark city 计算出来的 $\beta_{\mathrm{eff}}$。它是一个实践指数，不一定是理论指数。

### 10.4 Eq. 2.19：和 SAMI 的区别

作者接着提到 Scale-Adjusted Metropolitan Indicators，SAMI：

$$
\xi_i = \log \frac{Y_i}{Y_0 S_i^{\hat{\beta}}}. \tag{2.19}
$$

SAMI 的问题是：给定一个全局拟合指数 $\hat{\beta}$ 后，衡量某个城市相对于拟合线的偏离。它关心的是“城市是否高于或低于 scaling expectation”。

作者这里的方法不同。它不是先接受 $\hat{\beta}$，再看残差，而是先通过 pairwise local exponent 检查 scaling 是否稳定，并选择一个 effective exponent 用于预测。

所以 Eq. 2.19 的作用是划清边界：本文的 practical test 不是传统 residual ranking，而是 scaling validity 的诊断。

### 10.5 Eq. 2.20 和 Eq. 2.21：用预测命中率评价 scaling

最后，作者定义预测成功的区间：

$$
\varepsilon_1 Y_{\mathrm{data}}
< Y_{\mathrm{predicted}}
< \varepsilon_2 Y_{\mathrm{data}}. \tag{2.20}
$$

其中预测值由 benchmark city 给出：

$$
Y_{\mathrm{predicted}}
= Y(i_{\min})
\left(\frac{S}{S_{i_{\min}}}\right)^{\beta_{\mathrm{eff}}}. \tag{2.21}
$$

如果取 $\varepsilon_1=1/2$、$\varepsilon_2=2$，那么 $f(2)$ 就表示：有多少城市的预测值在真实值的一半到两倍之间。

这个指标很粗，但很有用。因为它直接回答 practical question：如果我们真的拿 scaling law 做预测，它大概能预测多少城市？这比单独报告 $\hat{\beta}$ 和 $R^2$ 更接近应用判断。

---

## 十一、配图链：每张图在论证中的作用

### 11.1 Fig. 2.4：拟合看起来很好，但结论仍然不稳

![Fig. 2.4 — GDP 的线性拟合和幂律拟合几乎都能解释数据](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-06-figure-01.jpg)

Fig. 2.4 是 fitting problem 的视觉版本。红线是 $\beta=1.13$ 的幂律拟合，绿线是线性拟合。两条线都穿过数据云，$R^2$ 都很高。

作者用它说明，在 $\beta$ 接近 1、样本跨度不够大、噪声仍然存在时，单靠 log-log plot 很难证明非线性。图的任务不是支持 GDP superlinearity，而是警告：看起来漂亮的幂律拟合可能没有足够判别力。

### 11.2 Fig. 2.5：先给出两个清楚的 global-fit 案例

![Fig. 2.5a — US GDP 的 superlinear fit](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-13-figure-01.jpg)

![Fig. 2.5b — US road miles 的 sublinear fit](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-13-figure-02.jpg)

Fig. 2.5 进入 practical test 的案例部分。左图是美国城市 GDP，拟合得到 $\hat{\beta}=1.11$；右图是道路总里程，拟合得到 $\hat{\beta}=0.85$。

这两张图提供两个相反类型的 scaling：GDP 是 superlinear，说明大城市的人均经济产出更高；道路里程是 sublinear，说明基础设施长度不需要随人口等比例增加。作者先选这两个案例，是为了展示 local exponent 方法在清楚案例中应当能确认 naive fit。

### 11.3 Fig. 2.6：tomography plot 验证清楚案例

![Fig. 2.6a — US GDP 的 local exponent 收敛到 superlinear 值](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-13-figure-03.jpg)

![Fig. 2.6b — US road miles 的 local exponent 收敛到 sublinear 值](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-13-figure-04.jpg)

Fig. 2.6 是 Eq. 2.10 到 Eq. 2.14 的图像化。灰点是所有城市对的 $\beta_{\mathrm{loc}}$，蓝线是分箱平均，红线是线性基准 $\beta=1$，绿线是全局幂律拟合值。

GDP 图中，蓝线稳定在 1 以上，并接近 $\hat{\beta}=1.11$。这说明 superlinear 不只是全局拟合造成的，而是在不同人口比的城市对里都能看到。

道路里程图中，蓝线稳定在 1 以下，并接近 $\hat{\beta}=0.85$。这说明 sublinear 基础设施 scaling 也被 pairwise comparison 支持。

两张图共同说明：当 scaling 真的比较清楚时，tomography plot 会让 $\beta_{\mathrm{loc}}$ 在大 $r$ 处收敛到全局拟合指数。

### 11.4 Fig. 2.7：人均 GDP 仍然保留非线性信号

![Fig. 2.7 — GDP per capita 的 local exponent 收敛到正值](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-14-figure-01.jpg)

Fig. 2.7 回应 Shalizi 的批评：如果 GDP superlinearity 只是因为使用了 extensive quantity，那么改成人均 GDP 后非线性应当消失。

但图中蓝线在大多数 $r$ 上收敛到约 0.11，而不是 0。这个 0.11 正好对应总量 exponent 的 $\hat{\beta}-1$。这说明至少在美国 GDP 案例中，superlinear signal 不是单纯由总量变量造成的。

这张图的作用是把讨论从“总量幂律是否假象”推进到“人均量是否也存在稳定尺度效应”。

### 11.5 Fig. 2.8：UK rail stations 暴露 threshold effect

![Fig. 2.8a — UK rail stations 的线性、阈值和幂律拟合](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-15-figure-01.jpg)

![Fig. 2.8b — UK rail stations 的 local exponent 不支持简单线性](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-15-figure-02.jpg)

Fig. 2.8 是第一个“拟合结论被拆开”的案例。左图里很多城市的 station count 等于 1 或接近 0，这说明数据不是普通连续幂律云，而带有明显离散和阈值结构。

红线是线性拟合，绿线是 $a+bS$，蓝线是幂律拟合。$a+bS$ 中 $a<0$ 的形式意味着存在一个人口阈值：低于阈值时城市可能没有铁路站，超过阈值后才近似线性增长。

右图的 tomography plot 显示 $\beta_{\mathrm{loc}}$ 波动很大，而且平均值低于 1。它不干净地支持线性，也不稳定地支持幂律。作者据此认为，这个案例不能简单说成 $\beta=1$，更可能包含 threshold effect 或其他 scaling form。

### 11.6 Fig. 2.9：Brazil AIDS cases 也可能不是简单 sublinear

![Fig. 2.9a — Brazil AIDS cases 的幂律拟合和阈值型拟合](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-16-figure-01.jpg)

![Fig. 2.9b — Brazil AIDS cases 的 local exponent 不清楚收敛](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-16-figure-02.jpg)

Fig. 2.9 延续 Fig. 2.8 的逻辑。左图中 power-law fit 给出 $\hat{\beta}=0.74$，看似 sublinear；但带阈值的形式也能解释数据。

右图中 local exponent 在某些人口比附近接近 1，在其他区域又低于 1，没有稳定收敛到单一指数。作者因此认为，原先的 sublinear 结论可能被 threshold 或线性机制挑战。

这张图说明，local exponent 不只是确认非线性，也能提示“幂律形式本身可能错了”。

### 11.7 Fig. 2.10：cinema capacity 支持线性 scaling

![Fig. 2.10a — cinema capacity 的 local exponent 收敛到 1](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-17-figure-01.jpg)

![Fig. 2.10b — cinema capacity 的 prediction ratio，多数城市落在灰区](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-17-figure-02.jpg)

Fig. 2.10 展示 local exponent 和 prediction ratio 如何一起使用。左图中 $\beta_{\mathrm{loc}}$ 收敛到 1，支持 cinema capacity 与人口近似线性。

右图展示 $Y_{\mathrm{predicted}}/Y_{\mathrm{data}}$。灰色区域是预测值在真实值一半到两倍之间的范围。约 74% 城市落在灰区内，所以 $\beta_{\mathrm{eff}}=0.98$ 不只是形式上接近 1，也有一定预测能力。

这张图说明，线性 scaling 不是因为“拟合懒得做非线性”，而是 local exponent 和 prediction test 都支持 $\beta \approx 1$。

### 11.8 Fig. 2.11：cinema usage 有 superlinear 倾向，但预测很差

![Fig. 2.11a — cinema usage 的 local exponent 大多高于 1](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-17-figure-03.jpg)

![Fig. 2.11b — cinema usage 的 prediction ratio 波动很大](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-17-figure-04.jpg)

Fig. 2.11 是一个重要灰区。左图中 local exponent 多数大于 1，说明 cinema usage 有 superlinear 倾向。全局拟合甚至给出 $\hat{\beta}=1.46$，effective exponent 约为 1.17。

但右图显示 prediction ratio 极不稳定，只有约 50% 城市落在 $[0.5,2]$ 灰区，另一些城市偏差可达两个数量级。因此，这个案例不能只说“superlinear”；更准确的说法是：存在 superlinear signal，但 simple scaling 的预测可靠性弱。

这张图把本章的实用标准推到前台：指数方向和预测能力必须分开判断。

### 11.9 Fig. 2.12：theaters 同时呈现 slight sublinearity 和 threshold 可能

![Fig. 2.12a — theaters 的幂律和阈值型拟合都可行](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-18-figure-01.jpg)

![Fig. 2.12b — theaters 的 local exponent 没有清楚收敛到拟合值](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-18-figure-02.jpg)

Fig. 2.12 处理 European theaters。左图中 power-law fit 给出 $\hat{\beta}=0.91$，看起来 slightly sublinear；但 $a+bS$ 形式也能解释数据，并暗示城市人口超过某个阈值后才更可能出现 theater。

右图中 $\beta_{\mathrm{loc}}$ 在小 $r$ 时接近 1，在大 $r$ 时低于 1，且没有清楚收敛到 $\hat{\beta}$。因此作者不把它简单归为 sublinear scaling，而保留 threshold effect 的可能。

这张图说明，城市设施类变量经常有“是否出现”的门槛。把这种变量强行放进单一幂律，会把 extensive growth 和 occurrence threshold 混在一起。

### 11.10 Fig. 2.13：external deaths 最终支持线性 scaling

![Fig. 2.13a — external deaths 的多个拟合形式](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-19-figure-01.jpg)

![Fig. 2.13b — external deaths 的 local exponent 收敛到 1](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/02-why-does-population-matter.mineru/hybrid_auto/images/page-19-figure-02.jpg)

Fig. 2.13 是另一个线性正例。左图里 power-law、$a+bS$ 和其他形式都可以给出看似合理的拟合，因此仅靠拟合图很难判断。

右图则更清楚：local exponent 很快收敛到 1，且平均值稳定在 1 附近。effective exponent 为 0.99，$f(2)$ 约为 82%。因此，虽然左图允许多个拟合形式，tomography plot 仍然支持线性 scaling。

这张图再次说明，作者更信任 local exponent 的收敛结构，而不是只看一张 global fit。

---

## 十二、本章最后给出的判断标准

作者最后把经验总结成三个必要条件。如果要相信全局拟合得到的 $\hat{\beta}$，至少应该满足：

1. $\beta_{\mathrm{loc}}$ 要向 $\hat{\beta}$ 收敛；
2. $\beta_{\mathrm{eff}}$ 要与 $\hat{\beta}$ 一致；
3. $f(2)$ 至少要达到一个可接受水平，作者给出的实用阈值是 50%，并且 $f(\varepsilon)$ 应该随容忍区间扩大而快速增加。

这三个条件分别对应三层问题。

第一层是结构问题：城市对之间的局部斜率是否支持同一个全局指数。这个问题由 tomography plot 回答。

第二层是指数问题：从 benchmark city 得到的 practical exponent 是否和全局 fit 的 $\hat{\beta}$ 一致。如果不一致，全局拟合很可能只是某种平均幻觉。

第三层是预测问题：即使指数看起来一致，用它预测其他城市是否足够可靠。这个问题由 $f(2)$ 或更一般的 $f(\varepsilon)$ 回答。

如果这些条件不满足，就可以安全地拒绝 $\hat{\beta}$，或者至少拒绝 simple power-law scaling form。失败的原因可能是噪声太大，也可能是城市量根本不服从单指数幂律，而需要 threshold、分段函数、多个指数或更复杂的生成机制。

这一章的最终态度很谨慎：scaling law 是理解城市的有力入口，但它不是城市科学的自动答案。真正有意义的不是拟合出一个 exponent，而是判断这个 exponent 是否稳定、可解释、可预测，并且不被边界定义和噪声结构支配。

---

## 十三、对当前研究问题的启发

这章对 `Synthetic_City` 的启发，不在于直接套一个 $Y=aS^\beta$，而在于它提供了一套处理“条件信息和目标结构”的诊断语言。

首先，人口或 census summaries 可以作为 conditioning variables，但它们不应被默认理解为充分条件。Chapter 2 反复提醒：即使人口是最自然的一阶尺度变量，也不保证相同人口的城市拥有相同结构。对你的问题来说，这意味着 census summaries 可以组织条件空间，但不能自动替代空间机制、边界定义和历史路径。

其次，scaling law 可以作为 baseline，而不是主模型。比如可以先问某些 PUMA-level quantity 是否随人口、家庭数、就业数或建成区面积呈现近似线性、sublinear 或 superlinear 关系。但如果只是得到一个接近 1 的 exponent，不应马上解释为机制。需要检查边界定义、噪声、样本跨度和条件变量是否足够稳定。

第三，local exponent / tomography plot 很适合作为跨空间单元迁移的诊断工具。对任意两个 PUMA 或城市区域，可以定义类似的 pairwise local exponent，检查某个 target quantity 在不同 population ratio 下是否收敛。如果不收敛，说明用单一 scaling exponent 做跨区域预测是不稳定的。

第四，本章反复出现的 threshold effect 对城市数据尤其重要。很多城市设施、社会活动或风险事件并不是从人口为零开始连续增长，而是达到某个规模后才出现。这对生成模型也很关键：如果 target quantity 具有阈值结构，那么用平滑的全局 scaling 或普通回归可能会把“是否出现”和“出现后增长”混在一起。

最后，这章也提示一个更大的问题：如果你的 observation 是 census summaries，target 是 PUMA-level spatial distribution，那么真正困难的不只是拟合条件到目标的映射，而是判断哪些关系是稳定的 scaling regularity，哪些只是边界定义、样本组成或历史路径造成的横截面相关。

---

## 十四、这一章可以压成的一句话

Chapter 2 的核心不是“城市量满足幂律”，而是：**人口是比较城市的自然尺度，scaling exponent 可以揭示非线性机制，但 urban scaling 只有在 local exponent 收敛、effective exponent 稳定、预测能力足够好时才值得相信。**
