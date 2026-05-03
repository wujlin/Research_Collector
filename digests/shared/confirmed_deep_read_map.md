---
title: "Confirmed Deep-Read Map"
generated_at: "2026-05-03"
paper_count: 12
book_chapter_count: 8
confirmed_item_count: 20
scope: "confirmed deep-read papers and book chapters only"
---

# Confirmed Deep-Read Map

这份文档只记录 **目前已经确认精读过** 的论文和书章，用来避免把三类东西混在一起：

1. 只是收进 `pdfs/` 的论文或书；
2. 建了 `digest` 但还没有真正精读的文本；
3. 已经做过逐节线性展开、公式讨论、图和逻辑反复改写的文本。

这里的标准按当前项目对话中的共同确认来定，而不是按 `pdfs/` 数量或 `digest` 数量来定。

## 一、当前已经形成的总脉络

目前真正搭起来的主线，不是“diffusion 模型总论”，而是下面这九层：

1. 生成模型可以被看成 **非平衡随机过程**，因此可以讨论不可逆性、熵产生和时间箭头。
2. forward diffusion protocol 不是普通 noise schedule，而是一条带有 **entropy production / Wasserstein speed cost** 的 probability path，它会约束 reverse generation 的 robustness。
3. 生成或采样过程可以被写成 **控制 / 势函数 / 输运问题**，因此 HJ/HJB 语言会自然进入。
4. 不完整观测下的问题本质上是 **inverse problem**，因此 posterior、VI、UQ 会自然进入。
5. 学习对象未必是单个样本，也可能是 **density、measure、path、posterior family** 这样的结构化对象。
6. 城市系统中的 scaling law 不是简单 log-log 拟合，而是关于 **条件期望、波动结构和预测能力** 的统计假设。
7. 城市增长模型从 Yule-Simon、Gibrat 到 GBM / Fokker-Planck，核心是在解释 **multiplicative growth、barrier、drift 和 tail formation**。
8. migration 不是外部细节，而是会改变城市 size distribution 的 **耦合、扩散和 regularization 机制**。
9. 当 migration shocks 具有 heavy tail 时，城市增长方程需要从 Gaussian noise 走向 **Levy noise、generalized CLT 和 fractional Fokker-Planck**。

下面按这条主线分组整理。

## 二、随机热力学、熵产生与不可逆性

### 1. Learning stochastic thermodynamics directly from correlation and trajectory-fluctuation currents

对应 digest：`2026-04-10/learning-stochastic-thermodynamics-directly-from-correlation-and-trajectory-fluctuation-currents.md`

作者：**Jinghao Lyu, Kyle J. Ray, James P. Crutchfield**。  
机构：**Complexity Sciences Center / Physics Department, University of California at Davis**。  
作者脉络：这是 UC Davis complexity science / computational mechanics 这条线进入 stochastic thermodynamics inference 的工作。Crutchfield 这条脉络长期把 information theory、computational mechanics 和 nonequilibrium statistical physics 接在一起；这篇文章把这个视角具体落到 trajectory currents 和 entropy production estimation 上。  
核心问题：如果没有显式的热力学标签，能否只靠短时间轨迹统计量直接学习局域热力学对象。  
核心逻辑：作者把随机热力学改写成一个 `self-supervised function learning` 问题，用局域相关函数和轨迹涨落电流构造 loss，直接学习 `drift`、`probability velocity`、`temporal score` 和 `diffusion field`，再由此恢复 entropy production 结构。  
在整条主线里的位置：这是你最早建立“**局域电流、涨落和熵产生可以直接相连**”这层理解的起点。

### 2. Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility

对应 digest：`2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level.md`

作者：**Julius Degünther, Jann van der Meer, Udo Seifert**。  
机构：**II. Institut für Theoretische Physik, Universität Stuttgart**。  
作者脉络：这是 Stuttgart 的 **Udo Seifert** stochastic thermodynamics 主线。Seifert 这条线的核心是把热力学量重新定义到 single trajectory 和 fluctuation level 上，再进一步讨论有限观测、粗粒化和不可逆性定位。  
核心问题：当系统只能被粗粒化地观测时，还能不能定义、推断并局域化 entropy production。  
核心逻辑：作者引入 `snippets` 和 `Markovian events`，在 coarse-grained 层重新定义 fluctuating entropy production。这个量不只给平均不可逆性，还能把 irreversibility 局域到具体事件类型和 waiting-time structure 上。  
在整条主线里的位置：这篇把你的“**有限观测下怎样仍然做 thermodynamic inference**”这条线真正钉住了。

### 3. Nonequilibrium Physics of Generative Diffusion Models

对应 digest：`2026-04-16/nonequilibrium-physics-of-generative-diffusion-models.md`

作者：**Zhendong Yu, Haiping Huang**。  
机构：**PMI Lab, School of Physics, Sun Yat-sen University**；Haiping Huang 同时关联 **Guangdong Provincial Key Laboratory of Magnetoelectric Physics and Devices, Sun Yat-sen University**。  
作者脉络：这是 Haiping Huang 统计物理理解 neural computation / generative model 的路线。Huang 的长期方向包括 disorder systems、replica / cavity methods、random matrix、dynamical mean-field theory，以及 deep neural networks 的统计物理机制。  
核心问题：diffusion generative model 是否可以被系统地解释为一个非平衡热力学过程。  
核心逻辑：文章用 fluctuation theorem、entropy production、equilibrium measure 和 Franz-Parisi potential 来分析 diffusion 的 forward / reverse dynamics，把生成扩散直接放进 stochastic thermodynamics 的语言里。  
在整条主线里的位置：这篇建立了“**diffusion 模型是耗散的、不可逆的非平衡过程**”这一层解释。

### 4. Speed-Accuracy Relations for Diffusion Models: Wisdom from Nonequilibrium Thermodynamics and Optimal Transport

对应 digest：`2026-04-28/speed-accuracy-relations-for-diffusion-models.md`

作者：**Kotaro Ikeda, Tomoya Uda, Daisuke Okanohara, Sosuke Ito**。
机构：**Kotaro Ikeda** 来自 The University of Tokyo Department of Mathematical Engineering and Information Physics；**Tomoya Uda** 来自 The University of Tokyo Department of Earth and Planetary Physics；**Daisuke Okanohara** 来自 Preferred Networks Inc.；**Sosuke Ito** 来自 The University of Tokyo Universal Biology Institute。
作者脉络：这是 Sosuke Ito 的 stochastic thermodynamics / information geometry / optimal transport 线和 diffusion model 结合的一篇文章。它不是泛泛地说 diffusion 有热力学类比，而是把 Fokker-Planck current、entropy production、Wasserstein speed limit 和 generative reverse error 放进同一条不等式链。
核心问题：diffusion model 的 forward protocol 是否会定量限制 reverse generation 对初始噪声误差的敏感性。
核心逻辑：文章证明 speed-accuracy relation：reverse error response 的 $\mathcal{W}_1$ 变化受 forward entropy production / Wasserstein speed cost 控制；没有 non-conservative force 时，最优 protocol 对应 $\mathcal{W}_2$ 空间中的 constant-speed geodesic。它还把 cosine schedule、conditional OT schedule 和真实图像 latent flow matching 放到同一个 robustness diagnostic 中比较。
在整条主线里的位置：这篇把“**diffusion 的热力学解释**”从概念类比推进到 **可计算的 protocol design criterion**：好的生成路径不只是 loss 低，还应该有低耗散、低绕路、低 sensitivity 的 distributional path。

### 5. Stochastic Thermodynamics for Autoregressive Generative Models

对应 digest：`2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models.md`

作者：**Takahiro Sagawa**。  
机构：论文署名来自 **Department of Applied Physics, The University of Tokyo**，并关联 **Quantum-Phase Electronics Center (QPEC), The University of Tokyo** 和 **Inamori Research Institute for Science (InaRIS)**。  
作者脉络：Sagawa 是 information thermodynamics / stochastic thermodynamics 的核心作者之一，长期研究 Maxwell demon、information processing 和 nonequilibrium thermodynamics 的关系。这篇文章把这条线从物理系统推进到 autoregressive generative models 和 LLM 序列生成。  
核心问题：entropy production 的语言能否从 diffusion 扩展到 autoregressive / non-Markov generative models。  
核心逻辑：文章为 Transformer、RNN、Kalman filter、SSM、Mamba 这类自回归生成模型建立统一的 stochastic thermodynamics 框架，定义非马尔可夫观测序列上的 entropy production，并讨论 token-level、block-level 和 retrospective decomposition。  
在整条主线里的位置：这篇把“**不可逆性不是 diffusion 专属**”这件事彻底讲清了。

## 三、diffusion 的统计物理、相变与动力学 regime

### 6. Dynamical regimes of diffusion models

对应 digest：`2026-04-11/dynamical-regimes-of-diffusion-models.md`

作者：**Giulio Biroli, Tony Bonnaire, Valentin de Bortoli, Marc Mézard**。  
机构：**Giulio Biroli** 和 **Tony Bonnaire** 来自 Laboratoire de Physique de l'Ecole Normale Supérieure, ENS / PSL / CNRS / Sorbonne Université / Université Paris Cité；**Valentin de Bortoli** 来自 ENS Computer Science Department, CNRS, PSL University；**Marc Mézard** 来自 Department of Computing Sciences, Bocconi University。  
作者脉络：这是 spin glass / disordered systems / high-dimensional statistical physics 进入 diffusion model 理论的一条强线。Biroli 和 Mézard 代表高维统计物理、玻璃态、相变和信息统计物理传统；de Bortoli 则把 score-based diffusion、采样和概率方法接入这条线。  
核心问题：在高维、大样本极限下，diffusion model 的 backward dynamics 会经历哪些不同的 dynamical regimes。  
核心逻辑：作者指出 backward dynamics 并不是单一 denoising，而会经历 `pure noise -> class-level speciation -> sample-level collapse` 三个阶段，并用高维统计物理语言解释 speciation、collapse、phase transition 和 dimension dependence。  
在整条主线里的位置：这篇和 Haiping Huang 那篇互补。前者更偏 **非平衡热力学**，这篇更偏 **相变 / regime / collapse**。

## 四、HJ / HJB / 控制 / 输运

### 7. Generative Optimal Transport via Forward-Backward HJB Matching

对应 digest：`2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.md`

作者：**Haiqian Yang, Vishaal Krishnan, Sumit Sinha, L. Mahadevan**。  
机构：**Haiqian Yang** 来自 MIT Mechanical Engineering；**Vishaal Krishnan** 和 **Sumit Sinha** 来自 Harvard SEAS；**L. Mahadevan** 关联 Harvard SEAS、Physics 和 Organismic and Evolutionary Biology。  
作者脉络：这是 Mahadevan 体系里 mechanics、geometry、applied mathematics 和 biological / physical transport 问题相互交叉的一条线。文章把 stochastic control、optimal transport、non-equilibrium relaxation 和 HJB value function 接在一起，风格更接近物理直觉驱动的应用数学。  
核心问题：生成过程能否被改写成 forward-backward HJB matching，而不是直接学习高维控制场。  
核心逻辑：文章把 backward generative control 改写成 forward value function 学习问题，用标量势函数 $W/U$ 代替直接学习控制向量场，并通过时间反转把训练时的 forward relaxation 接回生成时的 backward control。  
在整条主线里的位置：这篇建立了“**生成 = value function / optimal control / transport**”这一层统一理解。

### 8. HJ-sampler: Bayesian Sampler via Hamilton-Jacobi PDEs and Score-Based Generative Models

对应 digest：`2026-04-16/hj-sampler.md`

作者：**Tingwei Meng, Zongren Zou, Jérôme Darbon, George Em Karniadakis**。  
机构：**Tingwei Meng** 来自 UCLA Mathematics；**Zongren Zou** 和 **Jérôme Darbon** 来自 Brown Applied Mathematics；**George Em Karniadakis** 来自 Brown Applied Mathematics，并关联 Pacific Northwest National Laboratory。  
作者脉络：**Darbon** 是 HJ PDE、optimal control、optimization 和 curse of dimensionality 这条线；**Karniadakis** 是 SciML、UQ、stochastic multiscale modeling、physics-informed learning 和 PDE-based machine learning 的核心人物之一。这里的组合使这篇文章天然处在 HJ PDE、Bayesian inference、score-based generative model 和 scientific computing 的交界处。  
核心问题：已知随机过程时，能否把 posterior path sampling 直接接到 HJ PDE 和 score-based 方法。  
核心逻辑：文章先写线性传播链，再用 log / Cole-Hopf 变换得到 HJ + density flow，然后把这个框架直接对齐到随机过程 inverse problem 里的 posterior path sampling，最后给出 Riccati-HJ-sampler 和 SGM-HJ-sampler 两条实现路线。  
在整条主线里的位置：这篇说明了“**HJ 语言不仅能解释生成控制，还能解释 posterior path sampling**”。

## 五、逆问题、VI、UQ

### 9. A Primer on Variational Inference for Physics-Informed Deep Generative Modelling

对应 digest：`2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.md`

作者：**Alex Glyn-Davies, Arnaud Vadeboncoeur, O. Deniz Akyildiz, Ieva Kazlauskaite, Mark Girolami**。  
机构：**Alex Glyn-Davies, Arnaud Vadeboncoeur, Mark Girolami** 来自 University of Cambridge Department of Engineering；**O. Deniz Akyildiz** 来自 Imperial College London Department of Mathematics；**Ieva Kazlauskaite** 来自 London School of Economics Department of Statistics。  
作者脉络：这篇处在 Bayesian inverse problems、probabilistic numerics、engineering statistics 和 physics-informed deep generative modelling 的交叉处。**Mark Girolami** 是 Cambridge data-centric engineering 和 probabilistic numerics / Bayesian methodology 的代表人物，同时担任 The Alan Turing Institute Chief Scientist。  
核心问题：面对 forward solver 昂贵、观测不完整、后验难算的物理问题，VI 为什么会自然出现。  
核心逻辑：文章从 forward problem 走到 inverse problem，再从 Bayes VI 走到 generative-model VI，最后把 VAE、normalizing flow、forward-model-based learning、residual-based learning 和 deep generative prior 串成一条线。  
在整条主线里的位置：这篇建立了“**physics-informed inference 的核心不是单纯快，而是要组织 posterior、surrogate、PDE residual 和 uncertainty**”。

## 六、更一般的结构化动力学对象

### 10. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data

对应 digest：`2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-particle-data.md`

作者：**Liyao Lyu, Xinyue Yu, Hayden Schaeffer**。  
机构：三位作者均来自 **Department of Mathematics, University of California, Los Angeles**。  
作者脉络：这是 UCLA applied mathematics / scientific machine learning 这条线。Hayden Schaeffer 的方向包括 scientific machine learning、PDE、inverse problems、operator learning 和 mathematical modeling；Liyao Lyu 在 Schaeffer group 中，研究位置接近 interacting particle systems 与 measure-dependent dynamics。  
核心问题：如果单粒子动力学依赖整个粒子群当前分布，能否直接从粒子轨迹学习这种 `measure-dependent drift`。  
核心逻辑：文章提出 `measure-valued neural network`，把 probability measure 当作网络输入对象，通过 cylindrical features / measure embedding 学 McKean-Vlasov dynamics，并给出 well-posedness、propagation of chaos、universal approximation 和逼近率。  
在整条主线里的位置：这篇让“**学习对象可以是 measure，而不是普通向量**”这件事变得清楚。

### 11. Non-Markovian rock-paper-scissors games

对应 digest：`2026-04-13/non-markovian-rock-paper-scissors-games.md`

作者：**Ohad Vilk, Mauro Mobilia, Michael Assaf**。  
机构：**Ohad Vilk** 和 **Michael Assaf** 来自 Racah Institute of Physics, The Hebrew University of Jerusalem；**Mauro Mobilia** 来自 Department of Applied Mathematics, School of Mathematics, University of Leeds。  
作者脉络：这是 nonequilibrium stochastic dynamics、population dynamics、large deviations 和 evolutionary game theory 的交叉线。Assaf 的工作常围绕 stochastic population dynamics 和 large-deviation rare events；Mobilia 长期研究随机演化动力学、cyclic competition 和 finite-population effects。  
核心问题：当等待时间不是指数分布时，memory 和 non-Markov 更新怎样改写经典 rock-paper-scissors 动力学。  
核心逻辑：文章表明，一旦把 Markovian exponential clock 换成具有长记忆和非指数 waiting-time 的更新过程，经典的 `law of the weakest` 不再稳固，系统的长期选择结果会被 non-Markov structure 显著改写。  
在整条主线里的位置：这篇说明了“**动力学对象一旦脱离 Markov 假设，很多经典结论都会失效**”。

### 12. Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model

对应 digest：`2026-04-16/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.md`

作者：**Kentaro Fujii, Shingo Murata**。  
机构：**School of Integrated Design Engineering, Keio University**。  
作者脉络：这是 cognitive / developmental robotics、deep active inference、world model 和 real-world robot control 的交叉线。Murata 这条线更关心 predictive coding / active inference 这类认知计算框架如何落到机器人控制；这篇文章的重点是把 expected free energy 的决策逻辑做成真实机器人可运行的层级世界模型。  
核心问题：deep active inference 为什么很少真正落到真实机器人上，以及怎样把它变成可运行的控制框架。  
核心逻辑：文章用 `slow/fast` 两层时序世界模型表示环境，再用向量量化的 `action model` 把长动作序列压成少量离散 abstract actions，最后在抽象动作空间里计算 EFE，从而把 active inference 变成真实机器人上可跑的控制方法。  
在整条主线里的位置：这篇把“**free energy / active inference / world model**”从抽象理论推进到了实际控制。

## 七、城市 scaling、增长、迁移与重尾动力学

这条线来自 *Statistics and Dynamics of Urban Populations* 的连续章节精读。它和前面的生成模型主线不是同一类文献，但对 `Synthetic_City` 更直接：前面的论文提供 inverse problem、posterior、flow、control 和 uncertainty 的方法语言；这组章节则提供城市人口系统里 **scaling、growth、migration、heavy-tailed shock 和 spatial expansion** 的机制语言。

### 13. Statistics and Dynamics of Urban Populations, Chapter 2: Scaling in Cities

对应 digest：`2026-04-25/statistics-and-dynamics-of-urban-populations-ch02-scaling-in-cities.md`

核心问题：城市 scaling law 到底是在说什么，以及为什么不能只靠 log-log 拟合判断城市指标是否随人口规模呈现非线性。
核心逻辑：这一章把 scaling 从一句 $Y \sim P^\beta$ 展开成条件期望、噪声模型、Taylor's law、local exponent、benchmark city 和 out-of-sample prediction 的完整统计链条。它的关键点不是“找到一个漂亮指数”，而是检验 scaling exponent 是否真的稳定、是否能预测、是否只是 threshold effect 或 sampling artifact。
在整条主线里的位置：这章建立了“**城市 scaling 是强统计假设，不是默认事实**”这条警戒线。

### 14. Statistics and Dynamics of Urban Populations, Chapter 5: Stochastic Calculus for Urban Growth

对应 digest：`2026-04-25/statistics-and-dynamics-of-urban-populations-ch05-stochastic-calculus-for-urban-growth.md`

核心问题：如果城市增长要写成随机微分方程，white noise、Itô、Stratonovich 和 Fokker-Planck 到底各自承担什么角色。
核心逻辑：这一章从随机游走和 white noise 开始，解释为什么 stochastic integral 不能像普通积分一样处理；随后比较 Itô 与 Stratonovich 的物理含义，并把一步随机更新推到 Fokker-Planck equation。重点是 multiplicative noise 下 extra drift 从哪里来，以及为什么不同积分 convention 会改变概率密度演化。
在整条主线里的位置：这章给后面的城市增长模型提供 **SDE 到 density equation 的技术地基**。

### 15. Statistics and Dynamics of Urban Populations, Chapter 6: Stochastic Models of Growth

对应 digest：`2026-04-26/statistics-and-dynamics-of-urban-populations-ch06-stochastic-models-of-growth.md`

核心问题：城市 size distribution 的 power-law、lognormal 和 Zipf-like tail 能否从个体增长规则推出。
核心逻辑：这一章按机制展开 Yule、Simon、weak Gibrat、strong Gibrat、Marsili-Zhang、Zanette-Manrubia 和 Gabaix model。它说明 preferential attachment 可以通过年龄混合或 size-class master equation 生成 power-law；strong Gibrat 本身更自然地产生 lognormal；要得到稳定 Pareto / Zipf tail，通常还需要 negative drift、friction 或 reflective barrier。
在整条主线里的位置：这章把“**城市增长的尾部分布来自增长机制，而不只是拟合形状**”讲清楚。

### 16. Statistics and Dynamics of Urban Populations, Chapter 7: Models With Migration

对应 digest：`2026-04-27/statistics-and-dynamics-of-urban-populations-ch07-models-with-migration.md`

核心问题：当城市之间允许人口迁移时，原来只靠 birth-growth 的模型会怎样改变。
核心逻辑：这一章从 Haran-Vining 的 modified Yule-Simon model 进入 migration，再到 Haag et al. 的 utility-driven master equation，最后重点展开 Bouchaud-Mezard / Solomon-Richmond 这类 mean-field redistribution 模型。核心结构是：migration 既能把城市拉向平均规模，又能与 multiplicative growth noise 共同产生 stationary distribution 和 Pareto tail。
在整条主线里的位置：这章建立了“**migration 是 regularization / coupling / diffusion，不是增长模型的外部补丁**”。

### 17. Statistics and Dynamics of Urban Populations, Chapter 8: Generalized Central Limit Theorem and Levy Stable Laws

对应 digest：`2026-04-27/statistics-and-dynamics-of-urban-populations-ch08-generalized-central-limit-theorem-and-levy-stable-laws.md`

核心问题：为什么很多小扰动相加会给 Gaussian，但 heavy-tailed shocks 相加会给 Levy stable law。
核心逻辑：这一章从 law of large numbers、CLT 和 characteristic function 证明开始，逐步说明 finite variance 是 Gaussian limit 的关键前提；当 tail 足够重时，normalization 从 $\sqrt{N}$ 变成 $N^{1/\alpha}$，极限分布从 Gaussian 变成 Levy stable law。它还线性展开了 stable law 的 characteristic function、tail exponent、skewness parameter 和 generalized CLT。
在整条主线里的位置：这章给后面 migration shock 的 Levy noise 提供 **概率论理由**。

### 18. Statistics and Dynamics of Urban Populations, Chapter 9: From First Principles to the Growth Equation

对应 digest：`2026-04-27/statistics-and-dynamics-of-urban-populations-ch09-from-first-principles-to-the-growth-equation.md`

核心问题：如果不从 Zipf's law 倒推模型，而从人口 balance equation 出发，城市增长方程应该长什么样。
核心逻辑：这一章先把城市增长拆成 out-of-system growth 和 interurban migration，再把 migration 写成 directed weighted graph。平均迁移流可以用 size、distance、neighbor-number scaling 描述，但 pairwise residual / net migration shock 呈 heavy tail；因此 generalized CLT 会把 migration sum 推向 Levy stable noise，最终得到比 Gaussian Gibrat model 更能解释 turbulent rank dynamics 的增长方程。
在整条主线里的位置：这章是城市动力学线的核心转折点：**Gaussian growth noise 被 Levy migration noise 取代**。

### 19. Statistics and Dynamics of Urban Populations, Chapter 10: About City Dynamics

对应 digest：`2026-04-28/statistics-and-dynamics-of-urban-populations-ch10-about-city-dynamics.md`

核心问题：带 Levy noise 的城市增长方程会推出什么 population distribution 和 rank dynamics。
核心逻辑：这一章从 decoupled growth equation 出发，把 Levy SDE 推到 fractional Fokker-Planck equation，并比较 Itô / Stratonovich、force-free / linear force、large-tail expansion 和 scaling collapse。它还说明只看 distribution 不够，因为 heavy-tailed shocks 会产生更强的 rank jumps 和 turbulent rank dynamics。
在整条主线里的位置：这章把 Chapter 9 的机制方程推进到 **density evolution、tail asymptotics 和 rank dynamics**。

### 20. Statistics and Dynamics of Urban Populations, Chapter 11: Outlook: Beyond Zipf's Law

对应 digest：`2026-04-28/statistics-and-dynamics-of-urban-populations-ch11-outlook-beyond-zipfs-law.md`

核心问题：如果 Zipf's law 只是 loose approximation，城市动力学下一步应该研究什么。
核心逻辑：这一章把问题从 rank-size distribution 推到更宽的城市系统动力学：rare events、spatial migration flow、hierarchical organization、surface area growth、transport infrastructure 和 boundary evolution。它的主张是，未来模型不能只解释人口排序，还要解释城市如何在空间中扩张、如何通过迁移网络耦合、以及边界 $r(\theta,t)$ 如何变粗糙。
在整条主线里的位置：这章把城市动力学线从 **population distribution** 推向 **spatial structure and urban morphology**。

## 八、这 20 个 confirmed items 最后汇成了什么

如果把这 12 篇论文和 8 个章节再压成一句更紧的总脉络，它们共同搭出的不是“某一类生成模型教程”，而是：

1. 生成过程可以被理解为 **非平衡随机过程**。
2. 这些过程的方向性可以用 **entropy production / irreversibility** 来刻画。
3. diffusion 的 forward protocol 会产生 **entropy production / Wasserstein speed cost**，并约束 reverse generation 的 robustness。
4. 生成或采样又可以被改写成 **HJ/HJB、control、transport、posterior sampling**。
5. 一旦观测不完整，问题自然变成 **inverse problem**，需要 posterior、VI、UQ 语言。
6. 学习对象可以是 **sample、density、measure、path、posterior family**，而不只是单个输出向量。
7. 城市系统的 empirical regularity 不能只看 Zipf 或 log-log scaling，而要追问 **mechanism、noise、migration 和 prediction**。
8. 城市人口动力学里的随机项未必是 Gaussian；如果 migration residuals 重尾，growth equation 会自然走向 **Levy noise 和 fractional dynamics**。
9. 对城市研究来说，最终问题不只是人口分布，还包括 **迁移网络、空间层级、surface area 和边界演化**。

## 九、和当前 Synthetic_City 项目的直接关系

对 `Synthetic_City` 最有用的，不是所有 20 个 confirmed items 都等强，而是下面几条启发：

1. `VI primer` 提供主语义：你的问题本质上更像 **distribution-level amortized inverse problem**。
2. `HJB matching` 和 `HJ-sampler` 提供结构启发：不要直接学最难对象，要先换到更有结构的表示。
3. `MVNN` 提醒你：学习对象不一定是普通向量，distribution / measure 空间本身有几何结构。
4. `Speed-Accuracy Relations` 提供 protocol 诊断语义：如果后续继续使用 diffusion / flow / bridge model，不只要看 training loss，还要看 condition-to-target path 是否低耗散、短路径、低 sensitivity。
5. `entropy production / irreversibility` 这条线提醒你：如果以后真的引入 dynamics，才有必要认真讨论时间箭头、耗散和控制代价；在当前 `Synthetic_City` 问题里，这些更适合作为类比和灵感，而不是主数学语义。
6. `Scaling in Cities` 提醒你：condition summary 和 target distribution 之间不能只追求视觉拟合，还要问 scaling exponent、local exponent 和预测能力是否稳定。
7. `Stochastic Models of Growth` 到 `Models With Migration` 提醒你：PUMA-level synthetic allocation 可能需要区分内部增长、迁移耦合和空间 redistribution，而不是把所有残差都塞进一个 black-box decoder。
8. `Generalized CLT`、`Chapter 9` 和 `Chapter 10` 提醒你：如果 observed residual / migration shock 有 heavy tail，用 Gaussian uncertainty 会低估 rare but consequential allocation shifts。
9. `Chapter 11` 提醒你：未来如果把 `Synthetic_City` 从人口分配推进到空间形态生成，就需要显式处理 surface area、transport infrastructure 和 boundary roughness。

## 十、当前不应混入这份清单的文本

下面这些论文或章节即使已经建了 `digest`，目前也 **不应自动算进“确认精读主线”**：

- 只是收进 `pdfs/`，还没有系统展开；
- 只建了 `digest`，但没有做过逐节线性展开和反复改写；
- 在当前对话里没有被共同确认属于“已经精读过”。

这条边界要保留，避免以后再次把“候选阅读”和“已经吃透”混在一起。

## 十一、机构、作者与书章来源核对

这部分只记录用于核对作者、机构和学术脉络的来源，避免以后靠记忆补全。

- 局部电流与 entropy production：UC Davis Complexity Sciences Center 页面，`https://csc.ucdavis.edu/~cmg/compmech/pubs/currents.htm`。
- Coarse-grained entropy production：Physical Review Research 页面，`https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.023175`。
- Haiping Huang diffusion thermodynamics：Physical Review E 页面，`https://journals.aps.org/pre/abstract/10.1103/PhysRevE.111.014111`；Haiping Huang 中山大学主页，`https://spe.sysu.edu.cn/node/2338`。
- Speed-accuracy relations for diffusion models：本地 MinerU 源位于 `pdfs/2026-04-28/speed-accuracy-trade-off-for-diffusion-models/speed-accuracy-trade-off-for-diffusion-models.mineru/hybrid_auto/speed-accuracy-trade-off-for-diffusion-models.md`；论文 DOI 为 `10.1103/x5vj-8jq9`，digest 位于 `digests/2026-04-28/speed-accuracy-relations-for-diffusion-models.md`。
- Sagawa autoregressive thermodynamics：arXiv 页面，`https://arxiv.org/abs/2604.07867`；University of Tokyo / InaRIS 新闻，`https://www.t.u-tokyo.ac.jp/en/topics/tp2026-03-13-001`；Kyoto Hakubi 项目页面，`https://www.hakubi.kyoto-u.ac.jp/en/mem/sagawa/`。
- Dynamical regimes of diffusion models：Nature Communications 页面，`https://www.nature.com/articles/s41467-024-54281-3`。
- Forward-backward HJB matching：arXiv 页面，`https://arxiv.org/abs/2604.07762`；作者机构来自 arXiv TeX source。
- HJ-sampler：arXiv 页面，`https://arxiv.org/abs/2409.09614`；UCLA PDF，`https://ww3.math.ucla.edu/wp-content/uploads/2024/10/2409.09614v2.pdf`；Jérôme Darbon Brown profile，`https://vivo.brown.edu/display/jdarbon`；George Karniadakis Brown page，`https://www.cfm.brown.edu/faculty/gk/`。
- VI primer：Cambridge repository 页面，`https://www.repository.cam.ac.uk/items/6211012f-7fd9-4fb1-93dd-6565faef26a2`；published PDF，`https://www.repository.cam.ac.uk/bitstreams/aadef10e-1629-4456-a6af-8ad2f90e7aac/download`；Mark Girolami CHIA profile，`https://www.chia.cam.ac.uk/team/mark-girolami`。
- MVNN：arXiv 页面，`https://arxiv.org/abs/2604.00333`；Hayden Schaeffer profile，`https://sites.google.com/view/haydenschaeffer/`。
- Non-Markovian RPS：Physical Review Research 页面，`https://journals.aps.org/prresearch/abstract/10.1103/4mm1-943p`。
- Real-world robot active inference：arXiv 页面，`https://arxiv.org/abs/2512.01924`；IEEE RA-L DOI，`https://doi.org/10.1109/LRA.2025.3636032`；J-STAGE conference abstract，`https://www.jstage.jst.go.jp/article/pjsai/JSAI2025/0/JSAI2025_1B3OS41a01/_article/-char/en`。
- Statistics and Dynamics of Urban Populations：本地 PDF / MinerU 源位于 `pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations`；本次确认精读章节为 Chapter 2 与 Chapter 5-11，对应 digest 位于 `digests/2026-04-25`、`digests/2026-04-26`、`digests/2026-04-27`、`digests/2026-04-28`。
