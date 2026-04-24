---
title: "LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling"
authors: ["Yuxin Chen", "Chumeng Liang", "Hangke Sui", "Ruihan Guo", "Chaoran Cheng", "Jiaxuan You", "Ge Liu"]
year: 2026
journal: "ArXiv.org"
doi: ""
arxiv: ""
url: "https://openalex.org/W7154789785"
pdf_url: "https://arxiv.org/pdf/2604.11748"
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics/ddpm", "ai_for_physics/generative_dynamics/flow_matching", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 54.0
collected: "2026-04-23"
status: "unread"
source: "openalex"
---

## Abstract

Continuous diffusion has been the foundation of high-fidelity, controllable, and few-step generation of many data modalities such as images. However, in language modeling, prior continuous diffusion language models (DLMs) lag behind discrete counterparts due to the sparse data space and the underexplored design space. In this work, we close this gap with LangFlow, the first continuous DLM to rival discrete diffusion, by connecting embedding-space DLMs to Flow Matching via Bregman divergence, alongside three key innovations: (1) we derive a novel ODE-based NLL bound for principled evaluation of continuous flow-based language models; (2) we propose an information-uniform principle for setting the noise schedule, which motivates a learnable noise scheduler based on a Gumbel distribution; and (3) we revise prior training protocols by incorporating self-conditioning, as we find it improves both likelihood and sample quality of embedding-space DLMs with effects substantially different from discrete diffusion. Putting everything together, LangFlow rivals top discrete DLMs on both the perplexity (PPL) and the generative perplexity (Gen. PPL), reaching a PPL of 30.0 on LM1B and 24.6 on Open

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[ddpm]]
- [[flow_matching]]
- [[generative_dynamics]]

## Notes

