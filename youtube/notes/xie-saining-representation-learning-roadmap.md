# 谢赛宁的表征学习主线：怎么理解，以及怎么比较不同模型的表征

- Source interview: [xie-saining-world-model-interview.md](./xie-saining-world-model-interview.md)
- Core transcript anchor: [transcript.md](../transcripts/BV1tew5zVEDf-对谢赛宁的7小时马拉松访谈世界模型逃出硅谷反openaiami-labs两次拒绝ilya杨立昆李飞飞和42/transcript.md)

## 先说结论

谢赛宁说“我是做表征学习的人”，不是在给自己贴一个流行标签，而是在做一个刻意的研究定位。

这句话背后有 3 层意思：

1. 他想研究的是更稳定、更底层的问题，而不是某个短期热点。
2. 他把不同任务看成树枝，把表征看成树根。
3. 他后面的 `MoCo`、`MAE`、`3D SSL`、`diffusion representation`、`JEPA / world model`，在他自己那里不是断裂转向，而是一条连续的主线。

## 1. 他自己怎么定义表征学习

访谈里他给了一个很明确、也很实用的定义。

从数学上说，表征学习就是：

- 你有原始数据 `x`
- 你要把它映射到另一个空间
- 这个空间具有某些“好性质”
- 这些性质会让下游任务更容易做

所以本质上，表征学习研究的是：

`如何学习一个从原始观测到有用状态空间的映射。`

这里有两个关键补充。

第一，这个映射不只是扁平映射，而往往是层级化的。  
第二，真正重要的不是“压缩一下数据”，而是学到对 decision making、generalization、transfer 更有用的结构。

这也解释了为什么他后面会自然走向 `world model`。因为一旦你把问题表述成“学状态空间”，下一步自然就是问：

- 这个状态怎么演化？
- 哪些状态变量才值得保留？
- 这个表征能不能支持 prediction / planning？

## 2. 为什么他坚持用 `representation learning` 这个 title

他对这个 title 的偏好，其实很清楚：

- `representation` 是 fundamental problem
- 它是 relatively evergreen 的 problem
- 它不像 `NAS` 那样，可能两年后就被证明是局部潮流甚至错误方向

所以他坚持说自己是做表征学习的人，本质上是在说：

`我不想把自己的研究身份绑定在某个短周期技术名词上，而是绑定在一个长期未解的核心问题上。`

这也是他最值得借鉴的地方之一。  
不是“拒绝热点”，而是：

`用更高一层的问题，把热点重新组织进去。`

## 3. 我怎么理解他的主线

如果把访谈里的研究线压成一句话，我会写成：

`从更好的视觉表征出发，逐步走向更一般的预测性表征，最后把表征学习推进为世界模型与认知架构的问题。`

这条线不是：

`CV -> 多模态 -> 创业`

而是：

`architecture -> SSL -> scalable representation -> predictive representation -> world model`

## 4. 他研究线里的几次关键转向

### A. 早期阶段：architecture 和 structured priors

他博士论文的题目本身已经说明问题：

`deep representation learning with induced structural priors`

这个阶段的重点不是“已经找到终极方法”，而是先确认：

- 更好的 architecture 可以帮助学更好的 representation
- 结构化先验是有价值的
- 表征问题并不等于单一任务表现

这一段对应的是早期视觉深度学习时期常见的思路：

- 通过架构设计改善学习能力
- 通过 inductive bias 提升特征质量
- 典型代表可以放在 `Deeply-Supervised Nets / HED / ResNeXt` 这一带

这时他的关心点已经不是“某个任务分数”，而是“架构如何影响表征质量”。

### B. Fair 阶段：自监督与 scalable representation

这是他主线第一次真正收束。

在他的叙述里，Fair 阶段一个核心转变是：

- 不再把 `architecture` 当成全部
- 明确看到 `architecture + data + objective` 三者一起决定表征质量

这一步很重要，因为它把“做网络结构”升级成了“研究表征形成机制”。

在这条线上，`MoCo` 的意义不是一篇著名论文这么简单，而是：

- 对比学习重新定义了视觉自监督学习的有效范式
- 它告诉大家，表征可以在没有人工标签的情况下通过结构化目标学出来
- 它也把 `scaling` 这个问题真正带进了视觉 SSL

如果压成一句话，`MoCo` 在这条主线里的角色是：

`证明高质量视觉表征可以通过自监督目标被稳定训练出来。`

### C. 从 MoCo 到 MAE：从 invariance 优先转向 reconstruction 优先

访谈里他对 `MAE` 的描述非常重要，因为它说明他不是在给自己的旧工作做英雄叙事，而是在认真区分不同表征的性质。

`MAE` 这一步的关键不是“mask 一下图像”，而是研究焦点发生了变化：

- 对比学习更强调 invariance
- masked modeling 更强调从不完整观测中恢复结构

他提到一个很关键的经验判断：

- `MAE` 学到的表征在线性探针上未必最强
- 但在 end-to-end fine-tuning 下可能更有优势

这个判断很值钱，因为它说明：

`表征好坏不是单一标尺。`

有些表征更适合：

- frozen feature
- linear separability

有些表征更适合：

- adaptation
- task-specific refinement

所以 `MoCo` 和 `MAE` 不是“谁替代谁”的关系，而更像是：

`两种不同的表征偏好。`

### D. 3D / embodied / beyond image：表征问题不是 image-only 的

他提到把 SSL 拓展到 3D 和 point cloud，这里最重要的信息不是论文名本身，而是方法论上的扩展：

`representation learning is not an image-domain trick.`

也就是说，他逐步确认：

- 表征学习是跨模态、跨观测形式的
- 不同传感形式都可以被放进“学状态”的统一问题里

这一步是后面走向 `world model` 的必要过渡，因为没有这一步，表征学习很容易一直停留在 2D image benchmark 的局部最优里。

### E. diffusion representation：生成模型也许能学表征，但还不够

访谈里他还提到，他们认真比较过：

- diffusion model 学到的表征
- supervised / self-supervised 学到的表征

他的阶段性结论并不模糊：

- 生成模型能学到一些不错的表征
- 但在他们当时的判断里，和成熟的 SSL 表征相比，仍然差不少

这里的重点不是“diffusion 不行”，而是：

`能生成，不等于学到了最适合下游理解和控制的表征。`

这一步在他的路线里扮演的是反例和校准器的角色。它迫使问题继续上移：

- 真正重要的表征到底应该服务什么？
- 是线性分类？
- 是生成质量？
- 还是 prediction / planning / decision making？

### F. JEPA / world model：表征学习被重新抬升到认知架构

这一步是整条主线的再定义。

在他的理解里，JEPA 不再只是 “yet another SSL algorithm”，而是一种更接近认知架构的思路。也正是在这里，表征学习不再只是“学 feature”，而变成了：

- 学 latent state
- 学 predictive structure
- 学 support reasoning / planning 的内部表征

所以在他的最终叙事里：

`world model 不是离开 representation learning，而是 representation learning 的上升。`

## 5. 不同模型的表征应该怎么比较

这是你问得非常对的一点。

如果只问“哪个表征更好”，问题太粗。更准确的问法应该是：

`这个表征对什么任务、以什么接口、在什么约束下更好？`

我建议至少分 6 个维度比较。

### 1. 线性可分性

最常见的是 `linear probe`。

它回答的问题是：

`如果我冻结特征，只用很弱的读出头，这个表征本身是否已经把结构整理好了？`

优点是干净。  
缺点是它偏爱某些强 invariance 的表征，不一定等于真实最好。

### 2. 可适配性

也就是 full fine-tuning 或 task-adaptive tuning。

它回答的问题是：

`这个表征是否给下游任务留下了足够可塑的结构？`

这正是 `MAE` 和对比学习差异容易显出来的地方。  
有些表征未必最线性可分，但 fine-tune 以后更强。

### 3. 不变性和保真性之间的平衡

表征不是越 invariant 越好。

如果你把所有细节都抹掉，分类也许更轻松，但 prediction、control、world modeling 会变差。  
所以需要问：

- 它保留了多少 task-relevant variation？
- 它丢掉了多少 nuisance variation？

这是 `contrastive` 和 `masked modeling` 经常分岔的地方。

### 4. 时间预测能力

如果你关心的是动态系统，那就不能只看分类。

应该问：

- 给定当前表征，它能否支持预测未来状态？
- 它是否足够 Markov？
- 它是否保留了 planning 所需的信息？

这一步是把“图像特征”升级成“状态表征”的关键。

### 5. 跨模态和 grounded alignment

语言参与以后，表征会变得更方便读出，但也可能被语言污染。

所以要区分两件事：

- 它是否和语言对齐得更好？
- 它是否因此牺牲了对真实世界结构的保真？

这也是为什么谢赛宁会反复担心语言对视觉表征的污染。

### 6. OOD、干预和控制下的稳健性

如果你最后关心 `world model` 或机器人，那么评价表征就不能停留在 IID benchmark。

还要问：

- 分布变了以后还能不能用？
- 加入 action / intervention 以后还能不能预测？
- 是否能区分 feasible 和 infeasible future？

这是 `representation` 真正走向 `state` 的分水岭。

## 6. 一个更稳的比较框架

所以我会建议你把“比较不同模型表征”这件事，固定成下面这张逻辑表：

- `classification-oriented`
  看 linear probe、few-shot transfer、冻结特征质量。
- `adaptation-oriented`
  看 fine-tuning、task adaptation、sample efficiency。
- `dynamics-oriented`
  看 next-state prediction、memory sufficiency、planning support。
- `physics-oriented`
  看是否保留连续结构、约束、因果方向、可逆/不可逆信息。

只要这四类不分开，关于表征的争论就很容易变成鸡同鸭讲。

## 7. 我对他整条研究线的总理解

如果压成最短的一句，我会这样写：

`谢赛宁真正关心的，不是某一种训练技巧，而是怎样学出足够好的内部状态表示，使系统能从感知走向理解，再从理解走向预测与规划。`

所以：

- `MoCo` 是表征学习的有效范式化。
- `MAE` 是表征学习目标函数的一次重构。
- `3D / embodied extension` 是表征问题的域扩展。
- `diffusion representation` 是一次重要但不彻底成功的探路。
- `JEPA / world model` 是把表征学习提升成认知架构问题。

## 8. 对你最有价值的借鉴

这条主线对你最有价值的地方，不是去记他做过哪些名作，而是这三个研究习惯：

1. 不用短周期技术名词定义自己，而用长期问题定义自己。
2. 不把不同论文看成离散成果，而把它们看成同一棵树上的不同分叉。
3. 一旦评价表征，就明确“你到底在拿什么标准评价”，避免把所有任务揉成一个模糊的“更好”。

如果再往你自己的方向翻译一步，那这条线几乎可以改写成：

`如何为真实的非平衡动力系统，学到足够好的可预测状态表示。`

从这个角度看，你和他真正接得上的地方，恰恰不是大模型叙事本身，而是：

`representation as state construction`

也就是，表征不是 feature trick，而是状态构造问题。
