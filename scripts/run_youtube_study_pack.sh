#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/run_youtube_study_pack.sh \
    --url URL \
    --id VIDEO_ID \
    --slug SLUG \
    --title TITLE \
    [--transcript-slug SLUG] \
    [--prompt PROMPT] \
    [--model large-v3] \
    [--language en] \
    [--device cuda] \
    [--compute-type float16] \
    [--beam-size 8] \
    [--minimum-slides 10] \
    [--fallback-interval-seconds 150] \
    [--force-slides]

Runs the Research_Collector YouTube study-pack pipeline:
  metadata -> audio -> transcript -> video -> slide frames.

The runner is idempotent. It skips completed artifacts and uses flock locks for
heavy steps instead of waiting on fuzzy process names.
EOF
}

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

URL=""
VIDEO_ID=""
SLUG=""
TITLE=""
TRANSCRIPT_SLUG=""
PROMPT=""
MODEL="large-v3"
LANGUAGE="en"
DEVICE="cuda"
COMPUTE_TYPE="float16"
BEAM_SIZE="8"
MINIMUM_SLIDES="10"
FALLBACK_INTERVAL_SECONDS="150"
FORCE_SLIDES="0"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --url) URL="$2"; shift 2 ;;
    --id) VIDEO_ID="$2"; shift 2 ;;
    --slug) SLUG="$2"; shift 2 ;;
    --title) TITLE="$2"; shift 2 ;;
    --transcript-slug) TRANSCRIPT_SLUG="$2"; shift 2 ;;
    --prompt) PROMPT="$2"; shift 2 ;;
    --model) MODEL="$2"; shift 2 ;;
    --language) LANGUAGE="$2"; shift 2 ;;
    --device) DEVICE="$2"; shift 2 ;;
    --compute-type) COMPUTE_TYPE="$2"; shift 2 ;;
    --beam-size) BEAM_SIZE="$2"; shift 2 ;;
    --minimum-slides) MINIMUM_SLIDES="$2"; shift 2 ;;
    --fallback-interval-seconds) FALLBACK_INTERVAL_SECONDS="$2"; shift 2 ;;
    --force-slides) FORCE_SLIDES="1"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ -z "$URL" || -z "$VIDEO_ID" || -z "$SLUG" || -z "$TITLE" ]]; then
  usage >&2
  exit 2
fi

if [[ -z "$TRANSCRIPT_SLUG" ]]; then
  TRANSCRIPT_SLUG="$SLUG"
fi

AUDIO_DIR="youtube/audio/${SLUG}"
VIDEO_DIR="youtube/video/${SLUG}"
TRANSCRIPT_DIR="youtube/transcripts/${VIDEO_ID}-${TRANSCRIPT_SLUG}"
LOG_DIR="youtube/logs"
SLIDES_ROOT="youtube/slides"

mkdir -p "$AUDIO_DIR" "$VIDEO_DIR" "$TRANSCRIPT_DIR" "$LOG_DIR" "$SLIDES_ROOT"

log() {
  printf '[%s] %s\n' "$(date '+%F %T')" "$*"
}

first_existing_audio() {
  find "$AUDIO_DIR" -maxdepth 1 -type f \
    \( -name 'source.m4a' -o -name 'source.mp3' -o -name 'source.opus' -o -name 'source.webm' -o -name 'source.wav' \) \
    | sort | head -n 1
}

first_existing_video() {
  find "$VIDEO_DIR" -maxdepth 1 -type f \
    \( -name 'source.mp4' -o -name 'source.webm' -o -name 'source.mkv' \) \
    | sort | head -n 1
}

slide_dir() {
  find "$SLIDES_ROOT" -maxdepth 1 -type d -name "${VIDEO_ID}-*" | sort | head -n 1
}

slide_count() {
  local dir="$1"
  if [[ -z "$dir" || ! -d "$dir" ]]; then
    echo 0
    return
  fi
  find "$dir" -maxdepth 1 -type f -name 'slide-*.jpg' | wc -l | tr -d ' '
}

if [[ ! -s "$AUDIO_DIR/metadata.json" ]]; then
  log "metadata start"
  yt-dlp --dump-single-json --skip-download "$URL" > "$AUDIO_DIR/metadata.json"
  log "metadata done"
else
  log "metadata exists: $AUDIO_DIR/metadata.json"
fi

AUDIO_PATH="$(first_existing_audio)"
if [[ -z "$AUDIO_PATH" ]]; then
  log "audio download start"
  flock /tmp/research_collector_youtube_audio_download.lock \
    yt-dlp --continue --retries infinite --fragment-retries infinite --retry-sleep 5 --socket-timeout 30 --no-playlist \
      --extract-audio --audio-format m4a --audio-quality 0 \
      -o "${AUDIO_DIR}/source.%(ext)s" "$URL"
  AUDIO_PATH="$(first_existing_audio)"
  if [[ -z "$AUDIO_PATH" ]]; then
    echo "Audio download finished but no source audio found in $AUDIO_DIR" >&2
    exit 1
  fi
  log "audio download done: $AUDIO_PATH"
else
  log "audio exists: $AUDIO_PATH"
fi

if [[ ! -s "$TRANSCRIPT_DIR/transcript.md" || ! -s "$TRANSCRIPT_DIR/transcript.json" ]]; then
  log "ASR start"
  env \
    RC_AUDIO_PATH="$AUDIO_PATH" \
    RC_OUTPUT_DIR="$TRANSCRIPT_DIR" \
    RC_TITLE="$TITLE" \
    RC_URL="$URL" \
    RC_PROMPT="$PROMPT" \
    RC_MODEL="$MODEL" \
    RC_LANGUAGE="$LANGUAGE" \
    RC_DEVICE="$DEVICE" \
    RC_COMPUTE_TYPE="$COMPUTE_TYPE" \
    RC_BEAM_SIZE="$BEAM_SIZE" \
    flock /tmp/research_collector_youtube_asr.lock python - <<'PY'
from pathlib import Path
import importlib.util
import json
import os
import shutil
import sys

repo = Path.cwd()
module_path = repo / "scripts" / "transcribe_youtube.py"
spec = importlib.util.spec_from_file_location("transcribe_youtube", module_path)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)

audio = Path(os.environ["RC_AUDIO_PATH"])
output_dir = Path(os.environ["RC_OUTPUT_DIR"])
output_dir.mkdir(parents=True, exist_ok=True)
transcript_audio = output_dir / audio.name
if not transcript_audio.exists() or transcript_audio.stat().st_size != audio.stat().st_size:
    shutil.copy2(audio, transcript_audio)

segments, metadata, backend_used = mod.transcribe_audio(
    transcript_audio,
    backend="faster-whisper",
    model_name=os.environ["RC_MODEL"],
    language=os.environ["RC_LANGUAGE"],
    device=os.environ["RC_DEVICE"],
    compute_type=os.environ["RC_COMPUTE_TYPE"],
    beam_size=int(os.environ["RC_BEAM_SIZE"]),
    initial_prompt=os.environ.get("RC_PROMPT", ""),
)
outputs = mod.write_artifacts(
    output_dir=output_dir,
    title=os.environ["RC_TITLE"],
    url=os.environ["RC_URL"],
    backend=backend_used,
    model_name=os.environ["RC_MODEL"],
    requested_language=os.environ["RC_LANGUAGE"],
    detected_language=metadata.get("language") or "unknown",
    segments=segments,
    metadata=metadata,
)
print(json.dumps({
    "output_dir": str(output_dir),
    "backend": backend_used,
    "segments": len(segments),
    "metadata": metadata,
    "artifacts": {k: str(v) for k, v in outputs.items()},
}, ensure_ascii=False, indent=2))
PY
  log "ASR done: $TRANSCRIPT_DIR"
else
  log "transcript exists: $TRANSCRIPT_DIR"
fi

VIDEO_PATH="$(first_existing_video)"
if [[ -z "$VIDEO_PATH" ]]; then
  log "video download start"
  flock /tmp/research_collector_youtube_video_download.lock \
    yt-dlp --continue --retries infinite --fragment-retries infinite --retry-sleep 5 --socket-timeout 30 --no-playlist \
      -f "bestvideo[height<=720][ext=mp4]/bestvideo[height<=720]/best[height<=720]" \
      -o "${VIDEO_DIR}/source.%(ext)s" "$URL"
  VIDEO_PATH="$(first_existing_video)"
  if [[ -z "$VIDEO_PATH" ]]; then
    echo "Video download finished but no source video found in $VIDEO_DIR" >&2
    exit 1
  fi
  log "video download done: $VIDEO_PATH"
else
  log "video exists: $VIDEO_PATH"
fi

SLIDE_DIR="$(slide_dir)"
SLIDE_COUNT="$(slide_count "$SLIDE_DIR")"
if [[ "$FORCE_SLIDES" == "1" || "$SLIDE_COUNT" -lt "$MINIMUM_SLIDES" ]]; then
  log "slide extraction start: $VIDEO_PATH"
  python scripts/extract_video_slides.py \
    --input-video "$VIDEO_PATH" \
    --video-id "$VIDEO_ID" \
    --title "$TITLE" \
    --minimum-slides "$MINIMUM_SLIDES" \
    --fallback-interval-seconds "$FALLBACK_INTERVAL_SECONDS" \
    --force
  SLIDE_DIR="$(slide_dir)"
  SLIDE_COUNT="$(slide_count "$SLIDE_DIR")"
  log "slide extraction done: ${SLIDE_DIR:-missing} (${SLIDE_COUNT} frames)"
else
  log "slides exist: $SLIDE_DIR (${SLIDE_COUNT} frames)"
fi

log "study-pack pipeline complete"
