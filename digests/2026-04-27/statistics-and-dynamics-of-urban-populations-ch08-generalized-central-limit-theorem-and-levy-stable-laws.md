---
title: "Statistics and Dynamics of Urban Populations, Chapter 8: The generalized central limit theorem and Levy stable laws"
authors: "Marc Barthelemy, Vincent Verbavatz"
venue: "Oxford University Press (2023)"
date_read: "2026-04-27"
topics: ["urban growth", "central limit theorem", "generalized central limit theorem", "Levy stable laws", "heavy tails", "migration shocks"]
source: "pdfs/2026-04-24/statistics-and-dynamics-of-urban-populations/08-the-generalized-central-limit-theorem-and-levy-stable-laws.mineru/hybrid_auto/08-the-generalized-central-limit-theorem-and-levy-stable-laws.md"
---

# Statistics and Dynamics of Urban Populations, Chapter 8：Generalized Central Limit Theorem and Levy Stable Laws

## 精读笔记

---

## 一、这一章在全书动力学线里的位置

Chapter 6 和 Chapter 7 都在讨论城市增长模型。Chapter 6 主要问：

$$
\text{multiplicative growth 能不能生成 Zipf-like city-size distribution?}
$$

Chapter 7 进一步加入 migration，问：

$$
\text{城市之间的人口交换如何改变增长分布和规模分布?}
$$

Chapter 8 暂时不直接写城市增长方程，而是补一个概率论工具。这个工具是后面 Chapter 9 的前提。

作者的目标是说明：如果 interurban migration flows 不是由许多小而独立的迁移事件平均出来，而是由少数巨大迁移冲击主导，那么 ordinary central limit theorem 不再适用。此时，累加很多迁移流以后，极限分布不一定是 Gaussian，而可能是 Levy stable law。

所以这一章的主线可以写成：

$$
\begin{aligned}
&\text{finite-variance sums}\\
&\rightarrow \text{ordinary CLT}\\
&\rightarrow \text{Gaussian attraction}\\
&\rightarrow \text{heavy-tail failure of CLT}\\
&\rightarrow \text{stable-law attraction}\\
&\rightarrow \text{generalized CLT}\\
&\rightarrow \text{rare large migration shocks}.
\end{aligned}
$$

这章没有承担解释功能的经验图表。它主要由公式推进，因此笔记也按公式逐步展开。

为了避免公式之间变成孤立条目，这章可以按三层逻辑读。第一层是 ordinary CLT：在有限方差下，加总量的中心波动为什么变成 Gaussian。第二层是 failure of CLT：当 tail 太厚、方差不存在时，$\sqrt{N}$ scaling 为什么不再合适。第三层是 generalized CLT：在 heavy-tail 情况下，新的稳定吸引子是什么，以及它为什么会成为后面 migration shock 建模的数学语言。

### 1.1 本章符号口径

本章是后面 Chapter 9-10 的概率论准备，所以符号需要和后面区分开。

$X_i$ 表示被加总的微观随机变量，$S_N=\sum_{i=1}^NX_i$ 表示总和。这里的 $S_N$ 不是城市人口 $S_i$。

$\alpha$ 是 heavy-tail exponent，也是 stable-law index。若 density tail 写成 $\rho(x)\sim x^{-1-\alpha}$，则 survival tail 是 $\mathbb{P}(|X|>x)\sim x^{-\alpha}$。

$\beta$ 在 stable-law characteristic function 中表示 skewness parameter，控制左右尾不对称。它不是 Chapter 9-10 的 migration amplitude exponent $\beta$。

$\zeta_\alpha$ 表示 $\alpha$-stable limiting random variable。它和 Chapter 9-10 的 Levy noise 相关，但本章里它先作为 generalized CLT 的极限变量出现。

$\mu$ 在 generalized CLT 的分类里表示 finite mean 或 deterministic trend，例如 $n\mu$。它不是 Chapter 10 中 generic fractional equation 的 Levy index $\mu$。

Standard Gaussian CDF 在本笔记中统一写成 $\Phi$，避免和 Chapter 9 的 neighbor number $\mathcal{N}(i)$ 混淆。

---

## 二、为什么先从 central limit theorem 开始

Central limit theorem 的核心意义不是“很多东西相加会变成正态”这么简单。它真正说的是：在一组很强但常见的条件下，微观随机变量的许多细节会被加总过程洗掉。

假设每个个体行为由随机变量 $X_i$ 表示。如果 $X_i$ 独立同分布，并且均值和方差有限，那么大量 $X_i$ 相加以后，最终只剩下两个信息：

$$
\text{mean}
\quad
\text{and}
\quad
\text{variance}.
$$

这就是为什么 CLT 对社会系统很重要。不同个体可能有很复杂的异质性，但只要满足有限方差和足够弱相关，宏观加总量就会出现相对 universal 的 Gaussian fluctuation。

但这也是本章要突破的地方。如果城市迁移流有 heavy tail，尤其 tail exponent 小于 2，那么方差可能不存在。此时 CLT 的关键假设断裂，宏观加总量不会自动走向 Gaussian。

因此，作者不是为了复习概率论而讲 CLT，而是为了先把“Gaussian 为什么通常成立”说清楚。只有知道 Gaussian 成立依赖哪些假设，后面才能准确理解 Levy stable laws 不是额外的数学装饰，而是在有限方差假设失败时替代 Gaussian 的极限语言。

---

## 三、law of large numbers：先看平均值为什么稳定

这一节先解决最基础的问题：很多随机变量相加以后，平均值是否会稳定下来。这个问题比 CLT 更弱，因为它只关心 sample average 是否靠近 true mean，还不关心偏离均值的分布形状。作者先从这里开始，是为了把“平均值稳定”和“波动呈 Gaussian”分开。

### 3.1 Eq. 8.1：定义加总量

设有 $N$ 个 independent identically distributed random variables：

$$
X_1,X_2,\ldots,X_N.
$$

每个变量有有限均值

$$
m=\mathbb{E}(X_i)
$$

和有限方差

$$
\sigma^2=\mathbb{V}(X_i).
$$

作者先定义总和：

$$
S_N=\sum_{i=1}^{N}X_i.
\tag{8.1}
$$

这里 $S_N$ 是总量，不是平均量。比如在城市语境里，$X_i$ 可以理解成某类微观迁移贡献，$S_N$ 就是很多贡献加总后的总迁移流或总增长冲击。

定义 $S_N$ 之后，下一步自然要问：如果我们不看总量，而看平均贡献 $S_N/N$，它会不会随着样本数增加而稳定到某个值？这就是 Eq. 8.2 要回答的问题。

### 3.2 Eq. 8.2：law of large numbers 的意思

law of large numbers 说：

$$
\mathbb{P}
\left(
\left|
\frac{S_N}{N}-m
\right|>\epsilon
\right)
\rightarrow0.
\tag{8.2}
$$

这句话要分三层读。

第一，$S_N/N$ 是样本平均：

$$
\frac{S_N}{N}
=
\frac{1}{N}\sum_{i=1}^{N}X_i.
$$

第二，$m$ 是真实期望。式子里的

$$
\left|
\frac{S_N}{N}-m
\right|
$$

衡量样本平均偏离真实均值的程度。

第三，Eq. 8.2 说：当 $N$ 越来越大时，样本平均偏离真实均值超过任意固定阈值 $\epsilon$ 的概率趋向 0。

所以 law of large numbers 的作用是说明 average 的稳定性：

$$
\text{many observations}
\Rightarrow
\text{sample average approaches expected value}.
$$

它还没有告诉我们 fluctuation 的形状。它只告诉我们平均值会靠近 $m$。

为了证明这个稳定性，作者需要一个能把“偏离均值很远的概率”压住的工具。Markov inequality 就承担这个角色。它本身很粗，但足以推出 law of large numbers。

### 3.3 Eq. 8.3：Markov inequality

证明 law of large numbers 可以从 Markov inequality 开始。对任意非负随机变量 $Y$，有：

$$
\mathbb{P}(Y>a)
\leq
\frac{\langle Y\rangle}{a}.
\tag{8.3}
$$

这条不等式的直觉很简单。如果 $Y$ 的平均值很小，那么 $Y$ 经常取很大值的概率不能太高。否则平均值会被拉大。

它的作用是把一个 probability bound 转换成一个 expectation bound：

$$
\text{tail probability}
\leq
\frac{\text{mean size}}{\text{threshold}}.
$$

Markov inequality 还没有使用 $S_N$ 的结构。它只是一个通用概率界。为了把它变成关于 sample average 的结论，作者把非负变量 $Y$ 具体选成 squared deviation，也就是 $(S_N-mN)^2$。这样就进入 Chebyshev inequality。

### 3.4 Eq. 8.4：从 Markov 到 Chebyshev

作者把 Markov inequality 用到变量

$$
Y=(S_N-mN)^2
$$

上。这个变量非负，所以可以用 Eq. 8.3。

令 threshold 为

$$
a=t^2.
$$

于是

$$
\mathbb{P}\left((S_N-mN)^2>t^2\right)
\leq
\frac{
\mathbb{E}\left[(S_N-mN)^2\right]
}{t^2}.
$$

左边可以改写为

$$
\mathbb{P}\left(|S_N-mN|>t\right).
$$

右边的期望是 $S_N$ 的方差。因为 $S_N$ 是独立变量之和：

$$
\mathbb{V}(S_N)
=
\sum_{i=1}^{N}\mathbb{V}(X_i)
=
N\sigma^2.
$$

所以得到 Chebyshev inequality：

$$
\mathbb{P}\left(|S_N-mN|>t\right)
\leq
\frac{N\sigma^2}{t^2}.
\tag{8.4}
$$

这一步说明：总和 $S_N$ 的 fluctuation scale 是 $\sqrt{N}$ 级别。因为当 $t$ 和 $\sqrt{N}$ 同阶时，右边才是常数量级。

Chebyshev inequality 已经把问题从抽象的 $Y$ 拉回到 $S_N$。剩下只需要把 threshold $t$ 选成 $\epsilon N$，就能把总量偏差转换成平均值偏差。

### 3.5 从 Eq. 8.4 推回 Eq. 8.2

为了证明样本平均收敛到 $m$，我们要控制

$$
\mathbb{P}
\left(
\left|
\frac{S_N}{N}-m
\right|>\epsilon
\right).
$$

这个事件等价于

$$
|S_N-mN|>\epsilon N.
$$

因此在 Eq. 8.4 里取

$$
t=\epsilon N.
$$

得到

$$
\mathbb{P}
\left(
\left|
\frac{S_N}{N}-m
\right|>\epsilon
\right)
\leq
\frac{N\sigma^2}{\epsilon^2N^2}
=
\frac{\sigma^2}{\epsilon^2N}.
$$

当

$$
N\to\infty
$$

时，右边趋向 0，于是 Eq. 8.2 成立。

这一段的关键是：law of large numbers 依赖有限方差。只有当 $\sigma^2$ 有限时，Chebyshev bound 才能给出这个收敛结论。

到这里，作者只证明了 average 会稳定。接下来的问题更细：虽然 $S_N/N$ 会靠近 $m$，但它如何围绕 $m$ 波动？波动幅度是什么？波动分布是什么？这就从 law of large numbers 进入 central limit theorem。

---

## 四、central limit theorem：平均值稳定以后，波动形状是什么

这一节承接上一节的结果。law of large numbers 告诉我们 $S_N$ 的主导项是 $Nm$，Chebyshev inequality 暗示偏离量的自然尺度是 $\sqrt{N}$。CLT 把这两点合起来：先减掉 deterministic mean $Nm$，再除以 stochastic scale $\sigma\sqrt{N}$，然后看剩下的 normalized fluctuation 会收敛到什么分布。

### 4.1 Eq. 8.5：中心极限定理的分布形式

law of large numbers 只说明

$$
\frac{S_N}{N}
\rightarrow
m.
$$

但它没有说明偏离 $m$ 的 fluctuation 如何分布。CLT 进一步回答这个问题。

作者写。为了避免和后面 Chapter 9 的 neighbor number $\mathcal{N}(i)$ 混淆，这里把 standard Gaussian CDF 记为 $\Phi$：

$$
\mathbb{P}
\left(
\frac{S_N-Nm}{\sigma\sqrt{N}}
<
z
\right)
\rightarrow
\Phi(z)
=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{z}
e^{-y^2/2}\,dy.
\tag{8.5}
$$

这里

$$
\frac{S_N-Nm}{\sigma\sqrt{N}}
$$

是 centered and normalized sum。

它做了两件事。

第一，减去均值：

$$
S_N-Nm.
$$

因为 $S_N$ 的平均值是 $Nm$。

第二，除以 fluctuation scale：

$$
\sigma\sqrt{N}.
$$

因为独立变量加总时方差相加：

$$
\mathbb{V}(S_N)=N\sigma^2.
$$

所以标准差是

$$
\sqrt{N\sigma^2}
=
\sigma\sqrt{N}.
$$

Eq. 8.5 说：这个标准化后的变量，其 cumulative distribution function 收敛到 standard Gaussian CDF。

Eq. 8.5 用的是 one-sided cumulative probability。为了更直观地看它如何描述一个完整分布，作者马上把它改写成 interval probability，这就是 Eq. 8.6。

### 4.2 Eq. 8.6：区间概率形式

Eq. 8.5 的等价表达是：

$$
\mathbb{P}
\left(
a
<
\frac{S_N-Nm}{\sigma\sqrt{N}}
<
b
\right)
\rightarrow
\Phi(b)-\Phi(a).
\tag{8.6}
$$

这只是把 cumulative probability 变成 interval probability。

如果一个变量的 CDF 是 $\Phi$，那么它落在区间 $(a,b)$ 的概率就是：

$$
\Phi(b)-\Phi(a).
$$

有了 CDF 和区间概率，作者再用更紧凑的概率论符号表达同一个结论。Eq. 8.7 不再逐个写概率，而是直接说 normalized sum 的 law 收敛到 Gaussian law。

### 4.3 Eq. 8.7：convergence in law

作者把 CLT 写成更紧凑的形式：

$$
\frac{S_N-Nm}{\sqrt{N}\sigma}
\xrightarrow{\mathcal{L}}
Z,
\qquad
Z\sim\mathrm{Normal}(0,1).
\tag{8.7}
$$

这里 $\xrightarrow{\mathcal{L}}$ 表示 convergence in law，也就是 distributional convergence。它不是说每个样本路径都逐点收敛，而是说标准化变量的概率分布越来越接近 standard normal distribution。

这一点对城市系统很重要。CLT 不预测某个城市或某次迁移事件的具体值。它预测的是许多随机贡献加总以后的统计形状。

下一节的作用是解释为什么这个极限会是 Gaussian。作者不是直接引用 CLT，而是用 characteristic function 展开一遍证明。这样后面推广到 infinite-variance 情况时，我们能清楚看到普通证明究竟在哪一步断裂。

---

## 五、用 characteristic function 证明 CLT

这一节的叙事功能是找出 Gaussian 的来源。证明的逻辑很短：sum 在 characteristic function 空间里变成乘积；有限方差让 characteristic function 在零点附近有二阶展开；$N$ 次乘积的极限变成 $e^{-t^2/2}$。这三步合起来就是 ordinary CLT。

### 5.1 Eq. 8.8：characteristic function 是什么

作者使用 characteristic function：

$$
\varphi_X(t)
=
\mathbb{E}\left(e^{itX}\right).
\tag{8.8}
$$

它可以理解成 probability distribution 的 Fourier transform。

characteristic function 有两个关键性质。

第一，它唯一决定一个 probability distribution。也就是说，如果两个随机变量有同一个 characteristic function，它们就有同一个 distribution。

第二，独立随机变量之和的 characteristic function 等于各自 characteristic function 的乘积。若

$$
S=X_1+X_2,
$$

且 $X_1$ 和 $X_2$ 独立，则

$$
\varphi_S(t)
=
\varphi_{X_1}(t)\varphi_{X_2}(t).
$$

这就是为什么 characteristic function 特别适合处理 sums。

有了这个工具，下一步就是把 CLT 中的 normalized sum 写成 characteristic function。这里要先标准化单个变量，避免均值和方差在公式里反复出现。

### 5.2 Eq. 8.9：总和的 characteristic function

为了避免均值和方差符号干扰，可以先把变量标准化：

$$
Z_i=\frac{X_i-m}{\sigma}.
$$

那么

$$
\mathbb{E}(Z_i)=0,
\qquad
\mathbb{V}(Z_i)=1.
$$

CLT 中的标准化总和可以写成

$$
U
=
\frac{S_N-Nm}{\sigma\sqrt{N}}
=
\frac{1}{\sqrt{N}}\sum_{i=1}^{N}Z_i.
$$

因为 $Z_i$ 独立同分布，$U$ 的 characteristic function 是：

$$
\varphi_U(t)
=
\left[
\varphi_Z\left(\frac{t}{\sqrt{N}}\right)
\right]^N.
\tag{8.9}
$$

直观上，每个变量被缩放了 $1/\sqrt{N}$，所以在 characteristic function 里输入变成 $t/\sqrt{N}$；然后 $N$ 个独立变量相加，所以整体是 $N$ 次乘积。

现在问题变成：当 $N$ 很大时，$\varphi_Z(t/\sqrt{N})$ 在零点附近长什么样？这里 finite variance 第一次真正进入证明。

### 5.3 Eq. 8.10：有限方差如何进入证明

当 $Z$ 有零均值和单位方差时，它的 characteristic function 在 $0$ 附近可以展开为：

$$
\varphi_Z(s)
=
1
+is\mathbb{E}(Z)
-\frac{s^2}{2}\mathbb{E}(Z^2)
+o(s^2).
$$

因为

$$
\mathbb{E}(Z)=0,
\qquad
\mathbb{E}(Z^2)=1,
$$

所以

$$
\varphi_Z(s)
=
1-\frac{s^2}{2}+o(s^2).
$$

令

$$
s=\frac{t}{\sqrt{N}},
$$

就得到：

$$
\varphi_Z(t/\sqrt{N})
=
1-\frac{t^2}{2N}+o(1/N).
\tag{8.10}
$$

这一行是 CLT 证明的核心。它使用了二阶 Taylor expansion，而二阶项存在的前提就是 variance finite。

如果 $\mathbb{V}(X)$ 不存在，characteristic function 在 $0$ 附近不一定有正常的二阶展开。普通 CLT 就会失效。

Eq. 8.10 给出了单个缩小变量的近似。接下来把这个近似放回 $N$ 次乘积，就会看到 Gaussian characteristic function 自动出现。

### 5.4 Eq. 8.11：从乘积到 Gaussian

把 Eq. 8.10 代入 Eq. 8.9：

$$
\varphi_U(t)
=
\left[
1-\frac{t^2}{2N}+o(1/N)
\right]^N.
$$

使用极限

$$
\left(1+\frac{x}{N}\right)^N
\rightarrow
e^x,
$$

得到：

$$
\varphi_U(t)
\simeq
e^{-t^2/2}.
\tag{8.11}
$$

而

$$
e^{-t^2/2}
$$

正是 standard Gaussian distribution 的 characteristic function。因此，标准化总和收敛到 Gaussian。

这个证明把 CLT 的假设暴露得很清楚：独立性让 characteristic functions 相乘，有限方差让二阶展开成立。只要其中一个条件出问题，Gaussian attraction 就不再是自动结论。

### 5.5 CLT 的两个关键假设

作者强调 CLT 至少依赖两个条件。

第一，变量要 independent，或者至少 correlations 衰减得足够快。如果 $X_i$ 和 $X_j$ 长程相关，那么总方差不再简单等于 $N\sigma^2$，加总后的极限也可能改变。

第二，变量要有 finite variance。这个条件保证 Eq. 8.10 中的二阶展开成立。

对 heavy-tail distribution 来说，第二个条件最容易失败。如果 tail decay 很慢，比如

$$
\rho(x)\sim x^{-1-\alpha}
$$

且 $\alpha<2$，则 variance diverges。此时不能把所有个体冲击都压缩成 Gaussian noise。

不过，即使 CLT 成立，也需要注意它描述的是中心区域，而不是所有极端尾部。这个限定解释了为什么本章下一步会从“中心波动”转向“rare large events”。

### 5.6 “central” 的含义

作者还提醒：CLT 主要描述 distribution 的中心区域，而不是所有 tail。

即使变量方差有限，有限 $N$ 下的 sum distribution 也只有中心区域会比较快接近 Gaussian。远尾区域可能仍然保留原始 distribution 的痕迹。

所以 CLT 的实际含义是：

$$
\text{typical fluctuations}
\sim
\sigma\sqrt{N}
\quad
\text{become Gaussian}.
$$

它不保证 rare extreme events 也马上变成 Gaussian。

这为后面广义 CLT 埋下伏笔：如果 rare events 不只是尾部修正，而是能主导整个 sum，那么 Gaussian approximation 就不再是正确的宏观语言。

因此，前半章到这里完成了一个闭环：ordinary CLT 是有限方差、弱相关、小冲击加总下的极限理论。后半章要处理的是相反情形：单个冲击的 tail 太厚，以至于 rare large events 不能被平均掉。

---

## 六、为什么要 beyond CLT

这一节开始转向 generalized CLT。作者不是先给新定理，而是先指出 ordinary CLT 失败的具体数学原因：power-law tail 会让 variance diverge。只要 variance 不存在，$\sigma\sqrt{N}$ 这个 normalization 就失去了基础。

### 6.1 Eq. 8.12：power-law tail

作者接下来考虑 broad distribution：

$$
\rho(x)
\sim
\frac{1}{x^{1+\alpha}}.
\tag{8.12}
$$

这里要区分 density tail 和 survival tail。

如果 density 是

$$
\rho(x)\sim x^{-1-\alpha},
$$

那么 survival probability 是

$$
\mathbb{P}(X>x)
=
\int_x^\infty \rho(u)\,du
\sim
x^{-\alpha}.
$$

所以 $\alpha$ 经常被称为 tail exponent，但严格说它对应 survival tail exponent；density 的幂指数是 $1+\alpha$。

moment 是否存在由 $\alpha$ 决定。对正尾来说，

$$
\mathbb{E}(X^q)
\sim
\int^\infty x^q x^{-1-\alpha}\,dx
=
\int^\infty x^{q-1-\alpha}\,dx.
$$

这个积分在无穷远处收敛的条件是：

$$
q-1-\alpha<-1,
$$

也就是

$$
q<\alpha.
$$

因此：

$$
\text{mean finite}
\Leftrightarrow
\alpha>1,
$$

而

$$
\text{variance finite}
\Leftrightarrow
\alpha>2.
$$

本章关心的是 $\alpha<2$，也就是 variance 不存在的情形。

一旦 variance 不存在，前面 CLT 里的两个动作都需要重做：不能用 $Nm$ 和 $\sigma\sqrt{N}$ 机械地 center/scale，也不能期待 Gaussian 是唯一吸引子。于是作者回到最原始的 sum。

### 6.2 Eq. 8.13：仍然从总和开始

即使 CLT 失效，问题仍然是 sum：

$$
S_N
=
\sum_{i=1}^{N}X_i.
\tag{8.13}
$$

区别在于：现在 $X_i$ 可能有 infinite variance，甚至当 $\alpha<1$ 时 mean 也不存在。

因此不能再假设

$$
S_N
\approx
Nm
+\sigma\sqrt{N}\eta.
$$

我们需要重新寻找正确的 centering 和 scaling。

这就是 Eq. 8.14 的作用。它不再预设 centering 是 $Nm$、scale 是 $\sqrt{N}$，而是把它们写成待确定的 $b_N$ 和 $a_N$。

### 6.3 Eq. 8.14：新的 normalization

作者定义 normalized variable：

$$
\xi_N
=
\frac{S_N-b_N}{a_N}.
\tag{8.14}
$$

这里 $b_N$ 是 shift，也就是 centering term；$a_N$ 是 scale，也就是 width。

在 ordinary CLT 中，这两个量分别是：

$$
b_N=Nm,
\qquad
a_N=\sigma\sqrt{N}.
$$

但在 heavy-tail 情况下，这两个量不一定是这个形式。

尤其当 $\alpha<2$ 时，typical fluctuation scale 不再是 $\sqrt{N}$，而会变成

$$
N^{1/\alpha}.
$$

因为 $\alpha<2$ 时：

$$
\frac{1}{\alpha}
>
\frac{1}{2},
$$

所以 broad distribution 的 fluctuation 比 Gaussian scaling 更大。

有了新的 normalization，下一步才谈得上极限分布。Eq. 8.15 表达的就是：是否存在某种 $a_N,b_N$，能让 normalized sum 收敛到一个稳定的非 Gaussian 极限。

### 6.4 Eq. 8.15：寻找极限分布

作者希望 $\xi_N$ 的分布在 $N$ 很大时收敛到某个稳定极限：

$$
\lim_{N\rightarrow\infty}
\rho_{\xi_N}(x)
=
\rho(x).
\tag{8.15}
$$

这句话和 CLT 的逻辑完全平行。

CLT 是说：

$$
\frac{S_N-Nm}{\sigma\sqrt{N}}
\Rightarrow
\text{Gaussian}.
$$

广义 CLT 要问：

$$
\frac{S_N-b_N}{a_N}
\Rightarrow
\text{what?}
$$

答案就是 Levy stable law。

但这个答案不能凭空给出。下一节用 decimation 思路说明：如果一个极限分布在加总和重缩放后保持同一类型，那么它的 characteristic function 会被强约束，最终只能落到 stable-law family。

---

## 七、decimation 思路：把同一个总和拆成不同 block

这一节是从“我们希望有稳定极限”走向“稳定极限必须满足什么方程”的桥梁。核心想法是：同一个大总和 $S_N$ 可以直接看，也可以先分成 block 再加总。如果最终极限不依赖我们怎么分 block，那么 characteristic function 必须具有 scale-invariant 结构。

### 7.1 为什么要用 block 分解

作者使用一个 decimation idea。它和 renormalization 的思想很像：同一个大系统可以被分成不同尺度的 block；如果极限分布真的是 stable 的，那么换一种 block size 不应该改变最终的极限形式。

令

$$
N=m\times n.
$$

为了配合后面的公式，可以把 $S_N$ 看成 $N/n$ 个 independent block 的和，每个 block 内有 $n$ 个变量。于是每个 block 的和都和 $S_n$ 同分布。

因此：

$$
S_N
=
\sum_{k=1}^{N/n}S_n^{(k)},
$$

其中 $S_n^{(k)}$ 是第 $k$ 个 block 的 partial sum。

block 分解只是重写同一个总和。为了让这个重写变成方程，需要把“总和的分布”转到 characteristic function 空间，因为独立 block 相加在那里会变成乘法。

### 7.2 Eq. 8.16：极限变量的 characteristic function

设 $\xi_N$ 的 limiting characteristic function 是：

$$
\phi_{\xi_N}(\omega)
=
\phi(\omega)
=
\mathbb{E}\left(e^{i\omega x}\right).
\tag{8.16}
$$

这里 $\phi$ 被假设为 large-$N$ 极限下的 characteristic function，因此不再显式依赖 $N$。

这一步是在表达 stable limit 的要求：

$$
\text{after correct rescaling, the distribution stops changing with }N.
$$

既然 $\phi$ 描述的是 normalized variable $\xi_N$，下一步要把它翻译回 unnormalized sum $S_N$。这样才能比较“直接看 $S_N$”和“分 block 看 $S_N$”这两种写法。

### 7.3 Eq. 8.17：从 $\xi_N$ 回到 $S_N$

由 Eq. 8.14：

$$
\xi_N
=
\frac{S_N-b_N}{a_N}.
$$

等价地：

$$
S_N
=
a_N\xi_N+b_N.
$$

因此 $S_N$ 的 characteristic function 是：

$$
\phi_{S_N}(\omega)
=
\mathbb{E}\left(e^{i\omega S_N}\right)
=
\mathbb{E}\left(e^{i\omega(a_N\xi_N+b_N)}\right).
$$

把 deterministic shift 拿出来：

$$
\phi_{S_N}(\omega)
=
e^{ib_N\omega}
\mathbb{E}\left(e^{i(a_N\omega)\xi_N}\right).
$$

最后得到：

$$
\phi_{S_N}(\omega)
=
e^{ib_N\omega}
\phi(a_N\omega).
\tag{8.17}
$$

这一步的意义是：如果我们知道 rescaled limit 的 characteristic function $\phi$，就能写出 unscaled sum $S_N$ 的 characteristic function。

现在已经有了直接描述 $S_N$ 的方式。接下来换一个角度：把同一个 $S_N$ 写成很多个 $S_n$ block 的和，再利用 independence 把 characteristic function 写成乘积。

### 7.4 Eq. 8.18-Eq. 8.19：同一个 $S_N$ 也可以由 block 相加得到

因为 $S_N$ 是 $N/n$ 个 block sum 的和，而每个 block sum 都和 $S_n$ 同分布，所以独立加总给出：

$$
\phi_{S_N}(\omega)
=
\left[\phi_{S_n}(\omega)\right]^{N/n}.
$$

根据 Eq. 8.17，block sum $S_n$ 的 characteristic function 是：

$$
\phi_{S_n}(\omega)
=
e^{ib_n\omega}
\phi(a_n\omega).
$$

所以：

$$
\phi_{S_N}(\omega)
=
e^{i(N/n)b_n\omega}
\left[
\phi(a_n\omega)
\right]^{N/n}.
\tag{8.18-8.19}
$$

这一步是稳定性推导的核心。对于同一个 $S_N$，我们有两种描述。

第一种是直接使用 $N$ 的 normalization：

$$
\phi_{S_N}(\omega)
=
e^{ib_N\omega}\phi(a_N\omega).
$$

第二种是先把它分成 block，再把 block characteristic functions 相乘：

$$
\phi_{S_N}(\omega)
=
e^{i(N/n)b_n\omega}
\left[
\phi(a_n\omega)
\right]^{N/n}.
$$

如果极限分布真的是 stable 的，那么任意选择 block size $n$ 都不应该改变最终表达。

这句话把直觉变成了下一步的数学条件：对任意 coarse-graining scale $n$，表达式都应保持不变。因此作者对 $n$ 求导并令导数为 0。

### 7.5 Eq. 8.20：对 block size 的不变性要求

作者把这种不变性写成：

$$
\frac{\partial}{\partial n}
\left\{
e^{i(N/n)b_n\omega}
\left[
\phi(a_n\omega)
\right]^{N/n}
\right\}
=0.
\tag{8.20}
$$

这不是说真实的 $n$ 一定连续，而是把 large-$n$ 下的 block size 当作连续变量处理。物理直觉是：

$$
\text{same large sum}
\quad
\text{should not depend on arbitrary coarse-graining scale}.
$$

这和 renormalization 的思路一致：当我们改变观察尺度时，极限分布的形式应该保持不变，只允许 shift 和 scale 改变。

Eq. 8.20 是推导 stable law 的入口。下一节要做的只是代数整理：把这个 scale-invariance condition 转换成 $\phi$ 必须满足的一阶微分方程。

---

## 八、从 block 不变性推导 stable law 的 characteristic function

这一节是全章最技术的部分。它的叙事目标不是让每个代数变形都显得重要，而是说明：block 不变性会强迫 characteristic function 具有 $|\omega|^\alpha$ 的指数形式。这个形式就是 Levy stable laws 的来源。

### 8.1 Eq. 8.21：对数求导

为了推 Eq. 8.21，先对 Eq. 8.20 中的表达取 logarithm。令

$$
L(n)
=
\log\phi_{S_N}(\omega).
$$

由 Eq. 8.18-Eq. 8.19：

$$
L(n)
=
i\frac{N}{n}b_n\omega
+
\frac{N}{n}\log\phi(a_n\omega).
$$

引入

$$
d_n=\frac{b_n}{n},
$$

则

$$
\frac{N}{n}b_n
=
Nd_n.
$$

所以：

$$
L(n)
=
iNd_n\omega
+
\frac{N}{n}\log\phi(a_n\omega).
$$

对 $n$ 求导，并令结果为 0：

$$
\frac{dL}{dn}
=
iN\omega\frac{\partial d_n}{\partial n}
+
N
\left[
\frac{1}{n}
\frac{\phi'(a_n\omega)}{\phi(a_n\omega)}
\omega\frac{\partial a_n}{\partial n}
-
\frac{1}{n^2}\log\phi(a_n\omega)
\right]
=0.
$$

把

$$
\tilde{\omega}=a_n\omega
$$

代入。因为

$$
\omega\frac{\partial a_n}{\partial n}
=
\frac{\tilde{\omega}}{a_n}
\frac{\partial a_n}{\partial n},
$$

再整体整理，就得到：

$$
\frac{\phi'(\tilde{\omega})\tilde{\omega}}
{\phi(\tilde{\omega})}
-
\frac{a_n/n}{\partial a_n/\partial n}
\log\phi(\tilde{\omega})
+
i\tilde{\omega}n
\frac{\partial d_n/\partial n}
{\partial a_n/\partial n}
=0.
\tag{8.21}
$$

这一步看起来复杂，但它只是在表达一件事：如果 block size $n$ 改变，scale $a_n$ 和 shift $b_n$ 必须以某种方式一起改变，才能让整体 limiting distribution 不变。

Eq. 8.21 里还混着 $a_n$、$b_n$、$\phi$ 三类对象。为了看清结构，作者把 $a_n$ 和 $b_n$ 的变化率压缩成两个 scaling functions $C_1(n)$ 和 $C_2(n)$。

### 8.2 Eq. 8.22：把 scaling 变化率压缩成两个常数

作者定义：

$$
\left\{
\begin{array}{l}
\dfrac{a_n/n}{\partial a_n/\partial n}=C_1(n),\\[6pt]
-n\dfrac{\partial d_n/\partial n}{\partial a_n/\partial n}=C_2(n).
\end{array}
\right.
\tag{8.22}
$$

第一个量 $C_1(n)$ 描述 scale $a_n$ 随 block size $n$ 增长的速度。

如果 $a_n$ 是 power law：

$$
a_n\propto n^\gamma,
$$

那么

$$
\frac{\partial a_n}{\partial n}
\propto
\gamma n^{\gamma-1},
$$

于是

$$
\frac{a_n/n}{\partial a_n/\partial n}
=
\frac{1}{\gamma}.
$$

所以 $C_1$ 本质上是 scaling exponent 的倒数。

第二个量 $C_2(n)$ 描述 shift $b_n$ 的变化如何和 scale $a_n$ 的变化耦合。它控制最后 characteristic function 里的 location term。

为了得到一个不依赖 $n$ 的 limiting law，作者要求：

$$
C_1(n)\rightarrow C_1,
\qquad
C_2(n)\rightarrow C_2.
$$

也就是说，大尺度下的 renormalization flow 要收敛到固定的 scaling constants。

一旦 $C_1$ 和 $C_2$ 在大尺度下变成常数，我们就可以先求出 normalization 本身如何随 $n$ 变化。作者先处理 scale $a_n$，因为它决定 fluctuation width。

### 8.3 Eq. 8.23：求 $a_n$ 的 scaling

由 Eq. 8.22 第一行：

$$
\frac{a_n/n}{\partial a_n/\partial n}
=
C_1.
$$

移项得到：

$$
\frac{\partial a_n}{\partial n}
=
\frac{a_n}{n}\frac{1}{C_1}.
\tag{8.23}
$$

这是一个简单的一阶微分方程：

$$
\frac{1}{a_n}\frac{\partial a_n}{\partial n}
=
\frac{1}{C_1}\frac{1}{n}.
$$

对 $n$ 积分：

$$
\log a_n
=
\frac{1}{C_1}\log n+\text{constant}.
$$

因此：

$$
a_n
\propto
n^{1/C_1}.
$$

这就是新的 fluctuation scale。

普通 CLT 中

$$
a_n\propto\sqrt{n},
$$

对应

$$
\frac{1}{C_1}=\frac{1}{2},
\qquad
C_1=2.
$$

heavy-tail 情况下，后面会把

$$
C_1=\alpha
$$

所以

$$
a_n\propto n^{1/\alpha}.
$$

scale $a_n$ 解决的是 fluctuation 的宽度。接下来 shift $b_n$ 解决的是 distribution 的位置，也就是是否需要减掉类似 $n\mu$ 的 deterministic trend。

### 8.4 Eq. 8.24：求 shift 的 scaling

由 Eq. 8.22 第二行：

$$
-n
\frac{\partial d_n/\partial n}
{\partial a_n/\partial n}
=
C_2.
$$

移项得到：

$$
\frac{\partial d_n}{\partial n}
=
-
\frac{C_2}{n}
\frac{\partial a_n}{\partial n}.
\tag{8.24}
$$

因为

$$
b_n=nd_n,
$$

所以求出 $d_n$ 后还要乘回 $n$。在 leading order 下，作者得到：

$$
a_n\propto n^{1/C_1},
\qquad
b_n\propto n^{1/C_1}+bn.
$$

这里 $bn$ 是线性漂移项。若 mean exists，它对应 ordinary centering：

$$
b_n\sim n\mu.
$$

而 $n^{1/C_1}$ 项和 heavy-tail fluctuation scale 同阶。

现在 normalization 的 scaling 已经确定，作者回到 Eq. 8.21，把这些 scaling constants 代进去。这样原来关于 $n$ 的条件会变成一个只关于 limiting characteristic function $\phi$ 的方程。

### 8.5 Eq. 8.25：把 $C_1,C_2$ 代回 Eq. 8.21

把 Eq. 8.22 代入 Eq. 8.21，并除以 $\tilde{\omega}$，可以写成：

$$
\frac{\phi'(\tilde{\omega})}{\phi(\tilde{\omega})}
-
C_1
\frac{\log\phi(\tilde{\omega})}{\tilde{\omega}}
=
iC_2.
\tag{8.25}
$$

这一步的意义是：稳定极限的 characteristic function $\phi$ 必须满足一个一阶微分方程。也就是说，stable law 不是任意分布，而是由 coarse-graining invariance 约束出来的分布族。

为了让这个方程变成标准线性 ODE，作者把 $\log\phi$ 单独定义成 $u$。这一步也有直觉：characteristic functions 的乘法结构在 log 空间里会变成加法结构。

### 8.6 Eq. 8.26：令 $u=\log\phi$

定义：

$$
u(\omega)=\log\phi(\omega).
$$

则

$$
u'(\omega)
=
\frac{\phi'(\omega)}{\phi(\omega)}.
$$

于是 Eq. 8.25 变成：

$$
u'(\tilde{\omega})
-
C_1
\frac{u(\tilde{\omega})}{\tilde{\omega}}
=
iC_2.
\tag{8.26}
$$

这是一个 linear first-order ODE。

它的结构是：

$$
\text{change of log characteristic function}
-
\text{scale term}
=
\text{shift term}.
$$

这个 ODE 可以分两步解。第一步先忽略右侧 shift term，得到控制 tail/scaling 的 homogeneous solution。第二步再加入右侧，得到控制 location 的 particular solution。

### 8.7 Eq. 8.27：先解 homogeneous equation

先看齐次方程：

$$
u'
-
C_1\frac{u}{\omega}
=0.
$$

移项：

$$
\frac{u'}{u}
=
\frac{C_1}{\omega}.
$$

积分：

$$
\log u
=
C_1\log|\omega|+\text{constant}.
$$

因此：

$$
u_{\text{hom}}(\omega)
=
A|\omega|^{C_1}.
$$

由于 $\omega>0$ 和 $\omega<0$ 两侧可以有不同的 complex coefficient，作者写成：

$$
\left\{
\begin{array}{ll}
u_{\text{hom}}(\tilde{\omega})
=A_+\tilde{\omega}^{C_1},
&\tilde{\omega}>0,\\[4pt]
u_{\text{hom}}(\tilde{\omega})
=A_-|\tilde{\omega}|^{C_1},
&\tilde{\omega}<0.
\end{array}
\right.
\tag{8.27}
$$

这里 $A_+$ 和 $A_-$ 可以不同，因为 distribution 可以 asymmetric。右尾和左尾不一定一样厚。

齐次解给出了 $|\omega|^{C_1}$ 结构。接下来 particular solution 解释为什么 characteristic function 还会有一个 linear-in-frequency 的 shift term。

### 8.8 particular solution：shift term 从哪里来

现在解完整方程：

$$
u'
-
C_1\frac{u}{\omega}
=
iC_2.
$$

当 $C_1\neq1$ 时，尝试 particular solution：

$$
u_p=D\omega.
$$

代入：

$$
u_p'=D,
\qquad
C_1\frac{u_p}{\omega}=C_1D.
$$

所以：

$$
D-C_1D
=
D(1-C_1)
=
iC_2.
$$

因此：

$$
D
=
\frac{iC_2}{1-C_1}.
$$

这个 linear-in-$\omega$ term 在 characteristic function 里对应 location shift。

当 $C_1=1$ 时，上面这个解会发散，因为 denominator 为 0。此时 particular solution 要改成：

$$
u_p(\omega)
=
iC_2\omega\log\omega.
$$

这就是为什么 Levy stable law 在 $\alpha=1$ 时有单独的 logarithmic form。

把 homogeneous part 和 particular part 加起来，再从 $u=\log\phi$ 回到 $\phi$，就得到 stable law characteristic function 的雏形。

### 8.9 Eq. 8.28：指数化得到 characteristic function

当 $C_1\neq1$ 时，完整解是 homogeneous part 加 particular part：

$$
u(\omega)
=
A|\omega|^{C_1}
+
iD\omega.
$$

因为

$$
u=\log\phi,
$$

所以：

$$
\phi(\omega)
=
\exp\left(A|\omega|^{C_1}+iD\omega\right).
\tag{8.28}
$$

这已经是 stable law characteristic function 的核心形式。

其中：

$$
|\omega|^{C_1}
$$

控制 tail 和 scaling；

$$
iD\omega
$$

控制 location shift。

不过，$\phi$ 不是任意 complex function。它必须是某个真实 probability distribution 的 characteristic function，因此正负频率之间要满足共轭约束。

### 8.10 Eq. 8.29：real distribution 的共轭约束

如果 $\phi$ 是真实 probability distribution 的 characteristic function，就必须满足：

$$
\phi(-\omega)=\phi^*(\omega).
$$

这表示 negative frequency 上的信息不是独立的，而是 positive frequency 的 complex conjugate。

因此可以写成：

$$
\phi(\omega)
=
\left\{
\begin{array}{ll}
e^{A\omega^{C_1}},
&\omega>0,\\[4pt]
e^{A^*|\omega|^{C_1}},
&\omega<0.
\end{array}
\right.
\tag{8.29}
$$

这里先省略了 location term，重点是说明正负频率上的 complex coefficient 必须成共轭关系。

最后一步只是换参数。把 $C_1$ 改写成 standard stable-law notation $\alpha$，再把 complex coefficient 拆成 scale $c$ 和 skewness $\beta$，就得到 Eq. 8.30。

### 8.11 Eq. 8.30：Levy stable laws 的标准形式

最终，作者把参数改写成 stable-law 的常用记号：

$$
C_1=\alpha.
$$

当 $\alpha\neq1$ 时：

$$
\phi(\omega)
=
\exp
\left(
iD\omega
-
c|\omega|^\alpha
\left[
1
-
i\beta\operatorname{sign}(\omega)
\tan\left(\frac{\pi\alpha}{2}\right)
\right]
\right).
\tag{8.30a}
$$

当 $\alpha=1$ 时：

$$
\phi(\omega)
=
\exp
\left(
iD\omega
-
c|\omega|
\left[
1
+
\frac{2i}{\pi}
\beta\operatorname{sign}(\omega)\log|\omega|
\right]
\right).
\tag{8.30b}
$$

这就是 Levy stable laws 的 characteristic function。

它有四个参数。

第一，$\alpha$ 是 stability index，也控制 tail thickness。通常

$$
0<\alpha\leq2.
$$

$\alpha$ 越小，tail 越厚；$\alpha=2$ 时回到 Gaussian。

第二，$\beta$ 是 skewness parameter：

$$
-1\leq\beta\leq1.
$$

$\beta=0$ 表示 symmetric distribution；$\beta=1$ 表示右偏最强；$\beta=-1$ 表示左偏最强。

第三，$D$ 是 location parameter。它移动 distribution 的中心位置。

第四，$c$ 是 scale parameter。它控制 distribution 的宽度。

Eq. 8.30 的核心含义是：当 ordinary CLT 的有限方差条件失败时，加总变量的吸引子不再只有 Gaussian，而是一整个 Levy stable family。

到这里，技术推导完成。下一节不再推公式，而是解释“stable”这个名字的含义：为什么这一族分布在加总和重缩放下会保持同一个分布类型。

---

## 九、stable law 的定义和为什么它稳定

这一节把上一节的公式结果转成概念。Eq. 8.30 看起来复杂，但它表达的是一个简单性质：同一类变量相加以后，distribution family 不变，只改变 location 和 scale。这个性质正是 generalized CLT 需要的吸引子性质。

### 9.1 stable distribution 的定义

一个 distribution 被称为 stable，是指：如果两个 independent random variables $X_1$ 和 $X_2$ 都服从这个 distribution，那么它们的线性组合仍然属于同一个 distribution family，只是 location 和 scale 参数改变。

形式上，就是：

$$
X_1,X_2\sim F
\quad
\Rightarrow
\quad
aX_1+bX_2
\sim
\text{same family as }F.
$$

Gaussian 是最熟悉的 stable distribution。两个 independent Gaussian 相加还是 Gaussian，只是均值和方差改变。

Levy stable laws 是这个性质的广义版本。它们允许 infinite variance。

定义说明了 stable law 要满足什么性质。下一步需要回到 Eq. 8.30，说明它为什么确实满足这个性质。

### 9.2 为什么 Eq. 8.30 显示了 stability

characteristic function 有一个重要性质：

$$
\phi_{X_1+X_2}(\omega)
=
\phi_{X_1}(\omega)\phi_{X_2}(\omega).
$$

如果 $\phi$ 有 Eq. 8.30 的指数形式，那么两个 independent variables 相加时，characteristic functions 相乘，相当于 exponents 相加。

这会改变：

$$
c
\quad
\text{and}
\quad
D,
$$

但不会改变：

$$
\alpha
\quad
\text{and}
\quad
\beta.
$$

所以加总以后仍然在同一个 stable family 里。

这就是 stable law 的核心：

$$
\text{aggregation changes scale and location, not distributional type}.
$$

理解 stability 后，几个参数的含义也更清楚了：$\alpha$ 和 $\beta$ 决定分布类型，$c$ 和 $D$ 决定加总后的尺度和位置。接下来作者补充这些分布在 support、mean、median 上和普通 Gaussian 的差异。

### 9.3 support、mean 和 median

作者指出，Levy stable laws 的 support 通常是全实数：

$$
\mathbb{R}.
$$

但当

$$
\beta=1
$$

时，可以出现单侧 support，例如

$$
[D,\infty).
$$

这对 migration flows 很重要，因为很多 flow variables 是非负的。

mean 是否存在取决于 $\alpha$。

如果

$$
\alpha>1,
$$

mean exists，并且 location parameter $D$ 可以对应 mean。

如果

$$
\alpha\leq1,
$$

mean diverges。

当 $\beta=0$ 时 distribution symmetric，median 是 $D$。当 $\beta\neq0$ 时 median 没有简单解析表达。

这些性质说明 Levy stable laws 不是 Gaussian 的小修正，而是一类允许 infinite variance、可能单侧支撑、可能强偏斜的极限分布。下一节进一步把这些参数和原始变量的 power-law tail 对上。

---

## 十、tail 和 characteristic function 的关系

这一节回答一个关键衔接问题：如果原始迁移冲击的 empirical distribution 有 power-law tail，那么 stable-law 参数 $\alpha,\beta$ 从哪里来？答案是：$\alpha$ 来自 tail exponent，$\beta$ 来自左右尾强度不对称。

### 10.1 正尾和负尾

作者考虑一个 distribution，它在正方向和负方向都有 power-law tail：

$$
\rho(x)
\sim
\frac{A_+}{x^{1+\alpha}},
\qquad
x\to+\infty,
$$

以及

$$
\rho(x)
\sim
\frac{A_-}{|x|^{1+\alpha}},
\qquad
x\to-\infty.
$$

这里 $A_+$ 控制 right tail 的强度，$A_-$ 控制 left tail 的强度。

如果

$$
A_+=A_-,
$$

左右尾对称。

如果

$$
A_+>A_-,
$$

right tail 更重，distribution 更容易出现巨大正值。

如果

$$
A_- > A_+,
$$

left tail 更重，distribution 更容易出现巨大负值。

这些 tail amplitudes 是实空间里的信息。为了连接 Eq. 8.30，需要把它们翻译到 characteristic function 的小频率行为里。

### 10.2 Eq. 8.31：小频率行为

Tauberian theorem 连接两个东西：

$$
\text{large-}x\text{ tail of density}
\quad
\leftrightarrow
\quad
\text{small-}\omega\text{ behavior of characteristic function}.
$$

如果 density tail 是 power law，那么 characteristic function 在 $\omega\to0$ 时会有 non-analytic 项：

$$
\phi(\omega)
\simeq
1-C\omega^\alpha.
\tag{8.31}
$$

这里的关键是 $\omega^\alpha$。当 $\alpha$ 不是整数，或者 $\alpha<2$ 时，这不是普通的 Taylor expansion 的二阶项。

这正是 broad distribution 和 ordinary finite-variance distribution 的差别。

finite-variance 情况下：

$$
\phi(\omega)
=
1
+i\omega\mathbb{E}(X)
-
\frac{\omega^2}{2}\mathbb{E}(X^2)
+\cdots.
$$

heavy-tail 情况下，二阶矩不存在，dominant small-$\omega$ correction 变成：

$$
|\omega|^\alpha.
$$

Eq. 8.31 只说明 small-frequency correction 的幂次是 $\alpha$。下一步 Eq. 8.32 进一步说明这个 correction 的 complex coefficient 如何记录左右尾的权重。

### 10.3 Eq. 8.32：常数 $C$ 如何包含左右尾信息

作者给出：

$$
C
=
\frac{\Gamma(1-\alpha)}{\alpha}
\left(
A_+e^{-i\alpha\pi/2}
+
A_-e^{i\alpha\pi/2}
\right).
\tag{8.32}
$$

这条式子说明：small-frequency behavior 的 complex coefficient $C$ 由左右尾共同决定。

把指数项展开：

$$
e^{-i\alpha\pi/2}
=
\cos\left(\frac{\alpha\pi}{2}\right)
-
i\sin\left(\frac{\alpha\pi}{2}\right),
$$

$$
e^{i\alpha\pi/2}
=
\cos\left(\frac{\alpha\pi}{2}\right)
+
i\sin\left(\frac{\alpha\pi}{2}\right).
$$

因此：

$$
A_+e^{-i\alpha\pi/2}
+
A_-e^{i\alpha\pi/2}
$$

的 real part 是：

$$
(A_++A_-)
\cos\left(\frac{\alpha\pi}{2}\right),
$$

而 imaginary part 是：

$$
(A_- - A_+)
\sin\left(\frac{\alpha\pi}{2}\right).
$$

所以 real part 取决于 total tail weight：

$$
A_+ + A_-,
$$

imaginary part 取决于 tail imbalance：

$$
A_+ - A_-.
$$

这就自然引出 skewness parameter。既然 imaginary part 记录左右尾不平衡，就可以把这种不平衡标准化成一个介于 $-1$ 和 $1$ 之间的参数 $\beta$。

### 10.4 Eq. 8.33-Eq. 8.34：skewness parameter $\beta$

作者写：

$$
\frac{\operatorname{Im}(C)}
{\operatorname{Re}(C)}
=
-
\tan\left(\frac{\pi\alpha}{2}\right)\beta.
\tag{8.33}
$$

其中

$$
\beta
=
\frac{A_+-A_-}{A_++A_-}.
\tag{8.34}
$$

这个定义非常直观。

如果

$$
A_+=A_-,
$$

则

$$
\beta=0.
$$

distribution symmetric。

如果

$$
A_->0,
\qquad
A_+=0,
$$

则

$$
\beta=-1.
$$

distribution 完全左偏。

如果

$$
A_+>0,
\qquad
A_-=0,
$$

则

$$
\beta=1.
$$

distribution 完全右偏。

所以 $\beta$ 不是抽象参数，它就是左右 heavy tail 强度的归一化差异。

现在两个核心参数都已经从 tail 中读出来了：$\alpha$ 控制 tail decay 的幂次，$\beta$ 控制左右尾不对称。最后需要明确的是，为什么加总后的 stable law 会保留同一个 $\alpha$。

### 10.5 为什么 $\alpha$ 同时是 tail exponent 和 stable-law index

由 Eq. 8.31 可以看出，如果 density tail 是

$$
\rho(x)\sim x^{-1-\alpha},
$$

那么 characteristic function 的 small-frequency non-analytic term 是：

$$
|\omega|^\alpha.
$$

而 Eq. 8.30 中 Levy stable law 的 characteristic function 也正是由

$$
|\omega|^\alpha
$$

控制。

因此：

$$
\text{tail exponent}
\quad
\Longleftrightarrow
\quad
\text{stable-law index}.
$$

更具体地说，density tail 是：

$$
\rho(x)\sim |x|^{-1-\alpha},
$$

survival tail 是：

$$
\mathbb{P}(|X|>x)\sim x^{-\alpha}.
$$

而加总后的 stable law 也具有同一个 $\alpha$。

这就是广义 CLT 的核心机制：heavy-tail variables 的 sum 会保留原始 tail exponent，而不是被 Gaussian universality 洗掉。

这节完成了从 empirical tail 到 stable-law parameters 的连接。下一节通过几个 special cases 把抽象参数具体化：Gaussian、Cauchy 和 one-sided Levy distribution 都是同一个 stable family 的不同点。

---

## 十一、special cases：几个能写出实空间形式的稳定分布

一般 Levy stable laws 很难写出 closed-form density，所以作者用少数可解析例子建立直觉。这些例子的作用不是扩展主题，而是帮助读者把 $\alpha$ 的变化和 tail thickness、width scaling 联系起来。

### 11.1 symmetric case：$\beta=0$

当

$$
\beta=0
$$

时，distribution symmetric around $D$。Eq. 8.30 简化为：

$$
\phi(\omega)
=
e^{iD\omega-c|\omega|^\alpha}.
\tag{8.35}
$$

这个 characteristic function 是 stretched exponential in frequency space。

当

$$
\alpha=2,
$$

它变成 Gaussian。

当

$$
\alpha=1,
$$

它变成 Cauchy/Lorentzian。

当 $\alpha$ 从 2 降低时，distribution 的 tail 变厚，中心附近也不再像 Gaussian 那样集中。这类分布适合描述 intermittent process：

$$
\text{many small events}
\quad
\text{mixed with}
\quad
\text{rare huge events}.
$$

symmetric case 给出了最简洁的 characteristic function。接下来作者先取其中的 $\alpha=1$ 情况，也就是 Cauchy/Lorentzian，展示一个非 Gaussian stable law 的实空间形状。

### 11.2 Eq. 8.36：Lorentzian/Cauchy 的一个写法

作者给出 Lorentzian form：

$$
\mathbb{P}(x)
=
\frac{A}{x^2+\pi^2A^2}.
\tag{8.36}
$$

这个 distribution 的 tail 是：

$$
\mathbb{P}(x)\sim \frac{A}{x^2}.
$$

因此它对应

$$
1+\alpha=2,
\qquad
\alpha=1.
$$

Cauchy distribution 的 mean 和 variance 都不存在。它说明：即使 distribution 看起来有一个中心峰，加总也不一定会走向 Gaussian。

为了强调 Gaussian 也属于同一个 stable family，作者接着讨论 $\alpha=2$。这能把 ordinary CLT 和 generalized CLT 放到同一张图里：Gaussian 不是唯一 stable law，而是 finite-variance 端点。

### 11.3 Eq. 8.37：Gaussian 是 $\alpha=2$ 的 stable law

Gaussian characteristic function 写成：

$$
\phi(\omega)
=
e^{iD\omega-c\omega^2}.
\tag{8.37}
$$

这对应：

$$
\alpha=2.
$$

此时 variance 是：

$$
2c,
$$

mean 是：

$$
D.
$$

在 $\alpha=2$ 时，$\beta$ 不再重要。因为 Gaussian 的左右 tail 都是 thin tail，skewness parameter 不控制 power-law imbalance。

普通 CLT 就是这个 special case：

$$
\text{finite variance}
\Rightarrow
\alpha=2
\Rightarrow
\text{Gaussian stable law}.
$$

Gaussian 是 thin-tail 端点。为了看 thick-tail 端点，作者再给出 one-sided Levy distribution，它对应 $\alpha=1/2$，tail 比 Cauchy 更厚，并且只在非负轴上取值。

### 11.4 Eq. 8.38：Levy distribution

Levy distribution 是一个 one-sided stable law，对应：

$$
\alpha=\frac{1}{2},
\qquad
\beta=1.
$$

它的 density 是：

$$
\mathbb{P}(x)
=
\sqrt{\frac{C}{2\pi x^3}}
\exp\left(-\frac{C}{2x}\right),
\qquad
x\geq0.
\tag{8.38}
$$

这条式子有两个部分。

第一，power-law prefactor：

$$
x^{-3/2}.
$$

这对应：

$$
1+\alpha
=
\frac{3}{2},
\qquad
\alpha=\frac{1}{2}.
$$

第二，小 $x$ cutoff：

$$
\exp\left(-\frac{C}{2x}\right).
$$

当

$$
x\to0^+,
$$

指数项趋向 0，density 被压低。

当

$$
x\to\infty,
$$

指数项趋向 1，tail 由 $x^{-3/2}$ 控制。

所以 Levy distribution 是一个典型的 right-heavy-tail law。

实空间 density 已经显示了 $x^{-3/2}$ tail。下一步看它的 characteristic function，可以把这个例子和 Eq. 8.30 的 $\alpha=1/2,\beta=1$ 参数对应起来。

### 11.5 Eq. 8.39：Levy distribution 的 characteristic function

作者写它的 Fourier transform 为：

$$
\phi(\omega)
=
e^{-\sqrt{-2iC\omega}},
\qquad
\omega>0.
\tag{8.39}
$$

这个式子和 Eq. 8.30 对应。

因为

$$
\alpha=\frac{1}{2},
$$

所以 frequency dependence 是：

$$
|\omega|^{1/2}.
$$

又因为

$$
\tan\left(\frac{1}{2}\cdot\frac{\pi}{2}\right)
=
\tan\left(\frac{\pi}{4}\right)
=
1,
$$

所以它对应 $\beta=1$ 的 fully right-skewed stable law。

最后作者回到最常见的 $\alpha=1$ symmetric case，也就是标准 Cauchy distribution。这个例子特别适合说明 stable law 的加总尺度可以和 Gaussian 完全不同。

### 11.6 Eq. 8.40：Cauchy distribution

Cauchy distribution 对应：

$$
\alpha=1,
\qquad
\beta=0.
$$

它的 density 是：

$$
\mathbb{P}(x)
=
\frac{1/\pi\gamma}
{1+\left(\frac{x-x_0}{\gamma}\right)^2}.
\tag{8.40}
$$

这里 $x_0$ 是 location，$\gamma$ 是 scale。

当 $|x|$ 很大时：

$$
\mathbb{P}(x)
\sim
\frac{\gamma}{\pi x^2}.
$$

所以它的 density tail exponent 是 2，对应：

$$
\alpha=1.
$$

知道 Cauchy 的 characteristic function 后，可以直接看它为什么稳定：$N$ 个 Cauchy 相加只会把 scale 乘以 $N$，不会改变 distribution family。

### 11.7 Eq. 8.41-Eq. 8.42：Cauchy 为什么稳定

Cauchy distribution 的 characteristic function 是：

$$
\varphi(\omega)
=
e^{-\gamma|\omega|}.
\tag{8.41}
$$

如果把 $N$ 个 independent Cauchy variables 相加，characteristic function 变成：

$$
\varphi_N(\omega)
=
\left(e^{-\gamma|\omega|}\right)^N
=
e^{-N\gamma|\omega|}.
\tag{8.42}
$$

这仍然是 Cauchy characteristic function，只是 scale 从 $\gamma$ 变成：

$$
N\gamma.
$$

所以 Cauchy sum 的 width 随 $N$ 线性增长，而不是像 Gaussian 那样随 $\sqrt{N}$ 增长。

这说明一个非常重要的差异：

$$
\text{Gaussian aggregation}
\Rightarrow
\text{width}\sim\sqrt{N},
$$

但

$$
\text{Cauchy aggregation}
\Rightarrow
\text{width}\sim N.
$$

原因是 Cauchy tail 太厚，一个极端样本就可能和整个 sum 同阶。

special cases 到这里完成了直觉铺垫。下一节把这些例子收束成 generalized CLT 的统一 statement，明确不同 $\alpha$ 区间下 sum 的 leading behavior。

---

## 十二、generalized central limit theorem

这一节是全章的结论性公式。前面已经说明了普通 CLT 如何产生 Gaussian，也说明了 heavy-tail 如何产生 Levy stable laws。Eq. 8.43 把两者放进同一个分类：$\alpha$ 决定 mean 是否存在、variance 是否存在，也决定 sum 的正确 scaling 和极限噪声类型。

### 12.1 Eq. 8.43：三种加总极限

作者最后把结果写成 generalized CLT。

设 $\{X_i\}$ 独立同分布，并且有 power-law asymptotic behavior：

$$
\rho(x)\sim x^{-1-\alpha}.
$$

那么：

$$
\sum_{i=1}^{n}X_i
\xrightarrow{\mathcal{L}}
\left\{
\begin{array}{ll}
(bn)^{1/\alpha}\zeta_\alpha,
&\alpha<1,\\[4pt]
n\mu+(bn)^{1/\alpha}\zeta_\alpha,
&1<\alpha\leq2,\\[4pt]
n\mu+(bn)^{1/2}\eta,
&2<\alpha.
\end{array}
\right.
\tag{8.43}
$$

这里：

$$
\zeta_\alpha
$$

是 Levy stable law of parameter $\alpha$；

$$
\eta
$$

是 Gaussian law；

$$
\mu
$$

是 mean；

$$
b
$$

是和 tail amplitude 有关的 scale constant。

这条公式分三种情况。

这三种情况不是并列记忆点，而是一条由 tail 厚度控制的谱系：$\alpha$ 越小，极端事件越强，sum 越难被 average trend 描述；$\alpha$ 越大，普通 Gaussian 机制越容易恢复。

### 12.2 第一种情况：$\alpha<1$

当

$$
\alpha<1,
$$

mean 不存在。因为 mean moment 要求：

$$
1<\alpha.
$$

所以不能写

$$
n\mu.
$$

sum 的 leading scale 是：

$$
n^{1/\alpha}.
$$

因此：

$$
\sum_{i=1}^{n}X_i
\sim
(bn)^{1/\alpha}\zeta_\alpha.
$$

这里加总量几乎完全由 rare large events 控制。没有一个稳定的 average background 可以先减掉。

如果 $\alpha$ 稍微变大到超过 1，mean 开始存在，sum 就重新出现 deterministic trend。但只要 $\alpha$ 仍不超过 2，variance 仍然发散，fluctuation 仍然不是 Gaussian。

### 12.3 第二种情况：$1<\alpha\leq2$

当

$$
1<\alpha\leq2,
$$

mean exists，但 variance diverges。

所以 sum 有 deterministic drift：

$$
n\mu,
$$

但 fluctuation 不是 Gaussian：

$$
(bn)^{1/\alpha}\zeta_\alpha.
$$

完整形式是：

$$
\sum_{i=1}^{n}X_i
\sim
n\mu
+
(bn)^{1/\alpha}\zeta_\alpha.
$$

这一类最适合连接城市迁移冲击。系统有一个平均流量或平均增长趋势，但围绕这个趋势的 fluctuation 不是 $\sqrt{n}$ Gaussian noise，而是 $n^{1/\alpha}$ Levy noise。

因为 $\alpha<2$，所以：

$$
\frac{1}{\alpha}
>
\frac{1}{2}.
$$

这意味着 heavy-tail fluctuation 比 Gaussian fluctuation 增长得更快。

当 $\alpha$ 继续增大并超过 2，variance 终于恢复有限。此时 heavy-tail 不再控制极限波动，ordinary CLT 回来。

### 12.4 第三种情况：$\alpha>2$

当

$$
\alpha>2,
$$

variance exists。ordinary CLT 恢复：

$$
\sum_{i=1}^{n}X_i
\sim
n\mu
+
(bn)^{1/2}\eta.
$$

这里 fluctuation scale 是：

$$
\sqrt{n}.
$$

极限变量 $\eta$ 是 Gaussian。

所以 ordinary CLT 是 generalized CLT 的 special case：

$$
\alpha>2
\Rightarrow
\text{finite variance}
\Rightarrow
\text{Gaussian attraction}.
$$

Eq. 8.43 给出形式分类。作者随后用 Eq. 8.44-Eq. 8.45 解释它的物理含义：在 heavy-tail 情况下，单个新事件可能大到和已有总和同阶。

### 12.5 Eq. 8.44-Eq. 8.45：rare large events 为什么能主导 sum

作者用两条式子表达 heavy-tail sum 和 finite-variance sum 的差别。

在 broad distribution 中，可能出现：

$$
X_{N+1}
\sim
S_N.
\tag{8.44}
$$

意思是：新来的一个随机变量，就可能和前面 $N$ 个变量的总和同阶。

这不是 ordinary distribution 中的典型情况。对 finite-variance variables 来说，一般有：

$$
X_{N+1}
\ll
S_N.
\tag{8.45}
$$

因为如果 mean finite 且变量不被 extreme events 主导，那么：

$$
S_N\sim N\mu,
$$

而单个新变量通常是 $O(1)$ 量级。即使看 fluctuation，也通常是：

$$
\text{sum fluctuation}\sim\sqrt{N},
$$

单个变量不会和整个 sum 同阶。

heavy-tail 情况不同。最大值的典型尺度可以通过 survival tail 估算。

若

$$
\mathbb{P}(X>x)\sim x^{-\alpha},
$$

则 $N$ 个样本中最大值 $M_N$ 满足：

$$
N\mathbb{P}(X>M_N)\sim1.
$$

代入：

$$
NM_N^{-\alpha}\sim1.
$$

所以：

$$
M_N\sim N^{1/\alpha}.
$$

而 generalized CLT 中 sum fluctuation 的 scale 也是：

$$
S_N\text{ fluctuation}
\sim
N^{1/\alpha}.
$$

因此最大单个事件和整体 fluctuation 同阶。这就是 Eq. 8.44 的物理含义。

这一步把 generalized CLT 从抽象概率论带回城市问题：如果 migration shocks 的 empirical tail 足够厚，那么城市增长不能被理解为许多小迁移事件的平滑平均，而要允许少数大迁移事件直接改变宏观增长。

---

## 十三、这章对城市增长建模的含义

本章不是为了做纯概率论，而是为了改变后面城市增长方程的噪声语言。

前面如果使用 Gaussian noise，隐含的是：

$$
\begin{aligned}
&\text{many small independent shocks}\\
&\Rightarrow \text{finite-variance aggregation}\\
&\Rightarrow \text{Gaussian fluctuation}.
\end{aligned}
$$

但如果 interurban migration flows 的经验分布是：

$$
\rho(x)\sim x^{-1-\alpha},
\qquad
\alpha<2,
$$

那么 finite-variance assumption 失败。此时大城市增长中的 migration shock 不能被看成普通 Brownian noise，而应该被看成由 rare large jumps 主导的 broad noise。

这会改变 stochastic growth equation 的形式。

ordinary diffusion picture 是：

$$
dS
=
\text{drift}\,dt
+
\text{Gaussian noise}\,dB_t.
$$

但 broad migration shocks 更接近：

$$
dS
=
\text{drift}\,dt
+
\text{stable jump noise}.
$$

这里的核心不是数学形式更复杂，而是经验假设变了。作者想在 Chapter 9 证明：真实 interurban migration flows 由 rare but large events 主导，因此城市增长方程需要 generalized CLT 支持，而不是 ordinary CLT 支持。

所以 Chapter 8 的结论可以压缩为：

$$
\text{if migration shocks have infinite variance,}
\quad
\text{urban growth noise is not Gaussian.}
$$

更具体地说：

$$
\begin{aligned}
&\text{power-law migration flows}\\
&\rightarrow \text{Levy stable aggregation}\\
&\rightarrow \text{non-Gaussian stochastic growth equation}.
\end{aligned}
$$

---

## 十四、和前面章节的关系

Chapter 6 的 Gibrat-style models 通常把随机增长率写成普通 multiplicative noise。这个写法默认 noise 可以用 finite-variance fluctuation 来概括。

Chapter 7 加入 migration 后，城市之间的 exchange 会产生 coupled dynamics，并且在 Bouchaud-Mezard 模型里导出 stationary Pareto-like distribution。但那里的噪声仍然主要按 Gaussian multiplicative noise 来处理。

Chapter 8 的作用是提出一个更激进的问题：

$$
\text{如果 migration itself is heavy-tailed,}
\quad
\text{then what kind of noise should enter the growth equation?}
$$

答案是：不能直接用 Gaussian/Brownian language，而要使用 generalized CLT 和 Levy stable laws。

这也让后面 Chapter 9 的 bottom-up approach 有了数学基础。它不是先假设一个方便的 stochastic differential equation，而是先看 migration flow 的 empirical distribution；如果 empirical tail exponent 满足 $\alpha<2$，就必须让 growth equation 的 noise term 反映这个 broad-law structure。

---

## 十五、本章最重要的记忆点

第一，ordinary CLT 的关键不是独立同分布本身，而是 finite variance。只要 variance finite，大量独立变量加总后的中心波动会走向 Gaussian。

第二，power-law density

$$
\rho(x)\sim x^{-1-\alpha}
$$

的 moment 条件是：

$$
\mathbb{E}(X^q)\text{ finite}
\Leftrightarrow
q<\alpha.
$$

因此 $\alpha<2$ 意味着 variance diverges。

第三，heavy-tail sum 的 correct scale 是：

$$
n^{1/\alpha},
$$

而不是：

$$
\sqrt{n}.
$$

第四，Levy stable laws 是 Gaussian stable law 的推广。Gaussian 对应 $\alpha=2$；Cauchy 对应 $\alpha=1$；one-sided Levy distribution 对应 $\alpha=1/2$。

第五，$\beta$ 衡量左右尾的不对称：

$$
\beta
=
\frac{A_+-A_-}{A_++A_-}.
$$

它不是一个任意 skewness label，而是 right-tail weight 和 left-tail weight 的归一化差。

第六，generalized CLT 说明 rare large events 可以和整个 sum 同阶：

$$
X_{N+1}\sim S_N.
$$

这就是后面城市迁移模型的关键。这里的“迁移冲击”不是指任意一条迁移流本身，而是指一个城市在某个时间段里因为城市间迁移产生的净人口变化：

$$
\sum_{j\in N(i)}
\left(
J_{j\to i}-J_{i\to j}
\right).
$$

如果把城市 $i$ 和每个邻居 $j$ 之间的净迁移贡献记成 $X_{ij}$，那么城市 $i$ 的总迁移冲击就是许多 pairwise net migration contributions 的加总：

$$
\sum_{j\in N(i)}X_{ij}.
$$

在 thin-tail 情况下，这个总量会像许多小误差的平均，适合用 Gaussian noise 表示。可如果 $X_{ij}$ 是 heavy-tailed，那么少数特别大的 pairwise net migration events 就可能主导整个总和。此时城市增长方程里的随机项不能再写成普通 Gaussian noise，而要写成 Levy-type noise。
