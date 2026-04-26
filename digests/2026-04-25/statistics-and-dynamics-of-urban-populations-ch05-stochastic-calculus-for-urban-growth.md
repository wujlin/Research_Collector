---
title: "Statistics and Dynamics of Urban Populations, Chapter 5: Stochastic calculus"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-25"
topics: ["urban growth", "stochastic differential equations", "Itô calculus", "Stratonovich calculus", "Fokker-Planck equation", "multiplicative noise"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/05-stochastic-calculus.mineru/hybrid_auto/05-stochastic-calculus.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 5：Stochastic Calculus for Urban Growth

## 精读笔记

---

## 一、这一章在 urban growth 模块里的位置

Chapter 5 的标题在 MinerU 抽取里显示为 **Models of urban growth**，但这一章真正做的是数学铺垫：在进入 Chapter 6 的具体 stochastic growth models 之前，作者先解释为什么城市增长需要 SDE，以及使用 SDE 时最容易出错的地方在哪里。

城市人口增长不是一个纯确定性过程。出生、死亡、迁移、经济冲击、政策变化和历史事件都会让城市人口在短时间内出现不可预测的波动。作者因此把城市增长放入 stochastic differential equations 的语言里：确定性部分写成 drift，无法逐项解释的随机扰动写成 noise。

这一章最重要的线性逻辑是：

1. 从离散随机游走进入 Brownian motion；
2. 从 Brownian motion 引出 Wiener process 和 white noise；
3. white noise 的导数是奇异对象，因此 stochastic integral 需要 convention；
4. Itô 和 Stratonovich 对乘性噪声给出不同结果；
5. Itô 和 Stratonovich 的选择对应不同的噪声物理语义；
6. 对 SDE 的另一种读法是概率密度演化，也就是 Fokker-Planck equation；
7. 推导 Fokker-Planck equation 时，Eq. 5.38 到 Eq. 5.40 是关键阶数展开，决定了 extra drift 如何出现。

所以这一章不是单纯数学附录，而是后面城市增长方程的语法。特别是如果人口方程里出现 multiplicative noise，例如噪声项依赖城市规模 $S_i(t)$，那么选择 Itô 还是 Stratonovich 会改变漂移项，也会改变对应的概率演化方程。

---

## 二、从随机游走到 white noise

作者从最简单的一维随机游走开始。粒子每一步向右或向左移动距离 $a$：

$$
x(n)=\sum_{k=1}^n \xi(k),
\qquad
\xi(k)=
\begin{cases}
a, & \text{prob. } 1/2,\\
-a, & \text{prob. } 1/2.
\end{cases}
\tag{5.1}
$$

这一步建立的是最基本的 stochastic process 图像：未来位置不是由确定性轨道给出，而是由一串随机增量累加出来。因为每一步独立，整个过程是 Markovian。

随着步数 $n$ 增大，中心极限定理告诉我们，归一化位置趋向高斯分布：

$$
\frac{x(n)}{\sqrt{n}} \sim \mathcal{N}(0,a). \tag{5.3}
$$

这就是从离散随机游走走向 Brownian motion 的入口。接下来，作者把时间区间 $t$ 切成 $n$ 个小步，每一步长度为 $\tau=t/n$，并令每个增量服从方差为 $\tau$ 的高斯分布：

$$
\xi(k)\sim \mathcal{N}(0,\tau). \tag{5.5}
$$

当 $\tau\to 0$、$n\to\infty$，且 $t=n\tau$ 固定时，随机游走的连续极限就是 Wiener process：

$$
x(t)=\lim_{\tau\to 0}\sum_{i=1}^{n=t/\tau}\xi(i)
\equiv \int_0^t d\xi(t'). \tag{5.6}
$$

这里最关键的尺度关系是：Wiener 增量不是 $O(dt)$，而是 $O(\sqrt{dt})$。也就是说，

$$
dW \sim \sqrt{dt}.
$$

这条尺度关系会贯穿后面的推导。它解释了为什么某些看似高阶的小量不能直接丢掉。尤其在 Fokker-Planck 推导里，$(dW)^2$ 是 $O(dt)$，不是 $O(dt^2)$。

---

## 三、为什么 white noise 会制造积分歧义

Wiener process with drift 可以写成：

$$
x(t)=\mu t+\sigma W(t). \tag{5.7}
$$

形式上对时间求导，就得到 Langevin equation：

$$
\frac{dx(t)}{dt}
= \mu+\sigma\frac{dW(t)}{dt}
\equiv \mu+\sigma\eta(t). \tag{5.8}
$$

这里 $\eta(t)$ 被称为 white noise，它满足：

$$
\langle \eta(t)\rangle=0,
\qquad
\langle \eta(t)\eta(t')\rangle=\delta(t-t'). \tag{5.9}
$$

问题在于，$W(t)$ 连续但不可微，所以 $\eta(t)=dW/dt$ 不是普通函数。因为 $dW\sim\sqrt{dt}$，所以形式上的导数

$$
\eta(t)\sim \frac{\sqrt{dt}}{dt}=\frac{1}{\sqrt{dt}}
$$

在 $dt\to 0$ 时发散。

因此，SDE 不能像普通 ODE 那样直接读。特别是当噪声前面的系数依赖状态 $x(t)$ 时：

$$
\frac{dx(t)}{dt}=f(x(t))+g(x(t))\eta(t), \tag{5.10}
$$

随机积分

$$
\int g(x(s))\,dW
$$

必须说明 $g$ 到底在时间步的哪个位置求值。这个选择不是技术细节，而会改变结果。

---

## 四、Itô 与 Stratonovich：同一个 SDE 的两种读法

作者用一个参数 $\alpha\in[0,1]$ 统一描述积分 convention。在小区间 $[t,t+h]$ 上，随机积分近似为：

$$
\int_t^{t+h} g(x(s))\,dW
\simeq
g\!\left(\alpha x(t)+(1-\alpha)x(t+h)\right)
\left[W(t+h)-W(t)\right]. \tag{5.13}
$$

这里 $\alpha$ 决定 $g$ 在哪里求值。

当 $\alpha=1$，$g$ 在初始点 $x(t)$ 求值。这是 Itô prescription。它的含义是：先看当前状态，再让噪声作用；状态不提前知道同一步噪声。

当 $\alpha=1/2$，$g$ 在中点求值。这是 Stratonovich prescription。它更接近普通微积分链式法则，常对应带有限相关时间的平滑噪声极限。

作者用积分

$$
\int_t^{t'} W(s)\,dW
\tag{5.16}
$$

说明两者差异。这里最容易误解的是：Itô 和 Stratonovich 不是在算两个不同的随机过程，而是在给同一个符号 $\int W\,dW$ 规定两种不同的离散极限。

把区间 $[t,t']$ 切成很多小段，记

$$
W_i=W(t_i),\qquad \Delta W_i=W_i-W_{i-1}.
$$

普通 Riemann 积分里，函数很平滑，左端点、右端点、中点取样在极限里通常给出同一个结果。Brownian motion 不一样。它的路径连续但处处不可微，并且每一步增量的典型大小是

$$
\Delta W_i = O(\sqrt{\Delta t}).
$$

所以单个二阶项 $(\Delta W_i)^2$ 是 $O(\Delta t)$。把所有小段加起来后，

$$
\sum_i(\Delta W_i)^2
$$

不会消失，而会收敛到时间长度 $t'-t$。这叫 Brownian motion 的 quadratic variation。随机积分的 convention 差异，正是从这个二阶量里来的。

Stratonovich 使用中点取样。对这个例子来说，它把 $W(s)$ 放在每一步的中点值：

$$
\int_t^{t'} W(s)\,dW
=\lim_{N\to\infty}\sum_i
\frac{W_i+W_{i-1}}{2}\Delta W_i. \tag{5.19}
$$

这一步可以直接用代数恒等式展开：

$$
\frac{W_i+W_{i-1}}{2}(W_i-W_{i-1})
=\frac{W_i^2-W_{i-1}^2}{2}.
$$

把所有小段相加，中间项望远镜相消，只剩首尾两端：

$$
\int_t^{t'} W(s)\,dW
= \frac{W(t')^2-W(t)^2}{2}. \tag{5.20}
$$

这就是为什么 Stratonovich 给出普通链式法则式结果。它相当于仍然相信

$$
d(W^2)=2W\circ dW,
$$

其中 $\circ dW$ 表示 Stratonovich 积分。

这里的 $\circ$ 不是乘号，而是提醒读者：这个 $dW$ 要按 Stratonovich 的中点规则理解。也就是说，

$$
\int W\circ dW
$$

不是 Itô 积分 $\int W\,dW$，而是

$$
\lim_{N\to\infty}\sum_i
\frac{W_i+W_{i-1}}{2}\Delta W_i.
$$

为什么这叫“普通链式法则”？可以先看一条光滑路径 $w(t)$。如果 $F(w)=w^2$，普通微积分会写成

$$
dF=F'(w)\,dw=2w\,dw.
$$

积分后就是

$$
\int_t^{t'} w(s)\,dw
=\frac{w(t')^2-w(t)^2}{2}.
$$

Stratonovich 的思想是：Brownian path 虽然不光滑，但如果随机噪声可以看成有限相关时间噪声的极限，或者看成先被平滑、再取极限的路径，那么链式法则应该尽量保留下来。中点取样正好实现这一点，因为每一步都有精确恒等式

$$
W_i^2-W_{i-1}^2
=(W_i+W_{i-1})(W_i-W_{i-1})
=2\frac{W_i+W_{i-1}}{2}\Delta W_i.
$$

因此在 Stratonovich 规则下，

$$
d(W^2)=2W\circ dW
$$

的意思不是说 Brownian motion 真的可微，而是说：如果把随机积分定义成中点极限，那么平方函数的增量仍然可以像普通微积分一样只由一阶链式法则解释。

更一般地，Stratonovich calculus 对光滑函数 $F(W)$ 保持形式上的普通链式法则：

$$
dF(W)=F'(W)\circ dW.
$$

Itô calculus 则必须额外保留二阶项：

$$
dF(W)=F'(W)\,dW+\frac{1}{2}F''(W)\,dt.
$$

对 $F(W)=W^2$，有 $F'(W)=2W$、$F''(W)=2$，所以 Itô 形式变成

$$
d(W^2)=2W\,dW+dt.
$$

这就是同一个表达式在两套积分 convention 下的本质差异：Stratonovich 把二次变差吸收到中点积分定义里，于是公式看起来像普通链式法则；Itô 把二次变差显式写出来，于是多出 $dt$ 修正项。

Itô 使用左端点取样。它的定义是：

$$
\int_t^{t'} W(s)\,dW
=\lim_{N\to\infty}\sum_i W_{i-1}\Delta W_i. \tag{5.17}
$$

这时每一步不能再写成纯粹的平方差，而要从下面这个恒等式开始：

$$
W_{i-1}(W_i-W_{i-1})
=\frac{W_i^2-W_{i-1}^2}{2}
-\frac{(W_i-W_{i-1})^2}{2}.
$$

第一项相加后仍然只剩端点；第二项相加后不会消失，而是 Brownian motion 的 quadratic variation。因此 Itô 给出：

$$
\int_t^{t'} W(s)\,dW
= \frac{W(t')^2-W(t)^2}{2}
-\frac{1}{2}\lim_{N\to\infty}\sum_i
\left[W(t_i)-W(t_{i-1})\right]^2. \tag{5.18}
$$

由于

$$
\lim_{N\to\infty}\sum_i(\Delta W_i)^2=t'-t,
$$

这也可以写成更熟悉的形式：

$$
\int_t^{t'} W(s)\,dW
=\frac{W(t')^2-W(t)^2}{2}
-\frac{t'-t}{2}.
$$

这就是 Itô correction 的来源。它不是人为添加，而是来自 Brownian increment 的尺度：$dW$ 是 $\sqrt{dt}$，所以二阶项 $(dW)^2$ 仍然是 $dt$ 量级。用微分形式说，Itô calculus 里不是普通链式法则，而是

$$
d(W^2)=2W\,dW+(dW)^2=2W\,dW+dt.
$$

移项之后就是

$$
W\,dW=\frac{1}{2}d(W^2)-\frac{1}{2}dt.
$$

所以 Itô 积分比 Stratonovich 积分少了 $\frac{1}{2}(t'-t)$。

两者的直观差异可以这样记：

1. Itô 是左端点规则。先固定 $W_{i-1}$，再让下一段噪声 $\Delta W_i$ 作用。积分因子不预知同一步噪声，所以 $W_{i-1}$ 和未来增量 $\Delta W_i$ 独立。这使得 Itô 积分有很好的 martingale 性质，也适合“当前状态先确定，外部冲击随后到来”的建模。
2. Stratonovich 是中点规则。每一步的取样点包含了部分未来增量，因为 $W_i=W_{i-1}+\Delta W_i$。于是中点值里含有 $\frac{1}{2}\Delta W_i$，再乘上 $\Delta W_i$，就多出 $\frac{1}{2}(\Delta W_i)^2$。这个额外项正好补回 Itô 里留下的 quadratic variation 修正，所以 Stratonovich 保留普通链式法则。
3. 如果噪声是 additive 的，也就是 $g(x)$ 不依赖 $x$，两种 convention 通常不会造成 drift 差异。真正敏感的是 multiplicative noise：噪声幅度依赖状态，取样点不同会改变有效漂移项。
4. 从物理解释看，Stratonovich 更像有有限相关时间、被平滑过的 colored noise 的极限；Itô 更像理想化的白噪声冲击，每一时刻的噪声与当前状态不相关。

---

## 五、Physical meaning：积分 convention 对应什么噪声模型

前面的推导回答了一个数学问题：同一个符号 $\int W\,dW$，如果用左端点定义，就得到 Itô correction；如果用中点定义，就保留普通链式法则。原文接着问的是另一个问题：真实建模时应该选哪一个？这个选择不能只靠公式美观，而要看噪声在物理上怎样进入系统。

关键对象是噪声的时间相关函数：

$$
G(t,t')=\langle \eta(t)\eta(t')\rangle. \tag{5.22}
$$

它描述的是：$t$ 时刻的噪声和 $t'$ 时刻的噪声之间有没有记忆。如果噪声是理想 white noise，那么

$$
G(t,t')=\delta(t-t').
$$

这句话的意思是：两个不同时刻的噪声完全不相关，只有同一时刻有无限尖锐的相关。数学上这很方便，因为每个时间步的冲击都可以看成新的独立抽样；但物理上它也很极端，因为真实冲击通常不可能在无限短时间内剧烈跳变。

原文用 Gaussian noise 的路径概率来表达这一点。给定一整条噪声路径 $\{\eta(t)\}$，它的概率权重由相关函数 $G$ 决定：

$$
\mathbb{P}(\{\eta(t)\})
\propto
\exp\left[
-\frac{1}{2}
\int_0^T\int_0^T
dt\,dt'\,
\eta(t)G^{-1}(t,t')\eta(t')
\right]. \tag{5.23}
$$

这条公式不需要在这里深挖 path integral 技术。它的作用是说明：噪声不是只有“均值为 0、方差为 1”这么简单；噪声在时间上的相关结构也属于模型假设。改变 $G(t,t')$，就是改变我们允许哪些噪声路径更可能出现。

如果没有时间相关性，$G(t,t')=\delta(t-t')$，那么路径权重简化为：

$$
\mathbb{P}(\{\eta(t)\})
\propto
\exp\left[
-\frac{1}{2}
\int_0^T dt\,\eta(t)^2
\right]. \tag{5.25}
$$

这对应 white noise 的理想化图像：不同时间点之间没有记忆。每一个瞬间的噪声都像重新抽样出来的独立冲击。

但原文随后考虑另一种更物理的情况：噪声有有限相关时间 $\tau_c$。典型例子是 Ornstein-Uhlenbeck noise，它的相关函数是

$$
G(t,t')
=
\frac{1}{2\tau_c}
\exp\left(-\frac{|t-t'|}{\tau_c}\right). \tag{5.26}
$$

这里 $\tau_c$ 是 correlation time。它可以理解为噪声记忆能持续多久。如果 $|t-t'|\ll\tau_c$，两个时刻的噪声仍然相似；如果 $|t-t'|\gg\tau_c$，相关性才明显衰减。

这个设定带来一个重要变化：噪声不再能无限快速地跳动。原文在频率空间写成

$$
G(\omega)=\frac{1}{1+\omega^2\tau_c^2}. \tag{5.27}
$$

当 $\tau_c\to 0$ 时，$G(\omega)$ 近似变平，所有频率都可以出现，这就是 white noise：高频、低频都被同等允许。相反，当 $\tau_c>0$ 时，高频部分会被压低。换句话说，有限相关时间相当于过滤掉无限快的振荡，噪声变成 colored noise，也就是更平滑、更有记忆的噪声。

同一件事也可以在时间域里看。原文把逆相关函数写成

$$
G^{-1}(t,t')
=
\delta(t-t')
\left(1+\tau_c^2\partial_t\partial_{t'}\right). \tag{5.29}
$$

这个式子的重点不是算符细节，而是 $\partial_t\partial_{t'}$ 这一项：它让噪声路径的快速变化变得有代价。直观地说，如果一条噪声路径 $\eta(t)$ 在很短时间内剧烈上下跳动，那么它包含很强的高频成分；当 $\tau_c>0$ 时，这些高频成分会被压低。

因此路径概率里除了惩罚噪声幅度 $\eta(t)^2$，还会惩罚噪声变化速度。按这个意思，Eq. 5.30 可以读成：

$$
\mathbb{P}(\{\eta(t)\})
\propto
\exp\left[
-\frac{1}{2}
\int_0^Tdt\,
\left(\eta(t)^2+\tau_c^2\dot{\eta}(t)^2\right)
\right]. \tag{5.30}
$$

这一步给出有限相关时间的物理含义：white noise 只关心噪声幅度，不惩罚无限快的变化；colored noise 额外惩罚快速变化，所以噪声脉冲被平滑，轨迹也更接近普通微积分可以处理的路径。

这就是 “Physical meaning” 小节的核心：Itô 和 Stratonovich 不是两种任意记号，而是两种不同噪声极限。

第一种情况是 $\tau_c\gg dt$。在一个模型时间步 $dt$ 内，噪声还保留明显相关性。它不会每个瞬间完全重新抽样，而是有连续变化的趋势。此时系统轨迹被平滑，普通微积分的链式法则可以保留：

$$
\frac{dg}{dt}
=
\frac{\partial g}{\partial t}
+
\frac{\partial g}{\partial x}\dot{x}. \tag{5.31}
$$

这里的 $g$ 表示任意被求导的函数，不是前面 SDE 里噪声前面的那个 $g(x)$。原文的意思是：只要噪声足够平滑，对任意状态函数都可以继续使用普通链式法则。

这对应 Stratonovich。原因是中点取样默认噪声在一个小时间步内不是完全突变的，而是有一个可被平均的连续过程。它适合描述带有限相关时间的外部扰动，例如一段时间内持续影响城市增长的区域经济环境、政策环境、气候压力或金融条件。

但 Stratonovich 也有代价。因为噪声在时间上有相关性，$t$ 时刻的噪声不再完全独立于过去状态。也就是说，当前状态 $x(t)$ 和当前噪声 $\eta(t)$ 之间可能已经通过过去的相关性发生耦合。这样普通链式法则保住了，但“每一时刻冲击都是全新独立抽样”的 Markov 图像就弱了。

第二种情况是 $\tau_c\ll dt$。在模型时间步看来，噪声相关时间极短，可以近似成理想 white noise。此时每一步冲击都被视为和当前状态无关的新扰动。为了保留这种 non-anticipating 的结构，必须使用 Itô：先固定当前状态 $x(t)$，再让未来时间步的噪声作用。

这也是 Itô 的建模语义：系统不能提前知道同一步噪声。用原文的话说，函数先在当前状态上计算，然后噪声才作用。于是对任意函数 $g(x(t))$，可以保持

$$
\langle g(x(t))\eta(t)\rangle=0.
$$

但代价是普通链式法则失效，必须加入 Itô correction：

$$
\frac{dg}{dt}
=
\frac{\partial g}{\partial t}
+
\frac{\partial g}{\partial x}\dot{x}
+
\frac{1}{2}
\frac{\partial^2 g}{\partial x^2}. \tag{5.32}
$$

这里的 $g$ 同样表示任意状态函数。和 Eq. 5.31 相比，Eq. 5.32 多出来的就是 Itô correction。

这条式子的最后一项就是前面 quadratic variation 在一般函数上的表现。Brownian increment 的二阶项不会消失，所以对非线性函数 $g(x)$ 做变量变换时，必须额外保留二阶导数项。

因此，选择 Itô 还是 Stratonovich，可以按下面的建模问题来判断：

1. 如果噪声代表一个被平滑过的外部环境过程，并且这个过程在模型时间步内有持续性，那么 Stratonovich 更自然。
2. 如果噪声代表每个时间步新发生的独立冲击，并且当前状态不能预知这个冲击，那么 Itô 更自然。
3. 如果噪声是 additive noise，也就是噪声强度不依赖状态，两种选择通常不会改变 drift。
4. 如果噪声是 multiplicative noise，也就是噪声强度依赖 $x(t)$，两种选择会改变 effective drift，因此不能含混处理。

对城市增长的意义在于：人口增长中的随机项经常是 multiplicative 的。例如大城市可能有更大的迁移流、更大的就业冲击、更大的资本流动幅度，于是噪声强度会随城市规模 $S(t)$ 改变。这时 convention 不只是数学细节，而会改变增长方程里的系统性漂移项。

如果后面 Chapter 9 选择 Itô，它的含义应该读成：城市在时间 $t$ 的规模 $S(t)$ 先被观测或确定，随后 $[t,t+dt]$ 内的迁移、出生死亡、经济冲击才作用到系统上。当前城市规模不预知这一小段未来噪声。因此 Itô 对应一种“当前状态先定，未来冲击再来”的增长叙事。

如果改用 Stratonovich，则相当于假设增长冲击不是瞬时独立抽样，而是在时间上有相关性，并且在一个小时间步内与城市状态共同演化。这也可能合理，但它对应的是另一种城市增长机制：外部环境不是一个个独立冲击，而是一个有记忆、有持续性的背景过程。

所以 “Physical meaning” 这一节的结论是：Itô/Stratonovich 的差异不只是 Eq. 5.18 和 Eq. 5.20 的计算差异，而是关于噪声如何进入城市增长模型的机制假设。

---

## 六、从 trajectory 转向 probability：为什么需要 Fokker-Planck equation

前半章讨论的是单条随机轨迹 $x(t)$。但在城市增长问题里，我们往往不只关心一座城市的一条轨迹，而关心一组城市人口分布怎样演化。因此需要从 SDE 转到概率密度 $p(x,t)$。

作者考虑一般 SDE：

$$
\frac{dx}{dt}=f(x(t))+g(x(t))\eta(t), \tag{5.33}
$$

其中 $\eta(t)$ 是 Gaussian white noise。目标是推导对应的 Fokker-Planck equation，也就是 $p(x,t)$ 的演化方程。

推导从离散时间开始。设 $t_i=t_0+ih$，$x_i=x(t_i)$。在一个小时间步上：

$$
x_{i+1}
=x_i+\int_{t_i}^{t_{i+1}}ds\,
\left[f(x(s))+g(x(s))\eta(s)\right]. \tag{5.34}
$$

随机项用 $\alpha$ convention 离散化：

$$
\int_{t_i}^{t_{i+1}} g(x(s))\eta(s)\,ds
\simeq
\sqrt{h}\,u_i\,
g\!\left(\alpha x_i+(1-\alpha)x_{i+1}\right), \tag{5.35}
$$

其中 $u_i$ 是均值为 0、方差为 1 的标准高斯变量。因为

$$
W(t_{i+1})-W(t_i)\sim \sqrt{h}\,u_i,
$$

随机增量是 $O(\sqrt{h})$。

为了保持 convention 一致，drift 项也在同一个插值点上取值：

$$
\int_{t_i}^{t_{i+1}} f(x(s))\,ds
\simeq
h f\!\left(\alpha x_i+(1-\alpha)x_{i+1}\right). \tag{5.36}
$$

于是得到一步更新式：

$$
x_{i+1}
=x_i+h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i, \tag{5.37}
$$

其中

$$
f_\alpha^i
=f\!\left(\alpha x_i+(1-\alpha)x_{i+1}\right),
\qquad
g_\alpha^i
=g\!\left(\alpha x_i+(1-\alpha)x_{i+1}\right).
$$

这时难点出现了：$f_\alpha^i$ 和 $g_\alpha^i$ 依赖 $x_{i+1}$，但 $x_{i+1}$ 又由 $f_\alpha^i$ 和 $g_\alpha^i$ 决定。这是一个隐式关系。Eq. 5.38 和 Eq. 5.39 的作用，就是把这个隐式关系按 $h$ 展开成显式近似。

---

## 七、Eq. 5.38 线性展开：为什么 $f_\alpha^i=f(x_i)+O(\sqrt{h})$

Eq. 5.38 在原文里写得很紧：

$$
\begin{aligned}
f_\alpha^i
&=
f\!\left(
x_i+(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right)
\right)\\
&=f(x_i)+O(\sqrt{h}).
\end{aligned}
\tag{5.38}
$$

这一步折叠了三个小步骤。

第一步，把 $f_\alpha^i$ 的求值点写出来。按照定义：

$$
f_\alpha^i
=f\!\left(\alpha x_i+(1-\alpha)x_{i+1}\right).
$$

第二步，把 Eq. 5.37 代入 $x_{i+1}$：

$$
x_{i+1}
=x_i+h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i.
$$

于是：

$$
\alpha x_i+(1-\alpha)x_{i+1}
=\alpha x_i+(1-\alpha)
\left(x_i+h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right).
$$

把 $x_i$ 的系数合并：

$$
\alpha x_i+(1-\alpha)x_i=x_i.
$$

所以求值点变成：

$$
x_i+(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right).
$$

这就是 Eq. 5.38 第一行。

第三步，判断括号里的位移量有多大。因为 $u_i=O(1)$，且 $h\ll1$，所以

$$
h f_\alpha^i = O(h),
\qquad
\sqrt{h}\,u_i g_\alpha^i = O(\sqrt{h}).
$$

在小 $h$ 下，$O(\sqrt{h})$ 比 $O(h)$ 更大，因此整体位移

$$
\Delta x_i
=(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right)
$$

是 $O(\sqrt{h})$。

对 $f$ 做 Taylor expansion：

$$
f(x_i+\Delta x_i)
=f(x_i)+f'(x_i)\Delta x_i
+\frac{1}{2}f''(x_i)\Delta x_i^2+\cdots.
$$

由于 $\Delta x_i=O(\sqrt{h})$，所以第一阶修正 $f'(x_i)\Delta x_i$ 是 $O(\sqrt{h})$，第二阶修正是 $O(h)$。因此：

$$
f_\alpha^i=f(x_i)+O(\sqrt{h}).
$$

这就是 Eq. 5.38。

关键点是：这里不是说 $O(\sqrt{h})$ 永远不重要，而是因为在 Eq. 5.37 里 drift 项前面还有一个 $h$：

$$
h f_\alpha^i
=h f(x_i)+h\,O(\sqrt{h})
=h f(x_i)+O(h^{3/2}).
$$

后续推导只保留到 $O(h)$。所以 drift 展开里的 $O(\sqrt{h})$ 修正在乘上 $h$ 后变成 $O(h^{3/2})$，可以丢掉。

这就是 Eq. 5.38 的真正作用：**它允许我们在 drift 项中把 $f_\alpha^i$ 替换成 $f(x_i)$，因为误差只会影响 $O(h^{3/2})$。**

---

## 八、为什么 $g_\alpha^i$ 不能像 $f_\alpha^i$ 一样粗略处理

原文马上展开 $g_\alpha^i$：

$$
\begin{aligned}
g_\alpha^i
&=
g\!\left(
x_i+(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right)
\right)\\
&=
g(x_i)
+(1-\alpha)\sqrt{h}\,u_i g_\alpha^i g'(x_i)
+O(h)\\
&=
g(x_i)
+(1-\alpha)\sqrt{h}\,u_i g(x_i)g'(x_i)
+O(h).
\end{aligned}
\tag{5.39}
$$

这里看起来和 Eq. 5.38 类似，但保留阶数不同。原因在于 Eq. 5.37 中 noise 项前面是 $\sqrt{h}$：

$$
\sqrt{h}\,u_i g_\alpha^i.
$$

如果 $g_\alpha^i$ 的修正是 $O(\sqrt{h})$，那么乘上外面的 $\sqrt{h}$ 后会变成 $O(h)$。而 Fokker-Planck 推导正是要保留 $O(h)$ 项，所以这个修正不能丢。

这里的 $g'(x_i)$ 不是凭空多出来的项，而是 Taylor expansion 的一阶导数项。要看清这一点，先把 $g_\alpha^i$ 的求值点单独写出来。根据定义，

$$
g_\alpha^i
=
g\!\left(
\alpha x_i+(1-\alpha)x_{i+1}
\right).
$$

又因为一步更新式给出

$$
x_{i+1}
=x_i+h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i,
$$

所以

$$
\alpha x_i+(1-\alpha)x_{i+1}
=
x_i
+
(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right).
$$

这说明 $g_\alpha^i$ 其实是在 $x_i$ 附近一个稍微偏移的位置上求 $g$。把这个偏移记为

$$
\Delta x_i
=
(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right).
$$

于是

$$
g_\alpha^i=g(x_i+\Delta x_i).
$$

现在问题就变成普通 Taylor 展开：如果一个函数 $g(x)$ 的输入从 $x_i$ 变成 $x_i+\Delta x_i$，函数值的一阶变化不是直接等于 $\Delta x_i$，而是等于“斜率乘以位移”：

$$
g(x_i+\Delta x_i)
=
g(x_i)
+
g'(x_i)\Delta x_i
+
O(\Delta x_i^2).
$$

所以 $g'(x_i)$ 的来源就是：$g$ 本身是一个关于状态 $x$ 的函数，当求值点从 $x_i$ 移动到 $x_i+\Delta x_i$ 时，$g$ 的变化率由导数 $g'(x_i)$ 控制。如果 $g$ 是常数，也就是 additive noise，那么 $g'(x_i)=0$，这一项就消失；只有 multiplicative noise，也就是 $g$ 依赖状态时，这个导数项才会留下。

具体说，Taylor expansion 给出：

$$
g_\alpha^i
=g(x_i)+g'(x_i)\Delta x_i+O(\Delta x_i^2).
$$

其中

$$
\Delta x_i
=(1-\alpha)
\left(h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i\right).
$$

因为 $u_i=O(1)$，并且 $g_\alpha^i$ 在主阶上是 $O(1)$，所以 $\Delta x_i$ 里有两种尺度：

$$
h f_\alpha^i=O(h),
\qquad
\sqrt{h}\,u_i g_\alpha^i=O(\sqrt{h}).
$$

当 $h\to 0$ 时，$O(\sqrt{h})$ 比 $O(h)$ 更大。因此如果这里只需要找出 $g_\alpha^i$ 的一阶随机修正，就先保留 $\sqrt{h}u_i g_\alpha^i$，把 $h f_\alpha^i$ 合进 $O(h)$：

$$
g'(x_i)\Delta x_i
\simeq
(1-\alpha)\sqrt{h}\,u_i g_\alpha^i g'(x_i).
$$

这就得到原文第二行：

$$
g_\alpha^i
=
g(x_i)
+
(1-\alpha)\sqrt{h}\,u_i g_\alpha^i g'(x_i)
+
O(h).
$$

这里的 $O(h)$ 包含两类被压低的项：一类来自 $h f_\alpha^i$，另一类来自 Taylor 展开的二阶项 $O(\Delta x_i^2)$。因为 $\Delta x_i=O(\sqrt{h})$，所以 $\Delta x_i^2=O(h)$。

最后还要把右边的 $g_\alpha^i$ 替换成 $g(x_i)$。这样做是合法的，因为这个 $g_\alpha^i$ 已经乘在 $\sqrt{h}$ 后面。由 Eq. 5.38 同样的阶数逻辑可知，$g_\alpha^i=g(x_i)+O(\sqrt{h})$，所以

$$
\sqrt{h}\,u_i g_\alpha^i g'(x_i)
=
\sqrt{h}\,u_i g(x_i)g'(x_i)
+
O(h).
$$

于是得到 Eq. 5.39 的最后一行：

$$
g_\alpha^i
=g(x_i)
+(1-\alpha)\sqrt{h}\,u_i g(x_i)g'(x_i)
+O(h).
$$

这一步的核心可以压成一句话：**$g'$ 出现，是因为 $g$ 的输入点从 $x_i$ 被随机位移推到了 $x_i+\Delta x_i$；函数值对输入位移的一阶响应由导数 $g'(x_i)$ 给出。**

Eq. 5.38 和 Eq. 5.39 的区别可以压成一句话：

**$f_\alpha^i$ 的 $O(\sqrt{h})$ 修正被外面的 $h$ 压成 $O(h^{3/2})$，可以丢；$g_\alpha^i$ 的 $O(\sqrt{h})$ 修正被外面的 $\sqrt{h}$ 压成 $O(h)$，必须保留。**

---

## 九、Eq. 5.40：extra drift 从哪里来

把 Eq. 5.38 和 Eq. 5.39 代回一步更新式 Eq. 5.37：

$$
x_{i+1}
=x_i+h f_\alpha^i+\sqrt{h}\,u_i g_\alpha^i.
$$

drift 部分变成：

$$
h f_\alpha^i
=h f(x_i)+O(h^{3/2}).
$$

noise 部分变成：

$$
\sqrt{h}\,u_i g_\alpha^i
=\sqrt{h}\,u_i g(x_i)
+(1-\alpha)h u_i^2 g(x_i)g'(x_i)
+O(h^{3/2}).
$$

两部分合并：

$$
x_{i+1}
=x_i
+\sqrt{h}\,u_i g(x_i)
+h\left[
f(x_i)
+(1-\alpha)u_i^2 g(x_i)g'(x_i)
\right]
+O(h^{3/2}). \tag{5.40}
$$

这就是 Fokker-Planck 推导里的核心更新式。

这里出现了一个额外的 drift-like term：

$$
(1-\alpha)u_i^2 g(x_i)g'(x_i).
$$

它来自 multiplicative noise 的求值点依赖。只要 $g$ 依赖 $x$，并且 $\alpha\neq 1$，这个项就会出现。对 Itô prescription，$\alpha=1$，该项消失。对 Stratonovich prescription，$\alpha=1/2$，该项保留一半。

这也是为什么乘性噪声不是“普通噪声乘一个状态函数”这么简单。噪声幅度 $g(x)$ 随状态变化时，随机增量本身会反馈到下一步的有效漂移。

---

## 十、Eq. 5.41 到 Eq. 5.45：从一步更新到 Fokker-Planck equation

有了 Eq. 5.40，作者开始把单条 trajectory 的一步更新转成 probability density 的一步更新。前面关心的是：

$$
x_i \longrightarrow x_{i+1}.
$$

现在关心的是：如果时间 $t_i$ 的位置分布是 $p(x_i,t_i)$，那么经过一个小时间步 $h$ 后，时间 $t_{i+1}$ 的位置分布 $p(x_{i+1},t_{i+1})$ 怎么得到。

Eq. 5.40 给出一步更新：

$$
x_{i+1}
=
x_i+\sqrt{h}u_i g(x_i)
+h\left[f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right]
+O(h^{3/2}).
$$

为了让符号更清楚，先把一步位移记成

$$
A_i
=
\sqrt{h}u_i g(x_i)
+h\left[f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right].
$$

于是一步更新就是

$$
x_{i+1}=x_i+A_i+O(h^{3/2}).
$$

要在 $t_{i+1}$ 时刻到达某个给定位置 $x_{i+1}$，必须存在一个起点 $x_i$，并且噪声 $u_i$ 使得 $x_i+A_i=x_{i+1}$。这个约束用 delta function 写成：

$$
\begin{aligned}
p(x_{i+1},t_{i+1})
=
\left\langle
\int dx_i\,p(x_i,t_i)\,
\delta\!\left(
x_i+\sqrt{h}u_i g(x_i)
+h\left[f(x_i)+(1-\alpha)u_i^2 g(x_i)g'(x_i)\right]
-x_{i+1}
\right)
\right\rangle_{u_i}.
\end{aligned}
\tag{5.41}
$$

这里 $\langle\cdot\rangle_{u_i}$ 表示对噪声取平均。积分 $\int dx_i$ 表示把所有可能的起点都考虑进去。delta function 的作用是筛选路径：只有满足 $x_i+A_i=x_{i+1}$ 的起点和噪声组合，才会对 $p(x_{i+1},t_{i+1})$ 有贡献。

接下来要把 Eq. 5.41 变成一个 differential equation。关键是把 delta function 对小位移 $A_i$ 展开。令

$$
z_i=x_i-x_{i+1}.
$$

则

$$
\delta(x_i+A_i-x_{i+1})=\delta(z_i+A_i).
$$

对 $A_i$ 做 Taylor 展开：

$$
\delta(z_i+A_i)
=\delta(x_i-x_{i+1})
+A_i \partial_{x_i}\delta(x_i-x_{i+1})
+\frac{1}{2}A_i^2\partial_{x_i}^2\delta(x_i-x_{i+1})
+\cdots.
$$

这里导数可以写成 $\partial_{x_i}$，因为 $z_i=x_i-x_{i+1}$，而 $x_{i+1}$ 在这个计算里是固定的目标位置。

现在要判断哪些项保留。$A_i$ 由两部分组成：

$$
A_i
=\sqrt{h}u_i g(x_i)
+h\left[f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right].
$$

第一部分是 $O(\sqrt{h})$，第二部分是 $O(h)$。Fokker-Planck 方程来自 $h\to 0$ 时的一阶时间变化，所以展开时必须保留到 $O(h)$。

先看一阶项 $A_i\partial_{x_i}\delta$。这里 $A_i$ 的 $O(\sqrt{h})$ 和 $O(h)$ 两部分都要先写出来：

$$
A_i\partial_{x_i}\delta
=
\left[
\sqrt{h}u_i g(x_i)
+h\left(f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right)
\right]
\partial_{x_i}\delta(x_i-x_{i+1}).
$$

再看二阶项 $\frac{1}{2}A_i^2\partial_{x_i}^2\delta$。因为

$$
A_i^2
=
\left(\sqrt{h}u_i g(x_i)\right)^2
+2\left(\sqrt{h}u_i g(x_i)\right)
h\left[f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right]
+O(h^2),
$$

其中第一项是 $O(h)$，交叉项是 $O(h^{3/2})$，最后的平方项是 $O(h^2)$。保留到 $O(h)$ 时，只剩

$$
A_i^2
=
h u_i^2 g(x_i)^2+O(h^{3/2}).
$$

因此 Eq. 5.42 的完整意思是：

$$
\begin{aligned}
&\delta\!\left[
x_i+\sqrt{h}u_i g(x_i)
+h\left(f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right)
-x_{i+1}
\right]\\
&=
\delta(x_i-x_{i+1})\\
&\quad+
\left[
\sqrt{h}u_i g(x_i)
+h\left(f(x_i)+(1-\alpha)u_i^2g(x_i)g'(x_i)\right)
\right]
\partial_{x_i}\delta(x_i-x_{i+1})\\
&\quad+
\frac{1}{2}h u_i^2g(x_i)^2
\partial_{x_i}^2\delta(x_i-x_{i+1})
+O(h^{3/2}).
\end{aligned}
\tag{5.42}
$$

这一步容易被折叠的地方在于：二阶 Taylor 项不能直接丢。虽然它是二阶项，但 $A_i$ 的主导尺度是 $\sqrt{h}$，所以 $A_i^2$ 是 $h$，正好和 drift 项同阶。

接下来把 Eq. 5.42 代回 Eq. 5.41。为了看清结构，可以把结果拆成五项：

$$
p(x_{i+1},t_{i+1})=T_0+T_{\sqrt{h}}+T_f+T_{\mathrm{extra}}+T_{\mathrm{diff}}+O(h^{3/2}).
$$

第一项来自未扰动的 delta function：

$$
T_0
=
\left\langle
\int dx_i\,p(x_i,t_i)\delta(x_i-x_{i+1})
\right\rangle_{u_i}
=p(x_{i+1},t_i).
$$

这只是说：如果没有一步位移，$x_{i+1}$ 的概率就是旧时刻在同一位置的概率。

第二项来自 $O(\sqrt{h})$ 的随机位移：

$$
T_{\sqrt{h}}
=
\sqrt{h}
\left\langle
u_i
\int dx_i\,p(x_i,t_i)g(x_i)
\partial_{x_i}\delta(x_i-x_{i+1})
\right\rangle_{u_i}.
$$

在对 $u_i$ 取平均时，积分内部不含其他 $u_i$，所以这一项正比于 $\langle u_i\rangle$。由于 $u_i$ 是均值为 0 的标准高斯变量，

$$
\langle u_i\rangle=0,
$$

因此

$$
T_{\sqrt{h}}=0.
$$

这就是 Eq. 5.43 中 $\sqrt{h}$ 项消失的原因：单步噪声有正有负，平均后没有系统性一阶偏移。

第三项来自 deterministic drift $f(x_i)$：

$$
T_f
=
h
\int dx_i\,p(x_i,t_i)f(x_i)
\partial_{x_i}\delta(x_i-x_{i+1}).
$$

第四项来自 Eq. 5.40 中的 convention-dependent extra drift：

$$
T_{\mathrm{extra}}
=
h(1-\alpha)
\left\langle u_i^2\right\rangle
\int dx_i\,p(x_i,t_i)g(x_i)g'(x_i)
\partial_{x_i}\delta(x_i-x_{i+1}).
$$

因为 $\langle u_i^2\rangle=1$，所以

$$
T_{\mathrm{extra}}
=
h(1-\alpha)
\int dx_i\,p(x_i,t_i)g(x_i)g'(x_i)
\partial_{x_i}\delta(x_i-x_{i+1}).
$$

第五项来自二阶 delta 展开，也就是 diffusion 项：

$$
T_{\mathrm{diff}}
=
\frac{h}{2}
\left\langle u_i^2\right\rangle
\int dx_i\,p(x_i,t_i)g(x_i)^2
\partial_{x_i}^2\delta(x_i-x_{i+1}).
$$

同样用 $\langle u_i^2\rangle=1$，得到

$$
T_{\mathrm{diff}}
=
\frac{h}{2}
\int dx_i\,p(x_i,t_i)g(x_i)^2
\partial_{x_i}^2\delta(x_i-x_{i+1}).
$$

把这几项合在一起，就是 Eq. 5.43 的展开形式：

$$
\begin{aligned}
p(x_{i+1},t_{i+1})
&=
p(x_{i+1},t_i)\\
&\quad+
h\int dx_i\,p(x_i,t_i)f(x_i)
\partial_{x_i}\delta(x_i-x_{i+1})\\
&\quad+
h(1-\alpha)
\int dx_i\,p(x_i,t_i)g(x_i)g'(x_i)
\partial_{x_i}\delta(x_i-x_{i+1})\\
&\quad+
\frac{h}{2}
\int dx_i\,p(x_i,t_i)g(x_i)^2
\partial_{x_i}^2\delta(x_i-x_{i+1})
+O(h^{3/2}).
\end{aligned}
\tag{5.43}
$$

现在还要把 delta function 的导数处理掉。用两个 distribution 恒等式。对任意平滑函数 $\phi(x)$，

$$
\int dx\,\phi(x)\partial_x\delta(x-y)
=
-\partial_y\phi(y),
$$

以及

$$
\int dx\,\phi(x)\partial_x^2\delta(x-y)
=
\partial_y^2\phi(y).
$$

第一条来自一次分部积分，所以有负号；第二条来自两次分部积分，所以负号消失。

对 $T_f$，令

$$
\phi(x_i)=p(x_i,t_i)f(x_i),
$$

则

$$
T_f
=
-h\frac{\partial}{\partial x_{i+1}}
\left[
f(x_{i+1})p(x_{i+1},t_i)
\right].
$$

对 extra drift 项，令

$$
\phi(x_i)=p(x_i,t_i)g(x_i)g'(x_i),
$$

得到

$$
T_{\mathrm{extra}}
=
-h(1-\alpha)
\frac{\partial}{\partial x_{i+1}}
\left[
g(x_{i+1})g'(x_{i+1})p(x_{i+1},t_i)
\right].
$$

对 diffusion 项，令

$$
\phi(x_i)=p(x_i,t_i)g(x_i)^2,
$$

得到

$$
T_{\mathrm{diff}}
=
\frac{h}{2}
\frac{\partial^2}{\partial x_{i+1}^2}
\left[
g(x_{i+1})^2p(x_{i+1},t_i)
\right].
$$

因此 Eq. 5.44 应该读成：

$$
\begin{aligned}
p(x_{i+1},t_{i+1})
&=
p(x_{i+1},t_i)\\
&\quad+
h\Bigg(
-
\frac{\partial}{\partial x_{i+1}}
\left[
f(x_{i+1})p(x_{i+1},t_i)
\right]\\
&\qquad
-(1-\alpha)
\frac{\partial}{\partial x_{i+1}}
\left[
g(x_{i+1})g'(x_{i+1})p(x_{i+1},t_i)
\right]\\
&\qquad
+
\frac{1}{2}
\frac{\partial^2}{\partial x_{i+1}^2}
\left[
g(x_{i+1})^2p(x_{i+1},t_i)
\right]
\Bigg).
\end{aligned}
\tag{5.44}
$$

这里要特别注意括号。导数不是只作用在 $f$ 或 $g$ 上，而是作用在整个 probability flux 上，例如 $\partial_{x_{i+1}}[f(x_{i+1})p(x_{i+1},t_i)]$。如果把括号折叠掉，就会误读 Eq. 5.44。

最后把 Eq. 5.44 左右两边相减并除以 $h$：

$$
\frac{p(x_{i+1},t_{i+1})-p(x_{i+1},t_i)}{h}
=
\text{right-hand side terms}.
$$

令 $h\to 0$，并把 $x_{i+1}$ 重新记成连续变量 $x$，左边变成 $\partial_t p(x,t)$。于是得到一般 $\alpha$ convention 下的 Fokker-Planck equation：


$$
\frac{\partial}{\partial t}p(x,t)
=
-\frac{\partial}{\partial x}
\left[
\left(f(x)+(1-\alpha)g(x)g'(x)\right)p(x,t)
\right]
+\frac{1}{2}\frac{\partial^2}{\partial x^2}
\left[g(x)^2p(x,t)\right]. \tag{5.45}
$$

这就是 Eq. 5.38-5.40 的最终用途。它们负责把 multiplicative noise 的求值 convention 转化成 Fokker-Planck 方程里的 effective drift。整条推导可以压成一条线：

$$
\text{SDE step}
\rightarrow
\text{delta constraint}
\rightarrow
\text{expand to }O(h)
\rightarrow
\text{average over }u_i
\rightarrow
\text{integrate by parts}
\rightarrow
\text{Fokker-Planck equation}.
$$

---

## 十一、Itô 和 Stratonovich 的 Fokker-Planck 结果

当 $\alpha=1$ 时，对应 Itô prescription。Eq. 5.45 中 extra drift 消失：

$$
\frac{\partial}{\partial t}p(x,t)
=
-\frac{\partial}{\partial x}[f(x)p(x,t)]
+\frac{1}{2}\frac{\partial^2}{\partial x^2}
[g(x)^2p(x,t)]. \tag{5.46}
$$

当 $\alpha=1/2$ 时，对应 Stratonovich prescription。这一步不是重新推导一遍 Fokker-Planck equation，而是把 Eq. 5.45 里的 $\alpha$ 换成 $1/2$，然后用 product rule 整理。

从 Eq. 5.45 出发：

$$
\frac{\partial p}{\partial t}
=
-\partial_x
\left[
\left(f+\frac{1}{2}gg'\right)p
\right]
+
\frac{1}{2}\partial_x^2(g^2p).
$$

先把 drift 部分拆开：

$$
-\partial_x
\left[
\left(f+\frac{1}{2}gg'\right)p
\right]
=
-\partial_x(fp)
-\frac{1}{2}\partial_x(gg'p).
$$

所以除了 $-\partial_x(fp)$ 以外，剩下的 noise-related 部分是

$$
\frac{1}{2}\partial_x^2(g^2p)
-\frac{1}{2}\partial_x(gg'p).
$$

把 $\frac{1}{2}\partial_x$ 提出来：

$$
\frac{1}{2}
\left[
\partial_x^2(g^2p)-\partial_x(gg'p)
\right]
=
\frac{1}{2}
\partial_x
\left[
\partial_x(g^2p)-gg'p
\right].
$$

现在只需要整理括号里的项。由 product rule：

$$
\partial_x(g^2p)
=
2gg'p+g^2\partial_x p.
$$

因此

$$
\partial_x(g^2p)-gg'p
=
gg'p+g^2\partial_x p.
$$

右边可以重新写成

$$
g\left(g'p+g\partial_x p\right).
$$

而括号里的 $g'p+g\partial_xp$ 正好是

$$
\partial_x(gp)=g'p+g\partial_xp.
$$

所以

$$
\partial_x(g^2p)-gg'p
=
g\,\partial_x(gp).
$$

代回 noise-related 部分：

$$
\frac{1}{2}\partial_x^2(g^2p)
-\frac{1}{2}\partial_x(gg'p)
=
\frac{1}{2}
\partial_x
\left[
g\,\partial_x(gp)
\right].
$$

于是得到 Stratonovich 形式：

$$
\frac{\partial}{\partial t}p(x,t)
=
-\frac{\partial}{\partial x}[f(x)p(x,t)]
+\frac{1}{2}\frac{\partial}{\partial x}
\left(
g(x)\frac{\partial}{\partial x}[g(x)p(x,t)]
\right). \tag{5.47}
$$

这就是 Eq. 5.47 的来源。它把 Eq. 5.45 中的 extra drift 项 $-\frac{1}{2}\partial_x(gg'p)$ 和 diffusion 项 $\frac{1}{2}\partial_x^2(g^2p)$ 合并成一个更紧凑的 Stratonovich diffusion operator：

$$
\frac{1}{2}\partial_x\left(g\,\partial_x(gp)\right).
$$

直观地说，Stratonovich 形式把 “噪声强度随状态变化带来的 drift 修正” 吸收到扩散算子内部，所以它看起来更接近普通链式法则下的扩散项。

这两种形式在 additive noise 情况下等价，因为 $g$ 不依赖 $x$，所以 $g'(x)=0$。但在 multiplicative noise 情况下，它们不同。

这对城市增长很关键。城市人口增长常常写成比例增长形式，也就是噪声幅度依赖城市规模。例如后面的 growth models 会反复出现类似

$$
dS \sim S\,dW
$$

的结构。这时 $g(S)$ 不是常数，Fokker-Planck 方程中的 drift 和 diffusion 都会受到 convention 影响。

---

## 十二、这一章对后续 urban growth models 的作用

Chapter 5 为后续增长模型提供三条基础判断。

第一，随机增长不能只写成“确定性增长 + 噪声”就结束。只要噪声是 white noise，就必须说明 stochastic integral 的定义。

第二，multiplicative noise 会改变 drift。它不只是让轨迹更随机，还会通过 $g(x)g'(x)$ 这样的项改变概率密度的整体流动方向。

第三，Itô/Stratonovich 的选择要由建模语义决定。若当前状态先确定，随后随机迁移或增长冲击发生，Itô 更自然；若噪声有有限相关时间，代表某种平滑外部环境波动，Stratonovich 更自然。

这正好连接到城市增长。城市人口 $S_i(t)$ 的变化既有内部增长，也有迁移冲击；如果迁移冲击在每个时间步之后才作用于已知人口，那么 Chapter 9 采用 Itô convention 是合理的。否则，同一个形式的 SDE 会导出不同的 Fokker-Planck 方程和不同的城市人口分布演化。

---

## 十三、Eq. 5.38 可以压成的一句话

Eq. 5.38 的核心不是“把 $f_\alpha^i$ 近似成 $f(x_i)$”，而是：**由于一步随机位移的主导尺度是 $\sqrt{h}$，$f_\alpha^i$ 的修正只有 $O(\sqrt{h})$，乘上 drift 前面的 $h$ 后变成 $O(h^{3/2})$，因此在保留到 $O(h)$ 的 Fokker-Planck 推导中可以丢掉；但 $g_\alpha^i$ 的同阶修正乘上 $\sqrt{h}$ 后正好是 $O(h)$，所以必须保留，并最终产生 convention-dependent drift。**
