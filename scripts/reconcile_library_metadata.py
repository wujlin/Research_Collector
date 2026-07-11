#!/usr/bin/env python3
"""Import deliberate human metadata overrides from managed library Markdown files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline
from src.storage.markdown_store import MarkdownStore


STANDARD_STATUS_RANK = {"unread": 0, "reading": 1, "read": 2, "noted": 3}


def proposed_updates(paper, frontmatter: dict) -> dict:
    updates: dict = {}
    markdown_status = str(frontmatter.get("status", "") or "").strip()
    database_status = str(paper.status or "unread")
    if (
        markdown_status
        and markdown_status not in STANDARD_STATUS_RANK
        and markdown_status != database_status
    ):
        updates["status"] = markdown_status
    elif (
        markdown_status in STANDARD_STATUS_RANK
        and STANDARD_STATUS_RANK[markdown_status] > STANDARD_STATUS_RANK.get(database_status, -1)
    ):
        updates["status"] = markdown_status

    is_curated = bool(frontmatter.get("digest") or frontmatter.get("coverage_note"))
    if is_curated:
        field_map = {
            "year": "year",
            "journal": "journal",
            "arxiv": "arxiv_id",
            "source": "source",
        }
        for markdown_field, database_field in field_map.items():
            value = frontmatter.get(markdown_field)
            if value in (None, ""):
                continue
            if database_field == "year":
                value = int(value)
            if value != getattr(paper, database_field):
                updates[database_field] = value
    return updates


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write proposed updates and refresh artifacts.")
    args = parser.parse_args()

    pipeline = CollectionPipeline()
    changes = []
    for paper in pipeline.database.list_papers():
        if not paper.markdown_path:
            continue
        path = ROOT / "library" / paper.markdown_path
        frontmatter, _ = MarkdownStore._read_existing_paper(path)
        updates = proposed_updates(paper, frontmatter)
        if not updates:
            continue
        changes.append({"id": paper.id, "title": paper.title, "updates": updates})
        if args.apply:
            pipeline.database.update_paper_metadata(paper.id, **updates)

    if args.apply:
        pipeline.sync_library_markdown()
        pipeline.export_all(generate_periodic_digest=False)

    print({"applied": args.apply, "change_count": len(changes), "changes": changes})


if __name__ == "__main__":
    main()
