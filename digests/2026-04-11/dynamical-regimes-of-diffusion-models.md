---
title: "Dynamical regimes of diffusion models"
paper_title: "Dynamical regimes of diffusion models"
digest_type: "paper_note"
date: "2026-04-11"
---

# Dynamical Regimes Of Diffusion Models

## Core Answer

这篇文章的核心回答是：在高维、大样本、且 score 被最优训练到经验分布的极限下，diffusion model 的 backward dynamics 不是单一的 denoising 过程，而是依次经历 `pure noise -> class-level speciation -> sample-level collapse` 三个阶段；其中 speciation time 由协方差谱控制，collapse time 由熵控制，而最终是否过早进入 memorization，则由

$$
\alpha=\frac{\log n}{d}
$$

这个高维尺度比值决定。

## 0. Reading Frame

为了防止后面公式和图像越看越散，先把这篇的阅读框架固定下来：

1. 它要解决的问题是：diffusion model 的 backward generation 在高维和大样本极限下究竟处于什么动力学机制之下。
2. 它重要的地方在于：它直接回答了 diffusion 到底是在 generalize 还是 memorize。
3. 它研究的对象是 forward noising、backward generative process、exact empirical score 以及高维数据分布。
4. 它最核心的演化图像是三个 regime：pure noise、speciation、collapse。
5. 它关心的关键量是 speciation time、collapse time、协方差谱和 excess entropy。
6. 它的方法是：高维统计物理分析 + Gaussian mixture 可解模型 + 真实数据集数值验证。
7. 它最有说服力的证据是：speciation 在不同数据集上按 $t/t_S$ 对齐，collapse 可由熵判据与经验观测共同定位。
8. 你最后要带走的是：diffusion backward process 本身就是一个有阶段结构的高维随机动力学。

## 1. The Main Question And The Three-Regime Picture

这篇文章真正要回答的问题不是“diffusion model 效果好不好”，而是：在 backward generation 过程中，轨迹什么时候只是噪声，什么时候开始显示类别结构，什么时候又会进一步掉进具体训练样本。作者之所以能把这个问题说清楚，是因为他们研究的是一个干净极限：数据维度大、样本数大，而且模型学到的是 `exact empirical score`。

这里的 `dimension` 不是抽象的“维数”概念，而是单个数据样本在表示空间中的坐标数，也就是如果数据写成

$$
a\in\mathbb R^d,
$$

那么 $d$ 就是每个样本的维度。对图像来说，它基本就是像素数乘通道数。作者之所以一直强调 large $d$，是因为高维里向量长度、距离、体积和熵都会按维度放大，而样本数若增长不够快，就无法真正覆盖数据空间。

这篇还明确区分了两种分布。一种是潜在真实分布 $P_0(a)$，另一种是由有限训练样本构成的经验分布

$$
\hat P_0(a)=\frac1n\sum_{\mu=1}^n\delta(a-a^\mu).
$$

这一对区分非常关键，因为后面整篇文章讨论的 `exact empirical score`，说的就是模型学到的是经验分布加噪后的精确 score，而不是 population distribution 的平滑 score。这正是后来会出现 sample-level collapse 和 memorization 倾向的根源。

![Fig. 1 three dynamical regimes](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-01-figure-01.jpg)

`Figure 1` 先给出这篇文章最应该记住的几何图像。最开始是 regime I，轨迹还基本像从一团噪声里往回走，没有真正分出类别。接着进入 regime II，也就是 `speciation`，轨迹开始按类别分成不同 bundle。最后进入 regime III，也就是 `collapse`，这些 class-level bundles 进一步碎裂成围绕具体训练样本的团块。于是，这篇文章最核心的区分就是：

- `speciation` 是 class-level commitment
- `collapse` 是 sample-level commitment

也正因为如此，它给出的不是一句“diffusion 是 generalize 还是 memorize”的二选一，而是一条时间序列：它先表现为 class-level generalization，最后在 exact empirical score 极限下走向 sample-level memorization。

## 2. Speciation: When Class Structure Becomes Dynamically Visible

![Equation 4](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-01-equation-04.jpg)

speciation 的控制时间由 `Eq. (4)` 给出：

$$
\Lambda e^{-2t_S}=1,
$$

也就是

$$
t_S=\frac{1}{2}\log\Lambda.
$$

这里的 $\Lambda$ 是数据协方差矩阵最大的特征值，表示最显著的类结构强度。前向加噪会把这条最强结构乘上 $e^{-2t}$，因此真正控制类别可分性的不是 $\Lambda$ 本身，而是

$$
\Lambda e^{-2t}.
$$

当它远大于 $1$ 时，类结构还足够强，backward trajectory 有能力分出不同类别；当它远小于 $1$ 时，噪声已经把这条结构埋没，轨迹还没有“选边”。于是，作者把它降到 $O(1)$ 的时刻定义为 speciation time。

这也是为什么作者把 speciation 类比成 symmetry breaking。原来轨迹对不同类别还没有偏向，后来开始稳定地朝某一类分叉。更进一步，这个 cross-over 在大维极限下会越来越尖锐。如果典型地有 $\Lambda\propto d$，那么

$$
t_S\sim \frac{1}{2}\log d.
$$

随着维度升高，transition 发生的位置被推向更大的 $t$，但发生分化的窗口本身仍是 $O(1)$，于是相对宽度越来越小，看起来就越来越像 phase transition。

![Fig. 4 speciation in realistic datasets](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-05-figure-01.jpg)

`Figure 4` 正好支持这一点。把不同真实数据集上的时间轴都 rescale 成 $t/t_S$ 之后，speciation 的转折都收敛到 $t/t_S\approx 1$ 附近。右侧蓝区是“对称尚未破裂”，左侧红区是“类别已经被选定”。这说明 `Eq. (4)` 确实抓住了 speciation 的共同控制变量。

## 3. How Speciation Time Is Measured In Practice

单有 `Eq. (4)` 还不够，作者还需要在真实数据上给 speciation 一个可操作的数值定义。他们没有直接看样本“像不像某一类”，而是设计了一个 cloning procedure。核心问题是：如果在时间 $t$ 时，轨迹的类别命运已经被决定，那么从这个时刻复制出两个 clone，并让它们在独立噪声下继续往 $t=0$ 演化，它们最后应该落到同一类；反之，如果类别还没决定，两个 clone 仍可能去不同类。

于是作者定义

$$
\phi(t)=\Pr[\text{两个 clone 最终落到同一类}].
$$

这个概率有非常清楚的两个极限。在 $t\gg t_S$ 的 regime I，类别还没固定，对二分类来说

$$
\phi(t)\approx \frac{1}{2}.
$$

在 $t\ll t_S$ 的 regime II，类别命运已经形成，两个 clone 虽然后续噪声不同，但最终几乎总会落到同一类，因此

$$
\phi(t)\approx 1.
$$

真实图像数据里，类别标签不是直接写在轨迹上的，所以作者用一个高精度 `ResNet-18` classifier 给 clone 的终点打 class label。这样，`Figure 4` 中的曲线就变成了“类别命运是否已经被决定”的直接测量，而不是静态视觉相似度。

因此，这一节的方法论意义也很清楚：作者测量的不是“当前样本看起来像哪一类”，而是“如果在时间 $t$ 复制这条轨迹，它未来的类别命运是否已经稳定”。这比静态分类更贴近他们对 speciation 的动力学定义。

## 4. Why The Cloning Probability Has The Form Of Equation (6)

![Equation 6](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-03-equation-01.jpg)

在两类 Gaussian mixture toy model 里，`Eq. (6)` 把上面的 cloning 定义写成了一个显式公式：

$$
\phi (t) = \frac {1}{2} \int_ {- \infty} ^ {+ \infty} d y \,
\frac {G \left(y , m e ^ {- t} , \Gamma_ {t}\right) ^ {2} + G \left(y , - m e ^ {- t} , \Gamma_ {t}\right) ^ {2}}
{G \left(y , m e ^ {- t} , \Gamma_ {t}\right) + G \left(y , - m e ^ {- t} , \Gamma_ {t}\right)}.
$$

这条式子的逻辑其实很线性。两类数据的中心在 $\pm \mathbf m$。到时间 $t$ 后，类中心收缩成 $\pm \mathbf m e^{-t}$，类内宽度变成 $\Gamma_t$。对于分类这件事，真正重要的不是整个高维向量，而只是它沿分离方向 $\mathbf m$ 的投影，所以高维问题可以压缩成一个一维变量 $y$。

然后，$G(y,\pm m e^{-t},\Gamma_t)$ 分别表示“若当前点来自正类或负类，在时间 $t$ 观察到投影值 $y$ 的概率密度”。对给定 $y$，就能用 Bayes 公式写出它属于正类和负类的后验概率 $p_+(y)$、$p_-(y)$。而两个 clone 在固定 $y$ 的条件下最终落到同一类的概率，正是

$$
p_+(y)^2+p_-(y)^2.
$$

最后再对所有可能出现的 $y$ 做平均，就得到 `Eq. (6)`。因此，这个公式的物理意义并不神秘：它只是在测量“当前时刻的类别命运到底有多确定”。一旦 $y$ 已经明确指向某一类，它就接近 1；若 $y$ 还完全模糊，它就只剩 $1/2$。

## 5. The Dynamical Mechanism Behind Speciation

![Equation 7](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-03-equation-02.jpg)

![Equation 8](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-03-equation-03.jpg)

cloning 只是统计诊断。作者还进一步给出了 speciation 的动力学机制。他们不再直接追踪整个高维向量 $\mathbf x(t)$，而是只看与类中心的 overlap

$$
\mathbf m\cdot \mathbf x(t).
$$

这个量为什么重要很好理解：它的符号告诉你更偏向哪一类，大小告诉你偏向有多强。这里尺度必须讲清楚。文中设

$$
|\mathbf m|^2=d\tilde\mu^2,
$$

所以 $|\mathbf m|\sim O(\sqrt d)$。在 regime I，$\mathbf x(t)$ 基本还是一团近似各向同性的噪声云，对 $\mathbf m$ 没有系统性偏向，因此 $\mathbf m\cdot \mathbf x(t)$ 只是“噪声在固定方向上的投影”，典型大小自然是

$$
O(\sqrt d).
$$

到了 regime II，轨迹已经 committed to one class，于是可以粗略写成

$$
\mathbf x(t)\approx \pm c(t)\mathbf m+\text{noise},
$$

从而

$$
\mathbf m\cdot \mathbf x(t)\approx \pm c(t)|\mathbf m|^2+\mathbf m\cdot\text{noise}.
$$

第一项是 $O(d)$，第二项仍只是 $O(\sqrt d)$，所以一旦 class-level alignment 形成，overlap 的主导来源就从“噪声投影”变成了“真实类对齐项”，尺度也就从 $O(\sqrt d)$ 跳到

$$
O(d).
$$

正因为 regime I 里的 overlap 只有 $O(\sqrt d)$，作者才定义

$$
q(t)=\frac{\mathbf m\cdot\mathbf x(t)}{\sqrt d},
$$

把早期类方向上的微弱偏向提取成一个 $O(1)$ 的有效变量。接着他们证明，$q(t)$ 满足一个闭合的 Langevin 动力学：

$$
-dq = - \frac{\partial V(q,t)}{\partial q}\,dt + d\eta(t),
$$

其中有效势能是

$$
V(q,t)=\frac{1}{2}q^2-2\tilde\mu^2\log\cosh\!\bigl(q e^{-t}\sqrt d\bigr).
$$

这一步把高维 backward diffusion 压缩成了一个标准统计物理问题：一个粒子在时间依赖势能里运动。当 $t\gg t_S$ 时，势能近似是单阱，以 $q=0$ 为最低点，对应类别尚未破裂的 regime I；当 $t\ll t_S$ 时，势能裂成高势垒双阱，分别对应正类和负类。一条轨迹一旦滑进某个阱，就很难再翻到另一个阱，这就是 class-level symmetry breaking 的动力学实现。

最后，作者说 regime II 对应 $q\to\infty$，这不是说系统真的发散，而是说用于早期弱偏向的归一化已经不再合适。因为此时 $\mathbf m\cdot\mathbf x(t)\sim O(d)$，更自然的量已经变成

$$
\frac{\mathbf m\cdot\mathbf x(t)}{d},
$$

它在 regime II 才会保持有限。也正是在这一阶段，动力学等价于“对选定类的单个 Gaussian component 做 backward generation”，所以 regime II 仍然是 generalization，不是 memorization。

## 6. Collapse: When Generalization Turns Into Memorization

![Equation 5](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-02-equation-01.jpg)

如果说 `Eq. (4)` 解决的是“什么时候开始按类分化”，那么 `Eq. (5)` 解决的就是更细的一层问题：轨迹什么时候不再只是属于某一类，而是开始被某一个具体训练样本吸住。作者把这个从 regime II 到 regime III 的切换叫做 `collapse`，并定义 collapse time 为

$$
s(t_C)=s_{\mathrm{sep}}(t_C),
$$

其中

$$
s(t)=-\frac{1}{d}\int dx\,P_t(x)\log P_t(x)
$$

是 noised population distribution 的每维 Shannon entropy，而

$$
s_{\mathrm{sep}}(t)=\frac{\log n}{d}+\frac{1}{2}+\frac{1}{2}\log(2\pi\Delta_t)
$$

则是假设分布已经变成 $n$ 个彼此分离的 Gaussian lumps 时的每维熵。

这里讲的不是 entropy production，而是 Shannon entropy，也就是分布在高维空间里占据的有效体积。`Eq. (5)` 的物理意义也因此很清楚：它是在比较两种几何图像。一种是当前真实 noised distribution 占据了多大体积；另一种是“如果模型已经 collapse 成围绕训练样本的团块”时会占据多大体积。当这两个体积相等，作者就说 collapse 到来了。

作者进一步定义

$$
f(t)=s_{\mathrm{sep}}(t)-s(t),
$$

把它叫做 `excess entropy density`。在大时间极限，$P_t(x)$ 基本是一个单独 Gaussian，于是

$$
f(t)=\frac{\log n}{d}>0.
$$

这表示真实分布比“训练样本团块图像”更铺开。随着 backward process 往数据端推进，$f(t)$ 会下降，并在 $t_C$ 处穿过零点。于是：

- $f(t)>0$ 表示仍由 class-level generalization 支配
- $f(t)=0$ 是 collapse 临界点
- $f(t)<0$ 表示 sample-level memorization 开始接管

![Fig. 3 collapse in Gaussian mixtures](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-04-figure-01.jpg)

![Fig. 5 collapse in realistic datasets](../../pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto/images/page-06-figure-01.jpg)

`Figure 3` 和 `Figure 5` 分别在 Gaussian mixture 与真实数据集上展示了这一点。经验版本

$$
f^e(t)=s_{\mathrm{sep}}(t)-s^e(t)
$$

在 $t\ge t_C$ 时近似跟随理论上的 $f(t)$；而在 $t<t_C$ 时，经验分布本身已经贴住训练样本团块图像，于是 $f^e(t)$ 会压到接近零。这正是 memorization 的可观测信号。

这一点也解释了为什么作者说 `Eq. (5)` 的判据并不只属于 exact empirical score 的理想极限。真正起作用的不是某个特别精细的推导技巧，而是一个更稳的几何比较：当前生成分布占据多大体积，与训练样本团块图像占据多大体积。只要你能在实践里估计经验分布的 entropy，这个判据就能用来判断是否发生了 collapse。

## 7. The Local Competition Behind Collapse

这一小节是 collapse analysis 真正最有方法味道的地方。作者不再只盯着全局熵，而是问一个更局部的问题：如果点 $x$ 是从训练样本 $a_1$ 经 forward noising 得到的，那么经验分布的 score 在这个 $x$ 附近，到底会不会把反向轨迹拉回 $a_1$。

他们把这个点写成

$$
x=a_1 e^{-t}+z\sqrt{\Delta_t},
$$

其中 $z$ 的各分量都是独立标准高斯。然后把经验 noised distribution 拆成两部分：

$$
P_t^e(x)\propto Z_1+Z_{2\ldots n}.
$$

如果把归一化也显式写出来，它对应的就是文中的 `Eq. (9)`：

$$
P_t^e(x)=\frac{Z_1+Z_{2\ldots n}}{(2\pi\Delta_t)^{d/2}},
$$

其中

$$
Z_1=\exp\!\left[-\frac{(x-a_1 e^{-t})^2}{2\Delta_t}\right],
$$

而

$$
Z_{2\ldots n}
=
\sum_{\mu=2}^n
\exp\!\left[
-\frac{(x-a_\mu e^{-t})^2}{2\Delta_t}
\right].
$$

这里，$Z_1$ 是样本 $a_1$ 自己对 $x$ 的贡献，$Z_{2\ldots n}$ 是其余 $n-1$ 个样本的总贡献。由于 $x$ 本来就是从 $a_1$ 加噪得到的，所以

$$
Z_1=\exp\!\left[-\frac{(x-a_1 e^{-t})^2}{2\Delta_t}\right]
=
\exp\!\left(-\frac{z^2}{2}\right)
\simeq e^{-d/2}.
$$

`self-term` 的指数尺度是清楚的。真正难的是

$$
Z_{2\ldots n}
=
\sum_{\mu=2}^n
\exp\!\left[
-\frac{(x-a_\mu e^{-t})^2}{2\Delta_t}
\right].
$$

它虽然是很多独立项的和，但不能用普通中心极限定理，因为每一项都是“指数作用在一个会随维度增长的大随机量上”。这意味着总和往往不是由平均项主导，而是由极少数异常大的项主导。这正是玻璃模型和 random energy model 式的统计结构。

于是，collapse 被重新写成一个非常干净的局部竞争问题：

- 如果 $Z_1\gg Z_{2\ldots n}$，那么 score 主要由单个训练样本 $a_1$ 主导，backward trajectory 会被拉回它，出现 memorization
- 如果 $Z_{2\ldots n}\gg Z_1$，那么 score 主要由其余样本共同形成的背景主导，系统仍处在 generalization 图像里

这一步把全局的 entropy criterion 和局部的 score competition 接起来了。换句话说，`Eq. (5)` 给出的是 collapse 的体积判据，而 $Z_1$ 与 $Z_{2\ldots n}$ 的比较告诉你这个体积判据在局部 score 场上究竟是怎样实现的。

作者接着把这一局部竞争重新解释成一个统计物理模型。对固定的 $x$ 来说，$Z_{2\ldots n}$ 可以被看成一个具有 $n-1$ 个独立随机能级的配分函数。每个训练样本 $a_\mu$ 都对应一个有效能量，它在忽略归一化常数后的结构是

$$
E_\mu \propto
\frac{\big[(a_1-a_\mu)e^{-t}+z\sqrt{\Delta_t}\big]^2}{\Delta_t},
$$

从而

$$
Z_{2\ldots n}=\sum_{\mu=2}^n e^{-E_\mu}.
$$

这正是一个 `Random Energy Model` 式的结构。这里的随机性来自训练样本本身，于是背景项 $Z_{2\ldots n}$ 不再只是“很多样本的和”，而是玻璃理论里那种“很多随机能级的 Boltzmann 权重之和”。因此，后面真正需要问的不是普通平均值，而是：这个配分函数到底由很多普通能级共同主导，还是由极少数最低能级主导。

作者说明，在大 $d$、大 $n$ 极限下，

$$
\frac1d\log Z_{2\ldots n}
$$

会集中到一个确定值

$$
\psi_+(t),
$$

而它是时间 $t$ 和

$$
\alpha=\frac{\log n}{d}
$$

的增函数。这里阈值为什么正好是 $-1/2$，现在也能看清了：因为前面已经知道

$$
\frac1d\log Z_1 \to -\frac12.
$$

所以比较 $Z_{2\ldots n}$ 和 $Z_1$，就等价于比较 $\psi_+(t)$ 和 $-1/2$。

这一步直接给出两个 phase。若

$$
\psi_+(t)<-\frac12,
$$

那么背景项比自项指数级更小，经验分布 $P_t^e(x)$ 被 $Z_1$ 主导。于是 backward score 会把 $x$ 短时间内拉回 $a_1$，从

$$
x=a_1 e^{-t}+z\sqrt{\Delta_t}
$$

出发的轨迹最终会以概率 1 collapse 到训练样本 $a_1$。这就是 regime III。在 REM 语言里，这对应 `glass phase`：配分函数被极少数最低能态主导；在 diffusion 语言里，这正对应 memorization。

反过来，若

$$
\psi_+(t)>-\frac12,
$$

则 $P_t^e(x)$ 被 $Z_{2\ldots n}$ 主导，单一样本 $a_1$ 不再支配局部 score。此时经验分布在典型点上与 population distribution 一致到主导阶，因此系统仍然处在“没有 collapse”的相里。若类别已经形成，这就是 regime II 的 generalization；若类别尚未形成，则对应 regime I 的 Brownian / pure-noise 行为。在 REM 语言里，这对应 `liquid` 或 `high-temperature phase`。

作者还给出 collapse time 的显式表达式：

$$
t_C=
\frac12\log\!\left(
1+\frac{\sigma^2}{n^{2/d}-1}
\right).
$$

这条式子把前面的玻璃图像、局部 score 竞争和全局 entropy criterion 连成了一条线。它直接说明：只有当样本数随维度指数增长时，$t_C$ 才能保持在 $O(1)$ 并被显著推迟。换句话说，若想把 regime III 压缩到很短，必须有

$$
\frac{\log n}{d}\gg 1.
$$

这就是这篇文章给出的 curse of dimensionality。它也和前面的 entropy-based collapse criterion 一致：同一个 $t_C$ 既可以从体积匹配的熵论证读出来，也可以从 REM 的玻璃转变读出来。

## 8. Why High Dimension Pushes The Model Toward Collapse

collapse 最终由

$$
\alpha=\frac{\log n}{d}
$$

这个参数控制。它的重要性并不是拍脑袋定义出来的，而是因为大时间极限下

$$
f(t)=\frac{\log n}{d}=\alpha.
$$

如果 $\alpha$ 很小，说明样本数相对维度太少，那么 excess entropy density 一开始就不高，很快就会在 backward 过程中穿过零点，于是 collapse 几乎一开始就发生。若想把 collapse 推迟到 $t_C\sim O(1)$，就必须让

$$
\alpha\sim O(1),
$$

也就是要求

$$
\log n\sim d
\qquad\Longleftrightarrow\qquad
n\sim e^{c d}.
$$

这就是这篇文章说的 curse of dimensionality：如果你想在高维里避免 diffusion model 过早走向 memorization，样本数必须随维度指数增长。实践里之所以没那么糟，是因为真实模型不会学到 exact empirical score，而是学到一个更平滑、更正则化的近似 score。这里的 `regularization` 不是狭义的单一惩罚项，而是任何能阻止模型把训练集样本级结构学得过于尖锐、从而延缓 collapse 的机制。

## 9. What To Retain

这篇最该带走的，不是“diffusion 最终会 memorize”这一个结论，而是一种新的看法：生成过程本身可以被当成高维随机动力学系统来做统计物理分析。沿这条线，speciation 对应 symmetry breaking，collapse 对应 glass-like condensation，而谱结构和熵结构分别控制两次转变的时间尺度。

如果把这篇和你最近读的随机热力学文章放在一起，它们的共通主线不是“都提到了熵”，而是：它们都在研究轨迹集合如何随着动力学逐步失去自由度、逐步从更宽的分布收缩到更受约束的结构。只是在这篇 diffusion 文章里，这种收缩不再首先表现为 entropy production，而是表现为从 class-level generalization 走向 sample-level memorization。
