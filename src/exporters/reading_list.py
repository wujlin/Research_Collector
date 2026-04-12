"""阅读列表导出。"""

from __future__ import annotations

from pathlib import Path

from src.processors.importance_ranker import ImportanceRanker
from src.storage.database import Database
from src.utils.helpers import dump_json, utc_now


class ReadingListExporter:
    def __init__(
        self,
        output_path: str = "digests/shared/reading_list.md",
        json_path: str = "web/public/generated/reading_list.json",
    ):
        self.output_path = Path(output_path)
        self.json_path = Path(json_path)

    def export(self, database: Database, limit: int = 20) -> Path:
        ranker = ImportanceRanker()
        scored_papers = []
        for paper in database.list_papers():
            payload = {
                "title": paper.title,
                "abstract": paper.abstract,
                "topics": [topic.key for topic in paper.topics],
                "relevance_score": paper.relevance_score,
                "citation_count": paper.citation_count,
                "influential_citation_count": paper.influential_citation_count,
                "is_seminal": paper.is_seminal,
                "source": paper.source,
                "tier": paper.tier,
                "journal": paper.journal,
                "venue": paper.venue,
            }
            importance_score, importance_bucket = ranker.score_paper(payload)
            venue_quality = ranker.venue_quality_label(payload)
            scored_papers.append((paper, importance_score, importance_bucket, venue_quality))

        scored_papers.sort(
            key=lambda item: (
                item[1],
                float(item[0].relevance_score or 0.0),
                int(item[0].citation_count or 0),
            ),
            reverse=True,
        )
        papers = scored_papers[:limit]
        markdown_lines = [
            "---",
            f'title: "Reading List"',
            f'generated_at: "{utc_now().isoformat()}"',
            f"paper_count: {len(papers)}",
            "---",
            "",
            "# Reading List",
            "",
            "按 importance score 排序的当前优先阅读清单。",
            "",
        ]

        payload = []
        for index, (paper, importance_score, importance_bucket, venue_quality) in enumerate(papers, start=1):
            authors = ", ".join(author.name for author in paper.authors[:4]) if paper.authors else "Unknown"
            topics = [topic.key for topic in paper.topics]
            markdown_lines.extend(
                [
                    f"## {index}. {paper.title}",
                    "",
                    f"- Authors: {authors}",
                    f"- Year: {paper.year or 'N/A'}",
                    f"- Journal/Venue: {paper.journal or paper.venue or 'preprint'}",
                    f"- Venue Quality: {venue_quality}",
                    f"- Importance: {importance_score:.2f} ({importance_bucket})",
                    f"- Relevance: {paper.relevance_score:.2f}",
                    f"- Citations: {paper.citation_count}",
                    f"- Topics: {', '.join(topics) if topics else 'uncategorized'}",
                    f"- URL: {paper.url or paper.pdf_url or 'N/A'}",
                    "",
                ]
            )
            payload.append(
                {
                    "id": paper.id,
                    "title": paper.title,
                    "authors": [author.name for author in paper.authors],
                    "year": paper.year,
                    "journal": paper.journal,
                    "venue": paper.venue,
                    "importance_score": importance_score,
                    "importance_bucket": importance_bucket,
                    "venue_quality": venue_quality,
                    "relevance_score": paper.relevance_score,
                    "citation_count": paper.citation_count,
                    "topics": topics,
                    "url": paper.url,
                    "pdf_url": paper.pdf_url,
                }
            )

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text("\n".join(markdown_lines), encoding="utf-8")
        dump_json(self.json_path, payload)
        return self.output_path
