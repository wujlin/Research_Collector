# Percy Liang: Self-training Algorithms and Analyses for Unsupervised Domain Adaptation

- Source: SlidesLive `38955373`
- Talk: Self-training Algorithms and Analyses for Unsupervised Domain Adaptation
- Speaker: Percy Liang
- Venue: ICLR Robust ML Workshop 2021
- Transcript: [`transcript.md`](../../transcripts/38955373-self-training-algorithms-analyses-unsupervised-domain-adaptation-percy-liang-iclr2021/transcript.md)
- Slides: [`curated`](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/index.md), [`full deck`](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/all/index.md)

## 0. 这场 talk 的主线

这场 talk 表面上是在讲 self-training，但更深一层是在讲：当 source domain 和 target domain 不一致时，不能只把问题粗略叫作 OOD，而要先问 domain shift 里面有没有可利用的结构。

Liang 选择了两类结构来展开：

1. `auxiliary information`：每个样本除了输入 `x` 和目标 `y` 之外，还带着一个辅助变量 `z`。这个 `z` 可能有预测力，但也可能在 OOD 中漂移。
2. `gradual shift`：source 和 target 中间不是断裂的，而是存在一串逐渐变化的 intermediate domains。每一步变化不大，但累计起来可以很远。

self-training 在这两条线里的角色并不一样。第一条线里，它负责把一个模型里的预测能力转移到另一个模型里；第二条线里，它负责沿着 domain path 一步步追踪变化。也就是说，这场 talk 的核心不是“伪标签能不能用”，而是：

> self-training 只有在有结构可借力时才真正有意义。

如果没有辅助变量、没有中间路径、没有某种可解释的平滑结构，self-training 很容易只是把错误伪标签反复强化。

## 1. 问题入口：为什么 unsupervised domain adaptation 难

![title](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/01-title.png)

这场 talk 的中心问题是 unsupervised domain adaptation。它的设定很直接：源域有标注数据，目标域有大量无标注数据，目标是训练一个在目标域也能工作的模型。

Percy Liang 用 remote sensing 作为入口。任务是输入卫星图像，输出土地覆盖类型，例如 cropland、grassland、forest。这个任务的现实困难在于，卫星图像本身容易收集，但标注昂贵，而且标注通常只覆盖部分地区。如果只在有标注国家训练，模型在同一分布上能达到较好精度；但直接拿到非洲等目标地区测试，精度会明显下降。

![remote-sensing](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/02-remote-sensing-motivation.png)

这里真正的问题不是“没有数据”，而是“没有目标域标签”。目标域的输入很多，标签很少或没有。因此，关键变成：如何让无标签目标域数据参与训练，而不是只把模型从源域直接外推到目标域。

把这个设定写成最普通的机器学习语言，就是：

1. source domain 给你有标签数据 `(x_s, y_s)`；
2. target domain 给你无标签输入 `x_t`；
3. 训练时不能看到 `y_t`；
4. 但最终评估时关心的是 target domain 上的预测误差。

所以 unsupervised domain adaptation 的困难不在于“没有任何目标域信息”，而在于目标域信息只有输入、没有标签。它要求模型从无标签目标域样本中读出某种可迁移结构。

## 2. 旧路线的局限：只匹配分布不等于学到正确任务

早期 domain adaptation 常用 importance weighting。它的直觉是：用目标域无标签样本估计目标域更常出现的区域，再提高源域中相似样本的权重。这个方法的问题是，它仍然要求源域里已经覆盖了目标域相关区域。如果目标域落在源域外部，importance weighting 很难外推。

深度学习以后，很多方法转向 representation learning。典型做法是把源域输入和目标域输入映射到一个表示空间，让两个域的表示边缘分布尽量接近。问题在于，目标域没有标签，所以你只能匹配 marginal distribution，而不能保证类别语义被正确对齐。极端情况下，源域正类可能被映射到目标域负类附近，边缘分布看起来匹配，但任务语义完全错位。

这就是 Liang 在 talk 里收窄问题的原因。他不试图给所有 OOD 问题一个万能答案，而是问：如果 domain shift 本身带有某些结构，self-training 能不能利用这些结构？

这一步是整场 talk 的方法论转折点。与其说“我要解决 OOD”，不如先说清楚“我面对的是哪一种 OOD”。如果 shift 是由地理、气候、时间、设备、医院、人群组成差异造成的，那么不同 shift 对应的可利用结构完全不同。一个只匹配边缘分布的方法很难自动知道这些结构。

## 3. 第一条结构：auxiliary information

![aux-info](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/04-setting1-auxiliary-information.png)

第一类结构是 auxiliary information。还是 remote sensing 例子：输入 `x` 是卫星图像，输出 `y` 是土地覆盖类型，但每个样本还带有一个辅助变量 `z`，例如位置、时间、天气、气候信息。这些信息不是最终预测目标，但它们和任务有关。

训练数据的结构可以线性读成三层：

1. 源域里有完整的 `(x, y, z)`。
2. 源域和目标域里都有大量无标签的 `(x, z)`。
3. 目标是利用这些无标签 `(x, z)`，提高 in-domain 和 out-of-domain 两边的表现。

关键问题是：`z` 应该怎样进入模型？

这里要注意，`z` 的身份是暧昧的。它不是最终要预测的标签，但又不是完全无关的噪声。它可能同时满足两件事：

1. 在源域里，`z` 对 `y` 很有帮助；
2. 到目标域后，`z` 的分布或含义会发生漂移。

这就是它危险也有用的原因。直接用它，可能学到 shortcut；完全丢掉它，又浪费了结构信息。

## 4. Baseline 1：把 auxiliary information 当输入

![aux-inputs](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/08-aux-inputs-baseline.png)

最自然的方法是 aux-inputs：把 `z` 当作额外输入特征，让模型学习 `(x, z) -> y`。这个方法在 in-domain 上通常有用，因为 `z` 提供了额外信息。例如气候信息确实可能帮助判断某地区是否是 cropland。

但它在 OOD 上会出问题。原因是 `z` 本身也会发生 domain shift。如果模型过度依赖 `z`，那么源域里有用的相关性到了目标域可能不再成立。于是，aux-inputs 往往提高 ID 精度，却可能降低 OOD 精度。

![aux-inputs-hurt](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/15-aux-inputs-theory-id-vs-ood.png)

这里的逻辑很重要：`z` 不是天然“坏特征”，它在源域确实有预测力；问题是它作为输入时容易变成 spurious shortcut，因为模型会直接利用源域里 `z` 和 `y` 的相关性。

所以 aux-inputs 的失败不是因为 auxiliary information 没有价值，而是因为它被放在了太直接的位置上。只要 `z` 作为测试时输入出现，模型就可能依赖 `z -> y` 的源域相关性。一旦这个相关性在目标域改变，模型就会被误导。

## 5. Baseline 2：把 auxiliary information 当预训练输出

![aux-outputs](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/10-aux-outputs-pretraining-pipeline.png)

第二种方法是 aux-outputs：不把 `z` 输入最终分类器，而是先训练模型从 `x` 预测 `z`。这相当于用辅助任务做预训练。直觉是，如果模型能从卫星图像预测气候、地理或时间信息，它就必须学习图像里更稳定的高层结构，例如植被、水体、地形、季节性模式。

预训练完成后，再用 labeled source data 微调模型做 `x -> y`。注意，这时最终预测阶段不再输入 `z`，所以模型不会直接依赖目标域中可能漂移的 `z`。

这个方法的优点是 OOD robustness 更好，因为它利用 `z` 学表示，却不把 `z` 当 shortcut 使用。缺点是 ID 表现可能不如 aux-inputs，因为最终模型没有直接使用 `z` 的即时预测信息。

这里可以把 aux-outputs 理解成一种“间接使用 `z`”的策略。`z` 不再作为预测时的条件变量，而是作为训练表示时的监督信号。它告诉模型：哪些视觉结构、空间结构或环境结构值得学。但最终分类器仍然只看 `x`，所以它不会在 OOD 测试时依赖一个已经漂移的 `z`。

## 6. In-N-Out：self-training 把两种模型接起来

![in-n-out](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/12-in-n-out-algorithm.png)

In-N-Out 的目标是把 aux-inputs 的 ID 优势和 aux-outputs 的 OOD 优势接起来。它不是简单地同时把 `z` 当输入和输出，因为那样模型可能学到 `z -> z` 的恒等映射，直接忽略 `x`。

算法按顺序可以读成四步：

1. 先训练 aux-inputs 模型 `(x, z) -> y`。
2. 用这个模型给无标签 in-domain `(x, z)` 生成 pseudo-label。
3. 另一路先训练 aux-outputs 模型，即用 `x -> z` 做预训练。
4. 最后用真实标签和 pseudo-label 一起微调 aux-outputs 初始化出的模型，得到 In-N-Out 模型。

这一步里 self-training 的作用非常具体：它不是抽象地“利用无标签数据”，而是把 aux-inputs 模型在 ID 上得到的预测能力，通过 pseudo-label 转移给不依赖 `z` 输入的 aux-outputs 模型。

所以 In-N-Out 的核心不是一个复杂架构，而是一种信息搬运机制：`z` 作为输入时有强预测力，但不稳；`z` 作为输出时能学稳健表示，但 ID 精度不够。self-training 把前者的预测力迁移到后者的稳健模型里。

这也是 talk 标题里 self-training 的重点。伪标签不是为了“凭空增加标签”，而是为了让一个模型把它在某个结构下学到的预测能力转交给另一个更适合 OOD 的模型。这里有三种对象：

1. aux-inputs teacher：ID 上强，但 OOD 不稳；
2. aux-outputs representation：OOD 上更稳，但 ID 信息利用不充分；
3. pseudo-label：把 teacher 的预测力转移给最终模型的中介。

如果没有这个中介，aux-inputs 和 aux-outputs 就只是两个各有缺陷的 baseline。

## 7. 线性模型分析：为什么这件事可能成立

![robustness-analysis](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/16-aux-outputs-theory-robustness.png)

Liang 接着用 multitask linear regression 解释这个现象。设输入 `x` 里有一个低维 latent feature `w`，而另一个 latent variable `u` 同时影响目标 `y` 和辅助变量 `z`。关键设定是：`u` 会在源域和目标域之间 shift。

这个设定下，aux-inputs 的行为就清楚了。因为 `z` 能帮助恢复 `u`，而 `u` 又对 `y` 有用，所以在源域里把 `z` 当输入会提高预测精度。但如果 `u` 的分布在目标域变了，`z` 和 `y` 的关系也会变，模型就可能 OOD 失效。

aux-outputs 的逻辑不同。预训练 `x -> z` 会迫使模型从 `x` 中抽取能解释 `z` 的低维结构，相当于更好地识别稳定子空间。这样做把后续预测问题从原来的高维 `d` 维问题收缩到更低维的 `k` 维问题，因此样本复杂度和 OOD 风险都可能降低。

最后，In-N-Out 通过 pseudo-label 增加训练信号。只要 `z` 能减少 `y|x` 的不确定性，aux-inputs 生成的 pseudo-label 就会比普通模型更准；而这些 pseudo-label 又被用来训练一个最终不依赖 `z` 输入的模型。因此它既利用了 `z`，又避免在测试时被 `z` 的 shift 直接拖垮。

用一句话概括这段理论分析：

> auxiliary variable `z` 可以作为训练时的结构信息，但最好不要作为 OOD 测试时的直接依赖。

In-N-Out 的设计正是在这个边界上做文章。它让 `z` 参与训练，但不让最终预测函数直接以 `z` 为输入。

## 8. 第二条结构：gradual domain adaptation

![gradual-shift](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/20-gradual-domain-setup.png)

第二类结构是 gradual shift。这里不再依赖辅助变量，而是利用源域和目标域之间存在一系列中间域。

所谓中间域，指的不是一个额外标签，也不是某个单独变量，而是 source domain 和 target domain 之间的过渡数据分布。可以把它写成一串 domain：

```text
D_0 -> D_1 -> D_2 -> ... -> D_T
```

其中 $D_0$ 是有标签的 source domain，$D_T$ 是最终想适应的 target domain，中间的 $D_1,\ldots,D_{T-1}$ 是无标签或少标签的 intermediate domains。关键要求是：$D_0$ 和 $D_T$ 可以相距很远，但相邻两个域 $D_t$ 和 $D_{t+1}$ 的变化要小。

中间域通常来自问题本身的连续轴，而不是算法凭空发明出来的。例如：

- 时间轴：1905 年照片是 source，1973 年照片是 target，那么 1910、1920、1930、... 这些年份的数据就可以形成中间域。
- 空间轴：一个地区是 source，另一个远处地区是 target，那么两者之间相邻城市、相邻 PUMA、相邻气候带可能形成中间域。
- 风格或传感器轴：清晰图像到雾天图像、白天到夜晚、旧相机到新相机，如果变化强度可以分级，也可以形成中间域。
- 任务难度轴：轻微旋转的 MNIST 到大角度旋转的 MNIST，中间角度就是中间域。

所以，中间域的来源有两种。第一种是数据本来就带有时间、空间、年龄、年份、地理位置、设备类型等 metadata，可以按这些轴排序或分箱。第二种是人为构造 domain path，例如逐步旋转图像、逐步改变风格强度，或者用生成模型在 source 和 target 之间合成过渡样本。但第二种更危险，因为构造出来的路径必须保留任务相关语义，否则只是视觉上平滑，不一定对分类有用。

因此，gradual shift 的核心假设不是“我总能找到中间域”，而是：这个具体问题的 domain shift 是否真的沿某条可解释轴连续发生。如果 source 和 target 之间没有这样的路径，那么 gradual self-training 就没有可走的桥。

源域和目标域可能相距很远，但相邻两个域之间变化很小。

例子是从 1905 年到 1973 年的人像分类。源域是早期照片，目标域是晚期照片，中间年份构成一条逐渐变化的路径。直接把源域分类器用到目标域会失败，因为服饰、发型、图像风格都发生了变化。

![gradual-example](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/21-gradual-domain-example.png)

普通 self-training 是一步跳到目标域：源域训练分类器，给目标域打伪标签，再用伪标签训练。这通常不够，因为目标域离源域太远，初始伪标签已经错得太多。

Gradual self-training 则是一小步一小步走。先在有标签源域 $D_0$ 上训练分类器；然后用这个分类器给第一个无标签中间域 $D_1$ 打伪标签；再用 $D_1$ 的伪标签训练或更新分类器；接着用更新后的分类器去处理 $D_2$；如此重复，直到最后的目标域 $D_T$。

这一步可以理解成沿着 domain path 搬运预测能力。每次模型只需要跨过一个小 shift，而不是从 source 一步跳到 target。只要相邻域足够接近，当前模型在下一域上的伪标签就不会一开始错得太离谱，self-training 才有机会稳定推进。

这一条线和 auxiliary information 那条线的区别在于：这里没有一个额外变量 `z` 可以帮你学表示。可利用的结构变成了 domain sequence 本身。中间域提供了一条“可走的路”，self-training 的作用就是沿这条路逐步搬运预测能力。

换句话说，auxiliary information 里用来搭桥的是样本内部的额外变量 `z`；gradual shift 里用来搭桥的是样本分布之间的连续路径 $D_0\to D_1\to\cdots\to D_T$。

## 9. 为什么 gradual self-training 需要“小步变化”

![gradual-self-training](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/22-gradual-self-training.png)

这部分的理论直觉是：如果相邻域之间的变化小于分类 margin，那么当前分类器虽然不是完美的，但仍然能给下一域产生足够可靠的伪标签。每一步都只承担一个小 shift，错误不会立刻失控。

如果完全不做 self-training，源域分类器会 stale。也就是说，随着真实最优分类边界逐渐移动，旧分类器不更新，最终会在目标域系统性错误。

![stale-classifier](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/24-source-classifier-stale.png)

Liang 强调，这不是普通 covariate shift。这里最优分类器本身可能随时间变化。Gradual self-training 的作用，就是让分类器沿着变化路径持续追踪新的边界。

这句话非常关键。普通 covariate shift 往往假设 `p(x)` 变了，但 `p(y|x)` 或最优决策规则不变；而 gradual domain adaptation 允许最优分类器本身慢慢改变。如果边界本身会动，那么不更新分类器就会 stale。Gradual self-training 正是用无标签中间域来持续更新边界。

## 10. 理论结果和两个实践细节

![results](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/25-theory-results.png)

理论上，gradual self-training 的误差上界会随迭代次数出现 compounding。如果初始误差足够小，结果仍然非平凡；如果初始误差太大，错误会逐步放大。换句话说，gradual self-training 不是魔法，它依赖初始模型不要太差，也依赖每一步 shift 不要太大。

Liang 提到两个实践细节。

第一个是 regularization。没有正则化时，模型可能找到任意低训练损失的边界，而不是 margin 更大的边界。这样即使相邻域变化很小，边界附近的样本也容易被翻转，理论假设和实践表现都会崩。

第二个是 label sharpening。做 self-training 时，如果模型给出 0.6/0.4 的软标签，而你继续用软标签训练，模型可能只是复现自己，不真正移动边界。把伪标签 harden 成类别标签，反而能推动分类器向下一域适应。

## 11. “gradual” 不是任意插值

![wasserstein-shifts](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/29-wasserstein-infinity-shifts.png)

Talk 里还区分了两种“小”。这一步很重要，因为 gradual self-training 需要的不是任意意义上的“小变化”，而是对分类器来说可跟上的小变化。

第一种“小”，是样本级的小移动，也就是 Wasserstein-infinity 意义上的小变化。直观地说，每一个样本从当前域到下一域时都只移动一点。以 MNIST 旋转为例，如果当前域是旋转 $0^\circ$ 的数字，下一域是旋转 $5^\circ$ 的数字，那么每张图像都只是轻微旋转。分类器原本能识别 $0^\circ$ 的数字，通常也还能大致识别 $5^\circ$ 的数字，于是它给下一域打出的伪标签不会一开始就大面积崩掉。

这类路径对 gradual self-training 是友好的，因为它满足“逐步可追踪”的要求。分类边界虽然可能慢慢变化，但每一步变化都还在当前分类器的 margin 附近。模型用当前域训练出来以后，跨到下一域时仍然有足够可靠的 pseudo-label；再用这些 pseudo-label 更新模型，就能继续追踪后面的变化。

第二种“小”，只是分布混合比例上的小变化。例如，当前域里有 $99\%$ 的未旋转 MNIST 和 $1\%$ 的旋转 $60^\circ$ MNIST；下一步变成 $98\%$ 未旋转和 $2\%$ 旋转 $60^\circ$；再下一步变成 $97\%$ 和 $3\%$。从 KL divergence 或总分布比例来看，每一步变化可能很小，因为分布质量只是挪动了一点点。

但这对分类器未必是“小变化”。原因是那 $1\%$ 新出现的样本不是从 $0^\circ$ 轻轻移动到 $5^\circ$，而是直接跳到了 $60^\circ$。对当前分类器来说，这些样本可能已经落在它完全不会处理的区域。即使它们在总分布里只占很小比例，它们本身也是“大跳跃”的目标样本。

所以，KL 等分布距离上的平滑，不等于任务意义上的平滑。KL 只关心整体概率质量变化了多少；gradual self-training 真正需要的是：下一域里的每个重要样本都不要离当前域太远。否则模型面对的不是一条可以走过去的桥，而是一边慢慢往数据里混入已经很远的目标样本。

因此，后者虽然在统计距离上看起来 gradual，但对伪标签机制并不 gradual。分类器一开始就会给那些远距离目标样本打错标签，然后 self-training 会把这些错误标签当作训练信号继续强化，最终不一定能适应目标域。

这点对理解方法边界很关键。Gradual domain adaptation 需要的是任务相关的连续路径，而不是任意统计距离上的插值。路径要让分类器能从当前域可靠地迁移到下一域。

这也解释了为什么“用生成模型合成中间域”这个 Q&A 问题很有意思但不自动成立。生成模型确实可能在 source 和 target 之间插值，但插值路径必须是任务相关的。如果插值只是在视觉上平滑，却让类别边界变得不可解释，self-training 仍然可能失败。

## 12. Q&A：OOD 需要更细的语言

Q&A 中最重要的观点是：OOD 不是一种具体现象，而是 ID 的补集。只说 OOD 太粗糙，无法指导方法设计。真正需要的是描述 shift 的结构语言，例如 auxiliary information、gradual shift、conditional independence、subpopulation shift、adversarial shift 等。

Liang 还把 self-training 比喻成一种旧但有用的工具。它像 shovel，把一个模型或一个域里的预测能力搬运到另一个模型或另一个域里。在 auxiliary information 里，它把 aux-inputs 的 ID 预测力搬给 aux-outputs 模型；在 gradual shift 里，它把源域预测力沿中间域一步步搬到目标域。

Q&A 里还讨论了一个很有启发的问题：能不能用 generative model 在源域和目标域之间合成中间域，从而制造 gradual shift？Liang 的回答是，这个想法值得尝试，但关键要看插值路径是否保留任务相关结构。如果生成插值穿过奇怪的 latent 空间区域，或者没有保持 `y|x` 的可分类结构，那么它未必满足 gradual self-training 的理论条件。

## 13. 对当前研究框架的启发

这场 talk 对我们的研究框架有三个直接启发。

第一，不能把 domain shift 只说成“训练分布和测试分布不同”。需要继续问：shift 是由 auxiliary variable 引起的，还是沿某条时间、空间、社会经济轴逐步变化，还是由未观测混杂因素造成？

第二，self-training 的核心是预测力迁移。它不是简单“用伪标签扩数据”，而是在不同模型、不同域、不同结构信息之间搬运可用预测信号。

第三，伪标签是否有用取决于路径结构。如果从 source 到 target 是一步跳跃，pseudo-label 容易自我强化错误；如果中间存在可信路径，self-training 才可能稳定工作。

![final remarks](../../slides/38955373-self-training-algorithms-and-analyses-for-unsupervised-domain-adaptation/curated/31-final-remarks.png)

## 14. 两条方法线的对照

这场 talk 可以压缩成一个方法对照表。

| 结构 | 已知信息 | 困难 | self-training 的角色 | 关键风险 |
| --- | --- | --- | --- | --- |
| auxiliary information | 源域有 `(x,y,z)`，源域和目标域有 `(x,z)` | `z` 有用但会漂移 | 把 aux-inputs 的 ID 预测力转移到 aux-outputs 模型 | 直接用 `z` 会学 shortcut |
| gradual shift | 有源域标签，有一串无标签中间域 | source 到 target 太远 | 沿中间域逐步更新分类器 | 一步变化太大时伪标签会错 |

两者的共同点是：self-training 都不是单独工作。它必须依赖某种“结构性桥梁”。

在 In-N-Out 中，桥梁是 `z`；在 gradual self-training 中，桥梁是 intermediate domains。没有桥梁时，self-training 只是在已有模型的错误上自我循环。

## 15. 和我们当前研究问题的连接

这场 talk 对我们做条件生成、合成人口或城市系统建模很有启发，因为我们的数据里也经常出现类似结构。

第一，census summaries、marginals、PUMA-level constraints 等变量很像 auxiliary information。它们对目标 joint distribution 有约束力，但不能简单当作完整真相。直接把这些 summaries 当输入，模型可能学到局部 shortcut；完全不用，又会浪费结构信息。更合理的问题是：哪些变量应该作为条件输入，哪些变量应该作为辅助任务或表示学习目标？

第二，城市、地区、年份、收入层级、空间邻近关系可能形成 gradual shift。不同 PUMA 或不同年份之间不一定是孤立 domain，而可能存在空间或时间上的连续路径。如果这种路径存在，模型可以考虑沿路径迁移，而不是从一个 source distribution 直接跳到 target distribution。

第三，这场 talk 提醒我们，OOD 不能只作为一个口号。我们需要给自己的研究问题定义更细的 shift taxonomy。例如：

1. spatial shift：不同城市或不同 PUMA 的空间结构差异；
2. temporal shift：年份变化导致人口、迁移或访问模式变化；
3. measurement shift：summary statistics、survey、mobility records 的采样机制不同；
4. latent composition shift：不同人群组成、家庭结构、收入结构变化；
5. constraint shift：给定 marginals 或 aggregate constraints 不同。

如果能把这些 shift 说清楚，后面的生成模型设计才不会只是在“给条件、生成目标”之间机械映射，而是可以明确说明模型到底借用了哪一种结构。
