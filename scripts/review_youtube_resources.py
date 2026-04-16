#!/usr/bin/env python3
"""审查 YouTube 资源，并可选择删除 archive 桶或过滤失败的条目。"""

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
    parser = argparse.ArgumentParser(description="Review YouTube resources")
    parser.add_argument("--apply-delete", action="store_true", help="Delete filtered/archive resources")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    today = datetime.now().date().isoformat()
    pipeline = CollectionPipeline()
    ranker = ImportanceRanker()
    youtube_filter = YouTubeFilter()

    resources = pipeline.database.list_youtube_resources()
    buckets: dict[str, list[tuple[float, object, dict[str, object]]]] = {"keep": [], "review": [], "archive": []}
    archive_ids: list[int] = []

    for resource in resources:
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
        buckets[bucket].append((score, resource, verdict))
        if bucket == "archive":
            archive_ids.append(resource.id)

    for resources_in_bucket in buckets.values():
        resources_in_bucket.sort(key=lambda item: item[0], reverse=True)

    report_path = canonical_digest_path(ROOT / "digests", today, "collection_review")
    lines = [
        f"# YouTube Review {today}",
        "",
        f"- Keep: {len(buckets['keep'])}",
        f"- Review: {len(buckets['review'])}",
        f"- Archive: {len(buckets['archive'])}",
        "",
    ]
    for bucket in ["keep", "review", "archive"]:
        lines.append(f"## {bucket.title()}")
        lines.append("")
        for score, resource, verdict in buckets[bucket]:
            lines.append(
                f"- `{resource.id}` | {score:.1f} | {resource.channel_name} | {resource.title} | "
                f"{resource.topic_key or 'no_topic'} | {verdict['reason']} | {resource.url}"
            )
        lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")

    removed = 0
    if args.apply_delete:
        removed = pipeline.database.delete_youtube_resources_by_ids(archive_ids)
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
