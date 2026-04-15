#!/usr/bin/env python3
"""Apply deterministic terminology cleanup to a transcript directory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src.utils.helpers import load_config, normalize_whitespace
except ImportError:
    import yaml

    def load_config(config_name: str) -> dict[str, object]:
        config_path = ROOT / "config" / config_name
        return yaml.safe_load(config_path.read_text(encoding="utf-8"))

    def normalize_whitespace(value: str) -> str:
        return re.sub(r"\s+", " ", value or "").strip()


@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Refine a YouTube transcript with glossary corrections.")
    parser.add_argument("transcript_dir", help="Transcript artifact directory")
    parser.add_argument(
        "--terms-config",
        default="transcript_terms.yaml",
        help="Config file in config/ containing transcript cleanup rules",
    )
    parser.add_argument(
        "--max-gap-seconds",
        type=float,
        default=1.5,
        help="Merge neighboring segments if the pause is shorter than this value",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=420,
        help="Maximum paragraph length after merging segments",
    )
    return parser


def format_timestamp(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def load_segments(transcript_dir: Path) -> list[TranscriptSegment]:
    payload = json.loads((transcript_dir / "transcript.json").read_text(encoding="utf-8"))
    return [TranscriptSegment(**segment) for segment in payload["segments"]]


def load_metadata(transcript_dir: Path) -> dict[str, object]:
    return json.loads((transcript_dir / "metadata.json").read_text(encoding="utf-8"))


def infer_video_id(transcript_dir: Path, metadata: dict[str, object]) -> str | None:
    explicit = str(metadata.get("video_id", "")).strip()
    if explicit:
        return explicit

    url = str(metadata.get("url", "")).strip()
    if "v=" in url:
        return url.split("v=", 1)[-1].split("&", 1)[0]

    directory_name = transcript_dir.name
    if "-" in directory_name:
        return directory_name.split("-", 1)[0]
    return directory_name or None


def build_replacements(terms_config: dict[str, object], *, video_id: str | None) -> list[tuple[re.Pattern[str], str]]:
    rules: list[tuple[str, str]] = []
    for item in terms_config.get("global_replacements", []):
        rules.append((item["pattern"], item["replacement"]))

    video_specific = terms_config.get("video_specific", {})
    if video_id and video_id in video_specific:
        for item in video_specific[video_id].get("replacements", []):
            rules.append((item["pattern"], item["replacement"]))

    compiled: list[tuple[re.Pattern[str], str]] = []
    for pattern, replacement in rules:
        compiled.append((re.compile(pattern, re.IGNORECASE), replacement))
    return compiled


def clean_text(text: str, replacements: list[tuple[re.Pattern[str], str]]) -> str:
    updated = normalize_whitespace(text)
    for pattern, replacement in replacements:
        updated = pattern.sub(replacement, updated)
    updated = re.sub(r"\bI have asked to\b", "I was asked to", updated)
    updated = re.sub(r"\bThis is a single molecular experiment\b", "This is a single-molecule experiment", updated)
    updated = re.sub(r"\bThis is a very interesting platform\b", "These are very interesting platforms", updated)
    return normalize_whitespace(updated)


def merge_segments(
    segments: list[TranscriptSegment],
    *,
    max_gap_seconds: float,
    max_chars: int,
) -> list[TranscriptSegment]:
    if not segments:
        return []

    merged: list[TranscriptSegment] = []
    current = TranscriptSegment(start=segments[0].start, end=segments[0].end, text=segments[0].text)

    for segment in segments[1:]:
        gap = segment.start - current.end
        candidate_text = f"{current.text} {segment.text}".strip()
        if gap <= max_gap_seconds and len(candidate_text) <= max_chars:
            current.end = segment.end
            current.text = candidate_text
            continue
        merged.append(current)
        current = TranscriptSegment(start=segment.start, end=segment.end, text=segment.text)

    merged.append(current)
    return merged


def render_markdown(metadata: dict[str, object], segments: list[TranscriptSegment]) -> str:
    lines = [
        f"# {metadata['title']}",
        "",
        f"- URL: {metadata['url']}",
        f"- Model: `{metadata['model']}`",
        f"- Requested language: `{metadata['requested_language']}`",
        f"- Detected language: `{metadata['detected_language']}`",
        f"- Refined at: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
        "## Transcript",
        "",
    ]
    for segment in segments:
        lines.append(f"### [{format_timestamp(segment.start)} - {format_timestamp(segment.end)}]")
        lines.append("")
        lines.append(segment.text)
        lines.append("")
    return "\n".join(lines)


def render_plain_text(segments: list[TranscriptSegment]) -> str:
    return "\n\n".join(segment.text for segment in segments)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    transcript_dir = Path(args.transcript_dir).resolve()
    metadata = load_metadata(transcript_dir)
    segments = load_segments(transcript_dir)
    terms_config = load_config(args.terms_config)

    replacements = build_replacements(terms_config, video_id=infer_video_id(transcript_dir, metadata))
    cleaned_segments = [
        TranscriptSegment(start=segment.start, end=segment.end, text=clean_text(segment.text, replacements))
        for segment in segments
        if clean_text(segment.text, replacements)
    ]
    merged_segments = merge_segments(
        cleaned_segments,
        max_gap_seconds=args.max_gap_seconds,
        max_chars=args.max_chars,
    )

    metadata["refined_at"] = datetime.now().isoformat(timespec="seconds")
    metadata["cleanup_rules"] = len(replacements)
    metadata["paragraph_count"] = len(merged_segments)

    (transcript_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (transcript_dir / "transcript.json").write_text(
        json.dumps(
            {
                "segments": [segment.__dict__ for segment in cleaned_segments],
                "segment_count": len(cleaned_segments),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (transcript_dir / "transcript.md").write_text(render_markdown(metadata, merged_segments), encoding="utf-8")
    (transcript_dir / "transcript.txt").write_text(render_plain_text(merged_segments), encoding="utf-8")


if __name__ == "__main__":
    main()
