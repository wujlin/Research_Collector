"""为 Next.js 前端导出 JSON 快照。"""

from __future__ import annotations

from pathlib import Path

from src.storage.database import Database
from src.processors.importance_ranker import ImportanceRanker
from src.utils.helpers import dump_json


class WebSnapshotExporter:
    def __init__(self, output_dir: str = "web/public/generated"):
        self.output_dir = Path(output_dir)

    def export_all(self, database: Database) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        papers = database.list_papers()
        topics = database.list_topics()
        youtube_resources = database.list_youtube_resources()
        ranker = ImportanceRanker()
        topic_lookup = {topic.key: topic for topic in topics}

        def topic_depth(topic_key: str) -> int:
            depth = 0
            current = topic_lookup.get(topic_key)
            while current and current.parent_key:
                depth += 1
                current = topic_lookup.get(current.parent_key)
            return depth

        def topic_lineage(topic_key: str) -> list[str]:
            lineage: list[str] = []
            current = topic_lookup.get(topic_key)
            while current:
                lineage.append(current.display_name)
                if not current.parent_key:
                    break
                current = topic_lookup.get(current.parent_key)
            return list(reversed(lineage))

        paper_payload = []
        topic_counts: dict[str, int] = {}
        for paper in papers:
            topic_keys = [topic.key for topic in paper.topics]
            for topic_key in topic_keys:
                topic_counts[topic_key] = topic_counts.get(topic_key, 0) + 1
            payload = {
                "id": paper.id,
                "title": paper.title,
                "abstract": paper.abstract,
                "authors": [author.name for author in paper.authors],
                "year": paper.year,
                "publication_date": paper.publication_date.isoformat() if paper.publication_date else "",
                "journal": paper.journal,
                "venue": paper.venue,
                "doi": paper.doi,
                "arxiv_id": paper.arxiv_id,
                "url": paper.url,
                "pdf_url": paper.pdf_url,
                "citation_count": paper.citation_count,
                "influential_citation_count": paper.influential_citation_count,
                "relevance_score": paper.relevance_score,
                "tier": paper.tier,
                "status": paper.status,
                "is_seminal": paper.is_seminal,
                "source": paper.source,
                "topics": topic_keys,
                "markdown_path": paper.markdown_path,
            }
            importance_score, importance_bucket = ranker.score_paper(payload)
            payload["importance_score"] = importance_score
            payload["importance_bucket"] = importance_bucket
            payload["venue_quality"] = ranker.venue_quality_label(payload)
            paper_payload.append(payload)

        topic_payload = [
            {
                "key": topic.key,
                "display_name": topic.display_name,
                "parent_key": topic.parent_key,
                "description": topic.description,
                "paper_count": topic_counts.get(topic.key, 0),
                "depth": topic_depth(topic.key),
                "is_leaf": not any(candidate.parent_key == topic.key for candidate in topics),
                "lineage": topic_lineage(topic.key),
            }
            for topic in topics
        ]

        youtube_payload = []
        for resource in youtube_resources:
            payload = {
                "id": resource.id,
                "title": resource.title,
                "channel_name": resource.channel_name,
                "channel_id": resource.channel_id,
                "video_id": resource.video_id,
                "playlist_id": resource.playlist_id,
                "url": resource.url,
                "description": resource.description,
                "published_at": resource.published_at.isoformat() if resource.published_at else "",
                "duration": resource.duration,
                "view_count": resource.view_count,
                "topic_key": resource.topic_key,
                "resource_type": resource.resource_type,
            }
            importance_score, importance_bucket = ranker.score_youtube(payload)
            payload["importance_score"] = importance_score
            payload["importance_bucket"] = importance_bucket
            youtube_payload.append(payload)

        paper_payload.sort(
            key=lambda item: (
                float(item.get("importance_score", 0.0) or 0.0),
                float(item.get("relevance_score", 0.0) or 0.0),
                int(item.get("citation_count", 0) or 0),
            ),
            reverse=True,
        )
        youtube_payload.sort(
            key=lambda item: (
                float(item.get("importance_score", 0.0) or 0.0),
                int(item.get("view_count", 0) or 0),
                item.get("published_at", ""),
            ),
            reverse=True,
        )

        dump_json(self.output_dir / "papers.json", paper_payload)
        dump_json(self.output_dir / "topics.json", topic_payload)
        dump_json(self.output_dir / "youtube.json", youtube_payload)
        dump_json(self.output_dir / "stats.json", database.get_stats())
