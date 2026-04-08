#!/usr/bin/env python3
"""批量迁移 topic key 前缀，并重建导出产物。"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.exporters.web_snapshot import WebSnapshotExporter
from src.pipeline import CollectionPipeline
from src.storage.database import Database


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Migrate topic prefix in DB and generated artifacts")
    parser.add_argument("--old-prefix", required=True)
    parser.add_argument("--new-prefix", required=True)
    parser.add_argument("--clean-generated", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    db = Database("data/papers.db")
    renamed = db.rename_topic_key_prefix(args.old_prefix, args.new_prefix)

    pipeline = CollectionPipeline()
    pipeline.database.init_topics_from_yaml("config/topics.yaml")

    if args.clean_generated:
        old_library_dir = ROOT / "library" / args.old_prefix
        if old_library_dir.exists():
            shutil.rmtree(old_library_dir)
        old_playlist = ROOT / "youtube" / "playlists" / f"{args.old_prefix}.md"
        if old_playlist.exists():
            old_playlist.unlink()

    pipeline.markdown_store.ensure_directory_structure("config/topics.yaml")
    valid_markdown_paths: set[str] = set()
    for paper in pipeline.database.list_papers():
        markdown_path = pipeline.markdown_store.save_paper(paper)
        pipeline.database.update_paper_markdown_path(paper.id, markdown_path)
        valid_markdown_paths.add(markdown_path)

    for markdown_file in (ROOT / "library").rglob("*.md"):
        relative_path = markdown_file.relative_to(ROOT / "library").as_posix()
        if markdown_file.name in {"index.md", "_index.md"}:
            continue
        if relative_path not in valid_markdown_paths:
            markdown_file.unlink()

    from scripts.seed_seminal import write_knowledge_map, write_youtube_bootstrap

    write_knowledge_map()
    write_youtube_bootstrap()
    pipeline._refresh_library_indices()
    pipeline.export_all()
    WebSnapshotExporter().export_all(pipeline.database)
    print(
        {
            "renamed_topics": renamed,
            "old_prefix": args.old_prefix,
            "new_prefix": args.new_prefix,
        }
    )


if __name__ == "__main__":
    main()
