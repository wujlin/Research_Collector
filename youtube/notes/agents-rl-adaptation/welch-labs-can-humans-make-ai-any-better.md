# Welch Labs: Can humans make AI any better?

- Video: [Can humans make AI any better?](https://www.youtube.com/watch?v=2hcsmtkSzIw)
- Channel: Welch Labs
- Duration: 23:38
- Transcript: `youtube/transcripts/2hcsmtkSzIw-can-humans-make-ai-any-better/`
- Slides: `youtube/slides/2hcsmtkSzIw-can-humans-make-ai-any-better/semantic_curated/`

这期视频围绕 Richard Sutton 的 bitter lesson 展开，但重点不是复述“算力胜过人工知识”这句话，而是追问：LLM 到底是 bitter lesson 的正例，还是下一轮会被 bitter lesson 超越的负例。视频通过语音识别、AlphaGo、LLM 预训练和 reinforcement learning 串起一条线：人类知识可以提供启动结构，但真正超越人类知识，往往需要系统从环境反馈中学习。

## 1. 00:00-05:28：Harpy 说明人工知识能赢一阵，但难以扩展

视频从 1970 年代 ARPA speech recognition 项目讲起。Carnegie Mellon 的 Harpy 达到了识别千词词汇表的目标，它的核心是一个庞大的 knowledge graph。节点表示 phone，边表示这些 phone 如何组成合法句子；专家还要写 grammar、pronunciation graph 和 juncture rules，处理词与词之间发音变化。

Harpy 的成功说明人工知识非常有用。问题是，它的扩展代价太高。随着词汇表、语境和说话方式变复杂，手工 grammar 和规则越来越难维护。

之后 hidden Markov models 取代了 Harpy 式系统。HMM 仍然可以看成图，但图上的转移概率由数据学习，而不是由语言专家逐条指定。这条转变后来成为 Sutton bitter lesson 的典型例子：手工知识可以让系统早期表现更好，但最终会被更通用、能利用计算和数据的方法取代。

## 2. 05:25-08:54：Sutton 认为 LLM 也可能是“负面的 bitter lesson 案例”

GPT-2 发布后，很多人觉得 transformer 加 next-token prediction 加 massive compute 正是 bitter lesson 的胜利：一个通用架构、一个简单目标、大规模计算，就能产生强语言能力。

但 Sutton 在 2025 年访谈中的看法更微妙。他承认 LLM 利用了巨大计算，但也指出 LLM 训练数据是人类生成文本，里面包含大量人类知识、偏见、概念和发现。也就是说，LLM 不只是从环境经验中学习，而是在模仿人类已经写出来的东西。

这让 LLM 很像 Harpy 的升级版：不是规则由专家手写，而是人类知识以互联网文本的形式进入模型。Sutton 的担心是，真正可扩展的智能可能来自 agent 自己从 experience 中学习，而不是继续扩大人类文本的 imitation。

## 3. 09:21-14:39：next-token prediction 是监督模仿，AlphaGo 展示了从经验中超越模仿

视频接着把 LLM 预训练和 AlphaGo 的第一阶段作类比。LLM 给定前文预测下一个 token；AlphaGo 的 policy network 给定棋盘位置预测专家棋手下一步。两者都是 supervised learning，都在学习人类行为分布。

AlphaGo 的关键突破不是只模仿人类棋谱，而是进入 self-play reinforcement learning。模型和自己对弈，胜者路径成为正信号，败者路径成为负信号。训练信号从“专家会怎么下”变成“这一步最后是否带来胜利”。

这一步很关键，因为环境反馈可以揭示人类没有展示过的策略。AlphaGo 后来的风格被人类棋手形容为异质、陌生、来自另一个维度，正是因为它不再只受人类棋谱约束。

## 4. 14:35-17:35：value function 和 tree search 让 agent 不只会下一步模仿

视频强调 reinforcement learning 里另一个核心对象：value function。policy 回答“下一步做什么”，value function 回答“当前状态未来有多好”。AlphaGo 的 value network 估计从某个棋盘位置开始最终获胜的概率。

把 policy network、value network 和 Monte Carlo tree search 合在一起，AlphaGo 就不仅是在模仿下一步，而是在搜索未来分支、评估局面价值、选择长期更好的路径。AlphaGo Zero 更进一步，不用任何人类棋谱，只通过自我对弈学出更强棋力。

这条线和 LeCun 对 VLA 的批评有共鸣：可靠 agent 不应该只是根据当前 observation 直接输出 action，而应该能评估行动后果和未来价值。

## 5. 17:33-20:37：LLM 已经开始用 RL，但经验时代还没有真正到来

视频也没有把 LLM 和 RL 对立起来。现代 LLM 已经在后训练阶段使用 RLHF，把模型行为对齐到人类偏好；推理模型还用 RLVR，在数学和代码等可验证任务上通过 reward signal 发现更好的解题路径。

Silver 和 Sutton 的 “Era of Experience” 把这个方向推得更远：未来 agent 应该从真实世界 reward 中学习，例如成本、健康指标、气候指标、利润、能源消耗，而不是主要从人类已有文本中吸收知识。只有和现实交互，系统才可能推翻旧的人类思维范式，而不只是复述它。

视频作者对“RL renaissance 是否近在眼前”保持谨慎。游戏、数学证明、代码这些领域有明确规则或可验证反馈；厨房、医院、公司、城市和气候系统则开放得多、反馈慢得多、风险也高得多。因此，RL 可能是方向，但它不是一句口号就能解决现实 agent 的数据和安全问题。

## 6. 与本项目的连接

这期视频适合接到 David Silver 的 Era of Experience、Sutton 的 RL 传统、LeCun 的 world model 以及 VLA/robotics 线。

它留下的核心问题是：人类数据到底是 scaffold 还是 ceiling。对当前 LLM 来说，人类文本提供了强启动；但如果目标是发现新科学、新控制策略、新城市干预或新材料设计，仅靠 imitation 人类已有语料可能不够。更可扩展的路线需要 agent 在可验证或可模拟环境中获得自己的经验，并把 experience 转成 policy、value 或 world model。
