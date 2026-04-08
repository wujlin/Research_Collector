# 2026-04-08 Recent High-Quality Shortlist

这份清单是从今天采到的近期论文里筛出来的“优先看”集合。

筛选标准不是只看一个指标，而是同时看：

- `venue quality`
- `和当前主线的贴合度`
- `是否能服务后续复现`

## Tier A: 现在最值得看

### 1. Ergodicity and regime recoverability in finite Markov-modulated random walks

- Venue: `Scientific Reports`
- Venue quality: `solid_domain`
- Why keep:
  直接连接 `Markov chain / master equation / ergodicity / hidden regime inference`，和你现在的随机分析、非平衡统计物理主线贴合得最好。

### 2. Disentangled Deep Priors for Bayesian Inverse Problems

- Venue: `arXiv`
- Venue quality: `preprint`
- Why keep:
  虽然不是正式期刊，但它和 `AI for Physics / inverse problems / generative prior / Bayesian inference` 的连接最强，研究价值很高。

### 3. MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data

- Venue: `arXiv`
- Venue quality: `preprint`
- Why keep:
  这是这轮里被 taxonomy 修正后救回来的重点文献，和 `随机动力学 + mean-field / McKean-Vlasov + scientific ML` 很贴。

### 4. Uniform-in-time diffusion approximations for multiscale stochastic systems

- Venue: `arXiv`
- Venue quality: `preprint`
- Why keep:
  这篇偏数学骨架，适合接你已有的 `SDE / diffusion approximation / Fokker-Planck` 课程背景。

## Tier B: 高质量 venue，建议跟进

### 5. Efficient quantum thermal simulation

- Venue: `Nature`
- Venue quality: `top_tier`
- Why keep:
  venue 很强，主题也在热模拟和统计物理邻域内。它不是你当前最直接的复现对象，但值得作为“高质量前沿样本”追踪。

### 6. The Tracy-Widom Distribution at Large Dyson Index

- Venue: `Journal of Statistical Physics`
- Venue quality: `high_quality`
- Why keep:
  这是更偏理论统计物理/随机矩阵的一篇，方法质量不错，适合作为高质量数学-物理邻域文献保留。

### 7. Boundary layers, transport and universal distribution in boundary driven active systems

- Venue: `SciPost Physics`
- Venue quality: `solid_domain`
- Why keep:
  非平衡、边界驱动、active systems，这类题目和你之后想往非平衡统计物理推进是对路的。

## Tier C: 可读，但不以 venue 见长

### 8. PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration

- Venue: `International Journal of Information Technology and Computer Science`
- Venue quality: `unranked`
- Why keep:
  不是因为 venue，而是因为它对你现在的课程衔接最直接，能帮你把 `Brownian motion / Langevin / Fokker-Planck / PINN` 串起来。

### 9. A Physics-Constrained Deep-Learning Framework ... PM2.5 ...

- Venue: `Atmospheric Measurement Techniques`
- Venue quality: `solid_domain`
- Why keep:
  这是应用侧样本，适合你以后把 `physics-informed` 框架往城市复杂系统/城市环境数据里落。

## 暂不优先

下面这些暂时留库，但不建议先读：

- `Thermalization in high-dimensional systems: the (weak) role of chaos`
- `Non-Markovian Entropy Dynamics in Living Systems from the Keldysh Formalism`
- `Chaos and Parrondo’s paradox: an overview`
- `Diffusion models with physics-guided inference for solving partial differential equations`

它们不是不好，而是当前优先级低于前面的 `Tier A / Tier B`。

## 建议阅读顺序

如果只从今天这批里往下推进，我建议：

1. `Ergodicity and regime recoverability in finite Markov-modulated random walks`
2. `Disentangled Deep Priors for Bayesian Inverse Problems`
3. `MVNN: A Measure-Valued Neural Network for Learning McKean-Vlasov Dynamics from Particle Data`
4. `Uniform-in-time diffusion approximations for multiscale stochastic systems`
5. `Efficient quantum thermal simulation`

如果你想兼顾“课程衔接”，就把 `PINNs for Stochastic Dynamics...` 插到第 2 位。
