---
title: "Statistics and Dynamics of Urban Populations, Chapter 10: About city dynamics"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-28"
topics: ["urban dynamics", "Levy noise", "fractional Fokker-Planck equation", "Fox H-functions", "city-size distribution", "rank dynamics", "Gabaix model"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/10-about-city-dynamics.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 10：About City Dynamics

## 精读笔记

---

## 一、这一章在全书动力学线里的位置

Chapter 9 从 migration flows 出发，推出了一个新的城市增长方程：

$$
\frac{\partial S}{\partial t}
=
\eta S
+
D S^\beta \zeta_{\alpha,\delta}.
$$

这条式子改变了前面几章的建模语言。Gibrat-style model 只有 Gaussian multiplicative growth；Chapter 9 的方程则同时包含 Gaussian out-of-system growth 和 heavy-tailed Levy migration noise。

Chapter 10 的任务是回答三个问题。

第一，这个新方程能不能被进一步简化？

$$
\eta S
+
D S^\beta\zeta_{\alpha,\delta}
\quad
\Longrightarrow
\quad
rS
+
D S^\beta\zeta_\alpha.
$$

第二，简化后的方程对应什么样的 probability distribution？

$$
\text{Levy SDE}
\quad
\Longrightarrow
\quad
\text{fractional Fokker-Planck equation}.
$$

第三，这个解能否解释真实城市系统的两个现象？

$$
\text{city-size distribution scaling}
\quad
\text{and}
\quad
\text{rank turbulence}.
$$

这一章的主线可以写成：

$$
\begin{aligned}
&\text{Chapter 9 growth equation}\\
&\rightarrow \text{reduce Gaussian noise to drift}\\
&\rightarrow \text{derive fractional Fokker-Planck}\\
&\rightarrow \text{solve through Fox-function asymptotics}\\
&\rightarrow \text{large-}S\text{ expansion}\\
&\rightarrow \text{apparent Zipf and slow convergence}\\
&\rightarrow \text{universal scaling collapse}\\
&\rightarrow \text{rank dynamics test}\\
&\rightarrow \text{Levy shocks explain turbulent city histories}.
\end{aligned}
$$

所以 Chapter 10 不是单纯求一个技术解。它要说明：Chapter 9 的 Levy growth equation 不只是形式上漂亮，而且能解释为什么城市规模分布看起来像 power-law、为什么 Zipf exponent 不稳定、以及为什么城市 rank 会长期剧烈波动。

### 1.1 本章符号口径

Chapter 10 会在城市变量和通用 stochastic-process 变量之间切换。为了避免混淆，先固定读法。

$S$ 表示城市 population size，$P(S,t)$ 表示城市人口分布的 density。推导 fractional Fokker-Planck 时，作者暂时用 $x$ 表示 generic state variable，并用 $p(x,t)$ 表示 generic density。读回城市问题时，对应关系是：

$$
x\leftrightarrow S,
\qquad
p(x,t)\leftrightarrow P(S,t).
$$

$\alpha$ 是 Chapter 9 继承下来的 Levy stability index，也是 migration shock tail exponent。城市方程里的 Levy noise 写成 $\zeta_{\alpha,\delta}$ 或在 symmetric case 写成 $\zeta_\alpha$。

$\delta$ 是 Levy noise 的 skewness parameter。Chapter 10 为了求 analytic solution 取 $\delta=0$，所以后面主要写 symmetric noise $\zeta_\alpha$。

$\beta$ 表示 migration shock amplitude 的 size exponent，即 noise amplitude 是 $D S^\beta$。它不是 Chapter 8 stable law 的 skewness parameter。

$\mu$ 只在 Srokowski generic equation 和 Fox H-function 推导中表示 generic Levy index。回到城市方程时要替换：

$$
\mu\to\alpha.
$$

$\zeta(t)$、$d\zeta$、$\zeta_\alpha$ 是同一类 Levy noise 的不同写法：$\zeta(t)$ 强调 white-noise process，$d\zeta$ 强调小时间步的 increment，$\zeta_\alpha$ 强调它的 stable index。

$\eta$ 是 out-of-system Gaussian growth noise；把它近似为 $r$ 后，$rS$ 是 deterministic proportional drift。

---

## 二、Eq. 10.1 到 Eq. 10.2：从真实 balance equation 到 decoupled growth equation

作者先回到 Chapter 9 的一般 balance equation：

$$
\frac{\partial S_i}{\partial t}
=
\eta_iS_i
+
\sum_{j\in N(i)}
\left(
J_{j\to i}
-
J_{i\to j}
\right).
\tag{10.1}
$$

这条方程有两个部分。

第一部分是 out-of-system growth：

$$
\eta_iS_i.
$$

这里 $\eta_i$ 是 Gaussian white noise。它代表 natural growth、outside migration 和 hinterland exchange 的合并效果。

第二部分是 interurban migration balance：

$$
\sum_{j\in N(i)}
\left(
J_{j\to i}
-
J_{i\to j}
\right).
$$

它是城市 $i$ 从所有邻居城市获得的净迁移流。

Chapter 9 已经说明，平均意义上：

$$
\mathbb{E}
\left[
\sum_{j\in N(i)}
\left(
J_{j\to i}
-
J_{i\to j}
\right)
\right]
=0.
$$

这就是 average detailed balance。它表示平均流入和平均流出抵消，所以大城市在平均意义上并没有无条件吸引所有人口。

但这个平均值不能代表真实 dynamics。原因是 migration balance 的 fluctuations 很大。作者把：

$$
X_i
=
\sum_{j\in N(i)}
\left(
J_{j\to i}
-
J_{i\to j}
\right)
$$

看成一个随机变量。虽然它的平均值接近 0，但它的波动不是小的 Gaussian residual，而是 heavy-tailed shocks。

这就是为什么不能回到 Gibrat formalism。如果只保留平均值，就会把 interurban migration 的差异全部抹掉。但这些差异恰恰包含城市的设施、创新能力、吸引力、历史事件和区域冲击。

Chapter 9 将 Eq. 10.1 empirical simplification 成：

$$
\frac{\partial S}{\partial t}
=
\eta S
+
D S^\beta \zeta_{\alpha,\delta}.
\tag{10.2}
$$

这里：

$$
\eta
$$

是 Gaussian noise，有 mean $r$ 和 variance $\sigma^2$；

$$
\zeta_{\alpha,\delta}
$$

是 Levy white noise，$\alpha$ 是 stability index，$\delta$ 是 skewness；

$$
D
$$

是 migration noise amplitude 的 prefactor；

$$
\beta<1
$$

描述 migration shock amplitude 如何随 city size 增长。

Eq. 10.2 比 Eq. 10.1 简单，因为它把城市之间显式耦合的高维系统变成了单个城市的 decoupled stochastic equation。城市 $S$ 的未来只依赖当前 $S$ 和两个 noise terms。

但它仍然不是普通 Gibrat equation。Gibrat 只有 Gaussian proportional noise；Eq. 10.2 多了一个 state-dependent Levy noise。

---

## 三、为什么可以把 $\eta S$ 近似成 $rS$

这一节回答 Chapter 10 的第一个简化：为什么可以从 two-noise equation 变成 one-noise equation。

Eq. 10.2 有两个 stochastic terms：

$$
\eta S
\quad
\text{and}
\quad
D S^\beta\zeta_{\alpha,\delta}.
$$

其中 $\eta$ 是 Gaussian noise，$\zeta$ 是 Levy noise。

作者的判断是：如果这两项的量级相近，那么真正支配 tail 和大波动的是 Levy noise，而不是 Gaussian noise。原因是 Gaussian noise 的波动被 finite variance 限制，极端事件概率下降很快；Levy noise 有 broad tail，rare large shocks 会更频繁出现。

因此，可以把 Gaussian noise 近似为它的均值：

$$
\eta S
\simeq
rS.
\tag{10.3}
$$

这里 $r=\langle\eta\rangle$ 是平均增长率。

代入 Eq. 10.2，得到一噪声方程：

$$
\frac{\partial S}{\partial t}
=
rS
+
D S^\beta\zeta_{\alpha,\delta}.
\tag{10.4}
$$

这一步的含义不是说 out-of-system growth 不重要，而是说它的 random fluctuation 相对于 Levy migration fluctuation 是 subdominant 的。因此 out-of-system growth 主要提供 deterministic drift：

$$
\text{average exponential growth}.
$$

Fig. 10.1 用 numerical simulation 支撑这个简化。

![Fig. 10.1](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-03-figure-01.jpg)

图中灰线是保留 Gaussian noise $\eta\sim\mathrm{Normal}(r,\sigma^2)$ 的模拟结果，黑线是把 $\eta$ 固定为 $r$ 的模拟结果。两条 population density 曲线几乎重合，说明对于 population distribution 来说，保留 $\eta$ 的 Gaussian fluctuation 和只保留平均 drift 差异不大。

作者还进一步假设 Levy noise 的 skewness：

$$
\delta=0.
$$

这不是说经验 skewness 必须为 0，而是为了得到 analytic solution。于是 Eq. 10.4 进一步变成三参数问题：

$$
(r,\beta,\alpha).
$$

这个简化后的问题仍然保留核心机制：

$$
\text{deterministic proportional growth}
+
\text{multiplicative Levy migration shocks}.
$$

---

## 四、Eq. 10.5 到 Eq. 10.6：Levy SDE 对应 fractional Fokker-Planck

作者接下来聚焦于：

$$
\partial_t S
=
rS
+
D S^\beta\zeta_\alpha.
\tag{10.5}
$$

这是 Chapter 10 的基础方程。这里的 $\alpha$ 仍然是 Chapter 9 估计出的 migration-shock tail exponent。后面进入通用 fractional equation 时会临时改用 $\mu$，但回到城市方程时总是令 $\mu=\alpha$。Eq. 10.5 对应一个 Itô interpretation 下的 fractional Fokker-Planck equation：

$$
\partial_tP(S,t)
=
-
\partial_S
\left(
rSP(S,t)
\right)
+
D^\alpha
\frac{\partial^\alpha}{\partial S^\alpha}
\left(
P(S,t)S^{\alpha\beta}
\right).
\tag{10.6}
$$

这条式子要分两项读。

第一项：

$$
-
\partial_S(rSP)
$$

是 deterministic drift 的 probability flux。因为 $rS$ 把 population 向更大 $S$ 推，所以 probability density 会沿 $S$ 方向移动。

第二项：

$$
D^\alpha
\frac{\partial^\alpha}{\partial S^\alpha}
\left(
P(S,t)S^{\alpha\beta}
\right)
$$

是 Levy noise 产生的 fractional diffusion。

普通 Brownian noise 会给二阶导数：

$$
\partial_S^2(\cdots).
$$

Levy noise 的 characteristic function 有：

$$
|k|^\alpha
$$

而不是 $k^2$，所以在 real space 里对应 fractional derivative：

$$
\frac{\partial^\alpha}{\partial S^\alpha}.
$$

此外，noise amplitude 是：

$$
D S^\beta.
$$

对 $\alpha$-stable noise，amplitude 会以 $\alpha$ 次幂进入 generator：

$$
(DS^\beta)^\alpha
=
D^\alpha S^{\alpha\beta}.
$$

所以 Eq. 10.6 中的 fractional diffusion coefficient 是：

$$
D^\alpha S^{\alpha\beta}.
$$

这就是为什么 Eq. 10.6 的扩散项写成：

$$
D^\alpha
\partial_S^\alpha
\left(
S^{\alpha\beta}P
\right).
$$

---

## 五、Eq. 10.7 到 Eq. 10.17：fractional Fokker-Planck 的推导逻辑

这一节展开作者给出的 derivation sketch。为了避免符号混乱，作者暂时把 population variable 写成 $x$，并把 generic $x$-space density 写成小写 $p$：

$$
p(x,t)=p(x,t\mid x_0,0).
$$

它表示从初始人口 $x_0$ 出发，在时间 $t$ 观察到 population size $x$ 的 probability density。

### 5.1 Eq. 10.7-Eq. 10.8：从 observable average 开始

考虑任意函数或 functional $R(x)$。它的 expectation 是：

$$
\langle R\rangle
=
\int dx\,R(x)p(x,t).
\tag{10.7}
$$

对时间求导：

$$
\frac{d}{dt}\langle R\rangle
=
\int dx\,R(x)\partial_t p(x,t).
\tag{10.8}
$$

这条式子把 distribution evolution $\partial_t p$ 和 observable average 的变化联系起来。

后面的策略是：从 stochastic equation 直接算 $\langle dR/dt\rangle$，再和 Eq. 10.8 对比。这里的逻辑可以按 weak form 来读。

首先，$p(x,t)$ 本身是一个 density，直接写它的 evolution 有时不方便。更稳的做法是先看任意 observable $R(x)$ 的平均值如何变化：

$$
\langle R\rangle
=
\int dx\,R(x)p(x,t).
$$

如果我们知道所有 $R(x)$ 的平均值随时间怎样变化，就等价于知道整个 distribution 怎样变化。原因是一个概率分布不是只由均值或方差决定，而是由它对所有 test functions 的积分作用决定。

Eq. 10.8 从 distribution side 给出：

$$
\frac{d}{dt}\langle R\rangle
=
\int dx\,R(x)\partial_t p(x,t).
$$

另一边，stochastic equation 给出 sample path 的小时间变化：

$$
x(t)
\rightarrow
x(t+dt).
$$

因此同一个 observable 的变化也可以从 trajectory side 计算：

$$
\left\langle
\frac{dR}{dt}
\right\rangle
=
\left\langle
\frac{
R(x(t+dt))-R(x(t))
}{dt}
\right\rangle.
$$

这一步会把 drift term 和 Levy noise term 的贡献都算出来，得到一个形如：

$$
\left\langle
\frac{dR}{dt}
\right\rangle
=
\int dx\,p(x,t)\,\mathcal{L}R(x)
$$

的表达式。这里 $\mathcal{L}$ 是 stochastic process 作用在 test function 上的 generator。

然后把它和 Eq. 10.8 对齐：

$$
\int dx\,R(x)\partial_t p(x,t)
=
\int dx\,p(x,t)\,\mathcal{L}R(x).
$$

最后通过 integration by parts 或 Fourier transform，把右边的 operator 从 $R$ 上转移到 $p$ 上：

$$
\int dx\,p(x,t)\,\mathcal{L}R(x)
=
\int dx\,R(x)\,\mathcal{L}^{\dagger}p(x,t).
$$

由于这个等式对任意 test function $R(x)$ 都成立，只能有：

$$
\partial_t p(x,t)
=
\mathcal{L}^{\dagger}p(x,t).
$$

这就是 Fokker-Planck equation 的推导方式。它不是先猜 $\partial_t p$，而是先从 stochastic equation 算 observable 的平均变化，再把 generator 的 adjoint 读成 density 的演化方程。

### 5.2 Eq. 10.9-Eq. 10.11：把 $R(x(t+dt))-R(x(t))$ 写到 Fourier space

定义：

$$
dR
=
R(x(t+dt))-R(x(t)).
\tag{10.9}
$$

把 $R$ 写成 Fourier representation：

$$
R(x)
=
\int dk\,R(k)e^{ikx}.
$$

那么：

$$
dR
=
\int dk\,R(k)
\left(
e^{ikx(t+dt)}
-
e^{ikx(t)}
\right).
$$

这条式子是 single trajectory 上的变化，还没有对随机初始位置和 noise 做平均，所以不应该出现 $p(x,t)$。

接下来要算的是 ensemble average。若在时刻 $t$，随机变量 $x(t)$ 的 density 是 $p(x,t)$，那么对所有可能的当前状态 $x$ 加权平均，就得到：

$$
\langle dR\rangle
=
\int dx\,p(x,t)
\int dk\,R(k)
\left(
e^{ikx(t+dt)}
-
e^{ikx}
\right).
\tag{10.10}
$$

这里的 $p(x,t)$ 不是额外的动力学项，而是 averaging measure。它表示：在计算 $\langle dR\rangle$ 时，当前状态 $x$ 出现的概率密度是多少。

由 Eq. 10.5，在一个小时间步里：

$$
x(t+dt)
=
x
+
rx\,dt
+
Dx^\beta d\zeta.
$$

代入指数：

$$
e^{ikx(t+dt)}
=
e^{ikx}
e^{ik(rx\,dt+Dx^\beta d\zeta)}.
$$

所以：

$$
\langle dR\rangle
=
\int dx\,p(x,t)
\int dk\,R(k)e^{ikx}
\left[
e^{ik(rx\,dt+Dx^\beta d\zeta)}
-1
\right].
\tag{10.11}
$$

这一步的作用是把 stochastic increment $d\zeta$ 放进 characteristic function 里。后面还要对 $d\zeta$ 做 noise average，这样才能直接利用 Levy noise 的 characteristic exponent。

### 5.3 Eq. 10.12：Levy increment 的 characteristic function

对 Levy noise 平均，作者使用：

$$
\left\langle
e^{ikDx^\beta d\zeta}
\right\rangle
=
\exp
\left[
-
(Dx^\beta)^\alpha
|k|^\alpha dt
\right].
\tag{10.12}
$$

这条式子来自 symmetric $\alpha$-stable increment 的 characteristic function。对小时间步 $dt$，Levy increment 的 exponent 和 $dt$ 成正比。

这里的关键是：

$$
(Dx^\beta)^\alpha|k|^\alpha
=
D^\alpha x^{\alpha\beta}|k|^\alpha.
$$

这正是 fractional Fokker-Planck 中 $D^\alpha x^{\alpha\beta}$ 的来源。

### 5.4 Eq. 10.13-Eq. 10.15：展开到一阶 $dt$

对 Eq. 10.11 的括号做一阶 $dt$ 展开。

drift 部分给：

$$
e^{ikrx\,dt}
\simeq
1+ikrx\,dt.
$$

Levy noise 平均给：

$$
e^{-D^\alpha x^{\alpha\beta}|k|^\alpha dt}
\simeq
1
-
D^\alpha x^{\alpha\beta}|k|^\alpha dt.
$$

保留一阶项，得到：

$$
\left\langle
\frac{dR}{dt}
\right\rangle
=
\int dx\,p(x,t)
\int dk\,R(k)e^{ikx}
\left[
ikxr
-
D^\alpha x^{\alpha\beta}|k|^\alpha
\right].
\tag{10.13}
$$

把两部分拆开：

$$
\left\langle
\frac{dR}{dt}
\right\rangle
=
\int dx\,p(x,t)rx
\int dk\,R(k)e^{ikx}ik
-
\int dx\,p(x,t)D^\alpha x^{\alpha\beta}
\int dk\,R(k)e^{ikx}|k|^\alpha.
\tag{10.14}
$$

第一段 Fourier integral 是 ordinary derivative：

$$
\int dk\,R(k)e^{ikx}ik
=
\frac{dR}{dx}.
$$

第二段 Fourier integral 对应 fractional derivative。Riesz-type fractional derivative 在 Fourier space 中乘以 $-|k|^\alpha$。按作者符号，可以写成：

$$
\int dk\,R(k)e^{ikx}|k|^\alpha
\quad
\leftrightarrow
\quad
\frac{d^\alpha R}{d|x|^\alpha}.
$$

于是：

$$
\left\langle
\frac{dR}{dt}
\right\rangle
=
\int dx\,p(x,t)rx\frac{dR}{dx}
-
\int dx\,p(x,t)D^\alpha x^{\alpha\beta}
\frac{d^\alpha R}{d|x|^\alpha}.
\tag{10.15}
$$

这条式子是 generator acting on observables 的形式。

### 5.5 Eq. 10.16-Eq. 10.17：从 observable generator 转到 density equation

为了得到 density evolution，需要把 derivative 从 $R$ 转移到 $p$ 上，也就是做 adjoint operation。

ordinary drift term：

$$
\int dx\,p\,rx\,\partial_xR
$$

对应 density 方程中的：

$$
-
\partial_x(rxp).
$$

fractional derivative term：

$$
-
\int dx\,p\,D^\alpha x^{\alpha\beta}
\frac{d^\alpha R}{d|x|^\alpha}
$$

对应 density 方程中的：

$$
D^\alpha
\frac{\partial^\alpha}{\partial|x|^\alpha}
\left(
x^{\alpha\beta}p
\right).
$$

所以得到：

$$
\partial_t p(x,t)
=
-
\frac{\partial}{\partial x}
\left(
rxp(x,t)
\right)
+
D^\alpha
\frac{\partial^\alpha}{\partial|x|^\alpha}
\left(
x^{\alpha\beta}p(x,t)
\right).
\tag{10.16}
$$

把变量从 $x$ 换回 population $S$，得到：

$$
\partial_tP(S,t)
=
-
\partial_S
\left(
rSP(S,t)
\right)
+
D^\alpha
\frac{\partial^\alpha}{\partial S^\alpha}
\left(
P(S,t)S^{\alpha\beta}
\right).
\tag{10.17}
$$

这就是 Eq. 10.5 对应的 fractional Fokker-Planck equation。

---

## 六、Eq. 10.18：如果不把 Gaussian noise 删掉，会多出什么项

作者接着说明，若不做：

$$
\eta\simeq r
$$

的近似，而保留 Gaussian fluctuation with variance $\sigma^2$，则 Fokker-Planck equation 会多出 ordinary diffusion term：

$$
\partial_tP(S,t)
=
-
\partial_S(rSP)
+
\sigma^2
\frac{\partial^2}{\partial S^2}
\left(
S^2P(S,t)
\right)
+
D^\alpha
\frac{\partial^\alpha}{\partial S^\alpha}
\left(
S^{\alpha\beta}P(S,t)
\right).
\tag{10.18}
$$

这条式子有三部分。

第一，deterministic drift：

$$
-
\partial_S(rSP).
$$

第二，Gaussian multiplicative diffusion：

$$
\sigma^2
\partial_S^2(S^2P).
$$

第三，Levy fractional diffusion：

$$
D^\alpha
\partial_S^\alpha(S^{\alpha\beta}P).
$$

为什么作者说 Gaussian fluctuation 是 subdominant？

在 Fourier space 中，Gaussian diffusion 对应：

$$
k^2.
$$

Levy diffusion 对应：

$$
|k|^\alpha.
$$

因为本章关心：

$$
\alpha<2,
$$

所以在 small-$k$ behavior 中：

$$
|k|^\alpha
\gg
k^2
\quad
(k\to0).
$$

small $k$ 对应 large-scale distribution behavior。因此在 long-range / tail behavior 上，Levy term 比 Gaussian term 更重要。

这解释了为什么 Eq. 10.4 的一噪声近似不仅是数值上可行，也有 Fourier-space 的尺度理由。

---

## 七、为什么要引入更一般的 fractional Fokker-Planck 解法

Eq. 10.17 不是普通 PDE，因为它含有：

$$
\frac{\partial^\alpha}{\partial S^\alpha}.
$$

而且这个 fractional derivative 还作用在 state-dependent coefficient 上：

$$
S^{\alpha\beta}P(S,t).
$$

因此不能像普通 Fokker-Planck 那样直接用 Gaussian kernel 求解。

作者转向 Srokowski 的一般形式：

$$
\dot{x}
=
F(x)
+
G(x)\zeta(t).
\tag{10.19}
$$

这里 $F(x)$ 是 deterministic force，$G(x)$ 是 state-dependent Levy noise amplitude，$\zeta(t)$ 是 exponent 为 $\mu$ 的 uncorrelated Levy noise。注意这里的 $\mu$ 是 generic notation；它不是 Chapter 9 gravity model 里的 origin-size exponent。回到城市方程时，$\mu$ 会被替换成 $\alpha$。

Itô interpretation 下，对应的 Fokker-Planck equation 是：

$$
\frac{\partial}{\partial t}p(x,t)
=
-
\frac{\partial}{\partial x}
\left(
F(x)p(x,t)
\right)
+
\frac{\partial^\mu}{\partial x^\mu}
\left[
G(x)^\mu p(x,t)
\right].
\tag{10.20}
$$

Riesz-Weyl fractional operator 在 Fourier space 中定义为：

$$
\frac{\partial^\mu}{\partial x^\mu}
=
\mathcal{F}^{-1}(-|k|^\mu).
\tag{10.21}
$$

这条定义非常重要。它说明 fractional derivative 不是普通整数阶求导，而是通过 Fourier multiplier $-|k|^\mu$ 定义的 nonlocal operator。

如果 $\mu=2$，它退回 ordinary second derivative。因为：

$$
-|k|^2=-k^2.
$$

如果 $0<\mu<2$，它描述 Levy jumps 的 nonlocal diffusion。

我们的城市方程对应：

$$
F(S)=rS,
\qquad
G(S)=DS^\beta,
\qquad
\mu=\alpha.
$$

---

## 八、Eq. 10.22 到 Eq. 10.26：force-free case 如何产生 Fox H-function

这一节不能孤立地读成“作者突然介绍一个特殊函数”。它在全章里的作用是搭桥。

前面已经得到城市方程的 fractional Fokker-Planck form，但这个方程很难直接求解。难点有两个。第一，扩散算子不是普通二阶导数，而是 fractional derivative。第二，扩散系数依赖状态变量，城市方程里是 $S^{\alpha\beta}$。

作者的处理策略不是一步到位求城市方程，而是先建立一个可控的解法模板：

$$
\begin{aligned}
&\text{additive Levy diffusion}\\
&\rightarrow \text{Levy stable density}\\
&\rightarrow \text{Fox H-function representation}\\
&\rightarrow \text{use Fox H-function identities}\\
&\rightarrow \text{handle state-dependent coefficient}\\
&\rightarrow \text{map back to city population }S.
\end{aligned}
$$

所以 Eq. 10.22-Eq. 10.26 的目的不是解释城市机制，而是回答一个技术问题：Levy stable density 应该用什么函数族来写，后面才能继续做 asymptotic expansion。

作者先处理更简单的 force-free case：

$$
F(x)=0.
$$

设 power-law diffusion coefficient：

$$
G(x)=|x|^{-\theta/\mu}.
$$

则：

$$
G(x)^\mu
=
|x|^{-\theta}.
$$

Eq. 10.20 变为：

$$
\frac{\partial p(x,t)}{\partial t}
=
\frac{\partial^\mu}{\partial|x|^\mu}
\left[
|x|^{-\theta}p(x,t)
\right].
\tag{10.22}
$$

Fourier space 中：

$$
\frac{\partial p(k,t)}{\partial t}
=
-
|k|^\mu
\mathcal{F}
\left[
|x|^{-\theta}p(x,t)
\right].
\tag{10.23}
$$

先看 $\theta=0$。这时 diffusion coefficient 不依赖 $x$，Eq. 10.23 简化为：

$$
\frac{\partial p(k,t)}{\partial t}
=
-
|k|^\mu p(k,t).
$$

解为：

$$
p(k,t)
=
e^{-|k|^\mu t}.
\tag{10.24}
$$

回到 real space：

$$
p(x,t)
\propto
\int dk\,
e^{ikx-|k|^\mu t}.
\tag{10.25}
$$

这就是 symmetric Levy stable density 的 inverse Fourier transform。

这里出现第一个关键转折。一般 Levy stable density 很少有初等函数形式。除了 Gaussian、Cauchy、one-sided Levy 这些 special cases，多数 stable densities 不能写成简单的 $e^{-x^2}$ 或 $1/(1+x^2)$。但它们可以统一写成 Fox H-function。

也就是说，Fox H-function 在这里不是新的物理假设，而是一种函数表示法。它的作用是把 inverse Fourier transform 的结果放进一个封闭的函数族里：

$$
p(x,t)
=
\frac{1}{\mu|x|}
H_{2,2}^{1,1}
\left[
\frac{|x|}{(K^\mu t)^{1/\mu}}
\left|
\begin{array}{l}
(1,1/\mu),(1,1/2)\\
(1,1),(1,1/2)
\end{array}
\right.
\right].
\tag{10.26}
$$

这样做的好处是：一旦 density 写成 Fox H-function，后面就可以利用这个函数族的变换性质来处理更复杂的 $G(x)$ 和 large-$x$ asymptotics。换句话说，Eq. 10.26 是后面求尾部分布的技术入口。

---

## 九、Eq. 10.27 到 Eq. 10.31：Fox H-function 在这里承担什么角色

上一节说明了 Fox H-function 从哪里来：它是 Levy stable density 的统一表示。接下来还要说明为什么它有用。

对城市问题来说，我们最终不只是要写出一个 formal solution，而是要读出 large-$S$ tail。为此需要三类操作：把小变量和大变量互相转换、把 power-law coefficient 乘进解里、把 Fourier space 和 real space 来回变换。Fox H-function 的价值就在于它对这些操作封闭。

作者因此给出 Fox H-function 的定义：

$$
H_{pq}^{mn}
\left[
z
\left|
\begin{array}{c}
(a_1,A_1),(a_2,A_2),\ldots,(a_p,A_p)\\
(b_1,B_1),(b_2,B_2),\ldots,(b_q,B_q)
\end{array}
\right.
\right]
=
\frac{1}{2\pi i}
\int_L
\chi(s)z^sds.
\tag{10.27}
$$

其中：

$$
\chi(s)
=
\frac{
\prod_1^m\Gamma(b_j-B_js)
\prod_1^n\Gamma(1-a_j+A_js)
}{
\prod_{m+1}^q\Gamma(1-b_j+B_js)
\prod_{n+1}^p\Gamma(a_j-A_js)
}.
\tag{10.28}
$$

这一定义本身比较技术。对本章来说，关键不是记住所有参数，而是理解 Fox H-function 有三个有用性质。

第一，它有 $z\leftrightarrow1/z$ 的 duality：

$$
H_{pq}^{mn}
\left[
z
\left|
\begin{array}{l}
(a_p,A_p)\\
(b_q,B_q)
\end{array}
\right.
\right]
=
H_{pq}^{mn}
\left[
\frac{1}{z}
\left|
\begin{array}{l}
(1-b_q,B_q)\\
(1-a_p,A_p)
\end{array}
\right.
\right].
\tag{10.29}
$$

这使得 small-$z$ 和 large-$z$ behavior 可以互相转换。

第二，乘上一个幂 $z^\sigma$ 仍然得到 Fox H-function，只是参数平移：

$$
z^\sigma
H_{pq}^{mn}
\left[
z
\left|
\begin{array}{l}
(a_p,A_p)\\
(b_q,B_q)
\end{array}
\right.
\right]
=
H_{pq}^{mn}
\left[
z
\left|
\begin{array}{l}
(a_p+\sigma A_p,A_p)\\
(b_q+\sigma B_q,B_q)
\end{array}
\right.
\right].
\tag{10.30}
$$

这条性质对 Eq. 10.22 很关键，因为 equation 中有：

$$
|x|^{-\theta}p(x,t).
$$

如果 $p$ 是 Fox H-function，乘上 $|x|^{-\theta}$ 之后仍然可以保留 Fox H-function form。

第三，Fox H-function 的 cosine Fourier transform 还是 Fox H-function：

$$
\int_0^\infty
H_{pq}^{mn}
\left[
x
\left|
\begin{array}{l}
(a_p,A_p)\\
(b_q,B_q)
\end{array}
\right.
\right]
\cos(kx)\,dx
=
\frac{\pi}{k}
H_{q+1,p+2}^{n+1,m}
\left[
k
\left|
\begin{array}{l}
(1-b_q,B_q),(1,1/2)\\
(1,1),(1-a_p,A_p),(1,1/2)
\end{array}
\right.
\right].
\tag{10.31}
$$

这条性质说明：Fox H-function family 在 Fourier transform 下封闭。因此它适合解 fractional Fokker-Planck equation。

总结这一段，Fox H-function 在本章不是解释性机制，而是技术工具。它的作用是让具有 fractional derivative 和 power-law coefficient 的方程仍然可以写出 asymptotic solution。

---

## 十、Eq. 10.32 到 Eq. 10.34：Itô force-free case 的 large-tail 解

回到 Eq. 10.22，当 $\theta\neq0$ 时，作者寻找如下形式的解：

$$
p(x,t)
=
Na
H_{2,2}^{1,1}
\left[
a|x|
\left|
\begin{array}{l}
(a_1,A_1),(a_2,A_2)\\
(b_1,B_1),(b_2,B_2)
\end{array}
\right.
\right].
\tag{10.32}
$$

这里 $a=a(t)$ 是 time-dependent scale，$N$ 是 normalization constant。参数通过把这个 ansatz 代入 Eq. 10.23，并比较 small-$k$ expansion 来确定。

得到的 large-$x$ 解可以写成：

$$
p(x,t)
=
Na
H_{2,2}^{1,1}
\left[
a|x|
\left|
\begin{array}{l}
\left(1-\frac{1-\theta}{\mu+\theta},\frac{1}{\mu+\theta}\right),
\left(1-\frac{1-\theta}{2+\theta},\frac{1}{2+\theta}\right)\\
(b_1,B_1),
\left(1-\frac{1-\theta}{2+\theta},\frac{1}{2+\theta}\right)
\end{array}
\right.
\right].
\tag{10.33}
$$

真正重要的是它的 asymptotic behavior：

$$
p(x,t)
\sim
\frac{
t^{\mu/(\mu+\theta)}
}{
|x|^{1+\mu}
}.
\tag{10.34}
$$

这一结果有一个关键含义：在 Itô prescription 下，tail exponent 是：

$$
1+\mu.
$$

它只由 Levy noise index $\mu$ 控制，不依赖 $\theta$。

这点对城市方程非常重要，因为作者在 Chapter 9 已经倾向 Itô interpretation。若采用 Itô，population distribution 的 far tail 主要继承 Levy noise 的 tail。

---

## 十一、Eq. 10.35 到 Eq. 10.39：Stratonovich case 为什么不同

作者随后比较 Stratonovich interpretation。

在 Stratonovich prescription 中，可以做变量变换：

$$
y(x)
=
\frac{\mu}{\mu+\theta}
|x|^{(\mu+\theta)/\mu}
\operatorname{sgn}(x).
\tag{10.35}
$$

这个变换的目的，是把 multiplicative noise 变成 additive noise。

变换后，Fokker-Planck equation 变成：

$$
\frac{\partial}{\partial t}p_S(y,t)
=
\frac{\partial^\mu}{\partial|y|^\mu}
p_S(y,t).
\tag{10.36}
$$

这就是 additive Levy noise 的标准 fractional diffusion equation。

它的解为：

$$
p_S(y,t)
=
\frac{1}{\mu|y|}
H_{2,2}^{1,1}
\left[
\frac{|y|}{t^{1/\mu}}
\left|
\begin{array}{c}
(1,1/\mu),(1,1/2)\\
(1,1),(1,1/2)
\end{array}
\right.
\right].
\tag{10.37}
$$

再变回 $x$，得到：

$$
p_S(x,t)
=
\frac{\mu+\theta}{\mu^2|x|}
H_{2,2}^{1,1}
\left[
\frac{|x|^{1+\theta/\mu}}
{(1+\theta/\mu)t^{1/\mu}}
\left|
\begin{array}{c}
(1,1/\mu),(1,1/2)\\
(1,1),(1,1/2)
\end{array}
\right.
\right].
\tag{10.38}
$$

Stratonovich case 的 asymptotic behavior 是：

$$
p_S(x,t)
\sim
\frac{
t^{\mu/(\mu+\theta)}
}{
|x|^{1+\mu+\theta}
}.
\tag{10.39}
$$

这和 Itô case 不同。

Itô:

$$
p(x,t)\sim |x|^{-1-\mu}.
$$

Stratonovich:

$$
p_S(x,t)\sim |x|^{-1-\mu-\theta}.
$$

也就是说，在 Stratonovich interpretation 中，state-dependent noise coefficient 会改变 tail exponent；在 Itô interpretation 中，tail exponent 主要由 Levy noise itself 控制。

这段比较再次说明：multiplicative Levy noise 的 stochastic prescription 不是形式细节，而会改变最终 distribution tail。

---

## 十二、Eq. 10.40 到 Eq. 10.44：加入 linear force

为了更接近城市方程，作者继续考虑有 linear force 的情形：

$$
F(x)=-\lambda x.
$$

Itô Fokker-Planck equation 变成：

$$
\frac{\partial}{\partial t}p(x,t)
=
\lambda
\frac{\partial}{\partial x}
\left[
xp(x,t)
\right]
+
\frac{\partial^\mu}{\partial|x|^\mu}
\left[
|x|^{-\theta}p(x,t)
\right].
\tag{10.40}
$$

对应 Fourier transform：

$$
\frac{\partial}{\partial t}p(k,t)
=
-
\lambda k
\frac{\partial}{\partial k}p(k,t)
-
|k|^\mu
\mathcal{F}_c
\left[
|x|^{-\theta}p(x,t)
\right].
\tag{10.41}
$$

这个方程仍然用 Fox H-function ansatz 来解。把 Eq. 10.32 形式代入，并比较 small-$k$ expansion。比较 $|k|^\mu$ 阶项，会得到 $a(t)$ 的 differential equation，其解是：

$$
a(t)
=
\left[
\frac{\lambda/c_L}
{1-\exp[-\lambda(\mu+\theta)t]}
\right]^{1/(\mu+\theta)}.
\tag{10.42}
$$

这里 $c_L$ 是由 normalization 和参数决定的常数。

large-$|x|$ expansion 为：

$$
p(x,t)
=
N
\frac{\mu+\theta}{|x|}
\sum_{i=0}^{\infty}
C_i
\left(
a(t)|x|
\right)^{\theta-(\mu+\theta)i}.
\tag{10.43}
$$

这个展开式后面会被用来写城市 population distribution 的 large-$S$ asymptotic expansion。

作者还给出 Stratonovich prescription 下的 exact solution：

$$
p_S(x,t)
=
\frac{\mu+\theta}{\mu^2|x|}
H_{2,2}^{1,1}
\left[
\begin{array}{cc}
|x|^{1+\theta/\mu} &
(1,1/\mu),(1,1/2)\\
\hline
(1+\theta/\mu)K\sigma^{1/\mu} &
(1,1),(1,1/2)
\end{array}
\right].
\tag{10.44}
$$

对本章主线来说，Eq. 10.40-Eq. 10.44 的作用是建立一个可迁移模板。城市方程可以通过参数替换映射到这个 linear-force fractional Fokker-Planck problem。

---

## 十三、Eq. 10.45 到 Eq. 10.47：城市 population distribution 的 large-$S$ expansion

现在回到城市方程的 Fokker-Planck equation：

$$
\partial_tP(S,t)
=
-
\partial_S(rSP)
+
D^\alpha
\frac{\partial^\alpha}{\partial S^\alpha}
\left(
S^{\alpha\beta}P
\right).
$$

它可以从上一节的 general solution 通过参数替换得到：

$$
\lambda\to-r,
\qquad
\mu\to\alpha,
\qquad
\theta\to-\alpha\beta.
$$

为什么 $\theta\to-\alpha\beta$？

Srokowski 的系数是：

$$
|x|^{-\theta}.
$$

城市方程的系数是：

$$
S^{\alpha\beta}.
$$

所以：

$$
-\theta=\alpha\beta
\quad
\Rightarrow
\quad
\theta=-\alpha\beta.
$$

由此得到 large-$S$ expansion：

$$
P(S,t)
=
N\alpha(1-\beta)
\sum_{k=1}^{\infty}
C_k
\frac{
a(t)^{-\alpha\beta-\alpha(1-\beta)k}
}{
|S|^{1+\alpha\beta+\alpha(1-\beta)k}
}.
\tag{10.45}
$$

这个展开式值得线性读。

每个 $k$ 对应一个 power-law term。第 $k$ 项的 $S$ 幂指数是：

$$
1+\alpha\beta+\alpha(1-\beta)k.
$$

当 $k=1$ 时，指数为：

$$
1+\alpha\beta+\alpha(1-\beta)
=
1+\alpha.
$$

所以 large-$S$ tail 的 leading term 是：

$$
P(S,t)
\sim
S^{-1-\alpha}.
$$

这就是为什么作者说 large-$S$ limit 会趋向 Pareto distribution with exponent $\alpha$。注意这里 density exponent 是 $1+\alpha$，对应 cumulative tail exponent $\alpha$。

系数 $C_k$ 为：

$$
C_k
=
\frac{
(-1)^k
\Gamma(1+\alpha(1-\beta)k)
}{
\Gamma\left(
a_2+A_2(1+\alpha\beta+\alpha(1-\beta)k)
\right)
\Gamma\left(
-
\frac{\alpha-\alpha\beta}{2-\alpha\beta}
\right)
k!
}.
\tag{10.46}
$$

这些系数主要控制各阶 correction 的权重。对理解主线来说，最重要的是它们让 Eq. 10.45 不只是单一 power law，而是一个 power-law series。

time-dependent factor 是：

$$
a(t)
=
\left(
\frac{
r/c_L
}{
\exp[r\alpha(1-\beta)t]-1
}
\right)^{1/[\alpha(1-\beta)]}.
\tag{10.47}
$$

其中：

$$
c_L\propto D^\alpha.
$$

$a(t)$ 控制不同时间下 distribution 的尺度。随着 $t$ 变化，Eq. 10.45 的各阶项权重会发生变化，因此系统不会一开始就处在 stationary Pareto regime。

---

## 十四、Eq. 10.48 到 Eq. 10.49：为什么真正的 power-law regime 很难观察

Eq. 10.45 的 leading term 是 $k=1$，它给出：

$$
P(S,t)\sim S^{-1-\alpha}.
$$

如果只看这一项，似乎模型会给出一个 Pareto tail。

但作者强调：真实分布能否表现为这个 leading power law，取决于 higher-order terms 是否已经足够小。

他们用 first term 和 second term 的 ratio 来估计 convergence speed：

$$
\lambda(S,t)
\propto
a(t)^{-\alpha(1-\beta)}
S^{-\alpha(1-\beta)}
\sim
\frac{r}{D^\alpha}
\left(
\frac{e^{rt}}{S}
\right)^{\alpha(1-\beta)}.
\tag{10.48}
$$

这里 $\lambda(S,t)\ll1$ 表示 higher-order corrections 足够小，leading power-law term 支配 distribution。

问题在于，经验上：

$$
\beta\approx0.8,
\qquad
\alpha\approx1.3\text{ to }1.7.
$$

于是：

$$
\alpha(1-\beta)
\approx0.2.
$$

这个 exponent 很小。小 exponent 会让 convergence 非常慢，因为：

$$
\left(
\frac{e^{rt}}{S}
\right)^{0.2}
$$

只有在 $S$ 极大时才会很小。

作者估计 power-law equilibrium 条件大致变成：

$$
\left(
\frac{e^{rt}}{S}
\right)^{\alpha(1-\beta)}
\ll1
\quad
\Longleftrightarrow
\quad
S>10^5\overline{S(t)}.
\tag{10.49}
$$

这意味着，要真正观察到 asymptotic Pareto regime，城市规模可能需要比平均城市规模大 $10^5$ 倍。现实中这种范围通常不存在。

所以这节的结论很关键：

$$
\text{the model has a Pareto asymptotic tail}
\neq
\text{empirical city systems should visibly obey Zipf}.
$$

这直接回应 Chapter 3 的问题。Zipf-like fit 可能出现在有限区间，但真正 stationary power-law regime 通常未达到。

---

## 十五、Eq. 10.50：如果不能验证完整解，至少能验证 scaling collapse

作者承认，Eq. 10.45 是一个 time-dependent solution，但实际数据通常缺少完整 initial condition，因此很难直接验证某一时刻的完整 distribution。

不过 Eq. 10.45 预言一个更稳健的 scaling relation：

$$
P(S,t)
=
\frac{1}{S}
F_{\alpha,\beta}
\left(
\frac{S}{\overline{S(t)}}
\right).
\tag{10.50}
$$

这里：

$$
\overline{S(t)}
$$

是时间 $t$ 的平均城市规模；

$$
F_{\alpha,\beta}
$$

是依赖系统参数的 scaling function。

这条式子说：如果把横轴从 $S$ 改成 relative size：

$$
\frac{S}{\overline{S(t)}},
$$

并看：

$$
SP(S,t),
$$

不同年份的分布应该 collapse 到同一条 universal curve 上。

Fig. 10.2 用法国 1876-2015 年 500 个最大城市的数据验证这个关系。

![Fig. 10.2](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-10-figure-01.jpg)

图中不同颜色代表不同年份。它们在 $S/\overline{S(t)}$ 标准化后大体 collapse，说明虽然完整 distribution 随时间移动，但形状在相对尺度上具有稳定 scaling。

作者把这个 scaling curve 分成三个 regimes。

第一，当：

$$
S\ll\overline{S(t)}
$$

时，是 growing regime。

第二，当：

$$
S\sim\overline{S(t)}
$$

时，有近似：

$$
P(S,t)\sim\frac{1}{S}.
$$

第三，当：

$$
S\gg\overline{S(t)}
$$

时，upper tail 逐渐向：

$$
P(S,t)\sim\frac{1}{S^{1+\alpha}}
$$

收敛，但 convergence 很慢。

这就是为什么 empirical city-size distribution 可能在中间区间看起来像 Zipf，而在真正 tail 处又偏离。有限数据区间中的 apparent exponent 不一定等于 asymptotic exponent。

---

## 十六、Fig. 10.3：为什么 naive power-law fitting 会误导

作者进一步说明，如果把 Eq. 10.45 的 finite-time distribution 强行拟合成 power law，会得到很高的 $R^2$，但 exponent 会随 cutoff 改变。

Fig. 10.3 展示 apparent exponent $\alpha(S_{\min})$ 随 minimal threshold $S_{\min}$ 变化。

![Fig. 10.3](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-11-figure-01.jpg)

图中灰色水平线是 true $\alpha=1.3$，黑色点划线是用 $S>S_{\min}$ 拟合得到的 apparent exponent，虚线表示拟合质量 $R^2$。

关键现象是：$R^2$ 可以接近 1，但 apparent exponent 仍然明显低于 true $\alpha$，并且随 $S_{\min}$ 增大缓慢接近 1.3。

这说明一个重要方法论问题：

$$
\text{good power-law fit}
\not\Rightarrow
\text{true power-law regime}.
$$

如果 distribution 是多项 power-law expansion 的 finite-time 形态，简单地在一个截断区间上拟合直线，可能会产生看似可靠但依赖 threshold 的 exponent。

这与 Chapter 3 的批评相连：Zipf exponent 的不稳定可能不是数据噪声，而是因为城市系统本来就没有到达 stationary asymptotic power-law regime。

---

## 十七、parameters over time：为什么短期估计还能解释长期数据

作者承认一个潜在问题。Chapter 9 中 $r,\alpha,\beta$ 的估计来自 4-5 年的 migration datasets，但 Chapter 10 用这些参数讨论几十年甚至上百年的 city dynamics。

原则上，没有理由假设：

$$
r,\alpha,\beta
$$

在几十年内完全不变。

但 Fig. 10.2 的 scaling collapse 说明，至少对法国数据，relative distribution 的形状在 1876-2015 年间相当稳定。这意味着参数即使有变化，也没有破坏 Eq. 10.50 的 scaling structure。

因此作者的立场不是：

$$
\text{parameters are exactly constant over centuries}.
$$

而是：

$$
\text{parameters are stable enough to preserve the scaling law}.
$$

---

## 十八、rank dynamics：为什么只看 distribution 还不够

到这里，模型已经解释了 population distribution 的 scaling。但作者还要测试 temporal dynamics。

原因是：两个模型可能在某个时刻产生相似的 size distribution，但 rank trajectories 完全不同。

Gabaix model 能生成 stationary power-law，但它的 rank dynamics 很平滑。城市 rank 大体围绕某个位置小幅波动，不容易出现快速剧烈换位。

真实城市历史则更 turbulent。城市会崛起、衰落，甚至在短时间里发生巨大 rank jump。

作者使用 Batty's rank clocks 来比较三种情况：

$$
\text{real France 1876-2015},
\quad
\text{Gabaix model},
\quad
\text{Levy model}.
$$

Fig. 10.4 有三个 panels。

![Fig. 10.4 real France rank clock](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-12-figure-01.jpg)

![Fig. 10.4 Gabaix rank clock](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-12-figure-02.jpg)

![Fig. 10.4 Levy rank clock](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-12-figure-03.jpg)

rank clock 的读法是：半径表示 rank，角度表示时间。中心是最大城市，外圈是较小城市。每条线表示一个城市的 rank 随时间如何变化。

左图是真实法国城市。线条交叉和摆动很多，说明 rank dynamics turbulent。

中图是 Gabaix model。轨迹更接近同心环，说明 rank 相对稳定，城市主要在固定层级附近波动。

右图是 Levy model。它比 Gabaix model 更容易产生较大 rank changes，因此更接近真实 rank turbulence。

这张图的核心是：城市模型不能只验证 size distribution，还要验证 rank dynamics。否则一个模型可能在静态分布上看似正确，却无法解释城市历史的剧烈变化。

---

## 十九、Eq. 10.51：平均 rank jump 指标

为了量化 rank turbulence，作者定义 average rank variation per unit time。作为 rank jump 指标，它应按 rank change 的幅度理解：

$$
d
=
\frac{1}{NT}
\sum_t
\sum_{i=1}^{N}
\left|
r_i(t)-r_i(t-1)
\right|.
\tag{10.51}
$$

这里：

$$
r_i(t)
$$

是城市 $i$ 在时间 $t$ 的 rank；

$$
N
$$

是城市数；

$$
T
$$

是时间长度。

如果不按幅度读，正负 rank changes 会互相抵消，无法表示 average jump。因此这个指标衡量的是：平均每个城市每个时间单位改变多少 rank positions。

Table 10.1 比较 data、Levy model 和 Gabaix model。

| Average rank jump per time unit $d$ | Data | Levy | Gabaix |
|---|---:|---:|---:|
| France 1876-2015 | 6.0 | 6.1 | 8.0 |
| UK 1790-1990 | 4.7 | 16 | 27 |
| US 1861-1991 | 4.8 | 16 | 25 |

France 的 data 最完整，Levy model 几乎命中 $d$。UK 和 US 的差异较大，作者认为可能和数据只记录 top cities 有关。

总体上，Gabaix model 的 rank jumps 更不符合真实数据；Levy model 更能产生 turbulent rank dynamics。

---

## 二十、Eq. 10.52：为什么 Levy noise 能改变城市命运

作者用 Chapter 8 的核心性质解释 rank turbulence。

对 Levy-distributed random variables，可能出现：

$$
X_{n+1}
\sim
\sum_{i=1}^{n}X_i.
\tag{10.52}
$$

这句话的意思是：一个新的 extreme shock 可以和之前所有 shocks 的总和同阶。

这里的 $X_i$ 可以理解成一个城市在不同时段遭遇的随机增长冲击，尤其是 migration shock。$\sum_{i=1}^{n}X_i$ 表示这个城市过去很多期冲击的累计效果。$X_{n+1}$ 表示下一期新来的一个冲击。

如果随机冲击是 thin-tailed，历史累计量通常来自许多小项的平均叠加。单个新冲击虽然会改变轨迹，但很难和过去所有冲击的总和同等重要。

在 Gaussian/finite-variance 情况下，通常有：

$$
X_{n+1}
\ll
\sum_{i=1}^{n}X_i.
$$

单个冲击很难改变长期累积趋势。

原因是 Gaussian tail 下降得非常快。极端大冲击的概率近似按 exponential scale 消失，所以当历史已经累积了很多期以后，新来一期通常只是总和里的一个小修正。城市 rank 因而更像连续漂移：上升或下降需要很多期小变化慢慢累积。

但 Levy noise 的 heavy tail 允许：

$$
\text{one migration shock}
\sim
\text{past accumulated migration effect}.
$$

翻译成城市语言就是：一个迁移浪潮、资源发现、战争、政策改变、殖民扩张或产业转移，可以在短时间内改变某个城市的 rank trajectory。

这和 rank dynamics 的关系是：rank 不是由城市的绝对人口单独决定，而是由城市之间的相对位置决定。一个城市只要遭遇一次足够大的正向 shock，就可能越过许多原本规模接近的城市；反过来，一次足够大的负向 shock 也可能让它迅速掉出原来的层级。

所以 turbulent rank dynamics 需要的不是“所有城市都随机波动”这个弱条件，而是“某些城市可以遭遇足够大的离散跳变”这个强条件。Gabaix-style Gaussian model 有随机性，但随机性主要是连续小扰动；Levy model 的随机性包含 rare large jumps，因此更容易生成 rank clock 里那种大量交叉、突然跃迁和长期不稳定。

这就是为什么 Levy model 能生成 turbulent rank clocks，而 Gabaix model 很难做到。Gabaix model 的 Gaussian shocks 太平滑，rank changes 主要是渐进的；Levy model 允许 sudden jumps。

---

## 二十一、Fig. 10.5：最大 rank jump 的等待时间

作者最后用另一个角度比较模型：给定最大 rank variation $\Delta r$，平均要等多少年才能观察到这样的 jump？

![Fig. 10.5](../../pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/10-about-city-dynamics.mineru/hybrid_auto/images/page-13-figure-01.jpg)

黑线是真实法国数据，虚线是 Levy model，点划线是 Gabaix model。灰色区间表示 dispersion。

图的含义是：Gabaix model 对大 rank jump 的等待时间预测不合适，而 Levy model 更接近真实数据。尤其对较大的 $\Delta r$，Gaussian-type model 会低估或错估 extreme rank changes 的发生机制。

这再次说明，城市动态不是只有连续小扰动。历史中的城市系统会经历 rare large shocks，而这些 shocks 正是 Levy noise 的统计语言要表达的东西。

---

## 二十二、解释：为什么这是 emergence

作者最后把技术结果解释成 complex systems 的 emergence。

如果 migration shocks 的 tail exponent 满足：

$$
\alpha>2,
$$

那么 variance finite，ordinary CLT 生效。许多 migration shocks 会被 Gaussian noise 概括，Gibrat-like model 仍然合理。

但经验上：

$$
\alpha<2.
$$

这个看似只是 numerical threshold 的变化，会导致 qualitative shift。

从微观层面看，只是把：

$$
\text{Gaussian noise}
$$

替换成：

$$
\text{Levy noise}.
$$

但从宏观层面看，城市系统的行为完全不同。

Gaussian growth picture 表示城市通过许多小而不可控的 shocks 累积增长，最终形成高度不平等的 distribution。

Levy growth picture 表示一个足够大的 migration shock 可以在短时间内改变城市命运。这给 urban planning 和 political intervention 更大空间，因为城市 rank 和规模不是被无数微小随机扰动锁死的。

作者举了两个直观例子。

San Francisco 在 Gold Rush 期间快速增长，从 1850 年左右一千多人变成 1870 年左右十五万人。这类 jump 很难用平滑 Gaussian growth 理解。

Mariupol 在 2022 年俄罗斯入侵和城市破坏后人口大幅下降。这说明负向 extreme shock 同样可以快速改变城市命运。

这些例子不是模型的输入，而是说明模型的解释方向：城市历史中极端事件不可避免，Levy noise 给这种事件一个 quantitative representation。

---

## 二十三、本章最重要的记忆点

第一，Chapter 10 从 Chapter 9 的方程出发：

$$
\partial_tS
=
\eta S
+
DS^\beta\zeta_{\alpha,\delta}.
$$

第二，Gaussian noise $\eta$ 的 fluctuation 可以近似为平均 drift：

$$
\eta S\simeq rS.
$$

原因是 Levy noise 在 tail behavior 上支配 Gaussian noise。

第三，简化后的核心 SDE 是：

$$
\partial_tS
=
rS
+
DS^\beta\zeta_\alpha.
$$

第四，它对应 fractional Fokker-Planck equation：

$$
\partial_tP
=
-
\partial_S(rSP)
+
D^\alpha
\partial_S^\alpha(S^{\alpha\beta}P).
$$

第五，fractional derivative 来自 Levy noise 的 Fourier exponent：

$$
|k|^\alpha.
$$

第六，Fox H-functions 是求解 fractional Fokker-Planck 的技术工具，因为它们在幂乘法和 Fourier transform 下保持封闭。

第七，large-$S$ expansion 的 leading term 给出：

$$
P(S,t)\sim S^{-1-\alpha}.
$$

但 convergence 极慢，真实城市系统通常达不到 pure power-law regime。

第八，因此 Zipf-like fitting 可能是 finite-range artifact。拟合质量高不代表系统真的处于 stationary Pareto regime。

第九，模型预言 scaling collapse：

$$
P(S,t)
=
\frac{1}{S}
F_{\alpha,\beta}
\left(
\frac{S}{\overline{S(t)}}
\right),
$$

法国长期数据支持这一点。

第十，Levy model 比 Gabaix model 更能解释 turbulent rank dynamics，因为 Levy shocks 允许：

$$
X_{n+1}
\sim
\sum_{i=1}^{n}X_i.
$$

这句话不是说每一次 shock 都这么大，而是说 heavy-tailed distribution 让这种“单次冲击可与历史累计同阶”的事件具有不可忽略的概率。只要这种事件偶尔发生，城市 rank 就不会只是平滑漂移，而会出现突然跃迁、交叉和长期层级重排。

这就是本章的核心解释：城市动态由 rare but large migration shocks 深刻塑形，而不是只由平滑的 proportional Gaussian growth 决定。
