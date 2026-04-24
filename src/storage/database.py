"""SQLite 数据库管理：初始化、会话管理、CRUD 操作。"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy import create_engine, func, or_, select
from sqlalchemy.orm import Session, sessionmaker

from src.utils.helpers import flatten_topics, normalize_title, normalize_whitespace, parse_date, utc_now

from .models import Author, Base, CollectionLog, Paper, Topic, Venue, YouTubeResource, author_coauthors


@dataclass(frozen=True)
class UpsertResult:
    record: Any
    created: bool = False
    updated: bool = False

    @property
    def unchanged(self) -> bool:
        return not self.created and not self.updated


class Database:
    def __init__(self, db_path: str = "data/papers.db"):
        db_dir = Path(db_path).parent
        db_dir.mkdir(parents=True, exist_ok=True)

        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        Base.metadata.create_all(self.engine)
        self._session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)

    @contextmanager
    def session(self):
        session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    # ── Topic 管理 ──

    def init_topics_from_yaml(self, yaml_path: str = "config/topics.yaml") -> None:
        """从 topics.yaml 初始化/更新 Topic 表。"""
        with open(yaml_path, "r", encoding="utf-8") as handle:
            taxonomy = yaml.safe_load(handle)

        with self.session() as session:
            for entry in flatten_topics(taxonomy):
                self._upsert_topic(
                    session,
                    key=entry["key"],
                    display_name=entry["display_name"],
                    description=entry.get("description", ""),
                    parent_key=entry.get("parent_key"),
                )

    def _upsert_topic(
        self,
        session: Session,
        key: str,
        display_name: str,
        description: str = "",
        parent_key: str | None = None,
    ) -> Topic:
        topic = session.execute(select(Topic).where(Topic.key == key)).scalar_one_or_none()
        if topic is None:
            topic = Topic(
                key=key,
                display_name=display_name,
                description=description,
                parent_key=parent_key,
            )
            session.add(topic)
        else:
            topic.display_name = display_name
            topic.description = description
            topic.parent_key = parent_key
        return topic

    # ── Paper CRUD ──

    def add_paper(self, paper_data: dict[str, Any]) -> Paper:
        return self.upsert_paper(paper_data).record

    def upsert_paper(self, paper_data: dict[str, Any]) -> UpsertResult:
        """
        添加论文。如果 DOI 或 arXiv ID 已存在则跳过。
        paper_data 应包含: title, abstract, year, journal, doi, arxiv_id,
                           authors (list[str | dict]), topic_keys (list[str]), ...
        """
        normalized_data = self._normalize_paper_identifiers(paper_data)
        with self.session() as session:
            existing = self._find_existing_paper(session, normalized_data)
            if existing:
                return self._merge_existing_paper(session, existing, normalized_data)

            paper = Paper(
                title=normalized_data.get("title", ""),
                abstract=normalized_data.get("abstract", ""),
                year=normalized_data.get("year"),
                publication_date=parse_date(normalized_data.get("publication_date")),
                journal=normalized_data.get("journal", ""),
                venue=normalized_data.get("venue", ""),
                doi=normalized_data.get("doi"),
                arxiv_id=normalized_data.get("arxiv_id"),
                semantic_scholar_id=normalized_data.get("semantic_scholar_id"),
                openalex_id=normalized_data.get("openalex_id"),
                url=normalized_data.get("url", ""),
                pdf_url=normalized_data.get("pdf_url", ""),
                citation_count=normalized_data.get("citation_count", 0),
                influential_citation_count=normalized_data.get("influential_citation_count", 0),
                relevance_score=normalized_data.get("relevance_score", 0.0),
                tier=normalized_data.get("tier", 0),
                source=normalized_data.get("source", ""),
                is_seminal=normalized_data.get("is_seminal", False),
                notes=normalized_data.get("notes", ""),
            )
            session.add(paper)
            session.flush()
            self._attach_authors(session, paper, normalized_data.get("authors", []))
            self._attach_topics(session, paper, normalized_data.get("topic_keys", []))
            self._attach_venue(session, paper)
            self._update_coauthors(session, paper, previous_author_ids=set())
            return UpsertResult(record=paper, created=True)

    def _find_existing_paper(self, session: Session, data: dict[str, Any]) -> Paper | None:
        if data.get("doi"):
            existing = session.execute(select(Paper).where(Paper.doi == data["doi"])).scalar_one_or_none()
            if existing:
                return existing
        if data.get("arxiv_id"):
            existing = session.execute(
                select(Paper).where(Paper.arxiv_id == data["arxiv_id"])
            ).scalar_one_or_none()
            if existing:
                return existing
        title = normalize_title(data.get("title", ""))
        if title:
            for candidate in session.execute(
                select(Paper).where(func.lower(Paper.title) == data.get("title", "").lower())
            ).scalars():
                if normalize_title(candidate.title) == title:
                    return candidate
        return None

    @staticmethod
    def _normalize_paper_identifiers(data: dict[str, Any]) -> dict[str, Any]:
        normalized = dict(data)
        for key in ["doi", "arxiv_id", "semantic_scholar_id", "openalex_id"]:
            value = normalized.get(key)
            if isinstance(value, str):
                value = value.strip()
            normalized[key] = value or None
        return normalized

    def _merge_existing_paper(
        self,
        session: Session,
        paper: Paper,
        data: dict[str, Any],
    ) -> UpsertResult:
        changed = False

        merged_abstract = self._pick_longer_text(paper.abstract, data.get("abstract", ""))
        if merged_abstract != (paper.abstract or ""):
            paper.abstract = merged_abstract
            changed = True

        merged_year = paper.year or data.get("year")
        if merged_year != paper.year:
            paper.year = merged_year
            changed = True

        merged_publication_date = paper.publication_date or parse_date(data.get("publication_date"))
        if merged_publication_date != paper.publication_date:
            paper.publication_date = merged_publication_date
            changed = True

        merged_journal = paper.journal or data.get("journal", "")
        if merged_journal != (paper.journal or ""):
            paper.journal = merged_journal
            changed = True

        merged_venue = paper.venue or data.get("venue", "")
        if merged_venue != (paper.venue or ""):
            paper.venue = merged_venue
            changed = True

        merged_url = paper.url or data.get("url", "")
        if merged_url != (paper.url or ""):
            paper.url = merged_url
            changed = True

        merged_pdf_url = paper.pdf_url or data.get("pdf_url", "")
        if merged_pdf_url != (paper.pdf_url or ""):
            paper.pdf_url = merged_pdf_url
            changed = True

        merged_doi = paper.doi or data.get("doi")
        if merged_doi != paper.doi:
            paper.doi = merged_doi
            changed = True

        merged_arxiv_id = paper.arxiv_id or data.get("arxiv_id")
        if merged_arxiv_id != paper.arxiv_id:
            paper.arxiv_id = merged_arxiv_id
            changed = True

        merged_semantic_scholar_id = paper.semantic_scholar_id or data.get("semantic_scholar_id")
        if merged_semantic_scholar_id != paper.semantic_scholar_id:
            paper.semantic_scholar_id = merged_semantic_scholar_id
            changed = True

        merged_openalex_id = paper.openalex_id or data.get("openalex_id")
        if merged_openalex_id != paper.openalex_id:
            paper.openalex_id = merged_openalex_id
            changed = True

        merged_citation_count = max(paper.citation_count or 0, data.get("citation_count", 0) or 0)
        if merged_citation_count != (paper.citation_count or 0):
            paper.citation_count = merged_citation_count
            changed = True

        merged_influential_citation_count = max(
            paper.influential_citation_count or 0,
            data.get("influential_citation_count", 0) or 0,
        )
        if merged_influential_citation_count != (paper.influential_citation_count or 0):
            paper.influential_citation_count = merged_influential_citation_count
            changed = True

        merged_relevance_score = max(paper.relevance_score or 0.0, data.get("relevance_score", 0.0) or 0.0)
        if merged_relevance_score != (paper.relevance_score or 0.0):
            paper.relevance_score = merged_relevance_score
            changed = True

        merged_tier = self._pick_better_tier(paper.tier, data.get("tier", 0))
        if merged_tier != (paper.tier or 0):
            paper.tier = merged_tier
            changed = True

        merged_is_seminal = paper.is_seminal or bool(data.get("is_seminal"))
        if merged_is_seminal != bool(paper.is_seminal):
            paper.is_seminal = merged_is_seminal
            changed = True

        merged_source = self._merge_sources(paper.source, data.get("source", ""))
        if merged_source != (paper.source or ""):
            paper.source = merged_source
            changed = True

        if data.get("notes"):
            merged_notes = self._pick_longer_text(paper.notes, data["notes"])
            if merged_notes != (paper.notes or ""):
                paper.notes = merged_notes
                changed = True

        previous_author_ids = {author.id for author in paper.authors}
        self._attach_authors(session, paper, data.get("authors", []))
        if {author.id for author in paper.authors} != previous_author_ids:
            changed = True

        previous_topic_keys = {topic.key for topic in paper.topics}
        self._attach_topics(session, paper, data.get("topic_keys", []))
        if {topic.key for topic in paper.topics} != previous_topic_keys:
            changed = True

        previous_venue_id = paper.venue_id
        self._attach_venue(session, paper)
        if paper.venue_id != previous_venue_id:
            changed = True

        self._update_coauthors(session, paper, previous_author_ids=previous_author_ids)
        if changed:
            paper.updated_at = utc_now()
        return UpsertResult(record=paper, updated=changed)

    @staticmethod
    def _merge_sources(current: str, incoming: str) -> str:
        sources = {item for item in [current, incoming] if item}
        return ",".join(sorted(sources))

    @staticmethod
    def _pick_longer_text(current: str | None, incoming: str | None) -> str:
        current = current or ""
        incoming = incoming or ""
        return incoming if len(incoming) > len(current) else current

    @staticmethod
    def _pick_better_tier(current: int | None, incoming: int | None) -> int:
        current_value = int(current or 0)
        incoming_value = int(incoming or 0)
        if current_value == 0:
            return incoming_value
        if incoming_value == 0:
            return current_value
        return min(current_value, incoming_value)

    @staticmethod
    def _normalize_author_payload(author_data: Any) -> dict[str, str]:
        if isinstance(author_data, str):
            return {"name": author_data.strip(), "affiliation": "", "openalex_id": "", "semantic_scholar_id": ""}
        if isinstance(author_data, dict):
            return {
                "name": normalize_whitespace(str(author_data.get("name", ""))),
                "affiliation": normalize_whitespace(str(author_data.get("affiliation", ""))),
                "openalex_id": normalize_whitespace(str(author_data.get("openalex_id", ""))),
                "semantic_scholar_id": normalize_whitespace(str(author_data.get("semantic_scholar_id", ""))),
            }
        return {"name": "", "affiliation": "", "openalex_id": "", "semantic_scholar_id": ""}

    def _get_or_create_author(self, session: Session, author_data: Any) -> Author | None:
        payload = self._normalize_author_payload(author_data)
        name = payload["name"]
        affiliation = payload["affiliation"]
        openalex_id = payload["openalex_id"] or None
        semantic_scholar_id = payload["semantic_scholar_id"] or None
        if not name:
            return None

        candidates = session.execute(select(Author).where(Author.name == name)).scalars().all()

        if affiliation:
            normalized_affiliation = affiliation.lower()
            for candidate in candidates:
                if normalize_whitespace(candidate.affiliation).lower() == normalized_affiliation:
                    candidate.openalex_id = candidate.openalex_id or openalex_id
                    candidate.semantic_scholar_id = candidate.semantic_scholar_id or semantic_scholar_id
                    return candidate

        for candidate in candidates:
            if openalex_id and candidate.openalex_id == openalex_id:
                candidate.affiliation = candidate.affiliation or affiliation
                candidate.semantic_scholar_id = candidate.semantic_scholar_id or semantic_scholar_id
                return candidate
            if semantic_scholar_id and candidate.semantic_scholar_id == semantic_scholar_id:
                candidate.affiliation = candidate.affiliation or affiliation
                candidate.openalex_id = candidate.openalex_id or openalex_id
                return candidate

        for candidate in candidates:
            if not candidate.affiliation:
                candidate.affiliation = affiliation
                candidate.openalex_id = candidate.openalex_id or openalex_id
                candidate.semantic_scholar_id = candidate.semantic_scholar_id or semantic_scholar_id
                return candidate

        author = Author(
            name=name,
            affiliation=affiliation,
            openalex_id=openalex_id,
            semantic_scholar_id=semantic_scholar_id,
        )
        session.add(author)
        session.flush()
        return author

    # ── 查询 ──

    def _attach_authors(self, session: Session, paper: Paper, author_names: list[Any]) -> None:
        existing = {author.name: author for author in paper.authors}
        for author_name in author_names:
            payload = self._normalize_author_payload(author_name)
            if not payload["name"]:
                continue
            if payload["name"] in existing:
                author = existing[payload["name"]]
                if payload["affiliation"] and not author.affiliation:
                    author.affiliation = payload["affiliation"]
                if payload["openalex_id"] and not author.openalex_id:
                    author.openalex_id = payload["openalex_id"]
                if payload["semantic_scholar_id"] and not author.semantic_scholar_id:
                    author.semantic_scholar_id = payload["semantic_scholar_id"]
                continue
            author = self._get_or_create_author(session, payload)
            if author is None:
                continue
            paper.authors.append(author)
            existing[payload["name"]] = author

    def _attach_topics(self, session: Session, paper: Paper, topic_keys: list[str]) -> None:
        existing = {topic.key for topic in paper.topics}
        for topic_key in topic_keys:
            if not topic_key or topic_key in existing:
                continue
            topic = session.execute(select(Topic).where(Topic.key == topic_key)).scalar_one_or_none()
            if topic:
                paper.topics.append(topic)
                existing.add(topic_key)

    @staticmethod
    def _attach_venue(session: Session, paper: Paper) -> None:
        """将 paper.journal / paper.venue 匹配到 venues 表，写入 venue_id。"""
        if paper.venue_id:
            return
        for candidate_name in [paper.journal, paper.venue]:
            if not candidate_name:
                continue
            venue = session.execute(
                select(Venue).where(func.lower(Venue.name) == candidate_name.lower())
            ).scalar_one_or_none()
            if venue:
                paper.venue_id = venue.id
                venue.paper_count = (venue.paper_count or 0) + 1
                return

    @staticmethod
    def _update_coauthors(session: Session, paper: Paper, previous_author_ids: set[int]) -> None:
        """从论文的作者列表增量更新 author_coauthors 表。"""
        author_ids = sorted({a.id for a in paper.authors})
        if len(author_ids) < 2:
            return
        from itertools import combinations
        new_author_ids = set(author_ids) - previous_author_ids
        if not new_author_ids:
            return

        for a_id, b_id in combinations(author_ids, 2):
            if a_id not in new_author_ids and b_id not in new_author_ids:
                continue
            existing = session.execute(
                select(author_coauthors).where(
                    author_coauthors.c.author_a_id == a_id,
                    author_coauthors.c.author_b_id == b_id,
                )
            ).first()
            if existing:
                session.execute(
                    author_coauthors.update()
                    .where(
                        author_coauthors.c.author_a_id == a_id,
                        author_coauthors.c.author_b_id == b_id,
                    )
                    .values(shared_papers=existing.shared_papers + 1)
                )
            else:
                session.execute(
                    author_coauthors.insert().values(
                        author_a_id=a_id, author_b_id=b_id, shared_papers=1
                    )
                )

    def replace_paper_topics(self, paper_id: int, topic_keys: list[str]) -> None:
        with self.session() as session:
            paper = session.get(Paper, paper_id)
            if paper is None:
                return
            paper.topics.clear()
            self._attach_topics(session, paper, topic_keys)

    def get_papers_by_topic(self, topic_key: str, limit: int = 50) -> list[Paper]:
        with self.session() as session:
            papers = session.execute(
                select(Paper)
                .join(Paper.topics)
                .where(Topic.key == topic_key)
                .order_by(Paper.relevance_score.desc(), Paper.citation_count.desc())
                .limit(limit)
            ).scalars().all()
            for p in papers:
                _ = p.authors, p.topics
            return papers

    def get_recent_papers(self, days: int = 7, limit: int = 50) -> list[Paper]:
        cutoff = utc_now() - timedelta(days=days)
        with self.session() as session:
            papers = session.execute(
                select(Paper)
                .where(Paper.collected_at >= cutoff)
                .order_by(Paper.relevance_score.desc())
                .limit(limit)
            ).scalars().all()
            for p in papers:
                _ = p.authors, p.topics
            return papers

    def get_top_papers(self, limit: int = 20) -> list[Paper]:
        with self.session() as session:
            papers = session.execute(
                select(Paper)
                .order_by(Paper.relevance_score.desc(), Paper.citation_count.desc())
                .limit(limit)
            ).scalars().all()
            for p in papers:
                _ = p.authors, p.topics
            return papers

    def list_papers(self, limit: int | None = None) -> list[Paper]:
        with self.session() as session:
            stmt = select(Paper).order_by(Paper.relevance_score.desc(), Paper.collected_at.desc())
            if limit:
                stmt = stmt.limit(limit)
            papers = session.execute(stmt).scalars().all()
            for paper in papers:
                _ = paper.authors, paper.topics
            return papers

    def get_paper(self, paper_id: int) -> Paper | None:
        with self.session() as session:
            paper = session.get(Paper, paper_id)
            if paper:
                _ = paper.authors, paper.topics
            return paper

    def list_topics(self) -> list[Topic]:
        with self.session() as session:
            return session.execute(select(Topic).order_by(Topic.key.asc())).scalars().all()

    def list_youtube_resources(self, limit: int | None = None) -> list[YouTubeResource]:
        with self.session() as session:
            stmt = select(YouTubeResource).order_by(YouTubeResource.published_at.desc())
            if limit:
                stmt = stmt.limit(limit)
            return session.execute(stmt).scalars().all()

    def search_papers(self, query: str, limit: int = 50) -> list[Paper]:
        pattern = f"%{query}%"
        with self.session() as session:
            papers = session.execute(
                select(Paper)
                .where(or_(Paper.title.ilike(pattern), Paper.abstract.ilike(pattern)))
                .order_by(Paper.relevance_score.desc())
                .limit(limit)
            ).scalars().all()
            for paper in papers:
                _ = paper.authors, paper.topics
            return papers

    def update_paper_markdown_path(self, paper_id: int, markdown_path: str) -> None:
        with self.session() as session:
            paper = session.get(Paper, paper_id)
            if paper:
                paper.markdown_path = markdown_path

    def delete_papers_by_ids(self, paper_ids: list[int]) -> int:
        """删除指定论文，并清理失去关联的作者。"""
        if not paper_ids:
            return 0

        with self.session() as session:
            papers = session.execute(
                select(Paper).where(Paper.id.in_(paper_ids))
            ).scalars().all()
            for paper in papers:
                session.delete(paper)

            orphan_authors = session.execute(select(Author)).scalars().all()
            for author in orphan_authors:
                if not author.papers:
                    session.delete(author)

            return len(papers)

    def delete_youtube_resources_by_ids(self, resource_ids: list[int]) -> int:
        if not resource_ids:
            return 0

        with self.session() as session:
            resources = session.execute(
                select(YouTubeResource).where(YouTubeResource.id.in_(resource_ids))
            ).scalars().all()
            for resource in resources:
                session.delete(resource)
            return len(resources)

    def rename_topic_key_prefix(self, old_prefix: str, new_prefix: str) -> int:
        """
        重命名 topic key 前缀，并同步更新 parent_key、paper markdown_path 与 YouTube topic_key。
        返回受影响的 Topic 数量。
        """
        with self.session() as session:
            topics = session.execute(
                select(Topic).where(
                    or_(Topic.key == old_prefix, Topic.key.like(f"{old_prefix}/%"))
                )
            ).scalars().all()

            for topic in sorted(topics, key=lambda item: len(item.key)):
                topic.key = self._replace_prefix(topic.key, old_prefix, new_prefix)
                if topic.parent_key:
                    topic.parent_key = self._replace_prefix(topic.parent_key, old_prefix, new_prefix)

            youtube_resources = session.execute(select(YouTubeResource)).scalars().all()
            for resource in youtube_resources:
                if resource.topic_key:
                    resource.topic_key = self._replace_prefix(
                        resource.topic_key,
                        old_prefix,
                        new_prefix,
                    )

            papers = session.execute(select(Paper)).scalars().all()
            for paper in papers:
                if paper.markdown_path:
                    paper.markdown_path = self._replace_prefix(
                        paper.markdown_path,
                        old_prefix,
                        new_prefix,
                    )

            return len(topics)

    def remap_topic_keys(self, mapping: dict[str, str]) -> int:
        """
        按精确映射关系重命名 topic key，并同步更新 parent_key、paper markdown_path 与 YouTube topic_key。
        返回受影响的 Topic 数量。
        """
        if not mapping:
            return 0

        with self.session() as session:
            topics = session.execute(select(Topic)).scalars().all()
            affected = 0

            for topic in sorted(topics, key=lambda item: len(item.key), reverse=True):
                new_key = mapping.get(topic.key)
                new_parent_key = mapping.get(topic.parent_key or "", topic.parent_key)
                if new_key:
                    topic.key = new_key
                    affected += 1
                topic.parent_key = new_parent_key

            youtube_resources = session.execute(select(YouTubeResource)).scalars().all()
            for resource in youtube_resources:
                if resource.topic_key in mapping:
                    resource.topic_key = mapping[resource.topic_key]

            papers = session.execute(select(Paper)).scalars().all()
            for paper in papers:
                if paper.markdown_path:
                    for old_key, new_key in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
                        if paper.markdown_path == old_key or paper.markdown_path.startswith(f"{old_key}/"):
                            paper.markdown_path = paper.markdown_path.replace(old_key, new_key, 1)
                            break

            return affected

    def get_stats(self) -> dict[str, Any]:
        with self.session() as session:
            total = session.execute(select(func.count(Paper.id))).scalar()
            by_status = {}
            for status in ["unread", "reading", "read", "noted"]:
                count = session.execute(
                    select(func.count(Paper.id)).where(Paper.status == status)
                ).scalar()
                by_status[status] = count
            topic_counts = session.execute(
                select(Topic.key, func.count(Paper.id))
                .join(Paper.topics)
                .group_by(Topic.key)
                .order_by(func.count(Paper.id).desc())
            ).all()
            return {
                "total_papers": total,
                "by_status": by_status,
                "by_topic": {k: v for k, v in topic_counts},
            }

    def prune_topics(self, valid_keys: set[str]) -> int:
        """删除当前 taxonomy 中不存在且未被论文引用的 topic。"""
        with self.session() as session:
            stale_topics = session.execute(
                select(Topic).where(Topic.key.not_in(valid_keys))
            ).scalars().all()
            removed = 0
            for topic in stale_topics:
                if topic.papers:
                    continue
                session.delete(topic)
                removed += 1
            return removed

    def normalize_paper_topics(self) -> int:
        """根据当前 Topic.parent_key 为所有论文补全缺失的祖先 topic。"""
        with self.session() as session:
            topic_lookup = {
                topic.key: topic
                for topic in session.execute(select(Topic)).scalars().all()
            }
            attached = 0

            for paper in session.execute(select(Paper)).scalars().all():
                existing_keys = {topic.key for topic in paper.topics}
                for topic in list(paper.topics):
                    current = topic_lookup.get(topic.key)
                    while current and current.parent_key:
                        parent = topic_lookup.get(current.parent_key)
                        if parent and parent.key not in existing_keys:
                            paper.topics.append(parent)
                            existing_keys.add(parent.key)
                            attached += 1
                        current = parent

            return attached

    def normalize_empty_identifiers(self) -> int:
        """将历史数据中的空字符串标识符统一为 NULL。"""
        with self.session() as session:
            papers = session.execute(select(Paper)).scalars().all()
            updated = 0
            for paper in papers:
                changed = False
                for field in ["doi", "arxiv_id", "semantic_scholar_id", "openalex_id"]:
                    value = getattr(paper, field)
                    if isinstance(value, str) and not value.strip():
                        setattr(paper, field, None)
                        changed = True
                if changed:
                    updated += 1
            return updated

    @staticmethod
    def _replace_prefix(value: str, old_prefix: str, new_prefix: str) -> str:
        if value == old_prefix:
            return new_prefix
        if value.startswith(f"{old_prefix}/"):
            return value.replace(f"{old_prefix}/", f"{new_prefix}/", 1)
        return value

    # ── YouTube ──

    def add_youtube_resource(self, resource_data: dict[str, Any]) -> YouTubeResource:
        return self.upsert_youtube_resource(resource_data).record

    def upsert_youtube_resource(self, resource_data: dict[str, Any]) -> UpsertResult:
        with self.session() as session:
            if resource_data.get("video_id"):
                existing = session.execute(
                    select(YouTubeResource)
                    .where(YouTubeResource.video_id == resource_data["video_id"])
                ).scalar_one_or_none()
                if existing:
                    changed = False

                    merged_view_count = max(existing.view_count or 0, resource_data.get("view_count", 0) or 0)
                    if merged_view_count != (existing.view_count or 0):
                        existing.view_count = merged_view_count
                        changed = True

                    merged_description = self._pick_longer_text(
                        existing.description,
                        resource_data.get("description", ""),
                    )
                    if merged_description != (existing.description or ""):
                        existing.description = merged_description
                        changed = True

                    merged_topic_key = existing.topic_key or resource_data.get("topic_key", "")
                    if merged_topic_key != (existing.topic_key or ""):
                        existing.topic_key = merged_topic_key
                        changed = True

                    merged_channel_name = existing.channel_name or resource_data.get("channel_name", "")
                    if merged_channel_name != (existing.channel_name or ""):
                        existing.channel_name = merged_channel_name
                        changed = True

                    merged_channel_id = existing.channel_id or resource_data.get("channel_id", "")
                    if merged_channel_id != (existing.channel_id or ""):
                        existing.channel_id = merged_channel_id
                        changed = True

                    merged_url = existing.url or resource_data.get("url", "")
                    if merged_url != (existing.url or ""):
                        existing.url = merged_url
                        changed = True

                    merged_duration = existing.duration or resource_data.get("duration", "")
                    if merged_duration != (existing.duration or ""):
                        existing.duration = merged_duration
                        changed = True

                    merged_published_at = existing.published_at or resource_data.get("published_at")
                    if merged_published_at != existing.published_at:
                        existing.published_at = merged_published_at
                        changed = True

                    merged_resource_type = existing.resource_type or resource_data.get("resource_type", "video")
                    if merged_resource_type != (existing.resource_type or ""):
                        existing.resource_type = merged_resource_type
                        changed = True

                    return UpsertResult(record=existing, updated=changed)

            resource = YouTubeResource(**resource_data)
            session.add(resource)
            session.flush()
            return UpsertResult(record=resource, created=True)

    # ── 采集日志 ──

    def log_collection(self, source: str) -> int:
        with self.session() as session:
            log = CollectionLog(source=source)
            session.add(log)
            session.flush()
            return log.id

    def update_collection_log(self, log_id: int, **kwargs: Any) -> None:
        with self.session() as session:
            log = session.get(CollectionLog, log_id)
            if log:
                for k, v in kwargs.items():
                    setattr(log, k, v)
                log.finished_at = utc_now()
