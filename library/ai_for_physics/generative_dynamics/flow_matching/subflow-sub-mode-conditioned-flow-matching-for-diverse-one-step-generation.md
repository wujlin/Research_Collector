---
title: "SubFlow: Sub-mode Conditioned Flow Matching for Diverse One-Step Generation"
authors: ["Yexiong Lin", "Jia Shi", "Shanshan Ye", "Wanyu Wang", "Yu Yao", "Tongliang Liu"]
year: 2026
journal: "arXiv (Cornell University)"
doi: ""
arxiv: ""
url: "https://openalex.org/W7154656003"
pdf_url: "https://arxiv.org/pdf/2604.12273"
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics/flow_matching", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 51.0
collected: "2026-04-23"
status: "unread"
source: "openalex"
---

## Abstract

Flow matching has emerged as a powerful generative framework, with recent few-step methods achieving remarkable inference acceleration. However, we identify a critical yet overlooked limitation: these models suffer from severe diversity degradation, concentrating samples on dominant modes while neglecting rare but valid variations of the target distribution. We trace this degradation to averaging distortion: when trained with MSE objectives, class-conditional flows learn a frequency-weighted mean over intra-class sub-modes, causing the model to over-represent high-density modes while systematically neglecting low-density ones. To address this, we propose SubFlow, Sub-mode Conditioned Flow Matching, which eliminates averaging distortion by decomposing each class into fine-grained sub-modes via semantic clustering and conditioning the flow on sub-mode indices. Each conditioned sub-distribution is approximately unimodal, so the learned flow accurately targets individual modes with no averaging distortion, restoring full mode coverage in a single inference step. Crucially, SubFlow is entirely plug-and-play: it integrates seamlessly into existing one-step models such as MeanFlow and Sho

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[flow_matching]]
- [[generative_dynamics]]

## Notes

