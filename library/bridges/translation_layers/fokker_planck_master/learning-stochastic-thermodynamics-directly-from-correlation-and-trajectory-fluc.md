---
title: "Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents"
authors: ["Justin Sirignano", "Andrea Dechant", "others"]
year: 2025
journal: "arXiv"
doi: ""
arxiv: ""
url: "https://arxiv.org/abs/2504.19007"
pdf_url: ""
topics: ["bridges/translation_layers/fokker_planck_master", "statistical_physics", "statistical_physics/non_equilibrium_dynamics/nonequilibrium", "ai_for_physics", "ai_for_physics/generative_dynamics/sde_generative", "bridges", "bridges/thermodynamic_inference/info_geometry", "statistical_physics/non_equilibrium_dynamics", "ai_for_physics/generative_dynamics", "bridges/translation_layers", "bridges/thermodynamic_inference", "bridges/thermodynamic_inference/variational_free_energy"]
tier: 0
citations: 0
relevance_score: 0
collected: "2026-04-07"
status: "unread"
source: ""
is_seminal: true
---

## Abstract

(待填充)

## Key Contributions

- Recasts stochastic-thermodynamic inference as a self-supervised function-learning problem built directly from short-time trajectory observables.
- Constructs observable losses that recover four local quantities: drift, probability velocity, temporal score, and diffusion field.
- Places TUR-style lower-bound estimation and MSE-style regression in one short-time variational framework.
- Extends the inference logic beyond steady state by separating the flow term and the explicit time-dependent density term in entropy production.
- Introduces higher-order inference to reduce finite-$\Delta t$ bias in local quantity recovery.

## Connections

- [[fokker_planck_master]]
- [[statistical_physics]]
- [[nonequilibrium]]
- [[ai_for_physics]]
- [[sde_generative]]
- [[bridges]]
- [[info_geometry]]
- [[non_equilibrium_dynamics]]
- [[generative_dynamics]]
- [[translation_layers]]
- [[thermodynamic_inference]]
- [[variational_free_energy]]

## Notes

### Reading Frame

这篇的核心不是具体神经网络结构，而是统一推导模式：

`目标热力学函数不可直接观测 -> 从短时动力学构造可观测 loss -> loss 的极小值等价于目标函数`

后面的 `drift`、`probability velocity u`、`temporal score` 和 `diffusion field` 都沿用这条骨架。

### Problem

这篇要解决的问题是：在没有逐点标签、没有显式概率密度、也不依赖外加响应实验的情况下，能不能只用短时间轨迹数据本身，直接恢复随机热力学中的关键局域量，尤其是与 entropy production 直接相关的对象。

更具体地说，它要同时跨过三道障碍：

- `entropy production` 不是直接可观测量，通常只能从轨迹统计间接推断
- 传统 `TUR` 更擅长给 `lower bound`，不直接恢复局域函数场
- 一旦离开 `NESS`，只恢复流动项还不够，还必须补上分布显式随时间变化的那一项

因此这篇真正解决的不是“再设计一个神经网络”，而是“怎样把随机热力学量的推断写成一个由轨迹涨落驱动的可学习问题”。

### Main Contribution

这篇的主要贡献可以压成五点。

1. 它把随机热力学推断改写成了 `self-supervised function learning`。训练信号不来自标签，而来自短时增量、Stratonovich current 和相邻时间步的统计关系。
2. 它用同一套构造模板恢复四个局域对象：`drift`、`probability velocity u`、`temporal score` 和 `diffusion field`。这样 entropy production 不再是一个黑箱标量，而是被拆成可学习的组成部分。
3. 它把 `TUR/cosine` 型估计和 `L2/MSE` 型回归放进了同一个短时间变分框架里，说明前者更像方向匹配，后者更自然地支持函数回归。
4. 它把框架从 `NESS` 推广到非稳态情形，通过显式引入 `temporal score` 处理 \(\partial_t \log f\) 这一项。
5. 它进一步引入 `higher-order inference`，通过多步增量组合压低有限 \(\Delta t\) 带来的系统偏差。

### 四个目标量：定义与物理图像

先区分 Table I 里的四个目标量。它们对应平均动力学、不可逆概率流、分布时间变化和噪声强度。

#### 1. Drift

文中用 `force`，在 overdamped 情形里更准确的说法是 `drift`：

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

它表示系统在局域位置 `x` 和时刻 `t` 的平均运动方向与速度。没有噪声时，它就是确定性推力；有噪声时，它仍然决定平均运动方向。

#### 2. Probability Velocity \(u\) / Local EP

本文学习的不是局域熵产生标量本身，而是 `probability velocity`

$$
u(x,t) = \Phi(x,t) - D\,\partial_x \log f(x,t)
$$

它把 drift 和分布梯度修正合在一起，描述不可逆概率流。平均熵产生率满足

$$
\dot{\Sigma} \propto \frac{1}{D}\,\mathbb{E}[u(x,t)^2]
$$

所以 `u` 是本文用来表征 local EP 的核心局域场。

#### 3. Temporal Score

$$
\partial_t \log f(x,t)
$$

它表示在固定位置 `x` 上，概率密度 `f(x,t)` 随时间变化得有多快。在 `NESS` 下这一项消失；离开稳态后，它负责补上分布显式改写带来的熵产生贡献。

#### 4. Diffusion Field

在最简单的 overdamped 情形里，

$$
D = \frac{1}{2}\sigma^2
$$

如果系统非均匀，也可以推广成位置相关的 `D(x,t)`。它不决定平均往哪走，而决定轨迹抖动强度和分布扩散速度。

四个对象的层次关系是：

- `drift`：平均动力学
- `probability velocity u`：不可逆概率流
- `temporal score`：分布时间变化
- `diffusion field`：噪声强度

### Loss Functions in Overdamped Dynamics：总览

在 overdamped dynamics 里，paper 的统一起点是

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

对应的学习任务不是只恢复一个 drift，而是同时恢复四个局域对象：

- `drift` $\Phi(x,t)$
- `probability velocity` $u(x,t)$
- `temporal score` $\partial_t \log f(x,t)$
- `diffusion field` $\sigma^2$ 或等价的 $D=\sigma^2/2$

这四类 loss 的逻辑顺序可以统一写成：

1. 先选定一个目标函数 $G(x,t)$。
2. 找到一个可从短时间轨迹估计的量，使它的期望或相关项与 $G$ 成线性关系。
3. 写出

$$
\mathcal{L}_G(w)
=
\mathbb{E}\!\left[
\frac{1}{2}w^2\,dt - w \cdot (\text{observable})
\right]
$$

或与之等价的离散版本。

4. 把该可观测量的期望代回去。
5. 通过配方恢复成

$$
\mathcal{L}_G(w)
=
dt\,\mathbb{E}\!\left[\frac{1}{2}(w-G)^2\right] + \text{const}
$$

于是最优解满足

$$
\arg\min_w \mathcal{L}_G(w)=G.
$$

在 overdamped 情形里，四类目标函数对应的可观测量分别是：

- 对 `drift`，可观测量是一阶增量 `dx` 或离散增量 `\Delta x`
- 对 `probability velocity u`，可观测量是 `Stratonovich current`，因为它同时带入一阶漂移项和二阶扩散修正
- 对 `temporal score`，可观测量是测试函数期望在相邻时间步的变化
- 对 `diffusion field`，可观测量是二阶增量 `(dx)^2` 或 `(\Delta x)^2`

后面的四个小节就是把这张总图逐项展开。

### Force Loss：从轨迹增量恢复 Drift

观测量是轨迹点与短时增量，目标量是 drift $\Phi(x,t)$，但轨迹上没有逐点标签。起点是 overdamped Langevin：

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

离散到短时间步：

$$
\Delta x = \Phi(x,t)\,\Delta t + \sigma\,\Delta W
$$

由于噪声均值为零：

$$
\mathbb{E}[\Delta x \mid x] = \Phi(x,t)\,\Delta t
$$

核心输入是：短时增量的条件期望给出局域 drift 的方向与大小。

令神经网络 $w(x)$ 近似 $\Phi(x,t)$。对应的 first-order force loss 为：

$$
\mathcal{L}_{\mathrm{force}}(w)
=
\mathbb{E}\!\left[
\frac{1}{2} w(x)^2 \Delta t - w(x)\,\Delta x
\right]
$$

代入条件期望后：

$$
\mathcal{L}_{\mathrm{force}}(w)
=
\Delta t\,
\mathbb{E}\!\left[
\frac{1}{2} w^2 - w\Phi
\right]
$$

再配方：

$$
\frac{1}{2} w^2 - w\Phi
=
\frac{1}{2}(w-\Phi)^2 - \frac{1}{2}\Phi^2
$$

于是：

$$
\mathcal{L}_{\mathrm{force}}(w)
=
\Delta t\,
\mathbb{E}\!\left[
\frac{1}{2}(w-\Phi)^2
\right]
 + \text{const}
$$

因此：

$$
\arg\min_w \mathcal{L}_{\mathrm{force}}(w)
=
\arg\min_w \mathbb{E}\!\left[(w-\Phi)^2\right]
$$

因此 `force loss` 只依赖可观测量，但其极小值与真实 drift 的 MSE 目标等价。

### 与 Reverse Diffusion / Score Matching 的结构对应

结构相似点在于：

- 没有直接标签
- 已知前向随机动力学
- 从动力学构造替代训练信号
- 学习一个局域函数场

区别在于目标函数不同：

- reverse diffusion 学的是 reverse drift / score，用于生成
- 这篇学的是 `drift`、`probability velocity u`、`temporal score` 和 `diffusion field`，用于推断

### Table I 的统一模板

Table I 里的多条 loss 共享同一模板：

1. 先找一个可观测短时量，比如 `Δx`、Stratonovich current、`Δw`
2. 证明它的期望和目标函数之间有线性关系
3. 写成 `1/2 w^2 - w * observable` 这种 loss
4. 配方后恢复成与目标函数的 MSE 等价

对应到具体对象：

- `force loss` 恢复 drift
- `local EP loss` 恢复 probability velocity
- `temporal score loss` 恢复分布时间变化项

### Local EP Loss：为什么要用 Stratonovich Current

`local EP loss` 的目标量不是 drift $\Phi(x,t)$，而是 probability velocity

$$
u(x,t) = \Phi(x,t) - D\,\partial_x \log f(x,t)
$$

平均熵产生率与它满足

$$
\dot{\Sigma} \propto \frac{1}{D}\,\mathbb{E}[u(x,t)^2]
$$

问题变成：怎样从轨迹数据恢复 $u$，而不只是恢复 drift $\Phi$。

#### 先把对象说清楚

这一段里最容易混的是三个函数：

- $f(x,t)$：系统在时刻 $t$ 的概率密度，不是测试函数
- $u(x,t)$：目标函数，也就是 probability velocity
- $w(x)$：测试函数或待学习函数

这里的期望符号就是按 $f(x,t)$ 加权：

$$
\mathbb{E}[g(x_t)] = \int dx\, f(x,t)\,g(x)
$$

所以式子里出现 $f(x,t)$，只是因为作者在写“总体损失”或“总体期望”；真正拿来优化的函数是 $w(x)$，不是 $f(x,t)$。

#### 为什么总体 loss 写成这个形式

目标是让最优解满足

$$
u = \arg\min_w \mathcal{L}_u(w)
$$

最直接的想法就是对 $u$ 做 `L2` 回归：

$$
\mathcal{L}_u(w)
=
dt\,\mathbb{E}\!\left[\frac{1}{2}(w-u)^2\right]
$$

把平方展开：

$$
\mathcal{L}_u(w)
=
dt\,\mathbb{E}\!\left[\frac{1}{2}w^2 - wu + \frac{1}{2}u^2\right]
$$

最后一项 $\frac{1}{2}\mathbb{E}[u^2]dt$ 与 $w$ 无关，所以优化时可以丢掉，于是得到

$$
\mathcal{L}_u(w)
=
dt\int dx\,f(x,t)\left[\frac{1}{2}w(x)^2 - w(x)u(x,t)\right]
$$

因此式 (19) 不是凭空定义的，它就是“对目标函数 $u$ 做 MSE 回归”去掉常数项之后的总体风险。

#### 式 (20) 的线性展开

真正的困难不在第一项 $\frac{1}{2}w^2$，而在交叉项

$$
\mathbb{E}[w\,u\,dt]
$$

因为 $u(x,t)$ 里含有未知的密度梯度：

$$
u(x,t)
=
\Phi(x,t) - \frac{1}{2}\sigma^2 \frac{\partial_x f(x,t)}{f(x,t)}
$$

把它代回期望：

$$
\mathbb{E}[w\,u\,dt]
=
dt\int dx\, f(x,t)\,w(x)
\left[
\Phi(x,t) - \frac{1}{2}\sigma^2 \frac{\partial_x f(x,t)}{f(x,t)}
\right]
$$

把第二项中的 $f$ 约掉：

$$
\mathbb{E}[w\,u\,dt]
=
dt\int dx\,
\left[
f(x,t)w(x)\Phi(x,t)
- \frac{1}{2}\sigma^2 w(x)\partial_x f(x,t)
\right]
$$

接下来对第二项分部积分。假设边界项消失：

$$
-\int dx\, w\,\partial_x f
=
\int dx\, f\,\partial_x w
$$

于是

$$
\mathbb{E}[w\,u\,dt]
=
dt\int dx\, f(x,t)
\left[
w(x)\Phi(x,t) + \frac{1}{2}\sigma^2 \partial_x w(x)
\right]
$$

写成期望就是

$$
\mathbb{E}[w\,u\,dt]
=
\mathbb{E}[w(x)\Phi(x,t)\,dt]
+
\mathbb{E}\!\left[\frac{1}{2}\sigma^2 \partial_x w(x)\,dt\right]
$$

第一项再用 It\^o 形式的 SDE

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

改写成增量。因为噪声项的条件期望为零：

$$
\mathbb{E}[w(x)\,dx]
=
\mathbb{E}[w(x)\Phi(x,t)\,dt]
$$

所以

$$
\mathbb{E}[w\,u\,dt]
=
\mathbb{E}[w(x)\,dx]
+
\mathbb{E}\!\left[\frac{1}{2}\sigma^2 \partial_x w(x)\,dt\right]
$$

最后一步使用 It\^o 和 Stratonovich 的换算：

$$
w(x)\circ dx
=
w(x)\,dx + \frac{1}{2}\sigma^2 \partial_x w(x)\,dt
$$

取期望后得到

$$
\mathbb{E}[w\,u\,dt] = \mathbb{E}[w(x)\circ dx]
$$

这就是式 (20) 的核心。它把原来显式依赖密度梯度 $\partial_x f$ 的相关项，改写成了可以直接从轨迹增量估计的 `Stratonovich current`。

#### 式 (21) 为什么变成中点离散

在一个很小的时间步 $[t,t+\Delta t]$ 上，Stratonovich 积分用中点规则离散：

$$
\int_t^{t+\Delta t} w(X_s)\circ dX_s
\approx
\frac{1}{2}\big[w(x_t)+w(x_{t+\Delta t})\big]\,(x_{t+\Delta t}-x_t)
$$

记

$$
\Delta x = x(t+\Delta t)-x(t)
$$

就得到经验 loss

$$
\hat{\mathcal{L}}^{(1)}_u
=
\left\langle
\frac{1}{2}w(x)^2\Delta t
- \frac{1}{2}[w(x)+w(x+\Delta x)]\Delta x
\right\rangle
$$

这正是式 (21)。第一项对应总体风险里的 $\frac{1}{2}w^2dt$，第二项对应用离散 Stratonovich current 替代的 $\mathbb{E}[w\,u\,dt]$。

对应的总体 loss 满足

$$
\arg\min_w \mathcal{L}_{u}(w) = u(x,t)
$$

在无限数据和无穷小时间步极限下，离散 loss 的极小点收敛到同一个目标函数；有限数据和有限 $\Delta t$ 时，得到的是对 $u(x,t)$ 的近似估计。

这里论文里说 “the loss function is only correct up to $O(\Delta t)$” 的意思是：

- 连续时间极限下，目标函数确实是 $u(x,t)$；
- 但离散时间 loss $\hat{\mathcal L}^{(1)}_u$ 只保留了关于 $\Delta t$ 的一阶项；
- 被截断掉的高阶项会带来量级为 $O(\Delta t)$ 的系统偏差。

所以有限步长时，离散 loss 的极小点不是精确的 $u(x,t)$，而是一阶估计

$$
u^{(1)}(x) = u(x) + O(\Delta t).
$$

论文后面提到的 `higher-order inference`，就是继续把这些被忽略的高阶项补回来，从而把一阶估计 $u^{(1)}(x)$ 修正得更接近真实的 $u(x,t)$。

#### 为什么 \(2\Delta x - \tfrac{1}{2}\Delta_2 x\) 能消掉二阶偏差

这里最需要先分清的是记号：$\Delta_2 x$ 不是 $(\Delta x)^2$，而是跨两个时间步的增量

$$
\Delta x := x(t+\Delta t)-x(t),\qquad
\Delta_2 x := x(t+2\Delta t)-x(t).
$$

设 $h=\Delta t$。单步条件期望的短时展开一般写成

$$
\mathbb{E}[\Delta x \mid x_t=x]
=
\Phi(x,t)\,h + a(x,t)\,h^2 + O(h^3),
$$

其中 $a(x,t)$ 代表所有二阶修正项。把时间步长换成 $2h$，则有

$$
\mathbb{E}[\Delta_2 x \mid x_t=x]
=
2\Phi(x,t)\,h + 4a(x,t)\,h^2 + O(h^3).
$$

现在构造作者使用的组合：

$$
2\,\mathbb{E}[\Delta x \mid x_t=x]
- \frac{1}{2}\,\mathbb{E}[\Delta_2 x \mid x_t=x].
$$

代入展开式后得到

$$
2(\Phi h + ah^2 + O(h^3))
- \frac{1}{2}(2\Phi h + 4ah^2 + O(h^3))
=
\Phi h + O(h^3).
$$

所以这里不是把二次无穷小“直接删掉”，而是利用两个不同步长的增量组合，把 $O(h^2)$ 偏差精确抵消掉。这正是 `higher-order inference` 的核心。

如果 paper 的右边写成

$$
\Phi(x,t)f(x,t)\,\Delta t + O(\Delta t^3),
$$

多出来的 $f(x,t)$ 一般是因为作者写的是局域化后的无条件期望，例如乘了一个定位因子 $\delta(x_t-x)$。这时

$$
\mathbb{E}[\delta(x_t-x)] = f(x,t),
$$

于是会得到

$$
\mathbb{E}\!\left[\left(2\Delta x-\frac{1}{2}\Delta_2 x\right)\delta(x_t-x)\right]
=
\Phi(x,t)f(x,t)\,\Delta t + O(\Delta t^3).
$$

因此这一步的作用可以直接记成：一阶估计给的是 $\Phi\,\Delta t + O(\Delta t^2)$，而两步组合把偏差再压低一阶，提升到 $\Phi\,\Delta t + O(\Delta t^3)$。

到这一步为止，恢复的仍然只是轨迹级随机熵产生中的流动项。对于 `NESS`，由于 $\partial_t \log f = 0$，这一项已经足够；离开稳态后，还必须补上显式记录分布时间变化的 temporal score。

### Temporal Score：角色与对应 Loss

文中轨迹级 stochastic entropy production 写成：

$$
\sigma_{\Gamma}
=
\int_{\Gamma}
\left[
u(x,t)\circ dx + \partial_t \log f(x,t)\,dt
\right]
$$

这里的 `temporal score` 是

$$
\partial_t \log f(x,t)
$$

它表示在固定位置 $x$ 上分布 $f(x,t)$ 随时间变化的快慢。它与 score-based diffusion 中常见的 $\partial_x \log f$ 不同：

- $\partial_x \log f$ 是空间 score
- $\partial_t \log f$ 是时间 score

在 `NESS` 下，

$$
\partial_t f = 0
\Rightarrow
\partial_t \log f = 0
$$

这时只用

$$
\int u \circ dx
$$

就足以闭合熵产生表达式。离开稳态后，$\partial_t \log f$ 不再消失；若忽略这项，就无法恢复完整的 trajectory-level stochastic entropy production。

#### 先把目标和 loss 写清楚

这一段里：

- $f(x,t)$ 仍然是时刻 $t$ 的概率密度
- $g(x,t):=\partial_t \log f(x,t)$ 是目标函数
- $w(x)$ 是测试函数或待学习函数

如果仍按 `L2` 回归的统一模板写，总体 loss 是

$$
\mathcal{L}_g(w)
=
dt\,\mathbb{E}\!\left[\frac{1}{2}(w-g)^2\right]
$$

展开并丢掉与 $w$ 无关的常数项：

$$
\mathcal{L}_g(w)
=
dt\int dx\, f(x,t)
\left[
\frac{1}{2}w(x)^2 - w(x)\,\partial_t \log f(x,t)
\right]
$$

因此困难仍然只在交叉项

$$
\mathbb{E}[w\,\partial_t \log f\,dt].
$$

#### 为什么交叉项会变成“测试函数期望的变化”

先直接代入定义：

$$
\mathbb{E}[w\,\partial_t \log f\,dt]
=
dt\int f(x,t)\,w(x)\,\partial_t \log f(x,t)\,dx
=
dt\int w(x)\,\partial_t f(x,t)\,dx
$$

第二个等号只是用了

$$
\partial_t \log f = \frac{\partial_t f}{f}.
$$

接着把时间导数提出：

$$
dt\int w(x)\,\partial_t f(x,t)\,dx
=
dt\,\frac{d}{dt}\int f(x,t)\,w(x)\,dx
$$

而

$$
\int f(x,t)\,w(x)\,dx = \mathbb{E}_t[w(x_t)]
$$

所以

$$
\mathbb{E}[w\,\partial_t \log f\,dt]
=
dt\,\frac{d}{dt}\mathbb{E}_t[w(x_t)].
$$

这一步的物理意思是：

`temporal score` 并不通过空间增量读出来，而是通过“测试函数在相邻时间层上的平均值变化”读出来。

#### 为什么离散后会出现 \(-w(x+\Delta x)+w(x)\)

对一个小时间步 $\Delta t$，有

$$
dt\,\frac{d}{dt}\mathbb{E}_t[w(x_t)]
\approx
\mathbb{E}_{t+\Delta t}[w(x_{t+\Delta t})]
- \mathbb{E}_{t}[w(x_t)].
$$

因此交叉项的经验估计就是

$$
\left\langle w(x+\Delta x) - w(x) \right\rangle
$$

其中 $\Delta x = x(t+\Delta t)-x(t)$。

但在 loss 里，这个交叉项是被减掉的，所以离散 loss 变成

$$
\hat{\mathcal{L}}_g^{(1)}
=
\left\langle
\frac{1}{2}w(x)^2\Delta t - \big[w(x+\Delta x)-w(x)\big]
\right\rangle
$$

也就是

$$
\mathcal{L}_{\partial_t \log f}(w)
=
\left\langle
\frac{1}{2}w(x)^2\Delta t - w(x+\Delta x) + w(x)
\right\rangle
$$

这就是文中对应的 temporal score loss。

#### 这条线和 Local EP Loss 的区别

`local EP loss` 之所以要用 Stratonovich current，是因为目标函数 $u$ 里含有空间密度梯度，需要把一阶漂移项和二阶扩散项绑在一起。

`temporal score loss` 不需要这样做，因为目标函数本身就是

$$
\partial_t \log f
$$

它天然对应“分布在相邻时间层上的变化”。所以这条线不通过空间 current 来读，而是通过测试函数期望在 $t$ 与 $t+\Delta t$ 之间的变化来读。

因此，$u(x,t)$ 描述概率流，$\partial_t \log f(x,t)$ 描述分布显式时间变化；非稳态下两者一起闭合轨迹熵产生。

### Diffusion Field Loss：从二阶矩恢复噪声强度

`diffusion field` 与前面几项的区别在于：它不出现在一阶平均增量里，而出现在二阶涨落里。

对 overdamped Langevin：

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

短时间离散化后：

$$
\Delta x = \Phi(x,t)\,\Delta t + \sigma\,\Delta W
$$

如果目标是学习热噪声方差 $\sigma^2$，关键就不是看 $\Delta x$ 的平均，而是看它的平方：

$$
(\Delta x)^2
=
\Phi(x,t)^2 \Delta t^2
+ 2\Phi(x,t)\sigma\,\Delta t\,\Delta W
+ \sigma^2(\Delta W)^2
$$

取条件期望后，前两项都比 $\Delta t$ 更高阶，主导项是：

$$
\mathbb{E}[(\Delta x)^2 \mid x]
=
\sigma^2 \Delta t + O(\Delta t^2)
$$

因此短时二阶涨落直接编码噪声强度。

于是同样沿用统一模板。理论 loss 写成：

$$
\mathcal{L}_{\sigma^2}(w)
=
\mathbb{E}\!\left[
\frac{1}{2}w^2 \Delta t - w\,\sigma^2 \Delta t
\right]
$$

由于 $\sigma^2$ 不可直接观测，用 $(\Delta x)^2$ 替代相关项，得到一阶经验 loss：

$$
\widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w)
=
\left\langle
\frac{1}{2}w^2 \Delta t - w\,(\Delta x)^2
\right\rangle
$$

把上面的条件期望代回去：

$$
\widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w)
=
\Delta t\,\mathbb{E}\!\left[
\frac{1}{2}w^2 - w\sigma^2
\right] + O(\Delta t^2)
$$

再做同样的配方：

$$
\widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w)
=
\Delta t\,\mathbb{E}\!\left[
\frac{1}{2}(w-\sigma^2)^2
\right] + \text{const} + O(\Delta t^2)
$$

因此一阶近似下：

$$
\arg\min_w \widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w) \approx \sigma^2
$$

这里默认 $\sigma^2$ 是常数，所以 $w$ 也只是一个标量。论文随后说，如果扩散强度依赖位置，写成 $\sigma^2(x)$，就必须把标量权重 $w$ 推广成函数 $w(x)$。因为这时

$$
\mathbb{E}[(\Delta x)^2 \mid x]
=
\sigma^2(x)\,\Delta t + O(\Delta t^2)
$$

不同位置对应不同的局域噪声强度，一个全局常数 $w$ 无法同时拟合所有位置；模型必须输入位置 $x$，输出该位置的扩散强度估计。对应的经验 loss 也从“学一个数”推广成“学一个场”：

$$
\widehat{\mathcal{L}}_{\sigma^2(x)}^{(1)}(w)
=
\left\langle
\frac{1}{2} w(x)^2 \Delta t - w(x)\,(\Delta x)^2
\right\rangle
$$

在同样的一阶近似下，它的最优解满足

$$
w^*(x) \approx \sigma^2(x)
$$

所以这一步不是改了方法，而是把同一模板从“常数扩散”推广到“位置依赖扩散场”。

如果更习惯用扩散系数表示法：

$$
D = \frac{\sigma^2}{2}
$$

paper 在 loss 里直接学习的是 $\sigma^2$；写成 $D$ 只是换一个归一化。

与 `force loss` 的对照是：

- `force loss` 用一阶矩 $\Delta x$ 恢复平均漂移
- `diffusion field loss` 用二阶矩 $(\Delta x)^2$ 恢复噪声强度

### B. Unification with TUR Estimates

本节解释 `TUR` 估计与本文的 `MSE/self-supervised loss` 为什么在短时间极限下共享同一条数学骨架。阅读顺序是：

1. 为什么 `TUR` 先看 `current`；
2. `TUR` 原来约束什么；
3. 它的物理意义是什么；
4. 短时间极限下本文要估计什么；
5. `Cauchy-Schwarz` 如何给出 `TUR/cosine` 型下界；
6. `MSE` 非负如何给出 `L2` 型下界；
7. 为什么对固定的 $w$，前者比后者更紧。

#### 1. 为什么是 Current

`TUR` 关心的不是任意可观测量，而首先是 `current`，因为随机热力学里最直接表征不可逆性的对象就是“是否存在持续的定向流动”。

这里的 `current` 可以是：

- 空间中的概率流
- 粒子、质量、能量、化学物质的净传输
- 在更抽象的路径层上，一个 time-integrated observable 的净通量

之所以不是先看静态分布，是因为：

- 平衡态和非平衡稳态都可能有时间不变的分布
- 但只有非平衡过程才会维持持续的净流和持续的熵产生

所以 `current` 是最自然的不可逆性探针。它既可从轨迹直接估计，又能直接反映系统是否在持续“往一个方向做事”。

#### 2. TUR 的起点

经典 `steady-state TUR` 对观测时间 $\tau$ 内的积分流 $J_\tau$ 写成：

$$
\frac{\mathrm{Var}(J_\tau)}{\langle J_\tau \rangle^2}
\ge
\frac{2}{\Sigma_\tau}
$$

等价地：

$$
\Sigma_\tau
\ge
\frac{2\langle J_\tau \rangle^2}{\mathrm{Var}(J_\tau)}
$$

其中 $J_\tau$ 是 time-integrated current，$\Sigma_\tau$ 是同一时间窗内的总熵产生。它表达的是：

`如果一个电流平均很大而波动又很小，系统就必须耗散足够多的熵。`

#### 3. TUR 的物理意义

`TUR` 真正锁定的是三件事之间的关系：

- 定向输出：$\langle J_\tau\rangle$
- 输出精度：$\mathrm{Var}(J_\tau)$
- 热力学代价：$\Sigma_\tau$

它说的是：

`如果一个系统想持续、稳定、低噪声地输出一个净流，它就必须支付熵产生。`

因此 `TUR` 不是一个孤立的不等式，而是“方向性 + 精确性 + 耗散”三者之间的热力学约束。它的用途也不只是给一个抽象下界，而是让你通过可观测的涨落统计，反推出隐藏的不可逆性成本。

本文做的是把这条“电流涨落下界熵产生”的思想，翻译到 `短时间 / 局域函数学习` 的语境中。

#### 4. 短时间极限下的目标量

在本文里，要恢复的是一个局域目标函数 $F$ 的平方范数：

$$
A = \mathbb{E}[F^2]
$$

这里：

- $F$ 是真实目标函数
- $w$ 是测试函数或待学习函数
- 目标是用 $w$ 和数据的相关结构，给 $A$ 构造一个可计算的下界

记期望内积为

$$
\langle u,v \rangle := \mathbb{E}[uv]
$$

于是

$$
A = \langle F,F \rangle = \|F\|^2
$$

数学任务就是：

`用测试函数 w 去下界真实目标 F 的平方范数。`

#### 5. Cauchy-Schwarz 给出 TUR/cosine 下界

`Cauchy-Schwarz inequality` 是最基本的内积不等式：

$$
\langle w,F\rangle^2 \le \langle w,w\rangle \langle F,F\rangle
$$

写成期望形式就是

$$
\mathbb{E}[wF]^2 \le \mathbb{E}[w^2]\,\mathbb{E}[F^2]
$$

移项后得到

$$
\mathbb{E}[F^2]
\ge
\frac{\mathbb{E}[wF]^2}{\mathbb{E}[w^2]}
$$

于是自然定义

$$
B_{\mathrm{TUR}}(w)
:=
\frac{\mathbb{E}[wF]^2}{\mathbb{E}[w^2]}
$$

这就是 `TUR/cosine` 型下界。它反映的是：$w$ 和 $F$ 对齐得越好，这个下界越高。

取等号条件是

$$
w = cF
$$

也就是测试函数和真实目标函数成比例。这里恢复的是方向，不是精确幅值，所以这条线更像 `alignment`，不是标准 `regression`。

#### 6. MSE 非负给出 L2 下界

另一条线只用平方非负：

$$
\mathbb{E}[(F-w)^2] \ge 0
$$

展开得到

$$
\mathbb{E}[F^2] - 2\mathbb{E}[wF] + \mathbb{E}[w^2] \ge 0
$$

移项后得到

$$
\mathbb{E}[F^2]
\ge
2\mathbb{E}[wF] - \mathbb{E}[w^2]
$$

于是定义

$$
B_{\mathrm{L2}}(w)
:=
2\mathbb{E}[wF] - \mathbb{E}[w^2]
$$

并且

$$
A - B_{\mathrm{L2}}(w) = \mathbb{E}[(F-w)^2]
$$

所以 `L2` 下界和真实值之间的差，正好就是均方误差。

#### 7. 比较这两个下界

对同一个测试函数 $w$，有

$$
B_{\mathrm{TUR}}(w)
=
\frac{\mathbb{E}[wF]^2}{\mathbb{E}[w^2]}
$$

和

$$
B_{\mathrm{L2}}(w)
=
2\mathbb{E}[wF] - \mathbb{E}[w^2]
$$

它们满足

$$
A \ge B_{\mathrm{TUR}}(w) \ge B_{\mathrm{L2}}(w)
$$

令

$$
a=\mathbb{E}[wF], \qquad b=\mathbb{E}[w^2]
$$

那么

$$
B_{\mathrm{TUR}}(w)-B_{\mathrm{L2}}(w)
=
\frac{a^2}{b}-(2a-b)
=
\frac{(a-b)^2}{b}
\ge 0
$$

因此，对固定的 $w$，`TUR/cosine` 下界总是不低于 `L2` 下界。这里的“更紧”指的是：同样作为下界，`TUR/cosine` 给出的数值更接近真实值 $A$。

但这个结论只比较 `固定 w` 时的两个下界。它不能直接推出 `cosine loss` 一定比 `L2 loss` 更适合训练，因为训练过程中 $w$ 本身会变化。

### TUR 与 FDR Violation 的关系

`TUR` 和 `FDR violation` 都是在用涨落信息读取不可逆性，但它们看的不是同一种可观测量。

- `TUR` 看的对象是 `current`。它把 `平均净流`、`净流波动` 和 `entropy production` 连在一起，强调的是 `precision-dissipation tradeoff`。
- `FDR violation` 看的对象是 `correlation-response pair`。它比较的是“自发涨落”和“外加微扰响应”是否还满足平衡态中的对应关系。

因此两者对应不同层次：

- `TUR` 更接近 `path / current layer`
- `FDR violation` 更接近 `two-point correlation / response layer`

放在这篇里，`TUR` 是更自然的入口，因为作者手上直接有轨迹增量、Stratonovich current 和局域 velocity；这些量天然属于 `current` 语言，而不是 `response` 语言。

### 阅读时最该盯住的关系

1. `force loss` 恢复的是 $\Phi$
2. `local EP loss` 恢复的是 $u = \Phi - D\,\partial_x \log f$
3. `temporal score loss` 恢复的是 $\partial_t \log f$
4. `diffusion field loss` 恢复的是 $\sigma^2$，等价地也就是 $D = \sigma^2/2$
5. 完整的非稳态 stochastic entropy production 需要：

$$
\int u \circ dx + \int \partial_t \log f\,dt
$$

### 阅读时最该盯住的问题

1. 这篇到底是在学动力学、热力学量，还是两者之间的映射？
2. `current` 在每个 loss 里扮演的是可观测替代量，还是最终目标本身？
3. 哪些 loss 只能恢复平均量，哪些能恢复 trajectory-level information？
4. TUR 为什么只给出方向匹配式的估计，而 MSE 框架能更自然地做回归？
