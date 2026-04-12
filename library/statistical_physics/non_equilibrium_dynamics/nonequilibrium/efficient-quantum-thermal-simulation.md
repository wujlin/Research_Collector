---
title: "Efficient quantum thermal simulation"
authors: ["Chi-Fang Chen", "Michael J. Kastoryano", "Fernando G. S. L. Brandão", "András Gilyén"]
year: 2025
journal: "Nature"
doi: "10.1038/s41586-025-09583-x"
arxiv: ""
url: "https://openalex.org/W4415196111"
pdf_url: "https://www.nature.com/articles/s41586-025-09583-x.pdf"
topics: ["statistical_physics", "statistical_physics/non_equilibrium_dynamics/nonequilibrium", "statistical_physics/non_equilibrium_dynamics"]
tier: 1
citations: 4
relevance_score: 71.17
collected: "2026-04-08"
status: "unread"
source: "openalex"
---

## Abstract

Quantum computers promise to tackle quantum simulation problems that are classically intractable<sup>1</sup>. Although a lot of quantum algorithms<sup>2-4</sup> have been developed for simulating quantum dynamics, a general-purpose method for simulating low-temperature quantum phenomena remains unknown. In classical settings, the analogous task of sampling from thermal distributions has been largely addressed by Markov Chain Monte Carlo (MCMC) methods<sup>5,6</sup>. Here we propose an efficient quantum algorithm for thermal simulation that-akin to MCMC methods-exhibits detailed balance, respects locality and serves as a toy model for thermalization in open quantum systems. The enduring impact of MCMC methods suggests that our new construction may play an equally important part in quantum computing and applications in the physical sciences and beyond.

## Key Contributions

- Proposes a quantum thermal simulation algorithm that plays the role of `MCMC` for low-temperature quantum systems.
- The construction is designed to satisfy `detailed balance` while respecting locality.
- The paper frames thermal simulation as both an algorithmic task and a toy model for thermalization in open quantum systems.

## Connections

- [[statistical_physics]]
- [[nonequilibrium]]
- [[non_equilibrium_dynamics]]

## Notes

### Reading Frame

这篇的核心不是一般意义上的“量子算法提速”，而是把 `classical MCMC -> detailed balance -> thermal sampling` 这条结构搬到量子热模拟里。

### Problem

目标是高效模拟低温量子热分布，也就是高效制备或采样 `Gibbs state / thermal distribution`。

### Objects

- `thermal distributions / Gibbs state`
- open quantum system 中的热化过程
- 与 classical `MCMC` 对应的量子转移结构

### Evolution Structure

优先确认四个结构是否同时成立：

- `detailed balance`
- `locality`
- `thermalization`
- 与 classical `Markov chain Monte Carlo` 的结构对应

### Quantities

这篇关心的核心量不是 entropy production，而是：

- target thermal distribution
- sampling efficiency
- thermalization complexity

### Method Role

方法层要回答两个问题：

1. 它怎样把 classical `MCMC` 的结构搬到 quantum setting。
2. 它的新意是在具体算法步骤，还是在热化结构的统一表述。

### Evidence

证据主要来自：

- 理论构造是否完整
- 复杂度或效率保证
- 与 classical `MCMC` 的结构对应是否清晰

### Reproduction Path

首次阅读不需要完整复现。更合适的做法是先写一个结构对照表：

- `classical MCMC`
- `detailed balance`
- `thermal distribution`
- quantum construction

把这四项之间的对应关系写清，再决定是否进入算法细节。
