from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "transcribe_youtube.py"
SPEC = importlib.util.spec_from_file_location("transcribe_youtube", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_format_timestamp_handles_minutes_and_hours():
    assert MODULE.format_timestamp(65) == "01:05"
    assert MODULE.format_timestamp(3661) == "01:01:01"


def test_render_transcript_markdown_includes_metadata_and_segments():
    segments = [
        MODULE.TranscriptSegment(start=0.0, end=12.4, text="First point."),
        MODULE.TranscriptSegment(start=12.4, end=25.0, text="Second point."),
    ]

    markdown = MODULE.render_transcript_markdown(
        title="Test Talk",
        url="https://youtube.com/watch?v=test",
        model="large-v3",
        language="en",
        detected_language="en",
        segments=segments,
    )

    assert "# Test Talk" in markdown
    assert "- URL: https://youtube.com/watch?v=test" in markdown
    assert "### [00:00 - 00:12]" in markdown
    assert "Second point." in markdown
