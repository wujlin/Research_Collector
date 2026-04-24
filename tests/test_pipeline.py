from sqlalchemy import select

from src.pipeline import CollectionPipeline
from src.storage.markdown_store import MarkdownStore
from src.storage.models import CollectionLog


def test_pipeline_skips_disabled_source(tmp_path):
    pipeline = CollectionPipeline(db_path=str(tmp_path / "papers.db"))
    pipeline.settings["collection"]["source_policies"]["semantic_scholar"]["enabled"] = False

    summary = pipeline.collect(source="semantic_scholar", run_exports=False)

    assert summary["sources"]["semantic_scholar"]["status"] == "skipped"
    assert summary["sources"]["semantic_scholar"]["reason"] == "disabled_in_config"


def test_pipeline_reports_true_added_updated_and_unchanged_counts(tmp_path):
    pipeline = CollectionPipeline(db_path=str(tmp_path / "papers.db"))
    pipeline.markdown_store = MarkdownStore(str(tmp_path / "library"))
    pipeline.query_profiles["arxiv"] = ["dummy-query"]

    records = [
        {
            "title": "Score-Based Generative Modeling through Stochastic Differential Equations",
            "abstract": "We study reverse-time SDEs for score-based generation.",
            "authors": ["Alice Smith"],
            "year": 2026,
            "journal": "arXiv",
            "venue": "arXiv",
            "arxiv_id": "2601.00001",
            "url": "https://arxiv.org/abs/2601.00001",
            "pdf_url": "https://arxiv.org/pdf/2601.00001.pdf",
            "source": "arxiv",
        },
        {
            "title": "Score-Based Generative Modeling through Stochastic Differential Equations",
            "abstract": "A much longer abstract about reverse-time SDEs and probability flow ODEs.",
            "authors": ["Alice Smith", "Bob Lee"],
            "year": 2026,
            "journal": "arXiv",
            "venue": "arXiv",
            "arxiv_id": "2601.00001",
            "url": "https://arxiv.org/abs/2601.00001",
            "pdf_url": "https://arxiv.org/pdf/2601.00001.pdf",
            "source": "arxiv",
        },
        {
            "title": "Score-Based Generative Modeling through Stochastic Differential Equations",
            "abstract": "A much longer abstract about reverse-time SDEs and probability flow ODEs.",
            "authors": ["Alice Smith", "Bob Lee"],
            "year": 2026,
            "journal": "arXiv",
            "venue": "arXiv",
            "arxiv_id": "2601.00001",
            "url": "https://arxiv.org/abs/2601.00001",
            "pdf_url": "https://arxiv.org/pdf/2601.00001.pdf",
            "source": "arxiv",
        },
    ]

    class StubCollector:
        def __init__(self, items):
            self._items = list(items)
            self._idx = 0

        def collect(self, query: str = "", **kwargs):
            item = self._items[self._idx]
            self._idx += 1
            return [dict(item)]

    pipeline.collectors["arxiv"] = StubCollector(records)

    first = pipeline.collect(source="arxiv", run_exports=False)
    second = pipeline.collect(source="arxiv", run_exports=False)
    third = pipeline.collect(source="arxiv", run_exports=False)

    assert first["sources"]["arxiv"]["found"] == 1
    assert first["sources"]["arxiv"]["processed"] == 1
    assert first["sources"]["arxiv"]["added"] == 1
    assert first["sources"]["arxiv"]["updated"] == 0
    assert first["sources"]["arxiv"]["unchanged"] == 0

    assert second["sources"]["arxiv"]["added"] == 0
    assert second["sources"]["arxiv"]["updated"] == 1
    assert second["sources"]["arxiv"]["unchanged"] == 0

    assert third["sources"]["arxiv"]["added"] == 0
    assert third["sources"]["arxiv"]["updated"] == 0
    assert third["sources"]["arxiv"]["unchanged"] == 1

    with pipeline.database.session() as session:
        logs = session.execute(
            select(CollectionLog).where(CollectionLog.source == "arxiv").order_by(CollectionLog.id.asc())
        ).scalars().all()

    assert [log.papers_added for log in logs[-3:]] == [1, 0, 0]
    assert [log.papers_updated for log in logs[-3:]] == [0, 1, 0]
