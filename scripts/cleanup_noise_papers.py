#!/usr/bin/env python3
"""删除已确认的噪音论文，并刷新导出产物。"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline


NOISE_TITLE_PATTERNS = [
    "mutagenesis on syntaxin-1a-munc-18a complex formation",
    "methods for molecular recognition computing",
]


def remove_empty_directories(root: Path) -> None:
    for directory in sorted(root.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()


def main() -> None:
    pipeline = CollectionPipeline()
    papers = pipeline.database.list_papers(limit=500)
    targets = [
        paper for paper in papers
        if any(pattern in paper.title.lower() for pattern in NOISE_TITLE_PATTERNS)
    ]

    markdown_paths = [paper.markdown_path for paper in targets if paper.markdown_path]
    removed = pipeline.database.delete_papers_by_ids([paper.id for paper in targets])

    for relative_path in markdown_paths:
        file_path = ROOT / "library" / relative_path
        if file_path.exists():
            file_path.unlink()

    old_reading_list = ROOT / "library" / "reading_list.md"
    if old_reading_list.exists():
        old_reading_list.unlink()

    remove_empty_directories(ROOT / "library")
    pipeline._refresh_library_indices()
    pipeline.export_all()

    print(
        {
            "removed_papers": removed,
            "titles": [paper.title for paper in targets],
        }
    )


if __name__ == "__main__":
    main()
