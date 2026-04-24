---
title: "Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model"
paper_title: "Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model"
digest_type: "paper_note"
date: "2026-04-16"
---

# Real-World Robot Control By Deep Active Inference With A Temporally Hierarchical World Model

## Core Answer

这篇文章的核心回答是：`deep active inference` 之所以很少真正落到真实机器人上，不是因为 “epistemic value + extrinsic value” 这个目标本身没意义，而是因为原始做法需要在执行时对大量连续动作序列直接算 `EFE`，计算量太高，而且世界模型对长时依赖的表示也不够强。作者给出的工程性解法是：先用一个 `slow/fast` 两层的时序世界模型去表示环境，再用一个向量量化的 `action model` 把长动作序列压成少量离散 `abstract actions`，最后再训练一个只在慢时间尺度上预测未来状态的 `abstract world model`。这样，机器人就不必直接在原始动作空间里规划，而可以在抽象动作空间里算 `EFE`，从而把 active inference 变成一个真实机器人上可跑、可切换 goal-directed 与 exploratory 行为的控制框架。

## 0. Reading Frame

为了避免把这篇文章读成“又一篇 active inference 哲学文章”，先把阅读框架固定下来：

1. 它要解决的问题是：怎样让 `active inference` 在真实机器人控制中变得可表示、可规划、可计算。
2. 它真正的新意不是重新定义 `EFE`，而是通过 `temporal hierarchy + action abstraction` 让 `EFE` 的计算变得 tractable。
3. 它说的 `world model` 不是泛泛的“环境模拟器”，而是一个带 `slow/fast hidden states` 的层级 latent dynamics model。
4. 它说的 `action abstraction` 不是语言指令，而是把固定长度动作序列压成少量离散 code 的 `abstract actions`。
5. 它的证据重点不是大规模 benchmark 打榜，而是三件事：计算量是否降下来了、真实机器人目标操作是否成功、在不确定环境里是否真的会转向探索行为。
6. 你最后要带走的是：这篇文章最有价值的地方，不是它把 active inference 讲得多统一，而是它找到了一个具体的工程接口，把 `epistemic exploration` 放进真实机器人控制的计算图里。

## 1. What Problem The Paper Is Actually Solving

这篇文章要解决的问题很具体：真实环境里的机器人，不只是要“朝目标动作”，还要在不确定时主动去获取信息。例如，锅盖盖着的时候，机器人不知道锅里有没有球；如果它完全没有探索能力，就只能盲目执行目标动作，容易失败。

作者认为 `active inference` 在形式上很适合这种场景，因为它天然把两类行为写进同一个目标函数：

- `extrinsic value` 鼓励去完成目标。
- `epistemic value` 鼓励去降低不确定性。

但问题是，标准 deep active inference 一到真实机器人就会遇到两个实际瓶颈：

1. 世界模型对复杂环境动力学的表示能力不够，尤其是长时依赖。
2. 执行时要对大量未来动作序列直接算 `EFE`，计算代价太高。

所以这篇文章不是在证明 `active inference` 的哲学，而是在解决一个工程问题：

`怎样把 active inference 从一个形式优美但计算昂贵的框架，变成真实机器人上能执行的控制架构。`

### 1.1 Why The LfD Related Work Matters

文章在 `Related Work` 里先讲 `Learning from Demonstration (LfD)`，不是因为它想做一篇泛泛的机器人综述，而是因为这篇方法的真实入口本来就来自 demonstration data。对机器人来说，`LfD` 的优势很实际：它让系统先从人类专家的安全、任务相关轨迹里学，而不是一开始就在真实环境里盲目 trial-and-error。

但作者马上指出，机器人领域近年的关键进展，不是简单“模仿专家”，而是开始把学习对象从 `single-step action` 提升到 `multi-step action sequence`。这一步很重要，因为真实机器人有意义的行为本来就天然带时间延续性，例如接近目标、抓取、搬运、放置，很难被理解成彼此独立的一步一步控制。

接着作者又补上一句真正重要的限制：哪怕 demonstration 很多，`LfD` 在不确定环境里仍然很难泛化。原因不是数据量不够，而是机器人面对的往往是部分可观测环境，系统不仅要“会执行”，还要判断什么时候应该先获取信息。单纯模仿已有动作模式，并不能自动给出这种 exploratory behavior。

所以这一段 related work 的真正功能，是把问题收束成下面这句话：

`demonstration 最有价值的，不只是给出专家动作标签，而是提供一批可被压缩成抽象行为单元的多步动作片段。`

这也解释了为什么作者最后明确说，他们聚焦的是“从动作序列里提取量化特征，并把这些特征当成 abstract action representations”的路线。换句话说，这篇文章不是把 `LfD` 直接拿来当策略学习终点，而是把它当成构造抽象动作词表的数据来源。

### 1.2 Why The World-Model Related Work Matters

在 `Related Work` 的 `World Model` 小节里，作者做的第一件事，是把 world model 从一个模糊热词重新压回一个很具体的定义：它要同时建模观测、隐藏状态和动作之间的关系。也就是说，这里的 world model 不是单纯“预测下一帧图像”，而是一个 latent dynamics model。

但作者马上指出，仅仅“有一个 world model”还不够。真实机器人上，性能会直接受限于世界模型是否真的学到了环境动力学，尤其是长时依赖。如果模型只能吃住短时相关性，却抓不住任务阶段推进、物体状态变化和不确定性消除这些慢变量，那么它就无法支撑后续规划。

于是这篇文章在 related work 里做出的关键判断是：机器人 world model 的主要难点不是把模型做大，而是把时间结构做对。作者给出的答案，就是把 temporal hierarchy 引入状态建模里。更具体地说，他们认为慢变量和快变量不能混在一个单层状态里，否则要么长时依赖学不住，要么规划代价太高。

这里还有一条和前面 `LfD` 小节直接接起来的线：如果动作也有快慢之分，那么把多步动作序列压成 `abstract action representations`，就不仅仅是在做动作压缩，而是在给世界模型提供一组能表达慢动态的控制接口。这样一来，`world model + abstract action` 才能共同支撑一个低频、可规划的抽象层。

所以这段 world-model related work 的真正逻辑，不是“别人也在做 world model，我们也做一个”，而是：

`机器人控制想真正利用 world model，就必须把状态层级和动作层级一起做成时间抽象，否则 active inference 仍然会卡在表示能力和规划成本上。`

## 2. What Active Inference Means In This Paper

这篇文章里的 `active inference` 最好不要只记成“有 `epistemic value` 和 `extrinsic value` 两项”。更准确的读法是：它把机器人控制拆成两个连续步骤。

第一步是 `perception`，也就是：给定当前观测，机器人怎样推断“我现在处在什么隐藏状态”。  
第二步是 `action`，也就是：在已经形成当前状态信念之后，我应该执行哪条未来动作序列。

原文对应这两步，先给出方程 `(1)` 的 `variational free energy`，再给出方程 `(2)` 的 `expected free energy`。

### 2.1 The Shared Generative Setup

两条方程共享同一个起点：观测 $o_t$ 不是世界本身，而是由隐藏状态 $z_t$ 生成出来的；而隐藏状态又会在动作作用下演化。也就是说，这里的基本对象不是“图像 $\rightarrow$ 动作”的直接映射，而是一个部分可观测动力学系统。

这里先固定术语口径，避免后面混淆：

- 本节统一使用 `隐藏状态` 来指代状态变量 $z_t$，后面不再切换成别的叫法
- `先验` 和 `后验` 不是两种不同的状态，而是对同一个隐藏状态 $z_t$ 的不同分布
- 因此，严格说不应该把 $p(z_t)$ 叫作“先验状态”，更准确的说法应是“对隐藏状态 $z_t$ 的先验分布”
- 本节统一使用 `抽象动作` 表示 `abstract action`，使用 `抽象世界模型` 表示 `abstract world model`

如果再放回动力学语境，这里的先验还不是任意先验，而更接近 `动力学先验`。也就是说，在完整的时序模型里，它更严格地应该写成：

$$
p(z_t \mid z_{t-1}, a_{t-1}) ,
$$

表示根据前一时刻的状态和动作，对当前隐藏状态形成的先验预测。  
为了把方程 `(1)` 讲清楚，文中先写成简化记号 $p(z_t)$；但读的时候要记住，它代表的是“世界模型对当前隐藏状态的先验相信”，不是另一类新的状态对象。

于是模型内部同时需要两类分布：

- $p$：生成模型里的分布，包括先验分布和观测生成分布
- $q$：推断模型里的近似后验分布，也就是“看到数据之后，我对隐藏状态形成的信念分布”

最基本的三个对象是：

- $p(z_t)$：对当前隐藏状态 $z_t$ 的先验分布；在动力学语境下更准确地说，是 $p(z_t \mid z_{t-1}, a_{t-1})$ 这类动力学先验的简写
- $p(o_t \mid z_t)$：给定隐藏状态后，观测如何生成出来
- $q(z_t)$：看到当前观测之后，对同一个隐藏状态 $z_t$ 形成的近似后验

这套 $p/q$ 结构会先出现在方程 `(1)` 里，之后又被带到方程 `(2)` 的未来时刻版本里。

### 2.1.1 What $o_t$ And $z_t$ Mean In This Paper

这里还要把两个最基础的符号落到这篇机器人文章的具体对象上，否则后面的公式会一直显得悬空。

首先，$o_t$ 表示 `observation`，也就是机器人在时刻 $t$ 真正拿到的传感器输入。在这篇文章里，作者定义得很具体：$o_t$ 就是相机图像。因此，最直接地说，

$$
o_t \approx \text{当前摄像头看到的图像。}
$$

它是高维的、带噪声的，而且往往是不完整的。比如锅盖盖着时，相机可以看到锅盖本身，却看不到锅里到底有没有球。所以观测不是世界本身，而只是世界在传感器上的投影。

其次，$z_t$ 表示 `hidden state`，也就是模型内部推断出来的隐藏状态。它不是传感器直接给你的数据，而是模型根据当前观测、过去观测和过去动作，在内部形成的状态表示。它的作用是：把高维观测压缩成一个更适合解释、预测和规划的内部变量。

所以这两个量的关系可以先用一句最直白的话记住：

- $o_t$ 是“机器人真的看到了什么”
- $z_t$ 是“模型据此认为当前局面是什么样”

这也是为什么不能直接把 $o_t$ 当成状态。图像虽然信息很多，但它太高维、太冗余，而且不一定包含任务真正关心的信息。像“锅里有没有红球”这种任务相关信息，在单帧图像里可能是被遮挡的，但模型仍然需要对这件事形成内部信念，这正是隐藏状态 $z_t$ 存在的意义。

在这篇文章里，$z_t$ 还不是单层变量，而是被拆成了慢层和快层：

$$
z_t = \{ z_t^s, z_t^f \} .
$$

这里可以先作如下区分：

- $z_t^s$ 是慢状态，承载任务级、阶段级的信息，比如物体大概在哪里、锅盖是否已经打开、任务是否推进到了下一阶段
- $z_t^f$ 是快状态，承载瞬时、局部、短时变化，比如机械臂运动细节或图像里的短时变化

因此，在这篇文章里，$o_t$ 和 $z_t$ 的关系不是“两个不同的观测变量”，而是：

$$
\text{观测 } o_t \;\longrightarrow\; \text{推断隐藏状态 } z_t \;\longrightarrow\; \text{用 } z_t \text{ 做预测和规划。}
$$

后面再看到方程 `(1)` 和 `(2)` 时，就可以始终按这个口径去读：

- 观测项讨论的是模型如何解释图像 $o_t$
- 状态项讨论的是模型如何推断和更新内部状态 $z_t$

### 2.2 What ELBO Is, And Why It Appears Here

这里先补一个基础概念：`ELBO` 是 `evidence lower bound` 的缩写，中文通常叫“证据下界”。

这里的 `evidence` 指的是边缘似然，也就是当前观测在模型下出现的概率：

$$
p(o_t) = \int p(o_t, z_t)\,dz_t = \int p(o_t \mid z_t)p(z_t)\,dz_t .
$$

这个量重要，是因为它直接衡量模型是不是能解释当前观测；但它通常不好直接算，因为要把所有可能的隐藏状态都积分掉。

接下来最关键的一步，不是“突然引入 `ELBO`”，而是先从一个恒等式开始。由贝叶斯公式：

$$
p(z_t \mid o_t) = \frac{p(o_t, z_t)}{p(o_t)} ,
$$

取对数后可得：

$$
\log p(z_t \mid o_t) = \log p(o_t, z_t) - \log p(o_t) .
$$

移项之后就是：

$$
\log p(o_t) = \log p(o_t, z_t) - \log p(z_t \mid o_t) .
$$

这一步对任意具体的 $z_t$ 都成立。由于左边与 $z_t$ 无关，我们可以对任意分布 $q(z_t)$ 取期望：

$$
\log p(o_t)
=
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t, z_t) - \log p(z_t \mid o_t)
\big] .
$$

接着做变分法里最常见的一步：在括号里加上又减去同一个量 $\log q(z_t)$：

$$
\log p(o_t)
=
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t, z_t) - \log q(z_t)
\big]
+
\mathbb{E}_{q(z_t)}
\big[
\log q(z_t) - \log p(z_t \mid o_t)
\big] .
$$

第二项正好就是 KL 散度：

$$
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t \mid o_t)
\big)
=
\mathbb{E}_{q(z_t)}
\big[
\log q(z_t) - \log p(z_t \mid o_t)
\big] .
$$

因此，$\log p(o_t)$ 就可以被精确地写成：

$$
\log p(o_t)
=
\underbrace{
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t, z_t) - \log q(z_t)
\big]
}_{\mathcal{L}(q)}

+
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t \mid o_t)
\big) .
$$

这里要特别强调：这一步还是**恒等式**，不是近似，也不是下界。下界是下一步才出现的。

这里的

$$
\mathcal{L}(q)
=
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t, z_t) - \log q(z_t)
\big]
$$

就叫 `ELBO`。因为后面那项 KL 散度总是非负的，所以必然有：

$$
\mathcal{L}(q) \le \log p(o_t) .
$$

也就是说，`ELBO` 是对 `log evidence` 的一个下界。  
而 `variational free energy` 则正好定义成它的相反数：

$$
\mathcal{F}(t) = -\mathcal{L}(q) .
$$

所以“最小化 free energy”和“最大化 `ELBO`”其实只是同一件事的两种写法，因为两者只差一个负号。

但为什么“最大化 `ELBO`”又能被理解成“让模型更好地解释当前观测”？这里最好再拆成三步。

第一步，`ELBO` 越大，说明它作为

$$
\log p(o_t)
$$

的下界被抬得越高了。由于

$$
\log p(o_t)
=
\mathcal{L}(q)
+
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t \mid o_t)
\big) ,
$$

提高 `ELBO` 就是在尽量缩小“当前可计算下界”和“真实对数证据”之间的差距。

第二步，

$$
\log p(o_t)
$$

本身表示的是：当前观测 $o_t$ 在模型下到底有多可能出现。  
如果这个量越大，就说明模型给当前观测分配的概率越高，也就是模型越能把当前观测当成“合理会出现的数据”，而不是异常数据。

第三步，最大化 `ELBO` 不只是提高数据在模型下的概率，还会同时压缩

$$
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t \mid o_t)
\big) ,
$$

也就是让近似后验 $q(z_t)$ 更接近真实后验 $p(z_t \mid o_t)$。这意味着模型不仅要“把观测解释过去”，还要用一个更合理的隐藏状态分布来解释它。

所以更完整的说法应该是：

当你最小化 free energy 时，你等价于在最大化 `ELBO`；而最大化 `ELBO` 的作用，一方面是提升模型对当前观测的解释能力，另一方面是让近似后验更贴近真实后验。

### 2.2.1 Why The Negative ELBO Is Called Free Energy

这里还要补一个容易被忽略的问题：为什么 $-\mathrm{ELBO}$ 可以被叫作 `free energy`？这不是随便借一个物理词，而是因为它和统计物理里的变分自由能在数学结构上是同构的。

在统计物理里，Helmholtz 自由能写成

$$
F = U - TS ,
$$

也可以写成

$$
F = -\beta^{-1}\log Z ,
\qquad
\beta = \frac{1}{k_B T} .
$$

这里最好先把三个量分开：

- $U$ 是内能，也就是系统平均携带的总能量
- $S$ 是熵，衡量的是给定宏观状态下，系统有多少微观实现方式
- $F$ 是自由能，用来在固定温度下比较不同宏观状态谁更占优：内能更低会压低 $F$，熵更大也会压低 $F$，因此 $F$ 更小的状态在该温度下通常更稳定、也更容易出现

所以自由能不是另一种独立能量，而是一个把“降低内能”和“增加熵”这两种倾向合并起来的综合比较量。

这里的核心思想是：系统不仅要降低能量，还会受到熵项影响，所以平衡态不是单纯最低能量态，而是自由能最小的状态。

这一点可以从“系统 + 热浴”的总熵来线性推出。固定温度的情形下，真正被优化的不是系统单独的 $U$，而是系统与热浴合起来的总熵：

$$
S_{\mathrm{tot}} = S_{\mathrm{sys}} + S_{\mathrm{bath}} .
$$

这里要特别说明符号，避免和前面变分推断里的小写 $q(\cdot)$ 混淆：

- 大写 $Q$ 表示热量，也就是系统与热浴之间通过热交换传递的能量
- 小写 $q(\cdot)$ 表示概率分布，是前面变分推断里的近似后验

如果系统从热浴吸收一点能量 $\delta U$，那么热浴就损失同样多的能量。对一个温度固定、足够大的热浴来说，可逆热交换满足

$$
\delta S_{\mathrm{bath}}
=
\frac{\delta Q_{\mathrm{bath}}}{T}
=
-\frac{\delta U}{T} .
$$

其中

$$
\delta Q_{\mathrm{bath}}
$$

表示“流入热浴的微小热量”。如果系统从热浴吸收能量，那么热浴这边得到的热量就是负的。

这里负号的原因是：

$$
\delta Q_{\mathrm{bath}} = -\delta U ,
$$

也就是系统得到多少能量，热浴就失去多少能量。

因此，总熵变化可以写成

$$
\delta S_{\mathrm{tot}}
=
\delta S_{\mathrm{sys}} - \frac{\delta U}{T} .
$$

两边同乘 $-T$，就得到

$$
-T\,\delta S_{\mathrm{tot}}
=
\delta U - T\,\delta S_{\mathrm{sys}}
=
\delta F .
$$

所以在固定温度下：

- 总熵增加，对应 $\delta S_{\mathrm{tot}} > 0$
- 自由能降低，对应 $\delta F < 0$

这就是为什么热平衡问题最后会落到最小化

$$
F = U - TS
$$

而不是单纯最小化 $U$。

也正因为如此，“熵越大，自由能越小”这句话要放在固定温度和其他条件不剧烈变化的前提下理解。对同一个能量水平来说，如果某个宏观状态对应更多微观实现方式，那么它的熵更大，于是

$$
-TS
$$

这一项更负，自由能就更低。

同样地，低内能也会压低自由能，但这里最好不要只说“低能量更便宜”，而要说得更具体一些。  
如果系统和一个温度固定的热浴接触，那么系统进入某个能量较高的状态，意味着它需要从热浴中占用更多能量；而热浴失去能量后，热浴熵会下降更多。因此，高能量状态会对“系统 + 热浴”的总熵造成更大惩罚；反过来，低能量状态对应的热浴熵损失更小，所以在平衡下具有更高的统计权重。

这一点在概率上可以直接写成 Boltzmann 权重。对某个微观状态 $i$，

$$
P(i) \propto e^{-\beta E_i} .
$$

对某个宏观状态 $m$，如果它有 $\Omega_m$ 个微观实现方式、平均能量是 $U_m$，那么它的平衡权重可以写成

$$
P(m) \propto \Omega_m e^{-\beta U_m} .
$$

再利用

$$
S_m = k_B \ln \Omega_m ,
$$

就得到

$$
P(m) \propto e^{-\beta F_m} ,
\qquad
F_m = U_m - T S_m .
$$

所以这里要注意：$F_m$ 并不等于 $P(m)$，它们不是同一个量；但在固定温度下，两者是单调对应的。更准确地说：

- $F_m$ 是比较宏观状态 $m$ 是否占优的综合量
- $P(m)$ 是这个宏观状态真正出现的平衡概率

因此，在固定温度下，最小化 $F_m$ 等价于最大化 $P(m)$，但这并不意味着它们数值相等。更稳妥的理解是：$F_m$ 把内能和熵对平衡占优性的共同作用压缩到了一个量里。

#### State Weighting vs Process Direction

这里还要特别区分两个很容易混在一起的语境：

1. 平衡态的权重比较
2. 非平衡过程的能量流动

前面写

$$
P(m) \propto e^{-\beta F_m}
$$

时，讨论的是第一种语境，也就是：

“在固定温度下，不同宏观状态谁在平衡时更占优？”

这时说“高能量状态会让热浴熵更低”，意思不是系统真的正在发生某个过程，而是在比较不同候选状态对应的总统计权重。系统如果处在更高能的状态，就意味着热浴可用能量更少，因此“系统 + 热浴”整体可实现的微观方式更少，这个状态的平衡权重也就更低。

而当我们写

$$
\Delta S_{\mathrm{bath}} = -\frac{\Delta U}{T}
$$

时，讨论的是第二种语境，也就是：

“如果系统真的从一个状态演化到另一个状态，能量在系统和热浴之间怎样流动？”

这时它描述的是过程方向：如果系统内能下降，并把能量释放给热浴，那么热浴熵会上升；如果系统从热浴吸收能量、内能上升，那么热浴熵就会下降。

所以这两种说法并不矛盾，只是在回答不同问题：

- 平衡态权重比较：为什么高内能状态统计上不占优
- 过程方向描述：当系统能量真的变化时，热浴熵如何随之变化

把这两层分开之后，前面的几种表述就可以统一起来：  
高内能状态之所以在平衡上不占优，是因为它对应更低的热浴熵；而系统从高内能态向低内能态松弛时，则会把能量释放给热浴，从而使热浴熵上升。

但如果比较的是不同温度下的同一个系统，要再小心一点。温度降低时，熵项前面的权重 $T$ 会减小，同时系统通常也更难进入高能激发态，因此常见情况是：

- 内能 $U$ 下降
- 熵 $S$ 也下降，因为可访问微观状态变少
- 自由能 $F$ 逐渐趋近于基态能量

所以低温通常不是“熵变大”，更常见的是相反：系统可访问的可能性收缩，熵也随之减小。固定温度下比较不同状态，和改变温度看同一个系统的演化，是两种不同的比较问题。

如果进一步引入一个试探分布 $q(x)$ 来近似系统状态，那么物理里对应的变分自由能泛函可以写成

$$
\mathcal{F}[q]
=
\mathbb{E}_q[E(x)] - T S[q] .
$$

把熵写成

$$
S[q] = -k_B \sum_x q(x)\log q(x)
$$

之后，这个式子就会变成“能量项 + 一个由 $\log q$ 给出的熵项”的结构。

变分推断里发生的事非常类似，只不过这里的“能量”不再是真实物理能量，而是负对数概率。更具体地说，可以把

$$
E(z) \;\longleftrightarrow\; -\log p(o_t, z_t)
$$

看成一个对应关系。于是

$$
\mathbb{E}_{q(z_t)}[-\log p(o_t, z_t)]
+
\mathbb{E}_{q(z_t)}[\log q(z_t)]
$$

就扮演了“能量项减熵项”的角色。而这正好就是

$$
-\mathcal{L}(q) = -\mathrm{ELBO} .
$$

所以这里叫 `variational free energy`，不是因为模型真的在求一个热力学系统的物理自由能，而是因为这个目标函数和统计物理里的变分自由能泛函具有同样的数学结构。

更准确地说，在机器学习里：

- “能量”通常对应负对数联合概率 $-\log p(o_t, z_t)$
- “熵”对应近似后验分布 $q(z_t)$ 的熵
- “配分函数”对应边缘似然或 evidence

因此，这里的 `free energy` 更像是一个统计推断意义上的自由能，而不是直接的物理自由能。它保留了物理上的变分结构，但语境已经从热平衡系统变成了概率模型。

所以最稳的总结是：

`negative ELBO` 之所以叫 `free energy`，不是纯借词，而是因为它与统计物理里的变分自由能在数学形式上同构；只是到了机器学习里，能量被替换成了负对数概率，熵由近似后验分布给出。

### 2.3 How Equation (1) Is Obtained

原文的方程 `(1)` 是：

$$
\mathcal{F}(t)
=
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t)
\big)
-
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t \mid z_t)
\big]
\ge -\log p(o_t) .
$$

它之所以自然拆成两部分，不是作者随便拆的，而是因为联合分布本来就写成：

$$
p(o_t, z_t) = p(o_t \mid z_t)p(z_t) .
$$

把它代进 $-\mathcal{L}(q)$，就会自动得到：

$$
\mathcal{F}(t)
=
\mathbb{E}_{q(z_t)}
\big[
\log q(z_t) - \log p(o_t, z_t)
\big]
$$

$$
=
\mathbb{E}_{q(z_t)}
\big[
\log q(z_t) - \log p(z_t) - \log p(o_t \mid z_t)
\big]
$$

$$
=
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t)
\big)
-
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t \mid z_t)
\big] .
$$

### 2.4 How To Read The Two Parts Of Equation (1)

这一节最好和前面的物理解释连起来看。前面说变分自由能有“能量项减熵项”的结构；方程 `(1)` 并不是突然换了一套目标，而是把同一个结构在概率模型里进一步展开后的结果。

从前面的写法出发，

$$
\mathcal{F}(t)
=
\mathbb{E}_{q(z_t)}
\big[
-\log p(o_t, z_t)
\big]
+
\mathbb{E}_{q(z_t)}
\big[
\log q(z_t)
\big] .
$$

如果再把联合分布拆成

$$
p(o_t, z_t)=p(o_t\mid z_t)p(z_t),
$$

那么就得到

$$
\mathcal{F}(t)
=
\mathbb{E}_{q(z_t)}
\big[
-\log p(z_t)
\big]
+
\mathbb{E}_{q(z_t)}
\big[
\log q(z_t)
\big]
+
\mathbb{E}_{q(z_t)}
\big[
-\log p(o_t\mid z_t)
\big] .
$$

到这里，前两项会自动合并成

$$
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t)
\big),
$$

于是才变成方程 `(1)` 的标准形式。也就是说，方程 `(1)` 的两部分并不是两块互不相关的新对象，而是：

1. 前面“能量项减熵项”结构里，和先验分布有关的部分，被压缩成了一个 KL 项  
2. 和当前观测拟合有关的部分，则保留下来变成了观测项

因此，第一部分

$$
D_{\mathrm{KL}}
\big(
q(z_t)\,\|\,p(z_t)
\big)
$$

更准确地说，不只是一个抽象的 regularizer，而是“先验能量项”和“后验熵项”合并之后的结果。它在问：

“为了解释当前观测，你形成的后验分布 $q(z_t)$，有没有离模型自身动力学给出的先验分布 $p(z_t)$ 太远？”

如果这个项很大，说明模型虽然可能在强行解释当前观测，但这种解释和它原本根据动力学预测出来的状态信念差得太多。

第二部分

$$
-
\mathbb{E}_{q(z_t)}
\big[
\log p(o_t \mid z_t)
\big]
$$

则对应观测拟合项。它在问：

“在你当前相信的隐藏状态分布下，当前观测到底能不能被解释好？”

如果这个项很大，说明当前隐藏状态对观测解释得不够好。

所以方程 `(1)` 最好不要读成“一个 KL 项加一个 reconstruction 项”这么扁平，而要读成：

`这是同一个 free-energy 结构在概率模型里的展开：一边要求后验分布不要脱离动力学先验太远，一边要求当前观测能够被解释好。`

这两项目标并不是逻辑上天然对立的，因为它们都希望变小；但在真实优化里，它们经常会形成拉扯。最典型的情况是：当前观测在动力学先验下看起来并不典型，这时如果模型想把观测解释好，就往往需要让后验分布明显偏离先验分布。

这也是为什么它对应的是 `perception`。它本质上在做当前时刻的状态推断，而不是未来动作规划。

### 2.5 Why Equation (1) Is An Upper Bound On Surprise

原文还写了：

$$
\mathcal{F}(t) \ge -\log p(o_t) .
$$

这一步的含义是：真正理想的目标其实是让观测不那么“令人意外”，也就是减小 surprise：

$$
-\log p(o_t) .
$$

但这个量通常不好直接算，所以转而最小化它的一个 tractable upper bound，也就是 `variational free energy`。

所以这里的 free energy 可以理解成一个“可计算代理目标”：它不直接等于 surprise，但你把它压低，通常就会让模型更能解释当前观测。

### 2.6 How To Read Equation (2)

方程 `(2)` 开始从当前时刻走向未来。它不再问“我现在处在什么状态”，而是在问：

“如果我执行某条未来动作序列 $\pi$，这个选择到底值不值得？”

原文的方程 `(2)` 是：

$$
\mathcal{G}(\tau)
\approx
-
\underbrace{
\mathbb{E}_{q(o_\tau, z_\tau \mid \pi)}
\big[
\log q(z_\tau \mid o_\tau, \pi)
-
\log q(z_\tau \mid \pi)
\big]
}_{\text{epistemic value}}
-
\underbrace{
\mathbb{E}_{q(o_\tau \mid \pi)}
\big[
\log p(o_\tau \mid o_{\mathrm{pref}})
\big]
}_{\text{extrinsic value}} .
$$

这里最关键的转折是：到了未来时刻 $\tau > t$，你还没有真的看到未来观测 $o_\tau$。所以你不能像方程 `(1)` 那样直接根据真实未来数据做推断，只能根据当前 world model 去预测：

- 如果我执行 policy $\pi$
- 未来可能处在什么状态
- 未来可能看到什么观测

然后对这些未来可能性做期望。这就是为什么它叫 `expected free energy`。

### 2.7 What The Two q Terms In Equation (2) Mean

方程 `(2)` 第一项里最容易让人混淆的是这两个分布：

$$
q(z_\tau \mid \pi)
\qquad \text{and} \qquad
q(z_\tau \mid o_\tau, \pi) .
$$

它们的区别非常关键。

$q(z_\tau \mid \pi)$ 是 future prior belief。  
意思是：如果我现在决定执行 policy $\pi$，但还没真的看到未来观测，那我对未来隐藏状态的先验相信是什么。

$q(z_\tau \mid o_\tau, \pi)$ 是 future posterior belief。  
意思是：如果我执行了 policy $\pi$，并且真的看到了未来观测 $o_\tau$，那时我对未来隐藏状态的后验相信会变成什么。

所以它们的差值

$$
\log q(z_\tau \mid o_\tau, \pi)
-
\log q(z_\tau \mid \pi)
$$

衡量的其实就是：

未来观测 $o_\tau$ 到底会让我的状态信念改变多少。

如果一个动作导致未来观测非常有信息量，使得 posterior 相比 prior 变化很大，那说明这个动作能显著减少不确定性。把这件事再对未来可能的 $(o_\tau, z_\tau)$ 做期望，就得到 `epistemic value`。

如果要更正式地说，这一项等价于在给定 policy $\pi$ 时，未来观测 $o_\tau$ 和未来隐藏状态 $z_\tau$ 之间的 `条件互信息`：

$$
I_q(z_\tau; o_\tau \mid \pi)
=
\mathbb E_{q(o_\tau, z_\tau \mid \pi)}
\Big[
\log q(z_\tau \mid o_\tau, \pi)
-
\log q(z_\tau \mid \pi)
\Big] .
$$

这里的 `互信息` 不是又一个神秘新对象，它只是用来测量：

知道未来观测 $o_\tau$ 之后，我对未来隐藏状态 $z_\tau$ 的不确定性，平均来说会减少多少。

所以它也可以改写成更直观的熵差形式：

$$
I_q(z_\tau; o_\tau \mid \pi)
=
H_q(z_\tau \mid \pi)
-
\mathbb E_{q(o_\tau \mid \pi)}
H_q(z_\tau \mid o_\tau, \pi) .
$$

这条式子的读法非常直接：

- $H_q(z_\tau \mid \pi)$ 是在还没看到未来观测之前，我对未来隐藏状态有多不确定
- $H_q(z_\tau \mid o_\tau, \pi)$ 是看到未来观测之后，这种不确定性还剩多少
- 两者的差，就是这个动作预期能带来的平均信息增益

因此，在这篇文章里，`epistemic value` 最准确的理解不是抽象的“好奇心”，而是：

执行这个动作后，我预期会获得多少关于隐藏状态的新信息。

### 2.8 What The p Term In Equation (2) Means

第二项里的

$$
p(o_\tau \mid o_{\mathrm{pref}})
$$

不是 world model 里的观测生成分布，而是 preference distribution。它编码的是：

什么样的未来观测，是我想看到的。

也就是说，这里的 $p$ 扮演的是 goal template 的角色。  
如果某个未来观测更接近目标偏好 $o_{\mathrm{pref}}$，那它在这个偏好分布下的概率就更高，对应的 `extrinsic value` 就更好。

所以方程 `(2)` 的两项分工非常清楚：

- 第一项看信息增益，鼓励 exploration
- 第二项看目标一致性，鼓励 goal achievement

### 2.9 Are The q And p In Equation (2) Obtained From Equation (1)

严格说，不是“从方程 `(1)` 里直接算出来”的；更准确的说法是：

方程 `(1)` 用来训练和约束 world model，使模型学会了这些 $q$ 和 $p$ 结构；方程 `(2)` 再调用这些已经学到的分布，去评估未来动作。

也就是说，逻辑顺序是：

1. 先通过 `variational free energy` 学会当前状态推断和生成结构
2. 再在这个已经学好的 world model 上，对未来 policy 计算 `expected free energy`

所以你说“它是不是要算两步”，答案是：概念上是的。

- 第一步：根据当前观测推断当前隐藏状态
- 第二步：基于当前隐藏状态和 world model，想象未来并评估动作

而在这篇文章的具体实现里，这两步又被工程化成：

- world model 负责当前状态推断和局部动力学
- abstract world model 负责快速预测抽象动作下的未来慢状态

### 2.10 Method Part I: How To Read The Framework

如果按照线性逻辑来读这篇文章，先讲 `Eq. (1)` 和 `Eq. (2)` 会更顺。因为到这一步，读者已经知道：

- 方程 `(1)` 在做当前状态推断
- 方程 `(2)` 在做未来动作评价
- 真正的问题是：这些量在真实机器人上怎么才能算得动

于是 `Framework` 这一节的任务就不再是“先把三个模块名字列出来”，而是回答：

`这篇文章到底用什么工程结构，把前面那套 active inference 目标变成了一个能在线运行的控制系统。`

这里先把两张图的角色固定下来，避免后面重复：

- `Fig. 1` 是整个方法的总流程图，回答的是：`这套系统一共有哪些模块，数据怎样从左流到右`
- `Fig. 2` 不是另一张独立总览图，而是 `Fig. 1` 左侧 `world model` 模块的放大图，回答的是：`这个 world model 内部到底怎样表示快慢两种时间尺度`

所以这两张图不是并列关系，而是：

$$
\text{Fig. 1: 整体框架}
\;\longrightarrow\;
\text{Fig. 2: 对其中 world model 的内部展开}
$$

#### Fig. 1 Gives The Whole Method In One Pass

![Framework overview](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-02-figure-01.jpg)

如果只看 `Fig. 1`，整篇文章的方法其实已经可以压成一条非常清楚的线：

1. 当前观测 $o_t$ 进入 `world model`
2. `world model` 根据观测和动作，推断当前的层级隐藏状态 $z_t^s, z_t^f$
3. `action model` 把一段低层动作序列压成一个抽象动作 $A_t$
4. `abstract world model` 用“当前隐藏状态 + 抽象动作”来预测未来的慢状态
5. 系统在抽象动作空间里比较 future outcomes，而不再直接在原始连续动作空间里暴力搜索

换句话说，`Fig. 1` 讲的不是三个彼此独立的模型，而是一条顺序明确的计算链：

$$
\text{观测}
\;\longrightarrow\;
\text{当前状态表征}
\;\longrightarrow\;
\text{动作抽象}
\;\longrightarrow\;
\text{未来慢状态预测}
\;\longrightarrow\;
\text{在抽象层上做动作选择}
$$

这也是为什么这篇文章的方法不能简单总结成“用了 world model”。真正的方法动作是：作者把 active inference 原本难以计算的动作搜索问题，拆成了三个更可控的子问题。

#### Fig. 1 Left: World Model Solves Representation

`Fig. 1` 左边的 `world model` 接收的是当前观测 $o_t$、历史动作和历史隐藏状态，输出的是当前时刻的层级隐藏状态 $z_t^s, z_t^f$。它在整个框架里的任务不是直接产出动作，而是先回答一个更基础的问题：

`机器人现在到底处在什么局面里。`

这里最关键的是，作者没有把“当前局面”压成单一 latent，而是从一开始就分成慢层和快层。直觉上：

- 慢层承载的是任务级、阶段级信息，比如物体的大致配置、任务是否推进到下一阶段
- 快层承载的是瞬时、局部、短时变化，比如机械臂运动细节和图像短时变化

因此，`world model` 在这篇文章里的角色，不是一个泛泛的环境模拟器，而是一个带时间层级的状态表示器。它先把“当前世界是什么样”这件事表示好，后面的规划才有稳定的起点。

#### Fig. 1 Middle: Action Model Solves Action-Space Tractability

`Fig. 1` 中间的 `action model` 看起来只是一个压缩器，但它在方法里承担的是第二个关键任务：把原始动作空间变成可规划的抽象动作空间。

它做的事可以线性地理解成：

1. 取一段固定长度的真实动作序列
2. 把这段动作序列编码成一个低维表示
3. 再把它量化成少量离散 code，得到抽象动作 $A_t$
4. 必要时，还能把这个抽象动作再 decode 回具体动作序列

这一步的重要性在于，它把“连续控制信号”变成了“可枚举的行为单元”。于是系统后面不必再直接比较海量连续动作序列，而可以比较有限个抽象动作候选。

所以这里的 `abstract action` 最好不要理解成语言级或语义级的“抽象概念”，而应理解成：

`一个代表整段低层动作序列的离散行为 code。`

#### Fig. 1 Right: Abstract World Model Solves Planning-Space Tractability

`Fig. 1` 右边的 `abstract world model` 是整个框架里最像“工程接口”的部分。它不再逐步滚动完整世界模型，而是直接做一件更便宜的事：

`给定当前隐藏状态和一个抽象动作，直接预测 h 步之后的慢状态会变成什么。`

从图上看，它接收的是：

- 当前慢层和快层状态
- 一个抽象动作 $A_t$

输出的是：

- 未来的慢确定性状态 $d_{t+h}^s$

这里有一个非常重要的限制：它并不试图预测完整未来观测，也不试图在原始时间尺度上逐步 rollout 全部细节。它只预测规划真正需要的那部分低频结构，也就是未来慢状态。

因此，`abstract world model` 的作用不是替代 `world model`，而是：

`在已经学到状态表示和动作抽象之后，再提供一个低成本的未来慢变量预测器。`

这一步正是整篇文章把 `EFE` 变得 tractable 的关键。

#### Fig. 1 As A Whole: The Three Modules Solve Three Different Bottlenecks

把 `Fig. 1` 整体再压一次，会更清楚它为什么不是“堆三个网络”：

- `world model` 解决的是表示问题：怎样把高维观测压成适合推断和预测的层级状态
- `action model` 解决的是动作空间问题：怎样把连续动作序列压成可枚举的抽象动作
- `abstract world model` 解决的是规划空间问题：怎样在不做昂贵 rollout 的情况下评估未来结果

所以这篇文章的方法真正可以概括成：

`先把世界表示到一个带时间层级的状态空间，再把动作压成抽象行为单元，最后只在慢变量层上做未来预测和动作比较。`

#### Fig. 2 Explains Why The World Model Is Not A Single Latent State

![World model with temporal hierarchy](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-02-figure-03.jpg)

如果说 `Fig. 1` 告诉你整个框架怎么分工，那么 `Fig. 2` 真正补上的，是左侧 `world model` 为什么必须做成分层时间结构。

这张图最重要的信息不是“又有很多变量”，而是：

`world model` 里的状态本身就是分层的，而且每一层又分成 deterministic part 和 stochastic part。

也就是说，这篇文章不是只用一个 $z_t$ 来吃掉所有动态，而是把它拆成：

$$
z_t^s = \{ d_t^s, s_t^s \}, \qquad
z_t^f = \{ d_t^f, s_t^f \}.
$$

你可以把这四类量先粗略理解成：

- $d_t^s$：慢层确定性状态，承载较稳定的任务级演化主线
- $s_t^s$：慢层随机状态，承载慢层里的不确定性
- $d_t^f$：快层确定性状态，承载局部、短时、连续变化
- $s_t^f$：快层随机状态，承载快层里的不确定性

所以 `Fig. 2` 想说明的不是“world model 更复杂”，而是：

`真实机器人环境里，快变化和慢变化不能混在同一个状态里，否则既不利于表示，也不利于后面的抽象规划。`

#### How Fig. 1 And Fig. 2 Fit Together

现在可以把两张图合并成一条真正线性的读法：

1. `Fig. 1` 先给出整体框架：`world model -> action model -> abstract world model`
2. `Fig. 2` 再放大解释第一个模块：`world model` 为什么必须有 `slow/fast` 两层
3. 因为 `world model` 已经把当前局面表示成层级状态，所以 `action model` 才有稳定的状态上下文
4. 因为动作已经被压成抽象动作，所以 `abstract world model` 才能在较低成本下预测未来慢状态
5. 因为未来慢状态变得可预测，所以后面的 `EFE` 才能在抽象动作层上真正算起来

因此，`Framework` 这一小节真正要保留的是：

`这篇文章先用 Fig. 1 给出一条从观测到抽象规划的完整数据流，再用 Fig. 2 解释这条数据流左端的状态表示为什么必须是时序分层的。`

### 2.11 What Equation (4) Is Really Doing

如果说 `Fig. 1` 和 `Fig. 2` 只是把模块关系和状态分层画出来，那么 `Eq. (4)` 才真正规定了：

`这些 slow/fast、deterministic/stochastic 变量各自要学什么。`

原文把 world model 的训练目标写成：

$$
\mathcal {F} (t) = \mathcal {F} _ {\mathrm {s}} (t) + \mathcal {F} _ {\mathrm {f}} (t) - \log p _ {\theta} \left(o _ {t} \mid z _ {t} ^ {\mathrm {s}}\right).
$$

最直接的读法是：这篇文章不是只训练一个统一的 world model loss，而是同时给

- 慢层一个目标
- 快层一个目标
- 再额外给慢层一个辅助约束

所以 `Eq. (4)` 最好拆成三部分来看。

#### First: Why The Loss Is Split Into Slow And Fast Parts

原文在写 `Eq. (4)` 之前，先给了一个很关键的解释：快层确定性状态 $d_t^f$ 可以被看成慢层的“观测”。它的意思是：

- 对快层来说，真正要解释的是原始观测 $o_t$
- 对慢层来说，它不直接追图像，而是先追快层里更局部、更细节的主干状态 $d_t^f$

所以 world model 的训练不是“所有层一起直接拟合同一张图”，而是一个层级结构：

$$
\text{slow layer}
\;\longrightarrow\;
d_t^f
\;\longrightarrow\;
o_t.
$$

这也解释了为什么他们把变分自由能拆成 $\mathcal F_s(t)$ 和 $\mathcal F_f(t)$ 两部分。它不是数学上的任意拆分，而是在明确指定：

- 慢层负责更长期、更概括的状态主干
- 快层负责更贴近图像观测的局部细节

#### Second: What The Slow-Layer Loss $\mathcal F_s(t)$ Means

原文写的是：

$$
\mathcal {F} _ {\mathrm {s}} (t)
=
D _ {\mathrm {K L}} \!\left[
\operatorname {sg} \!\left(q _ {\theta} ^ {\mathrm {s}} \left(s _ {t} ^ {\mathrm {s}} \mid d _ {t} ^ {\mathrm {s}}, d _ {t - 1} ^ {\mathrm {f}}\right)\right)
\;\middle\|\;
p _ {\theta} ^ {\mathrm {s}} \left(s _ {t} ^ {\mathrm {s}} \mid d _ {t} ^ {\mathrm {s}}\right)
\right]
- \log p _ {\theta} (d _ {t} ^ {\mathrm {f}} \mid z _ {t} ^ {\mathrm {s}}).
$$

这两项分别在做两件事。

第一项 `KL` 是在说：

`慢层随机状态的后验，不要偏离慢层自己的先验太远。`

也就是说，慢层不能为了拟合数据而任意漂移，它仍然要服从自己的内部动力学先验。

第二项

$$
- \log p _ {\theta} (d _ {t} ^ {\mathrm {f}} \mid z _ {t} ^ {\mathrm {s}})
$$

是在说：

`慢层状态必须能够预测快层确定性状态。`

这一步很关键，因为它明确把慢层训练成一个更高层、更低频的动力学骨架。慢层不是直接去记图像，而是先去解释“快层主干为什么会是现在这样”。

所以 $\mathcal F_s(t)$ 的真正作用是：

`让慢层既要保持自己的先验结构，又要对快层主干负责。`

#### Third: What The Fast-Layer Loss $\mathcal F_f(t)$ Means

原文写的是：

$$
\mathcal {F} _ {\mathrm {f}} (t)
=
D _ {\mathrm {K L}}
\!\left[
\mathrm {s g} \!\left(q _ {\theta} ^ {\mathrm {f}} (s _ {t} ^ {\mathrm {f}} \mid d _ {t} ^ {\mathrm {f}}, o _ {t})\right)
\;\middle\|\;
p _ {\theta} ^ {\mathrm {f}} (s _ {t} ^ {\mathrm {f}} \mid d _ {t} ^ {\mathrm {f}})
\right]
- \log p _ {\theta} \left(o _ {t} \mid z _ {t}\right).
$$

这里的逻辑就更贴近标准 latent world model 了。

第一项 `KL` 表示：

`快层随机状态的后验，也不能脱离快层自己的先验太远。`

第二项

$$
- \log p_\theta(o_t \mid z_t)
$$

表示：

完整隐藏状态 $z_t$ 必须能够解释当前观测 $o_t$。

也就是说，快层在这里承担的是更贴近观测的建模任务。它吸收图像中的局部、短时、细节性变化，并把这些变化和完整隐藏状态连起来。

所以 $\mathcal F_f(t)$ 的真正作用是：

`让快层既服从自己的局部动力学先验，又要把当前图像解释好。`

#### Fourth: Why There Is An Extra $-\log p_\theta(o_t \mid z_t^s)$ Term

这一项特别值得单独拎出来，因为它不是把 `Eq. (1)` 直接照搬到层级 world model 里就会自然出现的项。

它的作用是：

`逼着慢层单独也保留足够的信息，不至于完全依赖快层才能解释观测。`

如果没有这一项，很容易出现一种退化：

- 快层把所有和图像有关的信息都学走
- 慢层只变成一个很弱的高层辅助变量
- 后面再拿慢层去做抽象规划时，慢层本身却不够有内容

所以作者专门加上

$$
- \log p _ {\theta} \left(o _ {t} \mid z _ {t} ^ {\mathrm {s}}\right)
$$

作为辅助约束，目的就是让慢层本身也具备解释观测的能力。这样慢层才更像一个真正可用于 coarse-grained planning 的状态，而不是装饰性的高层 latent。

#### What Equation (4) Ultimately Assigns To The Four State Pieces

现在再回头看

$$
z_t^s = \{ d_t^s, s_t^s \}, \qquad
z_t^f = \{ d_t^f, s_t^f \},
$$

`Eq. (4)` 实际上已经把这四块的功能定得很清楚：

- $d_t^s$：慢层确定性主干，承载长期、稳定、任务级的演化
- $s_t^s$：慢层随机修正，承载慢层里的不确定性
- $d_t^f$：快层确定性主干，承载局部、短时、连续变化
- $s_t^f$：快层随机修正，承载快层里的不确定性

所以这篇文章不是只在概念上说“我们有 slow/fast、deterministic/stochastic”，而是通过 `Eq. (4)` 真正把训练职责分配给了它们。

#### Two Small Engineering Details: `sg` And KL Balancing

原文这里还出现了两个很容易被跳过、但其实很重要的工程记号。

第一，`sg` 表示 `stop-gradient`。  
它的作用不是改数学定义，而是控制梯度流向，避免 posterior 和 prior 在训练时互相牵着跑，导致优化不稳定。

第二，作者提到 `KL balancing`，并使用一个权重因子 $w$。  
这也是为了稳定训练：如果 `KL` 项过强，latent 很容易塌缩；如果 `KL` 项过弱，后验又可能完全脱离先验。`KL balancing` 的作用就是让 prior 和 posterior 的对齐更平稳。

所以 `Eq. (4)` 不只是一个概念式子，它已经包含了这篇 world model 真正能训练起来的关键工程处理。

这一整节可以概括为：

`Eq. (4)` 的真正作用，是把这篇文章的层级世界模型从“有四类状态变量的结构图”变成“每一层各自承担不同建模职责的可训练系统”。

### 2.12 How To Read The Action Model

`Action model` 这一小节不能只读成“把动作压缩一下”。它在整篇文章里的真正作用，是把原始连续动作空间改写成一个可枚举、可比较、可用于 `EFE` 计算的抽象动作空间。

#### First: What Goes In, And What Must Come Out

动作模型的输入不是单步动作，而是一整段固定长度的动作序列：

$$
a_{t:t+h}.
$$

在这篇文章里，参数表里明确给了

$$
h = 50,
$$

也就是说，作者不是在学习“一步动作的 embedding”，而是在学习“50 步左右的行为片段表示”。

它最后要产出的，也不是一个连续 latent 而已，而是一个可以被当成 `abstract action` 的量化表示。原文把整个流程写成：

$$
A_t = \mathcal{E}_\phi(a_{t:t+h}),
$$

$$
\hat{A}_t = \mathcal{Q}_\phi(A_t),
$$

$$
\hat{a}_{t:t+h} = \mathcal{D}_\phi(\hat{A}_t). \tag{5}
$$

#### Second: Equation (5) Is A Three-Step Pipeline

第一步：

$$
A_t = \mathcal{E}_\phi(a_{t:t+h})
$$

表示编码器 $\mathcal E_\phi$ 先把一整段真实动作序列压成一个低维连续特征 $A_t$。

这里要先固定一个容易混淆的区分：

- $A_t$ 是连续特征
- $\hat A_t$ 才是量化后的抽象动作

所以后面当论文说“把 feature 当成 abstract action”时，更准确地读，应该是：

真正进入后续规划的是量化后的 $\hat A_t$，而不是未经量化的连续特征 $A_t$。

第二步：

$$
\hat{A}_t = \mathcal{Q}_\phi(A_t)
$$

表示把连续特征 $A_t$ 送进 residual vector quantizer，再把它映射到有限个离散 code 的组合上。

第三步：

$$
\hat{a}_{t:t+h} = \mathcal{D}_\phi(\hat{A}_t)
$$

表示解码器再把量化后的表示 $\hat A_t$ 重构回一段动作序列。  
这一步的作用不是为了部署时一定要重构，而是为了训练时强迫 $\hat A_t$ 保留足够多的动作信息。

所以 `Eq. (5)` 的本质不是普通自编码器，而是：

`把连续动作片段先编码成连续特征，再压到离散 code 上，最后要求这个离散 code 仍然能重构出原来的动作片段。`

#### Third: Why They Use Residual Vector Quantization

论文没有停在“做一次最近邻量化”，而是用了 `residual vector quantization`，并且有

$$
N_q = 2
$$

层 codebook。

每一层 codebook 里有

$$
K
$$

个可学习 code，记作 $\{c_{i,j}\}_{j=1}^K$。  
其中 $i$ 表示第几层量化器，$j$ 表示这一层里的第几个 code。

这里要先把 `codebook` 这个词讲清楚。它指的是一组可学习的向量字典。也就是说，第 $i$ 层的 codebook

$$
C_i = \{c_{i,j}\}_{j=1}^K
$$

包含的是 $K$ 个稠密向量，每个 $c_{i,j}$ 都是一个真正的 learnable code。量化时，模型会从这组候选向量里选出一个最接近当前 residual 的 code，并把这个被选中的 code 当成这一层的量化结果。

所以这里最需要记住的不是编码形式，而是：

- `codebook` 提供一组候选的 learnable vectors
- 每一层量化都会从中选出一个最接近当前 residual 的 code
- 真正进入后续计算的是被选中的稠密向量 $\hat A_{t,i}$

Residual quantization 的逻辑可以直接写成：

1. 第一层先拿整个连续特征 $A_t$ 去找最近的 code，得到 $\hat A_{t,1}$
2. 然后看剩下还没解释掉的残差
3. 第二层再去量化这个残差，得到 $\hat A_{t,2}$
4. 最后把所有量化结果加起来，形成总的量化表示

也就是：

$$
\hat A_t = \sum_{i=1}^{N_q} \hat A_{t,i}.
$$

这样做的意义是：不是要求单个 code 一次性吃掉全部动作信息，而是让多个 code 以“逐层修正残差”的方式共同逼近连续特征。

因此，这里的抽象动作其实不是一个单独标签，而是一个多层 code 组合。  
如果每层有 $K$ 个 code，一共有 $N_q$ 层，那么总候选数就是

$$
K^{N_q}.
$$

这正是后面能枚举多少个 `abstract actions` 的来源。

#### Fourth: Why Equation (6) Has Two Loss Terms

原文把动作模型的训练目标写成：

$$
\mathcal L_\phi
=
\lambda_{\mathrm{MSE}}
\|a_{t:t+h} - \hat a_{t:t+h}\|_2^2
+
\lambda_{\mathrm{commit}}
\sum_{i=1}^{N_q}
\left\|
\bigl(A_t - \text{previous quantized sum}\bigr)
- \operatorname{sg}(c_{i,k})
\right\|_2^2. \tag{6}
$$

第二项是在每一层上，都让“当前还没被量化掉的残差”贴近这一层选中的 code。

所以 `Eq. (6)` 最好拆成两件事。

第一项是 reconstruction loss：

$$
\lambda_{\mathrm{MSE}}
\|a_{t:t+h} - \hat a_{t:t+h}\|_2^2.
$$

它要求量化后的抽象动作 $\hat A_t$ 仍然能重构出原来的动作序列。  
这意味着抽象动作不能只是一个任意离散标签，而必须保留足够多的“如何执行这段行为”的信息。

第二项是 commitment loss。  
在第 $i$ 层量化时，当前真正要被量化的不是原始 $A_t$，而是“还没被前几层 code 解释掉的剩余部分”。把它记成

$$
r_{t,i}
=
A_t - \sum_{j=1}^{i-1} \hat A_{t,j},
\qquad
\hat A_{t,0}=0.
$$

这就是原式里

$$
A_t - \text{previous quantized sum}
$$

真正对应的量。

接着，这一层量化器会从第 $i$ 个 codebook 里选出一个最近的 code，记成

$$
c_{i,k_i}.
$$

于是，第 $i$ 层的 commitment loss 实际上就是：

$$
\left\|r_{t,i} - \operatorname{sg}(c_{i,k_i})\right\|_2^2.
$$

把所有层加起来，才得到原文里的第二项：

$$
\lambda_{\mathrm{commit}}
\sum_{i=1}^{N_q}
\left\|
\bigl(A_t - \text{previous quantized sum}\bigr)
- \operatorname{sg}(c_{i,k})
\right\|_2^2.
$$

这样再读，它的意思就非常具体了：

- $r_{t,i}$ 是第 $i$ 层当前还没被解释掉的连续 residual
- $c_{i,k_i}$ 是这一层最终选中的离散 code
- 这一项要求两者彼此靠近

所以 `commitment loss` 的真正含义不是泛泛的“稳定量化”，而是：

`在每一层上，都要求当前 residual 真正承诺落到它所选择的那个 code 附近。`

如果没有这一项，会很容易发生两种坏事：

- 编码器输出到处漂，但 codebook 跟不上
- 同一个行为片段在不同批次里映到不稳定的 code 上

所以 `commitment loss` 的作用是：让连续特征及其逐层 residual 都真正贴近各自选中的离散 code，从而把动作空间稳定地离散化。

#### Fifth: What $\operatorname{sg}$ Means Here

$$
\operatorname{sg}(\cdot)
$$

它表示 `stop-gradient`。

在这一项里，$\operatorname{sg}(c_{i,k})$ 的意思不是改变数值，而是：

`在这一步损失里，把选中的 code 当成一个常量目标，不让梯度直接通过这里去推动 code 本身。`

这样做的目的是把“让 encoder/residual 靠近 code”和“更新 codebook”这两件事分开处理，避免训练时互相拉扯得太厉害。

原文也明确说，codebook 的学习不是靠这项直接反传，而是通过 `exponential moving averages` 来更新。  
所以这里的训练逻辑是分工的：

- reconstruction + commitment 主要约束 encoder / decoder / quantized representation
- codebook 自身则通过 EMA 稳定更新

#### Sixth: Why This Model Is Exactly What The Later Planning Needs

到这里，动作模型的作用就可以说得非常清楚了。

它不是为了“压缩动作好看一点”，而是在构造一个介于连续控制和高层规划之间的中间层：

- 输入仍然是低层真实动作序列
- 中间变成可枚举的离散 code 组合
- 输出还保留成可执行的动作序列

所以它做出的不是语义标签，而是一种：

`可重构、可枚举、可用于规划的动作片段表示。`

这也是为什么后面 abstract world model 可以直接对所有候选 $\{\hat A_n\}$ 做未来状态预测。  
因为现在动作空间不再是无限连续的，而是被动作模型改写成了有限个 code 组合。

#### What To Retain From The Action Model

这一小节的最短结论是：

`Action model` 的真正贡献，不是“把动作嵌入成 latent”，而是通过 residual vector quantization，把固定长度动作片段变成既能重构、又能枚举、还能直接进入后续 `EFE` 计算的离散 planning unit。

同时，这里也埋下了一个明确限制：

`它依赖固定长度 h 的动作片段。`

这让它在工程上 tractable，但也意味着它默认一个动作单元可以被统一窗长表示；如果真实行为边界是可变长的，那么这种 chunking 可能会切坏自然的技能边界。

### 2.13 How To Read The Abstract World Model

`Abstract world model` 的任务是：

`给定当前隐藏状态和一个候选抽象动作，直接预测 h 步之后的慢确定性状态。`

到这一步，系统已经有了：

- 当前隐藏状态 $z_t$
- 有限个候选抽象动作 $\{\hat A_n\}_{n=1}^{K^{N_q}}$

它还缺的是：

`对每个候选抽象动作，快速估计 h 步之后的未来慢状态。`

#### First: Input Variables

原文说，抽象世界模型 $\mathcal W_\psi$ 学的是从当前 world model state $z_t$ 和一个 abstract action $A_t$ 到未来慢确定性状态 $d_{t+h}^s$ 的映射。

论文正文在 prose 里会把输入 abstract action 写成 $A_t$，但真正进入后续 planning 的，其实是由量化器给出的离散候选动作，也就是

$$
\{\hat A_n\}_{n=1}^{K^{N_q}} .
$$

这里需要把符号收紧：

- 连续动作特征是 $A_t$
- 量化后的抽象动作候选是 $\hat A_n$
- 抽象世界模型真正被拿来枚举比较的，是这些量化后的 $\hat A_n$

因此，这一节里最直接的输入关系是：

$$
(z_t,\hat A_n).
$$

#### Second: What Equation (7) Predicts

原文把抽象世界模型写成：

$$
\left\{\hat d_{t+h,n}^s\right\}_{n=1}^{K^{N_q}}
=
\mathcal W_\psi
\left(
z_t,\,
\left\{\hat A_n\right\}_{n=1}^{K^{N_q}}
\right). \tag{7}
$$

这条式子表达的是：

$$
(z_t,\hat A_n)
\;\longmapsto\;
\hat d_{t+h,n}^s ,
\qquad n=1,\dots,K^{N_q}.
$$

也就是说，对每个候选抽象动作 $\hat A_n$，抽象世界模型都输出一个对应的未来慢确定性状态预测 $\hat d_{t+h,n}^s$。

它预测的不是：

- 完整未来观测 $o_{t+h}$
- 完整未来隐藏状态 $z_{t+h}$

它只预测：

$$
d_{t+h}^s,
$$

也就是未来慢层的确定性主干。

#### Third: Why The Output Is Only The Future Slow Deterministic State

所以这里的分工是：

- 快层负责局部、短时、高频细节
- 慢层负责长期、任务级、可规划结构
- 慢层里的 $d_t^s$ 是最适合先做 long-horizon evaluation 的那部分状态

所以抽象世界模型学的是：

`在抽象动作作用下，未来慢确定性主干 $d_{t+h}^s$ 会变成什么。`

#### Fourth: What Equation (8) Uses As The Training Target

接着给出训练目标：

$$
\mathcal L_\psi
=
\frac{1}{K^{N_q}}
\sum_{n=1}^{K^{N_q}}
\left\|
\hat d_{t+h,n}^s - d_{t+h,n}^s
\right\|_2^2. \tag{8}
$$

这里真正要解释的是右边的 target：

$$
d_{t+h,n}^s.
$$

原文在这一段明确说了三件事：

1. 候选动作序列 $\{\hat a_{0:h,n}\}$ 是由动作模型的 decoder 从 $\{\hat A_n\}$ 生成的
2. target 慢确定性状态 $\{d_{t+h,n}^s\}$ 是通过 world model 的 `latent imagination` 得到的
3. 这个过程明确利用了 `prior distribution over the fast states`

因此，target 的生成过程应当写成：

1. 先拿每个候选抽象动作 $\hat A_n$
2. 用动作模型的 decoder 把它解码回一段真实动作序列 $\hat a_{0:h,n}$
3. 从当前隐藏状态 $z_t$ 出发，在没有未来真实观测输入的条件下，让 world model 沿这段动作序列向前想象 future latent trajectory
4. 在这段想象过程中，未来快层随机状态不再通过未来观测做 posterior inference，而是使用 fast states 的 prior distribution
5. 从 imagined future trajectory 中读出 $h$ 步之后的慢确定性状态 $d_{t+h,n}^s$

这里最该卡住的是第 4 步。原文明确点名的是：

`by leveraging the prior distribution over the fast states`

所以最准确的说法不是“整套系统都在做 prior rollout”，而是：

`latent imagination` 的 future fast states 是由 fast-state prior 提供的。

于是，$d_{t+h,n}^s$ 的含义就是：

`完整 world model 在 latent imagination 下得到的 h-step future slow deterministic state。`

所以 `Eq. (8)` 真正训练的不是“抽象世界模型去模仿真实外界标注”，而是：

`让抽象世界模型去模仿完整 world model 的 latent imagination 所给出的 h 步未来慢确定性 target。`

#### Fifth: What The Abstract World Model Is Approximating

这样一来，`Eq. (8)` 的训练含义就清楚了。

抽象世界模型不是在拟合外部人工标签，而是在拟合完整 world model 给出的 imagined target。它学的是下面这个昂贵过程的低成本近似：

$$
\text{decode } \hat A_n
\;\longrightarrow\;
\text{imagine future latent trajectory with the full world model}
\;\longrightarrow\;
d_{t+h,n}^s.
$$

于是可以把两者的关系固定成：

- 完整 world model：细粒度、高分辨率、计算更贵
- abstract world model：粗粒度、低分辨率、计算更便宜
- 后者被训练成前者在未来慢确定性状态 $d_{t+h}^s$ 上的低成本替身

#### Sixth: What This Means Computationally

从计算角度看，抽象世界模型学习的是：

`给定当前状态和抽象动作，未来慢层骨架的 h-step transition map。`

它把原本更贵的过程压缩成一次直接映射：

$$
(z_t,\hat A_n)
\;\longrightarrow\;
\hat d_{t+h,n}^s.
$$

这一步一旦成立，后面的 planning 就不必再对每个候选动作都做高频 rollout，而只需要比较这些预测出来的未来慢状态。

#### Seventh: What To Retain From The Abstract World Model

`Abstract world model` 的作用，是把“对每个抽象动作做完整 h-step 世界模型想象”这个昂贵过程，替换成“直接预测未来慢确定性状态”这个便宜过程。

所以它学到的不是完整未来世界，而是：

`abstract action -> future slow deterministic backbone`

这也正是后面 `Eq. (10)` 能成立的前提。

### 2.14 How Equation (2) Becomes Computable In This Paper

到这里，可以先把前面的逻辑重新接起来。

`Eq. (1)` 解决的是当前时刻的问题：给定当前观测，怎样推断当前隐藏状态。  
`Eq. (2)` 解决的是未来时刻的问题：给定一个候选动作，怎样评价它未来的信息价值和目标价值。

真正的困难在 `Eq. (2)`。如果还停留在一般形式，系统需要面对的是：

- 动作空间是连续的
- 动作序列是多步的
- 未来状态和未来观测都还没有发生

这就意味着，原始 active inference 要对大量候选 future policies 做想象和比较，计算上几乎不可承受。

这篇文章把这个难点拆成了两个工程化改造。

第一步，用 `action model` 把连续动作序列改写成有限个可枚举的 `abstract actions`。  
这样需要比较的对象，不再是无限多条连续动作轨迹，而是

$$
\{\hat A_n\}_{n=1}^{K^{N_q}}.
$$

第二步，用 `abstract world model` 直接预测每个候选抽象动作对应的未来慢确定性状态，而不再对每个候选动作都做一次完整的高分辨率 world-model rollout。

于是，这篇文章里的动作评价链条就变成了：

1. 先根据当前观测得到当前隐藏状态 $z_t$
2. 枚举有限个候选抽象动作 $\hat A_n$
3. 用 `abstract world model` 预测每个候选动作对应的未来慢状态 $\hat d_{t+h,n}^s$
4. 再结合 world model 的 slow/fast prior 与 decoder，补出后面计算 EFE 所需的分布
5. 计算每个候选抽象动作的 EFE
6. 选出 EFE 最小的那个抽象动作
7. 最后再把它解码回真实动作序列执行

所以这一步的关键不是重新定义 `EFE`，而是：

`把一般形式的 Eq. (2) 改写成一个真的可以在这套分层 world model 上被算出来的程序。`

所以下一步进入 `Eq. (9)` 时，真正要看的就是：

`这篇文章怎样把一般形式的 EFE，具体化成自己的 slow/fast world model 版本。`

### 2.15 What Equation (9) Is Really Doing

这一步要回答的问题是：

`一般形式的 EFE，到了这篇 slow/fast world model 里，具体要对什么求期望？`

原文写的是：

$$
\mathcal{G}(\tau)
\approx
-
\mathbb{E}_{q_\theta(o_\tau, z_\tau \mid \pi)}
\Big[
\log q_\theta(s_\tau^f \mid z_\tau^s, o_\tau)
-
\log q_\theta(s_\tau^f \mid z_\tau^s)
\Big]
-
\mathbb{E}_{q_\theta(o_\tau, z_\tau \mid \pi)}
\big[
\log p(o_\tau \mid o_{\mathrm{pref}})
\big] .
$$

线性地看，这一步做了两件事。

第一，把通用形式里的未来隐藏状态更新，具体落到这篇模型里的 `fast stochastic state` 上。  
在一般写法里，信息价值对应的是：

$$
\log q(z_\tau \mid o_\tau, \pi) - \log q(z_\tau \mid \pi),
$$

意思是：未来观测会让我们对未来隐藏状态的理解改变多少。

这篇文章把未来隐藏状态拆成：

$$
z_\tau = \{z_\tau^s, z_\tau^f\}.
$$

然后进一步把信息更新具体化成：

$$
\log q_\theta(s_\tau^f \mid z_\tau^s, o_\tau)
-
\log q_\theta(s_\tau^f \mid z_\tau^s).
$$

这表示：

- 先给定未来慢状态 $z_\tau^s$
- 再看未来观测 $o_\tau$
- 它会让我们对未来快层随机状态 $s_\tau^f$ 的信念改变多少

所以 `Eq. (9)` 的含义不是“重新定义 EFE”，而是：

`把信息价值具体放到未来快层随机状态的更新上。`

第二，把计算 EFE 所需的联合分布写成这篇 world model 可以提供的形式。原文给出的分解是：

$$
q_\theta(o_\tau, z_\tau \mid \pi)
=
p_\theta(o_\tau \mid z_\tau)\,
q_\theta(z_\tau^f \mid z_\tau^s)\,
q_\theta(z_\tau^s \mid \pi).
$$

这一步不能只当成一个形式分解来看，它背后对应的是这篇模型的生成顺序。

先把未来隐藏状态拆开：

$$
z_\tau = \{z_\tau^s, z_\tau^f\}.
$$

于是上面的联合分布其实是在说：

1. 先给定候选动作或策略 $\pi$，得到未来慢状态分布
   $$
   q_\theta(z_\tau^s \mid \pi)
   $$
2. 在未来慢状态给定的条件下，再得到未来快状态分布
   $$
   q_\theta(z_\tau^f \mid z_\tau^s)
   $$
3. 最后在完整未来隐藏状态
   $$
   z_\tau = \{z_\tau^s, z_\tau^f\}
   $$
   给定的条件下，生成未来观测
   $$
   p_\theta(o_\tau \mid z_\tau)
   $$

所以这条分解真正表达的是：

`在这篇模型里，未来是按“慢状态 -> 快状态 -> 观测”这条生成链展开的。`

这里还有一个隐含假设也值得点出来。第二项写成

$$
q_\theta(z_\tau^f \mid z_\tau^s)
$$

而不是

$$
q_\theta(z_\tau^f \mid z_\tau^s, \pi)
$$

意味着这篇文章把策略对未来的影响，主要先压到慢状态这一层；一旦未来慢状态给定，未来快状态就在这个条件下展开，而不再显式依赖 $\pi$。

这样一来，下面这句才真正成立：只要先拿到未来慢状态分布

$$
q_\theta(z_\tau^s \mid \pi),
$$

也就是“在给定候选动作或策略 $\pi$ 的情况下，未来慢状态会如何分布”，其余量都能沿着这条生成链补出来：

$$
q_\theta(z_\tau^s \mid \pi)
\;\Longrightarrow\;
q_\theta(z_\tau^f \mid z_\tau^s)
\;\Longrightarrow\;
p_\theta(o_\tau \mid z_\tau).
$$

因此，`Eq. (9)` 最终把问题压缩成了一个更具体的问题：

在每个候选动作下，未来慢状态分布

$$
q_\theta(z_\tau^s \mid \pi)
$$

怎么得到？

### 2.16 What Equation (10) Is Really Approximating

`Eq. (10)` 就是在回答刚才那个问题：未来慢状态分布

$$
q_\theta(z_\tau^s \mid \pi)
$$

在这篇方法里怎样近似得到。

原文写的是：

$$
q_\theta(z_\tau^s \mid \pi)
\approx
q_\theta(s_\tau^s \mid d_\tau^s, \hat{A})\,
q_\psi(d_\tau^s \mid \hat{A}) .
$$

这一步可以拆成两步。

第一步，先得到未来慢层里的确定性部分 $d_\tau^s$。  
这正是抽象世界模型做的事：给定当前隐藏状态和一个候选抽象动作，用

$$
\mathcal W_\psi
$$

直接预测未来慢确定性状态。

第二步，再把慢层里的随机部分 $s_\tau^s$ 补上。  
也就是说，在已经有了 $d_\tau^s$ 之后，再通过慢层先验得到对应的随机部分，从而组合出未来慢状态

$$
z_\tau^s = \{d_\tau^s, s_\tau^s\}.
$$

所以 `Eq. (10)` 的真正含义是：

用抽象世界模型先给出未来慢层骨架，再用慢层先验把未来慢状态分布补完整。

这里还要卡住一个符号细节。原文把

$$
q_\psi(d_\tau^s \mid \hat A)
$$

写得很紧，但按全文上下文，它实际上还隐含依赖当前状态 $z_t$，因为抽象世界模型的实际输入一直是

$$
(z_t,\hat A).
$$

所以把 `Eq. (10)` 读成更完整的意思，就是：

在当前隐藏状态 $z_t$ 下，给定候选抽象动作 $\hat A$，先预测未来慢确定性状态，再补出未来慢层随机状态，从而近似得到未来慢状态分布。

这样一来，为什么要把 policy $\pi$ 替换成抽象动作 $\hat A$ 也就清楚了：  
这篇文章真正枚举和比较的，不再是无限多条连续动作序列，而是有限个抽象动作。

### 2.17 Why Equation (11) Becomes A Squared-Error Goal Term

有了 `Eq. (10)` 之后，未来慢状态分布已经能近似得到，接下来还剩最后一个问题：

目标价值那一项，怎样变成真正可算的目标函数？

原文把 preference term 进一步具体化成：

$$
\mathcal{G}(\tau)
\approx
-
\mathbb{E}_{q_\theta(o_\tau, z_\tau \mid \pi)}
\Big[
\log q_\theta(s_\tau^f \mid z_\tau^s, o_\tau)
-
\log q_\theta(s_\tau^f \mid z_\tau^s)
\Big]
-
\mathbb{E}_{q_\theta(o_\tau, z_\tau \mid \pi)}
\Big[
-\gamma (o_\tau - o_{\mathrm{pref}})^2
\Big] .
$$

这里第二项之所以变成平方误差，是因为作者对 preference distribution 做了一个具体假设：

$$
p(o_\tau \mid o_{\mathrm{pref}})
=
\mathcal N(o_{\mathrm{pref}}, \sigma^2).
$$

对这个高斯分布取对数：

$$
\log p(o_\tau \mid o_{\mathrm{pref}})
=
\text{const}
-
\frac{1}{2\sigma^2}(o_\tau - o_{\mathrm{pref}})^2.
$$

把常数项丢掉，并记

$$
\gamma = \frac{1}{2\sigma^2},
$$

就得到文中的平方误差形式。

所以这里的目标价值不再是抽象的 “preference distribution”，而是：

未来观测 $o_\tau$ 与目标观测 $o_{\mathrm{pref}}$ 之间的加权平方距离。

这一步的作用是把 `Eq. (9)(10)` 里还比较抽象的 EFE，彻底压成一个可以实际比较的分数：

- 第一项衡量信息价值：未来观测会让快层随机状态的信念改变多少
- 第二项衡量目标价值：未来观测离目标观测还有多远

其中，$\gamma$ 是偏好分布的 `precision`。它越大，系统越强调逼近目标；它越小，信息价值相对更容易占主导。

### 2.18 Why The Approximation Signs In Equations (9)(10)(11) Are Different

`Eq. (9)(10)(11)` 都写成了 $\approx$，但这三个近似号不是同一种含义。

`Eq. (9)` 的近似是结构近似。  
通用形式的 EFE 本来比较的是未来完整隐藏状态的更新；这篇文章把这一更新具体压到快层随机状态

$$
s_\tau^f
$$

上，所以这里的 $\approx$ 来自一种建模选择：作者假定对探索最关键的不确定性，主要体现在快层随机状态里。

`Eq. (10)` 的近似是动力学替身近似。  
这里不是精确求未来慢状态分布

$$
q_\theta(z_\tau^s \mid \pi),
$$

而是用两步近似去构造它：

1. 先用 `abstract world model` 预测未来慢确定性状态
2. 再用慢层先验补出未来慢层随机状态

所以这里的 $\approx$ 表示：用抽象动作和抽象世界模型，去近似 full world model 在未来慢状态上的细粒度结果。

`Eq. (11)` 的近似则来自具体分布假设。  
一旦假设

$$
p(o_\tau \mid o_{\mathrm{pref}})
=
\mathcal N(o_{\mathrm{pref}}, \sigma^2),
$$

那么 preference term 就能改写成平方误差形式。严格地说，这一步是“在丢掉常数项之后的等价改写”；之所以文中仍然保留 $\approx$，是因为它继承了前面 `Eq. (9)` 和 `Eq. (10)` 的近似。

所以最简洁的区分是：

- `Eq. (9)`：结构近似
- `Eq. (10)`：动力学替身近似
- `Eq. (11)`：偏好分布具体化后的等价改写，并继承前面的近似

把 `(9)(10)(11)` 连起来，`B. Action Selection` 的整条逻辑就是：

1. `Eq. (9)`：把一般形式的 EFE 具体化到这篇 slow/fast world model 上
2. `Eq. (10)`：用抽象动作和抽象世界模型构造未来慢状态分布
3. `Eq. (11)`：把目标价值写成可直接计算的平方误差项

### 2.19 How Fig. 3 Maps To The Online Action-Selection Loop

![Fig. 3. Action selection based on the minimization of EFE.](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-04-figure-01.jpg)

*Fig. 3. Action selection based on the minimization of EFE.*

这张图表达的，不是新的数学对象，而是前面 `(9)(10)(11)` 在在线执行时的实际调用顺序：

1. 由当前观测推断当前隐藏状态 $z_t$
2. 枚举所有候选抽象动作 $\{\hat A_n\}$
3. 用抽象世界模型预测每个候选动作对应的未来慢确定性状态
4. 补出对应的未来慢状态分布
5. 对每个候选动作计算 EFE
6. 选择 EFE 最小的那个抽象动作
7. 把它解码回真实动作序列并执行

如果压成一句最短总结：

`B. Action Selection` 的作用，不是重新发明 EFE，而是把“未来动作值不值得”这个抽象原则，压缩成一个能在这套分层机器人系统里真正跑起来的动作选择程序。`

## 3. How The Experiments Are Designed

### 3.1 Environment Setup

![Fig. 4. Experimental environment and policy patterns.](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-04-figure-02.jpg)

*Fig. 4. Experimental environment (left) and policy patterns included in the collected dataset (right).*

实验部分不是一上来就看成功率，而是先看作者到底搭了一个什么环境。

原文的真实机器人环境很小，但设计得很刻意：

- 一个六自由度机械臂，其中一个自由度是 gripper
- 一个固定相机，拍到机器人和整个操作台
- 台面上有 dish、pot、pan 和一个 pot lid
- 环境中可能有蓝球、红球，或者两者同时存在

关键点在于：**不确定性是通过 lid 引入的。**

当 lid 盖着时，机器人并不知道 pot 里到底有没有球。这就让后面的 exploratory action 有了真正的任务语境，而不是纯粹的人造 curiosity toy example。

作者收集的数据也不是开放式人类示范，而是很明确的、受控的 demonstration dataset：

- 右图一共定义了 `8` 种 policy pattern
- 每条 demonstration 由 `2` 个 policy pattern 串起来
- 对所有有效组合都做了 teleoperation 采集
- 每个序列长度是 `100` 个 time steps，采样频率 `5 Hz`

这里还有一个和方法直接对应的设计细节：

`每个 policy pattern 大约对应 50 个 time steps。`

这正好和动作模型里的固定动作长度

$$
h = 50
$$

接上。也就是说，动作抽象不是在真空里学的，它和数据里的行为片段长度是对齐的。

### 3.2 What The Authors Expect The Model To Represent

在正式看结果之前，原文还先说明了一个很重要的解释框架：他们希望各个 latent/component 分别承载什么。

作者对这套系统的预期是：

- 慢隐藏状态 $z_t^s$ 表示任务的大尺度进展，比如球和 lid 的位置关系
- 快隐藏状态 $z_t^f$ 表示更即时、更短时的局部信息
- 抽象动作 $A_t$ 对应 demonstration 数据里有行为意义的动作片段

这一步很重要，因为它告诉你：后面的实验不是只看“有没有成功”，还在看这些 latent 到底有没有学出作者想要的语义分工。

换句话说，实验设计本身已经包含三个层次的问题：

1. 抽象世界模型有没有学会“动作 -> 未来状态”的对应关系
2. 整体系统能不能真的完成目标任务
3. 在不确定环境下，系统会不会偏向信息获取动作

### 3.3 What The Experiments Actually Evaluate

原文把实验目标分成了三类。

第一类是 **Capability of Abstract World Model**。  
这里要验证两件事：

- 它是不是比 sequential full-world-model rollout 更省计算
- 不同抽象动作是不是会导致不同且可解释的未来预测

第二类是 **Goal Achievement Performance**。  
这里就是最传统的任务成功率比较：给定 goal observation，系统能不能真的把球或 lid 操作到目标位置。

第三类是 **Environment Exploration**。  
这里不是看一般意义上的探索能力，而是看在 lid 盖住、pot 内部未知的场景里，系统会不会因为 epistemic value 的存在，先去做开盖这种信息获取动作。

所以整套实验的线性逻辑其实是：

1. 先证明 abstract world model 这个新模块不是空架子
2. 再证明整套系统在 goal-directed tasks 上确实有效
3. 最后再看它有没有表达 exploratory behavior 的能力

### 3.4 Baseline And Ablations

这一节也不能跳过，因为后面结果怎么读，很大程度取决于 baseline 和 ablation 的设置。

原文比较了三类对照：

- `GC-DP`
  这是一个 goal-conditioned diffusion policy baseline。它代表的是“直接从观测和 goal 生成未来动作”的那条路线。

- `Non-hierarchical`
  这是 world model 的去层级版本。它保留 latent dynamics，但去掉 slow/fast hierarchy。

- `No abstract world model (No AWM)`
  这是去掉抽象世界模型的版本。它仍然有抽象动作，但动作评价时不走 `AWM` 这条低成本近似，而是直接在实际动作序列上算 EFE。

这三个对照刚好对应三类问题：

- 和 `GC-DP` 比，问的是这套 active-inference 架构值不值得
- 和 `Non-hierarchical` 比，问的是 temporal hierarchy 有没有贡献
- 和 `No AWM` 比，问的是 abstract-world-model 这层近似有没有贡献

所以后面看结果时，不能只看 proposed 比 baseline 高多少，还要看：

`去掉 hierarchy 会损失多少，去掉 abstract world model 又会损失多少。`

## 4. What The Experiments Actually Show

### 4.1 Computation Becomes Tractable

文章最先展示的，不是成功率，而是计算代价确实降了。

它报告说：

- proposed framework：评估全部抽象动作只需要大约 `237 ms`
- conventional sequential evaluation：需要大约 `718 ms`

这不是数量级革命，但已经足够说明：抽象动作和抽象世界模型确实降低了在线动作选择的代价。

对于这篇文章来说，这是必要证据。因为如果 tractability 没有改善，整套架构就只是在堆模块。

### 4.2 Goal Achievement Is Better Than The Baseline

![Predicted observations and actual execution](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-05-figure-01.jpg)

![EFE over abstract actions](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-05-figure-03.jpg)

在真实机器人抓取与开合盖子的任务里，文章给出的总成功率是：

- Proposed: `70.7%`
- GC-DP baseline: `24.4%`
- Non-hierarchical ablation: `51.2%`
- No abstract world model: `37.2%`

这个结果说明两件事。

第一，它不是只比一个弱 baseline 稍好，而是两个关键 ablation 也明显退步。  
第二，这篇里最重要的两个结构，确实都有贡献：

- 去掉 temporal hierarchy，表现下降。
- 去掉 abstract world model，表现下降更多。

作者据此得出的判断是合理的：时间层级和动作/状态抽象都在起作用，而不只是某个 loss 凑巧有效。

### 4.3 Exploration Exists, But The Evidence Is Still Limited

文章最有意思的一段，是在不确定场景里比较两种抽象动作：

- goal-directed：把蓝球从平底锅移到盘子
- exploratory：先打开锅盖，看看红球是否在锅里

然后他们通过调 `preference precision` $\gamma$ 来改变 `EFE` 两项的权重：

- 当 $\gamma = 10^2$ 时，goal-directed action 的 EFE 更低，于是机器人直接执行目标动作。
- 当 $\gamma = 10^{-4}$ 时，exploratory action 的 EFE 更低，于是机器人先开盖探索。

这说明什么？

说明这篇至少做到了：

`机器人不是只能执行目标动作，而是可以在统一框架里切换到信息获取动作。`

但也要把边界说清楚。文章自己承认：

- 这里只验证了会不会出现 exploratory action
- 还没有真正验证探索行为是否系统性提高了长期任务成功率
- exploratory / goal-directed 的切换还依赖手工调参

所以这篇不能被读成“机器人已经学会主动探索”。更准确的说法是：

`它证明了这套架构可以表达探索，而且在真实机器人上出现了这种行为。`

## 5. What The Paper Is Not Yet Solving

这篇文章很容易让人兴奋，但它的边界也很明确。

### 5.1 It Is Not A General Robot World Model

它的数据来自人类示范，任务空间有限，环境结构也比较受控。  
这不是一个 open-world robot foundation model，更像一个：

`active-inference flavored, temporally hierarchical, action-abstracted manipulation controller`

所以它给的是一个可信连接点，不是终局。

### 5.2 Generalization Is Still Fragile

作者自己点出了一个很关键的失败模式：

如果某个动作-环境组合在训练数据里没出现过，抽象世界模型就可能学出错误依赖。例如锅里其实没有红球，它却预测出某种不一致的结果。

这点很重要，因为它说明这套方法虽然有 world model 的名字，但其泛化能力仍然被 demonstration distribution 明显约束。

### 5.3 Exploration Control Is Still Hand-Tuned

这篇里 exploratory behavior 的开关，本质上还是通过超参数 `γ` 来调。  
也就是说：

- 理论上 exploration 在目标函数里
- 但工程上何时探索，仍没有被自适应地学出来

这一点如果不解决，系统还不能算真正成熟。

## 6. Why This Paper Matters For Your Current Mainline

这篇对你现在最有价值，不是因为它已经是最强机器人论文，而是因为它恰好落在你刚刚整理的那条线交叉点上：

- `active inference`
- `world model`
- `representation as state construction`
- `temporal hierarchy`
- `goal-directed vs epistemic action`

更具体地说，它把你刚刚在谢赛宁访谈里抓到的几件事，都落成了一个工程架构：

1. `world model` 不是语言接口，而是内部状态与预测机制。
2. 好表征不是只为分类服务，而要服务于 planning。
3. 状态需要 coarse-graining，不可能在原始像素或原始动作层直接规划。
4. 真实系统里的不确定性，要求动作选择同时考虑 exploitation 和 exploration。

所以它虽然不是统计物理论文，但它确实是你那份 [world-model-as-learned-nonequilibrium-dynamics.md](../../youtube/notes/world-model-as-learned-nonequilibrium-dynamics.md) 里比较接地的一个实例。

## 7. What To Retain From This Paper

这篇最值得保留的是下面这条链：

1. 标准 deep active inference 在真实机器人上卡住的主要原因，是表示能力和在线规划成本。
2. 这篇的解法不是改 `EFE` 数学，而是引入 `temporal hierarchy + abstract action + abstract world model`。
3. `slow states` 负责可规划的任务级表示，`fast states` 负责短时细节。
4. 通过在抽象动作空间里比较 `EFE`，系统可以在统一框架里出现 goal-directed 和 exploratory 行为。
5. 文章已经证明这条路在小规模真实机器人任务上可跑，但还远没到通用机器人世界模型的程度。

## 8. What To Do With This Paper In Your Reading Chain

这篇最适合在你的链条里承担一个“概念落地样本”的角色，而不是理论支柱。

更具体地说，它可以帮助你把下面几组概念接起来：

- `active inference` 不只是哲学语言，也能落成可训练控制框架。
- `world model` 的关键不只是预测未来观测，而是构造适合规划的慢状态。
- `representation comparison` 不能只看分类精度，还要看它是否支持 planning、action abstraction 和 uncertainty reduction。

所以这篇文章读完后，最值得保留的不是某条公式，而是这个判断：

`真正能把 active inference 从概念推进到机器人控制的，不是再多讲一点 free energy，而是找到合适的状态抽象和动作抽象。`

## 9. Why Temporal Hierarchy Matters Here

这篇最值得认真想的一点，是为什么他们坚持做 `slow/fast` 两层。

答案不是“分层结构比较高级”，而是因为他们真正想解决的任务，本来就有两个时间尺度：

- 快时间尺度：机械臂即时动作、瞬时观测变化、短时微调。
- 慢时间尺度：物体位置变化、任务阶段推进、环境不确定性是否被消除。

如果把这两种变化都塞进同一个状态里，模型要么很难学长时依赖，要么规划代价很高。  
而作者做的事情是：

- 让完整 world model 负责吸收快慢两种动态。
- 让 abstract world model 只在慢状态上做预测和规划。

所以 temporal hierarchy 在这里不是单纯“更 biologically plausible”，而是一个明确的计算分解：

`用完整模型吸收现实复杂性，用慢变量模型负责可规划性。`

这和你刚整理的 `representation as state construction` 是直接接得上的。慢状态本质上就是一种任务相关的 coarse-grained representation。

### 9.1 How The Slow/Fast Split Relates To Statistical Physics

这套 `slow/fast states` 和统计物理里的快慢变量，确实有明显联系，但这个联系最好理解成：

`结构上高度相似，但不是把论文里的 latent state 直接等同成某个物理可观测量。`

先说最直接的共同点。统计物理里谈快慢变量，通常是在说：系统里有些自由度变化很快、会迅速弛豫；另一些自由度变化很慢，决定了更长期、更大尺度的演化。于是分析时常常会做两件事：

1. 把快变量看成局部、短时、容易弛豫的部分
2. 把慢变量看成更稳定、更能支配长期行为的有效变量

这篇文章的直觉与此非常接近。

- 快状态对应的是机械臂局部动作细节、图像的瞬时变化、短时修正
- 慢状态对应的是任务是否推进、物体配置是否改变、不确定性是否被消除

所以在结构上，作者其实也在做一件很像统计物理 coarse-graining 的事：

`不让所有自由度都以同样的重要性进入规划，而是把真正支配长期决策的那部分慢变量单独拎出来。`

如果再往统计物理的语言里翻，这件事最像下面这条思路：

- 完整 world model 类似一个高维、带噪声、包含快慢模式的动力系统
- 慢状态更像 coarse-grained variables，或者说更接近 order-parameter-like 的有效变量
- abstract world model 则像在这些慢变量上学习一个低频的有效动力学

也就是说，这篇文章最像统计物理的地方，不是“它也分了两层”，而是：

`它试图在一个复杂系统里找到更适合长期预测和规划的慢变量表示，再只在这些慢变量上写有效演化。`

这和统计物理里“消去快变量，在慢变量上写有效方程”的思想是接得上的。你可以把它和下面这些关键词放在一起理解：

- timescale separation
- coarse-graining
- effective dynamics
- slow manifold

但两者也有非常重要的区别，这里不能混。

第一，统计物理里的快慢变量，很多时候有明确的物理定义，比如密度、磁化强度、局域平衡涨落、快弛豫模态。  
而这篇文章里的快慢状态是学出来的 latent variables，不是直接可测的物理量。

第二，统计物理里做快变量消去时，往往关心的是有没有严格或近似的时间尺度分离，以及消去之后是否还能得到封闭的有效动力学。  
这篇文章没有证明这种严格封闭性，它只是通过训练让某些 latent 更倾向于承载慢结构，再让抽象世界模型只在这些慢结构上工作。

第三，统计物理里区分快慢变量，最终通常是为了理解系统的有效理论、相变、不可逆性或输运行为。  
这篇文章区分快慢变量，最终目的是让机器人规划变得 tractable。

所以最稳的总结不是：

`这篇文章的 slow/fast variables 就是统计物理里的 slow/fast variables。`

而是：

`这篇文章在方法论上复现了统计物理处理复杂系统的一种经典思想：把快变量留给完整动力学吸收，把慢变量拿来写更适合长期预测和决策的有效模型。`

这也是它和你当前主线最值得连接的地方。因为如果再往前推一步，这里的 `slow state` 就可以被理解成一种任务相关的 coarse-grained state，而 `abstract world model` 则可以被理解成这个 coarse-grained state 上的 learned effective dynamics。
