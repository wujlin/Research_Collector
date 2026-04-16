"""
SQLAlchemy 数据模型：Paper, Author, Venue, Topic, YouTubeResource 及关联表。

核心实体关系：
  Paper ↔ Author (多对多, paper_authors)
  Paper ↔ Topic  (多对多, paper_topics)
  Paper → Venue   (多对一, venue_id FK)
  Paper → Paper  (多对多, paper_references 引用网络)
  Author ↔ Author (多对多, author_coauthors 合作网络)
"""

from datetime import datetime

from sqlalchemy import (
    Column, Integer, String, Text, Float, Date, DateTime,
    Boolean, ForeignKey, Table, UniqueConstraint, Index,
)
from sqlalchemy.orm import DeclarativeBase, relationship

from src.utils.helpers import utc_now


class Base(DeclarativeBase):
    pass


# ── 多对多关联表 ──

paper_authors = Table(
    "paper_authors",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("papers.id", ondelete="CASCADE"), primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id", ondelete="CASCADE"), primary_key=True),
    Column("position", Integer, default=0),
)

paper_topics = Table(
    "paper_topics",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("papers.id", ondelete="CASCADE"), primary_key=True),
    Column("topic_id", Integer, ForeignKey("topics.id", ondelete="CASCADE"), primary_key=True),
    Column("confidence", Float, default=1.0),
)

paper_references = Table(
    "paper_references",
    Base.metadata,
    Column("citing_id", Integer, ForeignKey("papers.id", ondelete="CASCADE"), primary_key=True),
    Column("cited_id", Integer, ForeignKey("papers.id", ondelete="CASCADE"), primary_key=True),
)

author_coauthors = Table(
    "author_coauthors",
    Base.metadata,
    Column("author_a_id", Integer, ForeignKey("authors.id", ondelete="CASCADE"), primary_key=True),
    Column("author_b_id", Integer, ForeignKey("authors.id", ondelete="CASCADE"), primary_key=True),
    Column("shared_papers", Integer, default=1),
)


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    abstract = Column(Text, default="")
    year = Column(Integer)
    publication_date = Column(Date)
    journal = Column(String(200), default="")
    venue = Column(String(200), default="")
    venue_id = Column(Integer, ForeignKey("venues.id"), nullable=True)
    doi = Column(String(100), unique=True, nullable=True)
    arxiv_id = Column(String(50), unique=True, nullable=True)
    semantic_scholar_id = Column(String(50), nullable=True)
    openalex_id = Column(String(50), nullable=True)
    url = Column(String(500), default="")
    pdf_url = Column(String(500), default="")

    citation_count = Column(Integer, default=0)
    influential_citation_count = Column(Integer, default=0)
    relevance_score = Column(Float, default=0.0)
    tier = Column(Integer, default=0)

    status = Column(String(20), default="unread")
    is_seminal = Column(Boolean, default=False)

    source = Column(String(50), default="")
    collected_at = Column(DateTime, default=utc_now)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)
    markdown_path = Column(String(300), default="")
    notes = Column(Text, default="")

    authors = relationship("Author", secondary=paper_authors, back_populates="papers")
    topics = relationship("Topic", secondary=paper_topics, back_populates="papers")
    venue_ref = relationship("Venue", back_populates="papers")
    references = relationship(
        "Paper",
        secondary=paper_references,
        primaryjoin=id == paper_references.c.citing_id,
        secondaryjoin=id == paper_references.c.cited_id,
        backref="cited_by",
    )

    __table_args__ = (
        Index("ix_papers_year", "year"),
        Index("ix_papers_relevance", "relevance_score"),
        Index("ix_papers_status", "status"),
        Index("ix_papers_venue_id", "venue_id"),
    )

    def __repr__(self):
        return f"<Paper(id={self.id}, title='{self.title[:60]}...', year={self.year})>"


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    semantic_scholar_id = Column(String(50), nullable=True)
    openalex_id = Column(String(50), nullable=True)
    orcid = Column(String(50), nullable=True)
    affiliation = Column(String(300), default="")
    country = Column(String(100), default="")
    h_index = Column(Integer, default=0)
    works_count = Column(Integer, default=0)
    cited_by_count = Column(Integer, default=0)
    research_interests = Column(Text, default="")

    papers = relationship("Paper", secondary=paper_authors, back_populates="authors")
    coauthors = relationship(
        "Author",
        secondary=author_coauthors,
        primaryjoin=id == author_coauthors.c.author_a_id,
        secondaryjoin=id == author_coauthors.c.author_b_id,
    )

    __table_args__ = (
        UniqueConstraint("name", "affiliation", name="uq_author_name_affil"),
        Index("ix_authors_openalex_id", "openalex_id"),
    )

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"


class Venue(Base):
    """期刊 / 会议实体，用于构建期刊网络和统一 venue 名称归一化。"""
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False, unique=True)
    display_name = Column(String(300), default="")
    tier = Column(Integer, default=0)
    reputation = Column(String(20), default="unreviewed")
    issn = Column(String(20), nullable=True)
    openalex_id = Column(String(50), nullable=True)
    publisher = Column(String(200), default="")
    venue_type = Column(String(30), default="journal")
    paper_count = Column(Integer, default=0)

    papers = relationship("Paper", back_populates="venue_ref")

    __table_args__ = (
        Index("ix_venues_tier", "tier"),
    )

    def __repr__(self):
        return f"<Venue(name='{self.name}', tier={self.tier})>"


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(100), unique=True, nullable=False)
    display_name = Column(String(200), nullable=False)
    parent_key = Column(String(100), nullable=True)
    description = Column(Text, default="")

    papers = relationship("Paper", secondary=paper_topics, back_populates="topics")

    def __repr__(self):
        return f"<Topic(key='{self.key}', display_name='{self.display_name}')>"


class YouTubeResource(Base):
    __tablename__ = "youtube_resources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    channel_name = Column(String(200), default="")
    channel_id = Column(String(50), default="")
    video_id = Column(String(20), unique=True, nullable=True)
    playlist_id = Column(String(50), nullable=True)
    url = Column(String(500), default="")
    description = Column(Text, default="")
    published_at = Column(DateTime, nullable=True)
    duration = Column(String(20), default="")
    view_count = Column(Integer, default=0)
    topic_key = Column(String(100), default="")
    resource_type = Column(String(20), default="video")
    collected_at = Column(DateTime, default=utc_now)

    def __repr__(self):
        return f"<YouTubeResource(title='{self.title[:60]}...', type='{self.resource_type}')>"


class CollectionLog(Base):
    __tablename__ = "collection_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(50), nullable=False)
    started_at = Column(DateTime, default=utc_now)
    finished_at = Column(DateTime, nullable=True)
    papers_found = Column(Integer, default=0)
    papers_added = Column(Integer, default=0)
    papers_updated = Column(Integer, default=0)
    status = Column(String(20), default="running")
    error_message = Column(Text, default="")
