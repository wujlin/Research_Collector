---
title: "Claude's New Dreaming Feature Builds Self-Improving AI Agents"
source_type: "web_article"
publisher: "Forbes"
author: "Jon Markman"
published: "2026-05-11"
collected: "2026-05-24"
url: "https://www.forbes.com/sites/jonmarkman/2026/05/11/claudes-new-dreaming-feature-builds-self-improving-ai-agents/"
status: "collected"
topics:
  - ai_agents/self_improvement
  - multi_agent_systems/enterprise_agents
  - memory_systems/agent_memory
  - bridges/agent_evaluation
---

# Claude's New Dreaming Feature Builds Self-Improving AI Agents

## 采集定位

这不是学术论文，而是一篇产业观察文章。它的价值在于记录 Anthropic 在 Claude Managed Agents 中推出的三个关键能力：dreaming、outcomes、multi-agent orchestration。它可以作为我们理解“agent 如何从一次性工具变成可持续改进系统”的产业入口，但不应被当作理论论文使用。

## 文章主线

文章围绕 Anthropic 的 Claude Managed Agents 展开。核心观点是：如果 agent 能在空闲时回顾过去任务、整理记忆、提取错误模式和偏好，那么它就不再只是每次从零开始的工具，而更像一个会随使用历史积累的工作系统。

这里的 dreaming 可以理解成一种异步 memory consolidation workflow。它不是修改底层模型参数，而是在 agent 的记忆层上做整理：

- 合并重复信息；
- 删除过时信息；
- 标记反复出现的错误或团队偏好；
- 重组 memory store，让未来任务能使用过去经验。

文章还把 dreaming 和 outcomes、multi-agent orchestration 放在一起读。outcomes 让 agent 根据 rubric 评估自己的工作；multi-agent orchestration 让一个 agent 协调多个 sub-agents。三者合在一起，对应一个闭环：

```text
agent execution
  -> outcome evaluation
  -> memory consolidation / dreaming
  -> improved future execution
  -> multi-agent coordination
```

## 与研究脉络的连接

这篇文章可以接到我们最近读的 agent / RL / generative AI 线。

第一，它和 Agent-as-a-Judge 有直接连接。Agent-as-a-Judge 关心如何用 agent 评价 agent，从而提供更细粒度、更可扩展的反馈信号。Forbes 文章中的 outcomes 是产业版本的同类问题：如果 agent 要自我改进，就必须有可操作的评价信号。

第二，它和 self-supervised RL / skill learning 有间接连接。Eysenbach 那条线关心 agent 如何从自身经验中形成 reusable behavior structure；这里的 dreaming 更偏记忆层和任务经验整理，但共同点都是：系统不只执行当前任务，还要把经验转化成后续可复用结构。

第三，它和 multi-agent framework 论文形成应用背景。MetaGPT 强调 SOP 和角色分工，GPTSwarm 强调 agent graph 可优化；Claude Managed Agents 则把这些思路推到企业产品形态：agent 不仅协作，而且记忆、评价和改进都被产品化。

## 当前状态

这篇文章已完成资源级采集。后续如果精读，应优先对照 Anthropic 官方发布：

- Claude blog: https://claude.com/blog/new-in-claude-managed-agents
- Claude Managed Agents docs: https://platform.claude.com/

Forbes 文章适合作为背景材料，不适合作为理论依据。
