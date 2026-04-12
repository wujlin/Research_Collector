#!/usr/bin/env python3
"""Download YouTube audio and transcribe it locally with faster-whisper."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src.utils.helpers import ensure_data_dirs, slugify
except ImportError:
    def ensure_data_dirs() -> None:
        for relative in ["data", "digests", "library", "youtube", "youtube/transcripts"]:
            Path(relative).mkdir(parents=True, exist_ok=True)

    def slugify(value: str, max_length: int = 80) -> str:
        value = re.sub(r"\s+", " ", value or "").strip().lower()
        value = re.sub(r"[^\w\s-]", "", value)
        value = re.sub(r"[\s_]+", "-", value)
        value = re.sub(r"-+", "-", value)
        return value[:max_length].rstrip("-")


@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download a YouTube video and transcribe it locally.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--output-root",
        default="youtube/transcripts",
        help="Directory where transcript artifacts will be written",
    )
    parser.add_argument("--model", default="large-v3", help="faster-whisper model name")
    parser.add_argument(
        "--backend",
        default="auto",
        choices=["auto", "faster-whisper", "whisper"],
        help="ASR backend. 'auto' tries faster-whisper first, then openai-whisper.",
    )
    parser.add_argument(
        "--language",
        default="en",
        help="Language hint passed to ASR. Use 'auto' for detection.",
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cpu", "cuda"],
        help="Inference device",
    )
    parser.add_argument(
        "--compute-type",
        default="auto",
        help="CTranslate2 compute type. Examples: float16, int8_float16, int8",
    )
    parser.add_argument("--beam-size", type=int, default=5, help="Beam size for transcription")
    parser.add_argument(
        "--initial-prompt",
        default="",
        help="Optional domain prompt passed to the ASR backend.",
    )
    parser.add_argument(
        "--keep-audio",
        action="store_true",
        help="Keep the downloaded audio file after transcription",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing transcript artifacts for the same video",
    )
    return parser


def format_timestamp(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def render_transcript_markdown(
    *,
    title: str,
    url: str,
    model: str,
    language: str,
    detected_language: str,
    segments: list[TranscriptSegment],
) -> str:
    lines = [
        f"# {title}",
        "",
        f"- URL: {url}",
        f"- Model: `{model}`",
        f"- Requested language: `{language}`",
        f"- Detected language: `{detected_language}`",
        f"- Generated at: `{datetime.now().isoformat(timespec='seconds')}`",
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


def _choose_device(preferred: str) -> str:
    if preferred != "auto":
        return preferred
    try:
        import torch

        return "cuda" if torch.cuda.is_available() else "cpu"
    except Exception:
        return "cpu"


def _choose_compute_type(preferred: str, device: str) -> str:
    if preferred != "auto":
        return preferred
    return "float16" if device == "cuda" else "int8"


def _load_ytdlp():
    try:
        from yt_dlp import YoutubeDL
    except ImportError as exc:
        raise SystemExit("yt-dlp is not installed in the current environment.") from exc
    return YoutubeDL


def _load_faster_whisper():
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise SystemExit("faster-whisper is not installed in the current environment.") from exc
    return WhisperModel


def _load_openai_whisper():
    try:
        import whisper
    except ImportError as exc:
        raise SystemExit("openai-whisper is not installed in the current environment.") from exc
    return whisper


def download_audio(url: str, output_dir: Path) -> tuple[dict[str, Any], Path]:
    YoutubeDL = _load_ytdlp()
    output_dir.mkdir(parents=True, exist_ok=True)
    template = str(output_dir / "source.%(ext)s")
    with YoutubeDL(
        {
            "format": "bestaudio/best",
            "outtmpl": template,
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "restrictfilenames": False,
        }
    ) as ydl:
        info = ydl.extract_info(url, download=True)
        prepared = Path(ydl.prepare_filename(info))
    audio_path = _resolve_downloaded_audio(prepared, output_dir)
    return info, audio_path


def _resolve_downloaded_audio(prepared_path: Path, output_dir: Path) -> Path:
    if prepared_path.exists():
        return prepared_path
    candidates = sorted(output_dir.glob("source.*"))
    if not candidates:
        raise FileNotFoundError("Downloaded audio file was not found.")
    return candidates[0]


def transcribe_audio(
    audio_path: Path,
    *,
    backend: str,
    model_name: str,
    language: str,
    device: str,
    compute_type: str,
    beam_size: int,
    initial_prompt: str,
) -> tuple[list[TranscriptSegment], dict[str, Any], str]:
    if backend == "auto":
        try:
            return _transcribe_with_faster_whisper(
                audio_path,
                model_name=model_name,
                language=language,
                device=device,
                compute_type=compute_type,
                beam_size=beam_size,
                initial_prompt=initial_prompt,
            )
        except SystemExit:
            return _transcribe_with_openai_whisper(
                audio_path,
                model_name=model_name,
                language=language,
                device=device,
                beam_size=beam_size,
                initial_prompt=initial_prompt,
            )
    if backend == "faster-whisper":
        return _transcribe_with_faster_whisper(
            audio_path,
            model_name=model_name,
            language=language,
            device=device,
            compute_type=compute_type,
            beam_size=beam_size,
            initial_prompt=initial_prompt,
        )
    return _transcribe_with_openai_whisper(
        audio_path,
        model_name=model_name,
        language=language,
        device=device,
        beam_size=beam_size,
        initial_prompt=initial_prompt,
    )


def _transcribe_with_faster_whisper(
    audio_path: Path,
    *,
    model_name: str,
    language: str,
    device: str,
    compute_type: str,
    beam_size: int,
    initial_prompt: str,
) -> tuple[list[TranscriptSegment], dict[str, Any], str]:
    WhisperModel = _load_faster_whisper()
    model = WhisperModel(model_name, device=device, compute_type=compute_type)
    kwargs: dict[str, Any] = {"beam_size": beam_size}
    if language and language != "auto":
        kwargs["language"] = language
    if initial_prompt:
        kwargs["initial_prompt"] = initial_prompt
    segments, info = model.transcribe(str(audio_path), **kwargs)
    parsed_segments = [
        TranscriptSegment(start=segment.start, end=segment.end, text=segment.text.strip())
        for segment in segments
        if segment.text.strip()
    ]
    metadata = {
        "language": getattr(info, "language", ""),
        "language_probability": getattr(info, "language_probability", None),
        "duration": getattr(info, "duration", None),
    }
    return parsed_segments, metadata, "faster-whisper"


def _transcribe_with_openai_whisper(
    audio_path: Path,
    *,
    model_name: str,
    language: str,
    device: str,
    beam_size: int,
    initial_prompt: str,
) -> tuple[list[TranscriptSegment], dict[str, Any], str]:
    whisper = _load_openai_whisper()
    model = whisper.load_model(model_name, device=device)
    kwargs: dict[str, Any] = {"verbose": False, "beam_size": beam_size, "fp16": device == "cuda"}
    if language and language != "auto":
        kwargs["language"] = language
    if initial_prompt:
        kwargs["initial_prompt"] = initial_prompt
    result = model.transcribe(str(audio_path), **kwargs)
    parsed_segments = [
        TranscriptSegment(
            start=float(segment["start"]),
            end=float(segment["end"]),
            text=str(segment["text"]).strip(),
        )
        for segment in result.get("segments", [])
        if str(segment.get("text", "")).strip()
    ]
    metadata = {
        "language": result.get("language", ""),
        "language_probability": None,
        "duration": None,
    }
    return parsed_segments, metadata, "whisper"


def write_artifacts(
    output_dir: Path,
    *,
    title: str,
    url: str,
    backend: str,
    model_name: str,
    requested_language: str,
    detected_language: str,
    segments: list[TranscriptSegment],
    metadata: dict[str, Any],
) -> dict[str, Path]:
    transcript_json = output_dir / "transcript.json"
    transcript_txt = output_dir / "transcript.txt"
    transcript_md = output_dir / "transcript.md"
    metadata_json = output_dir / "metadata.json"

    metadata_payload = {
        "title": title,
        "url": url,
        "backend": backend,
        "model": model_name,
        "requested_language": requested_language,
        "detected_language": detected_language,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        **metadata,
    }
    transcript_payload = {
        "segments": [asdict(segment) for segment in segments],
        "segment_count": len(segments),
    }

    metadata_json.write_text(json.dumps(metadata_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    transcript_json.write_text(json.dumps(transcript_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    transcript_txt.write_text("\n".join(segment.text for segment in segments), encoding="utf-8")
    transcript_md.write_text(
        render_transcript_markdown(
            title=title,
            url=url,
            model=model_name,
            language=requested_language,
            detected_language=detected_language,
            segments=segments,
        ),
        encoding="utf-8",
    )
    return {
        "metadata_json": metadata_json,
        "transcript_json": transcript_json,
        "transcript_txt": transcript_txt,
        "transcript_md": transcript_md,
    }


def build_output_dir(output_root: Path, info: dict[str, Any]) -> Path:
    title = info.get("title") or info.get("id") or "youtube-video"
    slug = slugify(title, max_length=60)
    video_id = info.get("id", "video")
    return output_root / f"{video_id}-{slug}"


def main() -> None:
    args = build_parser().parse_args()
    ensure_data_dirs()

    output_root = Path(args.output_root)
    temp_root = output_root / ".tmp"
    temp_root.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(dir=temp_root) as temp_name:
        temp_dir = Path(temp_name)
        info, audio_path = download_audio(args.url, temp_dir)
        output_dir = build_output_dir(output_root, info)
        if output_dir.exists() and not args.force:
            raise SystemExit(f"Transcript directory already exists: {output_dir}. Use --force to overwrite.")
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        final_audio_path = output_dir / audio_path.name
        audio_path.replace(final_audio_path)

        device = _choose_device(args.device)
        compute_type = _choose_compute_type(args.compute_type, device)
        segments, metadata, resolved_backend = transcribe_audio(
            final_audio_path,
            backend=args.backend,
            model_name=args.model,
            language=args.language,
            device=device,
            compute_type=compute_type,
            beam_size=args.beam_size,
            initial_prompt=args.initial_prompt,
        )
        detected_language = metadata.get("language") or "unknown"
        outputs = write_artifacts(
            output_dir,
            title=info.get("title", "YouTube Transcript"),
            url=info.get("webpage_url") or args.url,
            backend=resolved_backend,
            model_name=args.model,
            requested_language=args.language,
            detected_language=detected_language,
            segments=segments,
            metadata=metadata,
        )

        if not args.keep_audio and final_audio_path.exists():
            final_audio_path.unlink()

        summary = {
            "title": info.get("title", ""),
            "video_id": info.get("id", ""),
            "backend": resolved_backend,
            "device": device,
            "compute_type": compute_type,
            "segment_count": len(segments),
            "output_dir": str(output_dir),
            "artifacts": {key: str(path) for key, path in outputs.items()},
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
