# Daily Learning Evolution Workflow

This project is a daily frontier-learning system, not only a paper collector. The workflow should keep two loops running at the same time:

- a fixed daily loop that keeps the knowledge base fresh
- an evolving vision loop that absorbs new directions supplied by Zhihang

## Current Frontier Scope

The original collector follows a research chain:

```text
stochastic analysis -> statistical physics -> AI for Physics -> urban complex systems
```

Zhihang's branch extends the scope with five additional fields:

```text
complex systems dynamics
general swarm intelligence
swarm robotics
physics-informed spatial intelligence
physical AI
```

These are represented in:

- `config/topics.yaml`
- `config/query_profiles.yaml`
- `config/settings.yaml`

When Zhihang adds a new interesting direction, update the vision base in this order:

1. Add or refine topic keywords in `config/topics.yaml`.
2. Add source-specific search phrases in `config/query_profiles.yaml`.
3. If the direction should be actively prioritized, add ranking weights in `config/settings.yaml`.
4. Run a small source-specific collection test before trusting it in the daily loop.
5. Write the resulting learning signal into a digest, reading list, or knowledge card.

## Daily Fixed Loop

### 1. Morning Frontier Scan

Run lightweight collection first. The default target is breadth, not deep reading.

```bash
python scripts/collect.py --source arxiv
python scripts/collect.py --source openalex
```

If `SEMANTIC_SCHOLAR_API_KEY` is configured, also run:

```bash
python scripts/collect.py --source semantic_scholar
```

If `YOUTUBE_API_KEY` is configured and the day includes video learning:

```bash
python scripts/collect.py --source youtube
```

### 2. Triage And Noise Control

Review new items as candidates for one of four outcomes:

- **must read**: central to current research or a surprising bridge
- **watch**: relevant but not urgent
- **archive**: useful background
- **noise**: outside the scope or low-quality

Use cleanup and review scripts when the batch is noisy:

```bash
python scripts/review_collection_batch.py
python scripts/rescore_papers.py
python scripts/reclassify_papers.py
python scripts/cleanup_noise_papers.py
```

### 3. Daily Study Selection

Pick a small number of items. A normal day should not try to deeply read everything.

Recommended daily load:

- 1 deep paper or lecture
- 2-5 skimmed papers
- 1 concept or method card when a reusable idea appears

### 4. Deep Reading Or Lecture Processing

For papers:

- keep raw PDFs and parsing intermediates on HKUSTGZ under `/home/jinlin/projects/Personal Learning System`
- sync back only curated Markdown notes, figures, tables, manifests, or links

For videos:

- keep raw video/audio and rough slide extraction on HKUSTGZ
- sync back cleaned transcript, curated slides, contact sheet, and final note only

The stable storage rule is:

```text
heavy raw materials stay remote; light curated learning artifacts come back local.
```

For books and long-form methods material:

- keep the source PDF, full MinerU Markdown, images, layout PDFs, OCR intermediates, and extraction logs on HKUSTGZ
- sync back only transformed chapter notes, method manuals, skill references, indexes, and manifests
- do not treat the book as a flat summary task; identify high-leverage method chapters and expand them in detail
- convert durable principles into Codex skills when they change repeated research behavior

The book-to-skill loop is:

```text
remote extraction -> weighted chapter notes -> method manual -> reusable skill -> installed skill -> repo update
```

When the material is about writing, research design, literature review, methods, or analysis habits, the final artifact should include an operational checklist or skill reference, not only a reading note.

### 5. Knowledge Base Update

Convert the day's useful material into one or more durable artifacts:

- `digests/YYYY-MM-DD/*.md`
- `library/<topic>/*.md`
- `knowledge_cards/*.md`
- `knowledge_map/*`
- `youtube/notes/*.md`

Keep the writing problem-driven: what changed in the research view, what mechanism matters, and what question it opens next.

### 6. Evolution Note

End the day by recording one of three updates:

- **scope update**: a new topic should enter the vision base
- **query update**: an existing topic needs better search phrases
- **research question update**: a surprising mismatch or mechanism deserves follow-up

This is the mechanism by which Zhihang and Codex evolve together: each day should either add evidence, sharpen a concept, or improve the collector's future attention.

## Weekly Maintenance Loop

Once a week:

```bash
python scripts/collect.py
python scripts/generate_collection_review.py
python scripts/generate_frontier_followup.py
```

Then check:

- whether new topics are over-collecting noise
- whether high-value papers are being missed
- whether query phrases should be split by source
- whether a new skill or script is needed for repeated work
- whether a long-form book, lecture series, or methods text should be converted into a reusable skill

## Source Status

| Source | Current behavior | Operational note |
|---|---|---|
| arXiv | Collector tests passed; live endpoint may return `429` when smoke-tested repeatedly | No API key required; respect `settings.yaml` interval and retry policy |
| OpenAlex | Local smoke test passed with `OPENALEX_API_KEY` loaded from private `.env` | Call through `OpenAlexCollector` or `scripts/collect.py --source openalex`; results still need topic filtering |
| Semantic Scholar | Local smoke test passed with `SEMANTIC_SCHOLAR_API_KEY` loaded from private `.env` | Keep requests below 1 RPS; do not commit the key |
| YouTube | Local smoke test passed with `YOUTUBE_API_KEY` loaded from private `.env` | Call through `YouTubeCollector` or `scripts/collect.py --source youtube`; do not commit the key |

## Minimal Smoke Test

Use this after changing collector configuration:

```bash
python - <<'PY'
from src.collectors.arxiv_collector import ArxivCollector
from src.collectors.openalex import OpenAlexCollector
from src.collectors.youtube_collector import YouTubeCollector
from src.utils.helpers import load_config

print("arxiv", len(ArxivCollector().collect(
    query="swarm robotics",
    categories=load_config("sources.yaml").get("arxiv_categories", []),
    max_results=1,
)))
print("openalex", len(OpenAlexCollector().collect(
    query="swarm robotics",
    per_page=1,
    year_from=2024,
)))
print("youtube", len(YouTubeCollector().collect(
    query="swarm robotics",
    max_results=1,
)))
PY
```

Run Semantic Scholar separately when an API key is configured.
