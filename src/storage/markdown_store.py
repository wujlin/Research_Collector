"""
Markdown 文件生成与管理。

将 Paper 对象转换为标准化 Markdown 文件，按主题分类存储到 library/ 目录。
使用 Jinja2 模板引擎渲染。
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
import shutil
from typing import Any

import yaml
from jinja2 import BaseLoader, Environment

from src.utils.helpers import build_topic_index, flatten_topics, slugify, utc_now

from .models import Paper

# ── Markdown 模板 ──

PAPER_TEMPLATE = """\
---
title: {{ title_yaml }}
authors: {{ authors_yaml }}
year: {{ year_yaml }}
journal: {{ journal_yaml }}
doi: {{ doi_yaml }}
arxiv: {{ arxiv_id_yaml }}
url: {{ url_yaml }}
pdf_url: {{ pdf_url_yaml }}
topics: {{ topics_yaml }}
tier: {{ tier }}
citations: {{ citation_count }}
relevance_score: {{ relevance_score }}
collected: {{ collected_yaml }}
status: {{ status_yaml }}
source: {{ source_yaml }}
{% if is_seminal %}is_seminal: true
{% endif %}{{ extra_frontmatter }}---

## Abstract

{{ abstract }}

## Key Contributions

{{ contributions }}

## Connections

{{ connections }}

## Notes

{{ notes }}
{{ extra_sections }}
"""

INDEX_TEMPLATE = """\
---
title: "{{ title }}"
description: "{{ description }}"
paper_count: {{ paper_count }}
last_updated: "{{ last_updated }}"
---

# {{ title }}

{{ description }}

## Papers ({{ paper_count }})

{% for paper in papers %}
- [{{ paper.title }}]({{ paper.filename }}) ({{ paper.year }}, {{ paper.journal }}, {{ paper.citation_count }} citations)
{% endfor %}
"""


class MarkdownStore:
    def __init__(self, library_dir: str = "library"):
        self.library_dir = Path(library_dir)
        self.env = Environment(loader=BaseLoader())
        self.paper_tmpl = self.env.from_string(PAPER_TEMPLATE)
        self.index_tmpl = self.env.from_string(INDEX_TEMPLATE)

    def ensure_directory_structure(self, topics_yaml_path: str = "config/topics.yaml") -> None:
        """根据 topics.yaml 创建完整的 library 目录结构。"""
        with open(topics_yaml_path, "r", encoding="utf-8") as handle:
            taxonomy = yaml.safe_load(handle)

        self.library_dir.mkdir(parents=True, exist_ok=True)

        for entry in flatten_topics(taxonomy):
            topic_dir = self.library_dir / entry["key"]
            topic_dir.mkdir(parents=True, exist_ok=True)
            index_path = topic_dir / "_index.md"
            if not index_path.exists():
                self.write_topic_index(
                    topic_key=entry["key"],
                    display_name=entry["display_name"],
                    description=entry.get("description", ""),
                    papers=[],
                )

        self.write_master_index(taxonomy)
        self.prune_stale_topic_directories(taxonomy)

    def save_paper(self, paper: Paper) -> str:
        """将 Paper 渲染为 Markdown 并保存，返回相对路径。"""
        topic_key = self._primary_topic(paper)
        target_dir = self.library_dir / topic_key
        target_dir.mkdir(parents=True, exist_ok=True)

        filename = slugify(paper.title) + ".md"
        filepath = target_dir / filename

        previous_path = None
        if paper.markdown_path:
            candidate = self.library_dir / paper.markdown_path
            if candidate.exists():
                previous_path = candidate
        existing_path = previous_path or (filepath if filepath.exists() else None)
        existing_frontmatter, existing_sections = self._read_existing_paper(existing_path)

        authors_list = [a.name for a in paper.authors] if paper.authors else []
        topics_list = [t.key for t in paper.topics] if paper.topics else []

        machine_fields = {
            "title", "authors", "year", "journal", "doi", "arxiv", "url", "pdf_url",
            "topics", "tier", "citations", "relevance_score", "collected", "status",
            "source", "is_seminal",
        }
        extra_frontmatter = "".join(
            f"{key}: {json.dumps(value, ensure_ascii=False)}\n"
            for key, value in existing_frontmatter.items()
            if key not in machine_fields
        )

        contributions = existing_sections.pop("Key Contributions", "").strip() or "(待补充)"
        existing_connections = existing_sections.pop("Connections", "").strip()
        if self._is_generated_connections(existing_connections):
            connections = self._generate_connections(topics_list)
        else:
            connections = existing_connections
        notes = existing_sections.pop("Notes", "").strip() or (paper.notes or "")
        existing_sections.pop("Abstract", None)
        extra_sections = "".join(
            f"\n## {heading}\n\n{body.strip()}\n"
            for heading, body in existing_sections.items()
            if body.strip()
        )

        collected_at = paper.collected_at
        collected = collected_at.date().isoformat() if collected_at else utc_now().date().isoformat()

        content = self.paper_tmpl.render(
            title_yaml=self._to_yaml_scalar(paper.title),
            authors_yaml=self._to_yaml_list(authors_list),
            year_yaml=self._to_yaml_scalar(paper.year or ""),
            journal_yaml=self._to_yaml_scalar(paper.journal or ""),
            doi_yaml=self._to_yaml_scalar(paper.doi or ""),
            arxiv_id_yaml=self._to_yaml_scalar(paper.arxiv_id or ""),
            url_yaml=self._to_yaml_scalar(paper.url or ""),
            pdf_url_yaml=self._to_yaml_scalar(paper.pdf_url or ""),
            topics_yaml=self._to_yaml_list(topics_list),
            tier=paper.tier or 0,
            citation_count=paper.citation_count or 0,
            relevance_score=round(paper.relevance_score or 0, 2),
            collected_yaml=self._to_yaml_scalar(collected),
            status_yaml=self._to_yaml_scalar(paper.status or "unread"),
            source_yaml=self._to_yaml_scalar(paper.source or ""),
            is_seminal=paper.is_seminal,
            extra_frontmatter=extra_frontmatter,
            abstract=paper.abstract or "(待填充)",
            contributions=contributions,
            connections=connections,
            notes=notes,
            extra_sections=extra_sections,
        ).rstrip() + "\n"

        filepath.write_text(content, encoding="utf-8")
        if previous_path and previous_path != filepath and previous_path.exists():
            previous_path.unlink()
        return str(filepath.relative_to(self.library_dir))

    def write_topic_index(
        self,
        topic_key: str,
        display_name: str,
        description: str,
        papers: list[Paper],
    ) -> None:
        """更新某主题 index。"""
        parts = topic_key.split("/")
        index_path = self.library_dir / "/".join(parts) / "_index.md"
        index_path.parent.mkdir(parents=True, exist_ok=True)

        paper_entries = []
        for p in papers:
            if p.markdown_path:
                paper_path = self.library_dir / p.markdown_path
            else:
                paper_path = self.library_dir / self._primary_topic(p) / f"{slugify(p.title)}.md"
            paper_entries.append({
                "title": p.title,
                "filename": Path(os.path.relpath(paper_path, index_path.parent)).as_posix(),
                "year": p.year,
                "journal": p.journal or "preprint",
                "citation_count": p.citation_count,
            })

        content = self.index_tmpl.render(
            title=display_name,
            description=description,
            paper_count=len(papers),
            last_updated=utc_now().strftime("%Y-%m-%d"),
            papers=paper_entries,
        )
        index_path.write_text(content, encoding="utf-8")

    def write_master_index(self, taxonomy: dict[str, Any]) -> None:
        master_index = self.library_dir / "index.md"
        lines = ["# Research Library\n\n前沿文献库总索引\n"]
        topic_index = build_topic_index(taxonomy)

        def render_node(topic_key: str, depth: int = 0) -> None:
            entry = topic_index[topic_key]
            path = f"{topic_key}/_index.md"
            if depth == 0:
                lines.append(f"\n## [{entry['display_name']}]({path})\n")
                if entry.get("description"):
                    lines.append(f"{entry['description']}\n")
            else:
                indent = "  " * (depth - 1)
                lines.append(f"{indent}- [{entry['display_name']}]({path})\n")

            children = [item["key"] for item in topic_index.values() if item.get("parent_key") == topic_key]
            for child_key in sorted(children):
                render_node(child_key, depth + 1)

        for root_key in [entry["key"] for entry in flatten_topics(taxonomy) if not entry.get("parent_key")]:
            render_node(root_key)

        uncategorized_index = self.library_dir / "uncategorized" / "_index.md"
        if uncategorized_index.exists():
            lines.append("\n## [Uncategorized](uncategorized/_index.md)\n")

        archive_readme = self.library_dir / "archive" / "README.md"
        if archive_readme.exists():
            lines.append("\n## [Archive](archive/README.md)\n")
        master_index.write_text("".join(lines), encoding="utf-8")

    def prune_stale_topic_directories(self, taxonomy: dict[str, Any]) -> None:
        valid_topic_dirs = {entry["key"] for entry in flatten_topics(taxonomy)}
        protected_dirs = {"uncategorized", "archive"}

        for directory in sorted(self.library_dir.rglob("*"), reverse=True):
            if not directory.is_dir():
                continue
            relative = directory.relative_to(self.library_dir).as_posix()
            if relative in {".", ""}:
                continue
            if relative in valid_topic_dirs or any(
                relative == protected or relative.startswith(f"{protected}/")
                for protected in protected_dirs
            ):
                continue
            shutil.rmtree(directory, ignore_errors=True)

    def _primary_topic(self, paper: Paper) -> str:
        """优先取最深的 topic 作为存储路径。"""
        if paper.topics:
            max_depth = max(topic.key.count("/") for topic in paper.topics)
            deepest_topics = [topic for topic in paper.topics if topic.key.count("/") == max_depth]
            if paper.markdown_path:
                for topic in deepest_topics:
                    if paper.markdown_path.startswith(f"{topic.key}/"):
                        return topic.key
            return sorted(topic.key for topic in deepest_topics)[0]
        return "uncategorized"

    @staticmethod
    def _to_yaml_list(items: list) -> str:
        return json.dumps(items, ensure_ascii=False)

    @staticmethod
    def _to_yaml_scalar(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False)

    @staticmethod
    def _read_existing_paper(path: Path | None) -> tuple[dict[str, Any], dict[str, str]]:
        if path is None or not path.exists():
            return {}, {}

        content = path.read_text(encoding="utf-8")
        frontmatter: dict[str, Any] = {}
        body = content
        if content.startswith("---\n"):
            end = content.find("\n---\n", 4)
            if end >= 0:
                raw_frontmatter = content[4:end]
                parsed = yaml.safe_load(raw_frontmatter) or {}
                if isinstance(parsed, dict):
                    frontmatter = parsed
                body = content[end + 5:]

        sections: dict[str, str] = {}
        matches = list(re.finditer(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE))
        for index, match in enumerate(matches):
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
            sections[match.group(1).strip()] = body[start:end].strip()
        return frontmatter, sections

    @staticmethod
    def _is_generated_connections(content: str) -> bool:
        if not content or content == "(待添加)":
            return True
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        return bool(lines) and all(re.fullmatch(r"- \[\[[^]]+]]", line) for line in lines)

    @staticmethod
    def _generate_connections(topic_keys: list) -> str:
        if not topic_keys:
            return "(待添加)"
        lines = []
        for key in topic_keys:
            short = key.split("/")[-1] if "/" in key else key
            lines.append(f"- [[{short}]]")
        return "\n".join(lines)
