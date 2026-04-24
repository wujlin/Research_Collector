---
title: "ScoRe-Flow: Complete Distributional Control via Score-Based Reinforcement Learning for Flow Matching"
authors: ["Xiaotian Qiu", "Lukai Chen", "Jinhao Li", "Qi Sun", "Cheng Zhuo", "Guohao Dai"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7154539235"
pdf_url: "https://arxiv.org/pdf/2604.10962"
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics/score_matching", "ai_for_physics/generative_dynamics/flow_matching", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-23"
status: "unread"
source: "openalex"
---

## Abstract

Flow Matching (FM) policies have emerged as an efficient backbone for robotic control, offering fast and expressive action generation that underpins recent large-scale embodied AI systems. However, FM policies trained via imitation learning inherit the limitations of demonstration data; surpassing suboptimal behaviors requires reinforcement learning (RL) fine-tuning. Recent methods convert deterministic flows into stochastic differential equations (SDEs) with learnable noise injection, enabling exploration and tractable likelihoods, but such noise-only control can compromise training efficiency when demonstrations already provide strong priors. We observe that modulating the drift via the score function, i.e., the gradient of log-density, steers exploration toward high-probability regions, improving stability. The score admits a closed-form expression from the velocity field, requiring no auxiliary networks. Based on this, we propose ScoRe-Flow, a score-based RL fine-tuning method that combines drift modulation with learned variance prediction to achieve decoupled control over the mean and variance of stochastic transitions. Experiments demonstrate that ScoRe-Flow achieves 2.4x fas

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[score_matching]]
- [[flow_matching]]
- [[generative_dynamics]]

## Notes

