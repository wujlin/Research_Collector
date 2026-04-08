# 2026-04-08 Three-Paper Study Guide

今天先读这 3 篇，顺序不要乱：

1. `PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration`
2. `Ergodicity and regime recoverability in finite Markov-modulated random walks`
3. `Disentangled Deep Priors for Bayesian Inverse Problems`

这样读的逻辑是：

- 先从你课程里最熟的 `Brownian motion / Langevin / Fokker-Planck` 出发
- 再转到 `Markov chain / master equation / ergodicity / hidden regime`
- 最后再接到 `generative prior / Bayesian inverse problem / scientific ML`

也就是：

`随机路径 -> 密度演化 -> 稳态/可恢复性 -> 生成先验 -> 逆问题`

## Paper 1

### PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration

这篇最适合拿来把你在 `FTEC 5220` 和 `Stat_dynamics` 里学的内容直接接上前沿。

你读它时要盯住 4 个点：

1. 论文到底在学什么对象？
   是轨迹，还是概率密度，还是两者都在用。

2. 物理约束是怎么进 loss 的？
   它不是一般 PINN，而是把 `Fokker-Planck`、边界条件和概率守恒一起放进训练。

3. Verlet 轨迹在这里扮演什么角色？
   它不是最终目标，而是给 PINN 提供高保真轨迹数据。

4. 它为什么比纯 data-driven operator learner 更稳？
   这个问题关系到后面你做复现时，为什么要保留 physics constraint。

这篇和你课程最直接的对应关系：

- `Brownian motion`
- `Langevin dynamics`
- `Fokker-Planck equation`
- `probability conservation`
- `SDE numerical simulation`

后续复现可以先做一个最小版：

- 1D Brownian motion
- analytic Gaussian density
- Euler-Maruyama vs Verlet trajectory data
- 用一个小 PINN 去拟合 density
- 比较是否加入 `Fokker-Planck residual` 的差别

## Paper 2

### Ergodicity and regime recoverability in finite Markov-modulated random walks

这篇是“随机分析 + 非平衡统计物理 + 可学习性”之间非常好的桥。

你读这篇时要看：

1. `Z_t = (X_t, E_t)` 这个 joint process 为什么重要？
   因为它把“可观测位置”和“隐藏环境状态”绑成一个更大的 Markov 链。

2. master equation 在这里的角色是什么？
   它不只是形式化写法，而是把路径更新翻译成分布更新的入口。

3. ergodicity / stationary distribution 在文中是理论保证还是学习前提？
   这个要分清。

4. supervised learning 预测隐藏 regime 时，真正被学到的是什么？
   是短时路径统计、稳态偏差，还是转移结构。

这篇最值得你用来巩固的课程概念：

- finite-state Markov chain
- stationary distribution
- irreducibility / aperiodicity
- master equation
- ergodicity

如果后面做复现，这篇很适合：

- 自己先搭一个两状态 hidden regime random walk
- 模拟轨迹
- 写出经验转移矩阵和经验稳态分布
- 再做一个简单分类器去恢复 hidden regime

这样复现成本很低，但研究味道很足。

## Paper 3

### Disentangled Deep Priors for Bayesian Inverse Problems

这篇是把你现在“随机过程 / 统计物理”往 `AI for Physics` 推进的关键一步。

这篇的核心不是 diffusion，而是：

- deep generative prior
- latent disentanglement
- Bayesian inverse problem
- MAP / MCMC

你读它时要盯住：

1. prior 是怎么构造的？
   它不是普通 Gaussian prior，而是 `disentangled deep generative prior`。

2. latent space 为什么要拆成 interpretable 和 residual 两块？
   这关系到“物理可解释参数”和“剩余不确定性”能不能分离。

3. posterior 的 block structure 是怎么来的？
   这个地方其实很值得你用线性化近似去推一下。

4. 为什么 inverse problem 会自然把这篇拉向你关心的 free-energy / variational 语言？
   因为 posterior inference、representation 和 uncertainty decomposition 本来就和那条线相通。

这篇和你当前知识连接最强的点：

- Bayesian inference
- inverse problems
- uncertainty decomposition
- generative prior
- scientific ML

后续复现可以从非常小的 PDE inverse problem 入手：

- 1D elliptic equation
- source / conductivity identification
- 一个小型 autoencoder 或 latent prior
- MAP 与 MCMC 的对比

## How To Read Them Together

今天不要把 3 篇当成 3 个平行阅读任务。

正确读法是：

1. 从 `Paper 1` 建立“轨迹 -> density -> Fokker-Planck -> physics-informed learning”的直觉。
2. 用 `Paper 2` 建立“Markov / master equation / ergodicity / hidden regime inference”的离散版桥梁。
3. 最后用 `Paper 3` 把这些东西推进到“inverse problem / latent prior / generative inference”。

如果你今天只记住 3 句话，应该是：

- `Fokker-Planck` 是随机动力学和学习模型之间的翻译层。
- `ergodicity / stationary structure` 是很多可学习性结论背后的稳定骨架。
- `deep generative prior` 不是偏离物理，而是在 inverse problem 中重写先验和不确定性。

## Reproduction Ladder

后面如果要做论文复现，我建议按难度从低到高：

1. `Paper 2`
   原因：最容易自己写出一个干净 toy model。

2. `Paper 1`
   原因：可以做一个 1D 最小 PINN 版本，计算成本也可控。

3. `Paper 3`
   原因：最有研究潜力，但也最容易因为建模细节和采样细节失控。

所以真正的项目起步顺序应该是：

`MMRW toy model -> 1D Brownian PINN -> small inverse-problem generative prior`
