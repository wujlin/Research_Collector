#!/usr/bin/env python3
"""Copy PDF-derived digest images into dated, Git-tracked digest figure folders."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIGESTS = ROOT / "digests"
IMAGE_RE = re.compile(r"!\[(?P<alt>[^]]*)]\((?P<target>[^)]+)\)")


def resolve_source(note: Path, target: str) -> Path | None:
    clean_target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if clean_target.startswith(("http://", "https://", "data:")):
        return None

    direct = (note.parent / clean_target).resolve()
    if direct.exists():
        return direct

    normalized = clean_target.replace("\\", "/")
    marker = "pdfs/"
    if marker in normalized:
        pdf_relative = normalized.split(marker, 1)[1]
        for base in (ROOT / "pdfs", ROOT / "web" / "out" / "pdfs"):
            fallback = base / pdf_relative
            if fallback.exists():
                return fallback.resolve()
    return None


def is_pdf_derived(path: Path) -> bool:
    for base in (ROOT / "pdfs", ROOT / "web" / "out" / "pdfs"):
        try:
            path.relative_to(base)
            return True
        except ValueError:
            continue
    return False


def destination_for(note: Path, source: Path) -> Path:
    relative_note = note.relative_to(DIGESTS)
    date_dir = DIGESTS / relative_note.parts[0]
    destination_dir = date_dir / "figures" / note.stem
    destination = destination_dir / source.name
    if not destination.exists():
        return destination
    if destination.read_bytes() == source.read_bytes():
        return destination
    digest = hashlib.sha256(source.read_bytes()).hexdigest()[:8]
    return destination_dir / f"{source.stem}-{digest}{source.suffix.lower()}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Copy images and rewrite Markdown references.")
    args = parser.parse_args()

    copied: set[Path] = set()
    rewritten_notes = 0
    unresolved: list[tuple[str, str]] = []

    for note in sorted(DIGESTS.rglob("*.md")):
        content = note.read_text(encoding="utf-8")
        changed = False

        def replace(match: re.Match[str]) -> str:
            nonlocal changed
            target = match.group("target").strip()
            if target.startswith(("http://", "https://", "data:")):
                return match.group(0)
            source = resolve_source(note, target)
            if source is None:
                unresolved.append((note.relative_to(ROOT).as_posix(), target))
                return match.group(0)
            if not is_pdf_derived(source):
                return match.group(0)

            destination = destination_for(note, source)
            if args.apply:
                destination.parent.mkdir(parents=True, exist_ok=True)
                if not destination.exists():
                    shutil.copy2(source, destination)
                relative_target = Path(os.path.relpath(destination, note.parent)).as_posix()
                changed = changed or relative_target != target
                copied.add(destination)
                return f"![{match.group('alt')}]({relative_target})"
            copied.add(destination)
            return match.group(0)

        rewritten = IMAGE_RE.sub(replace, content)
        if args.apply and changed and rewritten != content:
            note.write_text(rewritten, encoding="utf-8")
            rewritten_notes += 1

    print(
        {
            "applied": args.apply,
            "vendored_images": len(copied),
            "rewritten_notes": rewritten_notes,
            "unresolved_count": len(unresolved),
            "unresolved": unresolved,
        }
    )
    if unresolved:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
