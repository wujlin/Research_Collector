"""
Markdown 文件生成与管理。

将 Paper 对象转换为标准化 Markdown 文件，按主题分类存储到 library/ 目录。
使用 Jinja2 模板引擎渲染。
"""

from __future__ import annotations

from datetime import datetime
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
title: "{{ title }}"
authors: {{ authors_yaml }}
year: {{ year }}
journal: "{{ journal }}"
doi: "{{ doi }}"
arxiv: "{{ arxiv_id }}"
url: "{{ url }}"
pdf_url: "{{ pdf_url }}"
topics: {{ topics_yaml }}
tier: {{ tier }}
citations: {{ citation_count }}
relevance_score: {{ relevance_score }}
collected: "{{ collected }}"
status: "{{ status }}"
source: "{{ source }}"
{% if is_seminal %}is_seminal: true
{% endif %}---

## Abstract

{{ abstract }}

## Key Contributions

{{ contributions }}

## Connections

{{ connections }}

## Notes

{{ notes }}
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

        authors_list = [a.name for a in paper.authors] if paper.authors else []
        topics_list = [t.key for t in paper.topics] if paper.topics else []

        content = self.paper_tmpl.render(
            title=paper.title.replace('"', '\\"'),
            authors_yaml=self._to_yaml_list(authors_list),
            year=paper.year or "",
            journal=paper.journal or "",
            doi=paper.doi or "",
            arxiv_id=paper.arxiv_id or "",
            url=paper.url or "",
            pdf_url=paper.pdf_url or "",
            topics_yaml=self._to_yaml_list(topics_list),
            tier=paper.tier or 0,
            citation_count=paper.citation_count or 0,
            relevance_score=round(paper.relevance_score or 0, 2),
            collected=utc_now().strftime("%Y-%m-%d"),
            status=paper.status or "unread",
            source=paper.source or "",
            is_seminal=paper.is_seminal,
            abstract=paper.abstract or "(待填充)",
            contributions="(待补充)",
            connections=self._generate_connections(topics_list),
            notes="",
        )

        filepath.write_text(content, encoding="utf-8")
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
            paper_entries.append({
                "title": p.title,
                "filename": f"{slugify(p.title)}.md",
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
        master_index.write_text("".join(lines), encoding="utf-8")

    def prune_stale_topic_directories(self, taxonomy: dict[str, Any]) -> None:
        valid_topic_dirs = {entry["key"] for entry in flatten_topics(taxonomy)}
        protected_dirs = {"uncategorized"}

        for directory in sorted(self.library_dir.rglob("*"), reverse=True):
            if not directory.is_dir():
                continue
            relative = directory.relative_to(self.library_dir).as_posix()
            if relative in {".", ""}:
                continue
            if relative in valid_topic_dirs or relative in protected_dirs:
                continue
            shutil.rmtree(directory, ignore_errors=True)

    def _primary_topic(self, paper: Paper) -> str:
        """优先取最深的 topic 作为存储路径。"""
        if paper.topics:
            sorted_topics = sorted(paper.topics, key=lambda topic: topic.key.count("/"), reverse=True)
            return sorted_topics[0].key
        return "uncategorized"

    @staticmethod
    def _to_yaml_list(items: list) -> str:
        if not items:
            return "[]"
        return "[" + ", ".join(f'"{item}"' for item in items) + "]"

    @staticmethod
    def _generate_connections(topic_keys: list) -> str:
        if not topic_keys:
            return "(待添加)"
        lines = []
        for key in topic_keys:
            short = key.split("/")[-1] if "/" in key else key
            lines.append(f"- [[{short}]]")
        return "\n".join(lines)
