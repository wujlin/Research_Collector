#!/usr/bin/env python3
"""生成面向近期前沿跟进的阅读与复现包。"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline
from src.processors.importance_ranker import ImportanceRanker
from src.utils.helpers import canonical_digest_path, load_config, normalize_whitespace


@dataclass
class Candidate:
    paper_id: int
    title: str
    journal: str
    year: int | None
    url: str
    topics: list[str]
    importance_score: float
    importance_bucket: str
    venue_quality: str
    venue_reputation: str
    tier: int
    authors: list[str]
    author_signal: str
    author_signal_reason: str
    author_affiliations: list[str]
    fit_reason: str
    reproduction_reason: str


def load_venue_reputation_registry(config_name: str = "venue_reputation.yaml") -> tuple[dict[str, dict[str, str]], str]:
    config = load_config(config_name)
    venues = {normalize_venue_name(name): meta for name, meta in config.get("venues", {}).items()}
    return venues, str(config.get("default_status", "unreviewed"))


def normalize_venue_name(value: str) -> str:
    return normalize_whitespace(value).lower()


def venue_reputation_status(journal: str, venue: str, registry: dict[str, dict[str, str]], default_status: str) -> str:
    for candidate in (journal, venue):
        normalized = normalize_venue_name(candidate)
        if normalized and normalized in registry:
            return str(registry[normalized].get("status", default_status))
    return default_status


def load_author_affiliation_registry(config_name: str = "author_affiliation_reputation.yaml") -> dict[str, object]:
    config = load_config(config_name)
    return {
        "default_status": str(config.get("default_status", "unknown")),
        "strong_institutions": [normalize_venue_name(value) for value in config.get("strong_institutions", [])],
        "academic_keywords": [normalize_venue_name(value) for value in config.get("academic_keywords", [])],
        "off_topic_keywords": [normalize_venue_name(value) for value in config.get("off_topic_keywords", [])],
        "topic_keywords": {
            key: [normalize_venue_name(value) for value in values]
            for key, values in (config.get("topic_keywords", {}) or {}).items()
        },
    }


def infer_topic_families(topics: list[str]) -> list[str]:
    return sorted({topic.split("/", 1)[0] for topic in topics if topic})


def summarize_author_affiliation_signal(topics: list[str], affiliations: list[str], registry: dict[str, object]) -> tuple[str, str]:
    normalized_affiliations = [normalize_venue_name(value) for value in affiliations if normalize_venue_name(value)]
    if not normalized_affiliations:
        return str(registry.get("default_status", "unknown")), "No affiliation metadata available."

    strong_institutions = registry.get("strong_institutions", [])
    academic_keywords = registry.get("academic_keywords", [])
    off_topic_keywords = registry.get("off_topic_keywords", [])
    topic_keywords = registry.get("topic_keywords", {})
    families = infer_topic_families(topics)
    expected_keywords: list[str] = []
    for family in families:
        expected_keywords.extend(topic_keywords.get(family, []))

    strong_hit = any(any(token in affiliation for token in strong_institutions) for affiliation in normalized_affiliations)
    topical_hit = any(any(token in affiliation for token in expected_keywords) for affiliation in normalized_affiliations)
    academic_hit = any(any(token in affiliation for token in academic_keywords) for affiliation in normalized_affiliations)
    off_topic_hit = any(any(token in affiliation for token in off_topic_keywords) for affiliation in normalized_affiliations)

    if strong_hit and topical_hit:
        return "strong_match", "Strong institution and topic-aligned affiliation signal."
    if topical_hit:
        return "aligned_match", "Affiliation text looks topic-aligned even without a flagship institution match."
    if strong_hit:
        return "brand_only", "Strong institution signal is present, but the department or group fit is not explicit."
    if off_topic_hit:
        return "weak_match", "Affiliation metadata points to an explicitly off-topic department or organization."
    if academic_hit:
        return "unknown", "Academic affiliation metadata is present, but the department or group fit is not explicit."
    return "unknown", "Affiliation metadata is present, but the topical fit is still unclear."


def author_signal_rank(value: str) -> int:
    return {
        "strong_match": 4,
        "aligned_match": 3,
        "brand_only": 2,
        "unknown": 1,
        "weak_match": 0,
    }.get(value, 0)


def is_must_read_eligible(candidate: Candidate, ranker: ImportanceRanker) -> bool:
    allowed_reputation = set(ranker.paper_cfg.get("must_read_allowed_reputation", ["trusted"]))
    preprint_min_score = float(ranker.paper_cfg.get("must_read_preprint_min_score", 60))
    if candidate.author_signal == "weak_match":
        return False
    if candidate.venue_quality == "preprint":
        return candidate.importance_bucket == "keep" and candidate.importance_score >= preprint_min_score
    return candidate.venue_reputation in allowed_reputation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate frontier follow-up digest")
    parser.add_argument("--date", default="", help="Digest date in YYYY-MM-DD; defaults to today in local runtime.")
    parser.add_argument("--collected-after", default="", help="Only consider papers collected after YYYY-MM-DD")
    parser.add_argument("--must-read", type=int, default=3, help="Number of must-read papers")
    parser.add_argument("--repro", type=int, default=2, help="Number of reproduction candidates")
    parser.add_argument("--watchlist", type=int, default=5, help="Number of watchlist papers")
    return parser


def build_fit_reason(title: str, topics: list[str]) -> str:
    lower = title.lower()
    topic_text = " ".join(topics)
    if "markov" in lower or "ergod" in lower:
        return "直接连接 Markov chain、master equation 和 ergodicity。"
    if "inverse problem" in lower or "prior" in lower:
        return "直接连接 Bayesian inverse problem、generative prior 和 scientific ML。"
    if "mckean-vlasov" in lower or "measure-valued" in lower:
        return "把 mean-field stochastic dynamics 和学习模型直接接起来。"
    if "diffusion approximation" in lower:
        return "偏数学骨架，适合衔接 SDE 与 Fokker-Planck 的课程背景。"
    if "thermal" in lower:
        return "属于统计物理邻域里的高质量前沿样本。"
    if "physics-constrained" in lower or "physics-informed" in lower:
        return "能把 physics-informed 方法落到实际观测系统。"
    if "active" in lower or "boundary driven" in lower:
        return "适合延伸到非平衡统计物理和 active systems。"
    if "brownian motion" in lower or "pinn" in lower or "fokker_planck_master" in topic_text:
        return "和 Brownian motion、Fokker-Planck、PINN 这条主线衔接直接。"
    return "与当前随机分析、统计物理和 AI for Physics 主线相邻。"


def build_reproduction_reason(title: str, topics: list[str]) -> str:
    lower = title.lower()
    topic_text = " ".join(topics)
    if "markov" in lower or "random walk" in lower:
        return "最容易从 toy model 起步，适合先做低成本复现。"
    if "brownian motion" in lower or "pinn" in lower:
        return "可以落成 1D Brownian + Fokker-Planck residual 的最小实现。"
    if "inverse problem" in lower:
        return "适合做一个小型 PDE inverse problem 版本。"
    if "mckean-vlasov" in lower:
        return "适合做粒子系统到 mean-field 动力学的原型实验。"
    if "diffusion approximation" in lower or "fokker_planck_master" in topic_text:
        return "适合做 multiscale toy system 和 diffusion approximation 的验证。"
    return "可以作为第二梯队复现候选。"


def candidate_from_paper(
    paper,
    ranker: ImportanceRanker,
    registry: dict[str, dict[str, str]],
    default_status: str,
    author_registry: dict[str, object],
) -> Candidate:
    payload = {
        "title": paper.title,
        "abstract": paper.abstract,
        "topics": [topic.key for topic in paper.topics],
        "relevance_score": paper.relevance_score,
        "citation_count": paper.citation_count,
        "influential_citation_count": paper.influential_citation_count,
        "is_seminal": paper.is_seminal,
        "source": paper.source,
        "tier": paper.tier,
        "journal": paper.journal,
        "venue": paper.venue,
    }
    importance_score, importance_bucket = ranker.score_paper(payload)
    leaf_topics = [topic.key for topic in paper.topics if topic.key.count("/") == 2]
    author_names = [author.name for author in paper.authors]
    seen_affiliations: set[str] = set()
    author_affiliations: list[str] = []
    for author in paper.authors:
        affiliation = normalize_whitespace(author.affiliation or "")
        if not affiliation:
            continue
        lowered = affiliation.lower()
        if lowered in seen_affiliations:
            continue
        seen_affiliations.add(lowered)
        author_affiliations.append(affiliation)
    author_signal, author_signal_reason = summarize_author_affiliation_signal(
        leaf_topics,
        author_affiliations,
        author_registry,
    )
    return Candidate(
        paper_id=paper.id,
        title=paper.title,
        journal=paper.journal or paper.venue or "unknown venue",
        year=paper.year,
        url=paper.url or paper.pdf_url,
        topics=leaf_topics,
        importance_score=importance_score,
        importance_bucket=importance_bucket,
        venue_quality=ranker.venue_quality_label(payload),
        venue_reputation=venue_reputation_status(paper.journal or "", paper.venue or "", registry, default_status),
        tier=paper.tier or 0,
        authors=author_names,
        author_signal=author_signal,
        author_signal_reason=author_signal_reason,
        author_affiliations=author_affiliations[:3],
        fit_reason=build_fit_reason(paper.title, leaf_topics),
        reproduction_reason=build_reproduction_reason(paper.title, leaf_topics),
    )


def should_include_frontier(candidate: Candidate) -> bool:
    if candidate.importance_bucket not in {"keep", "review"}:
        return False
    if candidate.year and candidate.year < 2025:
        return False
    return True


def is_reproduction_friendly(candidate: Candidate) -> bool:
    lower = candidate.title.lower()
    keywords = [
        "markov",
        "random walk",
        "brownian",
        "pinn",
        "inverse problem",
        "mckean-vlasov",
        "diffusion approximation",
    ]
    return any(keyword in lower for keyword in keywords)


def sort_key(candidate: Candidate) -> tuple[float, int, int, str]:
    venue_rank = {
        "top_tier": 4,
        "high_quality": 3,
        "solid_domain": 2,
        "preprint": 1,
        "unranked": 0,
    }.get(candidate.venue_quality, 0)
    return (
        candidate.importance_score,
        venue_rank,
        author_signal_rank(candidate.author_signal),
        candidate.year or 0,
        candidate.title,
    )


def pick_first(
    candidates: list[Candidate],
    predicate,
    used_titles: set[str],
) -> Candidate | None:
    for candidate in candidates:
        if candidate.title in used_titles:
            continue
        if predicate(candidate):
            return candidate
    return None


def main() -> None:
    args = build_parser().parse_args()
    digest_date = args.date or datetime.now().date().isoformat()
    cutoff = datetime.fromisoformat(f"{args.collected_after}T00:00:00") if args.collected_after else None

    pipeline = CollectionPipeline()
    ranker = ImportanceRanker()
    venue_registry, default_venue_status = load_venue_reputation_registry()
    author_registry = load_author_affiliation_registry()
    candidates: list[Candidate] = []

    for paper in pipeline.database.list_papers(limit=2000):
        if cutoff and (not paper.collected_at or paper.collected_at < cutoff):
            continue
        candidate = candidate_from_paper(paper, ranker, venue_registry, default_venue_status, author_registry)
        if should_include_frontier(candidate):
            candidates.append(candidate)

    candidates.sort(key=sort_key, reverse=True)

    used_titles: set[str] = set()
    must_read: list[Candidate] = []

    must_read_pool = [candidate for candidate in candidates if is_must_read_eligible(candidate, ranker)]

    theory_pick = pick_first(
        must_read_pool,
        lambda candidate: any(
            keyword in candidate.title.lower()
            for keyword in ["ergod", "markov", "random walk", "thermalization", "diffusion approximation"]
        ),
        used_titles,
    )
    if theory_pick:
        must_read.append(theory_pick)
        used_titles.add(theory_pick.title)

    venue_pick = pick_first(
        must_read_pool,
        lambda candidate: candidate.venue_reputation == "trusted"
        and candidate.title != (theory_pick.title if theory_pick else ""),
        used_titles,
    )
    if venue_pick:
        must_read.append(venue_pick)
        used_titles.add(venue_pick.title)

    ai_pick = pick_first(
        must_read_pool,
        lambda candidate: (
            "inverse problem" in candidate.title.lower()
            or "prior" in candidate.title.lower()
            or "mckean-vlasov" in candidate.title.lower()
            or any(topic.startswith("ai_for_physics/") for topic in candidate.topics)
        ),
        used_titles,
    )
    if ai_pick:
        must_read.append(ai_pick)
        used_titles.add(ai_pick.title)

    for candidate in must_read_pool:
        if len(must_read) >= args.must_read:
            break
        if candidate.title in used_titles:
            continue
        must_read.append(candidate)
        used_titles.add(candidate.title)

    reproduction_candidates = [candidate for candidate in candidates if is_reproduction_friendly(candidate)]
    seen_titles = {candidate.title for candidate in must_read}
    reproduction = []
    for candidate in reproduction_candidates:
        if candidate.title in seen_titles:
            continue
        reproduction.append(candidate)
        if len(reproduction) >= args.repro:
            break

    watchlist = []
    seen_titles.update(candidate.title for candidate in reproduction)
    for candidate in candidates:
        if candidate.title in seen_titles:
            continue
        watchlist.append(candidate)
        if len(watchlist) >= args.watchlist:
            break

    output_path = canonical_digest_path(ROOT / "digests", digest_date, "paper_queue")
    lines = [
        "---",
        'title: "Paper Queue"',
        'digest_type: "paper_queue"',
        f'date: "{digest_date}"',
        "---",
        "",
        f"# Paper Queue {digest_date}",
        "",
        "这份文档是当天论文队列的唯一入口，用来决定：先读什么、继续跟踪什么、以及哪些值得进入复现。",
        "Must Read 默认只从已核验口碑的 venue 或高重要性 preprint 中选择；弱 venue 只进入复现候选或 watchlist。",
        "",
        "## Must Read",
        "",
    ]

    for index, candidate in enumerate(must_read, start=1):
        lines.extend(
            [
                f"### {index}. {candidate.title}",
                "",
                f"- Venue: `{candidate.journal}`",
                f"- Venue quality: `{candidate.venue_quality}`",
                f"- Venue reputation: `{candidate.venue_reputation}`",
                f"- Author signal: `{candidate.author_signal}`",
                f"- Authors: {', '.join(candidate.authors[:4]) if candidate.authors else 'Unknown'}",
                f"- Institutions: {', '.join(candidate.author_affiliations) if candidate.author_affiliations else 'No affiliation metadata'}",
                f"- Importance: `{candidate.importance_score:.1f}`",
                f"- Topics: {', '.join(candidate.topics) if candidate.topics else 'no_leaf_topic'}",
                f"- Why now: {candidate.fit_reason}",
                f"- Why team: {candidate.author_signal_reason}",
                f"- URL: {candidate.url or 'N/A'}",
                "",
            ]
        )

    lines.extend(
        [
            "## Reproduction Candidates",
            "",
        ]
    )

    for index, candidate in enumerate(reproduction, start=1):
        lines.extend(
            [
                f"### {index}. {candidate.title}",
                "",
                f"- Venue: `{candidate.journal}`",
                f"- Venue reputation: `{candidate.venue_reputation}`",
                f"- Author signal: `{candidate.author_signal}`",
                f"- Institutions: {', '.join(candidate.author_affiliations) if candidate.author_affiliations else 'No affiliation metadata'}",
                f"- Topics: {', '.join(candidate.topics) if candidate.topics else 'no_leaf_topic'}",
                f"- Why reproduce: {candidate.reproduction_reason}",
                f"- URL: {candidate.url or 'N/A'}",
                "",
            ]
        )

    lines.extend(
        [
            "## Watchlist",
            "",
        ]
    )

    for candidate in watchlist:
        lines.append(
            f"- `{candidate.title}` | {candidate.journal} | {candidate.venue_quality} | {candidate.venue_reputation} | {candidate.author_signal} | {candidate.importance_score:.1f}"
        )

    lines.extend(
        [
            "",
            "## Operating Rhythm",
            "",
            "每篇论文建议都按同一个模板处理：",
            "",
            "1. 写下它解决的核心问题。",
            "2. 写下它依赖的数学骨架或物理假设。",
            "3. 写下你能否把它压成一个 toy reproduction。",
            "",
            "如果一篇文章同时满足“理论骨架清楚 + toy model 可搭 + 和主线相连”，它就应该优先进入复现队列。",
            "",
        ]
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(
        {
            "output_path": str(output_path.relative_to(ROOT)),
            "must_read": [candidate.title for candidate in must_read],
            "reproduction": [candidate.title for candidate in reproduction],
            "watchlist_count": len(watchlist),
        }
    )


if __name__ == "__main__":
    main()
