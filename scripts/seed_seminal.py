#!/usr/bin/env python3
"""导入 seminal papers，并初始化知识地图与 YouTube 索引。"""

from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.exporters.knowledge_graph import KnowledgeGraphExporter
from src.exporters.web_snapshot import WebSnapshotExporter
from src.pipeline import CollectionPipeline
from src.utils.helpers import ensure_data_dirs, load_config


def seed_seminal_papers() -> None:
    ensure_data_dirs()
    pipeline = CollectionPipeline()
    pipeline.database.init_topics_from_yaml("config/topics.yaml")
    pipeline.markdown_store.ensure_directory_structure("config/topics.yaml")

    with open("config/seminal_papers.yaml", "r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)

    for paper_data in payload.get("papers", []):
        paper = pipeline.database.add_paper(paper_data)
        markdown_path = pipeline.markdown_store.save_paper(paper)
        pipeline.database.update_paper_markdown_path(paper.id, markdown_path)

    write_knowledge_map()
    write_youtube_bootstrap()
    KnowledgeGraphExporter().export(pipeline.database)
    WebSnapshotExporter().export_all(pipeline.database)


def write_knowledge_map() -> None:
    output_dir = Path("knowledge_map")
    output_dir.mkdir(parents=True, exist_ok=True)

    overview = """# Knowledge Map Overview

Research Collector 不把知识结构写成四个彼此独立的方向，而是写成一条连续的研究链。

## A Better Logic

### 1. 数学骨架

- 随机分析：Brownian motion, Ito calculus, SDE, path-space dynamics

### 2. 翻译层

- Fokker-Planck / Master equation：把路径级随机动力学翻译成密度演化

### 3. 物理语义层

- 统计物理：entropy, free energy, fluctuation theorems, NESS, irreversibility

### 4. AI for Physics 层

- 这一层继续展开成两条主线：
  - generative dynamics：score, diffusion, reverse-time SDE, flow matching
  - physics-informed modeling：variational / free-energy language, scientific inverse problems, scientific ML

### 5. 应用场景层

- 城市复杂系统：scaling, transport networks, migration dynamics, spatial diffusion

这里最重要的观点是：**Fokker-Planck 不是“又一个方向”，也不只是一个公共名词，而是一层翻译机制。**

它把“随机路径”翻译成“分布演化”，再进一步连接到：

- 统计物理对不可逆性、熵产生和自由能的解释
- AI for Physics 中的 diffusion / score / flow 模型对逆向生成和密度传输的构造
- 城市系统中迁移、扩散和网络流的连续极限表述

## Frontier Focus

当前最值得持续追踪的桥接主题是：

1. 非平衡统计物理 + 生成模型
2. 随机热力学 + 轨迹学习
3. variational free energy / ELBO 与物理先验生成模型
4. score-based diffusion / flow 在 scientific machine learning 中的物理化

```mermaid
graph LR
  SA["数学骨架\n随机分析"]
  FP["翻译层\nFokker-Planck / Master Eq."]
  SP["物理语义\n统计物理"]
  SD["AI for Physics\nGenerative Dynamics + Physics-Informed Modeling"]
  UC["应用场景\n城市复杂系统"]
  Frontier["Frontier\n非平衡统计物理 + 生成模型"]

  SA --> FP
  FP --> SP
  FP --> SD
  SP --> SD
  SP --> UC
  SD --> UC

  FP --- Frontier
  SP --- Frontier
  SD --- Frontier
```
"""

    reading_paths = """# Reading Paths

## Path A: 数学骨架 -> 翻译层 -> 生成模型

1. Brownian motion / Ito calculus
2. Fokker-Planck / master equation
3. stochastic thermodynamics / entropy production
4. score-based generative modeling through SDEs
5. non-equilibrium statistical mechanics + generative modelling

## Path B: 物理语义 -> 城市场景

1. maximum entropy / ensembles
2. nonequilibrium steady state
3. fluctuation theorems
4. urban scaling / transport networks
5. urban phase transitions / diffusion on spatial systems

## Path C: Frontier AI for Physics

这条路径不应被理解为“单独一个方向”，而应理解为对前两条路径的再耦合：

1. variational inference for physics-informed deep generative modelling
2. free energy and nonequilibrium bridges
3. diffusion / flow models for scientific systems
4. trajectory learning, entropy production, irreversibility
"""

    theory_landscape = """# Theory Landscape

## Three Different Meanings of Free Energy

- thermodynamic free energy: Helmholtz / Gibbs / partition function
- variational free energy: ELBO / Bayesian inference / amortized inference
- free energy principle: self-organization / generative models / non-equilibrium systems

这三条线在文献中经常被混用，因此 Research Collector 在标签上必须显式区分。

## Why Fokker-Planck Matters

Fokker-Planck 在这个项目里更适合被写成“翻译层”，而不是“四个方向的公共枢纽”。

它做的事情是：

1. 把随机分析中的路径动力学翻译成密度动力学
2. 把统计物理中的耗散、熵产生、稳态问题写成可计算的演化方程
3. 把 AI for Physics 中的 generative dynamics 和 physics-informed modeling 放进同一套动力学语言
4. 把城市系统中的迁移、扩散、空间相互作用写成连续极限模型

所以它的重要性不在于“它同时出现在四个地方”，而在于它承担了**跨层翻译**：

- `路径 -> 密度`
- `动力学 -> 热力学解释`
- `前向扩散 -> 逆向生成`
- `抽象模型 -> 城市场景`

## Current Frontier

最前沿的问题不再是“AI 能不能替代 physics”，而是：

- 生成模型能否学习不可逆轨迹与熵产生
- 变分自由能能否成为 physics-informed generative modelling 的统一训练语言
- score / diffusion / reverse-time dynamics 能否直接解释非平衡系统
"""

    (output_dir / "overview.md").write_text(overview, encoding="utf-8")
    (output_dir / "reading_paths.md").write_text(reading_paths, encoding="utf-8")
    (output_dir / "theory_landscape.md").write_text(theory_landscape, encoding="utf-8")


def write_youtube_bootstrap() -> None:
    config = load_config("youtube_channels.yaml")
    output_dir = Path("youtube")
    playlists_dir = output_dir / "playlists"
    output_dir.mkdir(parents=True, exist_ok=True)
    playlists_dir.mkdir(parents=True, exist_ok=True)

    index_lines = ["# YouTube Learning Resources", ""]
    for group_key, channels in config.get("channels", {}).items():
        file_path = playlists_dir / f"{group_key}.md"
        lines = [f"# {group_key}", ""]
        index_lines.append(f"- [{group_key}](playlists/{group_key}.md)")
        for channel in channels:
            lines.append(f"## {channel['name']}")
            if channel.get("channel_id"):
                lines.append(f"- Channel ID: `{channel['channel_id']}`")
            if channel.get("search_terms"):
                lines.append(f"- Search terms: {', '.join(channel['search_terms'])}")
            if channel.get("relevant_playlists"):
                lines.append(f"- Relevant playlists: {', '.join(channel['relevant_playlists'])}")
            if channel.get("topics"):
                lines.append(f"- Topics: {', '.join(channel['topics'])}")
            lines.append("")
        file_path.write_text("\n".join(lines), encoding="utf-8")

    (output_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    seed_seminal_papers()
