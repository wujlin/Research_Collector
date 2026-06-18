---
title: "Software in the natural world: A computational approach to hierarchical emergence"
source_type: "paper"
source: "arXiv"
arxiv_id: "2402.09090"
version: "v2"
authors: "Fernando E. Rosas; Bernhard C. Geiger; Andrea I. Luppi; Anil K. Seth; Daniel Polani; Michael Gastpar; Pedro A. M. Mediano"
submitted: "2024-02-14"
last_revised: "2024-06-05"
collected: "2026-05-14"
url: "https://arxiv.org/abs/2402.09090"
pdf_local: "../../pdfs/2026-05-14/software-in-the-natural-world-a-computational-approach-to-hierarchical-emergence/software-in-the-natural-world-a-computational-approach-to-hierarchical-emergence.pdf"
status: "collected"
topics:
  - statistical_physics/collective_structure
  - collective_agent_systems
  - bridges/translation_layers
---

# Software in the natural world: A computational approach to hierarchical emergence

## 采集定位

这篇论文是 Quanta 文章 "The New Math of How Large-Scale Order Emerges" 背后的主要技术论文。Quanta 文章负责把问题讲清楚；这篇论文才是正式提出数学框架的地方。

论文的核心问题是：宏观层级什么时候不只是观察者随意选择的 coarse-graining，而是系统本身支持的有效计算层级？换句话说，如果一个复杂系统在宏观尺度上表现出稳定秩序，我们不能只说“这就是 emergence”，还需要判断这个宏观层级是否真的具备自洽的信息、干预和计算结构。

## 基本信息

- Title: "Software in the natural world: A computational approach to hierarchical emergence"
- Authors: Fernando E. Rosas, Bernhard C. Geiger, Andrea I. Luppi, Anil K. Seth, Daniel Polani, Michael Gastpar, Pedro A. M. Mediano
- Source: arXiv
- arXiv ID: `2402.09090`
- Version: `v2`
- Submitted: 2024-02-14
- Last revised: 2024-06-05
- Length: 33 pages, 13 figures
- Local PDF: `pdfs/2026-05-14/software-in-the-natural-world-a-computational-approach-to-hierarchical-emergence/`

## 为什么值得读

这篇论文对我们当前项目有三个直接价值。

第一，它把 emergence 从“宏观现象出现了”推进到“宏观层级是否具备 closure”。这能帮助我们避免只用直觉讨论集体行为、城市模式、agent population，而是追问宏观变量是否真的能预测、控制或模拟系统未来。

第二，它和 Baronchelli / Leibo 那条线可以接起来。Baronchelli 研究 convention、consensus、tipping point；Leibo 研究 multi-agent social learning 和 generative agent-based modeling。Rosas 这篇提供的是更抽象的层级语言：population-level pattern 何时成为一个自洽的有效层级。

第三，它对 synthetic city 的问题有启发。我们现在面对的是 census summaries、PUMA targets、joint distribution / copula 这些宏观约束。论文提醒我们：不是所有宏观统计量都天然是好表示。更关键的问题是，这些统计量是否构成对城市人群结构的有效状态变量。

## 后续精读时要盯的线索

读这篇论文时不要只看 emergence 的哲学叙述，应该重点追踪四个技术线索：

- `informational closure`：宏观变量是否足以预测宏观未来；
- `interventional closure`：宏观变量是否足以支持宏观层面的干预；
- `computational closure`：宏观层级是否能形成自洽的计算过程；
- `nested self-contained processes`：不同层级之间如何嵌套，而不是彼此孤立。

这里最需要和我们之前读过的 HJB / HJ-sampler、VI primer、Amy Zhang / Eysenbach 的 RL 表示学习放在一起比较：这些工作虽然领域不同，但都在问同一个底层问题，即怎样找到足以预测、控制或生成系统行为的有效变量。

