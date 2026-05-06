---
title: "Predictor-Driven Diffusion for Spatiotemporal Generation"
authors: "Yuki Yasuda, Tobias Bischoff"
venue: "arXiv preprint, April 2 2026"
date_read: "2026-04-16"
date_deep_read: "2026-04-28"
date_linearized: "2026-05-04"
topics: ["spatiotemporal generation", "predictor-driven diffusion", "renormalization group", "path probability", "causal prediction", "super-resolution"]
source_mineru: "../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/predictor-driven-diffusion-for-spatiotemporal-generation.md"
---

# Predictor-Driven Diffusion for Spatiotemporal Generation

## 精读笔记

---

## 公式编号说明

这篇笔记按原文顺序重建阅读路径。原文公式保留原编号，例如 Eq. (1)、Eq. (58)、Eq. (68)。为了展开推导而增加的中间说明不额外编号。

对应的覆盖索引见：[predictor-driven-diffusion-for-spatiotemporal-generation-equation-map.md](./predictor-driven-diffusion-for-spatiotemporal-generation-equation-map.md)。它的作用是防止把 Appendix 中的关键推导当作“细节”漏掉。

---

## 〇、这篇文章在我们当前主线里的位置

这篇文章要解决的问题不是“如何把普通 diffusion model 用到视频或时空数据上”，而是更具体：

如果数据本身是一个随物理时间 $t$ 演化的空间场，那么 diffusion model 的去噪时间、物理演化时间、空间分辨率这三件事不能混在一起。

标准 diffusion model 通常只有一个 artificial diffusion time。它把样本从 data 推到 noise，再从 noise 反向去噪。这个过程可以在视觉上呈现 coarse-to-fine，但中间状态主要由 noise level 排列，不一定对应明确的空间尺度。

时空系统的问题更尖锐。物理时间 $t$ 不是一个可以随便平滑的轴。如果对时间轴做对称 smoothing，当前状态会混入未来信息；这在 forecasting 或 simulation 中等于偷看未来，因果性被破坏。

本文的核心设计是把两个轴拆开：

$$
\begin{aligned}
t
&: \text{physical time, causal evolution},\\
\lambda
&: \text{diffusion scale, spatial coarse-graining}.
\end{aligned}
$$

沿 $t$ 轴，模型只做 predictor。给定当前和过去状态，它预测未来演化。

沿 $\lambda$ 轴，模型做 RG-style diffusion。大的 $\lambda$ 表示更粗的空间尺度，小的 $\lambda$ 表示更细的空间尺度。

这就把一个容易混乱的问题拆成两条互不替代的链：

$$
\begin{aligned}
\text{causal dynamics}
&\Rightarrow
\text{learn } f_\lambda^\theta \text{ along physical time } t,\\
\text{spatial multiscale generation}
&\Rightarrow
\text{reverse sampling along diffusion scale } \lambda.
\end{aligned}
$$

和 PRX speed-accuracy 那篇相比，PRX 文章回答的是“什么样的 distributional protocol 更稳健”；这篇文章回答的是“对时空场来说，protocol 的坐标轴应该怎么拆，才能同时保留空间多尺度和时间因果性”。

对 Synthetic_City 来说，$t$ 可以对应真实年份、迁移阶段、scenario step 或 policy time；$\lambda$ 可以对应空间分辨率、行政层级、grid resolution 或 PUMA-to-block-group 的 coarse-to-fine allocation。本文的价值在于：不要把时间预测和空间细化塞进同一个黑箱 diffusion time，而是让 predictor 管时间，让 RG diffusion 管空间尺度。

全文主线可以写成：

$$
\begin{aligned}
&\text{standard diffusion has no explicit spatial scale}\\
&\rightarrow \text{RG diffusion gives a spatial scale axis } \lambda\\
&\rightarrow \text{temporal coarse-graining would violate causality}\\
&\rightarrow \text{learn a causal predictor along physical time } t\\
&\rightarrow \text{use the predictor to define a path density}\\
&\rightarrow \text{differentiate the path density to obtain a path score}\\
&\rightarrow \text{reverse-}\lambda\text{ sampling gives generation and super-resolution}.
\end{aligned}
$$

---

## 一、Abstract 的线性展开

摘要的第一句话先给出应用背景：multiscale spatial structure 会让 temporal prediction 变难。原因不是“大尺度和小尺度都存在”这么简单，而是小尺度 fluctuation 会影响大尺度演化。对于天气、湍流和复杂流体系统，如果全部解析小尺度，计算代价太高；如果直接丢掉小尺度，大尺度预测又会失真。

第二步，作者指出 standard diffusion model 没有很好解决这个问题。标准 diffusion 对 Fourier modes 的衰减是 scale-uniform 的。它可以通过信噪比差异表现出某种 coarse-to-fine 的视觉顺序，但它没有把空间尺度作为显式变量。

第三步，作者引入本文方案：Predictor-Driven Diffusion。这个框架把 renormalization-group-based spatial coarse-graining 和 physical-time path-integral formulation 结合起来。也就是说，空间方向通过 RG 建立 $\lambda$ 层级；时间方向通过 predictor 建立 trajectory probability。

第四步，作者说明 forward process 的结构：Laplacian damping 加 additive noise。Laplacian damping 让高波数小尺度成分快速衰减；additive noise 不是无关扰动，而是 RG 意义下对被消除小尺度自由度的统计积分。这样就得到一族按 diffusion scale $\lambda$ 索引的 coarse-grained fields。

第五步，训练目标是 KL divergence between data-induced and predictor-induced path densities。这个 KL 最后变成对 temporal derivatives 的简单 regression loss。这里是全文的关键：模型不是先训练 score network，而是训练 temporal predictor；predictor 诱导 path density；path density 再提供 reverse-$\lambda$ sampling 所需的 path score。

第六步，统一性来自同一个 predictor。它可以做三件事：

1. 固定 $\lambda$，沿 $t$ 前向积分，得到 simulation。
2. 从 Gaussian noise 出发，沿 $\lambda$ 反向积分，得到 unconditional generation。
3. 从粗分辨率路径出发，沿 $\lambda$ 反向积分，得到 super-resolution。

---

## 二、Introduction：问题为什么不是普通时空 diffusion

### 2.1 多尺度结构从哪里来

作者从 natural and engineered systems 的 hierarchical structure 讲起。天气模式受 cloud formation 这类小尺度过程影响；图像处理中的 Laplacian pyramid 也把图像拆成 coarse component 加 progressively finer residuals。共同点是：不同 levels of detail 不是彼此无关，而是会相互影响。

为了把“尺度”说清楚，作者转到 Fourier decomposition。空间波数 $k$ 和波长成反比：

$$
\text{large wavelength}
\quad\Longleftrightarrow\quad
\text{small } \|k\|
\quad\Longleftrightarrow\quad
\text{large-scale structure},
$$

$$
\text{small wavelength}
\quad\Longleftrightarrow\quad
\text{large } \|k\|
\quad\Longleftrightarrow\quad
\text{small-scale structure}.
$$

所以 spatial multiscale system 可以被读成：它的 Fourier modes 覆盖很宽的 wavenumber range。这个视角为后面用 Laplacian damping 做 scale-selective coarse-graining 铺路，因为 Laplacian 在 Fourier space 中天然会给出 $-\|k\|^2$。

### 2.2 标准 diffusion 的 coarse-to-fine 只是隐式的

扩散模型在生成中很强，并且 reverse denoising 常常看起来像从 coarse 到 fine。作者承认这一点，但随即指出关键区别：

标准 diffusion 中，小尺度结构通常因为 signal-to-noise ratio 更低而更早被破坏；reverse process 看起来先恢复大结构，再恢复细节。这个层级来自噪声强弱差异，而不是来自一个显式 spatial-scale coordinate。

因此，标准 diffusion 的中间状态回答的是：

$$
\text{how noisy is the sample?}
$$

而不是：

$$
\text{what spatial resolution does this state represent?}
$$

本文想要的是第二种对象：每个 $\lambda$ 都有可解释的空间尺度。

### 2.3 RG 的作用：不是低通滤波，而是积分掉小尺度自由度

Renormalization group 的传统目标是处理 multiscale structure。它不是简单 low-pass filtering。简单滤波把高波数成分抹掉；RG 则要把被消除的小尺度自由度对剩余大尺度变量的统计影响保留下来。

这一区分非常重要。对动力系统来说，小尺度变量虽然被隐藏，但它们仍然影响大尺度变量的未来演化。本文后面训练出的 $f_\lambda^\theta$ 正是在尝试学习这种“看不到小尺度但保留其统计反馈”的 coarse-grained dynamics。

### 2.4 为什么从静态 RG diffusion 到时空 RG diffusion 不平凡

已有 RG-based diffusion 主要用于 static fields，例如图像。静态数据没有 physical time，只需要考虑 $\lambda$ 轴。

时空动力学多了一个真实时间轴 $t$。如果把 RG coarse-graining 同时做在空间和时间上，就会出现 causality problem。时间平滑通常是 noncausal 的，因为平滑当前时刻需要未来和过去两侧的信息。对 forecasting 来说，这等于当前状态已经包含未来信息。

所以开放问题是：

$$
\text{How to extend RG diffusion to spatiotemporal dynamics}
\quad
\text{while preserving causality and scale awareness?}
$$

本文答案是：

$$
\begin{aligned}
&\text{do coarse-graining only along space } x,\\
&\text{learn causal prediction along physical time } t,\\
&\text{use predictor-induced path density to drive reverse-}\lambda\text{ sampling}.
\end{aligned}
$$

---

## 三、Background：RG diffusion 如何给出空间尺度轴

原文第 2 节先复述 RG-based diffusion 的已有结构。它的功能是把后面的 spatiotemporal extension 建在一个明确的 $\lambda$ 轴上。

### 3.1 Eq. (1)：forward RG diffusion

对矢量场 $u_\lambda := u_\lambda(x,t)$，forward process 是：

$$
\partial_\lambda u_\lambda
=
\alpha \nabla_x^2 u_\lambda
+
\beta \eta_\lambda .
\tag{1}
$$

这里每个符号都要分清：

$u_\lambda(x,t)$ 是在 diffusion scale $\lambda$ 下看到的空间场。它仍然依赖 physical time $t$，但 Eq. (1) 的演化变量不是 $t$，而是 $\lambda$。

$\nabla_x^2$ 是空间 Laplacian，只作用在 $x$ 上，不作用在 $t$ 上。这一点保证了 coarse-graining 不会混入未来时间。

$\eta_\lambda(x,t)$ 是沿 $\lambda$ 方向注入的 white Gaussian noise。它和后面 Eq. (6) 中 physical-time noise $\xi$ 不是同一个对象。

$\alpha$ 控制 Laplacian damping 强度，$\beta$ 控制噪声幅度。

要看懂为什么 Eq. (1) 会变成一个简单的指数衰减式，需要先把 Fourier 变换的作用说清楚。这里先把 physical time $t$ 固定住，只看某一个时刻的空间场 $u_\lambda(x,t)$。Fourier 分解的意思是：把一个空间场写成很多正弦/余弦波，或者更紧凑地写成复指数波的叠加：

$$
u_\lambda(x,t)
=
\sum_k
\widetilde{u}_\lambda(k,t)e^{ik\cdot x}.
$$

这里 $k$ 是 wavenumber，也就是空间频率。小 $\|k\|$ 对应长波长、大尺度结构；大 $\|k\|$ 对应短波长、小尺度纹理。$\widetilde{u}_\lambda(k,t)$ 是第 $k$ 个空间频率的系数，表示这个尺度成分在当前场里有多强。

Fourier 变换在这里有用，是因为 Laplacian 对每个 Fourier mode 的作用特别简单。空间 Laplacian 是二阶空间导数之和：

$$
\nabla_x^2
=
\sum_j \frac{\partial^2}{\partial x_j^2}.
$$

对一个单独的 Fourier mode $e^{ik\cdot x}$ 来说，先求一阶导数：

$$
\frac{\partial}{\partial x_j}e^{ik\cdot x}
=
ik_j e^{ik\cdot x}.
$$

再求二阶导数：

$$
\frac{\partial^2}{\partial x_j^2}e^{ik\cdot x}
=
(ik_j)^2e^{ik\cdot x}
=
-k_j^2e^{ik\cdot x}.
$$

把所有空间方向加起来：

$$
\nabla_x^2e^{ik\cdot x}
=
-\left(\sum_j k_j^2\right)e^{ik\cdot x}
=
-\|k\|^2e^{ik\cdot x}.
$$

这就是“$\nabla_x^2$ 对 mode $k$ 的作用是 $-\|k\|^2$”的具体来源。它不是一个凭空出现的规则，而是因为 Fourier basis 是 Laplacian 的 eigenfunction。换句话说，Laplacian 不会把一个 $k$ mode 变成另一个 $k'$ mode，它只会把原来的 mode 乘上一个系数 $-\|k\|^2$。

因此，如果暂时不看噪声项，也就是令 $\beta\eta_\lambda=0$，Eq. (1) 变成：

$$
\partial_\lambda u_\lambda
=
\alpha\nabla_x^2u_\lambda.
$$

把 Fourier 展开代入左边：

$$
\partial_\lambda u_\lambda(x,t)
=
\sum_k
\partial_\lambda\widetilde{u}_\lambda(k,t)e^{ik\cdot x}.
$$

把 Fourier 展开代入右边：

$$
\alpha\nabla_x^2u_\lambda(x,t)
=
\sum_k
-\alpha\|k\|^2\widetilde{u}_\lambda(k,t)e^{ik\cdot x}.
$$

左右两边都是同一组 Fourier basis $e^{ik\cdot x}$ 的展开，所以每个 $k$ 的系数必须分别相等。于是原来关于空间场的 PDE 被拆成每个 Fourier coefficient 上的 ODE：

$$
\partial_\lambda \widetilde{u}_\lambda(k,t)
=
-\alpha \|k\|^2 \widetilde{u}_\lambda(k,t).
$$

这一步的直觉是：不同空间频率不再互相纠缠。每个 $k$ mode 都沿 $\lambda$ 方向独立演化，只是衰减速度不同。

为了求解这个一阶线性方程，把

$$
a(\lambda)
:=
\widetilde{u}_\lambda(k,t)
$$

当作未知函数。方程就是：

$$
\frac{da}{d\lambda}
=
-\alpha\|k\|^2a.
$$

两边除以 $a$，再对 $\lambda$ 从 $0$ 积分到当前 scale：

$$
\int_{a(0)}^{a(\lambda)}
\frac{1}{a}\,da
=
\int_0^\lambda
-\alpha\|k\|^2\,d\lambda'.
$$

左边给出 $\ln a(\lambda)-\ln a(0)$，右边给出 $-\alpha\|k\|^2\lambda$，所以：

$$
\ln
\frac{a(\lambda)}{a(0)}
=
-\alpha\|k\|^2\lambda.
$$

两边取指数：

$$
\widetilde{u}_\lambda(k,t)
=
e^{-\alpha \|k\|^2\lambda}\widetilde{u}_0(k,t).
$$

这句话的含义不是“每个空间位置的 $u(x,t)$ 都独立指数衰减”，而是“每个空间频率成分 $\widetilde{u}(k,t)$ 都独立指数衰减”。高波数模式衰减更快。若 $\|k\|$ 很大，指数因子很快接近 0；若 $\|k\|$ 很小，指数因子仍接近 1。这就是 Laplacian damping 变成 spatial coarse-graining 的原因：小尺度纹理先被压掉，大尺度结构保留下来。

作者把有效 cutoff 写成：

$$
k_{\mathrm{cut}}
\sim
\frac{1}{\sqrt{\alpha\lambda}}.
$$

这个式子来自让指数中的量达到 $O(1)$：

$$
\alpha \|k\|^2\lambda \sim 1
\quad\Longrightarrow\quad
\|k\|\sim \frac{1}{\sqrt{\alpha\lambda}}.
$$

因此 $\lambda$ 越大，$k_{\mathrm{cut}}$ 越小，保留下来的 mode 越少，场越粗。

### 3.2 为什么 Eq. (1) 里的 noise 不能省

如果 $\beta=0$，Eq. (1) 只是 deterministic smoothing。它会直接抹掉小尺度成分：

$$
u_0
\quad\mapsto\quad
\mathcal{C}_\lambda u_0.
$$

这更像 low-pass filtering，而不是 RG。区别在于，low-pass filtering 的操作对象是一条具体样本。给定一个 fine field $u_0$，filter 只做一件事：把高波数成分压掉，留下平滑版本 $\mathcal{C}_\lambda u_0$。因此它给出的结果是确定的：

$$
u_0
\longrightarrow
\text{one smoothed field}.
$$

如果两个不同的 fine fields 在小尺度上不同、但在大尺度上相似，low-pass filtering 会把这些小尺度差异直接抹掉。被抹掉的信息不会以任何统计形式留下来。于是 coarse field 只知道“细节没有了”，不知道“这些细节原本可能怎样波动、怎样反馈到大尺度”。

RG 要处理的问题更强。它不是只想得到一张更模糊的图，而是想得到一个 coarse variables 的有效理论。也就是说，RG 关心的是：当小尺度自由度不可见时，剩下的大尺度变量应该服从什么 probability distribution 或 effective dynamics。

所以 RG 的操作对象不是单个样本，而是分布：

$$
q_0(u_0)
\longrightarrow
q_\lambda(u_\lambda).
$$

这里的核心动作是 marginalization over small-scale degrees of freedom。被消除的小尺度不是“消失后不再相关”，而是通过概率分布的 convolution 影响剩余变量的统计结构。换句话说，RG 会把看不见的小尺度影响转写成 coarse-scale distribution 的宽度、相关性、噪声和 effective drift。

噪声项正是让 forward process 从 deterministic smoothing 变成 stochastic coarse-graining 的部分。加入 $\beta\eta_\lambda$ 后，同一个 fine field 不再只对应一个 coarse field，而是对应一个以 $\mathcal{C}_\lambda u_0$ 为均值、以 $\Sigma_\lambda$ 为 covariance 的 coarse-field distribution：

$$
u_\lambda
=
\mathcal{C}_\lambda u_0
+
\sqrt{\Sigma_\lambda}\epsilon.
$$

这一步的生成模型意义是：reverse process 以后要从 coarse representation 重建 fine details。如果 forward 过程只是 deterministic low-pass filtering，那么小尺度结构只是被删除，模型没有看到“被删除小尺度的条件分布”。如果 forward 过程包含 noise injection，那么训练数据在每个 coarse scale 上形成一个 distribution，reverse-$\lambda$ sampling 才有机会学习如何从统计化的 coarse representation 采样出合理的小尺度细节。

所以 Eq. (1) 中两项的分工是：

$$
\begin{aligned}
\alpha\nabla_x^2 u_\lambda
&: \text{selectively damp high-wavenumber modes},\\
\beta\eta_\lambda
&: \text{turn smoothing into stochastic marginalization}.
\end{aligned}
$$

### 3.3 Eq. (2)：reverse RG diffusion

Eq. (1) 描述的是 forward coarse-graining。它从细尺度样本出发，沿 $\lambda$ 增大的方向走：

$$
\lambda=0
\quad\rightarrow\quad
\lambda>0.
$$

在这个方向上，Laplacian 把高波数小尺度成分压掉，noise 把被消除的小尺度影响写成 stochastic spread。结果是：原来的 fine path distribution $q_0$ 被推成一族 coarse path distributions $q_\lambda$。

generation 和 super-resolution 要做的是反方向。我们不是想继续把 fine path 变粗，而是想从粗尺度状态回到细尺度状态：

$$
\lambda_{\max}
\quad\rightarrow\quad
0.
$$

这就需要 reverse process。它不是简单地把 Eq. (1) 的符号全部取反。原因是 forward process 有噪声，许多 fine paths 会被压到相似的 coarse region；反向时必须知道当前 coarse path 附近哪些 fine directions 更符合数据分布。这个信息由 score 提供。

给定 Eq. (1) 的 forward process，对应的 reverse process 是：

$$
\partial_\lambda u_\lambda
=
\alpha \nabla_x^2 u_\lambda
-
\beta^2\nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t)
+
\beta\eta_\lambda .
\tag{2}
$$

这里要先纠正一个容易混淆的口径：Eq. (2) 本身不是 Fokker-Planck equation。它是 sample-level 的 reverse stochastic equation，也就是用来生成某一条具体 trajectory 的随机微分方程。它右边出现 $\beta\eta_\lambda$ 是正常的，因为 sample path 的演化需要随机噪声。

Fokker-Planck equation 描述的是 density-level evolution。为了看清两者关系，可以把整条 path 简写成一个高维变量：

$$
U_\lambda
:=
\{u_\lambda\}_t.
$$

再把 forward drift 简写成：

$$
b(U_\lambda)
:=
\alpha\nabla_x^2U_\lambda.
$$

这里 $\nabla_x^2$ 仍然是作用在每个 time slice 的空间 Laplacian；它不是对 probability density 求导。于是 Eq. (1) 可以读成 path space 里的 SDE：

$$
dU_\lambda
=
b(U_\lambda)d\lambda
+
\beta dW_\lambda.
$$

这个 SDE 对应的 density $q_\lambda(U)$ 满足 Fokker-Planck equation：

$$
\partial_\lambda q_\lambda(U)
=
-\nabla_U\cdot\left[b(U)q_\lambda(U)\right]
+
\frac{\beta^2}{2}\Delta_U q_\lambda(U).
$$

这里 $\nabla_U$ 和 $\Delta_U$ 是对 path variable $U$ 的梯度和 Laplacian。它们和空间 Laplacian $\nabla_x^2$ 是两层不同的导数：

$$
\begin{aligned}
\nabla_x^2
&: \text{对空间坐标 } x \text{ 求二阶导},\\
\nabla_U,\Delta_U
&: \text{对整条 path 的取值 } U \text{ 求导}.
\end{aligned}
$$

这条 Fokker-Planck equation 确实可以写成 continuity equation：

$$
\partial_\lambda q_\lambda(U)
=
-\nabla_U\cdot J_\lambda(U),
$$

其中 probability current 是：

$$
J_\lambda(U)
=
b(U)q_\lambda(U)
-
\frac{\beta^2}{2}\nabla_U q_\lambda(U).
$$

如果把 $\nabla_U q_\lambda$ 写成 $q_\lambda\nabla_U\ln q_\lambda$，就得到：

$$
J_\lambda(U)
=
\left[
b(U)
-
\frac{\beta^2}{2}\nabla_U\ln q_\lambda(U)
\right]
q_\lambda(U).
$$

所以你说得对：在 density-level 表达里，白噪声项不会直接以 $\eta_\lambda$ 的形式出现。它被平均掉了，变成 Fokker-Planck 方程里的 diffusion term $\frac{\beta^2}{2}\Delta_U q_\lambda$，或者 continuity equation 里的 current correction $-\frac{\beta^2}{2}\nabla_U q_\lambda$。

Eq. (2) 里的 score term和这个 density-level current 有直接关系，但不能把二者完全等同。continuity equation 里的 current velocity 是：

$$
\nu_\lambda(U)
=
\frac{J_\lambda(U)}{q_\lambda(U)}
=
b(U)
-
\frac{\beta^2}{2}\nabla_U\ln q_\lambda(U).
$$

而 reverse SDE 写成 Eq. (2) 时，显式 drift 是：

$$
b(U_\lambda)
-
\beta^2\nabla_U\ln q_\lambda(U_\lambda).
$$

这里系数从 $\frac{\beta^2}{2}$ 变成 $\beta^2$，不是笔误。原因是 reverse SDE 仍然带有自己的噪声项；当这个噪声项在 density-level 再贡献一次 diffusion current 后，整体 probability current 才能对应 forward process 的时间反向。换句话说，sample-level reverse drift 和 density-level probability velocity 不是同一个对象。

如果改用真正的 reverse time

$$
\tau
:=
\lambda_{\max}-\lambda,
$$

那么沿 $\tau$ 增大的采样方向是从粗到细。Eq. (2) 等价于：

$$
dU_\tau
=
\left[
-b(U_\tau)
+
\beta^2\nabla_U\ln q_{\lambda_{\max}-\tau}(U_\tau)
\right]d\tau
+
\beta d\bar W_\tau.
$$

这时它对应的 density evolution 正好是 forward Fokker-Planck 的反向。因此，笔记里应该把三层对象分开：

$$
\begin{aligned}
\text{sample-level forward SDE}
&: dU=b\,d\lambda+\beta dW,\\
\text{density-level FP/continuity equation}
&: \partial_\lambda q=-\nabla_U\cdot J,\\
\text{sample-level reverse SDE}
&: dU=(b-\beta^2\nabla_U\ln q)\,d\lambda+\beta d\bar W.
\end{aligned}
$$

这里先把对象拆开。

$\{u_\lambda\}_t$ 表示一整条 spatiotemporal path：

$$
\{u_\lambda\}_t
=
\left(
u_\lambda(\cdot,t^{(0)}),
u_\lambda(\cdot,t^{(1)}),
\ldots,
u_\lambda(\cdot,t^{(N_t)})
\right).
$$

它不是单个时刻的一张空间场，而是所有 time slices 合在一起的 trajectory。

$q_\lambda(\{u_\lambda\}_t)$ 是 diffusion scale $\lambda$ 下这整条 trajectory 的 probability density。它回答的问题是：在当前 spatial resolution 下，这样一整条时空路径有多像真实 coarse-grained data。

$\nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t)$ 是 path score。这个梯度不是对空间坐标 $x$ 求导，也不是对物理时间 $t$ 求导，而是对整条 path tensor 的取值求导。直观地说，它告诉我们：如果稍微改变当前 trajectory 中的每个空间点、时间点和通道，log density 会往哪个方向增加。

因此 score 的作用可以写成：

$$
\text{current path}
\quad\rightarrow\quad
\text{nearby higher-density path}.
$$

也就是说，它提供了“往数据流形靠近”的方向。

Eq. (2) 的三项分工是：

$$
\begin{aligned}
\alpha\nabla_x^2u_\lambda
&: \text{reverse equation 中保留 forward diffusion 的 drift 结构},\\
-\beta^2\nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t)
&: \text{score correction, 把样本拉回高概率 path region},\\
\beta\eta_\lambda
&: \text{reverse sampling 中继续保留 stochastic exploration}.
\end{aligned}
$$

这里最容易混淆的是第一个项的符号。Eq. (2) 仍然写成 $\partial_\lambda$，看起来像还在沿 $\lambda$ 增大的方向演化。但实际采样时，数值积分是从大 $\lambda$ 往小 $\lambda$ 走。也就是说，步长本身是负的：

$$
d\lambda < 0.
$$

所以不能只看方程右端的符号判断“它是不是在继续 smoothing”。真正的 reverse-$\lambda$ sampling 是沿负的 $\lambda$ 方向积分。

因此它的物理意义是：

$$
\text{coarse trajectory}
\quad\rightarrow\quad
\text{fine trajectory}.
$$

也就是 super-resolution。

如果没有 score term，只沿反方向积分 Laplacian，会变成不稳定的 anti-diffusion：高波数 mode 会被盲目放大，但不知道应该放大成哪种真实小尺度结构。这会产生噪声状、伪影状或不符合数据统计的细节。

score term 的作用就是避免这种盲目放大。它使用当前 scale 的 density $q_\lambda$，告诉 reverse process：哪些细节方向是数据分布支持的，哪些方向只是随机高频噪声。

所以第二项

$$
-\beta^2\nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t)
$$

是整个 reverse process 的核心。它把样本推向在 scale $\lambda$ 上高概率的 path。

已有 RG diffusion 可以通过 denoising score matching 直接学习这个 score。但本文的创新是：不单独训练 score network。作者先训练 temporal predictor $f_\lambda^\theta$，让它定义一个 predictor-induced path density $p_\lambda$；再用

$$
s_\lambda
=
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t)
$$

近似真实 score

$$
\nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t).
$$

这样，simulation 和 generation 被同一个对象连接起来：

$$
\text{causal temporal predictor}
\quad\Rightarrow\quad
\text{path density}
\quad\Rightarrow\quad
\text{reverse-}\lambda\text{ score}.
$$

### 3.4 Figure 1：二维坐标轴

![Figure 1 — framework schematic](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-02-figure-01.jpg)

Figure 1 把全文压成一个二维坐标系。读这张图时，不要先看模型模块，而要先看两个轴。

横轴是 diffusion scale $\lambda$。它控制空间粗粒化程度。向右走，$\lambda$ 变大，空间场变得更粗；向左走，$\lambda$ 变小，空间细节被逐步恢复。

$$
\text{small } \lambda
\quad\Longleftrightarrow\quad
\text{fine spatial resolution},
$$

$$
\text{large } \lambda
\quad\Longleftrightarrow\quad
\text{coarse spatial resolution}.
$$

纵轴是 physical time $t$。它不是 diffusion time，而是系统真实演化时间。沿这个轴走，表示从当前状态预测未来状态。因为 forecasting 不能偷看未来，所以沿 $t$ 方向的模型必须是 causal 的：只能使用当前和过去的信息。

图里的蓝色框对应第一类任务：simulation。它发生在固定的 $\lambda$ 上。也就是说，先选定一个空间尺度，然后沿 physical time $t$ 往前推：

$$
u_\lambda(\cdot,t^{(0)})
\rightarrow
u_\lambda(\cdot,t^{(1)})
\rightarrow
\cdots
\rightarrow
u_\lambda(\cdot,t^{(N_t)}).
$$

这里用到的是 predictor $f_\lambda^\theta$。它回答的问题是：在当前空间分辨率 $\lambda$ 下，给定过去若干 time steps，下一步的 time derivative 应该是什么。

图里的红色框首先不是在区分 unconditional generation 和 super-resolution，而是在说明 $\lambda$ 轴上的两条 diffusion dynamics。它的标题是 generation along $\lambda$，但框内实际画了两个方向：

$$
\begin{aligned}
\text{forward diffusion}
&: \lambda \text{ 变大，fine path }\rightarrow\text{ coarse/noisy path},\\
\text{reverse diffusion}
&: \lambda \text{ 变小，coarse/noisy path }\rightarrow\text{ fine path}.
\end{aligned}
$$

所以更精确地说，红色框的本体是正常的 forward / reverse pair：

$$
\{u_0\}_t
\rightarrow
\{u_{\Delta\lambda}\}_t
\rightarrow
\cdots
\rightarrow
\{u_{\lambda_{\max}}\}_t
\quad
\text{(forward, to larger } \lambda\text{)},
$$

以及

$$
\{u_{\lambda_{\max}}\}_t
\rightarrow
\{u_{\lambda_{\max}-\Delta\lambda}\}_t
\rightarrow
\cdots
\rightarrow
\{u_0\}_t
\quad
\text{(reverse, to smaller } \lambda\text{)}.
$$

这里的对象是一整条 trajectory，不是某个单独 time slice。这个设计很关键，因为 $\lambda$ 方向的 reverse process 要恢复的是 temporally consistent 的时空路径，而不是一帧一帧独立恢复的图像。

unconditional generation 和 super-resolution 不是红色框里直接画出来的两个入口，而是后文使用 reverse diffusion 时的两种初始化方式。它们共享同一个 reverse-$\lambda$ 方程，只是起点不同：

$$
\begin{aligned}
\text{unconditional generation}
&: \text{large-}\lambda\text{ Gaussian noise path}\rightarrow\text{fine path},\\
\text{super-resolution}
&: \text{observed coarse path}\rightarrow\text{fine path}.
\end{aligned}
$$

所以，Figure 1 这一处应该先读成 forward / reverse diffusion along $\lambda$。generation / super-resolution 是这个 reverse process 在 Section 3.4 和实验里的任务化解释。

底部训练框解释为什么同一个 predictor 能支撑这三类任务。作者不是单独训练一个 score network，而是训练 predictor-induced path density $p_\lambda$ 去贴近 data-induced path density $q_\lambda$。训练目标是最小化两条 path densities 的 KL divergence。

这一步的逻辑是：

$$
\begin{aligned}
f_\lambda^\theta
&\Rightarrow
p_\lambda(\{u_\lambda\}_t),\\
p_\lambda(\{u_\lambda\}_t)
&\Rightarrow
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t),\\
\nabla_{u_\lambda}\ln p_\lambda
&\Rightarrow
\text{reverse-}\lambda\text{ generation / super-resolution}.
\end{aligned}
$$

因此 Figure 1 的核心不是“蓝色模块加红色模块”，而是三件事被同一个二维结构统一起来：

$$
\begin{aligned}
\text{fixed } \lambda \text{ + forward } t
&: \text{simulation},\\
\text{reverse } \lambda \text{ + noise path}
&: \text{unconditional generation},\\
\text{reverse } \lambda \text{ + coarse path}
&: \text{super-resolution}.
\end{aligned}
$$

如果把 $\lambda$ 当成物理时间，就会误解这篇文章。$\lambda$ 管空间尺度，$t$ 管因果演化；这两个轴分开，才是本文框架成立的基础。

---

## 四、Proposed Method：从 RG path 到 predictor-driven score

### 4.1 离散化和路径记号

原文第 3.1 节先把 continuous-looking notation 固定成 discrete setting。空间坐标离散为 $\{x^{(i)}\}_{i=1}^{N_x}$，物理时间离散为：

$$
t^{(n)} = n\Delta t,
\quad
n=0,\ldots,N_t.
$$

一个 spatiotemporal sample 是所有空间点、时间点和通道组成的张量。笔记中统一写作：

$$
\{u_\lambda\}_t.
$$

这个记号非常重要。它不是某个 time step 的 state，而是一整条路径。后面 path density、path score、reverse-$\lambda$ sampling 都作用在这个对象上。

### 4.2 Eq. (3)：forward RG diffusion 的闭式解

Eq. (1) 在每个 $\lambda$ 上有闭式解：

$$
u_\lambda
=
\mathcal{C}_\lambda u_0
+
\sqrt{\Sigma_\lambda}\epsilon .
\tag{3}
$$

这里：

$$
\mathcal{C}_\lambda := e^{\lambda\alpha\nabla_x^2}
$$

是 coarse-graining operator。它是 Laplacian 的 matrix exponential。因为 Laplacian 只作用在空间上，$\mathcal{C}_\lambda$ 对每个 physical time slice 独立作用。

$\Sigma_\lambda$ 是 forward diffusion 在空间上诱导出来的 covariance matrix。它不是手动指定的噪声方差，而是由 Eq. (1) 的 OU 解推出。

$\epsilon$ 是标准 Gaussian noise，按空间点、时间点和通道独立采样。

Eq. (3) 的意义是：要得到 scale $\lambda$ 下的 coarse path，不需要数值积分 Eq. (1)。可以直接对 fine path $u_0$ 做线性粗粒化，再加上相应 covariance 的 Gaussian noise。

### 4.3 Eq. (4)：conditional density

由 Eq. (3) 可以直接得到条件分布：

$$
\begin{aligned}
\{u_\lambda\}_t \mid \{u_0\}_t
&\sim
\prod_{n=0}^{N_t}
\mathcal{N}\!\left(
\mathcal{C}_\lambda u_0(\cdot,t^{(n)}),
\Sigma_\lambda
\right)\\
&=: q_\lambda(\{u_\lambda\}_t\mid\{u_0\}_t).
\end{aligned}
\tag{4}
$$

这个 product form 的含义是：coarse-graining 对每个 $t^{(n)}$ 独立作用。也就是说，$\lambda$ 方向的 forward corruption 不在时间上卷积，不会用未来状态污染当前状态。

需要注意，Eq. (4) 并不是说不同时间步在数据中独立。它只是说，在给定整条 fine path $\{u_0\}_t$ 后，RG corruption 在每个 time slice 上独立。时间相关性仍然来自 fine path 的数据分布 $q_{\mathrm d}$。

### 4.4 Eq. (5)：coarse-grained path density

作者假设 fine-resolution path 来自 data density：

$$
\{u_0\}_t \sim q_{\mathrm d}(\{u_0\}_t).
$$

把 Eq. (4) 对所有 fine paths 积分掉，就得到 scale $\lambda$ 下的 marginal path density：

$$
q_\lambda(\{u_\lambda\}_t)
=
\int \mathcal{D}u_0\,
q_\lambda(\{u_\lambda\}_t\mid\{u_0\}_t)
q_{\mathrm d}(\{u_0\}_t).
\tag{5}
$$

这一步是 RG 的概率形式。它不是只生成一个 filtered sample，而是在定义一个新的 distribution。粗粒化后的 path density $q_\lambda$ 等于：先从真实数据分布抽 fine path，再经过 stochastic coarse-graining kernel 得到 coarse path。

这里 $\mathcal{D}u_0$ 是离散 path measure，也就是对所有空间点、时间点和通道上的 $u_0$ 积分。

Eq. (5) 的因果意义是：因为 kernel $q_\lambda(\{u_\lambda\}_t\mid\{u_0\}_t)$ 只沿空间 coarse-grain，所以 temporal correlations 只从 $q_{\mathrm d}$ 继承，而不是由 noncausal temporal smoothing 产生。

### 4.5 Eq. (6)：固定 $\lambda$ 下的 physical-time dynamics

在每个固定的 diffusion scale $\lambda$，作者用一个 stochastic governing equation 建模 physical-time evolution：

$$
\partial_t u_\lambda
=
f_\lambda^\theta(u_\lambda)
+
\sigma_\lambda\xi .
\tag{6}
$$

$f_\lambda^\theta$ 是 neural predictor，也叫 drift。它的输入可以包括当前状态和若干过去状态。理论上先写成 Markov drift；如果用 history window，则通过 state augmentation 恢复 Markov form。

$\xi(x,t)$ 是 physical-time white Gaussian noise。它不同于 Eq. (1) 里的 $\eta_\lambda$。两者对应不同轴：

$$
\begin{aligned}
\eta_\lambda
&: \text{noise along diffusion scale } \lambda,\\
\xi
&: \text{noise along physical time } t.
\end{aligned}
$$

$\sigma_\lambda$ 是 physical-time governing equation 的 noise amplitude。它不是随便加的 stochasticity，而是 coarse-graining 之后，小尺度自由度被消除所带来的 unresolved fluctuation。Appendix A.7 用 Eq. (58) 把它和 $\Sigma_\lambda$ 对齐。

### 4.6 Eq. (7)：predictor-induced path density

在 Itô 约定和 Euler-Maruyama 离散化下，Eq. (6) 诱导 path density：

$$
p_\lambda(\{u_\lambda\}_t)
=
\frac{r_\lambda}{Z_\lambda}
\exp\left[
-
\int_{\mathrm{x,t}}
\frac{
\|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2
}{
2\sigma_\lambda^2
}
\right].
\tag{7}
$$

这里 $p_\lambda$ 是 surrogate path density，不是 data path density。它由 learned predictor $f_\lambda^\theta$ 定义。

$r_\lambda$ 是 initial density，也就是 $t=t^{(0)}$ 处的 boundary distribution。训练时它会变成常数项；reverse-$\lambda$ sampling 时它的 score 会影响 temporal boundary，所以 Appendix B.6 用 extrapolation 处理。

$Z_\lambda$ 是 normalization constant。由于 $\sigma_\lambda$ 被设为 state-independent，$Z_\lambda$ 只依赖 $\sigma_\lambda,\Delta t$ 和维度，不依赖 $f_\lambda^\theta$。

指数里的平方项可以读成 path energy：

$$
\int_{\mathrm{x,t}}
\|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2.
$$

如果某条 path 的实际时间导数和 predictor 给出的 drift 很接近，那么它的 energy 低，density 高。如果 path 在很多 time step 上违反 predictor dynamics，那么 density 低。

这一步是全文的桥：

$$
\text{temporal predictor}
\quad\Rightarrow\quad
\text{path density}
\quad\Rightarrow\quad
\text{path score}.
$$

reverse-$\lambda$ sampling 需要的是：

$$
s_\lambda
:=
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t).
$$

因为 Eq. (7) 显式可微，作者可以通过 automatic differentiation 得到 $s_\lambda$，不需要单独训练 score network。

### 4.7 Eq. (8)：KL divergence 如何变成 regression loss

训练目标是让 predictor-induced path density $p_\lambda$ 逼近 coarse-grained data path density $q_\lambda$：

$$
\begin{aligned}
D_{\mathrm{KL}}(q_\lambda\|p_\lambda)
&=
\int \mathcal{D}u_\lambda\,
q_\lambda(\{u_\lambda\}_t)
\ln
\frac{
q_\lambda(\{u_\lambda\}_t)
}{
p_\lambda(\{u_\lambda\}_t)
}\\
&=
\frac{1}{2\sigma_\lambda^2}
\mathbb{E}_{q_\lambda}
\left[
\int_{\mathrm{x,t}}
\|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2
\right]
+
\mathrm{const.}
\end{aligned}
\tag{8}
$$

第一行是 KL 定义。第二行来自把 Eq. (7) 代入。

具体来说：

$$
\ln p_\lambda
=
\ln r_\lambda
-
\ln Z_\lambda
-
\frac{1}{2\sigma_\lambda^2}
\int_{\mathrm{x,t}}
\|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2.
$$

在 KL 中，$q_\lambda\ln q_\lambda$ 与 $\theta$ 无关，$\ln r_\lambda$ 和 $\ln Z_\lambda$ 也被当作与 $\theta$ 无关。因此，关于 $\theta$ 的训练目标只剩下 weighted squared residual。

所以这篇文章的训练不是 rollout loss，也不是 score matching loss，而是：

$$
\text{local temporal derivative regression at randomly sampled scale } \lambda.
$$

### 4.8 Eq. (9)：最终训练目标

作者对 $\lambda\in[0,1]$ 取均匀采样，得到最终 objective：

$$
\mathcal{L}(\theta)
=
\mathbb{E}_{\lambda\sim\mathcal{U}(0,1),\,q_\lambda}
\left[
\frac{1}{2\sigma_\lambda^2}
\int_{\mathrm{x,t}}
\|\partial_t u_\lambda - f_\lambda^\theta(u_\lambda)\|^2
\right].
\tag{9}
$$

这意味着一个网络跨所有尺度训练。$\lambda$ 作为条件输入告诉网络当前场处在哪个 coarse-graining level。

权重 $1/(2\sigma_\lambda^2)$ 的作用是：不同 scale 的 coarse-graining noise 不同，所以 residual 的单位不能直接比较。噪声越小的 scale，对同样 residual 的惩罚越大；噪声越大的 scale，允许更多 unresolved variability。

### 4.9 Eq. (10)：最优 predictor 到底学到了什么

在理想化情况下，fine-resolution dynamics 存在真实漂移：

$$
\partial_t u_0
=
f_0^{\mathrm{true}}(u_0).
$$

作者在主文给出最优 drift 的近似直觉：

$$
f_\lambda^*(u_\lambda)
\approx
\mathbb{E}
\left[
\mathcal{C}_\lambda f_0^{\mathrm{true}}(u_0)
\mid
u_\lambda
\right].
\tag{10}
$$

这句话的重点是算子顺序。

错误顺序是：

$$
u_0
\rightarrow
\mathcal{C}_\lambda u_0
\rightarrow
f_0^{\mathrm{true}}(\mathcal{C}_\lambda u_0).
$$

这等于先把小尺度抹掉，再在残缺的 coarse field 上求动力学。这样会丢失小尺度对大尺度 tendency 的反馈。

本文希望学到的顺序是：

$$
u_0
\rightarrow
f_0^{\mathrm{true}}(u_0)
\rightarrow
\mathcal{C}_\lambda f_0^{\mathrm{true}}(u_0)
\rightarrow
\mathbb{E}[\cdot\mid u_\lambda].
$$

先在 full-resolution field 上计算真实 tendency，再把 tendency 粗粒化，最后对所有可能产生当前 $u_\lambda$ 的 fine states 求 conditional expectation。这样小尺度虽然不直接可见，但它对大尺度 tendency 的统计影响被保留。

Appendix A.6 会说明 Eq. (10) 是主文中的简化直觉；更精确的最优 drift 还包含 denoising correction。

### 4.10 Eq. (11)：inference 时的 reverse-$\lambda$ sampling

训练完后，生成和超分辨率都使用：

$$
\partial_\lambda u_\lambda
=
\alpha\nabla_x^2 u_\lambda
-
\beta^2 s_\lambda
+
\beta\eta_\lambda,
\quad
s_\lambda
:=
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t).
\tag{11}
$$

它和 Eq. (2) 的区别是：真实 score

$$
\nabla_{u_\lambda}\ln q_\lambda(\{u_\lambda\}_t)
$$

被 predictor-induced score

$$
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t)
$$

替代。训练目标 Eq. (9) 的目的就是让 $p_\lambda\approx q_\lambda$，从而让这个替代有效。

---

## 五、三种 inference 模式

### 5.1 Simulation：固定 $\lambda$，沿 $t$ 前向

simulation 不需要 reverse-$\lambda$。给定初始条件和某个 scale $\lambda$，用 Eq. (6) 沿 physical time 前向积分：

$$
u_\lambda(t^{(n+1)})
\approx
u_\lambda(t^{(n)})
+
f_\lambda^\theta(u_\lambda(t^{(n)}))\Delta t.
$$

在确定性评估中，作者设 $\sigma_\lambda=0$。原因是参考 coarse-grained data 是把 physics simulation 经过 $\mathcal{C}_\lambda$ 得到的 deterministic coarse reference，不含额外 stochastic noise。这样比较更清楚。

### 5.2 Unconditional generation：从 Gaussian noise 出发，沿 $\lambda$ 反向

generation 从大 $\lambda$ 的 Gaussian noise path 初始化，再用 Eq. (11) 从 $\lambda_{\max}$ 积分到 $\lambda_{\min}$。这时生成对象不是单个空间场，而是一整条 spatiotemporal trajectory。

这里的关键验证是：同一个 $f_\lambda^\theta$ 原本只是 temporal predictor，但它通过 Eq. (7) 也提供了 path score。因此它可以驱动 diffusion-like generation。

### 5.3 Super-resolution：从 coarse path 出发，沿 $\lambda$ 反向

super-resolution 是 generation 的条件版本。输入不是纯 Gaussian noise，而是某个 $\lambda>0$ 的 coarse-grained path。然后沿 reverse-$\lambda$ 积分回 $\lambda=0$。

这和常见 image super-resolution 的差别是：作者恢复的不是单张图像，而是一条满足 temporal dynamics 的 spatiotemporal path。路径内部的 temporal consistency 由 predictor-induced path density 约束。

### 5.4 三种模式的统一表

| 模式 | 固定或积分的轴 | 起点 | 终点 | 用到的对象 |
|---|---|---|---|---|
| Simulation | 固定 $\lambda$，沿 $t$ 前向 | 初始状态 | 未来状态 | Eq. (6), $f_\lambda^\theta$ |
| Generation | 沿 $\lambda$ 反向 | Gaussian path at large $\lambda$ | fine path at $\lambda=0$ | Eq. (11), path score |
| Super-resolution | 沿 $\lambda$ 反向 | coarse path at $\lambda>0$ | fine path at $\lambda=0$ | Eq. (11), path score |

---

## 六、Experiments：主文实验逻辑

### 6.1 实验不是追 SOTA，而是验证统一框架

作者明确说实验目标不是在特定 benchmark 上追 state-of-the-art，而是验证一个框架是否能用同一个网络同时完成 simulation、generation、super-resolution。

两个系统都具有 chaotic multiscale dynamics：

| 系统 | 空间维度 | 变量 | 样本形状 | 训练样本 | 测试样本 |
|---|---|---|---|---|---|
| Lorenz-96 | 1D periodic | slow $X$ + fast $Y$ | 128 spatial points, 64 snapshots | 3000 | 100 |
| Kolmogorov flow | 2D periodic | vorticity $\zeta$ | $40\times40$ spatial grid, 40 snapshots | 6000 | 100 |

U-Net 是主网络。输入是当前状态加前四个时间步，沿 channel 维拼接。输出是当前 time derivative 的 finite-difference approximation。$\lambda$ 通过 FiLM conditioning 注入。

DDPM baseline 用同样 U-Net，但 simulation 和 generation 分别训练模型。由于 DDPM baseline 没有 spatial coarse-graining hierarchy，它不能在 $\lambda>0$ 评估 simulation，只能在 $\lambda=0$ 比较。

### 6.2 Figure 2：Lorenz-96 simulation

![Figure 2 — Lorenz-96 simulation](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-05-figure-01.jpg)

Figure 2 展示 Lorenz-96 的 simulation。上排是 fine resolution $\lambda=0$，下排是 coarse resolution $\lambda=0.2$。左边是 slow variable $X$，右边是 fast variable $Y$。每个 panel 又包含 spatiotemporal evolution 和 time-averaged spatial PSD。

读图顺序应该是：

第一，看 $\lambda=0$。surrogate 是否能复制 physics simulation 的时空纹理和谱统计。这里它基本能做到。

第二，看 $\lambda=0.2$。小尺度成分被粗粒化压掉，但剩余的大尺度 pattern 仍然随时间 fluctuation。这个 fluctuation 不是简单滤波能自动给出的，它要求 predictor 学会被消除小尺度对大尺度的统计反馈。

第三，看 PSD。PSD 用来判断模型是否只在短期轨迹上接近，还是长期统计结构也接近。

### 6.3 Figure 3：Kolmogorov flow simulation

![Figure 3 — Kolmogorov flow simulation](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-05-figure-02.jpg)

Figure 3 对 Kolmogorov flow 做同样验证。左侧展示第 6 个 time step 的 vorticity field，右侧展示 time-averaged PSD。

这里 $\lambda=0.2$ 的作用更直观：vorticity snapshot 里小尺度涡旋结构被抹掉，但大尺度流动仍保留。作者想说明的不是 coarse image 好看，而是 predictor 可以在不同 $\lambda$ 下模拟对应分辨率的 dynamics。

### 6.4 Table 1：simulation 和 DDPM baseline 的比较

Table 1 只在 $\lambda=0$ 比较，因为 DDPM baseline 没有 coarse-grained $\lambda$ 层级。

| 指标 | Predictor-Driven | DDPM baseline |
|---|---:|---:|
| L96 $L^2$ error | **0.503 ± 0.011** | 0.557 ± 0.031 |
| KF $L^2$ error | **0.691 ± 0.057** | 0.861 ± 0.023 |
| L96 spectral error | **0.120 ± 0.014** | 0.226 ± 0.077 |
| KF spectral error | 0.182 ± 0.029 | **0.139 ± 0.021** |

$L^2$ error 是第 6 个 time step 的 short-term prediction accuracy。spectral error 是 long-run statistical consistency。

结论要谨慎读：本文不是全方位压过 DDPM。它展示的是 comparable accuracy，同时多了 $\lambda>0$ simulation、generation、super-resolution 的统一能力。

### 6.5 Table 2：unconditional generation

Table 2 比较 unconditional generation 的 spectral error：

| 指标 | Predictor-Driven | DDPM baseline |
|---|---:|---:|
| L96 spectral error | 0.343 ± 0.028 | **0.267 ± 0.020** |
| KF spectral error | **0.457 ± 0.025** | 0.615 ± 0.121 |

L96 上 DDPM 更好，KF 上本文更好。作者的重点不是声称新方法总是更强，而是说明 predictor-induced path density 的 score 确实可用于生成。也就是说，Eq. (7) 到 Eq. (11) 的桥是可运行的。

### 6.6 Table 3 和 Figure 4：super-resolution

![Figure 4 — super-resolution](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-06-figure-01.jpg)

Table 3 对比 super-resolved output 和 low-resolution input：

| 指标 | SR | LR at $\lambda=0.2$ vs $\lambda=0$ |
|---|---:|---:|
| L96 spectral error | **0.345 ± 0.027** | 0.873 ± 0.005 |
| KF spectral error | **0.303 ± 0.011** | 0.743 ± 0.005 |

这个结果说明，reverse-$\lambda$ integration 不是只在视觉上加细节，而是在 spectral statistics 上显著接近 fine-resolution reference。

Figure 4 的读法是：

第一列是 super-resolved output at $\lambda=0$。

第二列是 low-resolution input at $\lambda=0.2$。

第三列是 PSD 对比。

如果只看 low-resolution input，它缺少高波数能量，spectral error 很大。经过 reverse-$\lambda$ 后，小尺度结构被恢复，PSD 更接近 physics-based fine simulation。

---

## 七、Related Work：作者怎样定位本文

### 7.1 diffusion / flow-based generative models

标准 SDE/ODE generative models 把 diffusion scale 当作 timelike parameter，网络通常学 score 或 drift。本文不同：网络学的是 physical time $t$ 方向的 drift，训练 KL 也是 physical-time path density 之间的 KL。

这一区分可以写成：

$$
\begin{aligned}
\text{standard diffusion}
&: \text{learn score/drift along diffusion time},\\
\text{Predictor-Driven Diffusion}
&: \text{learn temporal drift along physical time}.
\end{aligned}
$$

### 7.2 RG-based diffusion models

已有 RG diffusion 给静态数据建立空间尺度层级。本文继承 Laplacian-based damping，但加入 physical-time path density。换句话说，本文不是替代 RG diffusion，而是把 RG diffusion 从 static field 推到 spatiotemporal field。

### 7.3 scale-aware diffusion without explicit RG

有些模型通过 hierarchical networks、多分辨率表示或 factorized scores 引入 multiscale structure。但它们没有改变 forward process。本文把 scale dependence 写进 forward process 本身，所以中间状态有明确 coarse-graining 含义。

### 7.4 Neural ODE/SDE

Neural ODE/SDE 学 physical-time dynamics，但通常固定分辨率，没有显式 $\lambda$ 轴。本文学的是 $\lambda$-conditioned family of predictors，因此同一模型可以在不同 coarse-graining levels 下模拟。

### 7.5 Energy-based models

Eq. (7) 的 exponent 可以看成 path energy。因此它和 energy-based model 有形式类比：

$$
p(x)\propto e^{-E(x)}
\quad\Longleftrightarrow\quad
p_\lambda(\{u_\lambda\}_t)
\propto
e^{-S_\lambda(\{u_\lambda\}_t)}.
$$

区别在于，本文的 energy 是 trajectory-level residual energy，不是 static data energy。

### 7.6 super-resolution diffusion

已有很多 diffusion super-resolution 方法，但常见策略是先训练 low-resolution predictor，再单独训练 super-resolver。本文把二者统一：predictor 的 path density 同时给 temporal simulation 和 reverse-$\lambda$ super-resolution 提供依据。

---

## 八、Conclusion 和 limitations

作者的结论可以压成三步。

第一，RG-based spatial coarse-graining 给 diffusion states 一个明确解释：每个 $\lambda$ 对应一个空间分辨率。

第二，path-integral temporal dynamics 给 predictor 一个概率解释：$f_\lambda^\theta$ 不只是回归器，而是定义 trajectory density。

第三，trajectory density 的 score 可以驱动 reverse-$\lambda$ sampling，所以同一个网络统一 simulation、generation、super-resolution。

局限性也很具体：

1. 目前面向 physical dynamics 主导的 spatiotemporal fields，对普通视频数据是否适用还不清楚。
2. 初始密度 $r_\lambda$ 被经验处理，适合统计平稳系统；瞬态系统需要更认真建模。
3. 实验只覆盖 1D Lorenz-96 和 2D Kolmogorov flow，未验证 3D 和更高分辨率。
4. generation / super-resolution 比 simulation 贵，因为每个 reverse-$\lambda$ step 都要通过自动微分计算 path score。
5. $\alpha,\beta$ 需要系统特定调参；未来可采用 $\lambda$-dependent damping/noise schedule。

---

## 九、Appendix A：理论细节的线性展开

Appendix A 是这篇文章最容易被折叠的部分。主文给出直觉，Appendix A 负责把几个关键对象推清楚：

1. $\mathcal{C}_\lambda$ 和 $\Sigma_\lambda$ 从哪里来。
2. Eq. (7) 的 path density 如何从 Euler-Maruyama transition product 得到。
3. 使用 history window 为什么仍然可以写成 Markov dynamics。
4. Eq. (10) 的最优 drift 其实来自 KL minimization，并且精确形式含 denoising correction。
5. $\sigma_\lambda$ 为什么可以用 $\operatorname{tr}(\Sigma_\lambda)$ 估计。

### 9.1 Appendix A.1：符号口径

作者明确采用离散时空，不讨论连续极限。连续写法如

$$
\int_{\mathrm{x,t}}
$$

只是离散求和的紧凑记号：

$$
\int_{\mathrm{x,t}}
=
\sum_{i,n}\Delta x\,\Delta t.
$$

时间导数按 Euler-Maruyama 离散：

$$
\partial_t u_\lambda(t^{(n)})
\approx
\frac{
u_\lambda(t^{(n+1)})-u_\lambda(t^{(n)})
}{
\Delta t
}.
$$

概率密度统一用小写 $p,q,r$。这里的 density 不包含 differential measure。几个密度的区别如下：

| 符号 | 含义 |
|---|---|
| $q_{\mathrm d}(\{u_0\}_t)$ | fine-resolution data path density |
| $q_\lambda(\{u_\lambda\}_t)$ | scale $\lambda$ 下的 coarse-grained data path density |
| $q_\lambda^{\mathrm{joint}}(\{u_\lambda\}_t,\{u_0\}_t)$ | coarse path 和 fine path 的 joint density |
| $p_\lambda(\{u_\lambda\}_t)$ | predictor-induced surrogate path density |
| $r_\lambda$ | initial density at temporal boundary |

还要区分两种噪声：

| 噪声 | 出现位置 | 作用轴 |
|---|---|---|
| $\eta_\lambda(x,t)$ | Eq. (1), Eq. (11) | diffusion scale $\lambda$ |
| $\xi(x,t)$ | Eq. (6) | physical time $t$ |

### 9.2 Eq. (12)-Eq. (18)：coarse-graining operator 和 covariance 的推导

Appendix A.2 先定义 Fourier transform：

$$
\widetilde{u}_\lambda(k,t)
=
\mathcal{F}[u_\lambda(x,t)]
=
\int_{[0,2\pi)^d} dx\,
\frac{e^{-ik\cdot x}}{(\sqrt{2\pi})^d}
u_\lambda(x,t).
\tag{12}
$$

逆变换是：

$$
u_\lambda(x,t)
=
\mathcal{F}^{-1}[\widetilde{u}_\lambda(k,t)]
=
\sum_k
\frac{e^{ik\cdot x}}{(\sqrt{2\pi})^d}
\widetilde{u}_\lambda(k,t).
\tag{13}
$$

由于

$$
\mathcal{F}[\nabla_x^2 u_\lambda](k,t)
=
-\|k\|^2\widetilde{u}_\lambda(k,t),
$$

Eq. (1) 在 Fourier space 中变成：

$$
\partial_\lambda \widetilde{u}_\lambda
=
-\alpha\|k\|^2\widetilde{u}_\lambda
+
\beta\widetilde{\eta}_\lambda.
\tag{14}
$$

对每个 $k\neq0$，这是一个 Ornstein-Uhlenbeck process。解为：

$$
\widetilde{u}_\lambda
=
e^{-\alpha\|k\|^2\lambda}\widetilde{u}_0
+
\beta
\int_0^\lambda
e^{-\alpha\|k\|^2(\lambda-\lambda')}
\widetilde{\eta}_{\lambda'}\,d\lambda'.
\tag{15}
$$

第一项是 deterministic damping。第二项是经过同一 exponential kernel filtering 的 accumulated noise。

因为 noise 是 Gaussian，积分项也是 Gaussian。因此条件 density 为：

$$
\begin{aligned}
q_\lambda(\widetilde{u}_\lambda(\cdot,t)\mid \widetilde{u}_0(\cdot,t))
\propto
\prod_{k\neq0}
\exp\Bigg[
-
\frac{1}{2}
\frac{
2\alpha\|k\|^2
}{
\beta^2(1-e^{-2\alpha\|k\|^2\lambda})
}
\left|
\widetilde{u}_\lambda(k,t)
-
e^{-\alpha\|k\|^2\lambda}\widetilde{u}_0(k,t)
\right|^2
\Bigg].
\end{aligned}
\tag{16}
$$

从 Eq. (16) 可以直接读出每个 Fourier mode 的 mean 和 variance：

$$
\widetilde{\mathcal{C}}_\lambda(k)
=
e^{-\alpha\|k\|^2\lambda},
\tag{17}
$$

$$
\widetilde{\Sigma}_\lambda(k)
=
\beta^2
\frac{
1-e^{-2\alpha\|k\|^2\lambda}
}{
2\alpha\|k\|^2
}.
\tag{18}
$$

Eq. (17) 是 scale-selective damping。Eq. (18) 是 OU process 的 accumulated noise variance。$\lambda\to0$ 时，$\widetilde{\Sigma}_\lambda(k)\to0$；$\lambda$ 变大时，variance 接近 $\beta^2/(2\alpha\|k\|^2)$。

零波数 $k=0$ 被排除，因为数据预处理已经做了 zero mean standardization，constant Fourier mode 被去掉。如果保留 $k=0$，Eq. (18) 会出现 $1/\|k\|^2$ singularity，需要额外的 scale-independent damping。

### 9.3 Eq. (19)-Eq. (23)：Carosso RG 和 effective action

Appendix A.3 把 Eq. (5) 放回 statistical field theory 的 RG 语言。RG transformation 写成：

$$
q(\phi_\lambda)
:=
\int \mathcal{D}\phi_0\,
q(\phi_\lambda\mid\phi_0)
q(\phi_0).
\tag{19}
$$

bare field 的 density 写成 exponential form：

$$
q(\phi_0)
:=
\frac{1}{\mathcal{Z}_0}
e^{-S_0(\phi_0)}.
\tag{20}
$$

归一化常数是：

$$
\mathcal{Z}_0
:=
\int \mathcal{D}\phi_0\,
e^{-S_0(\phi_0)}.
\tag{21}
$$

这里 $S_0$ 是 action。它编码 fine-scale field 的统计结构。RG coarse-graining 后，新的 density 也可以写成 effective action：

$$
\int \mathcal{D}\phi_0\,
q(\phi_\lambda\mid\phi_0)q(\phi_0)
=
q(\phi_\lambda)
=
\frac{1}{\mathcal{Z}_0}
e^{-S_\lambda(\phi_\lambda)}.
\tag{22}
$$

归一化常数保持为：

$$
\mathcal{Z}_0
=
\int \mathcal{D}\phi_0 e^{-S_0(\phi_0)}
=
\int \mathcal{D}\phi_\lambda\mathcal{D}\phi_0\,
q(\phi_\lambda\mid\phi_0)e^{-S_0(\phi_0)}.
\tag{23}
$$

这组公式的作用是说明：coarse-graining 的效果被吸收到 action 从 $S_0$ 到 $S_\lambda$ 的变化里。本文 Eq. (7) 中的 squared path residual 就相当于一个 path-level effective action。

### 9.4 Eq. (24)-Eq. (31)：从 Euler-Maruyama 到 path density

Appendix A.4 展开 Eq. (7)。

先把 Eq. (6) 离散成：

$$
u_\lambda(t^{(n+1)})
=
u_\lambda(t^{(n)})
+
f_\lambda^\theta(u_\lambda(t^{(n)}))\Delta t
+
\sigma_\lambda\xi(t^{(n)})\Delta t.
\tag{24}
$$

white noise 在离散时间中的 convention 是：

$$
\xi(t^{(n)})
\sim
\mathcal{N}\left(0,\frac{1}{\Delta t}I_D\right).
\tag{25}
$$

这样 $\xi(t^{(n)})\Delta t$ 的 covariance 是 $\Delta t I_D$，符合 Wiener increment 的尺度。

对应噪声 density 为：

$$
\left(\frac{\Delta t}{2\pi}\right)^{D/2}
\exp\left[
-
\frac{\Delta t}{2}
\|\xi(t^{(n)})\|^2
\right].
\tag{26}
$$

由 Eq. (24) 解出：

$$
\xi(t^{(n)})
=
\frac{
u_\lambda(t^{(n+1)})
-
u_\lambda(t^{(n)})
-
f_\lambda^\theta(u_\lambda(t^{(n)}))\Delta t
}{
\sigma_\lambda\Delta t
}.
$$

代回 Eq. (26)，并考虑 change of variables 的常数 Jacobian，就得到 transition density：

$$
\begin{aligned}
p(u_\lambda(t^{(n+1)})\mid u_\lambda(t^{(n)}))
&=
(2\pi\sigma_\lambda^2\Delta t)^{-D/2}\\
&\quad\times
\exp\left[
-
\frac{
\|u_\lambda(t^{(n+1)})-u_\lambda(t^{(n)})
-f_\lambda^\theta(u_\lambda(t^{(n)}))\Delta t\|^2
}{
2\sigma_\lambda^2\Delta t
}
\right].
\end{aligned}
\tag{27}
$$

把每个 transition 连乘，并乘上初始密度 $r_\lambda$：

$$
\begin{aligned}
p_\lambda(\{u_\lambda\}_t)
&=
\frac{
r_\lambda(u_\lambda(t^{(0)}))
}{
(2\pi\sigma_\lambda^2\Delta t)^{DN_t/2}
}
\prod_{n=0}^{N_t-1}
\exp\left[
-
\frac{
\|u_\lambda(t^{(n+1)})-u_\lambda(t^{(n)})
-f_\lambda^\theta(u_\lambda(t^{(n)}))\Delta t\|^2
}{
2\sigma_\lambda^2\Delta t
}
\right].
\end{aligned}
\tag{28}
$$

把差分除以 $\Delta t$，得到：

$$
\begin{aligned}
p_\lambda(\{u_\lambda\}_t)
&=
\frac{r_\lambda(u_\lambda(t^{(0)}))}{Z_\lambda}
\prod_{n=0}^{N_t-1}
\exp\left[
-
\frac{\Delta t}{2\sigma_\lambda^2}
\left\|
\frac{u_\lambda(t^{(n+1)})-u_\lambda(t^{(n)})}{\Delta t}
-
f_\lambda^\theta(u_\lambda(t^{(n)}))
\right\|^2
\right].
\end{aligned}
\tag{29}
$$

最后用 $\partial_t u_\lambda$ 和 integral notation 压缩为：

$$
p_\lambda(\{u_\lambda\}_t)
=
\frac{r_\lambda(u_\lambda(t^{(0)}))}{Z_\lambda}
\exp\left[
-
\frac{1}{2\sigma_\lambda^2}
\int dt\,
\|\partial_t u_\lambda-f_\lambda^\theta(u_\lambda)\|^2
\right].
\tag{30}
$$

这里

$$
Z_\lambda
=
(2\pi\sigma_\lambda^2\Delta t)^{DN_t/2}.
$$

作者把下面的量视作 effective action：

$$
S_\lambda
=
\frac{1}{2\sigma_\lambda^2}
\int dt\,
\|\partial_t u_\lambda-f_\lambda^\theta(u_\lambda)\|^2.
\tag{31}
$$

因此 Eq. (7) 的 path density 不是拍脑袋写的，而是 transition density 连乘后的 Onsager-Machlup / path-integral 形式。

当 $\sigma_\lambda\to0$ 时，transition density 变成 delta distribution，path density 集中在 deterministic paths 上。数学上 path density 有分布意义的极限，但 path score 会因为 $1/\sigma_\lambda^2$ 发散，这就是后面要给 $\Sigma_\lambda$ 下界的原因。

### 9.5 Eq. (32)-Eq. (36)：history window 为什么仍然 Markov

实际网络用当前和过去四个 time steps。为了说明这不破坏理论，Appendix A.5 用一个只依赖当前和前一时刻的例子。

定义 augmented state：

$$
U^{(n)}
:=
\binom{
u_\lambda(t^{(n)})
}{
u_\lambda(t^{(n-1)})
}.
\tag{32}
$$

增强状态的演化写成：

$$
U^{(n+1)}
=
U^{(n)}
+
F(U^{(n)})\Delta t
+
G\Xi^{(n)}\Delta t.
\tag{33}
$$

其中：

$$
F(U^{(n)})
:=
\begin{pmatrix}
f_\lambda^\theta(u_\lambda(t^{(n)}),u_\lambda(t^{(n-1)}))\\
\dfrac{u_\lambda(t^{(n)})-u_\lambda(t^{(n-1)})}{\Delta t}
\end{pmatrix},
\quad
G
:=
\begin{pmatrix}
\sigma_\lambda I_D & 0\\
0 & 0
\end{pmatrix}.
\tag{34}
$$

第一行预测下一步，第二行只是把当前状态移入“过去状态”槽位。噪声只加到当前状态，不加到历史槽位。

于是原变量的 transition density 为：

$$
\begin{aligned}
p_\lambda(
u_\lambda(t^{(n+1)})
\mid
u_\lambda(t^{(n)}),u_\lambda(t^{(n-1)})
)
&=
\mathcal{N}\Big(
u_\lambda(t^{(n+1)});
u_\lambda(t^{(n)})\\
&\quad+
f_\lambda^\theta(u_\lambda(t^{(n)}),u_\lambda(t^{(n-1)}))\Delta t,
\sigma_\lambda^2\Delta t I_D
\Big).
\end{aligned}
\tag{35}
$$

路径密度对应分解为：

$$
p_\lambda(\{u_\lambda\}_t)
=
r_\lambda(u_\lambda(t^{(0)}),u_\lambda(t^{(-1)}))
\prod_{n=0}^{N_t-1}
p_\lambda(
u_\lambda(t^{(n+1)})
\mid
u_\lambda(t^{(n)}),u_\lambda(t^{(n-1)})
).
\tag{36}
$$

对更长窗口，逻辑相同：把过去若干步放进 state，过程就在 augmented state space 中 Markov。

### 9.6 Eq. (37)-Eq. (44)：KL minimization 给出 conditional increment

Appendix A.6 先假设 fine scale 存在真实 deterministic dynamics：

$$
\partial_t u_0(t)
=
f_0^{\mathrm{true}}(u_0(t)).
\tag{37}
$$

接着重写 coarse-graining kernel：

$$
q_\lambda(u_\lambda(t^{(n)})\mid u_0(t^{(n)}))
=
\mathcal{N}\left(
u_\lambda(t^{(n)});
\mathcal{C}_\lambda u_0(t^{(n)}),
\Sigma_\lambda
\right).
\tag{38}
$$

整条 path 的条件密度是：

$$
q_\lambda(\{u_\lambda\}_t\mid\{u_0\}_t)
=
\prod_{n=0}^{N_t}
q_\lambda(u_\lambda(t^{(n)})\mid u_0(t^{(n)})).
\tag{39}
$$

定义 joint density：

$$
q_\lambda^{\mathrm{joint}}(\{u_\lambda\}_t,\{u_0\}_t)
:=
q_\lambda(\{u_\lambda\}_t\mid\{u_0\}_t)
q_{\mathrm d}(\{u_0\}_t).
\tag{40}
$$

KL 写成：

$$
D_{\mathrm{KL}}(q_\lambda\|p_\lambda)
=
\int\mathcal{D}u_\lambda\,
q_\lambda(\{u_\lambda\}_t)
\ln
\frac{q_\lambda(\{u_\lambda\}_t)}{p_\lambda(\{u_\lambda\}_t)}.
\tag{41}
$$

由于 $q_\lambda$ 不依赖 $\theta$，关于 $\theta$ 的部分等价于：

$$
D_{\mathrm{KL}}(q_\lambda\|p_\lambda)
=
\mathbb{E}_{q_\lambda^{\mathrm{joint}}}
\left[
-\ln p_\lambda(\{u_\lambda\}_t)
\right]
+
\mathrm{const.}
\tag{42}
$$

把 Eq. (27)-Eq. (30) 代入，得到显式 loss：

$$
\begin{aligned}
\mathbb{E}_{q_\lambda^{\mathrm{joint}}}
\left[
\frac{1}{2\sigma_\lambda^2\Delta t}
\sum_{n=0}^{N_t-1}
\left\|
u_\lambda(t^{(n+1)})
-
u_\lambda(t^{(n)})
-
f_\lambda^\theta(u_\lambda(t^{(n)}))\Delta t
\right\|^2
\right].
\end{aligned}
\tag{43}
$$

对固定 $u_\lambda(t^{(n)})=u$，平方损失的 pointwise minimizer 是条件均值。因此：

$$
f_\lambda^*(u)\Delta t
=
\mathbb{E}
\left[
u_\lambda(t^{(n+1)})-u_\lambda(t^{(n)})
\mid
u_\lambda(t^{(n)})=u
\right].
\tag{44}
$$

这一步解释了 predictor 的统计意义：它学的是 coarse path 中 next increment 的 conditional expectation。

### 9.7 Eq. (45)-Eq. (50)：从 coarse increment 回到 fine dynamics

由于 Eq. (38) 中

$$
\mathbb{E}[u_\lambda(t^{(n+1)})\mid u_0(t^{(n+1)})]
=
\mathcal{C}_\lambda u_0(t^{(n+1)}),
$$

law of iterated expectations 给出：

$$
\begin{aligned}
\mathbb{E}
\left[
u_\lambda(t^{(n+1)})
\mid
u_\lambda(t^{(n)})
\right]
&=
\mathbb{E}
\left[
\mathbb{E}
\left[
u_\lambda(t^{(n+1)})
\mid
u_0(t^{(n+1)})
\right]
\mid
u_\lambda(t^{(n)})
\right]\\
&=
\mathbb{E}
\left[
\mathcal{C}_\lambda u_0(t^{(n+1)})
\mid
u_\lambda(t^{(n)})
\right].
\end{aligned}
\tag{45}
$$

把 Eq. (45) 代入 Eq. (44)：

$$
f_\lambda^*(u_\lambda(t^{(n)}))\Delta t
=
\mathbb{E}
\left[
\mathcal{C}_\lambda u_0(t^{(n+1)})
\mid
u_\lambda(t^{(n)})
\right]
-
u_\lambda(t^{(n)}).
\tag{46}
$$

然后加减同一个量

$$
\mathbb{E}[\mathcal{C}_\lambda u_0(t^{(n)})\mid u_\lambda(t^{(n)})],
$$

得到：

$$
\begin{aligned}
f_\lambda^*(u_\lambda(t^{(n)}))\Delta t
&=
\mathbb{E}
\left[
\mathcal{C}_\lambda
\left[
u_0(t^{(n+1)})-u_0(t^{(n)})
\right]
\mid
u_\lambda(t^{(n)})
\right]\\
&\quad+
\left(
\mathbb{E}
\left[
\mathcal{C}_\lambda u_0(t^{(n)})
\mid
u_\lambda(t^{(n)})
\right]
-
u_\lambda(t^{(n)})
\right).
\end{aligned}
\tag{47}
$$

第一项是 coarse-grained true increment。第二项是 denoising correction：

$$
\delta_\lambda^{(n)}
:=
\mathbb{E}
\left[
\mathcal{C}_\lambda u_0(t^{(n)})
\mid
u_\lambda(t^{(n)})
\right]
-
u_\lambda(t^{(n)}).
\tag{48}
$$

为什么会有 correction？因为 $u_\lambda(t^{(n)})$ 不是 $\mathcal{C}_\lambda u_0(t^{(n)})$ 本身，而是带噪观测：

$$
u_\lambda(t^{(n)})
=
\mathcal{C}_\lambda u_0(t^{(n)})
+
\sqrt{\Sigma_\lambda}\epsilon(t^{(n)}).
$$

因此，给定 noisy coarse observation 后，对 clean coarse mean 的 posterior expectation 不等于 observation 本身。

真实 fine dynamics 给出：

$$
\mathcal{C}_\lambda
\left[
u_0(t^{(n+1)})-u_0(t^{(n)})
\right]
=
\mathcal{C}_\lambda
\left(
\int_{t^{(n)}}^{t^{(n)}+\Delta t}
f_0^{\mathrm{true}}(u_0(t'))\,dt'
\right).
\tag{49}
$$

如果 $\Delta t$ 足够小：

$$
\mathcal{C}_\lambda
\left[
u_0(t^{(n+1)})-u_0(t^{(n)})
\right]
\approx
\mathcal{C}_\lambda f_0^{\mathrm{true}}(u_0(t^{(n)}))\Delta t.
\tag{50}
$$

这就是 Eq. (10) 的来源。主文把 denoising correction 暂时压掉，强调第一项的物理意义；Appendix 说明 exact optimum 还包含 Eq. (48)。

### 9.8 Eq. (51)-Eq. (54)：denoising correction 的 Tweedie 形式

Eq. (48) 依赖未知 posterior，所以一般不能闭式计算。但由于 Eq. (38) 是 additive Gaussian noise model，可以用 Tweedie-type identity：

$$
\mathbb{E}
\left[
\mathcal{C}_\lambda u_0(t^{(n)})
\mid
u_\lambda(t^{(n)})=u_\lambda
\right]
-
u_\lambda
=
\Sigma_\lambda
\nabla_{u_\lambda}
\ln q_\lambda^{(n)}(u_\lambda).
\tag{51}
$$

直观地说，denoising correction 指向当前 noisy sample 在 marginal density 中更高概率的方向。它和 score 相关，所以形式上像 denoising score matching 里的 correction。

若进一步假设 data marginal 是 Gaussian：

$$
u_0(t^{(n)})
\sim
\mathcal{N}(\bar{u}_{\mathrm d},\Sigma_{\mathrm d}),
$$

posterior mean 为：

$$
\begin{aligned}
\mathbb{E}
\left[
\mathcal{C}_\lambda u_0(t^{(n)})
\mid
u_\lambda(t^{(n)})=u_\lambda
\right]
&=
\mathcal{C}_\lambda\bar{u}_{\mathrm d}
+
\Sigma_{\mathrm d}'
(\Sigma_{\mathrm d}'+\Sigma_\lambda)^{-1}
(u_\lambda-\mathcal{C}_\lambda\bar{u}_{\mathrm d}).
\end{aligned}
\tag{52}
$$

其中：

$$
\Sigma_{\mathrm d}'
:=
\mathcal{C}_\lambda
\Sigma_{\mathrm d}
\mathcal{C}_\lambda^\top.
\tag{53}
$$

因此 correction 变成：

$$
\left.
\delta_\lambda^{(n)}
\right|_{u_\lambda(t^{(n)})=u_\lambda}
=
-
\Sigma_\lambda
(\Sigma_{\mathrm d}'+\Sigma_\lambda)^{-1}
(u_\lambda-\mathcal{C}_\lambda\bar{u}_{\mathrm d}).
\tag{54}
$$

如果 $\lambda\to0$，那么 $\Sigma_\lambda\to0$，correction 消失，Eq. (47) 回到主文 Eq. (10) 的直觉形式。

### 9.9 Eq. (55)-Eq. (58)：$\sigma_\lambda$ 如何设定

Appendix A.7 解释 physical-time SDE 中 $\sigma_\lambda$ 的来源。

从 Eq. (3) 得到每个 time step 的 coarse state：

$$
u_\lambda(\cdot,t^{(n)})
=
\mathcal{C}_\lambda u_0(\cdot,t^{(n)})
+
\sqrt{\Sigma_\lambda}\epsilon(\cdot,t^{(n)}).
\tag{55}
$$

做时间差分：

$$
\begin{aligned}
u_\lambda(\cdot,t^{(n+1)})
-
u_\lambda(\cdot,t^{(n)})
&=
\mathcal{C}_\lambda
\left[
u_0(\cdot,t^{(n+1)})
-
u_0(\cdot,t^{(n)})
\right]\\
&\quad+
\sqrt{\Sigma_\lambda}
\left[
\epsilon(\cdot,t^{(n+1)})
-
\epsilon(\cdot,t^{(n)})
\right].
\end{aligned}
\tag{56}
$$

第一项对应 Eq. (24) 中的 drift increment。第二项对应 unresolved stochastic increment。因此 coarse-graining 自然诱导了 physical-time noise。

对 Eq. (56) 取 conditional expectation：

$$
\begin{aligned}
&\mathbb{E}
\left[
u_\lambda(t^{(n+1)})-u_\lambda(t^{(n)})
\mid
u_\lambda(t^{(n)})
\right]\\
&=
\mathbb{E}
\left[
\mathcal{C}_\lambda
\left[
u_0(t^{(n+1)})-u_0(t^{(n)})
\right]
\mid
u_\lambda(t^{(n)})
\right]
-
\sqrt{\Sigma_\lambda}
\mathbb{E}
\left[
\epsilon(t^{(n)})
\mid
u_\lambda(t^{(n)})
\right].
\end{aligned}
\tag{57}
$$

$\epsilon(t^{(n+1)})$ 和当前 $u_\lambda(t^{(n)})$ 独立，所以其 conditional expectation 为 0。$\epsilon(t^{(n)})$ 不独立，因为它直接出现在当前 observation 里，所以留下来。这个留下来的项正是 denoising correction 的另一种写法。

为了给 $\sigma_\lambda$ 一个 concrete value，作者匹配 surrogate model 的 conditional covariance 和 coarse-graining noise 的平均 variance。Eq. (24) 的 conditional covariance 是：

$$
\sigma_\lambda^2\Delta t\,I_D.
$$

用 trace 匹配 $\Sigma_\lambda$：

$$
\sigma_\lambda^2
=
\frac{1}{\Delta t\cdot D}
\operatorname{tr}(\Sigma_\lambda).
\tag{58}
$$

这说明 $\sigma_\lambda$ 表示 coarse-graining noise 的 typical scale。

当 $\lambda\to0$，Eq. (18) 给出 $\Sigma_\lambda\to0$，于是 $\sigma_\lambda\to0$。path density 本身趋于 deterministic limit，但 path score 会发散。数值上，作者把 $\Sigma_\lambda$ 下界设为最小非零 diffusion scale $\Delta\lambda=10^{-3}$ 处的 covariance，防止 score divergence。

---

## 十、Appendix B：实验方法和算法细节

### 10.1 Eq. (59)-Eq. (60)：Lorenz-96 two-scale model

Lorenz-96 是一维周期域上的理想化大气模型。慢变量 $X_k$ 和快变量 $Y_{j,k}$ 满足：

$$
\frac{d}{dt}X_k
=
-X_{k-1}(X_{k-2}-X_{k+1})
-X_k
+F
-
\left(\frac{hc}{b}\right)
\sum_{j=1}^{J}Y_{j,k}.
\tag{59}
$$

$$
\frac{d}{dt}Y_{j,k}
=
-cbY_{j+1,k}(Y_{j+2,k}-Y_{j-1,k})
-cY_{j,k}
+
\frac{hc}{b}X_k.
\tag{60}
$$

$X$ 是 slow large-scale variable，$Y$ 是 fast small-scale variable。$Y$ 通过 $\sum_jY_{j,k}$ 反馈到 $X_k$，$X_k$ 又驱动对应的 $Y_{j,k}$。这正好提供一个跨尺度耦合测试场景。

参数设定为 $K=32,J=4$，所以总 spatial grid points 为 $KJ=128$。$F=b=c=10,h=1$。$b,c$ 让 slow 和 fast variables 的 amplitude 和 timescale 大约相差一个数量级。

### 10.2 Eq. (61)-Eq. (62)：Kolmogorov flow

Kolmogorov flow 用 vorticity form：

$$
\frac{\partial\zeta}{\partial t}
+
\mathbf{V}\cdot\nabla_x\zeta
=
-\mu\zeta
+
\nu\nabla_x^2\zeta
-
k_{\mathrm{forcing}}\cos(k_{\mathrm{forcing}}y).
\tag{61}
$$

vorticity、stream function、velocity 的关系是：

$$
\zeta=\nabla_x^2\psi
\quad\text{and}\quad
\mathbf{V}
=
\left(
-\frac{\partial\psi}{\partial y},
\frac{\partial\psi}{\partial x}
\right)^\top .
\tag{62}
$$

这里 $\zeta$ 是涡度，$\psi$ 是流函数，$\mathbf{V}$ 是不可压速度场。实验用 periodic domain $[0,2\pi)^2$，参数 $\mu=0.1,\nu=10^{-3},k_{\mathrm{forcing}}=4$。

### 10.3 网络结构

主实验使用 U-Net。Lorenz-96 用 1D convolution，Kolmogorov flow 用 2D convolution。网络输入包括当前状态和前 4 个 time steps。输出是 time derivative 的 finite-difference approximation。

这个设计与理论中的 history-window state augmentation 对齐。粗粒化后 dynamics 不再严格 Markov，所以用多个历史步帮助 predictor 表示 memory effects。

作者还用 FNO 做替代架构实验。FNO 不用 U-Net convolution/downsampling 和 self-attention，而是在 Fourier space 做 spectral convolution。Appendix D.5 说明框架不依赖特定 backbone。

### 10.4 Eq. (63)-Eq. (64)：评价指标

short-term prediction 用 relative $L^2$ error：

$$
\text{Relative } L^2 \text{ Error}(t)
:=
\frac{
\|u(\cdot,t)-\hat{u}(\cdot,t)\|_2
}{
\|u(\cdot,t)\|_2
}.
\tag{63}
$$

long-term statistical consistency 用 relative spectral error：

$$
\text{Relative Spectral Error}
:=
\frac{
\left\|
|\mathcal{G}[u]|^2
-
|\mathcal{G}[\hat{u}]|^2
\right\|_1
}{
\left\|
|\mathcal{G}[u]|^2
\right\|_1
}.
\tag{64}
$$

$\mathcal{G}$ 是对 space 和 time 的 Fourier transform。这个指标不要求单条 chaotic trajectory 长期逐点对齐，而是比较 spatiotemporal power spectrum 是否一致。

### 10.5 Algorithm 1：训练

训练步骤是：

1. 从训练集采样 fine path $\{u_0\}_t$。
2. 采样 $\lambda\sim\mathcal{U}(0,1)$ 和 $\epsilon\sim\mathcal{N}(0,I)$。
3. 用 Eq. (3) 构造 $u_\lambda=\mathcal{C}_\lambda u_0+\sqrt{\Sigma_\lambda}\epsilon$。
4. 用 Eq. (9) 计算 temporal derivative regression loss。
5. 更新 $\theta$。

这说明训练阶段不做 physical-time rollout，也不做 reverse-$\lambda$ sampling。训练成本接近普通 denoising training 的单步网络评估。

### 10.6 Algorithm 2：固定 $\lambda$ 的 forward simulation

Algorithm 2 从 fine-resolution initial condition 开始，先构造 coarse initial condition：

$$
u_\lambda(\cdot,t^{(0)})
\leftarrow
\mathcal{C}_\lambda u_0(\cdot,t^{(0)}).
$$

然后按 Eq. (6) 逐步前进。评估时常设 $\sigma_\lambda=0$，因为作者要和 deterministic coarse reference 比较。

### 10.7 Eq. (65)-Eq. (66)：predictor-corrector 和 ETD

reverse-$\lambda$ sampling 使用 predictor-corrector。corrector 是 Langevin step：

$$
u_\lambda'
=
u_\lambda
+
\chi s_\lambda
+
\sqrt{2\chi}z.
\tag{65}
$$

其中

$$
\chi
=
2\left(
\kappa\frac{\|z\|_2}{\|s_\lambda\|_2}
\right)^2,
\quad
z\sim\mathcal{N}(0,I).
$$

$\kappa$ 是 signal-to-noise ratio parameter。作者用 validation set 选 $\kappa=0.7$ for Lorenz-96，$\kappa=0.3$ for Kolmogorov flow。

predictor step 用 exponential time differencing，因为 reverse-$\lambda$ 时 Laplacian 变成 anti-diffusion，高波数会快速放大。Fourier space update 是：

$$
\begin{aligned}
\widetilde{u}_{\lambda-\Delta\lambda}(k,t)
&=
e^{\alpha\|k\|^2\Delta\lambda}
\widetilde{u}_\lambda(k,t)\\
&\quad+
\varphi(\alpha\|k\|^2\Delta\lambda)
\beta^2\widetilde{s}_\lambda(k,t)\Delta\lambda
+
\beta\widetilde{\eta}_\lambda(k,t)\Delta\lambda.
\end{aligned}
\tag{66}
$$

其中：

$$
\varphi(z)=\frac{e^z-1}{z},
\quad
\varphi(0)=1.
$$

为什么要用 ETD？因为 reverse 方向上，forward damping

$$
e^{-\alpha\|k\|^2\lambda}
$$

变成 high-wavenumber amplification：

$$
e^{\alpha\|k\|^2\Delta\lambda}.
$$

显式方法会因高波数刚性而不稳定。ETD 把线性 Laplacian 部分解析处理，剩下 score term 用 $\varphi$ 函数修正。

注意作者没有把 exponential amplification 乘到 noise term 上。原因是 Eq. (11) 假设 $\eta_\lambda$ 是 spatially white noise；如果也乘 $e^{\alpha\|k\|^2\Delta\lambda}$，噪声会变成 $k$-dependent，不再符合设定。

### 10.8 Algorithm 3：generation / super-resolution

Algorithm 3 有两个初始化方式：

1. Generation：在 $\lambda_{\max}$ 从 $\mathcal{N}(0,\Sigma_{\lambda_{\max}})$ 采样一整条 path。
2. Super-resolution：把 low-resolution path 作为 $\lambda_{\max}$ 的起点。

每个 reverse-$\lambda$ step 做：

1. 计算 $s_\lambda=\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t)$。
2. 用 Eq. (66) 做 predictor update。
3. 对 $t^{(0)}$ 做 boundary extrapolation。
4. 做 3 次 Langevin corrector Eq. (65)。

这里 boundary extrapolation 是为了绕开 $r_\lambda$ 的 score。训练和 simulation 不需要 $r_\lambda$，但 reverse sampling 的 path score 在 $t^{(0)}$ 会包含 $\nabla\ln r_\lambda$。作者没有显式建模它，而是用线性外推稳定边界。这也是 limitation 之一。

### 10.9 computational cost

训练便宜，因为每次只采一个 $\lambda$ 并做 local derivative regression。

simulation 便宜，因为只沿 $t$ 前向评估 predictor。

generation 和 super-resolution 贵，因为每个 reverse-$\lambda$ step 都要计算 path score。这个 score 是对整条 spatiotemporal tensor 的 input gradient，相当于一次 reverse-mode automatic differentiation。成本随 reverse-$\lambda$ steps 和 temporal length $N_t$ 近似线性增长。

---

## 十一、Appendix C-D：扩展实验如何支撑主结论

### 11.1 Figure 5-7：simulation 的补充验证

Figure 5 在 $\lambda=0$ 比较 Lorenz-96 的 physics simulation、surrogate prediction 和 DDPM baseline。

![Figure 5 — Lorenz-96 simulation at lambda 0](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-26-figure-01.jpg)

![Figure 5 — Lorenz-96 PSD at lambda 0](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-26-figure-02.jpg)

它的作用是支撑 Table 1：在 fine resolution 下，本文 surrogate 和 DDPM baseline 都能接近 physics-based simulation。

Figure 6 对 Kolmogorov flow 做同样比较。它强调 vorticity snapshot 和 PSD 都能被两类模型复现。

Figure 7 才是对本文更重要的图：它画出 evaluation metrics 随 $\lambda$ 的变化。随着 $\lambda$ 增大，spectral error 变大，说明 coarse-grained dynamics 更难预测。这符合 intuition：小尺度被消除后，大尺度 history-dependence 更强。

同时 $L^2$ error 对 $\lambda$ 较不敏感，甚至 Lorenz-96 在中间 $\lambda$ 处可能下降。原因是 coarse-graining 移除了 fast variable 的小尺度成分，使短期误差表面上变小。这个结果提醒我们：对 chaotic multiscale system，只看 short-term $L^2$ 不够，必须看 spectral statistics。

### 11.2 Figure 8-9：unconditional generation

Figure 8 展示 Lorenz-96 的 unconditional generation，Figure 9 展示 Kolmogorov flow 的 unconditional generation。

![Figure 8 — Lorenz-96 unconditional generation](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-28-figure-01.jpg)

![Figure 9 — Kolmogorov flow unconditional generation](../../pdfs/2026-04-16/predictor-driven-diffusion-for-spatiotemporal-generation.mineru/hybrid_auto/images/page-28-figure-04.jpg)

这两组图的功能不是展示单个样本完全等于某个 reference，而是看 generated samples 是否拥有类似的 spatiotemporal patterns 和 PSD。它们支撑 Table 2：predictor-defined path score 可以用于生成。

### 11.3 Figure 10：simulation with noise

Appendix D.1 只在这一节用 $\sigma_\lambda>0$ 做 temporal simulation。参考数据也按照 Eq. (3) 加噪。

Figure 10 比较 $\lambda=0.2$ 和 $\lambda=0.4$。在 $\lambda=0.2$，模型仍能给出类似 reference 的预测；到 $\lambda=0.4$，signal-to-noise ratio 下降，结果更难与 reference 对齐。

这个实验说明：Eq. (6) 的噪声项数值上可用，但主文为了清楚比较 deterministic coarse reference，把 simulation evaluation 中的 $\sigma_\lambda$ 设为 0。

### 11.4 Figure 11-12：输入历史窗口和 Mori-Zwanzig

Figure 11 用 only current time step 作为输入。结果是：

1. 在 $\lambda=0$，Lorenz-96 fine system 本来 Markov，所以单步输入也能预测。
2. 在 $\lambda=0.2$，coarse-graining 后单步输入失败，生成 monotonous patterns。

Figure 12 进一步显示，在 $\lambda=0.2$，input window 从 5 增加到 15，spectral error 从约 0.6 降到约 0.3。

这和 Mori-Zwanzig projection formalism 一致。消除小尺度变量后，大尺度变量的有效 dynamics 通常包含 memory term 和 noise term。因此 coarse-grained dynamics 不再 Markov，需要 history window 来补偿被消除变量的影响。

### 11.5 Eq. (67) 和 Figure 13-14：Laplacian term 的作用

Appendix D.3 比较 variance-preserving process 和加入 Laplacian 的版本：

$$
\partial_\lambda u_\lambda(x,t)
=
(\alpha\nabla_x^2-\gamma)u_\lambda(x,t)
+
\beta\eta_\lambda(x,t).
\tag{67}
$$

若 $\alpha=0$，所有 Fourier modes 以同样速率 damping。这是 scale-uniform 的 VP-like process。Figure 13 显示它不能建立明确 spatial hierarchy。

若 $\alpha=0.1$，即使保留 uniform damping $-\gamma u_\lambda$，Laplacian 仍会让 high-wavenumber modes 更快衰减。Figure 14 显示小尺度结构被有效 suppress。

所以决定 spatial hierarchy 的关键是 Laplacian term，而不是单纯 damping/noise。

### 11.6 Eq. (68) 和 Figure 15-16：noise injection 的必要性

Appendix D.4 做 noise ablation。作者训练一个 deterministic coarse-graining model：

$$
u_\lambda(x,t)
=
\mathcal{C}_\lambda u_0(x,t).
\tag{68}
$$

这等于在 Eq. (3) 里设置 $\epsilon=0$。

Figure 15 显示：没有 noise injection，$\lambda\approx0$ 的 simulation 仍可稳定，但 $\lambda$ 增大后数值不稳定增强。

generation 直接失败，样本像 noise。

Figure 16 显示：即使选择很小的 $\lambda=0.025$ 做 coarse input，super-resolution 也失败。

这组实验和 RG 理论对应非常紧。没有 noise，就没有 distribution convolution；没有 statistical integration，就没有学到如何从 coarse representation 重建小尺度 distribution。deterministic smoothing 不能替代 RG coarse-graining。

### 11.7 Figure 17：FNO 架构鲁棒性

Figure 17 用 FNO 替换 U-Net，展示 Lorenz-96 的 simulation 和 super-resolution。结果与 U-Net 相当。

这说明贡献主要来自 framework：

$$
\text{spatial RG axis}
+
\text{temporal predictor path density}
+
\text{reverse-}\lambda\text{ sampling},
$$

而不是某个特定 U-Net 结构。

---

## 十二、对 Synthetic_City 的直接启发

这篇文章对 Synthetic_City 有用，不是因为城市系统一定满足 Lorenz-96 或 Kolmogorov flow 那样的 PDE，而是因为它给出了一个清晰的生成结构：把真实演化时间和空间分辨率拆开。

在 Synthetic_City 中，可以做如下类比：

$$
\begin{aligned}
t
&\Longleftrightarrow
\text{年份、迁移阶段、scenario step 或 policy time},\\
\lambda
&\Longleftrightarrow
\text{spatial coarse-graining level},\\
u_\lambda(x,t)
&\Longleftrightarrow
\text{某个分辨率下的 population / household / activity field}.
\end{aligned}
$$

如果我们要从 coarse census summaries 生成 finer spatial allocation，一个直接风险是把时间预测和空间细化混成一个 diffusion chain。这样模型可能在训练中用未来信息解释当前分布，或者在空间细化时破坏跨时间一致性。

本文建议的结构更稳：

第一，沿真实时间 $t$ 训练 causal predictor。这个 predictor 学的是：

$$
\text{given current and past urban state}
\quad\rightarrow\quad
\text{predict next urban state}.
$$

第二，沿空间尺度 $\lambda$ 定义 coarse-to-fine path。大的 $\lambda$ 可以表示更粗的行政层级或更低空间分辨率，小的 $\lambda$ 表示更细的 spatial allocation。

第三，用 predictor-induced path density 给 reverse-$\lambda$ sampling 提供 score。这样空间细化不是单张图像超分辨率，而是整条城市演化轨迹的超分辨率。

需要注意的是，城市空间不一定是 regular Euclidean grid。PUMA、tract、block group 是不规则 polygon / graph。因此，如果把本文迁移到 Synthetic_City，$\nabla_x^2$ 不能直接照搬成 regular-grid Laplacian，更可能需要：

$$
\text{graph Laplacian}
\quad\text{or}\quad
\text{administrative adjacency / mobility-weighted Laplacian}.
$$

这也解释了为什么 graph-aware diffusion 值得接着看。城市问题中的 spatial coarse-graining 很可能不是视觉 blur，而是行政区、交通联系、通勤流和人口分布共同定义的 graph diffusion / aggregation。

---

## 十三、和 PRX speed-accuracy 文章的衔接

PRX speed-accuracy 文章告诉我们：diffusion model 的 forward path 不是随便选的；如果 path 在 distribution space 中运动代价很高，reverse generation 对 initial mismatch 会更敏感。它强调的是 protocol robustness。

本文进一步给出 spatiotemporal data 的 protocol decomposition：

$$
\text{physical time } t
\neq
\text{diffusion scale } \lambda.
$$

把两篇文章放在一起，可以得到一个更完整的生成模型设计原则。

第一，生成过程应该有清楚的 distributional path，而不是任意 schedule。

第二，对时空数据，path 的坐标轴要尊重物理含义。时间轴负责因果预测，尺度轴负责 coarse-to-fine generation。

第三，reverse sampling 的 score 不一定必须来自单独 score network。它也可以来自 predictor 定义的 path density。

共同结构是：

$$
\begin{aligned}
\text{define a path}
&\rightarrow
\text{define a cost or density on the path}\\
&\rightarrow
\text{derive a flow / score / control to move along the path}.
\end{aligned}
$$

差异在于，各框架对 path 的解释不同。VI 偏向 posterior approximation，HJB 偏向 optimal control，PRX diffusion thermodynamics 偏向 entropy production and OT，Predictor-Driven Diffusion 偏向 causal temporal prediction plus spatial RG.

---

## 十四、最终记忆版

这篇文章可以记成一句话：

Predictor-Driven Diffusion 把 physical time $t$ 和 spatial diffusion scale $\lambda$ 拆开：用 causal predictor 学时间演化，用 RG diffusion 学空间尺度层级，再用 predictor-induced path density 的 score 做 reverse-$\lambda$ generation 和 super-resolution。

最核心的公式链是：

$$
\begin{aligned}
\partial_\lambda u_\lambda
&=
\alpha\nabla_x^2u_\lambda+\beta\eta_\lambda
\quad\text{(spatial RG coarse-graining)},\\
\partial_t u_\lambda
&=
f_\lambda^\theta(u_\lambda)+\sigma_\lambda\xi
\quad\text{(causal temporal predictor)},\\
p_\lambda(\{u_\lambda\}_t)
&\propto
\exp\left[
-
\int_{\mathrm{x,t}}
\frac{\|\partial_tu_\lambda-f_\lambda^\theta(u_\lambda)\|^2}
{2\sigma_\lambda^2}
\right]
\quad\text{(path density)},\\
s_\lambda
&=
\nabla_{u_\lambda}\ln p_\lambda(\{u_\lambda\}_t)
\quad\text{(path score)},\\
\partial_\lambda u_\lambda
&=
\alpha\nabla_x^2u_\lambda-\beta^2s_\lambda+\beta\eta_\lambda
\quad\text{(reverse-}\lambda\text{ sampling)}.
\end{aligned}
$$

如果只记一个建模原则，就是：

$$
\text{time causality should be handled by predictor,}
\quad
\text{spatial scale should be handled by RG diffusion.}
$$

---

## 关键术语索引

| 中文 | 英文 | 简述 |
|---|---|---|
| 扩散尺度 | diffusion scale $\lambda$ | 参数化空间粗粒化程度的连续变量 |
| 物理时间 | physical time $t$ | 系统真实演化时间，必须保持因果性 |
| 粗粒化算子 | coarse-graining operator $\mathcal{C}_\lambda$ | $e^{\lambda\alpha\nabla_x^2}$，在 Fourier space 中逐模式指数衰减 |
| 协方差 | covariance $\Sigma_\lambda$ | forward RG diffusion 累积噪声产生的空间协方差 |
| 路径密度 | path density $p_\lambda$ | predictor 在 physical time 上诱导的 trajectory probability |
| 路径分数 | path score $s_\lambda$ | $\nabla_{u_\lambda}\ln p_\lambda$，用于 reverse-$\lambda$ sampling |
| 有效作用量 | effective action $S_\lambda$ | path residual energy，决定 path density 的指数 |
| 重正化群 | renormalization group | 通过积分掉小尺度自由度建立尺度层级 |
| Mori-Zwanzig | Mori-Zwanzig formalism | 解释粗粒化后 memory/noise 项为何出现 |
| 指数时间差分 | exponential time differencing | 用于处理 reverse-$\lambda$ anti-diffusion 的刚性 |
| 超分辨率 | super-resolution | 从大 $\lambda$ 的 coarse path 恢复到 $\lambda=0$ 的 fine path |
| 功率谱密度 | power spectral density | 衡量时空频率能量分布的统计量 |
