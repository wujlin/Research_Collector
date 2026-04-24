---
title: "Gdiffuse: Diffusion-Based Speech Enhancement with Noise Model Guidance"
authors: ["Efrayim Yanir", "David Burshtein", "Sharon Gannot"]
year: 2026
journal: ""
doi: "10.1109/icassp55912.2026.11462263"
arxiv: ""
url: "https://openalex.org/W4416373993"
pdf_url: "https://arxiv.org/pdf/2510.04157"
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics/ddpm", "ai_for_physics/generative_dynamics/conditional_generation", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 49.08
collected: "2026-04-23"
status: "unread"
source: "openalex"
---

## Abstract

We introduce a novel speech enhancement (SE) approach based on a denoising diffusion probabilistic model (DDPM), termed guided diffusion for speech enhancement (GDiffuSE). In contrast to conventional methods that directly map noisy speech to clean speech, our method employs a lightweight helper model to estimate the noise distribution, which is then incorporated into the diffusion denoising process via a guidance mechanism. This design improves robustness by enabling seamless adaptation to unseen noise types and by lever-aging large-scale DDPMs originally trained for speech generation in the context of SE. We evaluate our approach on noisy signals obtained by adding noise samples from the BBC sound effects database to LibriSpeech utterances, showing consistent improvements over state-of-the-art baselines under mismatched noise conditions.

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[ddpm]]
- [[conditional_generation]]
- [[generative_dynamics]]

## Notes

