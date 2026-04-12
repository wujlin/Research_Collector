"""周报 / 月报导出。"""

from __future__ import annotations

import re
from pathlib import Path

from src.storage.database import Database
from src.utils.helpers import canonical_digest_path, dump_json, extract_date_prefix, utc_now


class DigestExporter:
    def __init__(
        self,
        digest_dir: str = "digests",
        json_path: str = "web/public/generated/digests.json",
    ):
        self.digest_dir = Path(digest_dir)
        self.json_path = Path(json_path)

    def export(
        self,
        database: Database,
        period: str = "weekly",
        days: int = 7,
        paper_limit: int = 30,
    ) -> Path:
        papers = database.get_recent_papers(days=days, limit=paper_limit)
        stats = database.get_stats()
        today = utc_now().date().isoformat()
        output_path = canonical_digest_path(self.digest_dir, today, period)

        topic_counts: dict[str, int] = {}
        for paper in papers:
            for topic in paper.topics:
                topic_counts[topic.key] = topic_counts.get(topic.key, 0) + 1

        lines = [
            "---",
            f'title: "{period.title()} Digest"',
            f'period: "{period}"',
            f'generated_at: "{utc_now().isoformat()}"',
            f"paper_count: {len(papers)}",
            "---",
            "",
            f"# {period.title()} Digest",
            "",
            f"- Total papers in library: {stats['total_papers']}",
            f"- Newly highlighted papers: {len(papers)}",
            "",
            "## Topic Momentum",
            "",
        ]
        for topic_key, count in sorted(topic_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
            lines.append(f"- {topic_key}: {count}")

        lines.extend(["", "## Top Papers", ""])
        for paper in papers:
            authors = ", ".join(author.name for author in paper.authors[:4]) if paper.authors else "Unknown"
            lines.extend(
                [
                    f"### {paper.title}",
                    "",
                    f"- Authors: {authors}",
                    f"- Venue: {paper.journal or paper.venue or 'preprint'}",
                    f"- Year: {paper.year or 'N/A'}",
                    f"- Relevance: {paper.relevance_score:.2f}",
                    f"- Citations: {paper.citation_count}",
                    f"- Topics: {', '.join(topic.key for topic in paper.topics) if paper.topics else 'uncategorized'}",
                    f"- Link: {paper.url or paper.pdf_url or 'N/A'}",
                    "",
                    paper.abstract[:500] + ("..." if len(paper.abstract) > 500 else ""),
                    "",
                ]
            )

        self.digest_dir.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(lines), encoding="utf-8")
        self._write_digest_index()
        return output_path

    def _write_digest_index(self) -> None:
        payload = []
        pattern = re.compile(r'^title:\s*"(?P<title>.+)"$')
        for digest_path in sorted(self.digest_dir.rglob("*.md"), reverse=True):
            title = digest_path.stem
            relative_path = digest_path.relative_to(self.digest_dir)
            created = extract_date_prefix(digest_path)
            if not created:
                created = "shared" if relative_path.parts and relative_path.parts[0] == "shared" else digest_path.name[:10]
            with digest_path.open("r", encoding="utf-8") as handle:
                lines = handle.read().splitlines()
            for line in lines[:10]:
                match = pattern.match(line)
                if match:
                    title = match.group("title")
                    break
            payload.append(
                {
                    "title": title,
                    "path": relative_path.as_posix(),
                    "created_at": created,
                }
            )
        dump_json(self.json_path, payload)
