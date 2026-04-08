"""知识图谱数据导出。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.storage.database import Database
from src.utils.helpers import dump_json, flatten_topics, load_config


class KnowledgeGraphExporter:
    def __init__(self, output_path: str = "web/public/generated/graph.json"):
        self.output_path = Path(output_path)

    def export(self, database: Database, max_papers: int = 40) -> dict[str, Any]:
        taxonomy = load_config("topics.yaml")
        topic_entries = flatten_topics(taxonomy)
        papers = database.list_papers(limit=max_papers)

        nodes: list[dict[str, Any]] = []
        edges: list[dict[str, Any]] = []

        for entry in topic_entries:
            nodes.append(
                {
                    "id": entry["key"],
                    "label": entry["display_name"],
                    "type": "topic",
                    "parent_key": entry["parent_key"],
                    "depth": entry.get("depth", 0),
                    "is_leaf": entry.get("is_leaf", False),
                }
            )
            if entry["parent_key"]:
                edges.append(
                    {
                        "source": entry["parent_key"],
                        "target": entry["key"],
                        "type": "taxonomy",
                    }
                )

        for paper in papers:
            paper_id = f"paper:{paper.id}"
            nodes.append(
                {
                    "id": paper_id,
                    "label": paper.title,
                    "type": "paper",
                    "relevance_score": paper.relevance_score,
                    "citation_count": paper.citation_count,
                }
            )
            for topic in paper.topics[:3]:
                edges.append({"source": paper_id, "target": topic.key, "type": "belongs_to"})

        payload = {"nodes": nodes, "edges": edges}
        dump_json(self.output_path, payload)
        return payload
