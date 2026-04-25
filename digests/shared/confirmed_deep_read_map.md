---
title: "Confirmed Deep-Read Map"
generated_at: "2026-04-24"
paper_count: 11
scope: "confirmed deep-read papers only"
---

# Confirmed Deep-Read Map

这份文档只记录 **目前已经确认精读过** 的文章，用来避免把三类东西混在一起：

1. 只是收进 `pdfs/` 的论文；
2. 建了 `digest` 但还没有真正精读的论文；
3. 已经做过逐节线性展开、公式讨论、图和逻辑反复改写的论文。

这里的标准按当前项目对话中的共同确认来定，而不是按 `pdfs/` 数量或 `digest` 数量来定。

## 一、当前已经形成的总脉络

目前真正搭起来的主线，不是“diffusion 模型总论”，而是下面这四层：

1. 生成模型可以被看成 **非平衡随机过程**，因此可以讨论不可逆性、熵产生和时间箭头。
2. 生成或采样过程可以被写成 **控制 / 势函数 / 输运问题**，因此 HJ/HJB 语言会自然进入。
3. 不完整观测下的问题本质上是 **inverse problem**，因此 posterior、VI、UQ 会自然进入。
4. 学习对象未必是单个样本，也可能是 **density、measure、path、posterior family** 这样的结构化对象。

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

### 4. Stochastic Thermodynamics for Autoregressive Generative Models

对应 digest：`2026-04-16/stochastic-thermodynamics-for-autoregressive-generative-models.md`

作者：**Takahiro Sagawa**。  
机构：论文署名来自 **Department of Applied Physics, The University of Tokyo**，并关联 **Quantum-Phase Electronics Center (QPEC), The University of Tokyo** 和 **Inamori Research Institute for Science (InaRIS)**。  
作者脉络：Sagawa 是 information thermodynamics / stochastic thermodynamics 的核心作者之一，长期研究 Maxwell demon、information processing 和 nonequilibrium thermodynamics 的关系。这篇文章把这条线从物理系统推进到 autoregressive generative models 和 LLM 序列生成。  
核心问题：entropy production 的语言能否从 diffusion 扩展到 autoregressive / non-Markov generative models。  
核心逻辑：文章为 Transformer、RNN、Kalman filter、SSM、Mamba 这类自回归生成模型建立统一的 stochastic thermodynamics 框架，定义非马尔可夫观测序列上的 entropy production，并讨论 token-level、block-level 和 retrospective decomposition。  
在整条主线里的位置：这篇把“**不可逆性不是 diffusion 专属**”这件事彻底讲清了。

## 三、diffusion 的统计物理、相变与动力学 regime

### 5. Dynamical regimes of diffusion models

对应 digest：`2026-04-11/dynamical-regimes-of-diffusion-models.md`

作者：**Giulio Biroli, Tony Bonnaire, Valentin de Bortoli, Marc Mézard**。  
机构：**Giulio Biroli** 和 **Tony Bonnaire** 来自 Laboratoire de Physique de l'Ecole Normale Supérieure, ENS / PSL / CNRS / Sorbonne Université / Université Paris Cité；**Valentin de Bortoli** 来自 ENS Computer Science Department, CNRS, PSL University；**Marc Mézard** 来自 Department of Computing Sciences, Bocconi University。  
作者脉络：这是 spin glass / disordered systems / high-dimensional statistical physics 进入 diffusion model 理论的一条强线。Biroli 和 Mézard 代表高维统计物理、玻璃态、相变和信息统计物理传统；de Bortoli 则把 score-based diffusion、采样和概率方法接入这条线。  
核心问题：在高维、大样本极限下，diffusion model 的 backward dynamics 会经历哪些不同的 dynamical regimes。  
核心逻辑：作者指出 backward dynamics 并不是单一 denoising，而会经历 `pure noise -> class-level speciation -> sample-level collapse` 三个阶段，并用高维统计物理语言解释 speciation、collapse、phase transition 和 dimension dependence。  
在整条主线里的位置：这篇和 Haiping Huang 那篇互补。前者更偏 **非平衡热力学**，这篇更偏 **相变 / regime / collapse**。

## 四、HJ / HJB / 控制 / 输运

### 6. Generative Optimal Transport via Forward-Backward HJB Matching

对应 digest：`2026-04-16/generative-optimal-transport-via-forward-backward-hjb-matching.md`

作者：**Haiqian Yang, Vishaal Krishnan, Sumit Sinha, L. Mahadevan**。  
机构：**Haiqian Yang** 来自 MIT Mechanical Engineering；**Vishaal Krishnan** 和 **Sumit Sinha** 来自 Harvard SEAS；**L. Mahadevan** 关联 Harvard SEAS、Physics 和 Organismic and Evolutionary Biology。  
作者脉络：这是 Mahadevan 体系里 mechanics、geometry、applied mathematics 和 biological / physical transport 问题相互交叉的一条线。文章把 stochastic control、optimal transport、non-equilibrium relaxation 和 HJB value function 接在一起，风格更接近物理直觉驱动的应用数学。  
核心问题：生成过程能否被改写成 forward-backward HJB matching，而不是直接学习高维控制场。  
核心逻辑：文章把 backward generative control 改写成 forward value function 学习问题，用标量势函数 $W/U$ 代替直接学习控制向量场，并通过时间反转把训练时的 forward relaxation 接回生成时的 backward control。  
在整条主线里的位置：这篇建立了“**生成 = value function / optimal control / transport**”这一层统一理解。

### 7. HJ-sampler: Bayesian Sampler via Hamilton-Jacobi PDEs and Score-Based Generative Models

对应 digest：`2026-04-16/hj-sampler.md`

作者：**Tingwei Meng, Zongren Zou, Jérôme Darbon, George Em Karniadakis**。  
机构：**Tingwei Meng** 来自 UCLA Mathematics；**Zongren Zou** 和 **Jérôme Darbon** 来自 Brown Applied Mathematics；**George Em Karniadakis** 来自 Brown Applied Mathematics，并关联 Pacific Northwest National Laboratory。  
作者脉络：**Darbon** 是 HJ PDE、optimal control、optimization 和 curse of dimensionality 这条线；**Karniadakis** 是 SciML、UQ、stochastic multiscale modeling、physics-informed learning 和 PDE-based machine learning 的核心人物之一。这里的组合使这篇文章天然处在 HJ PDE、Bayesian inference、score-based generative model 和 scientific computing 的交界处。  
核心问题：已知随机过程时，能否把 posterior path sampling 直接接到 HJ PDE 和 score-based 方法。  
核心逻辑：文章先写线性传播链，再用 log / Cole-Hopf 变换得到 HJ + density flow，然后把这个框架直接对齐到随机过程 inverse problem 里的 posterior path sampling，最后给出 Riccati-HJ-sampler 和 SGM-HJ-sampler 两条实现路线。  
在整条主线里的位置：这篇说明了“**HJ 语言不仅能解释生成控制，还能解释 posterior path sampling**”。

## 五、逆问题、VI、UQ

### 8. A Primer on Variational Inference for Physics-Informed Deep Generative Modelling

对应 digest：`2026-04-16/a-primer-on-variational-inference-for-physics-informed-deep-generative-modelling.md`

作者：**Alex Glyn-Davies, Arnaud Vadeboncoeur, O. Deniz Akyildiz, Ieva Kazlauskaite, Mark Girolami**。  
机构：**Alex Glyn-Davies, Arnaud Vadeboncoeur, Mark Girolami** 来自 University of Cambridge Department of Engineering；**O. Deniz Akyildiz** 来自 Imperial College London Department of Mathematics；**Ieva Kazlauskaite** 来自 London School of Economics Department of Statistics。  
作者脉络：这篇处在 Bayesian inverse problems、probabilistic numerics、engineering statistics 和 physics-informed deep generative modelling 的交叉处。**Mark Girolami** 是 Cambridge data-centric engineering 和 probabilistic numerics / Bayesian methodology 的代表人物，同时担任 The Alan Turing Institute Chief Scientist。  
核心问题：面对 forward solver 昂贵、观测不完整、后验难算的物理问题，VI 为什么会自然出现。  
核心逻辑：文章从 forward problem 走到 inverse problem，再从 Bayes VI 走到 generative-model VI，最后把 VAE、normalizing flow、forward-model-based learning、residual-based learning 和 deep generative prior 串成一条线。  
在整条主线里的位置：这篇建立了“**physics-informed inference 的核心不是单纯快，而是要组织 posterior、surrogate、PDE residual 和 uncertainty**”。

## 六、更一般的结构化动力学对象

### 9. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data

对应 digest：`2026-04-13/mvnn-a-measure-valued-neural-network-for-learning-mckean-vlasov-dynamics-from-particle-data.md`

作者：**Liyao Lyu, Xinyue Yu, Hayden Schaeffer**。  
机构：三位作者均来自 **Department of Mathematics, University of California, Los Angeles**。  
作者脉络：这是 UCLA applied mathematics / scientific machine learning 这条线。Hayden Schaeffer 的方向包括 scientific machine learning、PDE、inverse problems、operator learning 和 mathematical modeling；Liyao Lyu 在 Schaeffer group 中，研究位置接近 interacting particle systems 与 measure-dependent dynamics。  
核心问题：如果单粒子动力学依赖整个粒子群当前分布，能否直接从粒子轨迹学习这种 `measure-dependent drift`。  
核心逻辑：文章提出 `measure-valued neural network`，把 probability measure 当作网络输入对象，通过 cylindrical features / measure embedding 学 McKean-Vlasov dynamics，并给出 well-posedness、propagation of chaos、universal approximation 和逼近率。  
在整条主线里的位置：这篇让“**学习对象可以是 measure，而不是普通向量**”这件事变得清楚。

### 10. Non-Markovian rock-paper-scissors games

对应 digest：`2026-04-13/non-markovian-rock-paper-scissors-games.md`

作者：**Ohad Vilk, Mauro Mobilia, Michael Assaf**。  
机构：**Ohad Vilk** 和 **Michael Assaf** 来自 Racah Institute of Physics, The Hebrew University of Jerusalem；**Mauro Mobilia** 来自 Department of Applied Mathematics, School of Mathematics, University of Leeds。  
作者脉络：这是 nonequilibrium stochastic dynamics、population dynamics、large deviations 和 evolutionary game theory 的交叉线。Assaf 的工作常围绕 stochastic population dynamics 和 large-deviation rare events；Mobilia 长期研究随机演化动力学、cyclic competition 和 finite-population effects。  
核心问题：当等待时间不是指数分布时，memory 和 non-Markov 更新怎样改写经典 rock-paper-scissors 动力学。  
核心逻辑：文章表明，一旦把 Markovian exponential clock 换成具有长记忆和非指数 waiting-time 的更新过程，经典的 `law of the weakest` 不再稳固，系统的长期选择结果会被 non-Markov structure 显著改写。  
在整条主线里的位置：这篇说明了“**动力学对象一旦脱离 Markov 假设，很多经典结论都会失效**”。

### 11. Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model

对应 digest：`2026-04-16/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.md`

作者：**Kentaro Fujii, Shingo Murata**。  
机构：**School of Integrated Design Engineering, Keio University**。  
作者脉络：这是 cognitive / developmental robotics、deep active inference、world model 和 real-world robot control 的交叉线。Murata 这条线更关心 predictive coding / active inference 这类认知计算框架如何落到机器人控制；这篇文章的重点是把 expected free energy 的决策逻辑做成真实机器人可运行的层级世界模型。  
核心问题：deep active inference 为什么很少真正落到真实机器人上，以及怎样把它变成可运行的控制框架。  
核心逻辑：文章用 `slow/fast` 两层时序世界模型表示环境，再用向量量化的 `action model` 把长动作序列压成少量离散 abstract actions，最后在抽象动作空间里计算 EFE，从而把 active inference 变成真实机器人上可跑的控制方法。  
在整条主线里的位置：这篇把“**free energy / active inference / world model**”从抽象理论推进到了实际控制。

## 七、这 11 篇文章最后汇成了什么

如果把这 11 篇再压成一句更紧的总脉络，它们共同搭出的不是“某一类生成模型教程”，而是：

1. 生成过程可以被理解为 **非平衡随机过程**。
2. 这些过程的方向性可以用 **entropy production / irreversibility** 来刻画。
3. 生成或采样又可以被改写成 **HJ/HJB、control、transport、posterior sampling**。
4. 一旦观测不完整，问题自然变成 **inverse problem**，需要 posterior、VI、UQ 语言。
5. 学习对象可以是 **sample、density、measure、path、posterior family**，而不只是单个输出向量。

## 八、和当前 Synthetic_City 项目的直接关系

对 `Synthetic_City` 最有用的，不是所有 11 篇都等强，而是下面 4 条启发：

1. `VI primer` 提供主语义：你的问题本质上更像 **distribution-level amortized inverse problem**。
2. `HJB matching` 和 `HJ-sampler` 提供结构启发：不要直接学最难对象，要先换到更有结构的表示。
3. `MVNN` 提醒你：学习对象不一定是普通向量，distribution / measure 空间本身有几何结构。
4. `entropy production / irreversibility` 这条线提醒你：如果以后真的引入 dynamics，才有必要认真讨论时间箭头、耗散和控制代价；在当前 `Synthetic_City` 问题里，这些更适合作为类比和灵感，而不是主数学语义。

## 九、当前不应混入这份清单的文章

下面这些论文即使已经建了 `digest`，目前也 **不应自动算进“确认精读主线”**：

- 只是收进 `pdfs/`，还没有系统展开；
- 只建了 `digest`，但没有做过逐节线性展开和反复改写；
- 在当前对话里没有被共同确认属于“已经精读过”。

这条边界要保留，避免以后再次把“候选阅读”和“已经吃透”混在一起。

## 十、机构与作者脉络核对来源

这部分只记录用于核对作者、机构和学术脉络的来源，避免以后靠记忆补全。

- 局部电流与 entropy production：UC Davis Complexity Sciences Center 页面，`https://csc.ucdavis.edu/~cmg/compmech/pubs/currents.htm`。
- Coarse-grained entropy production：Physical Review Research 页面，`https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.023175`。
- Haiping Huang diffusion thermodynamics：Physical Review E 页面，`https://journals.aps.org/pre/abstract/10.1103/PhysRevE.111.014111`；Haiping Huang 中山大学主页，`https://spe.sysu.edu.cn/node/2338`。
- Sagawa autoregressive thermodynamics：arXiv 页面，`https://arxiv.org/abs/2604.07867`；University of Tokyo / InaRIS 新闻，`https://www.t.u-tokyo.ac.jp/en/topics/tp2026-03-13-001`；Kyoto Hakubi 项目页面，`https://www.hakubi.kyoto-u.ac.jp/en/mem/sagawa/`。
- Dynamical regimes of diffusion models：Nature Communications 页面，`https://www.nature.com/articles/s41467-024-54281-3`。
- Forward-backward HJB matching：arXiv 页面，`https://arxiv.org/abs/2604.07762`；作者机构来自 arXiv TeX source。
- HJ-sampler：arXiv 页面，`https://arxiv.org/abs/2409.09614`；UCLA PDF，`https://ww3.math.ucla.edu/wp-content/uploads/2024/10/2409.09614v2.pdf`；Jérôme Darbon Brown profile，`https://vivo.brown.edu/display/jdarbon`；George Karniadakis Brown page，`https://www.cfm.brown.edu/faculty/gk/`。
- VI primer：Cambridge repository 页面，`https://www.repository.cam.ac.uk/items/6211012f-7fd9-4fb1-93dd-6565faef26a2`；published PDF，`https://www.repository.cam.ac.uk/bitstreams/aadef10e-1629-4456-a6af-8ad2f90e7aac/download`；Mark Girolami CHIA profile，`https://www.chia.cam.ac.uk/team/mark-girolami`。
- MVNN：arXiv 页面，`https://arxiv.org/abs/2604.00333`；Hayden Schaeffer profile，`https://sites.google.com/view/haydenschaeffer/`。
- Non-Markovian RPS：Physical Review Research 页面，`https://journals.aps.org/prresearch/abstract/10.1103/4mm1-943p`。
- Real-world robot active inference：arXiv 页面，`https://arxiv.org/abs/2512.01924`；IEEE RA-L DOI，`https://doi.org/10.1109/LRA.2025.3636032`；J-STAGE conference abstract，`https://www.jstage.jst.go.jp/article/pjsai/JSAI2025/0/JSAI2025_1B3OS41a01/_article/-char/en`。
