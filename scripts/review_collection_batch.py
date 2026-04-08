#!/usr/bin/env python3
"""审查某次采集批次，并可选择删除 archive 桶论文。"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline
from src.processors.importance_ranker import ImportanceRanker


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Review a collected paper batch")
    parser.add_argument("--collected-after", required=True, help="YYYY-MM-DD")
    parser.add_argument("--apply-delete", action="store_true", help="Delete archive-bucket papers in this batch")
    return parser


def remove_empty_directories(root: Path) -> None:
    for directory in sorted(root.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()


def main() -> None:
    args = build_parser().parse_args()
    cutoff = datetime.fromisoformat(f"{args.collected_after}T00:00:00")
    pipeline = CollectionPipeline()
    ranker = ImportanceRanker()

    batch = [
        paper for paper in pipeline.database.list_papers(limit=2000)
        if paper.collected_at and paper.collected_at >= cutoff
    ]

    buckets: dict[str, list[tuple[float, object]]] = {"keep": [], "review": [], "archive": []}
    for paper in batch:
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
        score, bucket = ranker.score_paper(payload)
        buckets[bucket].append((score, paper))

    for papers in buckets.values():
        papers.sort(key=lambda item: item[0], reverse=True)

    report_path = ROOT / "digests" / f"{args.collected_after}-batch-review.md"
    report_lines = [
        f"# Batch Review {args.collected_after}",
        "",
        f"- Keep: {len(buckets['keep'])}",
        f"- Review: {len(buckets['review'])}",
        f"- Archive: {len(buckets['archive'])}",
        "",
    ]

    for bucket in ["keep", "review", "archive"]:
        report_lines.append(f"## {bucket.title()}")
        report_lines.append("")
        for score, paper in buckets[bucket]:
            leaf_topics = [topic.key for topic in paper.topics if topic.key.count("/") == 2]
            report_lines.append(
                f"- `{paper.id}` | {score:.1f} | Tier {paper.tier} | {paper.journal or paper.venue or 'unknown venue'} | "
                f"{paper.title} | {', '.join(leaf_topics) if leaf_topics else 'no_leaf_topic'}"
            )
        report_lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    removed = 0
    if args.apply_delete:
        archive_papers = [paper for _, paper in buckets["archive"]]
        markdown_paths = [paper.markdown_path for paper in archive_papers if paper.markdown_path]
        removed = pipeline.database.delete_papers_by_ids([paper.id for paper in archive_papers])
        for relative_path in markdown_paths:
            file_path = ROOT / "library" / relative_path
            if file_path.exists():
                file_path.unlink()
        remove_empty_directories(ROOT / "library")
        pipeline._refresh_library_indices()
        pipeline.export_all()

    print(
        {
            "report_path": str(report_path.relative_to(ROOT)),
            "keep": len(buckets["keep"]),
            "review": len(buckets["review"]),
            "archive": len(buckets["archive"]),
            "removed": removed,
        }
    )


if __name__ == "__main__":
    main()
