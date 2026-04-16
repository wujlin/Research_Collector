---
title: "Fluctuating entropy production on the coarse-grained level"
paper_title: "Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility"
digest_type: "paper_note"
date: "2026-04-11"
---

# Fluctuating Entropy Production On The Coarse-Grained Level

## Core Answer

这篇文章的核心回答是：即使系统只能被粗粒化地观测，只要能识别出合适的 `Markovian events`，就仍然可以在 `snippet` 层重新定义一个会涨落的 coarse-grained entropy production；这个量不仅能给出平均不可逆性，还能把 irreversibility 局域到具体事件类型和 waiting-time structure 上，并在一定条件下检测 hidden driving、给出隐藏循环 affinity 的下界。

## 0. Reading Frame

为了避免后面展开时失去主线，先把这篇文章的阅读框架固定下来：

1. 它要解决的问题是：当系统只能被粗粒化地观测时，还能不能定义、推断并局域化 entropy production。
2. 它重要的地方在于：现实系统通常并非全可见，而你关心的不只是总 irreversibility，还关心它发生在哪里。
3. 它研究的对象不是完整微观动力学，而是 coarse-grained trajectory、Markovian events、snippets 和 hidden driving。
4. 它的核心演化重写是：把整条轨迹切成由两个 Markovian events 夹住的局部 snippets。
5. 它关心的核心量不是总熵产生，而是 fluctuating entropy production、irreversibility localization 和 hidden-driving detection。
6. 它的方法关键是：用 snippet 的正反权重比去重建 coarse-grained entropy production。
7. 它最有说服力的证据是：理论定义闭合、`Figure 3` 展示局域涨落、`Figure 4-5` 展示 hidden driving 的检测与定位。
8. 你最后要带走的是：真正高信息量的对象，不是全局总量，而是轨迹片段上的结构化不对称。

## 1. Why Coarse-Grained Irreversibility Is Hard

标准随机热力学默认你能看到完整微观轨迹，于是 entropy production 可以直接写成正向路径概率和反向路径概率的对数比。真实系统往往做不到这一点。观测者通常只能看到 coarse-grained trajectory，看不到隐藏自由度，也看不到所有中间跃迁，因此标准轨迹级公式不能直接照搬。

真正困难的地方不只是“少看了一些自由度”，而是 coarse-graining 之后很多原本清楚的热力学结构会一起丢失。你会失去完整 path weight、失去干净的时间反演对象，也失去总熵产生和局部不可逆性之间的直接联系。于是问题变成：在这种有限观测设定下，能不能重新找回一个仍然有物理意义的轨迹级不可逆性对象。

## 2. The Minimal Building Blocks: Markovian Events And Snippets

![Fig. 1 energy landscape and localized snippets](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/209f576534bf5edb8700493cb54e8b947f893989425f53de9e377b3ede9971ae.jpg)

![Fig. 1 localized snippet in the time series](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/2e61fb0331b7f1716bc25961d5a5d641b6011d09a1292de4c63b45112a5fe80d.jpg)

作者的关键想法不是继续把 coarse-grained state 当成基本对象，而是换一个更稳的基本单元：`Markovian event`。它的定义是，一旦观测到这个事件，未来演化和更早的过去条件独立。换句话说，它在粗粒化后重新提供了一个“记忆被切断”的时间点。

正式地，作者要求

$$
P[\gamma^+ \mid I,\gamma^-] = P[\gamma^+ \mid I].
$$

这里 $\gamma^-$ 表示事件 $I$ 之前的历史，$\gamma^+$ 表示事件 $I$ 之后的未来。这个式子的意义是：一旦事件 $I$ 已经发生，未来演化的统计就不再依赖更早的过去，于是 $I$ 可以充当切分 coarse-grained trajectory 的锚点。

这个定义之所以重要，是因为它允许作者把一条粗粒化轨迹切成很多 `snippets`。每个 snippet 都由“起始 Markovian event + 终止 Markovian event + 中间持续时间”构成。于是，后面的 entropy production 不再建立在完整微观轨迹上，而是建立在这些可观测 snippet 上。

如果一条 coarse-grained trajectory 写成

$$
\Gamma=(I_0 \to I_1 \to \cdots \to I_n),
$$

那么相邻两个 Markovian events 之间的局部片段

$$
I_{k-1}\to I_k
$$

就是一个 snippet。作者后面不是先给整条轨迹一个黑箱总量，而是先给每个 snippet 定义 entropy production，再把这些局部贡献组织起来。

这里有一个经常被省略、但对全文很关键的前提：并不是任何 coarse-grained observable 都能直接当作 `Markov state`。只有当系统满足清楚的时间尺度分离，例如阱内弛豫远快于阱间跃迁，也就是

$$
\tau_{\mathrm{intra}} \ll \tau_{\mathrm{inter}},
$$

一个粗粒化状态才可以近似视为马尔可夫状态。如果这种分离不清楚，那么系统离开某个可见状态时仍会保留进入该状态的历史信息，整体 coarse-grained dynamics 就会带记忆。作者正是因此放弃“状态必须是 Markov state”的要求，转而去找那些一旦发生就能切断记忆的 `Markovian events`。

![Fig. 2 transition-based coarse graining and snippet structure](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/eeff80d2060960772bbc51835b4fd85b9ea4d2c51903a46574d470f1f3c6713f.jpg)

![Fig. 2(a,b) coarse-grained event structure](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/fff04169c2caaea52dfba35c3f4afe0382495444869420729a8395f3091719db.jpg)

![Fig. 2(c) event pair used for localization](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/a3c02a452e54f95754152d71ef26d35f44a69a6835d83b5661f837fd6008287a.jpg)

这一步还要求你区分几组对象。第一组是 `state-based` 和 `transition-based` 描述：前者记录“当前在哪个状态”，后者记录“刚刚发生了哪次跃迁”。第二组是时间反演下的 `even observables` 和 `odd observables`：前者在时间反演下不变，后者会翻方向或变号。作者的方法之所以干净，在于它能在这些不同 coarse-grained 描述下都给出统一的 snippet-level 结构。

这两个区分不是术语游戏。`state-based` 与 `transition-based` 的区别，决定了 coarse-grained trajectory 到底是“状态序列”还是“事件序列”；`even` 与 `odd` observables 的区别，则决定了时间反演时观测量本身要不要变号、变方向。因此，若要在 coarse-grained level 上定义 entropy production，你不仅要知道正向轨迹是什么，还要知道反向轨迹应该怎样构造。

## 3. How Coarse-Grained Entropy Production Is Rebuilt

重建 coarse-grained entropy production 的逻辑其实很直接。微观层上，单条轨迹的 entropy production 仍然来自正向路径权重和反向路径权重的对数比。作者做的不是推翻这个结构，而是把它搬到 snippet 上：先比较正向 snippet 的权重，再比较与之对应的反向 snippet 的权重，从而得到 coarse-grained entropy production。

这里有一个不能省略的过渡层。若观察者只能看到 coarse-grained trajectory $\Gamma$，那么首先必须知道它的正向概率 $P[\Gamma]$ 和反向概率 $P[\tilde\Gamma]$ 分别是什么。它们不是另起炉灶定义出来的，而是由微观 path weight $P[\gamma]$ 以及 coarse-graining 映射 $\gamma\mapsto\Gamma$ 唯一诱导出来的。因此，时间反演在这里不是单纯把电影倒放，而是要连同 coarse-grained observable 在时间反演下的变换一起处理。

在这个基础上，snippet 的 coarse-grained entropy production 可以写成

$$
\Delta S[\Gamma_s]
=
\ln \frac{P(I)\,P[\Gamma_s \mid I]}{P(J)\,P[\tilde{\Gamma}_s \mid \tilde J]}.
$$

若系统是 stationary，并且把 snippet 写成“从事件 $I$ 到事件 $J$、持续时间为 $t$、附加 observable 为 $O$”的形式，那么也可以写成

$$
\Delta S[\Gamma_s]
=
\ln \frac{P(I)\,\psi_{I\to J}(t;O)}
{P(J)\,\psi_{\tilde J\to \tilde I}(t;\tilde O)}.
$$

这两种写法表达的是同一个骨架：coarse-grained entropy production 仍然是正向 snippet 权重和反向 snippet 权重的对数比，只不过现在比较的是 coarse-grained event pair 与 waiting-time statistics，而不是完整微观路径。

因此，这篇文章真正重建的不是“新的热力学量”，而是“有限观测下仍然可落到轨迹片段上的热力学定义”。也正因为它建立在 snippet 上，后面才能谈 fluctuation、localization 和 hidden driving，而不是只剩一个总的平均下界。

作者还给出了一条很关键的一致性关系：

$$
e^{-\Delta S[\Gamma]}
=
\left\langle e^{-\Delta s}\mid \Gamma \right\rangle.
$$

这条关系的意义是：固定一条 coarse-grained trajectory $\Gamma$ 后，所有与它兼容的微观轨迹 $\gamma$ 仍然形成一个条件分布，而 coarse-grained entropy production 不是这些微观 entropy production 的普通平均，而是它们的条件指数平均。于是，coarse-grained entropy production 不只是“总量被压小了一些”，而是仍然保留了 fluctuation relation 的骨架。再对这条关系应用 Jensen 不等式，就得到 coarse-graining 只会丢失 irreversibility、不会凭空增加 irreversibility 的不等式结论。

## 4. Why Coarse-Grained Entropy Production Still Fluctuates

![Fig. 3 fluctuating entropy production at microscopic and coarse-grained levels](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/90807edf729c8ea50da2e3e79b4384b1eb8fded921e0171e7325fb645772698a.jpg)

![Fig. 3 local snippet entropy production rates](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/becf653a0ad7c830a0d39ab9a9668a9fc1cc0441f0e0cc263be0f1fbf4a05ee4.jpg)

![Fig. 3 convergence of local rates](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/ae71ae3c08f75d1253175de0cc3a685ac7f02079254f87da076412301e278473.jpg)

这一篇最重要的推进，是作者证明 coarse-grained entropy production 不是“只有平均后才有意义”的量。它在整条轨迹上会波动，在固定 snippet 类型上也会波动。`Figure 3(a)(b)` 先说明累计 entropy production 和 entropy-production rate 都会沿单条轨迹随机起伏，只是 coarse-graining 会把整体可见的 irreversibility 压低。

`Figure 3(c)` 则把注意力缩到固定事件对上，例如从 $\tilde K$ 出发、最终又回到 $\tilde K$ 的 snippets。粗粒化后，这些 snippets 的标签看起来相同，但在微观层面它们对应许多不同隐藏路径。不同路径通常具有不同 waiting time，而 coarse-grained entropy production 正是由正反 waiting-time statistics 的不对称决定的。因此，即使事件标签相同，snippet 持续时间的波动也会直接转化成 entropy production 的波动。

所以这一节真正建立的是：coarse-grained entropy production 既可以在轨迹层面波动，也可以在事件层面局域；它不是平均量的残影，而是仍然保有 fluctuation structure 的随机热力量。

## 5. Hidden Driving: Detection, Localization, And Bounds

在 coarse-grained 设定下，最麻烦的情况是 hidden part 本身也不在平衡，甚至内部包含被驱动的循环，但这些循环并不直接推动可见事件之间的净流，也没有额外 observables 把它们暴露出来。作者把这种情形叫做 `hidden driving`。在 Markov 网络里，它最典型的形式就是：隐藏层里存在 nonzero affinity 的 driven cycle。

作者用一个非常干净的思路来检测这种 hidden driving。对于固定事件对

$$
I \xrightarrow{t} J,
$$

coarse-grained entropy production 会成为等待时间 $t$ 的函数。于是他们定义

$$
\Delta a_{I\to J}
=
\sup_t \Delta S\!\left[I \xrightarrow{t} J\right]
-
\inf_t \Delta S\!\left[I \xrightarrow{t} J\right].
$$

这个量衡量的不是某个固定等待时间的不可逆性，而是同一种可见 snippet 在所有持续时间上能展现出的时间不对称振幅。作者证明

$$
\max_C |A_C| \ge \Delta a_{I\to J},
$$

也就是说，只要 $\Delta a_{I\to J}>0$，就能肯定 hidden part 里至少存在一个非零 affinity 的循环，而且这个振幅给出了它的下界。

![Fig. 4(c) hidden-driving detection through time-dependent a(t)](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/d0d90016a49d27cdd658d9629c21265da60c6eb5048a9f1c0f643fd8c83d0312.jpg)

`Figure 4(c)` 给的是最基础的 hidden-driving detection 图像。若同一个可见事件对的 $a(t)$ 会随 $t$ 明显变化，那么这份时间依赖本身就已经说明 hidden part 中有被驱动的循环，且其驱动力至少达到 $\Delta a$ 这个量级。

作者还进一步说明，你并不一定只能用 $I$、$J$ 和总等待时间 $t$。如果有额外 observable，而且它在时间反演结构下是自洽的，就可以进一步增强 localization。但这里有严格约束：证明 hidden-driving bound 时需要构造一个与真实时间反演在 coarse-grained 层上不可区分的部分反演操作，因此附加 observable 必须是 time-reversal even。也正因为此，snippet 内部更细的 waiting times 一般不能直接加入；总时长 $t$ 可以用，是因为它在时间反演下保持不变。

![Fig. 5(a,c) localization and failure geometry](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/bf4917a98591a581db8882f77fe5c8cfe9afd64091492951bc8901d6789692d9.jpg)

![Fig. 5(b) localization enhanced by the observable H](../../pdfs/2026-04-11/fluctuating-entropy-production-on-the-coarse-grained-level-inference-and-localization-of-irreversibility.mineru/hybrid_auto/images/8e8d9e43db96d0aaeac93d562a7a131938de5a9a03a0502538c7097ed0cf833f.jpg)

`Figure 5` 展示的就是这种增强版 localization。对于 `1\to4` 的 trajectories，如果再区分“是否经过 $H$”，那么 hidden driving 的位置就能被明显剥离出来：不经过 $H$ 的轨迹几乎不呈现时间依赖；经过 $H$ 的轨迹则给出显著更大的 $\Delta a$；如果把这两类混在一起，信号会被平均稀释。这里真正被展示的不是“多一个 observable 更好”这么抽象的结论，而是：合适的、时间反演下自洽的附加信息，确实能把隐藏不可逆性从混合背景里局域出来。

## 6. When The Method Fails

作者也很明确地给出了失败情形。可能出现

$$
\Delta a = 0
\qquad\text{despite}\qquad
A \neq 0.
$$

如果一个 hidden driven cycle 被封装在某个 `compound state` 里，只通过单一接口和外界相连，且所有进出该黑箱的转移都满足 `direction-time independence`，那么外部 observable 就无法感受到内部驱动的方向性。此时，内部确实仍在耗散，但它不会在外部可见 snippet 的 waiting-time statistics 上留下可辨别痕迹，因此从黑箱外部出发就无法恢复这部分 irreversibility。

这一步很重要，因为它给出了这篇方法的真实边界：它抓住的不是“所有 hidden driving”，而是“那些会在 coarse-grained time statistics 上泄漏出来的 hidden driving”。

## 7. What To Retain

这篇最值得带走的，不是某个单独公式，而是一整套工作方式：

1. 先找到能在 coarse-grained 条件下切断记忆的 `Markovian events`。
2. 再用它们把轨迹重写成可以比较正反概率的 `snippets`。
3. 然后把 entropy production 从总量改写成会涨落、可局域化的对象。
4. 最后利用 waiting-time asymmetry 去检测和定位 hidden driving。

如果以后你要把不可逆性、局域 score、生成动力学这几条线接到一起，这篇文章最直接的启发就是：真正高信息量的对象，往往不是全局总量，而是轨迹片段上的结构化不对称。
