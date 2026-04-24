---
title: "Self-Adversarial One Step Generation via Condition Shifting"
authors: ["Deyuan Liu", "Peng Sun", "Yansen Han", "Zhenglin Cheng", "Chuyan Chen", "Tao Lin"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7154655379"
pdf_url: "https://arxiv.org/pdf/2604.12322"
topics: ["statistical_physics", "statistical_physics/collective_structure/phase_transitions", "statistical_physics/collective_structure"]
tier: 0
citations: 0
relevance_score: 51.0
collected: "2026-04-23"
status: "unread"
source: "openalex"
---

## Abstract

The push for efficient text to image synthesis has moved the field toward one step sampling, yet existing methods still face a three way tradeoff among fidelity, inference speed, and training efficiency. Approaches that rely on external discriminators can sharpen one step performance, but they often introduce training instability, high GPU memory overhead, and slow convergence, which complicates scaling and parameter efficient tuning. In contrast, regression based distillation and consistency objectives are easier to optimize, but they typically lose fine details when constrained to a single step. We present APEX, built on a key theoretical insight: adversarial correction signals can be extracted endogenously from a flow model through condition shifting. Using a transformation creates a shifted condition branch whose velocity field serves as an independent estimator of the model's current generation distribution, yielding a gradient that is provably GAN aligned, replacing the sample dependent discriminator terms that cause gradient vanishing. This discriminator free design is architecture preserving, making APEX a plug and play framework compatible with both full parameter and LoRA

## Key Contributions

(待补充)

## Connections

- [[statistical_physics]]
- [[phase_transitions]]
- [[collective_structure]]

## Notes

