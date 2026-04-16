---
title: "A framework for the use of generative modelling in non-equilibrium statistical mechanics"
paper_title: "A framework for the use of generative modelling in non-equilibrium statistical mechanics"
digest_type: "paper_note"
date: "2026-04-15"
---

# A Framework For The Use Of Generative Modelling In Non-Equilibrium Statistical Mechanics

## Core Answer

这篇文章的核心回答是：对于由 `Markov blanket` 分开的耦合非平衡系统，如果系统具有非平衡稳态分布，并且其随机动力学可以写成对稳态 surprisal 的梯度流，那么就可以进一步把内部状态的动力学改写成对 `variational free energy` 的梯度流。这样做的意义不在于宣称物理对象真的在做 Bayesian inference，而在于给出一种更可处理的建模框架：用 generative model 明确表示子系统之间的依赖关系，再把自组织、控制和稳态保持解释成“as if inference”的自由能下降过程。

## 0. Reading Frame

为了防止后面把统计物理、FEP、生成模型和哲学讨论混在一起，先把这篇文章的阅读框架固定下来：

1. 它要解决的问题是：怎样把 generative modelling 作为一种建模方法，用到 non-equilibrium statistical mechanics 里的耦合系统。
2. 它说的 `generative model` 不是现代机器学习里“从噪声生成样本”的训练模型，而是一个联合概率模型，用来表示系统各部分之间的依赖关系。
3. 它最关键的数学对象不是某个新网络结构，而是 `steady-state density`、`surprisal`、`variational free energy` 和 `Markov blanket`。
4. 它真正的主张不是“系统真的会推断”，而是“系统动力学可以被写成 as-if inference”。
5. 它的经验部分不是独立检验 FEP 普适性的实验，而是两个构造性的 worked examples。
6. 它后半部分的重要任务，是把 `generative model`、`variational density` 和真实物理系统分开，避免 map-territory fallacy。
7. 你最后要带走的是：这篇文章提出的是一种建模框架和解释语言，而不是一条新的物理定律或一个新的学习算法。

## 1. What Problem The Paper Is Actually Solving

这篇文章真正要解决的问题不是“自由能原理对不对”，也不是“某个具体系统能不能拟合得更好”。它要解决的是一个建模问题：当我们面对由多个对象耦合而成的开放系统，尤其是自组织、形态发生、周期活动这类非平衡系统时，能不能用一种统一的概率建模语言，把子系统之间的依赖关系和整体动力学同时写清楚。

作者给出的答案是：可以，前提是我们先把系统写成一个带有 `particular partition` 的联合系统，也就是把内部状态、外部状态和它们之间的边界状态分开。这个边界就是 `Markov blanket`。一旦这种划分存在，我们就可以把“系统如何受环境影响”和“系统如何对环境施加作用”写进同一个 generative model 里。

所以这篇文章的出发点不是“我们已经知道系统在做推断”，而是“如果一个系统与环境通过某种边界耦合，那么我们能否用推断的形式来重写它的动力学”。后面整篇文章都在为这个重写服务。

## 2. What Generative Modelling Means Here

这里的 `generative modelling` 必须先和机器学习语境分开。作者说的 generative model，不是 diffusion model、VAE 或 GAN 那种“学习数据分布再生成样本”的模型，而是一个联合概率分布

$$
p(\eta,b,\mu),
$$

其中 $\eta$ 表示环境或外部状态，$b$ 表示 blanket states，$\mu$ 表示内部状态。这个联合分布的任务，是明确系统各部分之间“谁依赖谁、谁屏蔽谁、哪些状态通过边界交换信息”。

这一步很重要，因为文章后面所有 inferential interpretation 都建立在这个联合分布之上。没有 generative model，就没有 posterior，也没有 variational density，更没有所谓自由能下降。换句话说，这篇文章先做的是概率建模，再做动力学重写。

在这个框架里，`Markov blanket` 的作用很具体。它不是抽象标签，而是统计上的条件独立边界：给定 blanket states 以后，内部状态和外部状态条件独立。正因为这条条件独立关系成立，系统内部状态才可能被解释为“对外部状态某些统计量的参数化估计”。

## 3. The Main Mathematical Move

这一节真正要回答的问题只有一个：作者怎样从“一个有稳态密度的随机动力系统”，走到“内部状态可以被写成 as-if variational inference”。这条链条不能从 free energy 开始，必须从完整的物理系统开始。

作者先考虑整个联合系统

$$
X_t = (\eta_t,b_t,\mu_t),
$$

这里的三块状态要先分清。$\eta_t$ 不是“所有外部世界”，而是相对于当前系统边界来说、会和系统发生耦合的外部变量。$\mu_t$ 则是系统边界之内的内部变量。$b_t$ 是两者之间的 `blanket states`，也就是内部和外部发生作用时必须经过的接口变量。作者需要单独引入 $b_t$，是因为后面要利用条件独立结构

$$
\eta_t \perp \mu_t \mid b_t,
$$

来说明内部状态和外部状态不是直接耦合，而是通过 blanket states 间接耦合。只有这样，后面 `Markov blanket` 的说法才有明确的数学内容，而不只是“系统有边界”这种直觉描述。

这也解释了为什么 $X_t$ 必须写成联合系统状态，而不能一开始只写内部状态。作者真正关心的不是一个孤立对象怎样演化，而是一个有边界的子系统怎样通过边界与外部发生耦合，并在这种耦合下表现出稳定性、自组织，乃至后面要说的 `as-if inference`。如果不把外部、边界和内部同时写出来，后面的 generative model、variational density 和 blanket-induced estimator 都接不上。

然后作者再加上一个关键假设：这个联合系统存在非平衡稳态密度 $p^*(x)$。这里的“稳态”说的是长期统计分布稳定，不是说系统停止运动；“非平衡”说的是系统仍然可以有持续的耗散、交换和概率流，而不是热平衡下的静止状态。这个假设不能省，因为后面所有 `surprisal` 的写法都依赖这个稳态密度。没有 $p^*(x)$，就没有

$$
-\log p^*(x),
$$

也就没有一个可供重写的稳定性函数。作者后面要做的事，正是利用这个稳态分布，把“哪些状态典型、哪些状态罕见”写成一个可以进入动力学方程的量。

在这个前提下，作者把完整随机动力系统写成

$$
\mathrm{d}X_t=f(X_t)\mathrm{d}t + D(X_t)\mathrm{d}W_t,
$$

然后进一步假设它的漂移项可以分解成对稳态 surprisal 的加权梯度流：

$$
\mathrm{d}X_t
=
-
\left(Q(X_t)-\Gamma(X_t)\right)\nabla_x\log p^*(X_t)\,\mathrm{d}t
+
D(X_t)\mathrm{d}W_t.
$$

这里有两个不能跳过的点。第一，$Q$ 是反对称矩阵场，$\Gamma$ 是正半定矩阵场，并且和扩散项相关。它们的作用不同：$\Gamma$ 对应耗散部分，把系统往更高概率、也就是更低 surprisal 的区域拉；$Q$ 允许沿等密度面的旋转或环流，所以这不是“纯粹的梯度下降”，而是“带环流项的加权梯度流”。第二，这一步说的不是系统已经在做推断，而只是说：如果系统长期维持在某个 attractor 附近，那么它的平均运动方向可以由稳态密度的几何结构来组织。`surprisal` 在这里首先是稳定性的刻画量，不是认知量。

接下来，文章才开始把 `Markov blanket` 和推断语言接上。因为 $\mu$ 和 $\eta$ 在给定 $b$ 时条件独立，作者调用一个映射

$$
\sigma(\hat{\mu}_b)=\hat{\eta}_b,
$$

把内部状态的条件模态和环境状态的条件模态关联起来。这里的逻辑是：如果内部状态通过 $\sigma$ 参数化了外部状态某个足够好的统计量，那么内部状态就可以被解释成“环境统计量的估计器”。这一步依赖额外假设。文章采用的是 `Laplace approximation`：在后验峰值附近把分布近似成高斯，于是局部均值或模态足以刻画后验的主要信息。正是在这个假设下，作者才引入 variational density

$$
q(\eta;\sigma(\mu)),
$$

并把它理解为由内部状态参数化的环境近似分布。

然后才出现 variational free energy。作者定义

$$
F(\mu,b)
=
D_{\mathrm{KL}}\bigl(q(\eta;\sigma(\mu))\,\|\,p(\eta\mid b)\bigr)
-\log p(\mu,b).
$$

这个定义最好先按“它想同时约束什么”来读。作者想同时表达两件事。第一，内部状态通过 $\sigma(\mu)$ 所给出的环境近似分布 $q(\eta;\sigma(\mu))$，应该尽量贴近由 blanket states 所决定的条件分布 $p(\eta\mid b)$。第二，当前的内部状态和 blanket 状态组合 $(\mu,b)$ 本身，不应该落在联合系统里很罕见的位置。也就是说，这个公式不是在凭空制造一个优化目标，而是在把“估计是否对”与“当前状态是否典型”这两件事绑在一起。

先看第一项

$$
D_{\mathrm{KL}}\bigl(q(\eta;\sigma(\mu))\,\|\,p(\eta\mid b)\bigr).
$$

它衡量的是：由内部状态参数化出来的环境近似分布，与 blanket 所允许的条件环境分布之间到底差了多少。如果这项很大，意思就是内部状态虽然可以被解释成某种环境模型，但这个模型和当前 blanket states 所支持的环境统计结构并不一致。只有当这项接近零时，我们才能说内部状态给出了一个好的环境估计。

再看第二项

$$
-\log p(\mu,b).
$$

这项不是在比较两个分布，而是在衡量当前 $(\mu,b)$ 这个状态本身有多不典型。概率越高，surprisal 越低；概率越低，surprisal 越高。所以第二项负责刻画“这个系统当前是不是待在它长期会待的那些典型状态附近”。这一步很重要，因为作者并不是只想让内部状态学一个正确的近似分布；他还想让系统本身处在一个稳定、可持续存在的状态区域里。

把这两项放在一起以后，$F(\mu,b)$ 的含义就清楚了：它小，当且仅当两件事同时成立。第一，内部状态对外部状态的近似是准的；第二，当前内部状态和 blanket 状态本身是典型的。换句话说，free energy 小，不只是“推断误差小”，也是“系统占据的状态不反常”。

现在才能理解为什么作者接着强调 `KL divergence` 非负。因为第一项永远大于等于零，所以

$$
F(\mu,b)\ge -\log p(\mu,b).
$$

这就是说，free energy 永远不会低于单纯的 surprisal。于是它成了一个更容易处理的上界：你即使暂时不直接去碰真实的 surprisal，也可以先控制 free energy。只有当 variational density 和目标条件分布完全对齐时，`KL` 项才会消失，这个上界才会贴住原来的 surprisal。这个多出来的距离，就是这篇文章里真正的 `inference gap`。如果 gap 很小，那么 free-energy descent 和 surprisal descent 几乎是同一件事；如果 gap 很大，那么“系统像在做 inference”的说法就只是一个很松的近似，而不是紧的数学重合。

现在才能做最后一步重写。前面完整系统的动力学已经被写成对 surprisal 的流；这里又把内部状态参数化成了一个 variational density，并且拿到了 surprisal 的一个 free-energy 上界。于是，作者把内部状态的动力学投影到 $\mu$ 坐标上，写成

$$
\mathrm{d}\mu_t
=
-(Q-\Gamma)\nabla_\mu F(\mu,b) + \mathrm{d}W_t.
$$

这就是全文真正的数学动作。它并不是从零推出“系统会推断”，而是依次做了四件事：先假设完整系统有非平衡稳态密度；再把完整动力学写成 surprisal 的加权梯度流；再用 `Markov blanket`、$\sigma$ 和 `Laplace approximation` 把内部状态变成外部状态分布的参数估计器；最后利用 `free energy = surprisal upper bound + inference gap` 这层关系，把内部动力学改写成 free-energy descent。

读到这里最容易困惑的地方，其实正是这三处静默假设。第一，稳态密度 $p^*(x)$ 不是推出来的，而是先假设存在。第二，$\sigma(\mu)$ 如何足够好地参数化环境分布，不是自动成立的，而是依赖特定结构和近似。第三，从 surprisal flow 走到 free-energy flow，靠的是 `KL gap` 足够小乃至为零时的重合关系。因此，这一节最稳妥的结论不是“所有有边界的系统都在做 Bayesian inference”，而是：在这些结构和近似都成立时，内部动力学可以被重写成一种 `as-if variational inference` 的形式。

## 4. Why This Rewriting Is Useful

这篇文章一直强调，这种重写有两个直接好处。

第一，`tractability`。直接处理耦合随机动力系统时，系统各部分之间的非线性依赖可能非常难算；而 variational free energy 是一个更容易处理的上界。于是，原本难以直接求解的 surprisal dynamics，可以改写成更容易操作的 free-energy gradient flow。

第二，`explanation`。generative model 把“对象如何依赖环境”显式写出来，所以模型不会只给出一条轨迹，还会告诉我们：内部状态在估计什么，blanket 在屏蔽什么，系统如何通过边界与环境耦合。这正是作者反复强调 generative modelling 比“直接写随机动力系统”更有解释力的原因。

因此，这篇文章真正想卖的不是“FEP 很深刻”这种抽象口号，而是一条很实际的建模主张：如果你已经知道系统是耦合的、开放的、非平衡的，并且它存在合适的 particular partition，那么用 generative model 来编码依赖关系，会让模型既更可处理，也更容易解释。

## 5. What The Paper Does Not Claim

这篇文章最容易被误读的地方，是把 inferential language 当成 literal claim。作者在引言、第二节和后半部分都反复澄清：他们并不主张物理对象在字面意义上执行了 Bayesian inference。

更准确的说法是：系统动力学可以被写成 `as if inference`。也就是说，作为建模者，我们可以把内部状态视为某个 variational density 的参数，把自由能下降视为 inference gap 的缩小，并用这种语言解释系统行为。但这仍然是模型层面的解释，不是对系统内部机理的字面描写。

这也是为什么文章后来要严格区分三样东西：

1. `generative model`：建模者写下的联合概率模型。
2. `variational density`：内部状态参数化的近似分布。
3. `real-world system`：真正的物理对象和它的动力学。

这三个对象不分开，后面关于 map-territory fallacy 的讨论就会全部混掉。

## 6. What The Empirical Section Is Actually Doing

第三节名叫 `Empirical validation`，但读的时候要克制，不要把它当成对 FEP 普适性的独立实验检验。作者在 `3(c) Looking ahead` 里自己已经说得很清楚：这里的两个例子，是 `worked examples`，不是从独立物理模型 bottom-up 推出来的严格验证。

第一个例子是 `cellular morphogenesis`。作者给一组细胞规定 target morphology，然后给每个细胞配一个 generative model，使它根据感受到的信号去推断“自己应该在整体形态中的哪个位置、表达哪种 signalling profile”。最后系统在 free-energy gradient flow 下形成预期形态。这个例子的作用，是说明 generative model 如何把“目标结构”编码进系统，并把自组织写成自由能下降。

第二个例子是 `periodically firing cells`。这里目标不再是固定形态，而是周期波形。系统因此不再收敛到固定点，而是收敛到一个极限环。这个例子的作用，是说明相同的 FEP 重写不仅能表示 fixed-point self-organization，也能表示 oscillatory self-organization。

所以第三节的阅读重点不是“这些实验是否证明所有细胞都在做推断”，而是“作者怎样把具体 generative model 写进 toy system，并让 free-energy flow 产生目标行为”。

## 7. Why Section 3(c) Matters More Than It First Looks

如果只看前两个 toy example，这篇文章很容易被误读成“先假设自己想要的结果，再造一个支持它的例子”。作者自己其实意识到了这个问题，所以 `3(c) Looking ahead` 很重要。

这一小节明确承认：他们现在做的不是 agnostic bottom-up derivation。也就是说，他们不是先拿一个独立给定的 Langevin model，再去问能否反推出 free-energy form；他们是先指定合适的 steady state、$Q$、$\Gamma$ 和 generative model，再构造一个动力系统，使它确实能写成 free-energy descent。

这段承认非常关键，因为它帮我们准确定位了文章贡献。它的贡献不是“证明任何非平衡系统都天然等价于 FEP”，而是“给出一套 constructive framework：只要 decomposition 和 Markov blanket 存在，就可以系统地构造相应的 generative model 和 variational interpretation”。这个说法严格得多，也更可信。

## 8. What The Philosophical Sections Add

第四、第五节不是和前面数学内容无关的附会，它们在完成一个必要任务：防止前面的 inferential rewriting 被误读成 model reification。

作者要回答的问题很直接：如果我们把某个系统写成“像是在推断环境”，这是不是把我们的模型误当成了系统本身，也就是犯了 `map-territory fallacy`。他们的回答是：不必然，因为 FEP 框架里本来就区分了 generative model、variational density 和真实系统。建模者的 generative model 是“我们的 map”；而系统内部某些状态之所以看起来像 map，是因为在 particular partition 下，它们可以被写成对外部状态的统计跟踪。

因此，第五节真正想说的不是一句修辞，而是一条方法论主张：`FEP 提供的是一张关于“哪些系统成分可以被建模成 map”的 map。` 也就是说，它是一套关于 modelling relation 本身的约束，而不是把所有物理系统直接神秘化成会思考的主体。

## 9. What To Keep From This Paper

如果把整篇文章压成最值得留下的几句话，可以保留下面这条线：

1. 先用 generative model 写出内部、外部和 blanket states 之间的依赖关系。
2. 再用非平衡稳态分布把系统动力学写成 surprisal gradient flow。
3. 然后利用 variational free energy 是 surprisal 上界这一点，把内部动力学重写成 as-if inference。
4. 最后用这个重写去构造更可处理、也更有解释力的 self-organization 和 control 模型。

所以，这篇文章最有价值的地方不在于它证明了“自然界万物都在推断”，而在于它给了一套更严格的说法：当 decomposition、steady state 和 Markov blanket 条件满足时，我们可以把某些非平衡耦合系统建模成自由能下降系统，并用 generative model 明确地表示子系统之间的依赖结构。

## 10. Why Active Inference Is Respected But Controversial

把这篇文章放回更大的 `active inference` 语境里，它的定位会更清楚。这个方向之所以一直有人认真看，不是因为它已经变成了主流工程方法，而是因为它提供了一套形式上很统一的语言，可以把 perception、action、learning、exploration 和 control 放进同一个概率框架里。对于喜欢统一解释的人来说，这是一种很有吸引力的理论结构。

但它之所以争议大，也正是因为它的语言常常比它已经严格证明和广泛验证的内容更大。支持者会说，这个框架把 generative model、variational free energy 和 decision-making 放进了一条连续的数学链条里；批评者会说，这条链条在很多地方依赖额外假设，而且经常是在重写已有系统，而不是发现新的机制。

因此，`active inference` 目前最稳妥的定位，不是“已经被充分验证的通用智能方法”，也不是“纯粹空话”。更准确的说法是：它是一套受尊重但高度争议的统一建模语言。它的强项在于提供统一解释、把 epistemic exploration 和 goal-directed behaviour 写进同一目标函数，并把一部分控制问题改写成 free-energy minimization；它的弱项在于经验验证仍然有限，很多应用结果还停留在 toy example、仿真或小规模系统上。

从这个角度回看本文，最合理的读法就不是“它提出了一个已经成熟可用的新 AI 方法”，而是“它在 `active inference` 这套语言内部，把 non-equilibrium interacting systems 系统地翻译成 generative-model / free-energy 的形式”。这样读，文章的贡献和边界都会更清楚。

## 11. What AI And ML Work Actually Exists Around Active Inference

如果把问题收紧成“`active inference` 有没有和现代 `ML/AI` 真正接起来”，答案是有，但规模不大，而且最像样的工作主要集中在 `RL`、`POMDP` 和机器人控制这条线上，而不是主流生成模型或大模型应用。

第一类文章在做理论接口。[Deep active inference agents using Monte-Carlo methods](https://proceedings.neurips.cc/paper/2020/hash/865dfbde8a344b44095495f3591f7407-Abstract.html)（`NeurIPS 2020`）把 active inference agent 推到更复杂的状态空间里，说明这套框架并不只能停留在低维 toy model 上。[Active Inference and Reinforcement Learning: A Unified Inference on Continuous State and Action Spaces Under Partial Observability](https://direct.mit.edu/neco/article/36/10/2073/124162/Active-Inference-and-Reinforcement-Learning-A)（`Neural Computation 2024`）则更直接地把 active inference 和 reinforcement learning 的关系拆开，重点说明它们在连续状态、连续动作和部分可观测条件下怎样重合，又在哪些目标项上不同。

第二类文章在做深度状态空间模型和 world model 的结合。[Deep active inference as variational policy gradients](https://www.sciencedirect.com/science/article/abs/pii/S0022249620300298)（`Journal of Mathematical Psychology 2020`）把 active inference 和 variational policy gradient 直接对齐，说明它和现代 policy optimization 并不是两套完全无关的数学。[Learning Generative State Space Models for Active Inference](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2020.574372/full)（`Frontiers in Computational Neuroscience 2020`）则把深度生成状态空间模型接到 active inference 上，这一支最接近 `VAE`、latent dynamics model 和 world model 这条机器学习路线。

第三类文章在做真实或接近真实的机器人任务。[Robot navigation as hierarchical active inference](https://www.sciencedirect.com/science/article/pii/S0893608021002021)（`Neural Networks 2021`）把层级 active inference 用在机器人导航、定位和建图问题上，而且不只是纯仿真。更新的 [Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model](https://doi.org/10.1109/LRA.2025.3636032)（`IEEE Robotics and Automation Letters 2026`）进一步把 temporally hierarchical world model 和 deep active inference 接在一起，用于真实机器人控制。

这些文章说明的事情很具体：`active inference` 不是完全脱离现代 `ML/AI` 的封闭语言，它确实已经和 `RL`、深度状态空间模型、world model、机器人控制发生了实质连接。但这组文章说明的也只有这一点。到目前为止，它还没有在主流 AI 里形成像 transformer、diffusion、standard model-based RL 那样的广泛采用地位。因此，更准确的判断不是“这条路已经成熟”，而是“这条路已经长出了几个可信的连接点，但仍然属于小而稳定的交叉研究线”。
