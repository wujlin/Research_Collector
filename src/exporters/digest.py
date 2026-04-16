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

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(lines), encoding="utf-8")
        self._write_digest_index()
        return output_path

    def _write_digest_index(self) -> None:
        payload = []
        title_re = re.compile(r'^title:\s*"(?P<title>.+)"$')
        authors_re = re.compile(r'^authors:\s*"(?P<authors>.+)"$')
        venue_re = re.compile(r'^venue:\s*"(?P<venue>.+)"$')
        topics_re = re.compile(r'^topics:\s*\[(?P<topics>.+)\]$')
        WORKFLOW_FILES = {"paper-queue.md", "study-guide.md", "collection-review.md", "weekly.md", "monthly.md"}

        for digest_path in sorted(self.digest_dir.rglob("*.md"), reverse=True):
            title = digest_path.stem
            relative_path = digest_path.relative_to(self.digest_dir)
            created = extract_date_prefix(digest_path)
            if not created:
                created = "shared" if relative_path.parts and relative_path.parts[0] == "shared" else digest_path.name[:10]

            # 分类：workflow / reading_note / shared
            parts = relative_path.parts
            if parts and parts[0] == "shared":
                entry_type = "shared"
            elif len(parts) >= 2 and parts[1] == "workflow":
                entry_type = "workflow"
            elif digest_path.name in WORKFLOW_FILES:
                entry_type = "workflow"
            else:
                entry_type = "reading_note"

            # 解析 frontmatter
            authors = ""
            venue = ""
            topics: list[str] = []
            with digest_path.open("r", encoding="utf-8") as handle:
                content = handle.read()
                lines = content.splitlines()
            in_fm = False
            for i, line in enumerate(lines[:30]):
                if line.strip() == "---":
                    in_fm = not in_fm
                    continue
                if not in_fm:
                    continue
                m = title_re.match(line)
                if m:
                    title = m.group("title")
                m = authors_re.match(line)
                if m:
                    authors = m.group("authors")
                m = venue_re.match(line)
                if m:
                    venue = m.group("venue")
                m = topics_re.match(line)
                if m:
                    topics = [t.strip().strip('"').strip("'") for t in m.group("topics").split(",")]

            # 正文字数粗略估计（用于阅读时间）
            word_count = len(content.split())

            payload.append(
                {
                    "title": title,
                    "path": relative_path.as_posix(),
                    "created_at": created,
                    "type": entry_type,
                    "authors": authors,
                    "venue": venue,
                    "topics": topics,
                    "word_count": word_count,
                }
            )
        dump_json(self.json_path, payload)
