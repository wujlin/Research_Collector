---
title: "Noise in the reverse process improves the approximation capabilities of diffusion models"
authors: ["Karthik Elamvazhuthi", "Samet Oymak", "Fabio Pasqualetti"]
year: 2023
journal: "arXiv"
doi: ""
arxiv: "2312.07851"
url: "http://arxiv.org/abs/2312.07851v2"
pdf_url: "https://arxiv.org/pdf/2312.07851v2"
topics: ["ai_for_physics/generative_dynamics/ddpm", "ai_for_physics/generative_dynamics", "ai_for_physics", "ai_for_physics/generative_dynamics/score_matching"]
tier: 0
citations: 0
relevance_score: 48.0
collected: "2026-04-16"
status: "unread"
source: "arxiv"
---

## Abstract

In Score based Generative Modeling (SGMs), the state-of-the-art in generative modeling, stochastic reverse processes are known to perform better than their deterministic counterparts. This paper delves into the heart of this phenomenon, comparing neural ordinary differential equations (ODEs) and neural stochastic differential equations (SDEs) as reverse processes. We use a control theoretic perspective by posing the approximation of the reverse process as a trajectory tracking problem. We analyze the ability of neural SDEs to approximate trajectories of the Fokker-Planck equation, revealing the advantages of stochasticity. First, neural SDEs exhibit a powerful regularizing effect, enabling $L^2$ norm trajectory approximation surpassing the Wasserstein metric approximation achieved by neural ODEs under similar conditions, even when the reference vector field or score function is not Lipschitz. Applying this result, we establish the class of distributions that can be sampled using score matching in SGMs, relaxing the Lipschitz requirement on the gradient of the data distribution in existing literature. Second, we show that this approximation property is preserved when network width i

## Key Contributions

(待补充)

## Connections

- [[ddpm]]
- [[generative_dynamics]]
- [[ai_for_physics]]
- [[score_matching]]

## Notes

