from src.storage.database import Database


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
