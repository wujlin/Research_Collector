---
title: "Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility"
authors: ["Julius Degünther", "Jann van der Meer", "Udo Seifert"]
year: 2024
journal: "Physical Review Research"
doi: "10.1103/PhysRevResearch.6.023175"
arxiv: "2309.07665"
url: "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.023175"
pdf_url: "https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.6.023175"
topics: ["statistical_physics", "statistical_physics/non_equilibrium_dynamics/nonequilibrium", "statistical_physics/non_equilibrium_dynamics/fluctuation_theorems", "bridges/thermodynamic_inference"]
tier: 1
citations: 0
relevance_score: 0
collected: "2026-04-11"
status: "unread"
source: "manual"
---

## Abstract

(待填充)

## Key Contributions

- Extends fluctuating entropy production from fully observed stochastic systems to coarse-grained observation levels.
- Introduces a trajectory-based framework built from snippets and Markovian events.
- Makes irreversibility localizable in time and space instead of only estimating a global entropy-production total.
- Demonstrates hidden-driving detection as an inference application.

## Connections

- [[statistical_physics]]
- [[nonequilibrium]]
- [[fluctuation_theorems]]
- [[thermodynamic_inference]]

## Notes

### Reading Frame

这篇的价值不在于再给一个总熵产生的 bound，而在于回答更现实的问题：当系统只能被粗粒化地观测时，entropy production 还能不能被重新定义，并重新定位到具体的时间、空间或事件上。

### Problem

核心问题是：在存在隐藏自由度、只看到 coarse-grained trajectories 的情况下，如何定义并推断 fluctuating entropy production，以及如何识别 irreversibility 的局域来源。

### Why Care

这篇值得读，因为真实实验和复杂系统里，完全可观测通常只是理想情况。更常见的情况是你只能看到局部片段、事件类型或模糊后的轨迹。此时如果只能得到一个全局总量，信息太少；真正有用的是知道不可逆性到底“发生在哪里”。

### Objects

- coarse-grained trajectories
- snippets
- Markovian events
- fluctuating entropy production
- hidden driving

### Evolution Structure

优先看清他们如何把完整轨迹切成 `snippets`，以及 `Markovian events` 如何成为 coarse-grained thermodynamic inference 的基本单元。

### Quantities

核心量包括：

- fluctuating entropy production
- localization of irreversibility
- hidden-driving signatures

### Method Role

方法层重点不是机器学习，而是重新搭建一个在 coarse-grained setting 下仍能落到 trajectory/event level 的热力学框架。

### Evidence

证据主要看三件事：

- 定义是否理论闭合
- 是否能在例子中定位 irreversibility
- hidden driving detection 是否是框架自然给出的，而不是额外拼接的应用

### Reproduction Path

更合适的 toy 路线是：

1. 从一个含隐藏驱动的简单 Markov 跳变或 Langevin 模型开始。
2. 只保留 coarse-grained 可见事件。
3. 比较全可见与粗粒化后对 irreversibility 的归因差别。

### Detailed Reading Notes

当天的精读展开统一放在：

- [study-guide.md](/Users/jinlin/Desktop/Project/Research_Collector/digests/2026-04-11/study-guide.md)

这份 `library` 条目只保留归档型信息与最小阅读框架，避免和当天 digest 出现两套并行笔记。
