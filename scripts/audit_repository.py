#!/usr/bin/env python3
"""Audit cross-layer consistency between DB, Markdown, generated JSON, and digest assets."""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "library"
IMAGE_RE = re.compile(r"!\[[^]]*]\(([^)]+)\)")
PAPER_LINK_RE = re.compile(r"^- \[[^]]+]\(([^)]+\.md)\)", re.MULTILINE)


def flatten_topics(node: dict, prefix: str = "", parent: str | None = None) -> list[dict]:
    entries = []
    for key, value in node.items():
        full_key = f"{prefix}/{key}" if prefix else key
        entries.append({"key": full_key, "parent_key": parent})
        entries.extend(flatten_topics(value.get("subtopics", {}), full_key, full_key))
    return entries


def load_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        return {}
    end = content.find("\n---\n", 4)
    if end < 0:
        return {}
    parsed = yaml.safe_load(content[4:end]) or {}
    return parsed if isinstance(parsed, dict) else {}


def main() -> None:
    database_path = ROOT / "data" / "papers.db"
    if not database_path.exists():
        print("SKIP: data/papers.db is not available in this checkout")
        return

    issues: list[str] = []
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    taxonomy = yaml.safe_load((ROOT / "config" / "topics.yaml").read_text(encoding="utf-8"))
    config_topics = {entry["key"] for entry in flatten_topics(taxonomy)}
    database_topics = {row["key"] for row in connection.execute("SELECT key FROM topics")}
    if config_topics != database_topics:
        issues.append(
            f"taxonomy keys differ: config-only={sorted(config_topics - database_topics)}, "
            f"db-only={sorted(database_topics - config_topics)}"
        )

    papers = {row["id"]: dict(row) for row in connection.execute("SELECT * FROM papers")}
    paper_topics: dict[int, list[str]] = defaultdict(list)
    for row in connection.execute(
        "SELECT pt.paper_id,t.key FROM paper_topics pt JOIN topics t ON t.id=pt.topic_id"
    ):
        paper_topics[row["paper_id"]].append(row["key"])

    managed_paths = {paper["markdown_path"] for paper in papers.values() if paper["markdown_path"]}
    for paper in papers.values():
        if not paper["markdown_path"] or not (LIBRARY / paper["markdown_path"]).exists():
            issues.append(f"missing managed Markdown for paper {paper['id']}: {paper['markdown_path']}")

    unmanaged = []
    for path in LIBRARY.rglob("*.md"):
        relative = path.relative_to(LIBRARY)
        if relative.parts[0] == "archive" or path.name == "_index.md" or relative.as_posix() == "index.md":
            continue
        if relative.as_posix() not in managed_paths:
            unmanaged.append(relative.as_posix())
    if unmanaged:
        issues.append(f"unmanaged library Markdown files: {len(unmanaged)}")

    metadata_mismatches = Counter()
    for paper_id, paper in papers.items():
        if not paper["markdown_path"]:
            continue
        path = LIBRARY / paper["markdown_path"]
        if not path.exists():
            continue
        frontmatter = load_frontmatter(path)
        checks = {
            "title": (frontmatter.get("title"), paper["title"]),
            "year": (str(frontmatter.get("year") or ""), str(paper["year"] or "")),
            "status": (frontmatter.get("status") or "", paper["status"] or ""),
            "source": (frontmatter.get("source") or "", paper["source"] or ""),
            "tier": (int(frontmatter.get("tier") or 0), int(paper["tier"] or 0)),
            "relevance_score": (
                float(frontmatter.get("relevance_score") or 0),
                round(float(paper["relevance_score"] or 0), 2),
            ),
            "collected": (
                str(frontmatter.get("collected") or ""),
                str(paper["collected_at"] or "")[:10],
            ),
            "topics": (
                sorted(frontmatter.get("topics") or []),
                sorted(paper_topics.get(paper_id, [])),
            ),
        }
        for field, (markdown_value, database_value) in checks.items():
            if markdown_value != database_value:
                metadata_mismatches[field] += 1
    if metadata_mismatches:
        issues.append(f"DB/Markdown metadata mismatches: {dict(metadata_mismatches)}")

    topic_counts = Counter()
    for keys in paper_topics.values():
        topic_counts.update(keys)
    topic_counts["uncategorized"] = sum(1 for paper_id in papers if not paper_topics.get(paper_id))

    broken_index_links = 0
    index_count_mismatches = 0
    for index_path in LIBRARY.rglob("_index.md"):
        key = index_path.parent.relative_to(LIBRARY).as_posix()
        frontmatter = load_frontmatter(index_path)
        if int(frontmatter.get("paper_count") or 0) != topic_counts.get(key, 0):
            index_count_mismatches += 1
        for target in PAPER_LINK_RE.findall(index_path.read_text(encoding="utf-8")):
            if not (index_path.parent / target).resolve().exists():
                broken_index_links += 1
    if index_count_mismatches:
        issues.append(f"topic index count mismatches: {index_count_mismatches}")
    if broken_index_links:
        issues.append(f"broken topic index links: {broken_index_links}")

    invalid_youtube_topics = connection.execute(
        """
        SELECT COUNT(*) FROM youtube_resources y
        WHERE COALESCE(y.topic_key, '') <> ''
          AND NOT EXISTS (SELECT 1 FROM topics t WHERE t.key = y.topic_key)
        """
    ).fetchone()[0]
    if invalid_youtube_topics:
        issues.append(f"invalid YouTube topic keys: {invalid_youtube_topics}")

    digest_paths = {
        path.relative_to(ROOT / "digests").as_posix()
        for path in (ROOT / "digests").rglob("*.md")
    }
    generated_digests = {
        item["path"]
        for item in json.loads(
            (ROOT / "web" / "public" / "generated" / "digests.json").read_text(encoding="utf-8")
        )
    }
    if digest_paths != generated_digests:
        issues.append(
            f"digest manifest differs: missing={len(digest_paths - generated_digests)}, "
            f"extra={len(generated_digests - digest_paths)}"
        )

    missing_images = 0
    nonportable_pdf_images = 0
    for note in (ROOT / "digests").rglob("*.md"):
        for target in IMAGE_RE.findall(note.read_text(encoding="utf-8")):
            clean_target = target.split("#", 1)[0].split("?", 1)[0].strip()
            if clean_target.startswith(("http://", "https://", "data:")):
                continue
            destination = (note.parent / clean_target).resolve()
            if not destination.exists():
                missing_images += 1
                continue
            try:
                relative = destination.relative_to(ROOT)
            except ValueError:
                continue
            if relative.parts and relative.parts[0] == "pdfs":
                nonportable_pdf_images += 1
    if missing_images:
        issues.append(f"missing digest images: {missing_images}")
    if nonportable_pdf_images:
        issues.append(f"digest images still pointing into ignored pdfs/: {nonportable_pdf_images}")

    connection.close()
    if issues:
        print("Repository consistency audit failed:")
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)
    print(
        {
            "status": "ok",
            "papers": len(papers),
            "topics": len(database_topics),
            "digests": len(digest_paths),
        }
    )


if __name__ == "__main__":
    main()
