---
title: "Study Guide"
digest_type: "study_guide"
date: "2026-04-08"
---

# Study Guide 2026-04-08

## Today Focus

今天的精读顺序保持为这 3 篇：

1. `PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration`
2. `Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents`
3. `Disentangled Deep Priors for Bayesian Inverse Problems`

这个顺序仍然最适合你当前的课程背景：

`随机路径 -> 密度演化 -> 随机热力学/熵产生 -> 生成先验 -> 逆问题`

## Paper 1

### PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration

- 先盯住：
  1. 它学的是轨迹、密度，还是两者都用。
  2. `Fokker-Planck residual` 是怎样进入 loss 的。
  3. Verlet 轨迹在训练里扮演的是“生成数据”还是“结构约束”。
  4. 加入 physics constraint 后，和纯拟合模型相比究竟稳在哪里。
- 课程连接：
  - `Brownian motion`
  - `Langevin dynamics`
  - `Fokker-Planck equation`
  - `SDE numerical methods`
- 配套视频：
  - `MIT OpenCourseWare | Lecture 24: Stochastic Calculus`
    https://www.youtube.com/watch?v=5cruqmIF6l0
  - `Steve Brunton | Hamiltonian Neural Networks (HNN)`
    https://www.youtube.com/watch?v=AEOcss20nDA
- 专题笔记：
  - [brunton-hnn-notes.md](/Users/jinlin/Desktop/Project/Research_Collector/youtube/notes/brunton-hnn-notes.md)

## Paper 2

### Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents

- 先盯住：
  1. 它怎样从 `correlation` 和 `trajectory-fluctuation currents` 直接学习随机热力学量。
  2. `entropy production` 在这里是被显式建模、被估计，还是被下界控制。
  3. 它和 `Fokker-Planck / path probability / reverse-time structure` 的关系是什么。
  4. 这篇里的“learning”到底是在学动力学、学热力学量，还是学两者之间的映射。
- 课程连接：
  - `stochastic thermodynamics`
  - `entropy production`
  - `trajectory fluctuations`
  - `Fokker-Planck / path-space viewpoint`
- 配套视频：
  - `Takahiro Sagawa | An introduction to stochastic thermodynamics`
    https://www.youtube.com/watch?v=m023IrSLF-k
  - `Bernard Derrida | Large deviations of non-equilibrium diffusive systems`
    https://www.youtube.com/watch?v=1faKoBxBvQU
- 专题笔记：
  - [landauer-to-generative-models.md](/Users/jinlin/Desktop/Project/Research_Collector/youtube/notes/landauer-to-generative-models.md)
- 延伸阅读：
  - 如果你后面还想补离散状态和稳态可恢复性的背景，再回头读 `Ergodicity and regime recoverability in finite Markov-modulated random walks`，把它当背景骨架，不当主阅读位。

## Paper 3

### Disentangled Deep Priors for Bayesian Inverse Problems

- 先盯住：
  1. prior 是如何被深度生成化的。
  2. disentanglement 对 inverse problem 为什么有价值。
  3. posterior inference 为什么自然连到 `variational free energy / Bayesian inference`。
  4. 它到底是在做“更好的 prior”，还是在做“更好的 inference pipeline”。
- 课程连接：
  - `Bayesian inference`
  - `variational inference`
  - `generative prior`
  - `inverse problems`
- 配套视频：
  - `Max Welling | Improved Variational Inference with Inverse Autoregressive Flow`
    https://www.youtube.com/watch?v=OYiwWvrat3s
  - `Max Welling | Variational Autoencoder (VAE) and Reparameterization Trick`
    https://www.youtube.com/watch?v=xAyuLq6W2fM

## How To Use This Guide

每篇都按同一套最小笔记模板来：

1. 这篇在解决什么问题。
2. 它依赖的数学骨架是什么。
3. 它最关键的结构假设是什么。
4. 它能不能压成一个 toy reproduction。

如果一篇文章你能写清这四件事，就说明你不是只“看过了”，而是已经把它纳入自己的研究语言里了。

## Reproduction Ladder

今天这 3 篇最合理的复现梯度是：

1. `PINNs for Stochastic Dynamics`
   从 `1D Brownian + analytic Gaussian density + Fokker-Planck residual` 开始。
2. `Learning Stochastic Thermodynamics`
   先做一个小型 trajectory-based entropy production estimation toy example，再考虑路径电流统计。
3. `Disentangled Deep Priors`
   最后再考虑做一个小型 inverse problem，用低维先验验证 inference pipeline。
