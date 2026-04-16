---
title: "FP4 Explore, BF16 Train: Diffusion Reinforcement Learning via Efficient Rollout Scaling"
authors: ["Yitong Li", "Junsong Chen", "Shuchen Xue", "Pengcuo Zeren", "Siyuan Fu", "Dinghao Yang", "Yangyang Tang", "Junjie Bai", "Ping Luo", "Song Han", "Enze Xie"]
year: 2026
journal: "arXiv (Cornell University)"
doi: ""
arxiv: ""
url: "https://openalex.org/W7153671532"
pdf_url: "https://arxiv.org/pdf/2604.06916"
topics: ["statistical_physics", "statistical_physics/collective_structure/phase_transitions", "statistical_physics/collective_structure"]
tier: 0
citations: 0
relevance_score: 51.0
collected: "2026-04-16"
status: "unread"
source: "openalex"
---

## Abstract

Reinforcement-Learning-based post-training has recently emerged as a promising paradigm for aligning text-to-image diffusion models with human preferences. In recent studies, increasing the rollout group size yields pronounced performance improvements, indicating substantial room for further alignment gains. However, scaling rollouts on large-scale foundational diffusion models (e.g., FLUX.1-12B) imposes a heavy computational burden. To alleviate this bottleneck, we explore the integration of FP4 quantization into Diffusion RL rollouts. Yet, we identify that naive quantized pipelines inherently introduce risks of performance degradation. To overcome this dilemma between efficiency and training integrity, we propose Sol-RL (Speed-of-light RL), a novel FP4-empowered Two-stage Reinforcement Learning framework. First, we utilize high-throughput NVFP4 rollouts to generate a massive candidate pool and extract a highly contrastive subset. Second, we regenerate these selected samples in BF16 precision and optimize the policy exclusively on them. By decoupling candidate exploration from policy optimization, Sol-RL integrates the algorithmic mechanisms of rollout scaling with the system-leve

## Key Contributions

(待补充)

## Connections

- [[statistical_physics]]
- [[phase_transitions]]
- [[collective_structure]]

## Notes

