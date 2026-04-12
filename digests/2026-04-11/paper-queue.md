---
title: "Paper Queue"
digest_type: "paper_queue"
date: "2026-04-11"
---

# Paper Queue 2026-04-11

这份文档是今天的论文筛选入口。原则只保留三类内容：

- 主线直接相关
- venue 和作者背景都相对可信
- 即使是 preprint，也必须有明确理论抓手

今天把 `Non-Markovian Entropy Dynamics in Living Systems from the Keldysh Formalism` 移出核心阅读位。原因不是题目不有趣，而是目前它只是 `arXiv` 预印本，作者团队和机构背景都不够强，不适合作为你当前主线的支撑文献。

## Must Read

### 1. Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents

- Venue: `arXiv`
- Venue quality: `preprint`
- Venue reputation: `cautious_but_high_fit`
- Why now: 和你现在正在读的 `Sagawa -> entropy production -> Fokker-Planck -> trajectory current -> diffusion / score` 主线贴得最紧。
- Core value: 把随机热力学推断改写成 `self-supervised function learning`，是你当前最值得吃透的桥接文章。
- URL: https://arxiv.org/abs/2504.19007

### 2. Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility

- Venue: `Physical Review Research`
- Venue quality: `strong_domain`
- Venue reputation: `trusted`
- Authors / institutions: `Julius Degünther, Jann van der Meer, Udo Seifert | University of Stuttgart`
- Published: `2024-05-16`
- Why now: 它直接讨论 `coarse-grained irreversibility` 和 `entropy production inference`，比量子输运里的 FDR bound 更贴近你现在的随机热力学主线。
- Core value: 强作者线、问题清楚，而且正好补你现在正在想的“有限观测下如何定位不可逆性”。
- URL: https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.023175

### 3. Dynamical regimes of diffusion models

- Venue: `Nature Communications`
- Venue quality: `top_tier_multidisciplinary`
- Venue reputation: `trusted`
- Authors / institutions: `Giulio Biroli, Tony Bonnaire, Valentin de Bortoli, Marc Mézard | ENS Paris, PSL, Bocconi`
- Published: `2024-11-17`
- Why now: 这是目前最适合补进你 `AI for physics` 线的高质量替代，不是应用堆砌，而是用统计物理直接分析 diffusion model 的动力学结构。
- Core value: 把 `speciation / collapse / phase transition / curse of dimensionality` 放进 diffusion model 的理论理解里。
- URL: https://www.nature.com/articles/s41467-024-54281-3

## Strong Follow-Up

### 1. Entropy production and thermodynamic inference for stochastic microswimmers

- Venue: `Physical Review Research`
- Venue quality: `strong_domain`
- Venue reputation: `trusted`
- Authors / institutions: `Michalis Chatzittofi, Jaime Agudo-Canalejo, Ramin Golestanian | Max Planck MPI-DS, UCL, Oxford`
- Published: `2024-05-21`
- Why follow: 直接做 `entropy production + thermodynamic inference + precision-dissipation tradeoff`，而且作者背景明显强于昨天那篇生命系统预印本。
- URL: https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.L022044

### 2. Out-of-Equilibrium Fluctuation-Dissipation Bounds

- Venue: `Physical Review Letters`
- Venue quality: `top_tier_domain`
- Venue reputation: `trusted`
- Authors / institutions: `Ludovico Tesser, Janine Splettstoesser | Chalmers University of Technology`
- Published: `2024-05-03`
- Why follow: 质量很高，但更偏量子输运和 mesoscopic conductor；可以保留作 `FDR` 的强样本，不必现在硬读。
- URL: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.186304

### 3. Generative learning for forecasting the dynamics of high-dimensional complex systems

- Venue: `Nature Communications`
- Venue quality: `top_tier_multidisciplinary`
- Venue reputation: `trusted`
- Authors / institutions: `Han Gao, Sebastian Kaltenbach, Petros Koumoutsakos | Harvard`
- Published: `2024-10-16`
- Why follow: 更贴近 `complex systems` 和你后面的城市系统兴趣，适合放在 `AI for complex dynamics` 分支。
- URL: https://www.nature.com/articles/s41467-024-53165-w

### 4. Synthetic Lagrangian turbulence by generative diffusion models

- Venue: `Nature Machine Intelligence`
- Venue quality: `top_tier_ml`
- Venue reputation: `trusted`
- Published: `2024-04-17`
- Why follow: 是 `diffusion models -> fluid / turbulence physics` 的代表性应用，适合做 AI for physics 的案例样本。
- URL: https://www.nature.com/articles/s42256-024-00810-0

### 5. Jensen bound for the entropy production rate in stochastic thermodynamics

- Venue: `Physical Review E`
- Venue quality: `strong_domain`
- Venue reputation: `trusted`
- Authors / institutions: `Matthew P. Leighton, David A. Sivak | Simon Fraser University`
- Published: `2024-01-04`
- Why follow: 和你现在在读的 `entropy production inference` 直接相关，而且讨论了位置依赖扩散、underdamped 等扩展情形。
- URL: https://journals.aps.org/pre/abstract/10.1103/PhysRevE.109.L012101

## Horizon Sample

### Efficient quantum thermal simulation

- Venue: `Nature`
- Venue quality: `top_tier`
- Venue reputation: `trusted`
- Why not now: 文章质量高，但量子前置要求高，暂时不适合进入你的核心精读位。
- URL: https://www.nature.com/articles/s41586-025-09583-x

## Dropped Today

### Non-Markovian Entropy Dynamics in Living Systems from the Keldysh Formalism

- Status: `removed_from_core_queue`
- Reason: `preprint + weaker institution line + author background mismatch with current claim strength`
- Action: 保留概念印象，不作为当前主线的理论支撑。
- URL: https://arxiv.org/abs/2603.12184

## Reading Order

今天之后，主线更合理的顺序是：

1. `Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents`
2. `Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility`
3. `Dynamical regimes of diffusion models`

如果要开新的支线，再从这两篇里选：

- `Entropy production and thermodynamic inference for stochastic microswimmers`
- `Generative learning for forecasting the dynamics of high-dimensional complex systems`
