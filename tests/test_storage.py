from sqlalchemy import select

from src.storage.database import Database
from src.storage.models import author_coauthors


def test_database_merge_prefers_better_tier(tmp_path):
    database = Database(str(tmp_path / "test.db"))
    first = database.add_paper(
        {
            "title": "Shared title",
            "abstract": "First",
            "journal": "Scientific Reports",
            "tier": 3,
            "authors": [],
            "topic_keys": [],
        }
    )
    merged = database.add_paper(
        {
            "title": "Shared title",
            "abstract": "Second",
            "journal": "Physical Review Letters",
            "tier": 1,
            "authors": [],
            "topic_keys": [],
        }
    )

    assert first.id == merged.id
    assert merged.tier == 1


def test_database_backfills_author_affiliation_on_merge(tmp_path):
    database = Database(str(tmp_path / "test.db"))
    database.add_paper(
        {
            "title": "Author affiliation test",
            "abstract": "First",
            "authors": ["Alice Smith"],
            "topic_keys": [],
        }
    )
    merged = database.add_paper(
        {
            "title": "Author affiliation test",
            "abstract": "Second",
            "authors": [
                {
                    "name": "Alice Smith",
                    "affiliation": "Department of Physics, Princeton University",
                    "openalex_id": "A123",
                }
            ],
            "topic_keys": [],
        }
    )

    assert len(merged.authors) == 1
    assert merged.authors[0].affiliation == "Department of Physics, Princeton University"
    assert merged.authors[0].openalex_id == "A123"


def test_upsert_paper_reports_created_updated_and_unchanged(tmp_path):
    database = Database(str(tmp_path / "test.db"))

    created = database.upsert_paper(
        {
            "title": "Shared title",
            "abstract": "First",
            "authors": ["Alice Smith"],
            "topic_keys": [],
        }
    )
    updated = database.upsert_paper(
        {
            "title": "Shared title",
            "abstract": "A much longer abstract",
            "authors": [
                "Alice Smith",
                {"name": "Bob Lee", "affiliation": "Department of Applied Mathematics, MIT"},
            ],
            "topic_keys": [],
        }
    )
    unchanged = database.upsert_paper(
        {
            "title": "Shared title",
            "abstract": "A much longer abstract",
            "authors": [
                "Alice Smith",
                {"name": "Bob Lee", "affiliation": "Department of Applied Mathematics, MIT"},
            ],
            "topic_keys": [],
        }
    )

    assert created.created is True
    assert created.updated is False
    assert updated.created is False
    assert updated.updated is True
    assert unchanged.created is False
    assert unchanged.updated is False
    assert unchanged.unchanged is True


def test_repeated_upsert_does_not_double_count_coauthors(tmp_path):
    database = Database(str(tmp_path / "test.db"))
    payload = {
        "title": "Coauthor test paper",
        "abstract": "First abstract",
        "authors": ["Alice Smith", "Bob Lee"],
        "topic_keys": [],
    }

    database.upsert_paper(payload)
    database.upsert_paper(payload)

    with database.session() as session:
        shared_papers = session.execute(
            select(author_coauthors.c.shared_papers)
        ).scalar_one()

    assert shared_papers == 1


def test_upsert_youtube_resource_reports_created_updated_and_unchanged(tmp_path):
    database = Database(str(tmp_path / "test.db"))

    created = database.upsert_youtube_resource(
        {
            "title": "Lecture 1",
            "channel_name": "Test Channel",
            "channel_id": "channel-1",
            "video_id": "video-1",
            "playlist_id": None,
            "url": "https://example.com/watch?v=video-1",
            "description": "Short description",
            "published_at": None,
            "duration": "PT10M",
            "view_count": 10,
            "topic_key": "ai_for_physics/generative_dynamics/flow_matching",
            "resource_type": "video",
        }
    )
    updated = database.upsert_youtube_resource(
        {
            "title": "Lecture 1",
            "channel_name": "Test Channel",
            "channel_id": "channel-1",
            "video_id": "video-1",
            "playlist_id": None,
            "url": "https://example.com/watch?v=video-1",
            "description": "A much longer description for the same resource",
            "published_at": None,
            "duration": "PT10M",
            "view_count": 20,
            "topic_key": "ai_for_physics/generative_dynamics/flow_matching",
            "resource_type": "video",
        }
    )
    unchanged = database.upsert_youtube_resource(
        {
            "title": "Lecture 1",
            "channel_name": "Test Channel",
            "channel_id": "channel-1",
            "video_id": "video-1",
            "playlist_id": None,
            "url": "https://example.com/watch?v=video-1",
            "description": "A much longer description for the same resource",
            "published_at": None,
            "duration": "PT10M",
            "view_count": 20,
            "topic_key": "ai_for_physics/generative_dynamics/flow_matching",
            "resource_type": "video",
        }
    )

    assert created.created is True
    assert updated.updated is True
    assert unchanged.unchanged is True
