#!/usr/bin/env python3
"""Generate the canonical daily collection review that merges papers and YouTube resources."""

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
from src.processors.youtube_filter import YouTubeFilter
from src.utils.helpers import canonical_digest_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate the merged daily collection review")
    parser.add_argument("--date", default="", help="Digest date in YYYY-MM-DD; defaults to today")
    parser.add_argument(
        "--collected-after",
        default="",
        help="Only consider papers collected after YYYY-MM-DD; defaults to digest date",
    )
    parser.add_argument("--apply-delete", action="store_true", help="Delete archive papers and YouTube resources")
    return parser


def remove_empty_directories(root: Path) -> None:
    for directory in sorted(root.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()


def main() -> None:
    args = build_parser().parse_args()
    digest_date = args.date or datetime.now().date().isoformat()
    collected_after = args.collected_after or digest_date
    cutoff = datetime.fromisoformat(f"{collected_after}T00:00:00")

    pipeline = CollectionPipeline()
    ranker = ImportanceRanker()
    youtube_filter = YouTubeFilter()

    paper_batch = [
        paper for paper in pipeline.database.list_papers(limit=2000)
        if paper.collected_at and paper.collected_at >= cutoff
    ]

    paper_buckets: dict[str, list[tuple[float, object]]] = {"keep": [], "review": [], "archive": []}
    for paper in paper_batch:
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
        paper_buckets[bucket].append((score, paper))

    for items in paper_buckets.values():
        items.sort(key=lambda item: item[0], reverse=True)

    youtube_buckets: dict[str, list[tuple[float, object, dict[str, object]]]] = {"keep": [], "review": [], "archive": []}
    youtube_archive_ids: list[int] = []
    for resource in pipeline.database.list_youtube_resources():
        payload = {
            "title": resource.title,
            "description": resource.description,
            "channel_name": resource.channel_name,
            "topic_key": resource.topic_key,
            "view_count": resource.view_count,
            "published_at": resource.published_at,
            "resource_type": resource.resource_type,
        }
        verdict = youtube_filter.evaluate(payload)
        score, bucket = ranker.score_youtube(payload)
        if not verdict["keep"]:
            bucket = "archive"
        youtube_buckets[bucket].append((score, resource, verdict))
        if bucket == "archive":
            youtube_archive_ids.append(resource.id)

    for items in youtube_buckets.values():
        items.sort(key=lambda item: item[0], reverse=True)

    output_path = canonical_digest_path(ROOT / "digests", digest_date, "collection_review")
    lines = [
        "---",
        'title: "Collection Review"',
        'digest_type: "collection_review"',
        f'date: "{digest_date}"',
        "---",
        "",
        f"# Collection Review {digest_date}",
        "",
        f"- Papers in batch: `{len(paper_batch)}` since `{collected_after}`",
        f"- Paper keep/review/archive: `{len(paper_buckets['keep'])} / {len(paper_buckets['review'])} / {len(paper_buckets['archive'])}`",
        f"- YouTube keep/review/archive: `{len(youtube_buckets['keep'])} / {len(youtube_buckets['review'])} / {len(youtube_buckets['archive'])}`",
        "",
        "## Papers",
        "",
    ]

    for bucket in ["keep", "review", "archive"]:
        lines.append(f"### {bucket.title()}")
        lines.append("")
        for score, paper in paper_buckets[bucket]:
            leaf_topics = [topic.key for topic in paper.topics if topic.key.count("/") == 2]
            lines.append(
                f"- `{paper.id}` | {score:.1f} | Tier {paper.tier} | {paper.journal or paper.venue or 'unknown venue'} | "
                f"{paper.title} | {', '.join(leaf_topics) if leaf_topics else 'no_leaf_topic'}"
            )
        lines.append("")

    lines.extend(["## YouTube", ""])
    for bucket in ["keep", "review", "archive"]:
        lines.append(f"### {bucket.title()}")
        lines.append("")
        for score, resource, verdict in youtube_buckets[bucket]:
            lines.append(
                f"- `{resource.id}` | {score:.1f} | {resource.channel_name} | {resource.title} | "
                f"{resource.topic_key or 'no_topic'} | {verdict['reason']} | {resource.url}"
            )
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    removed_papers = 0
    removed_youtube = 0
    if args.apply_delete:
        archive_papers = [paper for _, paper in paper_buckets["archive"]]
        markdown_paths = [paper.markdown_path for paper in archive_papers if paper.markdown_path]
        removed_papers = pipeline.database.delete_papers_by_ids([paper.id for paper in archive_papers])
        for relative_path in markdown_paths:
            file_path = ROOT / "library" / relative_path
            if file_path.exists():
                file_path.unlink()
        remove_empty_directories(ROOT / "library")
        removed_youtube = pipeline.database.delete_youtube_resources_by_ids(youtube_archive_ids)
        pipeline._refresh_library_indices()
        pipeline.export_all()

    print(
        {
            "report_path": str(output_path.relative_to(ROOT)),
            "paper_keep": len(paper_buckets["keep"]),
            "paper_review": len(paper_buckets["review"]),
            "paper_archive": len(paper_buckets["archive"]),
            "youtube_keep": len(youtube_buckets["keep"]),
            "youtube_review": len(youtube_buckets["review"]),
            "youtube_archive": len(youtube_buckets["archive"]),
            "removed_papers": removed_papers,
            "removed_youtube": removed_youtube,
        }
    )


if __name__ == "__main__":
    main()
