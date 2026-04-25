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

第一，scaling 暗示 self-similarity。也就是说，系统在尺度改变时保持某种结构关系。对城市来说，这对应一个强假设：大城市可以被看成小城市的 scaled-up version。

第二，scaling exponent 可以提示机制。如果指数不能从简单量纲推出，它往往说明系统里有非平凡的组织原则、相互作用或约束。

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

## 七、统计检验：把 scaling 写成概率模型

为了解决直接拟合的问题，作者介绍 Leitao et al. 的统计框架。这个框架不只拟合平均关系，而是把城市量 $y$ 看成给定城市人口 $x$ 后的随机变量：

$$
\mathbb{E}(y \mid x) = \alpha x^\beta.
$$

这样，scaling 不再只是图上的一条线，而是条件分布 $P(y \mid x)$ 的均值结构。

但只规定均值还不够，因为城市数据的波动很大。于是他们还规定方差随均值变化：

$$
\mathbb{V}(y \mid x) = \gamma \mathbb{E}(y \mid x)^\delta.
$$

这个关系就是 Taylor's law。它的作用是把 fluctuation structure 也放进模型里，而不是把所有偏离幂律的点都粗暴看成同一种误差。

接下来，他们为 $P(y \mid x)$ 选择不同分布形式，例如 Gaussian 和 log-normal，并通过 likelihood 估计参数 $(\alpha, \beta, \gamma, \delta)$。然后比较 $\beta \neq 1$ 的模型和固定 $\beta = 1$ 的模型，看非线性是否真正改善解释。

这一步的结论很谨慎：在很多数据集上，模型本身会被数据拒绝。也就是说，问题不只是“$\beta$ 估得准不准”，而是这些概率模型可能没有正确描述城市数据的波动结构。

这一点非常重要。作者实际上是在说：**估计 scaling exponent 和建立 generative model 是绑在一起的。** 如果你没有一个合理的数据生成和波动模型，$\beta$ 的统计显著性也会变得不稳定。

---

## 八、practical test：从全局拟合转向两城之间的 local exponent

作者随后给出一个更实用的检验方式。与其一次性把所有城市塞进一个全局拟合，不如先问一个更直接的问题：

**如果 scaling law 成立，给定城市 1 的人口 $S_1$ 和宏观量 $Y_1$，能不能预测城市 2 的宏观量 $Y_2$？**

在 scaling 假设下，有：

$$
Y_2 = Y_1 \left(\frac{S_2}{S_1}\right)^\beta.
$$

反过来，如果我们已知两个城市的 $(S_1, Y_1)$ 和 $(S_2, Y_2)$，就可以计算一个让这两个城市刚好互相对应的局部指数：

$$
\beta_{\mathrm{loc}} = \frac{\log(Y_2/Y_1)}{\log(S_2/S_1)}.
$$

这个量的几何意义很简单：在 log-log 图上，$\beta_{\mathrm{loc}}$ 就是连接两个城市点的直线斜率。

如果所有城市真的落在同一条幂律上，那么任意两座城市之间的 $\beta_{\mathrm{loc}}$ 都应该接近同一个 $\beta$。如果不同城市对给出非常不同的 $\beta_{\mathrm{loc}}$，那说明全局 scaling 至少不稳定。

作者把 $\beta_{\mathrm{loc}}$ 对人口比值

$$
r = \frac{S_2}{S_1}
$$

作图，称为 tomography plot。这个图相当于从不同人口尺度差异上扫描 scaling 关系。

这个诊断的关键在于噪声。如果设

$$
Y_2 = Y_1 \left(\frac{S_2}{S_1}\right)^\beta (1+\eta),
$$

那么

$$
\beta_{\mathrm{loc}} = \beta + \frac{\log(1+\eta)}{\log(S_2/S_1)}.
$$

这个式子说明两件事。

第一，当人口比 $r = S_2/S_1$ 很大时，分母 $\log r$ 较大，噪声项被压低。此时如果 scaling 成立，$\beta_{\mathrm{loc}}$ 应该向真实 $\beta$ 收敛。

第二，当两个城市人口很接近时，$\log r$ 很小，哪怕很小的噪声也会让 $\beta_{\mathrm{loc}}$ 变得很大或很不稳定。因此，相似规模城市之间的比较对估计 scaling exponent 反而不可靠。

这个推导让 tomography plot 有了明确解释：它不是另一种画图技巧，而是在检查 $\beta_{\mathrm{loc}}$ 是否随着人口比增大而收敛。如果不收敛，就说明简单 scaling form 有问题。

---

## 九、benchmark city 和 effective exponent

local exponent 还可以用来定义一个 practical prediction framework。对每一座城市 $i$，可以计算它和所有其他城市 $j$ 的局部指数：

$$
\beta_{\mathrm{loc}}(i,j) = \frac{\log(Y_j/Y_i)}{\log r_{ij}}.
$$

然后对固定城市 $i$，计算这些 $\beta_{\mathrm{loc}}(i,j)$ 的平均值和方差。作者选择方差最小的城市作为 benchmark city。直观地说，这座城市和其他城市做 scaling prediction 时，局部指数最稳定。

对应的平均局部指数就是 effective exponent $\beta_{\mathrm{eff}}$。它不一定等于全局拟合得到的 $\hat{\beta}$，但它有一个更实际的含义：如果我们真的要用一个指数从 benchmark city 预测其他城市，$\beta_{\mathrm{eff}}$ 是更稳健的选择。

预测式为：

$$
Y(j) = Y(i_{\min}) \left(\frac{S_j}{S_{i_{\min}}}\right)^{\beta_{\mathrm{eff}}}.
$$

为了评价预测效果，作者定义 $f(\varepsilon_1,\varepsilon_2)$：有多少城市的预测值落在真实值的某个倍数区间内。特别地，$f(2)$ 表示有多少城市的预测值位于真实值的 $[0.5,2.0]$ 区间内。

这一套方法把问题从“全局拟合线好不好看”改成了“如果真的拿 scaling 做预测，它能预测多少城市”。这也是这一章后半部分最实用的贡献。

---

## 十、案例结果：有些 scaling 被确认，有些被拆开

作者用多个数据集展示 local exponent 方法能给出什么信息。

第一个清楚案例是美国 GDP 和道路里程。GDP 的全局拟合给出 superlinear exponent，$\hat{\beta} = 1.11$；道路里程给出 sublinear exponent，$\hat{\beta} = 0.85$。tomography plot 支持这两个判断：大多数城市对的 $\beta_{\mathrm{loc}}$ 与拟合值一致。effective exponent 也相近，GDP 为 $\beta_{\mathrm{eff}} = 1.13 \pm 0.07$，道路里程为 $\beta_{\mathrm{eff}} = 0.80 \pm 0.1$。用纽约作为 benchmark city 时，$f(2)$ 分别达到 98% 和 91%。这里 local exponent 不是推翻拟合，而是加强了非线性结论。

GDP per capita 的分析回应了一个常见批评：superlinear GDP 可能只是因为用了 extensive quantity。如果改看人均 GDP，拟合 exponent 约为 0.11，对应总量 exponent 的 $\hat{\beta}-1$。tomography plot 显示局部指数快速收敛到约 0.11，$\beta_{\mathrm{eff}} = 0.13 \pm 0.07$，$f(2)=98\%$。这说明在美国 GDP 案例中，非线性不只是 extensive quantity 的假象。

但 UK train stations 的案例完全不同。已有统计分析认为它近似线性，但 tomography plot 显示局部指数存在严重波动，甚至呈现 sublinear 信号。作者指出，这可能不是一个简单 power law，而是存在 threshold effect：低于某个人口阈值时没有车站，超过阈值后才近似线性。这里 local exponent 暴露了一个全局线性拟合掩盖的问题。

Brazil AIDS cases 也类似。power-law fit 给出 $\hat{\beta}=0.74$，看似 sublinear；但数据也可以由带阈值的形式解释。tomography plot 不清楚，$\beta_{\mathrm{eff}}=1.03$，$f(2)=67\%$。因此，原先的 sublinear 结论可能被 threshold 或线性机制挑战。

European cinema capacity 是一个 local exponent 支持线性的案例。naive fit 给出 $\hat{\beta}=0.99$，tomography plot 也收敛到 1，$\beta_{\mathrm{eff}}=0.98$，$f(2)=74\%$。这说明即便标准统计证据不够强，local exponent 可以提供实用层面的支持。

European cinema usage 则更模糊。power-law fit 给出很强的 superlinear exponent，$\hat{\beta}=1.46$，但 $\beta_{\mathrm{eff}}$ 下降到约 1.17，且 $f(2)$ 只有约 50%。这说明可能存在 superlinear 倾向，但预测稳定性很差。

European theaters 的案例同样复杂。局部指数在小人口比时接近 1，在大人口比时小于 1，没有清楚收敛到拟合值。作者认为，这可能是 slightly sublinear，也可能是 threshold effect。这里的重点不是给出单一答案，而是说明 simple power-law scaling 可能不是正确形式。

Brazil external deaths 最后提供一个正例。虽然直接拟合和阈值形式都可以给出不错结果，但 tomography plot 清楚显示局部指数快速收敛到 1，$\beta_{\mathrm{eff}}=0.99$，$f(2)=82\%$。因此 local exponent 支持线性 scaling。

这些案例共同说明：local exponent 方法不是为了永远证明 scaling，而是为了区分三类情形：

1. 拟合和 local exponent 一致，scaling 可信；
2. 拟合看似清楚，但 local exponent 暴露噪声或阈值；
3. 数据太复杂，simple power law 本身应该被拒绝。

---

## 十一、本章最后给出的判断标准

作者最后把经验总结成三个必要条件。如果要相信全局拟合得到的 $\hat{\beta}$，至少应该满足：

1. $\beta_{\mathrm{loc}}$ 要向 $\hat{\beta}$ 收敛；
2. $\beta_{\mathrm{eff}}$ 要与 $\hat{\beta}$ 一致；
3. $f(2)$ 至少要达到一个可接受水平，作者给出的实用阈值是 50%，并且 $f(\varepsilon)$ 应该随容忍区间扩大而快速增加。

如果这些条件不满足，就可以安全地拒绝 $\hat{\beta}$，或者至少拒绝 simple power-law scaling form。失败的原因可能是噪声太大，也可能是城市量根本不服从单指数幂律，而需要 threshold、分段函数、多个指数或更复杂的生成机制。

这一章的最终态度很谨慎：scaling law 是理解城市的有力入口，但它不是城市科学的自动答案。真正有意义的不是拟合出一个 exponent，而是判断这个 exponent 是否稳定、可解释、可预测，并且不被边界定义和噪声结构支配。

---

## 十二、对当前研究问题的启发

这章对 `Synthetic_City` 的启发，不在于直接套一个 $Y=aS^\beta$，而在于它提供了一套处理“条件信息和目标结构”的诊断语言。

首先，人口或 census summaries 可以作为 conditioning variables，但它们不应被默认理解为充分条件。Chapter 2 反复提醒：即使人口是最自然的一阶尺度变量，也不保证相同人口的城市拥有相同结构。对你的问题来说，这意味着 census summaries 可以组织条件空间，但不能自动替代空间机制、边界定义和历史路径。

其次，scaling law 可以作为 baseline，而不是主模型。比如可以先问某些 PUMA-level quantity 是否随人口、家庭数、就业数或建成区面积呈现近似线性、sublinear 或 superlinear 关系。但如果只是得到一个接近 1 的 exponent，不应马上解释为机制。需要检查边界定义、噪声、样本跨度和条件变量是否足够稳定。

第三，local exponent / tomography plot 很适合作为跨空间单元迁移的诊断工具。对任意两个 PUMA 或城市区域，可以定义类似的 pairwise local exponent，检查某个 target quantity 在不同 population ratio 下是否收敛。如果不收敛，说明用单一 scaling exponent 做跨区域预测是不稳定的。

第四，本章反复出现的 threshold effect 对城市数据尤其重要。很多城市设施、社会活动或风险事件并不是从人口为零开始连续增长，而是达到某个规模后才出现。这对生成模型也很关键：如果 target quantity 具有阈值结构，那么用平滑的全局 scaling 或普通回归可能会把“是否出现”和“出现后增长”混在一起。

最后，这章也提示一个更大的问题：如果你的 observation 是 census summaries，target 是 PUMA-level spatial distribution，那么真正困难的不只是拟合条件到目标的映射，而是判断哪些关系是稳定的 scaling regularity，哪些只是边界定义、样本组成或历史路径造成的横截面相关。

---

## 十三、这一章可以压成的一句话

Chapter 2 的核心不是“城市量满足幂律”，而是：**人口是比较城市的自然尺度，scaling exponent 可以揭示非线性机制，但 urban scaling 只有在 local exponent 收敛、effective exponent 稳定、预测能力足够好时才值得相信。**
