# Frontier Follow-up Pack 2026-04-08

这份文档的目标不是记录所有新论文，而是给你一个可以持续执行的前沿跟进入口。

## Must Read 3

### 1. Ergodicity and regime recoverability in finite Markov-modulated random walks

- Venue: `Scientific Reports`
- Venue quality: `solid_domain`
- Importance: `120.8`
- Topics: stochastic_analysis/path_foundations/brownian_motion, stochastic_analysis/stochastic_dynamics/sde_theory, statistical_physics/non_equilibrium_dynamics/nonequilibrium
- Why now: 直接连接 Markov chain、master equation 和 ergodicity。
- URL: https://openalex.org/W7150102012

### 2. Efficient quantum thermal simulation

- Venue: `Nature`
- Venue quality: `top_tier`
- Importance: `100.2`
- Topics: statistical_physics/non_equilibrium_dynamics/nonequilibrium
- Why now: 属于统计物理邻域里的高质量前沿样本。
- URL: https://openalex.org/W4415196111

### 3. A Physics-Constrained Deep-Learning Framework based on Long-Term Remote-Sensing Data for Retrieving Vertical Distribution of PM <sub>2.5</sub> Chemical Components

- Venue: `Atmospheric measurement techniques`
- Venue quality: `solid_domain`
- Importance: `70.8`
- Topics: ai_for_physics/physics_informed_modeling/physics_informed_generative, urban_complex_systems/urban_data_and_generation/urban_data_science
- Why now: 能把 physics-informed 方法落到实际观测系统。
- URL: https://openalex.org/W7146945880

## Reproduction Candidates

### 1. PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration

- Venue: `International Journal of Information Technology and Computer Science`
- Topics: stochastic_analysis/path_foundations/brownian_motion, bridges/translation_layers/fokker_planck_master
- Why reproduce: 可以落成 1D Brownian + Fokker-Planck residual 的最小实现。
- URL: https://openalex.org/W7143947385

### 2. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data

- Venue: `ArXiv.org`
- Topics: stochastic_analysis/stochastic_dynamics/sde_theory, statistical_physics/non_equilibrium_dynamics/nonequilibrium, ai_for_physics/physics_informed_modeling/scientific_ml_applications
- Why reproduce: 适合做粒子系统到 mean-field 动力学的原型实验。
- URL: https://openalex.org/W7149209803

## Watchlist

- `Disentangled Deep Priors for Bayesian Inverse Problems` | ArXiv.org | preprint | 68.6
- `A hybrid bio-inspired model for predicting urban air pollution using deep learning` | Scientific Reports | solid_domain | 60.8
- `Non-Markovian Entropy Dynamics in Living Systems from the Keldysh Formalism` | ArXiv.org | preprint | 60.4
- `Thermalization in high-dimensional systems: the (weak) role of chaos` | arXiv (Cornell University) | unranked | 54.6
- `The Tracy-Widom Distribution at Large Dyson Index` | Journal of Statistical Physics | high_quality | 54.4

## Operating Rhythm

每篇论文建议都按同一个模板处理：

1. 写下它解决的核心问题。
2. 写下它依赖的数学骨架或物理假设。
3. 写下你能否把它压成一个 toy reproduction。

如果一篇文章同时满足“理论骨架清楚 + toy model 可搭 + 和主线相连”，它就应该优先进入复现队列。
