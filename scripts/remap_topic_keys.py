#!/usr/bin/env python3
"""按映射表批量重命名 topic key，并重建导出产物。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline
from src.utils.helpers import flatten_topics, load_config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Remap topic keys in DB and generated artifacts")
    parser.add_argument(
        "--mapping-file",
        default="config/topic_key_remap_2026-04.yaml",
        help="YAML file containing a top-level `mapping` dictionary",
    )
    return parser


def remove_stale_library_files(library_dir: Path, valid_markdown_paths: set[str]) -> None:
    for markdown_file in library_dir.rglob("*.md"):
        relative_path = markdown_file.relative_to(library_dir).as_posix()
        if markdown_file.name in {"index.md", "_index.md"}:
            continue
        if relative_path not in valid_markdown_paths:
            markdown_file.unlink()

    for directory in sorted(library_dir.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()


def main() -> None:
    args = build_parser().parse_args()
    with open(args.mapping_file, "r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}
    mapping: dict[str, str] = payload.get("mapping", {})
    if not mapping:
        raise SystemExit("No topic mapping found.")

    pipeline = CollectionPipeline()
    renamed = pipeline.database.remap_topic_keys(mapping)
    pipeline.database.init_topics_from_yaml("config/topics.yaml")
    attached = pipeline.database.normalize_paper_topics()

    valid_keys = {entry["key"] for entry in flatten_topics(load_config("topics.yaml"))}
    removed = pipeline.database.prune_topics(valid_keys)

    pipeline.markdown_store.ensure_directory_structure("config/topics.yaml")
    valid_markdown_paths: set[str] = set()
    for paper in pipeline.database.list_papers():
        markdown_path = pipeline.markdown_store.save_paper(paper)
        pipeline.database.update_paper_markdown_path(paper.id, markdown_path)
        valid_markdown_paths.add(markdown_path)

    remove_stale_library_files(ROOT / "library", valid_markdown_paths)

    from scripts.seed_seminal import write_knowledge_map, write_youtube_bootstrap

    write_knowledge_map()
    write_youtube_bootstrap()
    pipeline._refresh_library_indices()
    pipeline.export_all()

    print(
        {
            "renamed_topics": renamed,
            "ancestor_topics_added": attached,
            "stale_topics_removed": removed,
            "mapping_file": args.mapping_file,
        }
    )


if __name__ == "__main__":
    main()
