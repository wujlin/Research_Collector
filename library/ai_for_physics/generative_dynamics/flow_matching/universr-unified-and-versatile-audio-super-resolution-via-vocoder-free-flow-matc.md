---
title: "Universr: Unified and Versatile Audio Super-Resolution Via Vocoder-Free Flow Matching"
authors: ["Woojae Choi", "Sangmin Lee", "Hyungseob Lim", "Hong-Goo Kang"]
year: 2026
journal: ""
doi: "10.1109/icassp55912.2026.11460830"
arxiv: ""
url: "https://openalex.org/W4414809122"
pdf_url: "https://arxiv.org/pdf/2510.00771"
topics: ["ai_for_physics", "ai_for_physics/generative_dynamics/flow_matching", "ai_for_physics/generative_dynamics/conditional_generation", "ai_for_physics/generative_dynamics"]
tier: 0
citations: 0
relevance_score: 49.67
collected: "2026-04-23"
status: "unread"
source: "openalex"
---

## Abstract

In this paper, we present a vocoder-free framework for audio super-resolution that employs a flow matching generative model to capture the conditional distribution of complex-valued spectral coefficients. Unlike conventional two-stage diffusion-based approaches that predict a mel-spectrogram and then rely on a pre-trained neural vocoder to synthesize waveforms, our method directly reconstructs waveforms via the inverse Short-Time Fourier Transform (iSTFT), thereby eliminating the dependence on a separate vocoder. This design not only simplifies end-to-end optimization but also overcomes a critical bottleneck of two-stage pipelines, where the final audio quality is fundamentally constrained by vocoder performance. Experiments show that our model consistently produces high-fidelity 48 kHz audio across diverse upsampling factors, achieving state-of-the-art performance on both speech and general audio datasets.

## Key Contributions

(待补充)

## Connections

- [[ai_for_physics]]
- [[flow_matching]]
- [[conditional_generation]]
- [[generative_dynamics]]

## Notes

