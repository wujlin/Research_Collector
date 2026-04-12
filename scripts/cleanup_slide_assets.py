#!/usr/bin/env python3
"""Clean lecture slide artifacts by cropping curated frames and purging legacy raw frames."""

from __future__ import annotations

import argparse
from math import ceil
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Crop curated lecture slides and remove legacy raw artifacts.")
    parser.add_argument("slide_root", help="Lecture slide directory, e.g. youtube/slides/<video-id-title>")
    parser.add_argument("--brightness-threshold", type=float, default=15.0, help="Threshold for non-black columns")
    parser.add_argument("--purge-root", action="store_true", help="Delete legacy slide-*.jpg and root contact sheet")
    parser.add_argument("--dry-run", action="store_true", help="Report actions without writing files")
    return parser


def curated_images(curated_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in curated_dir.glob("*.jpg")
        if path.stem[:2].isdigit()
    )


def detect_crop_box(image_paths: list[Path], threshold: float) -> tuple[int, int, int, int]:
    left_edges: list[int] = []
    right_edges: list[int] = []
    widths: list[int] = []
    heights: list[int] = []

    for path in image_paths:
        image = Image.open(path).convert("L")
        widths.append(image.width)
        heights.append(image.height)
        pixels = image.load()

        def column_mean(x: int) -> float:
            return sum(pixels[x, y] for y in range(image.height)) / image.height

        left = next((x for x in range(image.width) if column_mean(x) > threshold), 0)
        right = next((x for x in range(image.width - 1, -1, -1) if column_mean(x) > threshold), image.width - 1)
        left_edges.append(left)
        right_edges.append(right)

    left = max(left_edges)
    right = min(right_edges) + 1
    top = 0
    bottom = min(heights)

    if left >= right:
        raise ValueError("Invalid crop box detected; check the slide inputs.")
    return left, top, right, bottom


def crop_images(image_paths: list[Path], crop_box: tuple[int, int, int, int], dry_run: bool) -> None:
    for path in image_paths:
        with Image.open(path) as image:
            cropped = image.crop(crop_box)
            scrub_conference_tile(cropped)
            if not dry_run:
                cropped.save(path, quality=95)


def scrub_conference_tile(image: Image.Image) -> None:
    """Mask the small video-conference tile that sits in the top-right corner."""
    overlay_width = min(118, image.width)
    overlay_height = min(88, image.height)
    left = image.width - overlay_width
    draw = ImageDraw.Draw(image)
    draw.rectangle((left, 0, image.width, overlay_height), fill="white")


def build_contact_sheet(image_paths: list[Path], output_path: Path, dry_run: bool) -> None:
    thumb_width = 360
    thumb_height = 202
    columns = 3
    margin = 24
    label_height = 28
    rows = ceil(len(image_paths) / columns)
    sheet_width = columns * thumb_width + (columns + 1) * margin
    sheet_height = rows * (thumb_height + label_height) + (rows + 1) * margin

    sheet = Image.new("RGB", (sheet_width, sheet_height), "white")
    draw = ImageDraw.Draw(sheet)

    for index, path in enumerate(image_paths):
        row, column = divmod(index, columns)
        x = margin + column * (thumb_width + margin)
        y = margin + row * (thumb_height + label_height + margin)

        with Image.open(path) as image:
            thumb = ImageOps.contain(image.convert("RGB"), (thumb_width, thumb_height))
        thumb_x = x + (thumb_width - thumb.width) // 2
        thumb_y = y + (thumb_height - thumb.height) // 2
        sheet.paste(thumb, (thumb_x, thumb_y))
        draw.rectangle((x, y, x + thumb_width, y + thumb_height), outline="#d0d7de", width=2)
        draw.text((x, y + thumb_height + 6), path.stem, fill="#24292f")

    if not dry_run:
        sheet.save(output_path, quality=92)


def purge_legacy_root(slide_root: Path, dry_run: bool) -> list[str]:
    removed: list[str] = []
    for path in sorted(slide_root.glob("slide-*.jpg")):
        removed.append(path.name)
        if not dry_run:
            path.unlink(missing_ok=True)

    legacy_contact_sheet = slide_root / "contact_sheet.jpg"
    if legacy_contact_sheet.exists():
        removed.append(legacy_contact_sheet.name)
        if not dry_run:
            legacy_contact_sheet.unlink()

    return removed


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    slide_root = Path(args.slide_root).resolve()
    curated_dir = slide_root / "curated"
    if not curated_dir.exists():
        raise SystemExit(f"Missing curated directory: {curated_dir}")

    image_paths = curated_images(curated_dir)
    if not image_paths:
        raise SystemExit(f"No curated slide images found in {curated_dir}")

    crop_box = detect_crop_box(image_paths, args.brightness_threshold)
    print(f"crop_box={crop_box}")
    crop_images(image_paths, crop_box, args.dry_run)
    build_contact_sheet(image_paths, curated_dir / "contact_sheet.jpg", args.dry_run)

    removed: list[str] = []
    if args.purge_root:
        removed = purge_legacy_root(slide_root, args.dry_run)
    if removed:
        print("removed=" + ",".join(removed))


if __name__ == "__main__":
    main()
