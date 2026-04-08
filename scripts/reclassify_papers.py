#!/usr/bin/env python3
"""按当前 taxonomy 和 classifier 重新分类现有论文。"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline
from src.processors.classifier import TopicClassifier


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reclassify stored papers with current taxonomy")
    parser.add_argument("--collected-after", default="", help="Only reclassify papers collected after YYYY-MM-DD")
    parser.add_argument("--include-seminal", action="store_true", help="Also reclassify curated seminal papers")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    cutoff = datetime.fromisoformat(f"{args.collected_after}T00:00:00") if args.collected_after else None

    pipeline = CollectionPipeline()
    pipeline.database.init_topics_from_yaml("config/topics.yaml")
    classifier = TopicClassifier()

    updated = 0
    for paper in pipeline.database.list_papers(limit=1000):
        if paper.is_seminal and not args.include_seminal:
            continue
        if cutoff and (not paper.collected_at or paper.collected_at < cutoff):
            continue

        record = classifier.classify_record({"title": paper.title, "abstract": paper.abstract})
        pipeline.database.replace_paper_topics(paper.id, record.get("topic_keys", []))
        refreshed_paper = pipeline.database.get_paper(paper.id)
        if refreshed_paper is None:
            continue
        markdown_path = pipeline.markdown_store.save_paper(refreshed_paper)
        pipeline.database.update_paper_markdown_path(paper.id, markdown_path)
        updated += 1

    pipeline._refresh_library_indices()
    pipeline.export_all()
    print({"reclassified_papers": updated, "collected_after": args.collected_after or None})


if __name__ == "__main__":
    main()
