---
title: "Language Agents as Optimizable Graphs"
alias: "GPTSwarm"
source_type: "paper"
venue: "ICML 2024"
authors: "Mingchen Zhuge; Wenyi Wang; Louis Kirsch; Francesco Faccio; Dmitrii Khizbullin; Jürgen Schmidhuber"
published: "2024-02-26"
latest_version: "v3"
collected: "2026-05-24"
arxiv_id: "2402.16823"
url: "https://arxiv.org/abs/2402.16823"
html_url: "https://arxiv.org/html/2402.16823v3"
pdf_url: "https://arxiv.org/pdf/2402.16823v3"
local_pdf: "pdfs/2026-05-24/language-agents-as-optimizable-graphs/language-agents-as-optimizable-graphs.pdf"
project_url: "https://gptswarm.org"
status: "collected_pdf"
topics:
  - ai_agents/agent_graphs
  - multi_agent_systems/optimization
  - prompt_optimization
  - agent_orchestration
---

# Language Agents as Optimizable Graphs

## 采集定位

这篇论文就是视频中说的 GPTSwarm。arXiv 标题是 `Language Agents as Optimizable Graphs`，评论信息显示它发表在 ICML 2024。

它的核心价值是把 LLM agent system 从“手写 prompt pipeline”改写成“可优化的 computational graph”。这对我们最近关心的 multi-agent / generative RL / self-improving agent 很重要，因为它把 agent collaboration 的结构本身变成了优化对象。

## 核心问题

不同 prompt engineering 技巧和 agent workflow 往往是分散实现的。GPTSwarm 的统一口径是：一个 language agent 可以被表示为 graph。

```text
nodes:
  functions, tools, LLM calls, multimodal processors

edges:
  information flow between operations

composite graphs:
  hierarchies of inter-agent collaboration
```

在这个表示下，优化不只发生在 prompt 文本上，也可以发生在 graph connectivity 上：

- node optimization：优化节点内部的 LLM prompt 或处理方式；
- edge optimization：改变 agent 之间或操作之间的信息流连接；
- recursive composition：把多个小 graph 组合成更大的 agent collaboration structure。

## 与研究脉络的连接

它和 MetaGPT 的差异很关键。MetaGPT 把人类 SOP 固化进 multi-agent workflow；GPTSwarm 则进一步问：这个 workflow 本身能否自动优化？

这也可以和 Claude dreaming / outcomes 连起来。dreaming 主要整理经验记忆；outcomes 提供评价信号；GPTSwarm 提供结构优化空间。三者合起来才更接近一个可持续自改进的 agent system。

## 当前状态

- PDF 已下载到本地。
- 这篇目前是资源级采集，尚未精读。
- 如果后续精读，应重点展开 graph representation、node optimization、edge optimization，以及实验中哪些 agent workflow 被自动改进。
