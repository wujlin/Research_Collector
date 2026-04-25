#!/usr/bin/env python3
"""Rename MinerU image assets to stable page/type-based file names.

Example:
    python scripts/rename_mineru_images.py \
        pdfs/2026-04-11/dynamical-regimes-of-diffusion-models.mineru/hybrid_auto
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


KIND_MAP = {
    "image": "figure",
    "table": "table",
    "interline_equation": "equation",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", help="MinerU output dir, usually .../<paper>.mineru/hybrid_auto")
    parser.add_argument("--dry-run", action="store_true", help="Show planned renames without writing files")
    return parser


def load_middle_json(output_dir: Path) -> tuple[Path, list[dict[str, object]]]:
    candidates = sorted(output_dir.glob("*_middle.json"))
    if len(candidates) != 1:
        raise RuntimeError(f"Expected exactly one *_middle.json in {output_dir}, got {len(candidates)}")
    middle_path = candidates[0]
    payload = json.loads(middle_path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return middle_path, payload
    if isinstance(payload, dict) and isinstance(payload.get("pdf_info"), list):
        return middle_path, payload["pdf_info"]
    raise RuntimeError(f"Unexpected middle json structure in {middle_path}")


def collect_image_records(payload: list[dict[str, object]]) -> list[tuple[str, int, str]]:
    records: list[tuple[str, int, str]] = []
    for page in payload:
        raw_page_idx = int(page.get("page_idx", -1))
        if raw_page_idx < 0:
            continue
        page_number = raw_page_idx + 1

        def walk(obj: object) -> None:
            if isinstance(obj, dict):
                image_path = obj.get("image_path")
                image_type = obj.get("type")
                if isinstance(image_path, str) and isinstance(image_type, str):
                    records.append((image_path, page_number, image_type))
                for value in obj.values():
                    walk(value)
            elif isinstance(obj, list):
                for value in obj:
                    walk(value)
        walk(page)
    return records


def build_rename_map(records: list[tuple[str, int, str]]) -> dict[str, str]:
    rename_map: dict[str, str] = {}
    counters: dict[tuple[int, str], int] = defaultdict(int)
    for image_path, page_idx, image_type in records:
        if image_path in rename_map:
            continue
        kind = KIND_MAP.get(image_type, image_type.replace("_", "-"))
        counters[(page_idx, kind)] += 1
        suffix = Path(image_path).suffix.lower() or ".jpg"
        rename_map[image_path] = f"page-{page_idx:02d}-{kind}-{counters[(page_idx, kind)]:02d}{suffix}"
    return rename_map


def rewrite_text_references(output_dir: Path, rename_map: dict[str, str], dry_run: bool) -> None:
    text_files = sorted(
        path for path in output_dir.iterdir() if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )
    for text_file in text_files:
        content = text_file.read_text(encoding="utf-8")
        updated = content
        for old_name, new_name in rename_map.items():
            updated = updated.replace(f"images/{old_name}", f"images/{new_name}")
            updated = updated.replace(f'"{old_name}"', f'"{new_name}"')
        if updated != content and not dry_run:
            text_file.write_text(updated, encoding="utf-8")


def rename_image_files(output_dir: Path, rename_map: dict[str, str], dry_run: bool) -> None:
    images_dir = output_dir / "images"
    if not images_dir.is_dir():
        raise RuntimeError(f"Missing images dir: {images_dir}")

    operations: list[tuple[Path, Path]] = []
    for old_name, new_name in rename_map.items():
        if old_name == new_name:
            continue
        src = images_dir / old_name
        dst = images_dir / new_name
        if not src.exists():
            continue
        operations.append((src, dst))

    if dry_run:
        for src, dst in operations:
            print(f"{src.name} -> {dst.name}")
        return

    staged: list[tuple[Path, Path]] = []
    for idx, (src, dst) in enumerate(operations):
        tmp = images_dir / f".rename-tmp-{idx}-{src.name}"
        if tmp.exists():
            raise RuntimeError(f"Temporary rename path already exists: {tmp}")
        src.rename(tmp)
        staged.append((tmp, dst))

    for tmp, dst in staged:
        if dst.exists():
            raise RuntimeError(f"Refusing to overwrite existing image: {dst}")
        tmp.rename(dst)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    output_dir = Path(args.output_dir).expanduser().resolve()
    _, payload = load_middle_json(output_dir)
    records = collect_image_records(payload)
    rename_map = build_rename_map(records)
    if not rename_map:
        raise RuntimeError(f"No image records found in {output_dir}")

    rename_image_files(output_dir, rename_map, dry_run=args.dry_run)
    rewrite_text_references(output_dir, rename_map, dry_run=args.dry_run)

    print(f"renamed {len(rename_map)} image assets in {output_dir}")
    for old_name, new_name in sorted(rename_map.items()):
        print(f"{old_name} -> {new_name}")


if __name__ == "__main__":
    main()
