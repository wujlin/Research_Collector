---
title: "Inequality in infrastructure access and its association with health disparities"
authors: "Ying Tu, Bin Chen, Chuan Liao, Shengbiao Wu, Jiafu An, Chen Lin, Peng Gong, Bin Chen, Hong Wei, Bing Xu"
venue: "Nature Human Behaviour"
doi: "10.1038/s41562-025-02208-3"
published: "2025-05-22"
source_pdf: "../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.pdf"
source_mineru: "../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/inequality-in-infrastructure-access-and-its-association-with-health-disparities.md"
date_created: "2026-05-08"
status: "linearized digest"
---

# Inequality in infrastructure access and its association with health disparities

## 0. 这篇文章在解决什么问题

这篇文章研究的是 infrastructure access inequality 及其与 health disparities 的关系。它不只是问一个国家有多少基础设施，而是问：人口实际暴露到、接近到、能够享受到多少经济、社会和环境基础设施？这些 access 是否在空间上不平等？这种不平等是否与健康结局相关？

文章的核心逻辑可以写成：

```text
multi-source geospatial infrastructure data
    ↓
economic / social / environmental infrastructure maps
    ↓
population-weighted exposure model
    ↓
country- and county-level access
    ↓
Gini / inequality index
    ↓
association with HALE and DALYs
```

它的问题意识来自一个测量缺口。传统研究常用总投资、资本存量、人均供应、道路长度、建成区面积等 aggregate indicators 描述 infrastructure。但这些指标默认人群在空间上均匀暴露，容易忽略“设施在哪里、人口在哪里、人口是否接近设施”之间的错位。

作者的关键改进是把 infrastructure supply 和 population distribution 放到同一个 gridded spatial framework 中，用 population-weighted exposure 来估计 human access。

## 1. Introduction 的线性逻辑

基础设施是社会发展的底座。交通、能源、水与卫生、通信、教育、医疗和环境设施都支撑经济运行和人类福祉。联合国 SDG 9 明确提出建设 resilient infrastructure；同时，基础设施与 169 个 SDG targets 中的多数目标都有直接关联。

但作者指出，基础设施研究存在三个知识缺口。

第一，基础设施 access 的全球测量不充分。很多研究只看 infrastructure stocks 或 per capita supply，而不是人口实际暴露到多少附近基础设施。一个国家总设施量高，不代表多数居民接近这些设施。

第二，多数研究只看单一类型基础设施，例如道路、水、电或绿地。这样难以比较 economic、social、environmental infrastructure 之间的差异，也难以识别某个地区到底是经济设施短缺、社会服务短缺，还是环境基础设施薄弱。

第三，基础设施不平等与健康之间的全球关系还不清楚。交通、电力、医疗、绿地和环境质量都可能影响健康，但多维基础设施 access/inequality 与 HALE、DALYs 的关系缺少跨国比较。

因此，文章提出三个研究问题：

```text
1. 不同 infrastructure types 和 scales 上，access 有什么差异？

2. infrastructure access inequality 怎样随类型和地区变化？

3. infrastructure access / inequality 与 health outcomes 有什么关系？
```

## 2. Figure 1：概念框架和研究设计

![Fig. 1 conceptual framework](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-02-figure-01.jpg)

Fig. 1a 定义三类基础设施。

Economic infrastructure 指支持商业和经济活动的设施，包括通信、能源、交通和分配网络。

Social infrastructure 指支持社会服务的设施，包括学校、医院和诊所。

Environmental infrastructure 指影响生活条件和 ecosystem services 的设施或环境条件，包括水和废弃物设施、绿地、清洁空气和热舒适。

Fig. 1b 给出研究流程。作者先用 population-weighted exposure model 估计 human access，然后把 economic、social、environmental 三个维度放进一个三维框架中分成 high/medium/low。接着分析 access disparities、access inequality，最后检验它们与 human health 的关系。

这个图的作用是把文章从“基础设施数量”转向“人口-设施互动”：

```text
infrastructure is not only supply

access depends on where people are

inequality depends on how access is distributed across people

health association depends on both level and inequality
```

## 3. Infrastructure mapping：三类基础设施怎样被建图

作者首先在全球尺度生成 2020 年 $0.1^\circ\times0.1^\circ$ 网格的 economic、social、environmental infrastructure maps。

基础数据包括 Harmonized Global Critical Infrastructure dataset、land cover、PM2.5、ERA5 climate reanalysis、night-time lights 等。critical infrastructure dataset 来自 OSM 衍生数据，包含 39 种基础设施类型。

作者先把 39 种基础设施重分类。

```text
economic:
    telecommunication
    energy
    transport

social:
    health
    education

environmental:
    water and waste
    green space
    clean air
    thermal comfort
```

每种基础设施原始 raster value 可能量纲不同。例如 power poles 数量和 tertiary roads 数量不能直接相加。因此作者先把每个 infrastructure type layer 标准化到 0-1，然后 equal-weight aggregation 到三类初始基础设施图层。

Environmental infrastructure 比较特殊，因为它不只是“设施数量”，还包括环境质量。因此作者把 water/waste infrastructure、green space、PM2.5 和 heat duration 合成：

$$
\mathrm{Env}
=
0.5\times \mathrm{CI}_{env}
+
0.5\times
\frac{
e^{\mathrm{Green}}
}{
\ln\!\left(e^{\mathrm{Air}}\times e^{\mathrm{Heat}}\right)
}.
\tag{1}
$$

这里 $\mathrm{CI}_{env}$ 是从 critical infrastructure dataset 重分类出来的 water/waste layer。$\mathrm{Green}$ 是绿地覆盖层。$\mathrm{Air}$ 是归一化 PM2.5，$\mathrm{Heat}$ 是归一化 heat duration。

这个公式可以按“好因素”和“坏因素”读。

绿地越多，$e^{\mathrm{Green}}$ 越大，environmental infrastructure score 越高。PM2.5 和 heat duration 越高，分母 $\ln(e^{\mathrm{Air}}e^{\mathrm{Heat}})$ 越大，score 被压低。也就是说，环境基础设施不是简单的绿地数量，而是把水/废弃物设施、绿地、空气污染和热暴露合成一个正向指标。

## 4. Socio-economic infrastructure calibration：为什么要用 night-time lights

Economic 和 social infrastructure 来自 OSM 衍生 critical infrastructure dataset。OSM 是 volunteered geographic information，全球覆盖不均衡。发展中地区可能有系统性缺失。如果直接使用 OSM 设施数量，容易把“没被记录”误读成“没有设施”。

作者用 VIIRS night-time lights，简称 NTL，作为 surrogate 来校准 economic/social infrastructure。NTL 指卫星在夜间观测到的地表灯光辐射强度。城市道路照明、居民区、商业区、工业区、港口、机场和交通节点都会贡献夜间灯光，所以 NTL 常被当作 socio-economic activity 的遥感代理变量。

这里需要注意，NTL 不是基础设施本身。它不直接告诉我们某个 grid cell 里有多少医院、学校、道路或电力设施。它的作用是提供一个外部参照：如果某个区域 OSM-derived infrastructure value 很低，但夜间灯光很强，那么它可能不是“真实基础设施很少”，而是 OSM 记录不完整。反过来，如果 OSM 值和 NTL 在统计上有稳定关系，就可以用 NTL 帮助校准 OSM 衍生的 economic/social infrastructure layers。

作者选择 continental United States 作为 calibration site，因为美国 OSM 覆盖相对完整，更适合作为“OSM 记录较可信”的标定区域。校准的逻辑是先在美国建立关系：

```text
OSM-derived infrastructure value
    <->
VIIRS night-time light intensity
```

然后把这个关系迁移到全球，用来修正其他地区可能因 OSM 缺失而低估的 infrastructure value。

接下来作者使用 global urban boundary，简称 GUB，来限制 calibration pixels。原因是 NTL 与经济、社会基础设施的关系主要发生在城市和城市边缘。如果把大量 rural 或 undeveloped pixels 放进回归，很多地方既没有灯光也没有基础设施，会让回归关系被“共同接近 0”的像素主导，反而削弱对城市基础设施的解释力。

因此，他们在 GUB 周边设置不同 buffer sizes，从 0 到 25 km，分别取这些城市边界附近的 grid cells。buffer size 的含义是：以 global urban boundary 为基准，向外或周边扩展一定距离，保留这个范围内的像素做 NTL-infrastructure regression。buffer 太小，可能只看到核心建成区，漏掉城市边缘基础设施；buffer 太大，又会把太多非城市区域纳入，增加噪声。

在每个 buffer setting 下，作者都在 $0.1^\circ\times0.1^\circ$ grid scale 上回归 NTL 和 infrastructure values。这里使用的是 log-log relationship，也就是比较 $\ln(\mathrm{NTL})$ 和 $\ln(I')$ 或 $\ln(I)$ 的线性关系。这样做的原因是夜间灯光和基础设施都高度偏态：少数城市格网值很高，大量区域值较低。取 log 后，极端高值不会完全主导拟合，也更接近 power-law scaling 的形式。

结果显示，5-km buffer 中 NTL 与 economic infrastructure 的 log-log 关系最强，相关系数约为 $r=0.71$，且显著。因此作者采用 5-km model 的回归系数进行全球校准：

$$
\ln(I)
=
1.58\times \ln(I')
+
5.03.
\tag{2}
$$

这里 $I'$ 是 OSM-derived initial economic/social infrastructure value，$I$ 是校准后的 infrastructure value。

把 Eq. (2) 指数化，可以看得更直观：

$$
I
=
e^{5.03}\left(I'\right)^{1.58}.
$$

这说明校准不是简单加一个常数，而是一个 power-law scaling。初始设施值较高的地方会被非线性放大；初始值较低的地方被保留在较低区间。

作者再用 GDP 和 HDI 做 validation：经济基础设施总量与 GDP 相关，社会基础设施总量与 HDI 相关。主文报告 country-level 相关系数分别约为 $r=0.90$ 和 $r=0.89$，都显著。

## 5. Human access：为什么要 population-weighted exposure

文章最核心的测量公式是 population-weighted exposure：

$$
\mathrm{IE}^{k}
=
\frac{
\sum_{i=1}^{N}P_i I_i^k
}{
\sum_{i=1}^{N}P_i
}.
\tag{3}
$$

这里 $k$ 表示 infrastructure type，可以是 economic、social 或 environmental。$i$ 是某个 administrative unit 内的 grid cell。$P_i$ 是第 $i$ 个 grid 的人口，$I_i^k$ 是该 grid 的第 $k$ 类基础设施值，$N$ 是该 administrative unit 内 grid 数量。

这个公式本质上是一个人口加权平均。若某个 grid 有很多 infrastructure 但几乎没人住，它对 human access 的贡献很小；若某个 grid 人口很多且基础设施高，它贡献很大。

这一步的物理含义是：

```text
infrastructure access
    ≠ average infrastructure per grid

infrastructure access
    = average infrastructure experienced by people
```

作者随后把每类 $\mathrm{IE}^k$ 除以其 95th percentile，并把超过阈值的值截断为 1。这样得到 0-1 范围内的 normalized access index。值越高，表示人口加权意义上的基础设施 access 越高。

## 6. Figure 2 和 Table 1：全球 access 格局

![Fig. 2a economic access map](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-03-figure-01.jpg)

Fig. 2a 显示 country-level economic infrastructure access。欧洲、亚洲、北美、南美总体较高；非洲较低。

![Fig. 2b social access map](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-03-figure-02.jpg)

Fig. 2b 显示 social infrastructure access。社会基础设施的全球差距更明显，非洲最低，Global North 显著高于 Global South。

![Fig. 2c environmental access map](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-03-figure-05.jpg)

Fig. 2c 显示 environmental infrastructure access。它和 economic/social 不完全一致，因为它受绿地、污染和热暴露影响。Oceania、South America 和 Europe 较高；Asia 的 environmental access 最低。

![Fig. 2d economic access boxplot](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-03-chart-01.jpg)

![Fig. 2e social access boxplot](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-03-chart-02.jpg)

![Fig. 2f environmental access boxplot](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-03-chart-03.jpg)

Fig. 2d-f 用 boxplots 比较 Global North 和 Global South。主文结果是：Global North 的 economic、social、environmental infrastructure access 分别是 Global South 的 1.25、2.00 和 1.43 倍。county level 上差异仍然存在，三类 access 分别是 1.41、2.63 和 1.22 倍。

Table 1 提供区域统计。全球均值上，economic access 最高，约 0.39；environmental 约 0.35；social 约 0.29。Africa 在 economic 和 social 上最低，Asia 在 environmental 上最低。

这一步建立第一条结论：Global South 不是所有基础设施都低到同一程度，而是不同 infrastructure dimensions 之间存在异质性。

## 7. Figure 3：三维 access 组合怎样分类

作者把 economic、social、environmental 三个 access values 分别按 25th 和 75th percentiles 分成 H/M/L。三维组合一共有 $3^3=27$ 种，例如 H-M-L 表示 economic high、social medium、environmental low。

然后作者把 27 种组合聚合成三类。

```text
Class I:
    overall above average
    no dimension is low
    relatively balanced high/medium access

Class II:
    moderate overall access
    at least one high and one low
    strong cross-dimensional disparity

Class III:
    below average
    no dimension is high
    generally low or medium-low access
```

![Fig. 3 composite access map](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-05-figure-01.jpg)

Fig. 3a 是 country-level composite map。最常见类别是 M-M-M、H-M-M 和 H-H-M。H-H-H 只有少数国家，包括 Australia、Canada、Chile、Peru 和 Portugal。L-L-L 则包括 Burkina Faso、Central African Republic、Chad、Djibouti、Guinea、Mauritania、Niger、South Sudan 和 Sierra Leone。

![Fig. 3 country/county bars](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-05-chart-01.jpg)

Fig. 3 的 bar charts 显示 Global North 大多数国家属于 Class I，Global South 则分布更分散。主文给出：Global North 中 45/54 属于 Class I；Global South 中 38 个国家属于 Class I，约 26% 属于 Class II，约 40% 属于 Class III。

![Fig. 3 zoomed county maps](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-05-figure-05.jpg)

Fig. 3c-e 的 zoomed maps 说明一个重要问题：国家级分类会掩盖内部差异。即使 Canada 和 United States 这类 Class I countries 内部，也有不少 counties 属于 Class II 或 III。反过来，非洲或亚洲某些整体较弱的国家内部，也存在 Class I regions。

这一步把文章从“Global North vs Global South”推进到“within-country heterogeneity”。

## 8. Gini：infrastructure access inequality 怎么计算

Access level 是平均水平，不等于 inequality。一个国家可以平均 access 很高，但国内分配极不均匀。作者用 Gini coefficient 和 Inq 来衡量 infrastructure access inequality。

Gini 来自 Lorenz curve。把居民按 infrastructure access 从低到高排序，横轴是 cumulative population share，纵轴是 cumulative infrastructure access share。若所有人 access 完全一样，Lorenz curve 就是 45-degree equality line。Lorenz curve 离 equality line 越远，不平等越高。

补充材料写出：

$$
\mathrm{Gini}
=
\frac{\mathrm{Area}_A}{\mathrm{Area}_A+\mathrm{Area}_B}.
\tag{S1}
$$

其中 $\mathrm{Area}_A$ 是 equality line 与 Lorenz curve 之间的面积，$\mathrm{Area}_B$ 是 Lorenz curve 下方的面积。因为坐标轴都在 0 到 1 范围内，$\mathrm{Area}_A+\mathrm{Area}_B=0.5$，所以：

$$
\mathrm{Gini}
=
\frac{\mathrm{Area}_A}{0.5}
=
\frac{0.5-\mathrm{Area}_B}{0.5}
=
1-2\mathrm{Area}_B.
\tag{S2}
$$

接下来要计算 $\mathrm{Area}_B$。作者把 Lorenz curve 下方区域拆成一系列 trapezoids。第 $i$ 个居民贡献的 trapezoid 面积为：

$$
\mathrm{Area}_{B_i}
=
\frac{1}{2}
\left(
\frac{\sum_{j=1}^{i-1} I_j}{\sum_{j=1}^{n} I_j}
+
\frac{\sum_{j=1}^{i} I_j}{\sum_{j=1}^{n} I_j}
\right)
\frac{1}{n}.
\tag{S3}
$$

这里 $I_j$ 是第 $j$ 个居民暴露到的 infrastructure access，$n$ 是居民总数。括号中两个分数分别是 trapezoid 左右两端的 cumulative infrastructure share，高度取平均；$1/n$ 是每个居民对应的 cumulative population share 宽度。

把所有 trapezoids 加起来：

$$
\mathrm{Area}_B
=
\sum_{i=1}^{n}
\frac{1}{2}
\left(
\frac{\sum_{j=1}^{i-1} I_j}{\sum_{j=1}^{n} I_j}
+
\frac{\sum_{j=1}^{i} I_j}{\sum_{j=1}^{n} I_j}
\right)
\frac{1}{n}.
\tag{S4}
$$

把 Eq. (S4) 代入 Eq. (S2)，得到离散形式的 Gini：

$$
\mathrm{Gini}
=
1
-
\frac{
\sum_{i=1}^{n}\sum_{j=1}^{i-1} I_j
+
\sum_{i=1}^{n}\sum_{j=1}^{i} I_j
}{
n\sum_{j=1}^{n} I_j
}.
\tag{S5}
$$

这个公式的意义是：如果 infrastructure access 在居民之间分布越均匀，Lorenz curve 越接近 equality line，$\mathrm{Area}_B$ 越接近 0.5，Gini 越接近 0。反之，若少数人享有大部分 infrastructure access，Lorenz curve 下方面积变小，Gini 越接近 1。

作者还使用 Inequality index 作为辅助：

$$
\mathrm{Inq}
=
\frac{\sigma}{\sqrt{\mu(1-\mu)}},
\qquad
0<\mu<1.
\tag{S6}
$$

这里 $\mu$ 是一个国家内 county-scale access values 的均值，$\sigma$ 是标准差。它把空间异质性相对于均值尺度标准化。Inq 同样在 0 到 1 之间，越高表示空间不均等越强。

## 9. Figure 4 和 Table 1：基础设施不平等的全球格局

![Fig. 4 access inequality](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-06-figure-01.jpg)

Fig. 4a-c 是 economic、social、environmental infrastructure access inequality 的地图，Fig. 4d-f 是 Global North/Global South 的 boxplots。

主文结论很清楚：social infrastructure access inequality 最高，平均 Gini 为 0.83；economic 平均 Gini 为 0.55；environmental 平均 Gini 为 0.35。

为什么 social infrastructure Gini 高？因为学校、医院、诊所等社会服务设施高度集中，且不一定随着人口分布均匀铺开。一个国家可能有高水平医疗或教育设施，但高度集中在首都、核心城市或富裕地区。

区域上，Africa 的 economic 和 social inequality 最高，均值分别约 0.61 和 0.87。Asia 的 environmental inequality 最高，约 0.43。

Global South 的不平等也显著高于 Global North：economic、social、environmental access inequality 分别是 Global North 的 1.23、1.09 和 1.44 倍。

这一步建立第二条结论：

```text
Global South:
    lower infrastructure access
    higher infrastructure inequality

Social infrastructure:
    highest inequality globally

Economic infrastructure inequality:
    later becomes strongest health predictor
```

## 10. Figure 5：access / inequality 与 HALE 的相关关系

作者使用 HALE，即 health-adjusted life expectancy，作为健康水平指标。HALE 比普通 life expectancy 更严格，因为它考虑健康状态下的预期寿命。

![Fig. 5a economic access vs HALE](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-07-chart-01.jpg)

Fig. 5a 显示 economic access 与 HALE 正相关。Global South 的斜率更陡，说明在 access 较低的发展中地区，经济基础设施改善与 HALE 提升的关联更强。

![Fig. 5b social access vs HALE](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-07-chart-02.jpg)

Fig. 5b 显示 social access 与 HALE 也为正相关。教育和医疗设施的可及性越高，健康调整寿命越高。

![Fig. 5c environmental access vs HALE](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-07-chart-03.jpg)

Fig. 5c 中 environmental access 与 HALE 没有显著关系。这不意味着环境基础设施不重要，而可能说明这个 composite environmental index 与 national-level HALE 的关系更复杂，或者被 income、health system、climate zone 等因素混合。

![Fig. 5d economic inequality vs HALE](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-07-chart-04.jpg)

Fig. 5d 是最关键的相关图。economic access inequality 越高，HALE 越低。Global North 和 Global South 都呈负相关。

![Fig. 5e social inequality vs HALE](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-07-chart-05.jpg)

Fig. 5e 显示 social inequality 与 HALE 也有负相关趋势，但后面的 mixed-effects model 中 social variables 不如 economic variables 稳定显著。

![Fig. 5f environmental inequality vs HALE](../../pdfs/2026-05-01/inequality-in-infrastructure-access-and-its-association-with-health-disparities/inequality-in-infrastructure-access-and-its-association-with-health-disparities.mineru/inequality-in-infrastructure-access-and-its-association-with-health-disparities/auto/images/page-07-chart-06.jpg)

Fig. 5f 的 environmental inequality 呈现 Global North 与 Global South 的对比关系。Global North 中 inequality 上升对应 HALE 下降；Global South 中关系不同。这提示 environmental infrastructure 与 health 的关系可能受到气候、污染、城市化阶段和基础健康系统的调节。

## 11. Mixed-effects models：为什么要从相关走向控制变量模型

相关图只能说明 association，不能控制 GDP、人口规模和 Global North/South baseline differences。作者因此建立 linear mixed-effects models。

Model I 只放 infrastructure access：

$$
\mathrm{Health}_{j,g}
=
\beta_0
+
\gamma_g
+
\beta_1 \mathrm{LnPop}_{j,g}
+
\beta_2 \mathrm{LnGDP}_{j,g}
+
\beta_3 \mathrm{ExpEco}_{j,g}
+
\beta_4 \mathrm{ExpSoc}_{j,g}
+
\varepsilon_{j,g}.
\tag{4}
$$

这里 $j$ 表示国家，$g$ 表示 Global North 或 Global South group。$\gamma_g$ 是 group-level random intercept，用来吸收 Global North/South baseline health differences。$\mathrm{LnPop}$ 和 $\mathrm{LnGDP}$ 是控制变量。$\mathrm{ExpEco}$ 和 $\mathrm{ExpSoc}$ 是 economic/social infrastructure access。

Model II 只放 access inequality：

$$
\mathrm{Health}_{j,g}
=
\beta_0
+
\gamma_g
+
\beta_1 \mathrm{LnPop}_{j,g}
+
\beta_2 \mathrm{LnGDP}_{j,g}
+
\beta_3 \mathrm{GiniEco}_{j,g}
+
\beta_4 \mathrm{GiniSoc}_{j,g}
+
\varepsilon_{j,g}.
\tag{5}
$$

这一步问的是：在控制人口和 GDP 后，基础设施不平等本身是否仍然与健康相关。

Model III 同时放 access 和 inequality：

$$
\mathrm{Health}_{j,g}
=
\beta_0
+
\gamma_g
+
\beta_1 \mathrm{LnPop}_{j,g}
+
\beta_2 \mathrm{LnGDP}_{j,g}
+
\beta_3 \mathrm{ExpEco}_{j,g}
+
\beta_4 \mathrm{ExpSoc}_{j,g}
+
\beta_5 \mathrm{GiniEco}_{j,g}
+
\beta_6 \mathrm{GiniSoc}_{j,g}
+
\varepsilon_{j,g}.
\tag{6}
$$

Model III 的作用是比较 level effect 和 inequality effect。也就是说，在 access 水平相似时，不平等是否仍然有独立关联。

Table 2 的核心结果是：在 Model III 中，economic infrastructure access $\mathrm{ExpEco}$ 与 HALE 正相关，coefficient 为 3.84，$P=0.035$；economic infrastructure inequality $\mathrm{GiniEco}$ 与 HALE 负相关，coefficient 为 -9.95，$P=0.003$。

作者解释为：economic infrastructure access inequality 每增加 10%，对应 HALE 约减少 1 年。这个说法来自 $-9.95\times0.1\approx-0.995$。

相比之下，social access 和 social inequality 在 mixed model 中没有达到 $P<0.05$。这不说明社会基础设施不重要，而是说明在这个国家级模型、控制 GDP/人口和 group random intercept 后，economic infrastructure factors 是更稳定的 predictor。

作者还把 response variable 换成 DALYs，发现类似方向：economic access 越低、economic inequality 越高，disease burden 越高。

## 12. Random forest 和 sensitivity analyses

除了 mixed-effects regressions，作者还用 random forest 检验变量重要性。输入变量是 Models I-III 中的六个 covariates：ExpEco、ExpSoc、GiniEco、GiniSoc、LnPop、LnGDP。响应变量分别是 HALE 和 DALYs。每个 random forest 有 500 trees，重复 100 次。

这个机器学习部分的作用不是替代 mixed-effects model，而是从 nonlinear predictive importance 的角度验证哪些变量对 health outcomes 更重要。

Sensitivity analyses 有两类。

第一，测试 water and waste infrastructure 是否放入 economic/social categories 会影响结果。因为基础设施分类没有全球统一标准，water/waste 可以被归为环境，也可以被归为经济或社会基础设施。作者用这个 sensitivity check 检查分类选择是否改变 country-level access values。

第二，检查基础设施类型之间的 correlations 和 interactions。现实中基础设施存在 interdependency：医院需要能源，通信依赖电力，道路影响医疗可达性。文章主模型没有完整建模这种 interdependency，因此用补充分析作为初步检验。

## 13. Discussion：主结论与政策含义

文章的第一条主结论是 Global South 的双重 disadvantage。Global South 拥有全球约 85% 的人口，但 infrastructure access 只有 Global North 的 50-80%，不平等水平却高 9-44%。

第二条主结论是多维 access pattern 很重要。一个地区可能 economic/social 高但 environmental 低，例如 H-H-L 或 H-M-L；也可能 environmental 高但 economic/social 低，例如 L-L-H。政策不能只问“基础设施够不够”，还要问“哪一类不足，以及三类之间是否失衡”。

第三条主结论是 inequality 本身与健康相关。经济基础设施不平等，特别是 transportation、telecommunications、housing 等维度的不平等，可能削弱健康 outcomes。即使提高总量，如果新增设施集中在少数地区，也可能无法改善甚至可能加剧健康差距。

政策含义是：基础设施投资应该基于 spatial assessment of needs，而不是只追求总量增长。尤其在快速人口增长的 Global South，如果人口增长快于基础设施建设，access inequality 可能继续恶化。

## 14. 局限：为什么这不是完整的人-基础设施互动模型

作者承认四类局限。

第一，infrastructure classification 没有统一标准。Economic、social、environmental 的分类是一个 flexible comparative framework，但某些设施可能跨类，例如 water/waste。

第二，population-weighted exposure model 假设人口分布静态，强调 physical proximity，而没有考虑日常 mobility。人们可能在居住地之外使用医院、学校或交通设施，也可能在通勤中暴露于噪声和空气污染。

第三，空间接近不等于真实可达。gated communities、restricted roads、制度性隔离、费用门槛都可能让 nearby infrastructure 无法被实际使用。

第四，数据分辨率和 OSM 缺失限制了结果。0.1° 网格适合全球比较，但不能细致刻画 intra-country heterogeneity。OSM-derived critical infrastructure 在欠发达地区可能缺失更多，这会影响测量。

## 15. 对 Synthetic_City / 城市生成研究的启发

这篇文章对 Synthetic_City 的启发在 condition construction 和 exposure metrics 上。

第一，它提醒我们，condition 不应只做行政区 aggregate summaries。人口和设施的空间错位会导致 per capita 或 total supply 指标失真。对于 synthetic population / mobility generation，condition 更合理的形式可能是 population-weighted 或 mobility-weighted exposure。

第二，它提供了多维 condition 的组织方式。Economic、social、environmental 三个维度可以变成一个 structured condition vector，而不是混合成一个黑箱指标。这样可以检查生成结果对不同维度的敏感性。

第三，Gini/Inq 说明 target distribution 的公平性可以单独测量。一个生成模型可能复现平均 access，但没有复现 inequality。对于 Synthetic_City，除了 marginal distribution，也应检查 group-level 或 region-level inequality metrics。

第四，作者明确指出下一步需要 human mobility data 来构建 spatiotemporally explicit interaction framework。这正好和 route generation / mobility prediction 的问题衔接：真实 access 不只是居住地附近有什么设施，还取决于人怎样移动、去哪里、哪些路径可行。

一句话总结：这篇文章把全球基础设施从“设施总量”改写成“人口加权 access + access inequality + health association”的问题，并说明 economic infrastructure inequality 是健康差距中最稳定的关联因素之一。
