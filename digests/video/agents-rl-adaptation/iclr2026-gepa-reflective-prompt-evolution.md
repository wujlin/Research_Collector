# GEPA：把强化学习的“数值奖励”改写成 text-space reflective optimization

- Video: https://www.youtube.com/watch?v=HbGah-uP1fI
- Transcript: `youtube/transcripts/HbGah-uP1fI-iclr2026-oral-gepa-reflective-prompt-evolution/transcript.md`
- Slides: `youtube/slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/`
- Speaker: Lakshya A. Agarwal

## 1. 起点：怎样让 AI 学会新任务

GEPA 的问题很直接：面对一个新任务，我们怎样让 AI 系统变得更好？

![Teach AI new tasks](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/01-teach-ai-new-tasks.jpg)

标准路径是更新模型权重。预训练需要海量 token，SFT 需要大量标注样本，RL 需要大量 rollout。这个路线有效，但 sample efficiency 很差。对于真实任务，这个问题会被放大，因为很多领域没有足够的 domain-specific training data。

![Sample efficiency challenge](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/02-sample-data-efficiency-challenge.jpg)

第二个瓶颈是 rollout 本身很贵。agent 工作流可能要调用工具、访问数据库、等待真实环境反馈或运行长时间 verifier。即使 GPU 更便宜，环境交互和验证过程也可能成为瓶颈。

## 2. 为什么 agent 场景会放大这个问题

现代 LLM agent 不再只是一次性生成答案，而是会调用工具、检索信息、执行代码、等待环境返回结果。系统能力提高了，但每一次 rollout 的成本也更高。

![Agents for real-world applications](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/03-agents-real-world-applications.jpg)

这时如果继续使用传统 RL with verified rewards，训练信号会被压缩得很厉害。模型做了很多中间步骤，但最后只拿到一个 reward，可能是 0 或 1。中间的 chain of thought、tool calls、error messages、environment response 都被丢掉了。

![RL with verified rewards](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/04-rl-with-verified-rewards.jpg)

GEPA 的切入点就是：不要只把 rollout 当成产生 reward 的黑箱，而要把整个 trace 当成可读的诊断材料。

## 3. 核心转向：从 weight update 转向 text-space update

GEPA 的第一层想法是 reflective optimization in text space。模型不只是看 reward，而是读取 rollout trace，分析哪里成功、哪里失败，并把这些诊断写成新的 prompt 或系统说明。

![Reflective optimization](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/05-reflective-optimization-text-space.jpg)

例如在代码任务里，compiler error 可能直接告诉系统某个 API 不存在。传统 RL 可能只看到“这次失败了”；GEPA 则可以利用错误信息，反思下一版 prompt 应该避免这个 API 或改用别的调用方式。

第二层想法是 prompt update 可以产生大行为变化。权重更新通常是小步变化，但自然语言 prompt 的一个词或一句话可能直接改变系统行为。比如把“生成一行摘要”改成“生成十行摘要”，不需要上千次梯度更新。

## 4. GEPA 的基本形式：遗传搜索加 Pareto 选择

GEPA 把 prompts 看成 gene pool。每轮从候选 prompt 中选一个，用 rollout trace 和文字反馈生成 mutation，再把新候选放回池子中评估。

![GEPA overview](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/06-gepa-evolutionary-prompt-optimization.jpg)

这里最重要的不是“它会改 prompt”这个事实，而是它把 prompt optimization 组织成一个 multi-objective process。不同 prompt 可能擅长不同样本；如果只追求一个平均分最高的 prompt，就会丢掉少数样本上很有价值的策略。Pareto pool 的作用是保留这些 per-instance insight。

## 5. 和 GRPO 的对比：为什么 sample efficiency 会高

在 Multi-Hop QA 例子里，GEPA 用很少的数据和几轮 reflection 就达到比 GRPO 大量 rollout 更好的提升。talk 强调的不是绝对 benchmark 排名，而是样本效率差异。

![GEPA vs GRPO](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/07-gepa-vs-grpo-multihop-qa.jpg)

线性地看，这个结果来自三个条件同时成立。第一，rollout trace 本身含有大量诊断信息。第二，LLM 能把这些诊断信息翻译成 prompt-level 修改。第三，prompt-level 修改比权重更新更容易产生大幅行为变化。

## 6. GEPA 学到的不是小技巧，而是完整 system specification

GEPA 生成的 prompt 往往不是几个零散提示词，而是完整系统说明，包括任务定义、隐含需求、解题策略和输出格式。

![Complete system specification](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/08-complete-system-specification.jpg)

这点很重要。随着模型 instruction following 能力增强，精确的任务 specification 本身会变成一种强控制变量。GEPA 的意义不只是自动调 prompt，而是自动发现“这个系统真正应该如何被说明”。

## 7. 算法流程

GEPA 接收一个训练集、一个由 prompts 参数化的 agent，以及一个 evaluation metric。然后把训练集分成 dev 和 val。

![GEPA algorithm](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/09-gepa-algorithm.jpg)

流程可以顺着读：

1. 初始化候选 prompt pool。
2. 记录每个候选在每个 validation item 上的表现。
3. 形成 Pareto frontier，保留不同样本上的强候选。
4. 每轮从 Pareto frontier 选一个 prompt。
5. 用这个 prompt 在 dev mini-batch 上运行 agent。
6. 收集 score、tool feedback、error message 和中间 trace。
7. 调用 LLM 反思并提出新 prompt。
8. 在 val set 上评估新候选。
9. 更新候选池和 Pareto frontier。

这个算法的关键是把“失败的轨迹”变成“可编辑的文本反馈”，而不是只变成一个梯度信号。

## 8. 为什么 Pareto 比简单迭代反思更稳

简单 iterative reflection 容易陷入局部最优。它找到一个不错的 prompt 后，后续预算可能都花在微调这个候选上，而忽略其他样本暴露出的不同失败模式。

![Pareto diversity and quality](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/10-pareto-diversity-quality.jpg)

Pareto 选择保留多个互补候选：有的在样本 A 上强，有的在样本 B 上强。这样 mutation 的出发点不会过早收缩到单一模式，探索和利用之间更平衡。

![Prompt optimizer choices](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/11-prompt-optimizer-choices.jpg)

GEPA 和 prior prompt optimizers 的差异可以概括成三点：per-instance Pareto pool、global LLM reflection、evolutionary tree plus system-aware merge。

## 9. 从 prompt optimization 推到 broader optimization

talk 后半段把 GEPA 放进更大框架：LLM 可以成为 smart proposer。只要一个问题有 evaluator，而且 evaluator 能返回 actionable side information，就可能被改写成 text-parameter optimization。

![Optimization with smarter proposers](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/12-optimization-with-smarter-proposers.jpg)

这里的 side information 可以是 compiler trace、profiler output、SLA violation、retrieval feedback 或 structured validation error。LLM 不需要直接求导，只需要把这些反馈转化成更好的候选方案。

![Optimize anything API](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/13-optimize-anything-api.jpg)

因此 GEPA 的适用对象不只 prompts，还包括 agent harnesses、kernels、numeric parameters 和 algorithms，只要它们能被文本表达、被 evaluator 评分，并且能得到可行动反馈。

## 10. 应用例子和边界

GEPA 被展示在 agent architecture discovery、OCR、复杂信息抽取等任务上。

![Agent architecture discovery](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/14-agent-architecture-discovery.jpg)

![VLM OCR performance](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/15-vlm-ocr-performance.jpg)

![Complex information extraction](../../slides/HbGah-uP1fI-gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning/curated/16-complex-information-extraction.jpg)

但它也有明确边界。GEPA 不是无条件自动学习器。它需要 evaluator，需要可读反馈，需要可被文本参数化的搜索对象。如果一个任务没有可靠评分机制，或者反馈完全不可解释，GEPA 的优势就会下降。

对我们的研究框架来说，GEPA 值得注意的是它把“优化”从连续参数空间部分转移到 text-structured design space。它和 self-training、VI、HJB 的共同点不是数学形式相同，而是都在寻找一种更有效的监督信号重写方式：把原本稀疏、昂贵或难微分的反馈，改写成更可用的训练目标。
