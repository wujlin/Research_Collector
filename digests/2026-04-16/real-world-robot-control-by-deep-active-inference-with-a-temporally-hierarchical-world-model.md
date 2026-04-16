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

## 2. The Architectural Move: Three Models, Not One

这篇文章的关键不是单个网络，而是三个部件的组合：

1. `world model`
2. `action model`
3. `abstract world model`

这三者的分工非常清楚。

### 2.1 World Model

![Framework overview](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-02-figure-01.jpg)

![World model with temporal hierarchy](../../pdfs/2026-04-15/real-world-robot-control-by-deep-active-inference-with-a-temporally-hierarchical-world-model.mineru/hybrid_auto/images/page-02-figure-03.jpg)

世界模型负责把观测和动作写成一个层级 latent dynamics。它不是单层状态，而是把隐藏状态拆成：

- `slow states`
- `fast states`

并且每一层又各自有 deterministic part 和 stochastic part。

这一步的直觉很重要。作者并不认为所有环境变化都应该在同一个时间尺度上建模。像“球是不是已经被移到盘子里”“锅盖是否打开”这种任务级变化，应该更像慢变量；而机械臂短时间的细节变化、瞬时视觉变化，更像快变量。

所以这篇里的 temporal hierarchy 不是装饰，而是整个方法能工作的重要前提。因为后面抽象世界模型只预测慢变量，如果慢变量本身没有学对，后面的抽象规划就站不住。

### 2.2 Action Model

动作模型负责把一个固定长度的动作序列压成一个离散的 `abstract action`。做法不是直接 clustering，而是：

- 先用 encoder 把长度为 `h=50` 的动作序列映射到低维连续表示。
- 再用 residual vector quantizer 把它量化成离散 code 组合。
- 最后 decoder 可以把抽象动作再还原成真实动作序列。

这一步的关键意义是：

`把原始连续动作空间，替换成一个可枚举、可评价的抽象动作空间。`

这对 active inference 非常重要。因为如果还停留在原始动作空间，`EFE` 计算会爆炸；但如果先压到抽象动作空间，动作选择就从“搜索大量连续序列”变成“比较有限个抽象动作”。

文章这里最值得记住的不是具体量化器实现，而是这个思路：

`用 learned latent action code，给 active inference 提供一个 tractable planning vocabulary。`

### 2.3 Abstract World Model

抽象世界模型进一步把“抽象动作”和“未来慢状态”连起来。它不再逐步滚动完整世界模型，而是直接预测：

`给定当前状态 + 某个 abstract action，未来的 slow state 会变成什么。`

这一点很关键。因为它把规划从高频、细粒度、昂贵的 rollout，变成了低频、粗粒度、可枚举的 rollout。

所以这篇文章真正的工程突破点，其实就在这里：

`不是让原始 world model 更万能，而是增加了一个只服务于规划的慢变量预测层。`

## 3. What Active Inference Means In This Paper

这篇文章里的 `active inference` 不需要你把整套 FEP 哲学全背下来。真正需要抓住的只有一件事：

动作选择基于 `expected free energy (EFE)`。

作者把它分成两部分：

- `epistemic value`
- `extrinsic value`

这里最稳妥的读法是：

- `epistemic value` 关心“这个动作会不会带来新信息，减少我对环境的无知”。
- `extrinsic value` 关心“这个动作会不会让我更接近目标观察”。

所以在这个框架里，探索不是额外加的 heuristic，而是目标函数里的一部分。

但文章真正的贡献不在这个公式本身，而在于：他们没有再像很多 active inference 工作那样，把 `EFE` 只当训练 loss；他们是让机器人在执行时真正用它来选动作，而且通过抽象动作和抽象世界模型，让这个选择过程变得可计算。

## 4. Why Temporal Hierarchy Matters Here

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

## 5. What The Experiments Actually Show

### 5.1 Computation Becomes Tractable

文章最先展示的，不是成功率，而是计算代价确实降了。

它报告说：

- proposed framework：评估全部抽象动作只需要大约 `237 ms`
- conventional sequential evaluation：需要大约 `718 ms`

这不是数量级革命，但已经足够说明：抽象动作和抽象世界模型确实降低了在线动作选择的代价。

对于这篇文章来说，这是必要证据。因为如果 tractability 没有改善，整套架构就只是在堆模块。

### 5.2 Goal Achievement Is Better Than The Baseline

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

### 5.3 Exploration Exists, But The Evidence Is Still Limited

文章最有意思的一段，是在不确定场景里比较两种抽象动作：

- goal-directed：把蓝球从平底锅移到盘子
- exploratory：先打开锅盖，看看红球是否在锅里

然后他们通过调 `preference precision γ` 来改变 `EFE` 两项的权重：

- 当 `γ = 10^2` 时，goal-directed action 的 EFE 更低，于是机器人直接执行目标动作。
- 当 `γ = 10^-4` 时，exploratory action 的 EFE 更低，于是机器人先开盖探索。

这说明什么？

说明这篇至少做到了：

`机器人不是只能执行目标动作，而是可以在统一框架里切换到信息获取动作。`

但也要把边界说清楚。文章自己承认：

- 这里只验证了会不会出现 exploratory action
- 还没有真正验证探索行为是否系统性提高了长期任务成功率
- exploratory / goal-directed 的切换还依赖手工调参

所以这篇不能被读成“机器人已经学会主动探索”。更准确的说法是：

`它证明了这套架构可以表达探索，而且在真实机器人上出现了这种行为。`

## 6. What The Paper Is Not Yet Solving

这篇文章很容易让人兴奋，但它的边界也很明确。

### 6.1 It Is Not A General Robot World Model

它的数据来自人类示范，任务空间有限，环境结构也比较受控。  
这不是一个 open-world robot foundation model，更像一个：

`active-inference flavored, temporally hierarchical, action-abstracted manipulation controller`

所以它给的是一个可信连接点，不是终局。

### 6.2 Generalization Is Still Fragile

作者自己点出了一个很关键的失败模式：

如果某个动作-环境组合在训练数据里没出现过，抽象世界模型就可能学出错误依赖。例如锅里其实没有红球，它却预测出某种不一致的结果。

这点很重要，因为它说明这套方法虽然有 world model 的名字，但其泛化能力仍然被 demonstration distribution 明显约束。

### 6.3 Exploration Control Is Still Hand-Tuned

这篇里 exploratory behavior 的开关，本质上还是通过超参数 `γ` 来调。  
也就是说：

- 理论上 exploration 在目标函数里
- 但工程上何时探索，仍没有被自适应地学出来

这一点如果不解决，系统还不能算真正成熟。

## 7. Why This Paper Matters For Your Current Mainline

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

## 8. What To Retain From This Paper

如果把这篇压成最值得留下的几句话，我会保留下面这条链：

1. 标准 deep active inference 在真实机器人上卡住的主要原因，是表示能力和在线规划成本。
2. 这篇的解法不是改 `EFE` 数学，而是引入 `temporal hierarchy + abstract action + abstract world model`。
3. `slow states` 负责可规划的任务级表示，`fast states` 负责短时细节。
4. 通过在抽象动作空间里比较 `EFE`，系统可以在统一框架里出现 goal-directed 和 exploratory 行为。
5. 文章已经证明这条路在小规模真实机器人任务上可跑，但还远没到通用机器人世界模型的程度。

## 9. What To Do With This Paper In Your Reading Chain

这篇最适合在你的链条里承担一个“概念落地样本”的角色，而不是理论支柱。

更具体地说，它可以帮助你把下面几组概念接起来：

- `active inference` 不只是哲学语言，也能落成可训练控制框架。
- `world model` 的关键不只是预测未来观测，而是构造适合规划的慢状态。
- `representation comparison` 不能只看分类精度，还要看它是否支持 planning、action abstraction 和 uncertainty reduction。

所以这篇文章读完后，最值得保留的不是某条公式，而是这个判断：

`真正能把 active inference 从概念推进到机器人控制的，不是再多讲一点 free energy，而是找到合适的状态抽象和动作抽象。`
