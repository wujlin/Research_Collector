#!/usr/bin/env python3
"""Extract page images from a PDF with basic self-checks.

This script is intentionally simple and local-first:

1. Split selected pages into single-page PDFs via pypdf
2. Rasterize each single-page PDF to PNG via macOS `sips`
3. Optionally crop the PNG with a fixed box
4. Run basic checks so the output is not silently blank
5. Write a JSON manifest for later reuse

Example:
    python scripts/extract_pdf_page_images.py \
        --pdf pdfs/2026-04-11/foo.pdf \
        --pages 3,9 \
        --out .tmp_figures/foo_check

    python scripts/extract_pdf_page_images.py \
        --pdf pdfs/2026-04-11/foo.pdf \
        --pages 3 \
        --out .tmp_figures/foo_check \
        --crop 120,80,1700,1250
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageStat
from pypdf import PdfReader, PdfWriter


@dataclass
class ImageCheck:
    width: int
    height: int
    bbox_is_none: bool
    grayscale_stddev: float
    non_white_ratio: float


def parse_pages(spec: str) -> list[int]:
    pages: list[int] = []
    for part in spec.split(","):
        item = part.strip()
        if not item:
            continue
        if "-" in item:
            start_s, end_s = item.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            step = 1 if end >= start else -1
            pages.extend(range(start, end + step, step))
        else:
            pages.append(int(item))
    deduped: list[int] = []
    seen: set[int] = set()
    for p in pages:
        if p not in seen:
            seen.add(p)
            deduped.append(p)
    return deduped


def parse_crop(spec: str | None) -> tuple[int, int, int, int] | None:
    if not spec:
        return None
    vals = [int(v.strip()) for v in spec.split(",")]
    if len(vals) != 4:
        raise ValueError("--crop must be x1,y1,x2,y2")
    x1, y1, x2, y2 = vals
    if not (x2 > x1 and y2 > y1):
        raise ValueError("--crop requires x2>x1 and y2>y1")
    return x1, y1, x2, y2


def ensure_sips() -> str:
    tool = shutil.which("sips")
    if not tool:
        raise RuntimeError("`sips` not found; this script currently supports macOS only.")
    return tool


def write_single_page_pdf(reader: PdfReader, page_number: int, out_pdf: Path) -> None:
    writer = PdfWriter()
    writer.add_page(reader.pages[page_number - 1])
    with out_pdf.open("wb") as f:
        writer.write(f)


def rasterize_pdf(sips_path: str, in_pdf: Path, out_png: Path) -> None:
    subprocess.run(
        [sips_path, "-s", "format", "png", str(in_pdf), "--out", str(out_png)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def crop_image(src: Path, dst: Path, crop_box: tuple[int, int, int, int]) -> None:
    with Image.open(src) as img:
        cropped = img.crop(crop_box)
        cropped.save(dst)


def compute_checks(image_path: Path) -> ImageCheck:
    with Image.open(image_path) as img:
        rgb = img.convert("RGB")
        gray = img.convert("L")
        stat = ImageStat.Stat(gray)
        bbox = gray.getbbox()
        pixels = list(rgb.getdata())
        non_white = sum(1 for px in pixels if px != (255, 255, 255))
        total = max(1, len(pixels))
        return ImageCheck(
            width=rgb.width,
            height=rgb.height,
            bbox_is_none=bbox is None,
            grayscale_stddev=float(stat.stddev[0]),
            non_white_ratio=non_white / total,
        )


def validate_checks(check: ImageCheck, label: str) -> list[str]:
    issues: list[str] = []
    if check.width < 400 or check.height < 400:
        issues.append(f"{label}: image too small ({check.width}x{check.height})")
    if check.bbox_is_none:
        issues.append(f"{label}: blank image (bbox is None)")
    if check.grayscale_stddev < 5:
        issues.append(f"{label}: suspiciously low contrast (stddev={check.grayscale_stddev:.2f})")
    if check.non_white_ratio < 0.01:
        issues.append(f"{label}: suspiciously sparse non-white content ({check.non_white_ratio:.4f})")
    return issues


def iter_pages(reader: PdfReader, pages: Iterable[int]) -> list[int]:
    total = len(reader.pages)
    checked: list[int] = []
    for p in pages:
        if p < 1 or p > total:
            raise ValueError(f"page {p} out of range; PDF has {total} pages")
        checked.append(p)
    return checked


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, help="Path to source PDF")
    parser.add_argument("--pages", required=True, help="Pages like 3 or 3,5,7-9")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--crop", help="Optional crop box x1,y1,x2,y2 in output PNG pixels")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    crop_box = parse_crop(args.crop)
    sips_path = ensure_sips()
    reader = PdfReader(str(pdf_path))
    pages = iter_pages(reader, parse_pages(args.pages))

    manifest: dict[str, object] = {
        "pdf": str(pdf_path),
        "pages": pages,
        "crop": crop_box,
        "artifacts": [],
        "issues": [],
    }

    for page_number in pages:
        stem = f"page_{page_number:03d}"
        page_pdf = out_dir / f"{stem}.pdf"
        page_png = out_dir / f"{stem}.png"
        write_single_page_pdf(reader, page_number, page_pdf)
        rasterize_pdf(sips_path, page_pdf, page_png)
        page_check = compute_checks(page_png)
        page_issues = validate_checks(page_check, f"page {page_number}")

        artifact: dict[str, object] = {
            "page": page_number,
            "page_pdf": str(page_pdf),
            "page_png": str(page_png),
            "page_check": asdict(page_check),
        }

        if crop_box:
            crop_png = out_dir / f"{stem}.crop.png"
            crop_image(page_png, crop_png, crop_box)
            crop_check = compute_checks(crop_png)
            crop_issues = validate_checks(crop_check, f"page {page_number} crop")
            artifact["crop_png"] = str(crop_png)
            artifact["crop_check"] = asdict(crop_check)
            page_issues.extend(crop_issues)

        manifest["artifacts"].append(artifact)
        manifest["issues"].extend(page_issues)

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n")

    print(f"wrote manifest: {manifest_path}")
    if manifest["issues"]:
        print("issues:")
        for issue in manifest["issues"]:
            print(f"- {issue}")
    else:
        print("all checks passed")


if __name__ == "__main__":
    main()
