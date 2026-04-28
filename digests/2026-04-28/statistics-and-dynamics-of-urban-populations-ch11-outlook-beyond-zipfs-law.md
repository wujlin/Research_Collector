---
title: "Statistics and Dynamics of Urban Populations, Chapter 11: Outlook: Beyond Zipf's law"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-28"
topics: ["urban dynamics", "Zipf's law", "migration shocks", "spatial urban systems", "urban sprawl", "city hierarchy"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/11-outlook-beyond-zipfs-law.mineru/hybrid_auto/11-outlook-beyond-zipfs-law.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 11：Outlook: Beyond Zipf's Law

## 精读笔记

---

## 一、这一章在全书里的位置

Chapter 11 是全书的收束和转向。

前面几章做了两件事。第一，作者不断削弱 Zipf's law 作为 universal law 的地位。Chapter 3 说明 empirical city-size distribution 并不总是稳定地服从 Zipf。Chapter 6-7 说明，很多能生成 Zipf 的 stochastic growth models 其实是为了复现 Zipf 而构造的，不一定从真实城市机制出发。Chapter 8-10 则从 migration shocks 出发，建立了一套更 bottom-up 的动力学解释。

第二，作者把城市增长从静态分布问题转成了动态问题。城市规模分布不是单纯由一个优美的 rank-size law 决定，而是由 interurban migration flows、heavy-tailed shocks、finite-size effects 和 rank turbulence 共同塑造。

所以 Chapter 11 的任务不是再推一个新方程，而是回答两个问题。

第一，全书对 Zipf's law 的最终态度是什么？

第二，如果只研究 population size 还不够，下一步应该把什么维度纳入模型？

这一章的主线可以写成：

$$
\begin{aligned}
&\text{Zipf's law as hoped-for universality}\\
&\rightarrow \text{empirical deviations from Zipf}\\
&\rightarrow \text{migration shocks control city-size statistics}\\
&\rightarrow \text{population distribution is not a simple universal power-law}\\
&\rightarrow \text{rare shocks matter for planning}\\
&\rightarrow \text{population alone is incomplete}\\
&\rightarrow \text{space, hierarchy, and urban surface growth become the next frontier}.
\end{aligned}
$$

这条线很重要。作者不是说 Zipf's law 完全没用，而是说它不能继续作为城市人口研究的终点。Zipf 更像一个粗糙经验近似，而不是一个需要被所有模型追逐的基本定律。

### 1.1 本章符号口径

$S(n)$ 表示 rank 为 $n$ 的城市人口。这里的 $n$ 是 rank，不是时间，也不是样本数。

$A$ 是 rank-size law 里的 scale constant，不是后面城市 surface area $A(t)$。

$\zeta$ 是 Zipf/rank-size exponent。它和 Chapter 6 的 Yule-Simon tail parameter $\zeta$ 有联系，但这里主要读成 rank-size scaling slope。

$A(t)$ 表示城市建成区或表面积随时间的变化。它是空间增长问题里的变量，不是 Eq. 11.1 的常数 $A$。

$r(\theta,t)$ 表示用极坐标描述的城市边界。给定角度 $\theta$ 和时间 $t$，$r$ 表示城市边界从某个中心向外延伸的距离。

---

## 二、Eq. 11.1：Zipf's law 到底说了什么

作者先回到全书反复讨论的经验规律：Zipf's law。

对城市 rank-size distribution，Zipf's law 写成：

$$
S(n)
=
\frac{A}{n^\zeta}.
\tag{11.1}
$$

这里 $S(n)$ 是 rank 为 $n$ 的城市人口。rank 1 是最大城市，rank 2 是第二大城市，以此类推。

如果 $\zeta\simeq1$，就得到经典 Zipf form：

$$
S(n)
\approx
\frac{A}{n}.
$$

这意味着 rank 翻倍时，城市规模大约减半。例如 rank 2 城市大约是最大城市的一半，rank 10 城市大约是最大城市的十分之一。

在 log-log 坐标里，Eq. 11.1 变成：

$$
\log S(n)
=
\log A-\zeta\log n.
$$

所以 Zipf's law 对应一条近似直线，斜率是 $-\zeta$。如果 $\zeta=1$，斜率就是 $-1$。

这也是为什么 Zipf's law 很有吸引力。它把复杂城市系统压缩成一个简单指数，仿佛不同国家、不同时期、不同城市定义下都存在一个 universal pattern。

但作者在这里要反过来强调：这种吸引力本身可能误导研究。

---

## 三、为什么作者说 Zipf's law 更像一种“希望”，而不是普遍事实

作者说，过去很多研究试图解释 Zipf's law 的出现，却没有充分质疑它是否真的普遍成立。

这句话对应全书前半部分的批判。只要先假设 Zipf's law 是核心事实，模型任务就会变成：

$$
\text{construct a mechanism}
\rightarrow
\text{generate Zipf exponent close to }1.
$$

这条路径的问题是，它容易把模型评价标准缩窄成“能不能生成 Zipf”。但如果 empirical $\zeta$ 本身会显著偏离 1，那么模型即使能生成 Zipf，也不一定解释了真实城市系统。

数据增多以后，研究者发现：

$$
\zeta
\not\simeq
1
\quad
\text{in many systems}.
$$

更进一步，不只是 $\zeta$ 偏离 1，有些城市系统的 population distribution 本身也未必是简单 power-law。

所以作者的判断是：Zipf's law 更像一种 hoped-for universality。人们希望城市系统像物理系统里的 universality class 一样，可以用一个简单指数概括。但城市人口分布没有稳定到这种程度。

这不是说 Eq. 11.1 毫无价值。它仍然可以作为粗略描述、比较基准或经验近似。但它不能被当作城市增长理论的最终解释对象。

---

## 四、真正的问题不是解释 Zipf，而是估计城市人口分布

作者接着把问题重新定义。

错误的问题是：

$$
\text{Why does Zipf's law hold?}
$$

更合适的问题是：

$$
\text{What is the population distribution of cities, and what mechanisms shape it?}
$$

这个重述很关键。因为一旦问题从“解释 Zipf”转成“估计 population distribution”，模型就不必被 Zipf exponent 1 绑架。

Chapter 9-10 给出的替代路线是：从 first principles 和 interurban migration data 出发，推导城市增长方程，再看这个方程产生什么样的 population distribution。

最终得到的结论是：城市 population distribution 不是一个简单 universal power-law。它在非常大的城市区间可以近似 power-law，但这个近似的 exponent 不是 universal constant，而是由 migration shock statistics 控制。

也就是说，tail behavior 来自：

$$
\text{broadly distributed microscopic migration flows}
\rightarrow
\text{Levy-type aggregate shocks}
\rightarrow
\text{non-universal city-size distribution}.
$$

这就是全书最重要的 paradigm shift。

旧的视角是：

$$
\text{statistical universality}
\rightarrow
\text{Zipf-like law}.
$$

新的视角是：

$$
\text{migration shocks}
\rightarrow
\text{non-universal stochastic organization of cities}.
$$

城市系统不再被理解成自动收敛到同一个 scaling law 的整体，而是被理解成由 rare but large shocks、finite-size effects 和历史路径共同塑造的复杂系统。

---

## 五、Zipf 为什么只是 loose approximation

作者说，Zipf's law does not hold in general，而是一个 loose approximation。

这句话可以拆成三层。

第一，finite-size effects 会影响观察到的 exponent。真实城市系统不是无限样本，最大城市数量有限，tail 区间有限。即使 underlying model 在极大 $S$ 时有 power-law tail，现实数据也可能还没进入 asymptotic regime。

第二，noise strength 会影响 distribution 的形状。Chapter 10 已经说明，Levy shocks 会让城市系统出现 slow convergence 和 apparent Zipf。也就是说，在有限数据区间里，看起来像 Zipf，并不等于真正的 asymptotic exponent 就是 1。

第三，migration flow statistics 本身不是 universal。不同国家、不同时期、不同城市定义下，migration shock tail exponent $\alpha$、migration amplitude exponent $\beta$、平均增长率 $r$ 都可能不同。因此最终 population distribution 也不应该被期待有一个固定 universal exponent。

所以更准确的读法是：

$$
\text{Zipf-like behavior}
\neq
\text{Zipf's law as a universal law}.
$$

Zipf-like behavior 可以存在，但它可能只是局部近似、有限样本效应或某些参数组合下的表观规律。

---

## 六、为什么 rare events 对城市规划也重要

作者接着把理论结论转到 urban planning。

如果城市动态主要由 Gaussian-like small fluctuations 组成，那么城市未来更像一个平滑趋势。规划者可以把重点放在平均增长率、长期趋势和渐进调整上。

但 Chapter 9-10 的结果强调的是 heavy-tailed migration shocks。也就是说，城市未来可能被少数 rare but large events 显著改变。

这种 shock 可以来自：

$$
\text{large migration wave},
\quad
\text{industrial relocation},
\quad
\text{resource discovery},
\quad
\text{war or crisis},
\quad
\text{policy intervention},
\quad
\text{transport infrastructure change}.
$$

这些事件不只是短期扰动。由于它们可能和过去很多年累积的变化同阶，所以它们可以改变城市 rank、规模轨迹和长期发展方向。

这也是作者为什么说 interurban migration flows 在 urban planning 中被低估了。传统规划理论往往关注土地使用、交通、住房和公共服务，但如果城市吸引大量新居民的能力受到 heavy-tailed migration fluctuations 控制，那么 migration network 本身就应该成为规划对象。

换句话说，规划不只要问：

$$
\text{How fast will this city grow on average?}
$$

还要问：

$$
\text{What kinds of shocks can redirect migration flows into or out of this city?}
$$

---

## 七、为什么接下来必须把 space 放进模型

到这里，全书已经对 population dynamics 给出了一条较完整的路线。但作者马上指出：population 不是城市的全部。

城市还有一个明显缺失的维度：

$$
\text{space}.
$$

人口规模告诉我们一个城市有多少人，但不告诉我们这些人分布在哪里，也不告诉我们城市如何向外扩展、如何被交通网络约束、如何和周边城市形成空间结构。

如果只看 population size，两个城市可能有相似人口，但空间形态完全不同。

一个城市可能是 compact high-density form，另一个可能是 low-density sprawl。它们的人口规模相同，但交通需求、碳排放、土地消耗和公共服务成本都可能非常不同。

所以 Chapter 11 的后半部分不是附带讨论，而是全书的自然下一步：在 population dynamics 之外，建立 spatial dynamics。

---

## 八、Spatial structure of migration flows：迁移流不是空间随机的

作者首先讨论 migration flows 的 spatial structure。

前面 Chapter 9 把 interurban migration 看成城市之间的 flow network，但这个 network 主要用于推导 population dynamics。Chapter 11 进一步问：

$$
\text{these flows are between which spatial parts of cities?}
$$

Reia et al. (2022) 对 US migration flows 的研究显示，迁移流不仅连接城市，还携带城市内部空间结构信息。

Fig. 11.1 总结了这种空间结构。

![Fig. 11.1 Schematic representation of interurban migration flows in the US](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/11-outlook-beyond-zipfs-law.mineru/hybrid_auto/images/page-02-figure-01.jpg)

这张图可以按三类流来读。

第一，core-to-core interurban flows。图中两个 MSA 的 core county 之间有蓝色箭头。它表示一个城市核心区和另一个城市核心区之间存在强迁移联系。作者说，core counties 更可能接收来自其他城市 core counties 的 inflows，而不是来自外部 county 的 inflows。

第二，core-to-external intracity redistribution。每个 MSA 内部有从 core county 指向 external counties 的红色箭头。这说明城市内部人口迁移通常沿着负 density gradient 走：人从高密度中心向低密度外围移动。

第三，MicroSAs / NonSAs 与 external counties 的联系。绿色箭头表示微型统计区或非统计区与大城市外部 county 更容易发生迁移联系。这说明城市系统不是只有大城市核心之间的交换，外围区域和小型地区也参与迁移网络。

这张图的关键不是展示某一条具体迁移路径，而是说明 migration flow 有空间方向性。

它不是：

$$
\text{random people moving between abstract city nodes}.
$$

而更像：

$$
\text{spatially structured flows between cores, peripheries, and smaller settlements}.
$$

这对前面 Chapter 9 的模型是一个补充。Chapter 9 用城市节点之间的 flow 推导 population shocks；Chapter 11 提醒我们，下一步应该把 city node 打开，看 migration shocks 在城市内部空间上如何进入和扩散。

---

## 九、为什么需要跨国家验证这些 migration flow patterns

作者强调，Reia et al. 的结果来自 US，因此需要在其他国家验证。

这个提醒很重要，因为空间结构高度依赖制度和地理背景。

US 的城市系统有自己的 county 划分、MSA 定义、郊区化历史、交通依赖和住房市场结构。其他国家可能有不同的城市边界、中心-外围关系、公共交通系统和迁移制度。

因此，不能直接把 US 的 spatial migration pattern 当成 universal law。

需要进一步问：

$$
\text{core-to-core flows 是否普遍?}
$$

$$
\text{center-to-periphery redistribution 是否普遍?}
$$

$$
\text{MicroSAs / small settlements 与大城市外围的联系是否普遍?}
$$

如果这些模式在不同国家都存在，那么它们可能是城市空间迁移的一般机制。如果只在 US 明显存在，那么它们就更像特定制度和空间结构下的结果。

这和全书对 Zipf's law 的态度一致：不要过早把某个经验 pattern 当成 universal law，要先看它在不同系统中是否稳健。

---

## 十、Hierarchical organization of cities：城市系统不只是规模排序，也有空间层级

作者接着讨论另一个空间问题：城市系统的 hierarchical organization。

前面的 rank-size law 只按 population 排序。它告诉我们谁大、谁小，但不告诉我们城市在哪里，也不告诉我们一个城市在空间网络中支配哪些区域。

作者指出，city location 也很关键。一个城市的重要性不只来自 population size，还来自它在空间系统里的位置，以及它周围有哪些城市。

这就把问题从一维 rank 变成空间统计问题：

$$
\text{city-size distribution}
\rightarrow
\text{marked point process}.
$$

这里 point 是城市的位置，mark 是城市人口、经济功能或其他属性。城市系统不再是一串按大小排列的数，而是一组带有属性的空间点。

Louail and Barthelemy (2022) 提出了一种 non-parametric 方法，用 Voronoi tessellation 和 dominance tree 来描述这种结构。

这套方法可以线性读成：

$$
\begin{aligned}
&\text{city locations}\\
&\rightarrow \text{Voronoi tessellation}\\
&\rightarrow \text{recursive neighborhood analysis}\\
&\rightarrow \text{dominance tree}\\
&\rightarrow \text{tree height as spatial-population importance}.
\end{aligned}
$$

Voronoi tessellation 的作用是把空间分给最近的城市。每个城市得到一个 region，表示它在几何上最接近的影响范围。

dominance tree 的作用是进一步编码层级关系。一个城市在树中的 height 不只反映它的人口，也反映它和周边城市的空间组织关系。

这比单纯 rank 更丰富。rank 只说：

$$
\text{city A is larger than city B}.
$$

spatial hierarchy 还会问：

$$
\text{city A dominates which local region?}
$$

$$
\text{city B is embedded under which larger spatial center?}
$$

$$
\text{urban hierarchy changes over history in what spatial pattern?}
$$

这也是作者为什么说 further research is needed。人口、空间位置和邻域结构之间的耦合，还没有达到前面 population dynamics 那样的建模清晰度。

---

## 十一、The next frontier：城市空间增长和 surface area

最后一节把问题推进到城市 surface area 的动态。

人口增长只是城市变化的一部分。城市还会向外扩张，改变 built-up area、边界形状和土地使用。

作者强调 urban sprawl 是城市面临的重要挑战，因为它直接关联：

$$
\text{more car use},
\quad
\text{larger greenhouse gas emissions},
\quad
\text{land artificialization}.
$$

也就是说，空间增长不是纯形态问题，而是环境、交通和政策问题。

Fig. 11.2 展示 London 从 1800 到 1978 的 built area expansion。

![Fig. 11.2 Expansion of London from 1800 to 1978](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/11-outlook-beyond-zipfs-law.mineru/hybrid_auto/images/page-03-figure-01.jpg)

这张图按时间分成三个 built-up layers。

蓝色区域表示 1800 年左右的 London built area，集中在核心区。

绿色区域表示 1914 年前后的扩张，城市已经明显向外扩展，并形成不规则的外缘。

灰色区域表示 1978 年的 built area，城市空间大幅铺开，边缘变得破碎、伸展，并和周边小斑块产生复杂关系。

这张图带出的核心问题是：城市空间增长不是简单地把圆形按比例放大。它有方向性、不规则边界、局部跳跃、交通走廊和周边斑块。

所以作者提出三个自然问题。

---

## 十二、第一个空间动力学问题：surface area $A(t)$ 如何增长

第一个问题是城市 surface area 的时间演化。

设城市建成区面积为：

$$
A(t).
$$

那么最直接的问题是：

$$
\frac{dA}{dt}
=
?
$$

这对应 population dynamics 中的：

$$
\frac{dS}{dt}
=
?
$$

前面全书主要建立的是 population equation：

$$
\partial_t S
=
\text{growth}
+
\text{migration shocks}.
$$

现在 spatial growth 需要类似问题：

$$
\partial_t A
=
\text{land conversion}
+
\text{transport effects}
+
\text{planning constraints}
+
\text{spatial shocks}.
$$

关键是，$A(t)$ 不一定和 $S(t)$ 同步增长。

如果 population 增加但 density 提高，$A(t)$ 可以增长较慢。如果 population 增加同时低密度扩张，$A(t)$ 会增长很快。如果 population 停滞但土地继续开发，也可能出现 spatial expansion without proportional population growth。

所以真正的问题不是只估计 $A(t)$，而是估计 population 和 area 的耦合：

$$
S(t)
\leftrightarrow
A(t).
$$

这对 synthetic city 或 spatial allocation 问题很直接：不能只生成 population totals，还要决定这些 population 如何落在空间上，以及是否导致 built area 扩张。

---

## 十三、第二个空间动力学问题：transport infrastructure 如何影响扩张

作者提出的第二个问题是 transport infrastructure。

城市不是在均匀平面上扩张。道路、铁路、地铁、高速公路、河流和地形都会改变扩张方向。

如果 transport infrastructure 降低某些方向的 travel cost，那么城市可能沿这些方向更快增长。空间增长就会从 isotropic expansion 变成 anisotropic expansion。

可以用直觉式写成：

$$
\text{transport corridor}
\rightarrow
\text{lower effective distance}
\rightarrow
\text{higher accessibility}
\rightarrow
\text{faster built-area growth along that direction}.
$$

这和 Fig. 11.2 中 London 的不规则扩张有关。城市边界不是完美圆形，而是在某些方向更向外伸展。这种伸展可能和交通、地形、产业位置、规划政策有关。

所以空间增长模型需要解释的不只是：

$$
\text{how much area grows}.
$$

还要解释：

$$
\text{where the area grows}.
$$

---

## 十四、第三个空间动力学问题：城市边界 $r(\theta,t)$ 如何演化

作者最后提出最接近物理建模的问题：如果用极坐标描述城市 frontier，增长方程应该是什么？

设城市中心为参考点。对每个角度 $\theta$，城市边界到中心的距离是：

$$
r(\theta,t).
$$

那么城市边界就是一条随时间变化的曲线。

如果城市只是均匀扩张，那么 $r(\theta,t)$ 对所有 $\theta$ 都差不多，边界接近圆形。

但真实城市不是这样。某些方向扩张快，某些方向扩张慢，某些方向被地形或政策阻挡，某些方向沿交通线跳跃式发展。因此 $r(\theta,t)$ 是一个 rough frontier。

作者提出的问题可以写成：

$$
\partial_t r(\theta,t)
=
?
$$

这个式子和前面 population equation 是平行的。

人口动力学问：

$$
\partial_t S(t)
=
\text{population growth mechanisms}.
$$

空间 frontier 动力学问：

$$
\partial_t r(\theta,t)
=
\text{local spatial growth mechanisms}.
$$

可能进入右端的因素包括：

$$
\text{local population pressure},
\quad
\text{land price},
\quad
\text{transport accessibility},
\quad
\text{zoning},
\quad
\text{terrain constraint},
\quad
\text{historical path dependence}.
$$

这和你之前读的 city growth rough surface 文章也能接上。那篇文章把城市边界粗糙性看成 surface growth problem，而这里作者也在指向类似方向：城市边界不是单一半径，而是随角度和时间变化的 rough interface。

---

## 十五、为什么作者说空间增长还没有达到人口增长的理解水平

作者最后承认，虽然已有一些尝试，但 urban spatial growth 还没有达到 population evolution 那样的 quantitative understanding。

这句话可以从三个层面理解。

第一，population size 是一维变量。虽然它的 stochastic dynamics 很复杂，但变量本身是标量：

$$
S(t).
$$

第二，surface area 是空间变量。即使只看总面积，也需要知道城市边界如何定义、built-up area 如何测量、remote sensing 数据如何处理。

第三，frontier dynamics 是函数变量。$r(\theta,t)$ 不是一个数，而是一整条曲线。它的演化可能涉及局部相互作用、交通网络、规划政策和地形约束。

所以空间增长的困难不是“多加一个变量”这么简单，而是从 scalar dynamics 进入 spatial field dynamics。

可以把难度提升写成：

$$
\begin{aligned}
&S(t): \text{one-dimensional population dynamics}\\
&\rightarrow A(t): \text{aggregate spatial area dynamics}\\
&\rightarrow r(\theta,t): \text{frontier shape dynamics}\\
&\rightarrow \text{full urban morphology and land-use dynamics}.
\end{aligned}
$$

这也是 Chapter 11 的开放结论：下一代城市动力学模型需要同时处理 population、migration、space 和 infrastructure。

---

## 十六、这一章和前面章节的关系

Chapter 3 问：Zipf's law 是否真的稳健？

Chapter 6 问：哪些 stochastic growth models 可以生成 power-law？

Chapter 7 问：migration 加入后，城市规模分布和不平等如何改变？

Chapter 8 问：如果 shocks 是 heavy-tailed，加总极限为什么不是 Gaussian？

Chapter 9 问：能否从 empirical migration flows 推导城市增长方程？

Chapter 10 问：这个 Levy growth equation 能否解释 city-size distribution 和 rank turbulence？

Chapter 11 的位置是：把这些问题收束成一个判断，并打开下一步。

收束判断是：

$$
\text{Zipf's law is not the endpoint}.
$$

下一步问题是：

$$
\text{population dynamics must be coupled with spatial dynamics}.
$$

这也是为什么本章标题是 Beyond Zipf's law。Beyond 不只是说“找一个比 Zipf 更好的 exponent”，而是说研究对象本身要扩展：从 rank-size law 扩展到 migration shocks、city hierarchy、spatial flows 和 urban surface growth。

---

## 十七、本章最重要的记忆点

第一，Zipf's law 的 rank-size form 是：

$$
S(n)=\frac{A}{n^\zeta}.
$$

当 $\zeta\simeq1$ 时，它给出经典 Zipf relation。但作者认为它不是 universal law，而是 loose approximation。

第二，全书的核心转向是：不要问“为什么城市服从 Zipf”，而要问“城市人口分布由什么机制塑造”。

第三，Chapter 9-10 的答案是：microscopic migration flows 的 broad fluctuations 会产生 Levy-type shocks，从而控制 city-size distribution 和 rank turbulence。

第四，population distribution 可能在 very large city regime 近似 power-law，但 exponent 不 universal，而是由 migration shock statistics 决定。

第五，rare events 对城市动态和规划都重要，因为一次大迁移冲击可能改变城市长期 rank trajectory。

第六，只看 population 不够。城市还具有空间结构：core-periphery flows、intercity spatial migration patterns、city hierarchy 和 built-area expansion。

第七，Fig. 11.1 的核心是：migration flows 有空间方向性。它们不只是抽象城市节点之间的随机边，而是连接 core counties、external counties、MicroSAs 和 NonSAs 的 structured flows。

第八，Fig. 11.2 的核心是：城市空间增长不是均匀放大，而是不规则、方向性强、受基础设施和历史路径影响的 built-area expansion。

第九，空间增长的三个核心变量是：

$$
A(t),
\qquad
\frac{dA}{dt},
\qquad
r(\theta,t).
$$

第十，本章真正打开的 next frontier 是：

$$
\text{population dynamics}
+
\text{migration shocks}
+
\text{spatial structure}
+
\text{urban morphology}.
$$

这条线和你的研究问题直接相关：如果 observation 里有 census summaries，target 是 PUMA 或 spatial allocation，那么仅仅拟合 population totals 不够，还需要思考 population 的空间组织、迁移流结构和城市形态约束如何进入 generative model。
