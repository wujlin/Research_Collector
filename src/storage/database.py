"""SQLite 数据库管理：初始化、会话管理、CRUD 操作。"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy import create_engine, func, or_, select
from sqlalchemy.orm import Session, sessionmaker

from src.utils.helpers import flatten_topics, normalize_title, parse_date, utc_now

from .models import Author, Base, CollectionLog, Paper, Topic, YouTubeResource


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
        """
        添加论文。如果 DOI 或 arXiv ID 已存在则跳过。
        paper_data 应包含: title, abstract, year, journal, doi, arxiv_id,
                           authors (list[str]), topic_keys (list[str]), ...
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
            return paper

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
    ) -> Paper:
        paper.abstract = self._pick_longer_text(paper.abstract, data.get("abstract", ""))
        paper.year = paper.year or data.get("year")
        paper.publication_date = paper.publication_date or parse_date(data.get("publication_date"))
        paper.journal = paper.journal or data.get("journal", "")
        paper.venue = paper.venue or data.get("venue", "")
        paper.url = paper.url or data.get("url", "")
        paper.pdf_url = paper.pdf_url or data.get("pdf_url", "")
        paper.doi = paper.doi or data.get("doi")
        paper.arxiv_id = paper.arxiv_id or data.get("arxiv_id")
        paper.semantic_scholar_id = paper.semantic_scholar_id or data.get("semantic_scholar_id")
        paper.openalex_id = paper.openalex_id or data.get("openalex_id")
        paper.citation_count = max(paper.citation_count or 0, data.get("citation_count", 0) or 0)
        paper.influential_citation_count = max(
            paper.influential_citation_count or 0,
            data.get("influential_citation_count", 0) or 0,
        )
        paper.relevance_score = max(paper.relevance_score or 0.0, data.get("relevance_score", 0.0) or 0.0)
        paper.tier = self._pick_better_tier(paper.tier, data.get("tier", 0))
        paper.is_seminal = paper.is_seminal or bool(data.get("is_seminal"))
        paper.source = self._merge_sources(paper.source, data.get("source", ""))
        if data.get("notes"):
            paper.notes = self._pick_longer_text(paper.notes, data["notes"])
        self._attach_authors(session, paper, data.get("authors", []))
        self._attach_topics(session, paper, data.get("topic_keys", []))
        paper.updated_at = utc_now()
        return paper

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

    def _get_or_create_author(self, session: Session, name: str) -> Author:
        author = session.execute(
            select(Author).where(Author.name == name)
        ).scalar_one_or_none()
        if author is None:
            author = Author(name=name)
            session.add(author)
            session.flush()
        return author

    # ── 查询 ──

    def _attach_authors(self, session: Session, paper: Paper, author_names: list[str]) -> None:
        existing = {author.name for author in paper.authors}
        for author_name in author_names:
            if not author_name or author_name in existing:
                continue
            paper.authors.append(self._get_or_create_author(session, author_name))
            existing.add(author_name)

    def _attach_topics(self, session: Session, paper: Paper, topic_keys: list[str]) -> None:
        existing = {topic.key for topic in paper.topics}
        for topic_key in topic_keys:
            if not topic_key or topic_key in existing:
                continue
            topic = session.execute(select(Topic).where(Topic.key == topic_key)).scalar_one_or_none()
            if topic:
                paper.topics.append(topic)
                existing.add(topic_key)

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
        with self.session() as session:
            if resource_data.get("video_id"):
                existing = session.execute(
                    select(YouTubeResource)
                    .where(YouTubeResource.video_id == resource_data["video_id"])
                ).scalar_one_or_none()
                if existing:
                    existing.view_count = max(existing.view_count or 0, resource_data.get("view_count", 0) or 0)
                    existing.description = self._pick_longer_text(
                        existing.description,
                        resource_data.get("description", ""),
                    )
                    return existing

            resource = YouTubeResource(**resource_data)
            session.add(resource)
            session.flush()
            return resource

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
