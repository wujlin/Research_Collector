---
title: "Truncated Rectified Flow Policy for Reinforcement Learning with One-Step Sampling"
authors: ["Xubin Zhou", "Yipeng Yang", "Zhan Li"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7154426978"
pdf_url: "https://arxiv.org/pdf/2604.09159"
topics: ["ai_for_physics/generative_dynamics/flow_matching", "ai_for_physics/generative_dynamics", "ai_for_physics", "statistical_physics/equilibrium_structures/equilibrium", "statistical_physics/equilibrium_structures", "statistical_physics"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

Maximum entropy reinforcement learning (MaxEnt RL) has become a standard framework for sequential decision making, yet its standard Gaussian policy parameterization is inherently unimodal, limiting its ability to model complex multimodal action distributions. This limitation has motivated increasing interest in generative policies based on diffusion and flow matching as more expressive alternatives. However, incorporating such policies into MaxEnt RL is challenging for two main reasons: the likelihood and entropy of continuous-time generative policies are generally intractable, and multi-step sampling introduces both long-horizon backpropagation instability and substantial inference latency. To address these challenges, we propose Truncated Rectified Flow Policy (TRFP), a framework built on a hybrid deterministic-stochastic architecture. This design makes entropy-regularized optimization tractable while supporting stable training and effective one-step sampling through gradient truncation and flow straightening. Empirical results on a toy multigoal environment and 10 MuJoCo benchmarks show that TRFP captures multimodal behavior effectively, outperforms strong baselines on most benc

## Key Contributions

(待补充)

## Connections

- [[flow_matching]]
- [[generative_dynamics]]
- [[ai_for_physics]]
- [[equilibrium]]
- [[equilibrium_structures]]
- [[statistical_physics]]

## Notes

