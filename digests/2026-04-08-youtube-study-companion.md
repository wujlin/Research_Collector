# 2026-04-08 YouTube Study Companion

今天这份视频清单不是单独学习任务，而是给你读三篇论文时做“概念补强”用的。

对应顺序仍然是：

1. `PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration`
2. `Ergodicity and regime recoverability in finite Markov-modulated random walks`
3. `Disentangled Deep Priors for Bayesian Inverse Problems`

## Paper 1

### 先补随机动力学和连续极限

- `MIT OpenCourseWare | Lecture 24: Stochastic Calculus`
  https://www.youtube.com/watch?v=5cruqmIF6l0

- `Steve Brunton | Hamiltonian Neural Networks (HNN) [Physics Informed Machine Learning]`
  https://www.youtube.com/watch?v=AEOcss20nDA

你看第一篇时，最容易卡住的是：

- 随机路径和密度演化到底是什么关系
- 物理约束为什么能进入 neural loss
- “physics-informed” 到底比纯拟合多了什么

这两条视频分别补：

- `stochastic calculus / SDE` 的数学底层
- `physics-informed scientific ML` 的建模直觉

## Paper 2

### 再补非平衡、稳态与大偏差

- `Takahiro Sagawa | An introduction to stochastic thermodynamics`
  https://www.youtube.com/watch?v=m023IrSLF-k

- `Bernard Derrida | Large deviations of non-equilibrium diffusive systems`
  https://www.youtube.com/watch?v=1faKoBxBvQU

这篇论文的关键不是“random walk 很熟”，而是：

- hidden regime 如何嵌进更大的 Markov structure
- ergodicity / stationary behavior 为什么给可恢复性提供骨架
- 路径统计怎样转成分布层面的理论语言

这两条视频正好补 `nonequilibrium + large deviations + stationary structure`。

## Paper 3

### 最后补变分推断与生成先验

- `Max Welling | Improved Variational Inference with Inverse Autoregressive Flow`
  https://www.youtube.com/watch?v=OYiwWvrat3s

- `Max Welling | Variational Autoencoder (VAE) and Reparameterization Trick`
  https://www.youtube.com/watch?v=xAyuLq6W2fM

第三篇最值得你盯住的是：

- prior 到底怎样被“深度生成化”
- latent disentanglement 为什么重要
- posterior inference 为什么会自然连到 `variational free energy / Bayesian inference`

这两条视频就是最直接的补课材料。

## Optional Frontier Pair

如果你今天读完三篇还有精力，再看这两条：

- `MIT 6.S184 | Flow Matching and Diffusion Models - Score Functions`
  https://www.youtube.com/watch?v=ngC3QnYSVNM

- `Neural Policy Composition from Free Energy Minimization`
  https://www.youtube.com/watch?v=NyLFA8folLw

这两条不是为了直接解释今天的三篇论文，而是为了把你往下一步主线推进：

- `score / diffusion`
- `free energy`
- `AI for physics`

## Suggested Use

今天不要把视频当主任务。

更好的节奏是：

1. 先读论文正文和引言。
2. 卡在定义、建模假设或方法直觉时，再回来看对应视频。
3. 读完后把每篇论文各写 3 个复现问题。

真正要服务的是后面的复现路线：

`MMRW toy model -> 1D Brownian PINN -> small generative inverse problem`
