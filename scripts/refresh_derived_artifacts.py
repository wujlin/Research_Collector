#!/usr/bin/env python3
"""Refresh library indexes and web snapshots without creating a dated digest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-library-sync",
        action="store_true",
        help="Refresh indexes and web JSON without rewriting managed paper Markdown files.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    pipeline = CollectionPipeline()
    pipeline.database.init_topics_from_yaml("config/topics.yaml")
    pipeline.markdown_store.ensure_directory_structure("config/topics.yaml")

    if args.skip_library_sync:
        pipeline._refresh_library_indices()
    else:
        pipeline.sync_library_markdown()

    pipeline.export_all(generate_periodic_digest=False)
    stats = pipeline.database.get_stats()
    print(
        {
            "papers": stats["total_papers"],
            "library_synced": not args.skip_library_sync,
            "generated_dir": "web/public/generated",
        }
    )


if __name__ == "__main__":
    main()
