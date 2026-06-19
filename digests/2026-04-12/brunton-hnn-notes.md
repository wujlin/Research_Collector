# 2026-04-08 Brunton HNN Notes

这页笔记对应：

- `Steve Brunton | Hamiltonian Neural Networks (HNN) [Physics Informed Machine Learning]`
- https://www.youtube.com/watch?v=AEOcss20nDA

这条视频对你现在的意义，不是单独学一个 `HNN` 模型，而是把“物理结构怎样进入机器学习”这件事讲清楚。

## Core Takeaway

视频的主线可以压成一句话：

`不要让神经网络直接背轨迹，而要让它学习生成轨迹的动力学结构。`

这也是你现在从课程走向前沿最关键的一步。

## Symmetry -> Conservation -> Learning Bias

你提到视频前面回顾了一位女科学家关于 symmetry 的工作，这里大概率是在指 `Emmy Noether`。

真正重要的不是“对称性很优美”，而是：

- symmetry 对应可检验的结构约束
- 结构约束会诱导守恒量
- 守恒量可以成为学习模型的 inductive bias

放到机器学习里，意思就是：

- 不只拟合 `x(t) -> x(t + Δt)`
- 还要约束模型保留系统的 `invariance / conservation / geometry`

所以这条线不是“物理给 ML 加一点解释”，而是“物理结构决定了什么样的模型更可信”。

## Why Black-Box ODE Models Drift

Brunton 用 chaotic pendulum / nonlinear dynamics 讲的关键，不是短时预测，而是长时演化。

纯黑箱的 neural ODE 或一般回归器，即使短时拟合不错，长时间 rollout 往往会出现：

- phase drift
- energy drift
- attractor geometry 失真

也就是说，逐点误差小，不代表动力学结构学对了。

这和你后面读随机动力学论文时要记住的是同一个原则：

- `short-term fit` 不等于 `correct mechanism`

## What HNN Actually Learns

这里需要把概念说精确一点。

不是简单地“把两个微分方程和一个势能/动能 loss 丢给神经网络”，而是：

1. 先让网络学习一个标量函数 `H(q, p)`。
2. 再通过 Hamilton 方程自动生成动力学：

```text
dq/dt = ∂H/∂p
dp/dt = -∂H/∂q
```

3. 模型的预测不是任意向量场，而是受 Hamiltonian structure 约束的向量场。

这样做的效果是：

- 模型天然更接近 conservative dynamics
- 能量漂移会显著减弱
- 长时轨迹通常更稳

所以核心不是“额外加一个能量 loss”，而是“把向量场参数化方式改成结构守恒的形式”。

## Why This Matters For You

这条视频和你现在的知识结构可以这样接：

- `FTEC 5220`
  你已经在学 `ODE / SDE / Brownian motion / numerical methods`，这里补的是“结构化动力系统学习”。

- `Stat_dynamics`
  你在学 `热力学 / 统计物理 / 非平衡`，这里补的是“守恒结构怎样成为建模先验”。

- `Research_Collector`
  你后面要跟的 `PINNs / stochastic dynamics / AI for physics`，都绕不开这个思想：
  不是黑箱拟合，而是把已知结构直接写进模型。

## Connection To Your Paper Queue

它和今天三篇论文的关系不是平行的，而是一个入口。

### 对 Paper 1

`PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration`

这条视频给你的核心帮助是：

- 为什么 physics constraint 能进 loss
- 为什么只做 trajectory fitting 不够
- 为什么数值结构和学习结构最好一致

但也要看清一个差别：

- `HNN` 处理的是偏确定性的 Hamiltonian structure
- `Paper 1` 处理的是带随机性的 density evolution / Fokker-Planck constraint

所以两者共通的是“结构先验”，不是同一个数学对象。

### 对 Paper 2

`Ergodicity and regime recoverability in finite Markov-modulated random walks`

这篇更偏 `Markov structure / stationary behavior / recoverability`。

Brunton 这条视频给它的启发是：

- 结构化状态空间表示，比纯观测拟合更稳
- 真正重要的是系统生成规律，而不只是观测结果

### 对 Paper 3

`Disentangled Deep Priors for Bayesian Inverse Problems`

这条线把“物理结构先验”推进成了“生成先验 / 后验结构 / 可解释 latent representation”。

所以你可以把今天三篇论文读成这个推进链：

`Hamiltonian structure -> physics-informed constraint -> structured inference`

## The Right Abstraction

你刚才的总结里，最值得保留的是这句：

- 普通方法没有捕捉到 conservative energy 这条 pattern

但更准确的抽象应该写成：

- 黑箱模型可能拟合数据，却不保留动力学不变量
- 结构化模型通过约束参数化方式来保留系统骨架

这比“加一个能量损失”更接近 Brunton 真正想讲的东西。

## Reproduction Hint

如果你后面要做很小的复现，最自然的顺序是：

1. 普通 MLP 学 `x -> x_dot`
2. 观察长时 rollout 的 energy drift
3. 改成学习 `H(q, p)`
4. 用自动微分生成 `dq/dt` 和 `dp/dt`
5. 比较 phase portrait 和 energy conservation

这会是你后面做 `PINNs for Stochastic Dynamics` 之前非常好的热身。

## One Sentence Summary

这条视频最值得你记住的一句话是：

`机器学习真正和物理接轨，不是在输出端贴物理标签，而是在模型内部保留动力学结构。`
