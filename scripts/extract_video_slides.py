#!/usr/bin/env python3
"""Download a video and extract representative slide frames."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src.utils.helpers import ensure_data_dirs, slugify
except ImportError:
    def ensure_data_dirs() -> None:
        for relative in ["youtube", "youtube/slides"]:
            (ROOT / relative).mkdir(parents=True, exist_ok=True)

    def slugify(value: str, max_length: int = 80) -> str:
        value = re.sub(r"\s+", " ", value or "").strip().lower()
        value = re.sub(r"[^\w\s-]", "", value)
        value = re.sub(r"[\s_]+", "-", value)
        value = re.sub(r"-+", "-", value)
        return value[:max_length].rstrip("-")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract slide-like keyframes from a lecture video.")
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument("--input-video", help="Use an existing local video file instead of downloading from YouTube")
    parser.add_argument("--video-id", help="Video id used when --input-video is provided")
    parser.add_argument("--title", help="Video title used when --input-video is provided")
    parser.add_argument("--output-root", default="youtube/slides", help="Slide artifact root directory")
    parser.add_argument("--scene-threshold", type=float, default=0.12, help="ffmpeg scene change threshold")
    parser.add_argument(
        "--min-gap-seconds",
        type=float,
        default=6.0,
        help="Drop neighboring frames if they appear within this many seconds",
    )
    parser.add_argument("--max-height", type=int, default=1080, help="Maximum downloaded video height")
    parser.add_argument(
        "--minimum-slides",
        type=int,
        default=8,
        help="If scene detection returns fewer slides than this, fall back to interval sampling.",
    )
    parser.add_argument(
        "--fallback-interval-seconds",
        type=float,
        default=180.0,
        help="Sampling interval for fallback extraction when scene detection under-fires.",
    )
    parser.add_argument("--keep-video", action="store_true", help="Keep the downloaded mp4")
    parser.add_argument("--force", action="store_true", help="Overwrite existing extracted slides")
    return parser


def run(command: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=True, capture_output=True, text=True)


def download_video(url: str, working_dir: Path, max_height: int) -> tuple[str, str, Path]:
    from yt_dlp import YoutubeDL

    template = str(working_dir / "source.%(ext)s")
    with YoutubeDL(
        {
            "format": f"bestvideo[height<={max_height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={max_height}][ext=mp4]/best[ext=mp4]/best",
            "outtmpl": template,
            "quiet": True,
            "no_warnings": True,
            "merge_output_format": "mp4",
        }
    ) as ydl:
        info = ydl.extract_info(url, download=True)
        video_id = info["id"]
        title = info.get("title", video_id)
        prepared = Path(ydl.prepare_filename(info))

    video_path = prepared if prepared.exists() else next(working_dir.glob("source.*"))
    return video_id, title, video_path


def resolve_input_video(args: argparse.Namespace, temp_dir: Path) -> tuple[str, str, Path]:
    if args.input_video:
        video_path = Path(args.input_video).expanduser().resolve()
        if not video_path.exists():
            raise SystemExit(f"Missing --input-video file: {video_path}")
        video_id = args.video_id or video_path.stem
        title = args.title or video_path.stem
        return video_id, title, video_path
    if not args.url:
        raise SystemExit("Provide a YouTube URL or --input-video.")
    return download_video(args.url, temp_dir, args.max_height)


def extract_frames(video_path: Path, output_dir: Path, filter_expression: str) -> list[float]:
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "info",
        "-y",
        "-i",
        str(video_path),
        "-vf",
        f"{filter_expression},showinfo,scale=-2:960",
        "-vsync",
        "vfr",
        str(output_dir / "slide-%04d.jpg"),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    timestamps = [float(match.group(1)) for match in re.finditer(r"pts_time:([0-9.]+)", result.stderr)]
    return timestamps


def extract_slides(video_path: Path, output_dir: Path, scene_threshold: float) -> list[float]:
    return extract_frames(video_path, output_dir, f"select='gt(scene,{scene_threshold})'")


def extract_interval_frames(video_path: Path, output_dir: Path, interval_seconds: float) -> list[float]:
    interval_seconds = max(interval_seconds, 1.0)
    return extract_frames(video_path, output_dir, f"fps=1/{interval_seconds}")


def clear_slide_files(destination: Path) -> None:
    for path in destination.glob("slide-*.jpg"):
        path.unlink(missing_ok=True)


def format_timestamp(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def render_index(title: str, url: str, timestamps: list[float], slide_files: list[Path]) -> str:
    lines = [
        f"# Slides: {title}",
        "",
        f"- URL: {url}",
        f"- Slide count: `{len(slide_files)}`",
        "",
        "## Frames",
        "",
    ]
    for idx, slide_file in enumerate(slide_files):
        timestamp = timestamps[idx] if idx < len(timestamps) else 0.0
        lines.append(f"- `{slide_file.name}` @ `{format_timestamp(timestamp)}`")
    lines.append("")
    return "\n".join(lines)


def prune_neighbor_frames(
    slide_files: list[Path],
    timestamps: list[float],
    *,
    min_gap_seconds: float,
) -> tuple[list[Path], list[float]]:
    if not slide_files:
        return [], []

    kept_files: list[Path] = []
    kept_timestamps: list[float] = []
    last_timestamp: float | None = None

    for slide_file, timestamp in zip(slide_files, timestamps, strict=False):
        if last_timestamp is not None and timestamp - last_timestamp < min_gap_seconds:
            slide_file.unlink(missing_ok=True)
            continue
        kept_files.append(slide_file)
        kept_timestamps.append(timestamp)
        last_timestamp = timestamp

    for index, slide_file in enumerate(kept_files, start=1):
        target = slide_file.with_name(f"slide-{index:04d}{slide_file.suffix}")
        if slide_file != target:
            slide_file.rename(target)
            kept_files[index - 1] = target

    return kept_files, kept_timestamps


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    ensure_data_dirs()

    root = ROOT / args.output_root
    temp_root = root / ".tmp"
    temp_root.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(dir=temp_root) as temp_name:
        temp_dir = Path(temp_name)
        video_id, title, video_path = resolve_input_video(args, temp_dir)
        destination = root / f"{video_id}-{slugify(title)}"

        if destination.exists() and not args.force:
            raise SystemExit(f"{destination} already exists. Use --force to overwrite.")

        if destination.exists():
            shutil.rmtree(destination)
        destination.mkdir(parents=True, exist_ok=True)

        timestamps = extract_slides(video_path, destination, args.scene_threshold)
        slide_files = sorted(destination.glob("slide-*.jpg"))
        slide_files, timestamps = prune_neighbor_frames(
            slide_files,
            timestamps,
            min_gap_seconds=args.min_gap_seconds,
        )
        if len(slide_files) < args.minimum_slides:
            clear_slide_files(destination)
            timestamps = extract_interval_frames(video_path, destination, args.fallback_interval_seconds)
            slide_files = sorted(destination.glob("slide-*.jpg"))
        source_url = args.url or f"local:{video_path}"
        (destination / "index.md").write_text(render_index(title, source_url, timestamps, slide_files), encoding="utf-8")

        if args.keep_video and not args.input_video:
            target_video = destination / video_path.name
            video_path.replace(target_video)


if __name__ == "__main__":
    main()
