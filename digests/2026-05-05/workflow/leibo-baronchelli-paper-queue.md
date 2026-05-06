---
title: "Leibo-Baronchelli Paper Queue"
date: "2026-05-05"
focus: "collective agent systems, social conventions, LLM populations, generative agent-based modeling"
---

# Leibo-Baronchelli Paper Queue

本次采集专门围绕 Joel Z. Leibo 与 Andrea Baronchelli。目标不是收作者全集，而是建立一条服务当前研究问题的主线：

`局部互动 -> 社会惯例/合作结构 -> population-level dynamics -> LLM agent societies -> synthetic city / route-corridor modes`

## Priority Order

### 1. The spontaneous emergence of conventions

- Author line: Baronchelli classic convention line.
- Role: 说明没有中央协调时，局部互动怎样形成全局惯例。
- Local PDF: `pdfs/2026-05-05/the-spontaneous-emergence-of-conventions/the-spontaneous-emergence-of-conventions.pdf`

### 2. Experimental evidence for tipping points in social convention

- Author line: Baronchelli tipping-point line.
- Role: 在既有惯例形成后，少数 committed minority 如何触发规范转换。
- Local PDF: `pdfs/2026-05-05/experimental-evidence-for-tipping-points-in-social-convention/experimental-evidence-for-tipping-points-in-social-convention.pdf`

### 3. Evidence for a conserved quantity in human mobility

- Author line: Baronchelli mobility line.
- Role: 把复杂系统视角落到城市流动，强调个体 familiar location set 的稳定容量。
- Local PDF: `pdfs/2026-05-05/evidence-for-a-conserved-quantity-in-human-mobility/evidence-for-a-conserved-quantity-in-human-mobility.pdf`

### 4. Multi-agent Reinforcement Learning in Sequential Social Dilemmas

- Author line: Leibo MARL/social dilemma line.
- Role: 把 social dilemma 从一次性矩阵博弈改写成时间展开的 Markov game。
- Local PDF: `pdfs/2026-05-05/multi-agent-reinforcement-learning-in-sequential-social-dilemmas/multi-agent-reinforcement-learning-in-sequential-social-dilemmas.pdf`

### 5. Scalable Evaluation of Multi-Agent Reinforcement Learning with Melting Pot

- Author line: Leibo cooperative AI benchmark line.
- Role: 从训练得分转向跨伙伴、跨场景的 social generalization evaluation。
- Local PDF: `pdfs/2026-05-05/scalable-evaluation-of-multi-agent-reinforcement-learning-with-melting-pot/scalable-evaluation-of-multi-agent-reinforcement-learning-with-melting-pot.pdf`

### 6. SocialJax

- Author line: Leibo/SocialJax follow-up.
- Role: 把 sequential social dilemma evaluation 做成高效 JAX 环境，适合后续计算实验参考。
- Local PDF: `pdfs/2026-05-05/socialjax-evaluation-suite-for-multi-agent-reinforcement-learning/socialjax-evaluation-suite-for-multi-agent-reinforcement-learning.pdf`

### 7. Generative agent-based modeling with Concordia

- Author line: Leibo generative ABM / LLM agent society line.
- Role: 从 RL agents 转向 LLM-based generative agents，由 Game Master 管理物理/社会/数字空间。
- Local PDF: `pdfs/2026-05-05/generative-agent-based-modeling-with-concordia/generative-agent-based-modeling-with-concordia.pdf`

### 8. Emergent social conventions and collective bias in LLM populations

- Author line: Baronchelli LLM populations line.
- Role: 直接测试 LLM agents 是否会通过局部互动形成社会惯例和集体偏差。
- Local PDF: `pdfs/2026-05-05/emergent-social-conventions-and-collective-bias-in-llm-populations/emergent-social-conventions-and-collective-bias-in-llm-populations.pdf`

### 9. How malicious AI swarms can threaten democracy

- Author line: Baronchelli AI swarm / policy-risk line.
- Role: 说明 LLM agent swarms 的 population-level dynamics 可能制造合成共识。
- Local PDF: `pdfs/2026-05-05/how-malicious-ai-swarms-can-threaten-democracy/how-malicious-ai-swarms-can-threaten-democracy.pdf`

### 10. Generative AI collective behavior needs an interactionist paradigm

- Author line: Leibo + Baronchelli intersection.
- Role: 给出总纲：不能只研究单体 LLM agent，要研究交互后出现的 population-level behavior。
- Local PDF: `pdfs/2026-05-05/generative-ai-collective-behavior-needs-an-interactionist-paradigm/generative-ai-collective-behavior-needs-an-interactionist-paradigm.pdf`

## Research Use

这组文献可以支持三个后续问题：

- `corridor as convention`: route generation 里的 corridor mode 可以被理解成 OD 条件下的可重复选择惯例，而不只是单条路径的几何最优。
- `synthetic population as interacting agents`: synthetic city 不只是静态联合分布恢复，也可以进入多智能体互动后的宏观结构分析。
- `uncertainty as population-level multiplicity`: 对同一组 census summaries / marginals，可能有多种 plausible population states；这些多模态结构可能由互动、规范和历史路径共同稳定。
