#!/usr/bin/env python3
"""Move library Markdown files not referenced by the database into an explicit archive."""

from __future__ import annotations

import argparse
import shutil
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "library"
ARCHIVE = LIBRARY / "archive" / "legacy_unmanaged_2026-07-11"


def unmanaged_files() -> list[Path]:
    connection = sqlite3.connect(ROOT / "data" / "papers.db")
    managed = {
        row[0]
        for row in connection.execute("SELECT markdown_path FROM papers WHERE markdown_path <> ''")
    }
    connection.close()

    candidates = []
    for path in LIBRARY.rglob("*.md"):
        relative = path.relative_to(LIBRARY)
        if relative.parts[0] == "archive":
            continue
        if path.name == "_index.md" or relative.as_posix() == "index.md":
            continue
        if relative.as_posix() not in managed:
            candidates.append(path)
    return sorted(candidates)


def write_archive_readme(moved: list[tuple[Path, Path]]) -> None:
    readme = LIBRARY / "archive" / "README.md"
    lines = [
        "# Library Archive",
        "",
        "Files here are preserved historical Markdown records that are not managed by the current",
        "SQLite paper catalog. They are excluded from generated topic counts and integrity checks.",
        "",
        "## Legacy unmanaged files archived on 2026-07-11",
        "",
    ]
    for source, destination in moved:
        original = source.relative_to(LIBRARY).as_posix()
        archived = destination.relative_to(readme.parent).as_posix()
        lines.append(f"- [{source.stem}]({archived}) (formerly `{original}`)")
    readme.parent.mkdir(parents=True, exist_ok=True)
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Move files instead of only listing them.")
    args = parser.parse_args()

    candidates = unmanaged_files()
    moved: list[tuple[Path, Path]] = []
    if args.apply:
        for source in candidates:
            relative = source.relative_to(LIBRARY)
            destination = ARCHIVE / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(source, destination)
            moved.append((source, destination))
        write_archive_readme(moved)

    print(
        {
            "applied": args.apply,
            "unmanaged_count": len(candidates),
            "paths": [path.relative_to(LIBRARY).as_posix() for path in candidates],
        }
    )


if __name__ == "__main__":
    main()
