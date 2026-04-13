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
