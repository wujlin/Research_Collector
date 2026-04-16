#!/usr/bin/env python3
"""迁移脚本：创建 venues / author_coauthors 表，从现有数据填充。

操作：
1. 新建 venues 表和 author_coauthors 表（如不存在）
2. 给 papers 表添加 venue_id 列（如不存在）
3. 给 authors 表添加新列（orcid, country, works_count, cited_by_count, research_interests）
4. 从 sources.yaml + venue_reputation.yaml 填充 venues 表
5. 将 papers.journal / papers.venue 匹配到 venues.id
6. 从 paper_authors 推导 author_coauthors 合作网络
"""

from __future__ import annotations

import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sqlite3

import yaml

DB_PATH = ROOT / "data" / "papers.db"


def _load_yaml(name: str) -> dict:
    with open(ROOT / "config" / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def migrate() -> dict:
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    stats: dict[str, int] = {}

    # ── 1. Schema changes ──
    c.execute("""
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(300) NOT NULL UNIQUE,
            display_name VARCHAR(300) DEFAULT '',
            tier INTEGER DEFAULT 0,
            reputation VARCHAR(20) DEFAULT 'unreviewed',
            issn VARCHAR(20),
            openalex_id VARCHAR(50),
            publisher VARCHAR(200) DEFAULT '',
            venue_type VARCHAR(30) DEFAULT 'journal',
            paper_count INTEGER DEFAULT 0
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS author_coauthors (
            author_a_id INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
            author_b_id INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
            shared_papers INTEGER DEFAULT 1,
            PRIMARY KEY (author_a_id, author_b_id)
        )
    """)

    existing_cols = {row[1] for row in c.execute("PRAGMA table_info(papers)")}
    if "venue_id" not in existing_cols:
        c.execute("ALTER TABLE papers ADD COLUMN venue_id INTEGER REFERENCES venues(id)")

    author_cols = {row[1] for row in c.execute("PRAGMA table_info(authors)")}
    for col, typ in [
        ("orcid", "VARCHAR(50)"),
        ("country", "VARCHAR(100) DEFAULT ''"),
        ("works_count", "INTEGER DEFAULT 0"),
        ("cited_by_count", "INTEGER DEFAULT 0"),
        ("research_interests", "TEXT DEFAULT ''"),
    ]:
        if col not in author_cols:
            c.execute(f"ALTER TABLE authors ADD COLUMN {col} {typ}")

    c.execute("CREATE INDEX IF NOT EXISTS ix_papers_venue_id ON papers(venue_id)")
    c.execute("CREATE INDEX IF NOT EXISTS ix_authors_openalex_id ON authors(openalex_id)")
    c.execute("CREATE INDEX IF NOT EXISTS ix_venues_tier ON venues(tier)")
    conn.commit()

    # ── 2. Populate venues from config ──
    sources = _load_yaml("sources.yaml")
    reputation = _load_yaml("venue_reputation.yaml")
    venue_rep = reputation.get("venues", {})

    venue_count = 0
    for tier_name, tier_data in sources.get("journal_tiers", {}).items():
        tier_level = 0 if tier_name == "preprint" else int(tier_name.split("_")[-1])
        tier_weight = int(tier_data.get("weight", 0))
        vtype = "preprint" if tier_name == "preprint" else "journal"

        for journal in tier_data.get("journals", []):
            name = journal["name"]
            rep_entry = venue_rep.get(name.lower(), {})
            rep_status = rep_entry.get("status", "unreviewed")
            issn = journal.get("issn", "")
            oa_id = journal.get("openalex_id", "")

            c.execute("SELECT id FROM venues WHERE name = ?", (name,))
            if c.fetchone() is None:
                c.execute(
                    """INSERT INTO venues (name, display_name, tier, reputation, issn, openalex_id, venue_type)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (name, name, tier_level, rep_status, issn, oa_id, vtype),
                )
                venue_count += 1

            for alias in journal.get("aliases", []):
                c.execute("SELECT id FROM venues WHERE name = ?", (alias,))
                if c.fetchone() is None:
                    c.execute(
                        """INSERT INTO venues (name, display_name, tier, reputation, issn, openalex_id, venue_type)
                           VALUES (?, ?, ?, ?, ?, ?, ?)""",
                        (alias, name, tier_level, rep_status, issn, oa_id, vtype),
                    )
                    venue_count += 1

    conn.commit()
    stats["venues_created"] = venue_count

    # ── 3. Link papers to venues ──
    c.execute("SELECT id, name FROM venues")
    venue_lookup: dict[str, int] = {}
    for vid, vname in c.fetchall():
        venue_lookup[vname.lower()] = vid

    c.execute("SELECT id, journal, venue FROM papers WHERE venue_id IS NULL")
    link_count = 0
    for pid, journal, venue in c.fetchall():
        matched_vid = venue_lookup.get((journal or "").lower()) or venue_lookup.get((venue or "").lower())
        if matched_vid:
            c.execute("UPDATE papers SET venue_id = ? WHERE id = ?", (matched_vid, pid))
            link_count += 1

    conn.commit()
    stats["papers_linked_to_venue"] = link_count

    # Update venue paper counts
    c.execute("""
        UPDATE venues SET paper_count = (
            SELECT COUNT(*) FROM papers WHERE papers.venue_id = venues.id
        )
    """)
    conn.commit()

    # ── 4. Build co-authorship network ──
    c.execute("SELECT paper_id, author_id FROM paper_authors ORDER BY paper_id")
    paper_to_authors: dict[int, list[int]] = defaultdict(list)
    for pid, aid in c.fetchall():
        paper_to_authors[pid].append(aid)

    coauth_counts: dict[tuple[int, int], int] = defaultdict(int)
    for authors_list in paper_to_authors.values():
        if len(authors_list) < 2:
            continue
        for a, b in combinations(sorted(set(authors_list)), 2):
            coauth_counts[(a, b)] += 1

    c.execute("DELETE FROM author_coauthors")
    for (a, b), count in coauth_counts.items():
        c.execute(
            "INSERT INTO author_coauthors (author_a_id, author_b_id, shared_papers) VALUES (?, ?, ?)",
            (a, b, count),
        )

    conn.commit()
    stats["coauthor_pairs"] = len(coauth_counts)

    conn.close()
    return stats


if __name__ == "__main__":
    result = migrate()
    print(result)
