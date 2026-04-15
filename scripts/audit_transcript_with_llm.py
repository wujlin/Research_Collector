#!/usr/bin/env python3
"""Audit transcript paragraphs with an OpenAI-compatible LLM endpoint."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src.utils.helpers import normalize_whitespace
except ImportError:
    def normalize_whitespace(value: str) -> str:
        return re.sub(r"\s+", " ", value or "").strip()


DEFAULT_BASE_URL = "http://127.0.0.1:18082/v1"
DEFAULT_MODEL = "Qwen3-8B"
STYLE_REASON_PATTERNS = (
    "正式语境",
    "口语化",
    "更自然",
    "更流畅",
    "加逗号",
    "不够规范",
    "建议使用全称",
    "保留英文原词",
    "表达习惯",
)
SUBSTANTIVE_REASON_PATTERNS = (
    "成语",
    "固定表达",
    "古诗词",
    "人名",
    "机构名",
    "术语",
    "书名",
    "专有名词",
)


@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Use a local or remote LLM to audit transcript paragraphs for probable ASR errors.",
    )
    parser.add_argument("transcript_dir", help="Transcript artifact directory")
    parser.add_argument("--base-url", default=os.getenv("TRANSCRIPT_LLM_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--api-key", default=os.getenv("TRANSCRIPT_LLM_API_KEY", "local-qwen3"))
    parser.add_argument("--model", default=os.getenv("TRANSCRIPT_LLM_MODEL", DEFAULT_MODEL))
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--max-gap-seconds", type=float, default=1.5)
    parser.add_argument("--max-chars", type=int, default=260)
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--max-paragraphs", type=int, default=0, help="0 means all paragraphs")
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--max-completion-tokens", type=int, default=1200)
    parser.add_argument(
        "--enable-thinking",
        action="store_true",
        help="Allow the model to emit reasoning traces. Off by default for stable JSON output.",
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


def load_metadata(transcript_dir: Path) -> dict[str, Any]:
    return json.loads((transcript_dir / "metadata.json").read_text(encoding="utf-8"))


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


def batched(items: list[Any], size: int) -> list[list[Any]]:
    return [items[idx : idx + size] for idx in range(0, len(items), size)]


def extract_first_json_object(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    cleaned = re.sub(r"(?is)^<think>.*?</think>\s*", "", cleaned)
    cleaned = re.sub(r"(?is)^```json\s*", "", cleaned)
    cleaned = re.sub(r"(?is)^```\s*", "", cleaned)
    cleaned = re.sub(r"(?is)\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in model response")
    return json.loads(match.group(0))


def normalize_compare_text(text: str) -> str:
    return re.sub(r"[\s\W_]+", "", text, flags=re.UNICODE).lower()


def keep_model_flag(
    *,
    status: str,
    paragraph_text: str,
    suspicious_spans: list[str],
    corrected_text: str,
    issue_types: list[str],
    reason: str,
) -> bool:
    if status not in {"needs_review", "uncertain"}:
        return False
    if not corrected_text:
        return False

    normalized_corrected = normalize_compare_text(corrected_text)
    if not normalized_corrected:
        return False

    if normalized_corrected == normalize_compare_text(paragraph_text):
        return False
    if any(normalized_corrected == normalize_compare_text(span) for span in suspicious_spans if span):
        return False

    if any(pattern in reason for pattern in STYLE_REASON_PATTERNS):
        return False

    if "需确认" in reason and not any(pattern in reason for pattern in SUBSTANTIVE_REASON_PATTERNS):
        return False

    if len(corrected_text) > 24 and not any(pattern in reason for pattern in SUBSTANTIVE_REASON_PATTERNS):
        return False

    if any(issue in {"proper_noun", "technical_term"} for issue in issue_types):
        return True

    return any(pattern in reason for pattern in SUBSTANTIVE_REASON_PATTERNS)


def build_messages(batch: list[dict[str, Any]]) -> list[dict[str, str]]:
    system = """
你是一个中文长访谈 transcript 审校助手。你的任务不是润色文风，而是检查 ASR/转写中是否存在明显错误。

规则：
1. 默认判定为 ok。只有在你能指出具体错误位置，并给出更可信的修正时，才标为 needs_review。
2. 只关注高置信度问题：人名、机构名、术语名、书名、固定表达、成语、明显语义漂移、明显错词。
3. 不要为了更流畅而改写口语。
4. 如果只是口语重复、停顿、赘词、结巴、中英夹杂、网络用语，但意思没错，判定为 ok。
5. 如果看起来可能有错，但你没有足够把握，不要强行纠正，判定为 uncertain。
6. 如果需要修改，给出 corrected_text，但尽量只改必要的字词。
7. 如果 corrected_text 只是删除口头禅、停顿词、重复词，而没有修正内容性错误，应判定为 ok。
8. 必须返回 JSON，不要输出任何解释性前缀。
9. 不要输出 <think> 标签，不要输出推理草稿。

这些通常应判定为 ok：
- “ACM班”
- “死宅”
- “蛮蛮骄傲的”
- “我很喜欢podcast”
- “比较I人”

这种才值得标记：
- “为负心词强说愁” 更可能是 “为赋新词强说愁”
- 明显错掉的人名、机构名、术语名、书名
- 明显不通顺到破坏原意的片段

输出格式：
{
  "results": [
    {
      "id": 0,
      "status": "ok" | "needs_review" | "uncertain",
      "issue_types": ["proper_noun", "technical_term", "semantic_drift", "other"],
      "suspicious_spans": ["..."],
      "corrected_text": "...",
      "reason": "..."
    }
  ]
}
""".strip()

    lines = ["请审校以下 transcript 段落："]
    for item in batch:
        lines.append(
            json.dumps(
                {
                    "id": item["id"],
                    "time_range": item["time_range"],
                    "text": item["text"],
                },
                ensure_ascii=False,
            )
        )
    user = "\n".join(lines)
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def render_markdown(
    *,
    metadata: dict[str, Any],
    model_name: str,
    base_url: str,
    results: list[dict[str, Any]],
) -> str:
    review_items = [item for item in results if item["status"] != "ok"]
    counts: dict[str, int] = {"ok": 0, "needs_review": 0, "uncertain": 0, "error": 0}
    for item in results:
        counts[item["status"]] = counts.get(item["status"], 0) + 1

    lines = [
        f"# LLM Audit: {metadata['title']}",
        "",
        f"- Model: `{model_name}`",
        f"- Base URL: `{base_url}`",
        f"- Audited at: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Paragraphs: `{len(results)}`",
        f"- `ok / needs_review / uncertain / error = {counts.get('ok', 0)} / {counts.get('needs_review', 0)} / {counts.get('uncertain', 0)} / {counts.get('error', 0)}`",
        "",
        "## Flagged Paragraphs",
        "",
    ]

    if not review_items:
        lines.append("No flagged paragraphs.")
        return "\n".join(lines)

    for item in review_items:
        lines.extend(
            [
                f"### [{item['time_range']}] #{item['id']} `{item['status']}`",
                "",
                f"- Issue types: `{', '.join(item.get('issue_types', [])) or 'none'}`",
                f"- Suspicious spans: `{'; '.join(item.get('suspicious_spans', [])) or 'none'}`",
                "",
                "**Original**",
                "",
                item["text"],
                "",
                "**Suggested**",
                "",
                item.get("corrected_text") or "(no direct correction proposed)",
                "",
                "**Reason**",
                "",
                item.get("reason") or "(none)",
                "",
            ]
        )

    return "\n".join(lines)


def main() -> None:
    args = build_parser().parse_args()

    transcript_dir = Path(args.transcript_dir).resolve()
    metadata = load_metadata(transcript_dir)
    merged_segments = merge_segments(
        load_segments(transcript_dir),
        max_gap_seconds=args.max_gap_seconds,
        max_chars=args.max_chars,
    )

    paragraphs = [
        {
            "id": idx,
            "time_range": f"{format_timestamp(segment.start)} - {format_timestamp(segment.end)}",
            "start": segment.start,
            "end": segment.end,
            "text": normalize_whitespace(segment.text),
        }
        for idx, segment in enumerate(merged_segments)
    ]

    selected = paragraphs[args.start_index :]
    if args.max_paragraphs > 0:
        selected = selected[: args.max_paragraphs]

    client = OpenAI(base_url=args.base_url, api_key=args.api_key, timeout=args.timeout)

    results: list[dict[str, Any]] = []
    for batch in batched(selected, args.batch_size):
        extra_body = None
        if not args.enable_thinking:
            extra_body = {"chat_template_kwargs": {"enable_thinking": False}}
        response = client.chat.completions.create(
            model=args.model,
            temperature=0,
            max_completion_tokens=args.max_completion_tokens,
            response_format={"type": "json_object"},
            extra_body=extra_body,
            messages=build_messages(batch),
        )
        raw = response.choices[0].message.content or ""
        try:
            parsed = extract_first_json_object(raw)
            parsed_results = parsed.get("results", [])
            by_id = {item["id"]: item for item in parsed_results if isinstance(item, dict) and "id" in item}
            for paragraph in batch:
                model_item = by_id.get(paragraph["id"], {})
                status = str(model_item.get("status", "error")).strip().lower()
                if status not in {"ok", "needs_review", "uncertain"}:
                    status = "error"
                results.append(
                    {
                        **paragraph,
                        "issue_types": list(model_item.get("issue_types", [])) if isinstance(model_item.get("issue_types", []), list) else [],
                        "suspicious_spans": list(model_item.get("suspicious_spans", [])) if isinstance(model_item.get("suspicious_spans", []), list) else [],
                        "corrected_text": normalize_whitespace(str(model_item.get("corrected_text", ""))),
                        "reason": normalize_whitespace(str(model_item.get("reason", ""))),
                        "model_status": status,
                        "raw_response": raw,
                    }
                )
                current = results[-1]
                current["status"] = (
                    current["model_status"]
                    if keep_model_flag(
                        status=current["model_status"],
                        paragraph_text=current["text"],
                        suspicious_spans=current["suspicious_spans"],
                        corrected_text=current["corrected_text"],
                        issue_types=current["issue_types"],
                        reason=current["reason"],
                    )
                    else "ok"
                )
        except Exception as exc:
            for paragraph in batch:
                results.append(
                    {
                        **paragraph,
                        "status": "error",
                        "model_status": "error",
                        "issue_types": [],
                        "suspicious_spans": [],
                        "corrected_text": "",
                        "reason": f"Failed to parse model response: {exc}",
                        "raw_response": raw,
                    }
                )

    payload = {
        "title": metadata["title"],
        "url": metadata["url"],
        "model": args.model,
        "base_url": args.base_url,
        "audited_at": datetime.now().isoformat(timespec="seconds"),
        "paragraph_count": len(results),
        "start_index": args.start_index,
        "max_paragraphs": args.max_paragraphs,
        "batch_size": args.batch_size,
        "results": results,
    }

    (transcript_dir / "llm_audit.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (transcript_dir / "llm_audit.md").write_text(
        render_markdown(metadata=metadata, model_name=args.model, base_url=args.base_url, results=results),
        encoding="utf-8",
    )
    flagged = sum(1 for item in results if item["status"] in {"needs_review", "uncertain"})
    print(
        f"Audited {len(results)} paragraphs via {args.model} at {args.base_url}. "
        f"Flagged {flagged} paragraphs.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
