from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "refine_youtube_transcript.py"
SPEC = importlib.util.spec_from_file_location("refine_youtube_transcript", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_clean_text_applies_domain_replacements():
    replacements = MODULE.build_replacements(
        {
            "global_replacements": [
                {"pattern": r"\bstochastic ceramics\b", "replacement": "stochastic thermodynamics"},
                {"pattern": r"\bTakahiro Saga\b", "replacement": "Takahiro Sagawa"},
            ]
        },
        video_id=None,
    )

    cleaned = MODULE.clean_text(
        "I am Takahiro Saga and I will talk about stochastic ceramics.",
        replacements,
    )

    assert "Takahiro Sagawa" in cleaned
    assert "stochastic thermodynamics" in cleaned


def test_merge_segments_combines_short_gaps():
    segments = [
        MODULE.TranscriptSegment(start=0.0, end=3.0, text="First sentence."),
        MODULE.TranscriptSegment(start=3.8, end=6.0, text="Second sentence."),
        MODULE.TranscriptSegment(start=10.0, end=13.0, text="Third sentence."),
    ]

    merged = MODULE.merge_segments(segments, max_gap_seconds=1.0, max_chars=100)

    assert len(merged) == 2
    assert merged[0].text == "First sentence. Second sentence."
