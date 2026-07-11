from datetime import datetime
from pathlib import Path

import yaml

from src.storage.markdown_store import MarkdownStore
from src.storage.models import Paper, Topic


def test_ensure_directory_structure_does_not_clear_existing_indexes(tmp_path):
    store = MarkdownStore(str(tmp_path / "library"))
    store.ensure_directory_structure("config/topics.yaml")
    index_path = tmp_path / "library" / "ai_for_physics" / "_index.md"
    index_path.write_text("preserve me\n", encoding="utf-8")

    store.ensure_directory_structure("config/topics.yaml")

    assert index_path.read_text(encoding="utf-8") == "preserve me\n"


def test_topic_index_uses_canonical_relative_paper_path(tmp_path):
    store = MarkdownStore(str(tmp_path / "library"))
    paper = Paper(
        title="Energy Landscape Test",
        year=2026,
        journal="arXiv",
        markdown_path="ai_for_physics/generative_dynamics/energy_based_models/energy-landscape-test.md",
    )
    target = tmp_path / "library" / paper.markdown_path
    target.parent.mkdir(parents=True)
    target.write_text("paper\n", encoding="utf-8")

    store.write_topic_index("ai_for_physics", "AI for Physics", "", [paper])

    index = (tmp_path / "library" / "ai_for_physics" / "_index.md").read_text(encoding="utf-8")
    assert "(generative_dynamics/energy_based_models/energy-landscape-test.md)" in index


def test_save_paper_preserves_human_fields_and_uses_original_collection_date(tmp_path):
    store = MarkdownStore(str(tmp_path / "library"))
    paper = Paper(
        title="Backslash ${\\rm SU}(N)$ Test",
        abstract="Canonical abstract",
        year=2026,
        status="read",
        collected_at=datetime(2026, 4, 7, 12, 0, 0),
    )
    paper.topics = [Topic(key="ai_for_physics/generative_dynamics/energy_based_models")]

    relative = store.save_paper(paper)
    path = tmp_path / "library" / relative
    content = path.read_text(encoding="utf-8")
    content = content.replace(
        'source: ""\n---',
        'source: ""\ndigest: "digests/example.md"\n---',
    ).replace("## Notes\n", "## Notes\n\nHuman note.\n")
    path.write_text(content, encoding="utf-8")
    paper.markdown_path = relative

    store.save_paper(paper)

    refreshed = path.read_text(encoding="utf-8")
    frontmatter_text = refreshed.split("---", 2)[1]
    frontmatter = yaml.safe_load(frontmatter_text)
    assert frontmatter["title"] == paper.title
    assert frontmatter["collected"] == "2026-04-07"
    assert frontmatter["digest"] == "digests/example.md"
    assert "Human note." in refreshed
