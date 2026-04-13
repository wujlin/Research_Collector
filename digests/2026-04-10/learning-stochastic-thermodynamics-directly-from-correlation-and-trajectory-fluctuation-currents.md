---
title: "Learning stochastic thermodynamics directly from correlation and trajectory-fluctuation currents"
paper_title: "Learning Stochastic Thermodynamics Directly from Correlation and Trajectory-Fluctuation Currents"
digest_type: "paper_note"
date: "2026-04-10"
---

# Learning Stochastic Thermodynamics Directly From Correlation And Trajectory-Fluctuation Currents

## Core Answer

这篇文章最值得带走的核心回答是：作者不是把随机热力学当成“先算好标签再做回归”的问题，而是把它改写成了一个 `self-supervised function learning` 框架。通过短时间轨迹统计构造 loss，他们可以直接学习四类局域对象：`drift`、`probability velocity u`、`temporal score` 和 `diffusion field`，并由此恢复非稳态条件下的 stochastic entropy production 结构。

## Reading Frame

为了避免后面被大量 loss 和离散公式带跑，这篇最好先固定一条阅读框架：

1. 它要解决的问题是：没有标签、没有显式密度、也不借助外加响应实验时，能否直接从轨迹恢复随机热力学里的关键局域量。
2. 它研究的对象不是单个网络，而是 correlation functions、trajectory-fluctuation currents 和它们对应的局域热力学场。
3. 它最核心的量不是一个总 entropy production 数字，而是 `u(x,t)`、`\partial_t\log f(x,t)` 这样的局域对象。
4. 它的方法关键是：把目标场写成一个短时间变分问题，使最优预测器等于真实局域热力学量。
5. 它最有说服力的证据是：不仅平均量能恢复，trajectory-level stochastic entropy production 的涨落结构也能被学出来。
6. 你真正该带走的是：先构造可学习的局域场，再由这些局域场重建热力学量。

## Paper Info

- 为什么先读：
  这篇最直接接你这两天刚整理好的主线：`Sagawa -> fluctuation theorem -> entropy production -> Fokker-Planck -> trajectory current`。
- 论文链接：
  https://arxiv.org/abs/2504.19007

#### 1. 问题

这篇的问题不是“再做一个生成模型”，而是：

`能不能直接从相关函数和轨迹涨落电流里学习随机热力学量，尤其是 entropy production？`

不要被标题里的 `learning` 带跑，先确认它是否在解决“热力学量可识别性”问题。

把问题再压缩一层，这篇真正要解决的是：

`在没有标签、没有显式概率密度、也不依赖外加响应实验的情况下，能不能只用轨迹数据本身恢复随机热力学里的关键局域量。`

这里的难点不是单纯“拟合得准不准”，而是：

- `entropy production` 本身不是直接可观测量
- `TUR` 通常给的是 `lower bound`，不是完整局域场
- 一旦离开 `NESS`，只看流动项就不够，还要处理分布显式随时间变化的那一项

#### 1.5 主要贡献

这篇的主要贡献不是网络结构，而是推断框架：

1. 它把随机热力学推断改写成 `self-supervised function learning`，训练信号直接来自短时间轨迹统计。
2. 它用同一套 loss 模板恢复四个局域对象：`drift`、`probability velocity u`、`temporal score` 和 `diffusion field`。
3. 它把 `TUR/cosine` 型下界和 `L2/MSE` 型回归放进同一条短时间变分逻辑里。
4. 它把 entropy production 从 `NESS` 推广到非稳态情形，显式补上 \(\partial_t \log f\) 对应的时间变化项。
5. 它通过 `higher-order inference` 进一步压低有限 \(\Delta t\) 带来的系统偏差。

#### 2. 对象

这篇优先看的对象应该有两个：

- `trajectory-fluctuation currents`
- `correlation functions`

需要确认：作者到底是在路径层操作，还是在密度层操作，还是在两层之间来回翻译。

#### 3. 演化

这里优先找这几个骨架：

- `stochastic process`
- `path probability`
- `Fokker-Planck` 或其等价的路径表述
- `forward / reverse-time structure`

如果文中没有直接把 `Fokker-Planck` 写成主角，也要看它是不是在隐含地通过路径概率或 current structure 使用同一套动力学。

#### 4. 量

优先盯住以下量：

- `entropy production`
- 可能出现的 `irreversibility measure`
- correlation/current 与热力学量之间的函数关系

关键问题是：

`它是在显式估计 entropy production，还是给一个 proxy / lower bound / identifiable quantity？`

#### 5. 方法

方法部分要确认它的 `learning` 到底在做什么：

- 学动力学参数
- 学热力学量
- 学从统计量到热力学量的映射

如果方法部分开始变复杂，先抓一件事：

`方法到底是为了恢复路径结构，还是为了恢复热力学量？`

#### Four Target Quantities: 定义与作用

先区分 Table I 里的四个目标量。它们对应平均动力学、不可逆概率流、分布时间变化和噪声强度。

**1. Drift**

文中用 `force`，在 overdamped 情形里更准确的说法是 `drift`：

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

它描述在局域位置 `x` 和时刻 `t` 的平均运动方向与速度。没有噪声时，它就是确定性推力；有噪声时，它仍然决定平均运动方向。

**2. Probability Velocity \(u\) / Local EP**

本文学习的不是局域熵产生标量本身，而是 `probability velocity`

$$
u(x,t) = \Phi(x,t) - D\,\partial_x \log f(x,t)
$$

它把 drift 和分布梯度修正合在一起，描述不可逆概率流。平均熵产生率满足

$$
\dot{\Sigma} \propto \frac{1}{D}\,\mathbb{E}[u(x,t)^2]
$$

所以 `u` 是本文表征 local EP 的核心局域场。

**3. Temporal Score**

$$
\partial_t \log f(x,t)
$$

它表示在固定位置 `x` 上，概率密度 `f(x,t)` 随时间变化得有多快。在 `NESS` 下这一项消失；离开稳态后，它负责补上分布显式改写带来的熵产生贡献。

**4. Diffusion Field**

在最简单的 overdamped 情形里，它对应噪声强度或扩散系数：

$$
D = \frac{1}{2}\sigma^2
$$

如果系统是空间非均匀的，也可以推广成位置相关的 `D(x,t)`。它不决定平均往哪走，而决定轨迹抖动强度和分布扩散速度。

四个对象的层次关系是：

- `drift`：平均动力学
- `probability velocity u`：不可逆概率流
- `temporal score`：分布时间变化
- `diffusion field`：噪声强度

因此这篇 paper 同时恢复平均动力学、不可逆概率流、分布时间变化和噪声强度。

#### Loss Functions in Overdamped Dynamics: 总览

![Fig. 1 learning framework](../../pdfs/2026-04-10/learning-stochastic-thermodynamics-directly-from-correlation-and-trajectory-fluctuation-currents.mineru/hybrid_auto/images/44953915ad02b10b94c1333ed4656925efe87f626b0e44ea8c5a434ef2f152ae.jpg)

在 overdamped dynamics 里，paper 的统一起点是

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

对应的学习任务不是只恢复一个 drift，而是同时恢复四个局域对象：

- `drift` $\Phi(x,t)$
- `probability velocity` $u(x,t)$
- `temporal score` $\partial_t \log f(x,t)$
- `diffusion field` $\sigma^2$ 或等价的 $D=\sigma^2/2$

这四类 loss 的共同逻辑是：

1. 先选定一个目标函数 $G(x,t)$。
2. 找到一个可以从短时间轨迹估计的量，使它的期望或相关项与 $G$ 成线性关系。
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

这张 framework 图其实把全文的方法骨架压得很清楚：输入不是标签化的热力学量，而是相邻两个或三个时间点组成的局部轨迹片段；一阶 loss 用两点，二阶 loss 用三点，目标都是把“短时间可观测统计”变成对局域热力学场的 self-supervised 估计。所以这篇的关键不是网络结构，而是如何把 `trajectory snippet -> loss -> local thermodynamic field` 这条线写成可训练的二次泛函。

#### Force Loss: 从轨迹增量恢复 Drift

观测量是轨迹点与短时增量 $\Delta x_n = x_{n+1} - x_n$，目标量是 drift $\Phi(x,t)$，但轨迹上没有逐点标签。作者从 overdamped Langevin dynamics 直接构造只依赖可观测量的 loss。

动力学起点是：

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

离散到短时间步 $\Delta t$：

$$
\Delta x = \Phi(x,t)\,\Delta t + \sigma\,\Delta W
$$

其中噪声均值为零，所以条件期望满足：

$$
\mathbb{E}[\Delta x \mid x] = \Phi(x,t)\,\Delta t
$$

核心输入是：短时增量的条件期望给出局域 drift 的方向与大小。

接着用神经网络 $w(x)$ 去近似 $\Phi(x,t)$，并定义：

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

然后做一次完全平方：

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

最后那项 `const` 和网络参数无关，所以：

$$
\arg\min_w \mathcal{L}_{\mathrm{force}}(w)
=
\arg\min_w \mathbb{E}\!\left[(w-\Phi)^2\right]
$$

因此作者构造的是一个 `只依赖可观测量、但与 drift MSE 等价` 的自监督损失函数。

它与 `reverse diffusion / score matching` 共享以下结构：

- 都没有直接标签
- 都利用前向随机动力学
- 都构造了一个替代训练信号

区别在于：这里学习的不是 reverse sampler，而是 `局域动力学/热力学函数`。

Table I 里的很多条目共享同一个模板：

- `Force`
  用 `Δx` 构造 loss
- `Local entropy production`
  用 current / Stratonovich product 构造 loss
- `Temporal score`
  用 `Δw` 或时间变化构造 loss

统一逻辑是：

```text
目标量不可直接观测
-> 找到与它同均值结构的短时增量 / current
-> 写成只含可观测量的 loss
-> 配方后恢复成 MSE 等价
```

#### Local EP Loss: 为什么要用 Stratonovich Current

`local EP loss` 的目标量不是 drift $\Phi(x,t)$，而是 probability velocity

$$
u(x,t) = \Phi(x,t) - D\,\partial_x \log f(x,t)
$$

平均熵产生率与它满足

$$
\dot{\Sigma} \propto \frac{1}{D}\,\mathbb{E}[u(x,t)^2]
$$

问题在于，如果只用 $\Delta x$，它的条件均值只能告诉你

$$
\mathbb{E}[\Delta x \mid x] = \Phi(x,t)\,\Delta t
$$

这只能恢复 $\Phi$，恢复不了 $-D\,\partial_x \log f$ 这部分分布梯度信息。

#### 先把对象说清楚

这段里最容易混的是三个函数：

- $f(x,t)$：系统在时刻 $t$ 的概率密度，不是测试函数
- $u(x,t)$：目标函数，也就是 probability velocity
- $w(x)$：测试函数或待学习函数

这里的期望符号就是按 $f(x,t)$ 加权：

$$
\mathbb{E}[g(x_t)] = \int dx\, f(x,t)\,g(x)
$$

所以式子里写 $f(x,t)$，只是因为作者在写总体风险；真正被优化的是 $w(x)$。

#### 为什么总体 loss 写成这个形式

作者希望最优解满足

$$
u = \arg\min_w \mathcal{L}_u(w)
$$

最直接的构造就是对 $u$ 做 `L2` 回归：

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

最后一项与 $w$ 无关，可以丢掉，于是得到

$$
\mathcal{L}_u(w)
=
dt\int dx\,f(x,t)\left[\frac{1}{2}w(x)^2 - w(x)u(x,t)\right]
$$

所以式 (19) 本质上就是 “对目标函数 $u$ 做 MSE 回归” 去掉常数项之后的总体风险。

#### 式 (20) 的线性展开

真正困难的是交叉项

$$
\mathbb{E}[w\,u\,dt]
$$

因为 $u(x,t)$ 里含有未知的密度梯度：

$$
u(x,t)
=
\Phi(x,t) - \frac{1}{2}\sigma^2 \frac{\partial_x f(x,t)}{f(x,t)}
$$

代回期望：

$$
\mathbb{E}[w\,u\,dt]
=
dt\int dx\, f(x,t)\,w(x)
\left[
\Phi(x,t) - \frac{1}{2}\sigma^2 \frac{\partial_x f(x,t)}{f(x,t)}
\right]
$$

把第二项里的 $f$ 约掉：

$$
\mathbb{E}[w\,u\,dt]
=
dt\int dx\,
\left[
f(x,t)w(x)\Phi(x,t)
- \frac{1}{2}\sigma^2 w(x)\partial_x f(x,t)
\right]
$$

对第二项分部积分，并假设边界项消失：

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

改写成增量。因为噪声项期望为零：

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

最后用 It\^o 和 Stratonovich 的换算：

$$
w(x)\circ dx
=
w(x)\,dx + \frac{1}{2}\sigma^2 \partial_x w(x)\,dt
$$

取期望后得到

$$
\mathbb{E}[w\,u\,dt] = \mathbb{E}[w(x)\circ dx]
$$

这就是式 (20) 的核心。原来显式依赖密度梯度 $\partial_x f$ 的相关项，被改写成了可以直接从轨迹增量估计的 `Stratonovich current`。

#### 式 (21) 为什么是中点离散

在一个小时间步 $[t,t+\Delta t]$ 上，Stratonovich 积分用中点规则离散：

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

这就是式 (21)。第一项来自 $\frac{1}{2}w^2dt$，第二项来自离散化的 Stratonovich current。

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

这里最先要分清记号：`higher-order inference` 里出现的 $\Delta_2 x$ 不是 $(\Delta x)^2$，而是跨两个时间步的增量

$$
\Delta x := x(t+\Delta t)-x(t),\qquad
\Delta_2 x := x(t+2\Delta t)-x(t).
$$

设 $h=\Delta t$。对短时间增量做展开时，单步条件期望一般可以写成

$$
\mathbb{E}[\Delta x \mid x_t=x]
=
\Phi(x,t)\,h + a(x,t)\,h^2 + O(h^3),
$$

其中 $a(x,t)$ 收集了所有二阶修正项。把时间步长换成 $2h$，对应地有

$$
\mathbb{E}[\Delta_2 x \mid x_t=x]
=
2\Phi(x,t)\,h + 4a(x,t)\,h^2 + O(h^3).
$$

现在看作者构造的线性组合：

$$
2\,\mathbb{E}[\Delta x \mid x_t=x]
- \frac{1}{2}\,\mathbb{E}[\Delta_2 x \mid x_t=x].
$$

把上面两条展开代进去：

$$
2(\Phi h + ah^2 + O(h^3))
- \frac{1}{2}(2\Phi h + 4ah^2 + O(h^3))
=
\Phi h + O(h^3).
$$

这里一阶项留下来，二阶项正好抵消掉，所以这个组合不是“忽略了”二次无穷小，而是用两个不同步长的增量把它消掉了。这就是 `higher-order inference` 的核心结构。

如果 paper 的右边写成

$$
\Phi(x,t)f(x,t)\,\Delta t + O(\Delta t^3),
$$

多出来的 $f(x,t)$ 通常不是因为 drift 变了，而是因为作者写的是局域化后的无条件期望，例如乘了一个定位因子 $\delta(x_t-x)$。这时

$$
\mathbb{E}[\delta(x_t-x)] = f(x,t),
$$

于是就会得到

$$
\mathbb{E}\!\left[\left(2\Delta x-\frac{1}{2}\Delta_2 x\right)\delta(x_t-x)\right]
=
\Phi(x,t)f(x,t)\,\Delta t + O(\Delta t^3).
$$

所以这一步的作用很明确：一阶方法给的是 $\Phi\,\Delta t + O(\Delta t^2)$，而这个两步组合把偏差再压低一阶，变成 $\Phi\,\Delta t + O(\Delta t^3)$。

到这一步为止，恢复的仍然只是轨迹级随机熵产生中的流动项。对于 `NESS`，由于 $\partial_t \log f = 0$，这一项已经足够；离开稳态后，还必须补上显式记录分布时间变化的 temporal score。

#### Temporal Score: 角色与对应 Loss

文中 stochastic entropy production 的轨迹形式是：

$$
\sigma_{\Gamma}
=
\int_{\Gamma}
\left[
u(x,t)\circ dx + \partial_t \log f(x,t)\,dt
\right]
$$

这里的 `temporal score` 是：

$$
\partial_t \log f(x,t)
$$

它表示在固定位置 $x$ 上，概率密度 $f(x,t)$ 随时间变化得有多快。这和 score-based diffusion 里常见的 $\partial_x \log f$ 不同：

- $\partial_x \log f$ 是空间方向上的 score
- $\partial_t \log f$ 是时间方向上的 score

在 `NESS` 里，

$$
\partial_t f = 0
\quad \Rightarrow \quad
\partial_t \log f = 0
$$

只靠

$$
\int u \circ dx
$$

就足以闭合熵产生表达式。离开稳态后，$\partial_t \log f$ 不再消失；若忽略这项，就无法恢复完整的 trajectory-level stochastic entropy production。

#### 先把目标和 loss 写清楚

这一段里：

- $f(x,t)$ 仍然是时刻 $t$ 的概率密度
- $g(x,t):=\partial_t \log f(x,t)$ 是目标函数
- $w(x)$ 是测试函数或待学习函数

如果继续按 `L2` 回归的统一模板写，总体 loss 是

$$
\mathcal{L}_g(w)
=
dt\,\mathbb{E}\!\left[\frac{1}{2}(w-g)^2\right]
$$

展开并去掉与 $w$ 无关的常数项：

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

先代入定义：

$$
\mathbb{E}[w\,\partial_t \log f\,dt]
=
dt \int f(x,t)\,w(x)\,\partial_t \log f(x,t)\,dx
=
dt \int w(x)\,\partial_t f(x,t)\,dx
$$

第二个等号只是用了

$$
\partial_t \log f = \frac{\partial_t f}{f}.
$$

再把时间导数拿出来：

$$
dt \int w(x)\,\partial_t f(x,t)\,dx
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

它的物理意义是：

`temporal score` 不是通过空间增量读出来，而是通过“测试函数在相邻时间层上的平均值变化”读出来。

#### 为什么离散后会出现 \(-w(x+\Delta x)+w(x)\)

对一个小时间步 $\Delta t$，有

$$
dt\,\frac{d}{dt}\mathbb{E}_t[w(x_t)]
\approx
\mathbb{E}_{t+\Delta t}[w(x_{t+\Delta t})]
- \mathbb{E}_{t}[w(x_t)].
$$

因此交叉项的经验估计是

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

也就是文中的 temporal score loss：

$$
\mathcal{L}_{\partial_t \log f}(w)
=
\left\langle
\frac{1}{2}w(x)^2\Delta t - w(x+\Delta x) + w(x)
\right\rangle
$$

#### 这条线和 Local EP Loss 的区别

`local EP loss` 之所以要用 Stratonovich current，是因为目标函数 $u$ 里含有空间密度梯度，需要把一阶漂移项和二阶扩散项绑在一起。

`temporal score loss` 不需要这样做，因为目标函数本身就是

$$
\partial_t \log f
$$

它天然对应“分布在相邻时间层上的变化”。所以这条线不通过空间 current 来读，而是通过测试函数期望在 $t$ 与 $t+\Delta t$ 之间的变化来读。

因此，$u(x,t)$ 描述概率流，$\partial_t \log f(x,t)$ 描述分布显式时间变化；非稳态下两者一起闭合轨迹熵产生。

#### Diffusion Field Loss: 从二阶矩恢复噪声强度

`diffusion field` 不是平均漂移，而是噪声强度。它不出现在一阶矩里，而出现在二阶涨落里，所以这里改用：

$$
(\Delta x)^2
$$

对 overdamped Langevin：

$$
dx = \Phi(x,t)\,dt + \sigma\,dW_t
$$

在短时间内有：

$$
\Delta x = \Phi(x,t)\,\Delta t + \sigma\,\Delta W
$$

把它平方：

$$
(\Delta x)^2
=
\Phi(x,t)^2 \Delta t^2
+ 2\Phi(x,t)\sigma\,\Delta t\,\Delta W
+ \sigma^2 (\Delta W)^2
$$

由于 $\Delta W \sim \mathcal{N}(0,\Delta t)$，并且 $(\Delta W)^2$ 的平均是 $\Delta t$，所以主导项是：

$$
\mathbb{E}[(\Delta x)^2 \mid x]
=
\sigma^2 \Delta t + O(\Delta t^2)
$$

因此短时位移的二阶矩直接读出噪声强度。

于是同样沿用那套模板。若目标量是常数扩散强度 $\sigma^2$，先写理论 loss：

$$
\mathcal{L}_{\sigma^2}(w)
=
\mathbb{E}\!\left[
\frac{1}{2} w^2 \Delta t - w\,\sigma^2 \Delta t
\right]
$$

再把不可观测的 $\sigma^2 \Delta t$ 用可观测的 $(\Delta x)^2$ 替代，得到离散 loss：

$$
\widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w)
=
\left\langle
\frac{1}{2} w^2 \Delta t - w\,(\Delta x)^2
\right\rangle
$$

把条件期望代回去：

$$
\widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w)
=
\Delta t\,\mathbb{E}\!\left[
\frac{1}{2}w^2 - w\sigma^2
\right] + O(\Delta t^2)
$$

再配方：

$$
\widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w)
=
\Delta t\,\mathbb{E}\!\left[
\frac{1}{2}(w-\sigma^2)^2
\right] + \text{const} + O(\Delta t^2)
$$

因此在一阶近似下：

$$
\arg\min_w \widehat{\mathcal{L}}_{\sigma^2}^{(1)}(w) \approx \sigma^2
$$

上面这个版本默认 $\sigma^2$ 是常数，所以 $w$ 也只是一个标量。论文接着说，如果扩散强度依赖位置，写成 $\sigma^2(x)$，就必须把标量权重 $w$ 推广成函数 $w(x)$。原因很直接：这时

$$
\mathbb{E}[(\Delta x)^2 \mid x]
=
\sigma^2(x)\,\Delta t + O(\Delta t^2)
$$

不同位置对应不同的局域噪声强度，一个全局常数 $w$ 无法同时拟合所有位置；模型必须输入 $x$，输出该位置的扩散强度估计。对应的经验 loss 也从“学一个数”变成“学一个场”：

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

所以这句话的真正含义是：数学模板没有变，只是从“恢复一个全局常数扩散系数”推广成“恢复一个位置依赖的扩散场”。

如果你更习惯用扩散系数 $D = \sigma^2 / 2$，这篇 paper 在 loss 里直接学的是 $\sigma^2$；写成 $D$ 只是换一个常数因子。

与 `force loss` 的对照是：

- `force loss` 用 $\Delta x$ 的一阶矩恢复 drift
- `diffusion field loss` 用 $(\Delta x)^2$ 的二阶矩恢复噪声强度

#### B. Unification with TUR Estimates

本节解释 `TUR` 估计与本文的 `MSE/self-supervised loss` 为什么在短时间极限下共享同一条数学骨架。阅读顺序是：

1. 为什么 `TUR` 先看 `current`；
2. `TUR` 原来约束什么；
3. 它的物理意义是什么；
4. 本文在短时间极限下想估计什么；
5. `Cauchy-Schwarz` 如何给出 `TUR/cosine` 型下界；
6. `MSE` 非负如何给出 `L2` 型下界；
7. 为什么对固定的 $w$，前者总比后者紧。

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

经典 `steady-state TUR` 针对观测时间 $\tau$ 内的积分流 $J_\tau$：

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

其中：

- $J_\tau$ 是你选定的 time-integrated current
- $\Sigma_\tau$ 是同一时间窗内的总熵产生

物理图像是：如果一个电流平均值大、波动又小，系统就必须耗散足够多的熵。

#### 3. TUR 的物理意义

`TUR` 真正锁定的是三件事之间的关系：

- 定向输出：$\langle J_\tau\rangle$
- 输出精度：$\mathrm{Var}(J_\tau)$
- 热力学代价：$\Sigma_\tau$

它说的是：

`如果一个系统想持续、稳定、低噪声地输出一个净流，它就必须支付熵产生。`

因此 `TUR` 不是一个孤立的不等式，而是“方向性 + 精确性 + 耗散”三者之间的热力学约束。它的用途也不只是给一个抽象下界，而是让你通过可观测的涨落统计，反推出隐藏的不可逆性成本。

本文做的不是直接重复这条稳态公式，而是把它翻译到 `短时间 / 局域函数学习` 的语境里。

#### 4. 短时间极限下的目标量

在本文里，要恢复的是一个局域目标函数 $F$ 的平方范数：

$$
A = \mathbb{E}[F^2]
$$

这里：

- $F$ 是真实目标函数，比如 local EP 对应的局域热力学量
- $w$ 是测试函数或待学习函数
- 目标是用 $w$ 和数据的相关结构，给 $A$ 构造一个可计算的下界

把期望内积记为

$$
\langle u,v \rangle := \mathbb{E}[uv]
$$

于是

$$
A = \langle F,F \rangle = \|F\|^2
$$

这一节的数学任务是：

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

因此定义

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
A - B_{\mathrm{L2}}(w)
=
\mathbb{E}[(F-w)^2]
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

它们都满足

$$
A \ge B_{\mathrm{TUR}}(w),
\qquad
A \ge B_{\mathrm{L2}}(w)
$$

而且进一步有

$$
B_{\mathrm{TUR}}(w) \ge B_{\mathrm{L2}}(w)
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

因此，对固定的 $w$，`TUR/cosine` 下界总是不低于 `L2` 下界。这里的“更紧”指的是：同样在下界这个角色里，`TUR/cosine` 给出的数值更接近真实值 $A$。

但这个结论只比较 `固定 w` 时的两个下界。它不能直接推出 `cosine loss` 一定比 `L2 loss` 更适合训练，因为训练过程中 $w$ 本身会变化。

#### 8. TUR 与 FDR Violation 的关系

`TUR` 和 `FDR violation` 都不是直接“看见熵产生”，而是借助可观测涨落去读不可逆性，但它们读的是不同层的对象。

- `TUR` 看的对象是 `current`。它问的是：如果系统维持了一个稳定的净流，而且这个净流的相对波动很小，那么至少需要多少熵产生。
- `FDR violation` 看的对象是 `correlation-response pair`。它问的是：系统的自发涨落和线性响应，是否还满足平衡态里的对应关系；如果不满足，这个偏离量本身就是非平衡驱动的信号。

所以两者对应的是两种不同的观测层：

- `TUR` 更接近 `path / current layer`
- `FDR violation` 更接近 `two-point correlation / response layer`

在这篇里，`TUR` 是更自然的入口，因为作者直接操作的是轨迹增量、Stratonovich current 和局域 velocity；到 `Paper 3` 时，重点会转到频域相关函数与响应函数，那时 `FDR violation` 会成为更自然的入口。

#### 9. 证据

优先看这三类证据里哪一类最强：

- toy stochastic system
- 数值实验里 entropy production 的恢复效果
- 与已有理论公式或 benchmark 的一致性

如果论文只有实验图，没有明确理论对照，那你就把它记成“方法提议型”，不要误判成理论闭环已经完成。

![Fig. 2(b) trajectory-level entropy production inference](../../pdfs/2026-04-10/learning-stochastic-thermodynamics-directly-from-correlation-and-trajectory-fluctuation-currents.mineru/hybrid_auto/images/0ad01a47c9b721f27ac42e60a1caf317b2404e104010f007825f89d3b4181653.jpg)

![Fig. 2(f) stochastic entropy production versus the $u$-integral contribution](../../pdfs/2026-04-10/learning-stochastic-thermodynamics-directly-from-correlation-and-trajectory-fluctuation-currents.mineru/hybrid_auto/images/a013a87dc01978871c5f88fdfa191940d22a7b678e9ed6910f70e2f67c590e3d.jpg)

如果只挑两张最值得盯的图，我会选这里这两张。`Fig. 2(b)` 直接对应“单条轨迹上的 stochastic entropy production 能不能被学出来”这个最硬的问题；右图里二阶 loss 随路径数增加持续压低 $1-R^2$，说明它不仅能恢复平均熵产生，还能在 trajectory level 上更稳定地恢复涨落结构。`Fig. 2(f)` 则把本文为什么要单独学习 `temporal score` 这件事可视化了：红线是真正的 stochastic entropy production，蓝线只是 $\int D^{-1}u \circ dx$ 这一部分，两者之间的系统差异正是非稳态下 $\partial_t \log f$ 不能被忽略的证据。

#### 10. 复现

这篇最自然的 toy reproduction 是：

1. 先做一个 `1D overdamped Langevin` 或双稳态系统。
2. 生成轨迹。
3. 估计 correlation / trajectory current。
4. 看是否能恢复或近似 `entropy production`。

- 卡住时先看：
  - `Takahiro Sagawa | An introduction to stochastic thermodynamics`
    https://www.youtube.com/watch?v=m023IrSLF-k
  - `Bernard Derrida | Large deviations of non-equilibrium diffusive systems`
    https://www.youtube.com/watch?v=1faKoBxBvQU
- 对应笔记：
  - [takahiro-sagawa-stochastic-thermodynamics.md](/Users/jinlin/Desktop/Project/Research_Collector/youtube/notes/takahiro-sagawa-stochastic-thermodynamics.md)
  - [bernard-derrida-large-deviations-of-non-equilibrium-diffusive-systems.md](/Users/jinlin/Desktop/Project/Research_Collector/youtube/notes/bernard-derrida-large-deviations-of-non-equilibrium-diffusive-systems.md)
  - [landauer-to-generative-models.md](/Users/jinlin/Desktop/Project/Research_Collector/youtube/notes/landauer-to-generative-models.md)
