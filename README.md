# Research Collector: 前沿文献采集与知识架构系统

一个全自动的前沿文献采集、分类与知识管理系统，但它的知识结构不是四个彼此独立的栏目。更准确地说，这个项目跟踪的是一条连续的研究链：

- **随机分析**：提供路径级和微观随机动力学的数学骨架
- **统计物理**：提供熵、自由能、不可逆性等宏观语义
- **AI for Physics**：提供把这些动力学转成可训练模型的计算机制，内部再分为 `generative dynamics` 和 `physics-informed modeling`
- **城市复杂系统**：提供真实数据、真实结构和真实问题的应用场景

因此，这里更接近“主干 + 翻译层 + 桥接主题 + 应用场景”，而不是“四个相互独立的学科盒子”。

## 项目架构

```
Python 采集引擎 → SQLite 存储 → Markdown 数据层 → Next.js 展示层
```

- **采集引擎**：自动从 arXiv / Semantic Scholar / OpenAlex / YouTube 抓取前沿文献与学习资源
- **Markdown 数据层**：按主题分类法组织的文献库，兼容 Obsidian
- **Web 展示层**：Next.js 静态站点，提供知识图谱可视化、文献浏览与搜索

## 快速开始

### 1. 安装依赖

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
cp .env.example .env
# 编辑 .env，填入所需的 API key
```

建议至少配置 `OPENALEX_API_KEY` 和 `YOUTUBE_API_KEY`。`Semantic Scholar` 当前在默认工作流中已封存，不必填写。

### 3. 初始化 seminal papers

```bash
python scripts/seed_seminal.py
```

### 4. 手动采集

```bash
python scripts/collect.py                    # 采集全部源
python scripts/collect.py --source arxiv     # 仅 arXiv
python scripts/collect.py --source youtube   # 仅 YouTube
```

### 5. 启动定时采集

```bash
python scripts/setup_scheduler.py
```

### 6. 启动 Web 前端

```bash
cd web && npm install && npm run dev
```

## 知识地图

更准确的写法不是“Fokker-Planck 方程是四个方向的公共枢纽”，而是：

**Fokker-Planck / Master equation 是一层翻译机制。**

它把以下几层连起来：

- **随机分析层**：从 Brownian motion、Ito calculus、SDE 出发，描述路径如何随机演化
- **密度演化层**：用 Fokker-Planck / Kolmogorov / Master equation 把路径动力学翻译成分布演化
- **统计物理层**：把分布演化进一步解释为熵产生、耗散、稳态、自由能与不可逆性
- **AI for Physics 层**：把前向/逆向动力学转成 score-based diffusion、flow matching、reverse-time SDE 等可训练机制
- **AI for Physics 内部层次**：
  - `generative dynamics`：score matching、DDPM、reverse-time SDE、flow matching
  - `physics-informed modeling`：variational / free-energy language、physics-informed generative modelling、scientific ML
- **应用层**：在城市迁移、交通网络、空间扩散等系统里检验这些结构是否成立

所以本项目的核心逻辑是：

`随机路径 -> 密度演化 -> 热力学/信息论解释 -> 生成机制 -> 城市应用`

这也是为什么“非平衡统计物理 + 生成模型 / 自由能”会成为当前的重点前沿。

## 数据源

| 源 | 用途 | 认证 |
|---|---|---|
| arXiv API | 预印本实时采集 | 免费，无需 key |
| Semantic Scholar | 引用网络、影响力指标 | 免费，可选 API key |
| OpenAlex | 期刊筛选、开放获取 | 免费，建议配置 API key |
| YouTube Data API | 学习视频采集 | 需 Google API key |

## 目标期刊层级

- **Tier 1**：Nature, Science, Nature Physics, Nature Computational Science, Nature Cities, PRL, PNAS
- **Tier 2**：PRX, PRE, PRB, JSTAT, J. Stat. Phys., PR Research, SciPost Physics, NeurIPS, ICML, ICLR, New J. Phys.
- **Tier 3**：CEUS, EPB, J. R. Soc. Interface, EPJ Data Science, Chaos, Chaos, Solitons & Fractals, MLST, EPJ B, Atmospheric Measurement Techniques

默认不放进目标期刊层级、只做 article-level 审核的 venue：

- **Article-level only**：Scientific Reports, The European Physical Journal Special Topics

## 项目状态

- [x] 阶段1：基础骨架（配置、数据模型、存储层）
- [x] 阶段2：采集引擎（四个采集器 + 处理器）
- [x] 阶段3：自动化与导出（定时采集、摘要生成）
- [x] 阶段4：知识播种（seminal papers、知识地图）
- [x] 阶段5：Web 前端（知识图谱、文献浏览、搜索）
