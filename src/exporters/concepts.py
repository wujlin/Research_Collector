"""概念词条库导出：扫描精读笔记，索引关键概念的出现位置与上下文。"""

from __future__ import annotations

import re
from pathlib import Path

from src.utils.helpers import dump_json, extract_date_prefix, load_config

WORKFLOW_FILES = {"paper-queue.md", "study-guide.md", "collection-review.md", "weekly.md", "monthly.md"}


def _strip_frontmatter(content: str) -> str:
    """去掉 YAML frontmatter 区块。"""
    if not content.startswith("---"):
        return content
    end = content.find("---", 3)
    if end < 0:
        return content
    return content[end + 3:].lstrip()


def _extract_title(content: str) -> str:
    match = re.search(r'^title:\s*"(?P<t>[^"]+)"', content, re.MULTILINE)
    if match:
        return match.group("t")
    match = re.search(r"^#\s+(?P<t>.+)$", content, re.MULTILINE)
    return match.group("t").strip() if match else ""


def _find_alias_positions(content: str, aliases: list[str]) -> list[tuple[int, str]]:
    """返回所有 alias 在正文中的 (位置, 命中的 alias)。

    对全英文/全字母数字的短 alias（≤ 4 字符）强制加词边界 \b，避免
    "OT" 误匹配 "not" / "photon"；对中文或长短语直接子串匹配。
    """
    hits: list[tuple[int, str]] = []
    for alias in aliases:
        is_short_latin = len(alias) <= 4 and bool(re.match(r"^[A-Za-z0-9\-]+$", alias))
        if is_short_latin:
            pattern = re.compile(r"(?<![A-Za-z])" + re.escape(alias) + r"(?![A-Za-z])", re.IGNORECASE)
        else:
            pattern = re.compile(re.escape(alias), re.IGNORECASE)
        for m in pattern.finditer(content):
            hits.append((m.start(), alias))
    hits.sort(key=lambda x: x[0])
    seen: set[int] = set()
    dedup: list[tuple[int, str]] = []
    for pos, alias in hits:
        if not any(abs(pos - s) < 3 for s in seen):
            dedup.append((pos, alias))
            seen.add(pos)
    return dedup


def _snippet_around(content: str, pos: int, window: int = 180) -> str:
    """提取位置附近的上下文片段。"""
    start = max(0, pos - window)
    end = min(len(content), pos + window)
    snippet = content[start:end].strip()
    # 截断至最近的标点，让片段读起来更通顺
    if start > 0:
        # 从头切到第一个句号/换行后开始
        m = re.search(r"[。.\n！？!?]\s*", snippet[:window])
        if m:
            snippet = snippet[m.end():]
    snippet = re.sub(r"\s+", " ", snippet).strip()
    if len(snippet) > 300:
        snippet = snippet[:297] + "…"
    return snippet


class ConceptsExporter:
    """扫描 digests/*/reading_note 中的概念出现，输出到 concepts.json。"""

    def __init__(
        self,
        digest_dir: str = "digests",
        output_path: str = "web/public/generated/concepts.json",
        config_path: str = "concepts.yaml",
    ):
        self.digest_dir = Path(digest_dir)
        self.output_path = Path(output_path)
        self.concepts_config = load_config(config_path).get("concepts", [])

    def export(self) -> list[dict]:
        # 收集所有精读笔记
        notes: list[dict] = []
        for md_path in sorted(self.digest_dir.rglob("*.md")):
            # 跳过 workflow 文件和 shared 目录
            rel = md_path.relative_to(self.digest_dir)
            parts = rel.parts
            if parts and parts[0] == "shared":
                continue
            if len(parts) >= 2 and parts[1] == "workflow":
                continue
            if md_path.name in WORKFLOW_FILES:
                continue

            content = md_path.read_text(encoding="utf-8")
            body = _strip_frontmatter(content)
            title = _extract_title(content) or md_path.stem
            notes.append({
                "path": rel.as_posix(),
                "title": title,
                "date": extract_date_prefix(md_path),
                "body": body,
            })

        # 对每个概念，统计它在哪些笔记中出现、每篇里的上下文
        concept_entries = []
        for concept in self.concepts_config:
            aliases = concept.get("aliases", [])
            if not aliases:
                continue

            occurrences: list[dict] = []
            total_count = 0
            for note in notes:
                hits = _find_alias_positions(note["body"], aliases)
                if not hits:
                    continue
                snippets: list[str] = []
                for pos, alias in hits[:3]:  # 每篇最多取 3 个片段
                    snippets.append(_snippet_around(note["body"], pos))
                occurrences.append({
                    "note_path": note["path"],
                    "note_title": note["title"],
                    "note_date": note["date"],
                    "hit_count": len(hits),
                    "snippets": snippets,
                })
                total_count += len(hits)

            if occurrences:
                occurrences.sort(key=lambda o: o["hit_count"], reverse=True)
                concept_entries.append({
                    "id": concept["id"],
                    "display_name": concept.get("display_name", concept["id"]),
                    "category": concept.get("category", "general"),
                    "short_description": concept.get("short_description", ""),
                    "aliases": aliases,
                    "total_occurrences": total_count,
                    "note_count": len(occurrences),
                    "occurrences": occurrences,
                })

        # 按笔记覆盖数排序
        concept_entries.sort(key=lambda c: (c["note_count"], c["total_occurrences"]), reverse=True)
        dump_json(self.output_path, concept_entries)
        return concept_entries
