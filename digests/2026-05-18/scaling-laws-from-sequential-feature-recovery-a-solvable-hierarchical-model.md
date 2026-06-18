---
title: "Scaling Laws from Sequential Feature Recovery: A Solvable Hierarchical Model"
authors: "Arie Wortsman-Zurich, Hugo Tabanelli, Yatin Dandi, Florent Krzakala, Bruno Loureiro"
date_read: "2026-05-18"
topics: ["scaling laws", "feature learning", "hierarchical models", "spectral methods", "random matrix theory", "deep learning theory"]
source: "arXiv:2605.14567"
source_mineru: "../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.md"
equation_map: "./scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model-equation-map.md"
---

# Scaling Laws from Sequential Feature Recovery

## 精读笔记

---

## 公式编号说明

这篇笔记保留原文主文公式编号。原文 Eq. (2.1)-Eq. (2.15) 建立层级 teacher model、spectral algorithm 和 MSE scaling heuristic；Eq. (3.1)-Eq. (3.4) 给出 feature-wise recovery theorem 和 final generalization rate。Appendix 中最重要的是 Algorithm 1、Appendix C 的 resolvent perturbation proof skeleton，以及 Appendix D 的 MSE rate derivation。

覆盖索引见：[scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model-equation-map.md](./scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model-equation-map.md)。

---

## 一、Introduction：这篇文章想解释什么 scaling law

这篇文章的起点不是经验上拟合一条 power law，而是追问一个更机制化的问题：

$$
\text{features are learned one by one}
\quad\Longrightarrow\quad
\text{test error decays as a smooth power law}.
$$

也就是说，作者想解释的是：为什么神经网络的整体 learning curve 看起来很平滑，但内部 representation learning 可能是离散的、分阶段的、带 threshold 的。

Introduction 先把问题放进三条已有文献线里。

第一条线是 neural scaling laws。大模型的 loss 常随 data、compute 或 parameter count 呈 power-law decay。但很多理论解释来自 kernel、random feature 或 linearized models。在这些模型里，representation 事先固定，learning curve 主要由固定 feature spectrum 决定。这个视角能解释一些 scaling，但没有解释“网络自己发现 feature”的过程。

第二条线是 feature learning dynamics。很多训练过程并不是平滑吸收所有信息，而是出现 plateau、abrupt risk drop、feature emergence 或 concept emergence。也就是说，模型可能先学到强 feature，再学到弱 feature；整体误差下降可能是多个 sharp transition 的叠加。

第三条线是 depth 和 compositional task。深度网络的优势往往来自中间 representation：复杂 target 在输入空间里看起来是高阶、困难的函数，但如果先恢复某些 latent features，后面的任务会变成低维、简单的任务。

本文把这三条线合到一个可解模型里。作者构造一个层级 target：

$$
\text{input}
\rightarrow
\text{degree-}q\text{ latent features}
\rightarrow
\text{power-law weighted scalar feature}
\rightarrow
\text{output}.
$$

关键设置是：latent feature 的权重不是均匀的，而是按 power law 衰减。强 feature 的 spike 更大，所以少量样本就能被 spectral method 检出；弱 feature 的 spike 更小，需要更多样本。于是样本量 $n$ 增加时，模型不是一次性学完整个 representation，而是按 feature strength 依次跨过 recovery threshold。

这就是全文的核心机制：

$$
\begin{aligned}
&\text{power-law feature strengths}\\
&\Rightarrow \text{feature-wise spectral thresholds}\\
&\Rightarrow \text{sequential recovery}\\
&\Rightarrow \text{unrecovered spectral tail controls error}\\
&\Rightarrow \text{smooth scaling law}.
\end{aligned}
$$

---

## 二、Figure 1：全文逻辑的图形压缩

![Figure 1 left](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-02-figure-01.jpg)

![Figure 1 right](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-02-figure-02.jpg)

Figure 1 左侧说明 teacher function 的层级结构。输入 $\boldsymbol{x}\in\mathbb{R}^d$ 先被送进 degree-$q$ Hermite feature space，再投影到若干 latent directions，得到第一层 hidden features $h^{(1)}$。这些 hidden features 再经过二次非线性 $\mathrm{He}_2$，并按 power-law weights $\lambda_i$ 组合成一个 scalar latent feature $h^{(2)}$。最后输出 $y=g(h^{(2)})$。

这张图要表达的是：从原始输入 $\boldsymbol{x}$ 看，target 是高阶函数；但从 latent representation 看，它是“先恢复方向，再做低维读出”的层级任务。

Figure 1 右侧说明 proof idea。spectral estimator 的矩阵谱由两部分组成。

第一部分是 noise bulk。它来自有限样本下的 empirical fluctuation，近似像一个 high-dimensional random matrix bulk。

第二部分是 signal spikes。每个 spike 对应一个 latent direction $A_i^{(1)}$，spike 强度由 $\lambda_i$ 控制。由于 $\lambda_i$ 按 $i^{-\gamma}$ 衰减，前几个 spike 更强，后面的 spike 更弱。

随着 sample size $n$ 增加，noise bulk 的尺度下降。强 spike 先从 bulk 中分离出来，弱 spike 后分离出来。某个样本量下已经被分离的 spike 数记作 $m_n$；还没分离的方向 $i>m_n$ 贡献剩余 MSE。这就是“sequential feature recovery”的视觉版本。

---

## 三、Section 2：层级 teacher model 如何定义

### 3.1 监督学习问题

原文先从普通 supervised learning 写起：

$$
\forall \mu \in [n],
\quad
y_{\mu}=f_{\star}(x_{\mu}).
\tag{2.1}
$$

这里 $\mu$ 是样本编号，$x_\mu\sim\mathcal{N}(0,I_d)$ 是 $d$ 维 Gaussian input，$y_\mu$ 是由 teacher function $f_\star$ 生成的 label。

如果只看 Eq. (2.1)，这就是一个普通 regression problem。真正的结构在下一步：作者不把 $f_\star$ 当成 generic high-dimensional function，而是假设它有层级组合结构。

### 3.2 Eq. (2.2)：从 input 到 latent features 再到 output

原文把 target 的 compositional structure 写成：

$$
x_{\mu}\in\mathbb{R}^{d}
\longrightarrow
h_{\mu}^{(1)}\in\mathbb{R}^{d^{\varepsilon}}
\longrightarrow
h_{\mu}^{(2)}\in\mathbb{R}
\longrightarrow
y_{\mu}=g(h_{\mu}^{(2)}).
\tag{2.2}
$$

这条链条里有三个层次。

第一，$x_\mu$ 是原始输入，维度是 $d$。

第二，$h_\mu^{(1)}$ 是第一层 latent representation，维度是 $d_1=\lfloor d^\varepsilon\rfloor$。这里 $\varepsilon>0$ 控制 hidden directions 的数量随输入维度增长的速度。

第三，$h_\mu^{(2)}$ 是 scalar latent feature。它把 $d_1$ 个第一层 features 合成一个标量。

第四，$g$ 是最后的一维 readout，把 scalar latent feature 变成输出 $y_\mu$。

Eq. (2.2) 的作用是把问题从“在 $\mathbb{R}^d$ 上学一个复杂函数”改写成“先找 latent directions，再学一个低维 readout”。后面的 spectral algorithm 就是围绕这个层级结构设计的。

### 3.3 Eq. (2.3)：第一层 features 是 degree-$q$ Hermite space 中的投影

作者先把 input 提升到 degree-$q$ Hermite feature space。定义：

$$
F_\mu
=
\mathcal{F}(\mathrm{He}_q(x_\mu))
\in\mathbb{R}^{D},
\qquad
D:=B(d,q)=\binom{d+q-1}{q}.
$$

这里 $\mathrm{He}_q(x_\mu)$ 是 degree-$q$ Hermite tensor，$\mathcal{F}$ 表示 flattening，$D$ 是这个对称张量空间 flatten 后的维度。量级上 $D=\Theta_d(d^q)$。

teacher 有 $d_1$ 个第一层方向：

$$
A_i^{(1)}\in\mathbb{R}^{D},
\qquad
i\in[d_1],
$$

每个方向是 Gaussian weight vector，entries 的 variance 约为 $1/d^q$。第一层 feature 是 Hermite feature $F_\mu$ 在这些方向上的投影：

$$
\forall(\mu,i)\in[n]\times[d_1],
\quad
h_{\mu,i}^{(1)}
=
\left\langle A_i^{(1)},F_\mu\right\rangle.
\tag{2.3}
$$

这一步的意义是：hidden direction 不是原始 input space 中的线性方向，而是 degree-$q$ polynomial feature space 中的方向。因此，从原始输入看，第一层已经在学习高阶 feature。

### 3.4 Eq. (2.4)：第二层用 power-law weights 组合第一层 features

第二层先给每个 latent direction 一个权重：

$$
\lambda_i=Z_\gamma z_i i^{-\gamma},
\qquad
z_i\sim\mathrm{Rad}(1/2).
$$

这里 $\gamma\geq0$ 是 power-law exponent，控制 feature strength 衰减速度；$z_i$ 是随机符号；$Z_\gamma$ 是 normalization factor，用来让输出方差保持 $\Theta_d(1)$。原文给出：

$$
Z_\gamma
=
\left(\sum_{i=1}^{d_1}i^{-2\gamma}\right)^{-1/2}.
$$

然后第二层写成：

$$
h_{\mu}^{(2)}
=
\left\langle A^{(2)},\mathrm{He}_2(h_\mu^{(1)})\right\rangle
=
\frac{1}{\sqrt{2}}
\sum_{i=1}^{d_1}
\lambda_i
\left((h_{\mu,i}^{(1)})^2-1\right).
\tag{2.4}
$$

这一步有两个关键点。

第一，$\mathrm{He}_2(u)$ 本质上是 centered quadratic feature，形式是 $u^2-1$。因此第二层不是线性组合 $h_{\mu,i}^{(1)}$，而是组合第一层 feature 的二次结构。

第二，$\lambda_i$ 按 $i^{-\gamma}$ 衰减。强 feature 和弱 feature 同时存在，但强度不同。这个 anisotropic power-law spectrum 是本文 scaling law 的来源。如果 $\lambda_i$ 都差不多，很多 directions 会在相似样本量下一起出现；如果 $\lambda_i$ 服从 power law，就会出现从强到弱的 sequential recovery。

### 3.5 Eq. (2.5)：输出 readout

最后输出为：

$$
\forall\mu\in[n],
\quad
y_\mu=g(h_\mu^{(2)}).
\tag{2.5}
$$

作者要求 $g$ centered，并且 information exponent $\mathrm{IE}(g)=1$。在这里最重要的是：

$$
\mathbb{E}[g(z)]=0,
\qquad
\mathbb{E}[g'(z)]\neq0,
\qquad
z\sim\mathcal{N}(0,1).
$$

直观上，$\mathbb{E}[g'(z)]\neq0$ 表示 $g$ 的一阶 Hermite coefficient 不为零。后面 spectral estimator 要从 $y_\mu$ 和 Hermite moment 的相关性中提取 signal；如果一阶信息完全消失，主导 signal 会换到更高阶，本文证明就不再是当前这个 regime。

---

## 四、为什么 shallow kernel 需要更大样本量

这个层级 target 有一个重要统计后果。

第一层 features 是 degree-$q$ Hermite features：

$$
x
\mapsto
F=\mathcal{F}(\mathrm{He}_q(x)).
$$

第二层又对 $h^{(1)}$ 做二次变换，所以从原始 input $x$ 看，leading informative component 是 degree-$2q$ 的函数。

如果一个 shallow orthogonally invariant kernel 不利用层级结构，它看到的是一个 degree-$2q$ 的高阶 target。原文指出这类 shallow method 需要的样本量尺度是：

$$
n=\omega_d(d^{2q}).
$$

但如果 learner 先恢复 degree-$q$ latent representation，那么第一步只需要在 $D=\Theta_d(d^q)$ 的 Hermite feature space 里做 spectral recovery。恢复后，第二层和 readout 都发生在低维 $d_1$ 或一维空间里。因此 depth-adapted / hierarchy-adapted 方法可以把关键样本尺度从 $d^{2q}$ 降到 $d^q$ 级别，再叠加 feature strength 的 power-law threshold。

这就是文章里“depth advantage”的具体含义：不是说深度网络魔法般更强，而是说它能利用中间 representation，把一个全局高阶任务拆成两个较低层次的任务。

---

## 五、Section 2.1：spectral algorithm 的第一层 recovery

### 5.1 Eq. (2.6)：构造 moment matrix

作者定义 spectral estimator：

$$
\widehat{C}
=
\frac{1}{n}
\sum_{\mu=1}^{n}
y_\mu
\mathrm{He}_2(F_\mu)
\in\mathbb{R}^{D\times D}.
\tag{2.6}
$$

更直观地说，$\widehat C$ 是一个 label-weighted second moment matrix。因为 $\mathrm{He}_2(F_\mu)$ 可以理解成 centered quadratic moment，所以 $\widehat C$ 衡量的是：

$$
\text{which quadratic directions in Hermite feature space correlate with }y.
$$

如果某个 hidden direction $A_i^{(1)}$ 真的影响 label，那么沿这个方向的 second moment 会和 $y_\mu$ 相关。于是 $\widehat C$ 的 top eigenvectors 就有可能恢复 teacher directions $A_i^{(1)}$。

### 5.2 Eq. (2.7)：signal + noise decomposition

为了说明为什么 $\widehat C$ 能恢复 hidden directions，原文先把它拆成：

$$
\widehat{C}
=
\mathbb{E}[\widehat{C}]
+
(\widehat{C}-\mathbb{E}[\widehat{C}])
=
\text{signal}+\text{noise}.
\tag{2.7}
$$

这一步是整篇文章的 random matrix 入口。

signal 是 population moment。它告诉我们无限样本时 $\widehat C$ 的 eigenspace 是否对准 teacher directions。

noise 是 finite-sample fluctuation。它告诉我们样本量有限时，signal spike 能否从 noise bulk 中露出来。

### 5.3 Eq. (2.8)：population signal 支持在 teacher subspace 上

作者用 Gaussian equivalence heuristic 解释 $\mathbb{E}[\widehat C]$ 的结构。degree-$q$ Hermite features $F_\mu$ 在高维下近似像一个 $D$ 维 Gaussian vector $\tilde{x}_\mu$。label $y_\mu$ 只依赖于 $\tilde{x}_\mu$ 在 $A^{(1)}$ row space 上的投影；与这个 subspace 正交的部分和 label 独立。

于是 $\widehat C$ 近似分解为：

$$
\widehat{C}
\simeq
\underbrace{
\nu_1 A^{(1)\top}A^{(2)}A^{(1)}
}_{\text{signal } \mathbb{E}[\widehat C]}
+
\underbrace{
\frac{1}{n}\tilde{X}_{\perp}Y\tilde{X}_{\perp}^{\top}
+o_d(1)
}_{\text{noise } \widehat C-\mathbb{E}[\widehat C]}.
\tag{2.8}
$$

这里 $\nu_1=\mathbb{E}[g'(z)]$ 是 $g$ 的 first Hermite coefficient；$\tilde X_\perp$ 收集与 teacher subspace 正交的 feature components；$Y$ 是 label 权重。

Eq. (2.8) 的含义是：signal term 是一个 rank-$d_1$ matrix，支撑在 $A^{(1)}$ 所张成的 latent subspace 上；noise term 像一个在高维正交空间中的 random covariance bulk。

所以 top eigenvectors 的任务可以被读成 spike detection：

$$
\text{recover } A_i^{(1)}
\quad\Longleftrightarrow\quad
\text{the corresponding spike separates from the noise bulk}.
$$

### 5.4 Eq. (2.9)：noise bulk 的尺度

因为 noise term 生活在维度 $\sim d^q$ 的空间里，并且由 $n$ 个样本平均，作者给出 heuristic：

$$
\widehat{C}
\simeq
\mathbb{E}[\widehat C]
+
\sqrt{\frac{d^q}{n}}W,
\qquad
W\sim\mathrm{GOE}\text{-like}.
\tag{2.9}
$$

这一步的核心是 noise operator norm 的尺度：

$$
\|\text{noise}\|_{\mathrm{op}}
\sim
\sqrt{\frac{d^q}{n}}.
$$

样本量越大，noise bulk 越小；feature strength 越大，signal spike 越容易冒出 bulk。

### 5.5 Eq. (2.10)：第 $i$ 个 feature 的 recovery threshold

第 $i$ 个 population spike 的强度是：

$$
|\lambda_i|=Z_\gamma i^{-\gamma}.
$$

noise bulk 的尺度是：

$$
\sqrt{\frac{d^q}{n}}.
$$

第 $i$ 个 feature 开始可恢复的条件是 signal 大于 noise：

$$
Z_\gamma i^{-\gamma}
\gtrsim
\sqrt{\frac{d^q}{n}}.
$$

两边平方：

$$
Z_\gamma^2 i^{-2\gamma}
\gtrsim
\frac{d^q}{n}.
$$

移项得到：

$$
n
\gtrsim
\frac{d^q i^{2\gamma}}{Z_\gamma^2}.
\tag{2.10}
$$

这就是全文最重要的 threshold 公式。它说明：feature index $i$ 越大，权重越小，需要的样本量越大；$\gamma$ 越大，强弱 feature 差距越大，sequential recovery 越明显。

---

## 六、Weak recovery 和 learned first-layer representation

作者接着定义 weak recovery。一个 estimator $u_N$ weakly recovers teacher vector $v_N$，意思是二者内积在高维极限下不会趋于零：

$$
\liminf_{N\to\infty}
\mathbb{P}
\left(
|\langle u_N,v_N\rangle|\geq c
\right)
=1
$$

for some constant $c>0$。

这里 weak recovery 不是要求 perfect alignment，而是要求 estimator 至少捕捉到 teacher direction 的非平凡方向信息。这个定义适合 spectral phase transition：threshold 以下 overlap 近似消失；threshold 以上 overlap 开始保持正值，并进一步随 $n$ 改善。

给定 recovered eigenvectors 后，作者定义 learned first-layer features：

$$
\widehat h_{\mu,i}^{(1)}
=
\left\langle
\widehat A_i^{(1)},F_\mu
\right\rangle,
\qquad
(\mu,i)\in[n]\times[d_1].
\tag{2.11}
$$

这一步把 spectral recovery 转回 representation learning：如果 $\widehat A_i^{(1)}$ 对准 $A_i^{(1)}$，那么 $\widehat h_{\mu,i}^{(1)}$ 就是对应 true hidden feature 的估计。

---

## 七、Section 2.2：第二层和 readout 为什么不是高维瓶颈

一旦 $\widehat h^{(1)}$ 被估计出来，后面的计算都发生在低维 latent space $\mathbb{R}^{d_1}$。

第二层 estimator 是：

$$
\widehat A^{(2)}
=
\frac{1}{n}
\sum_{\mu=1}^{n}
y_\mu
\mathrm{He}_2(\widehat h_\mu^{(1)})
\in\mathbb{R}^{d_1\times d_1}.
\tag{2.12}
$$

这和 Eq. (2.6) 形式相似，但维度完全不同。Eq. (2.6) 在 $D\times D$ 的 degree-$q$ Hermite feature space 里，$D=\Theta(d^q)$；Eq. (2.12) 在 $d_1\times d_1$ 的 learned latent space 里，$d_1=d^\varepsilon$，通常远小于 $D$。

因此，高维 spectral transition 主要发生在第一层 recovery。第二层只是利用已经恢复的低维 representation 估计 diagonal power-law combination。

然后 learned second latent feature 是：

$$
\widehat h_\mu^{(2)}
=
\left\langle
\widehat A^{(2)},
\mathrm{He}_2(\widehat h_\mu^{(1)})
\right\rangle.
\tag{2.13}
$$

最后用一维 ridge regression 学 readout：

$$
\widehat a
\in
\operatorname*{argmin}_{a\in\mathbb{R}^{p}}
\frac{1}{n}
\sum_{\mu=1}^{n}
\left(
y_\mu
-
\langle a,\phi(\widehat h_\mu^{(2)})\rangle
\right)^2
+
\rho\|a\|^2.
\tag{2.14}
$$

这里 $\phi:\mathbb{R}\to\mathbb{R}^p$ 是固定 feature map。因为输入是一维 scalar $\widehat h^{(2)}$，这个 readout step 的统计误差约为 $1/n$，在主 scaling regime 中不是主要瓶颈。

所以全文的误差逻辑可以压缩成：

$$
\text{MSE}
\approx
\text{error from unrecovered first-layer directions}
+
\text{subdominant readout error}.
$$

---

## 八、Eq. (2.15)：从 unrecovered tail 得到 power-law MSE

作者定义 generalization MSE：

$$
\mathrm{MSE}(n)
=
\mathbb{E}_{x\sim\mathcal{N}(0,I_d)}
\left[
(\widehat f(x)-f_\star(x))^2
\right].
$$

接下来用 threshold heuristic 推导 scaling law。

令：

$$
a_i=|\lambda_i|\propto i^{-\gamma}.
$$

第 $i$ 个方向的 recovery threshold 来自 Eq. (2.10)：

$$
n_i
\asymp
\frac{d^q}{a_i^2}.
$$

如果样本量是 $n$，已经恢复的 directions 数记为 $m(n)$。那么主要误差来自还没恢复的 directions：

$$
\mathrm{MSE}(n)
\simeq
\sum_{i>m(n)}a_i^2.
$$

因为 $a_i^2\propto i^{-2\gamma}$，对于 summable spectra，即 $2\gamma>1$，尾和满足：

$$
\sum_{i>m}i^{-2\gamma}
\asymp
m^{1-2\gamma}.
$$

另一方面，由 threshold 关系：

$$
n
\asymp
\frac{d^q m^{2\gamma}}{Z_\gamma^2}
\quad\Longrightarrow\quad
m(n)
\asymp
\left(\frac{Z_\gamma^2 n}{d^q}\right)^{1/(2\gamma)}.
$$

代入尾和：

$$
\mathrm{MSE}(n)
\asymp
\left(\frac{n}{d^q}\right)^{-1+1/(2\gamma)}.
\tag{2.15}
$$

Eq. (2.15) 的意义是：smooth power-law learning curve 可以来自一串 discrete feature transitions。每个单独 feature 的恢复是 sharp 的，但很多 feature 的 thresholds 按 power-law 排列，叠加后就表现为平滑的 scaling law。

---

## 九、Figure 2：整体 transition 的经验图

![Figure 2 left](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-04-figure-01.jpg)

![Figure 2 center](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-04-figure-02.jpg)

![Figure 2 right](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-04-figure-03.jpg)

Figure 2 用 $q=2,\varepsilon=0.5,\gamma=0.4,g^\star=\mathrm{id}$ 展示整体 transition。

左图是 test MSE 随 $\alpha=\log(n)/\log(d)$ 的变化。$\alpha$ 越大，表示 $n=d^\alpha$ 越大。小 $\alpha$ 时样本不足，MSE 高；跨过 spectral recovery scale 后，MSE 开始下降。

中图是 first-layer feature overlap $q_h^{(1)}$。它衡量 learned first-layer representation 和 true first-layer representation 的 subspace overlap。MSE 下降和 $q_h^{(1)}$ 上升发生在同一 sample scale，说明误差下降确实由 latent feature recovery 驱动。

右图是 $\widehat C$ 的 spectrum。蓝色 bulk 是 noise；红色 outliers 是 signal spikes。当样本量足够大时，top eigenvalues 从 bulk 中分离。这正是 Eq. (2.9)-Eq. (2.10) 的可视化证据。

---

## 十、Section 3：主定理如何把 heuristic 变成 threshold

### 10.1 Assumption 3.1：readout regime

主定理在两个 regime 下证明。

第一种是 identity readout：

$$
g(t)=t,
\qquad
\gamma>0.
$$

这种情况最干净，因为 output 直接等于 scalar second latent feature。

第二种是 delocalized nonlinear readout：

$$
0<\gamma<1/2,
\qquad
\mathbb{E}[g'(Z)]\neq0,
\qquad
Z\sim\mathcal{N}(0,1).
$$

这里 $0<\gamma<1/2$ 是 delocalized regime。原因是当 $\gamma<1/2$ 时，normalization $Z_\gamma$ 依赖 $d_1$，很多 feature 共同贡献输出；非线性项的控制需要更强的技术条件。

### 10.2 Theorem 3.1：第 $k$ 个 feature 的充分和必要样本量

Theorem 3.1 的第一部分给出 sufficient sample complexity：

$$
\left|
\left\langle
\frac{u_k}{\|u_k\|_2},
\frac{A_k^{(1)}}{\|A_k^{(1)}\|_2}
\right\rangle
\right|
=
1
-
O_d
\left(
\frac{d^q k^{2\gamma}}{nZ_\gamma^2}
\right).
\tag{3.1}
$$

这里 $u_k$ 是 $\widehat C$ 的第 $k$ 个 eigenvector，$A_k^{(1)}$ 是第 $k$ 个 teacher direction。等式右侧的误差项告诉我们：

$$
\text{overlap error}
\sim
\frac{d^q k^{2\gamma}}{nZ_\gamma^2}.
$$

因此只要：

$$
n
=
\omega_d
\left(
d^q k^{2\gamma}Z_\gamma^{-2}
\right),
$$

overlap error 就趋于 0，第 $k$ 个方向被恢复。这个结果把 Eq. (2.10) 的 heuristic threshold 变成 theorem。

Theorem 3.1 的第二部分给出 necessary sample complexity。如果：

$$
n
=
\Theta
\left(
d^q k^{2\gamma}Z_\gamma^{-2}d^{-\delta}
\right),
\qquad
\delta>0,
$$

那么以高概率，第 $k$ 个方向不能被 Algorithm 1 恢复。也就是说，threshold 不只是上界，也是基本必要尺度。

这点很重要。要推 scaling law，不能只证明“样本够多就能学到 feature”；还需要证明“样本不够时 feature 确实没学到”。否则 unrecovered tail 的说法没有 sharp 边界。

### 10.3 Eq. (3.2)：为什么不用 Davis-Kahan，而用 resolvent expansion

如果直接用 Davis-Kahan theorem，通常会得到形如：

$$
\text{subspace error}
\lesssim
\frac{\|\Delta\|_{\mathrm{op}}}{\text{spectral gap}}.
$$

问题是这里 spike strength 按 power law 变化，相邻 spikes 的 gap 会随 feature index 变小。Davis-Kahan 给的是 worst-case subspace bound，不够 sharp，不能逐个 direction 给出匹配上下界。

作者改用 resolvent-based perturbation expansion。原文给出：

$$
\widehat u_k
=
u_k
+
\sum_{j=1,j\neq k}^{d_1}
\frac{u_j^\top\Delta u_j}{\lambda_k-\lambda_j}u_j
+
\frac{1}{\lambda_k}
P_{\mathrm{Ker}}\Delta u_k
+
o(\|\Delta\|_{\mathrm{op}}^2).
\tag{3.2}
$$

这里 $\Delta=\widehat C-\mathbb{E}[\widehat C]$；$P_{\mathrm{Ker}}$ 是投影到 $\mathbb{E}[\widehat C]$ 的 kernel；$u_k$ 是 population eigenvector。

这条式子可以分成三项读。

第一项 $u_k$ 是想恢复的 true signal direction。

第二项是 signal subspace 内部的 mixing。它把 $u_k$ 混到其他 $u_j$ 上，分母 $\lambda_k-\lambda_j$ 表示 spike gap。这个项解释了为什么 gap 小会带来 perturbation。

第三项是 noise 投影到 signal subspace 之外的方向。它被 $1/\lambda_k$ 放大，所以弱 feature 的 $\lambda_k$ 小，更容易被 noise 污染。

Theorem 3.1 的证明就是证明：在 threshold 以上，第二项和第三项都小；在 threshold 以下，关键 noise 项不能忽略。

### 10.4 Corollary 3.1：样本量 $n$ 下恢复多少个方向

由 Eq. (2.10) 或 Theorem 3.1 可得：第 $i$ 个 direction 被恢复需要：

$$
n
\gtrsim
\frac{d^q i^{2\gamma}}{Z_\gamma^2}.
$$

给定样本量 $n$，把这个关系对 $i$ 反解：

$$
i^{2\gamma}
\lesssim
\frac{Z_\gamma^2 n}{d^q}.
$$

于是已恢复方向数 $m_n$ 的尺度是：

$$
m_n
=
\left(
\frac{Z_\gamma^2}{D}n
\right)^{1/(2\gamma)}.
\tag{3.3}
$$

原文这里写 $D$，而 $D=\Theta(d^q)$。因此 Eq. (3.3) 和前面的 heuristic 口径一致：

$$
m_n
\asymp
\left(
\frac{Z_\gamma^2 n}{d^q}
\right)^{1/(2\gamma)}.
$$

这一步把 feature-wise threshold 转成 aggregate recovery count。后面的 MSE rate 就靠 $m_n$ 和 unrecovered tail 相接。

---

## 十一、Figure 4：direction-wise recovery 不是事后解释，而是 theorem 的直接检验

![Figure 4 left](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-09-figure-01.jpg)

![Figure 4 center](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-09-figure-02.jpg)

![Figure 4 right](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-09-figure-03.jpg)

Figure 4 不再只看整体 MSE，而是直接追踪每个 teacher direction 是否被恢复。

左图画 direction-wise alignment：

$$
\cos^2(\theta_i)
=
\|\widehat U^\top u_i\|^2,
$$

其中 $u_i=A_i^{(1)}/\|A_i^{(1)}\|$，$\widehat U$ 是 recovered eigenspace 的 orthonormal basis。$\cos^2(\theta_i)\approx0$ 表示第 $i$ 个 direction 没进入 learned subspace；$\cos^2(\theta_i)\approx1$ 表示它已经被恢复。

左图的现象是：不同 $i$ 的曲线按顺序打开。小 $i$ 对应强 $\lambda_i$，先恢复；大 $i$ 对应弱 $\lambda_i$，后恢复。这直接验证 Eq. (2.10) 和 Theorem 3.1 的 sequential recovery picture。

中图画 recovery 后的 angular error：

$$
1-\cos(\theta_i).
$$

Theorem 3.1 预测它按：

$$
O_d
\left(
\frac{d^q i^{2\gamma}}{nZ_\gamma^2}
\right)
$$

衰减。在固定 $i,d$ 后，这就是 $1/n$ 级别的下降。图中 $1/n$ guide 对应这个 post-transition refinement。

右图把 empirical aggregate overlap 和 theoretical count $m_{\mathrm{th}}(\alpha)$ 比较。理论 count 是数一数哪些 directions 满足 predicted threshold $n_i\leq d^\alpha$。有限 $d$ 下 staircase 被平滑，但顺序和尺度吻合。

---

## 十二、Theorem 3.2：generalization error 的两种 regime

Theorem 3.2 说明 MSE rate 由 unrecovered tail 决定。原文给出：

$$
\mathrm{MSE}(n)
=
\begin{cases}
\Theta_d(1)
-
\left(
\frac{n}{d_1d^q}
\right)^{\frac{1}{2\gamma}-1},
&
\text{if }0<\gamma<\frac12,\ d^q\ll n\ll d^q d_1,
\\
n^{-1+\frac{1}{2\gamma}},
&
\text{if }\gamma>\frac12
\text{ under regime (i)},\ d^q\ll n.
\end{cases}
\tag{3.4}
$$

这个式子要分开读。

当 $0<\gamma<1/2$ 时，spectrum 不可求和，很多 weak directions 总体上仍然贡献大量能量。此时 normalization $Z_\gamma$ 随 $d_1$ 缩放。模型在 $d^q\ll n\ll d^q d_1$ 的窗口中逐渐恢复更多 directions，MSE 从 $\Theta_d(1)$ 开始被减去一个已恢复能量项：

$$
\left(
\frac{n}{d_1d^q}
\right)^{1/(2\gamma)-1}.
$$

这不是一个从 0 开始衰减的 tail，而是“总误差减去已学部分”。

当 $\gamma>1/2$ 时，spectrum 可求和，tail energy 有清晰 Pareto tail。恢复到 $m_n$ 后，剩下的尾部给出：

$$
\mathrm{MSE}(n)
\asymp
n^{-1+1/(2\gamma)}
$$

忽略 $d^q$ 常数尺度后就是 Eq. (2.15) 的 rate。这里 $\gamma$ 越大，feature strength 衰减越快，tail 更轻，恢复少数强 feature 后误差下降更快。

Remark 3.2 说明：$\gamma>1/2$ 的非线性 readout 情况尚未完全证明，虽然数值证据支持类似结论。这里不能把 theorem 读成“所有 nonlinear $g$ 都已严格覆盖”。

---

## 十三、Appendix D：MSE rate 是怎么从 threshold 推出来的

Appendix D 是主文 Eq. (3.4) 的实际推导。它的逻辑比主文略展开，值得单独记录。

### 13.1 Eq. (D.1)-Eq. (D.7)：readout error 不是主项

作者先把训练拆成两批数据。第一批 $\mathcal D$ 用来学 representation，第二批 $\mathcal D'$ 用来在 learned scalar feature 上做 KRR。对新样本：

$$
x_\mu'
\rightarrow
\widehat h_{\mathcal D}^{(2)}(x_\mu').
\tag{D.1}
$$

这里下标 $\mathcal D$ 是提醒：这个 feature map 是第一批数据学出来的，和第二批 KRR 样本独立。

KRR 的 generalization bound 给出：

$$
L(\widehat f)
-
\min_{f\in\mathcal H}L(f)
=
O(1/n).
\tag{D.4}
$$

如果 kernel 足够 universal，且 regularization 选得合适，那么最终 MSE 可以被控制为：

$$
\mathrm{MSE}(n)
\leq
\mathbb{E}
\left[
\left(
g(h_\mu^2)
-
g(\widehat h_\mu^2)
\right)^2
\right]
+
O(1/n).
\tag{D.7}
$$

这一步的意义是把问题从“最终 predictor 的误差”转成“second latent feature 有没有被估准”。而 $\widehat h^{(2)}$ 的误差又主要来自哪些 first-layer directions 没恢复。

### 13.2 Eq. (D.8)：linear 部分的误差就是未恢复方向的平方和

对 linear leading term，作者写：

$$
\mathrm{MSE}_{\mathrm{linear}}
=
\mathbb{E}
\left[
\left\|
\sum_{j\geq i^\star}
j^{-\gamma}
\left((h_j^{(1)})^2-1\right)
\right\|^2
\right],
\tag{D.8}
$$

这里 $i^\star$ 是已经学到的 directions 数。式子中的 $j\geq i^\star$ 表示还没恢复的 tail。由于各方向在高维下近似正交，平方误差主要就是这些未恢复系数的平方和。

### 13.3 Eq. (D.9)-Eq. (D.10)：threshold 反解得到 learned count

Theorem 3.1 说第 $i$ 个方向在：

$$
n
\asymp
\frac{d^q i^{2\gamma}}{Z_\gamma^2}
\tag{D.9}
$$

附近被学到。反解得：

$$
i^\star
=
\left(
\frac{Z_\gamma^2 n}{d^q}
\right)^{1/(2\gamma)}.
\tag{D.10}
$$

这就是 Corollary 3.1 的核心。

### 13.4 Eq. (D.11)：MSE 是 tail sum

把 Eq. (D.8) 中的正交性和 power-law weights 合起来：

$$
\mathrm{MSE}_{\mathrm{linear}}(n)
=
\Theta
\left(
Z_\gamma^2
\sum_{i\geq i^\star}
i^{-2\gamma}
\right).
\tag{D.11}
$$

此时问题变成纯粹的 tail-sum asymptotics。

### 13.5 Eq. (D.12)-Eq. (D.15)：$0<\gamma<1/2$ 的 delocalized regime

当 $\gamma<1/2$：

$$
\sum_{i=1}^{d_1}i^{-2\gamma}
\asymp
d_1^{1-2\gamma},
\qquad
Z_\gamma^2
\asymp
d_1^{-(1-2\gamma)}.
$$

因此：

$$
\begin{aligned}
Z_\gamma^2
\sum_{i\geq i^\star}
i^{-2\gamma}
&=
Z_\gamma^2
\left(
Z_\gamma^{-2}
-
\sum_{i\leq i^\star}i^{-2\gamma}
\right)
\tag{D.12}
\\
&=
1
-
\frac{1}{d_1^{1-2\gamma}}
(i^\star)^{1-2\gamma}
\tag{D.13}
\\
&=
1
-
\frac{1}{d_1^{1-2\gamma}}
\left(
\frac{Z_\gamma^2 n}{d^q}
\right)^{-1+1/(2\gamma)}
\tag{D.14}
\\
&=
1
-
\left(
\frac{n}{d_1d^q}
\right)^{-1+1/(2\gamma)}.
\tag{D.15}
\end{aligned}
$$

注意这里指数 $-1+1/(2\gamma)$ 是正的，因为 $\gamma<1/2$。所以随着 $n$ 增加，被减掉的 learned energy 增加，MSE 从常数量级下降。

### 13.6 Eq. (D.16)-Eq. (D.20)：$\gamma>1/2$ 的 summable regime

当 $\gamma>1/2$，tail sum 满足：

$$
\sum_{i\geq i^\star}i^{-2\gamma}
=
\Theta_d((i^\star)^{1-2\gamma}).
\tag{D.16}
$$

代入 $i^\star$：

$$
\begin{aligned}
\mathrm{MSE}_{\mathrm{linear}}(n)
&=
\Theta_d
\left(
\sum_{i\geq i^\star}i^{-2\gamma}
\right)
\tag{D.17}
\\
&=
\Theta_d
\left(
(i^\star)^{1-2\gamma}
\right)
\tag{D.18}
\\
&=
\left(
\frac{n}{d^q}
\right)^{(1-2\gamma)/(2\gamma)}
\tag{D.19}
\\
&=
\left(
\frac{n}{d^q}
\right)^{-1+1/(2\gamma)}.
\tag{D.20}
\end{aligned}
$$

这就是 Eq. (3.4) 第二行的来源。

---

## 十四、Appendix C：resolvent perturbation proof skeleton

Appendix C 的目标是证明 Theorem 3.1。主线可以压成三步。

第一步，研究 $\widehat C$ 的 signal part。Lemma C.1 表明：

$$
\mathbb{E}[\widehat C]
\approx
\frac{\nu_1}{\sqrt{2}}
A^{(1)}D_\gamma(A^{(1)})^\top.
$$

因此 population matrix 的 eigenvectors 基本就是 teacher directions $A_i^{(1)}$，eigenvalues 基本由 $\lambda_i$ 给出。

第二步，控制 noise operator norm。Lemma C.2 给出：

$$
\|\widehat C-\mathbb{E}[\widehat C]\|_{\mathrm{op}}
\lesssim
\sqrt{\frac{d^q}{n}}.
\tag{C.27}
$$

这和主文 Eq. (2.9) 的 heuristic noise scale 匹配。

第三步，使用 resolvent expansion 得到 eigenvector perturbation。Appendix C.2 从 resolvent：

$$
R_{\bar C}(z)
=
(zI_D-\mathbb{E}[\widehat C])^{-1},
\qquad
R_{\widehat C}(z)
=
(zI_D-\widehat C)^{-1}
\tag{C.4}
$$

出发，通过 Neumann series：

$$
(I_D-R_{\bar C}(z)\Delta)^{-1}
=
\sum_{\ell\geq0}(R_{\bar C}(z)\Delta)^\ell
\tag{C.8}
$$

把 perturbed projector 展开成 signal-subspace mixing 和 kernel-noise leakage 两部分，最后得到 Eq. (C.24)，也就是主文 Eq. (3.2) 的完整版：

$$
\widehat u_k
=
u_k
+
\sum_{j\neq k}
\frac{u_j^\top\Delta u_j}{\lambda_k-\lambda_j}u_j
+
\frac{1}{\lambda_k}
P_{\mathrm{Ker}}\Delta u_k
+
o(\|\Delta\|_{\mathrm{op}}^2).
\tag{C.24}
$$

这个 proof skeleton 的科学意义是：它不是只告诉我们 subspace 离得多远，而是把第 $k$ 个 recovered eigenvector 的误差来源拆成可估计的项。这样才能得到 feature-wise threshold 和必要性结果。

---

## 十五、Appendix A：Algorithm 1 和实验 metrics

Algorithm 1 的训练流程和主文一致。

第一步，把 $x_\mu$ 映射到 degree-$q$ Hermite feature：

$$
\phi_\mu
=
\mathcal F[\mathrm{He}_q(x_\mu)]
\in\mathbb{R}^D.
$$

第二步，构造：

$$
\widehat C
=
\frac{1}{n}
\sum_{\mu=1}^n
y_\mu
\mathrm{He}_2(\phi_\mu).
$$

第三步，取 $\widehat C$ 的 top $d_1$ eigenvectors，得到 $\widehat A_i^{(1)}$，并计算 learned first-layer features $\widehat h_{\mu,i}^{(1)}$。

第四步，在 learned latent space 中估计第二层：

$$
\widehat A^{(2)}
=
\frac{1}{n}
\sum_{\mu=1}^{n}
y_\mu
\mathrm{He}_2(\widehat h_\mu^{(1)}).
$$

第五步，计算 $\widehat h_\mu^{(2)}$，再在 $(\widehat h_\mu^{(2)},y_\mu)$ 上做 regression。

Appendix A 还定义了三个实验指标。

第一个是 empirical MSE：

$$
\widehat{\mathrm{MSE}}
=
\frac{1}{n_{\mathrm{test}}}
\sum_{\mu=1}^{n_{\mathrm{test}}}
\left(
\widehat f(x_\mu^{\mathrm{test}})
-
y_\mu^{\mathrm{test}}
\right)^2.
\tag{A.1}
$$

第二个是 first-layer feature overlap：

$$
q_h^{(1)}
=
\frac{1}{d_1}
\|Q^\top\widehat Q\|_F^2.
\tag{A.2}
$$

这里 $Q$ 和 $\widehat Q$ 分别是真实 first-layer feature matrix 与 learned first-layer feature matrix 的 column-space orthonormal bases。这个指标看的是 subspace 是否恢复，而不是坐标是否逐个完全对齐。这样处理是合理的，因为 eigenvectors 有符号、排列和有限样本旋转的不确定性。

第三个是 direction-wise alignment：

$$
\cos^2(\theta_i)
=
\|\widehat U^\top u_i\|^2
=
u_i^\top\widehat U\widehat U^\top u_i.
\tag{A.3}
$$

它回答的是第 $i$ 个 teacher direction 是否已经进入 recovered eigenspace。post-transition 之后，Theorem 3.1 预测：

$$
1-\cos(\theta_i)
=
O_d
\left(
\frac{d^q i^{2\gamma}}{nZ_\gamma^2}
\right).
\tag{A.4}
$$

这正是 Figure 4 中间图用 $1/n$ guide 检查的对象。

---

## 十六、Figure 3、Figure 5：$\gamma$ 和 nonlinear readout 的作用

![Figure 3 left](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-07-figure-01.jpg)

![Figure 3 right](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-07-figure-02.jpg)

Figure 3 改变 power-law exponent $\gamma$。由 Eq. (2.10)：

$$
n_i
\gtrsim
\frac{d^q i^{2\gamma}}{Z_\gamma^2}.
$$

当 $\gamma$ 变大时，强 feature 更强、弱 feature 更弱。结果是：最强的 directions 更早被恢复，但弱 tail 被推到更大的 sample size。整体 recovery window 被拉宽，MSE decay 更像跨多个阶段逐步发生。

![Figure 5 left](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-10-figure-01.jpg)

![Figure 5 right](../../pdfs/2026-05-18/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model/scaling-laws-from-sequential-feature-recovery-a-solvable-hierarchical-model.mineru/hybrid_auto/images/page-10-figure-02.jpg)

Figure 5 把 readout 换成 $g^\star=\tanh$。现象仍然是：first-layer overlap 上升时，MSE 同时下降。这说明主要瓶颈仍然是 first-layer representation recovery，而不是最后一维 readout。非线性 readout 增加了 finite-size effect，但没有改变核心机制。

---

## 十七、Discussion：这篇文章的结论和限制

作者的结论是：scaling laws 不一定只能来自固定 kernel spectrum，也可以来自 representation learning 中的 sequential feature recovery。

更具体地说，层级结构和 anisotropy 共同起作用。

层级结构让 learner 能先恢复中间 representation，把全局高阶 task 分解成低阶 feature recovery 和低维 readout。

Power-law anisotropy 让不同 latent directions 有不同 spike strength，于是 recovery thresholds 按 feature index 展开。

两者合起来，就得到：

$$
\text{depth exposes latent representation}
\quad+\quad
\text{power-law weights spread recovery thresholds}
\quad\Rightarrow\quad
\text{smooth scaling law}.
$$

限制也很明确。模型中的 hierarchy 是预先指定的；输入是 Gaussian；学习算法是 layer-wise spectral procedure，而不是真实端到端 SGD 训练的通用神经网络。作者用这些假设换来了 sharp recovery 和 non-recovery theorem。下一步自然问题是：这个机制能否扩展到更一般数据、更复杂非线性、更高 information exponent，以及更真实的 gradient-based training。

---

## 十八、和我们最近 generative model 主线的连接

这篇文章不是 generative model 论文，但它对我们最近的项目思路有一个很清楚的接口：它把 smooth scaling law 拆成了 hidden structure 的 sequential recovery。

这和我们读 diffusion / flow / VI / HJ-sampler 时反复遇到的问题有相似结构。

在 diffusion 或 flow matching 中，模型不是一次性学会整个 data distribution，而是在一条 probability path 上逐步恢复 structure。强结构、低频结构或大尺度 mode 往往先被恢复，弱结构、细节结构或 rare modes 往往需要更多数据、更多 compute 或更精确的 path design。

在 VI / adaptive proposal / importance sampling 中，固定 proposal 容易先覆盖强 mode，而漏掉弱 mode。一个 adaptive generative proposal 的目标，可以被理解成逐步恢复 posterior 的 mode structure，并用 importance weights 校正剩余 mismatch。

因此，如果把这篇文章接到课程 project 的路线 B，一个自然切入点是：

$$
\text{sequential feature recovery}
\quad\longleftrightarrow\quad
\text{sequential mode/proposal recovery}.
$$

也就是说，课程项目不一定要直接复现这篇高维 Hermite 模型；更实用的结合点是借用它的叙事：

$$
\begin{aligned}
&\text{target/posterior has anisotropic hidden structure}\\
&\rightarrow \text{fixed sampler/proposal first captures strong components}\\
&\rightarrow \text{adaptive generative proposal progressively captures weaker components}\\
&\rightarrow \text{ESS increases and variance decreases in stages}\\
&\rightarrow \text{aggregate curve looks like a smooth scaling law}.
\end{aligned}
$$

这条线能把 adaptive importance sampling、Bayesian inference、variance reduction 和 generative model 放在同一个 implementation project 里。
