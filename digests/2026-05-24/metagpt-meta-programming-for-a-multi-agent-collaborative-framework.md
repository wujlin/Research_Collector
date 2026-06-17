---
title: "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"
source_type: "paper"
venue: "arXiv"
authors: "Sirui Hong; Mingchen Zhuge; Jiaqi Chen; Xiawu Zheng; Yuheng Cheng; Ceyao Zhang; Jinlin Wang; Zili Wang; Steven Ka Shing Yau; Zijuan Lin; Liyang Zhou; Chenyu Ran; Lingfeng Xiao; Chenglin Wu; Jürgen Schmidhuber"
published: "2023-08-01"
latest_version: "v7"
collected: "2026-05-24"
arxiv_id: "2308.00352"
url: "https://arxiv.org/abs/2308.00352"
pdf_url: "https://arxiv.org/pdf/2308.00352"
local_pdf: "pdfs/2026-05-24/metagpt-meta-programming-for-a-multi-agent-collaborative-framework/metagpt-meta-programming-for-a-multi-agent-collaborative-framework.pdf"
status: "collected_pdf"
topics:
  - ai_agents/multi_agent_frameworks
  - software_engineering_agents
  - workflow_sop
  - agent_collaboration/role_assignment
---

# MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

## 采集定位

这篇论文属于 LLM multi-agent framework 线。它的核心不是提出一个新的基础模型，而是把人类软件工程 workflow 中的角色、文档和 SOP 编码进 multi-agent collaboration。

这篇适合和后面的 GPTSwarm 对比：

- MetaGPT 更强调固定流程、角色分工和 SOP；
- GPTSwarm 更强调把 agent system 写成可优化 graph；
- Agent-as-a-Judge 更强调 agent system 的评价和反馈信号。

## 核心问题

普通 multi-agent LLM 系统容易把多个 agent 简单串起来。这样做的问题是：每个 agent 的 hallucination 和逻辑偏差会沿着链条传播，最后形成 cascading hallucination。

MetaGPT 的思路是：不要只让 agent 自由聊天，而是把 agent 放进一个结构化软件生产流程里。每个角色有明确职责，每个阶段产生标准化中间产物，后续 agent 基于这些中间产物继续工作。

## 当前状态

- PDF 已下载到本地。
- 这篇目前是资源级采集，尚未精读。
- 如果后续精读，建议重点看 SOP 如何形式化、role assignment 如何影响 error propagation、以及它和 GPTSwarm 的 graph optimization 思路差异。
