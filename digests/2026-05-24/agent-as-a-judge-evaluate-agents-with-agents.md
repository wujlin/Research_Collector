---
title: "Agent-as-a-Judge: Evaluate Agents with Agents"
source_type: "paper"
venue: "arXiv"
authors: "Mingchen Zhuge; Changsheng Zhao; Dylan Ashley; Wenyi Wang; Dmitrii Khizbullin; Yunyang Xiong; Zechun Liu; Ernie Chang; Raghuraman Krishnamoorthi; Yuandong Tian; Yangyang Shi; Vikas Chandra; Jürgen Schmidhuber"
published: "2024-10-14"
latest_version: "v2"
collected: "2026-05-24"
arxiv_id: "2410.10934"
url: "https://arxiv.org/abs/2410.10934"
pdf_url: "https://arxiv.org/pdf/2410.10934"
local_pdf: "pdfs/2026-05-24/agent-as-a-judge-evaluate-agents-with-agents/agent-as-a-judge-evaluate-agents-with-agents.pdf"
status: "collected_pdf"
topics:
  - ai_agents/evaluation
  - llm_as_judge/agent_as_judge
  - self_improving_agents/reward_signals
  - software_engineering_agents
---

# Agent-as-a-Judge: Evaluate Agents with Agents

## 采集定位

这篇论文属于 agent evaluation 线。它的核心不是“让 LLM 给最终答案打分”，而是把评价对象扩展到 agentic system 的完整任务过程。

它适合和 Claude outcomes / dreaming 放在一起读：

- outcomes 需要一个 rubric-based feedback signal；
- dreaming 需要从历史任务中总结可改进信息；
- Agent-as-a-Judge 试图提供更细粒度、更可靠的 agent-level 评价机制。

## 核心问题

传统 LLM-as-a-Judge 往往只看最终输出。对 agent 来说，这不够。Agent 的失败可能发生在任务分解、工具选择、中间推理、文件修改、测试执行或最终报告等多个环节。如果只评价最终答案，就会丢掉大量过程信息。

Agent-as-a-Judge 的基本想法是：用具备 agentic features 的系统去评价另一个 agent 的完整任务轨迹。这样评价者可以检查中间步骤，而不是只看最终产物。

论文还提出 DevAI benchmark，用于自动化 AI development tasks。这个 benchmark 包含 realistic code-generation / development tasks 和人工标注的 hierarchical user requirements，用来测试 agent evaluator 是否能产生可靠评价。

## 与研究脉络的连接

这篇论文提供的是 self-improving agent 的 feedback layer。如果没有可靠评价信号，agent 的自我改进就很容易变成无监督的记忆整理，无法判断哪些经验真的提高了未来任务成功率。

因此它可以和 GPTSwarm 形成互补：

```text
GPTSwarm:
  optimize agent graph structure

Agent-as-a-Judge:
  provide reward / evaluation signal for agent behavior

Claude dreaming:
  consolidate memory and patterns across sessions
```

## 当前状态

- PDF 已下载到本地。
- 这篇目前是资源级采集，尚未精读。
- 如果后续精读，应重点展开 Agent-as-a-Judge 如何区别于 LLM-as-a-Judge、DevAI benchmark 如何构造、以及评价信号如何服务 dynamic and scalable self-improvement。
