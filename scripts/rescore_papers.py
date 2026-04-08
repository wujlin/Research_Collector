#!/usr/bin/env python3
"""按当前 venue tier 和 relevance 规则重算现有论文。"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline
from src.processors.citation_analyzer import CitationAnalyzer
from src.processors.relevance_scorer import RelevanceScorer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Rescore stored papers with current venue/relevance rules")
    parser.add_argument("--collected-after", default="", help="Only rescore papers collected after YYYY-MM-DD")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    cutoff = datetime.fromisoformat(f"{args.collected_after}T00:00:00") if args.collected_after else None

    pipeline = CollectionPipeline()
    scorer = RelevanceScorer()
    analyzer = CitationAnalyzer()

    updated = 0

    with pipeline.database.session() as session:
        from src.storage.models import Paper

        papers = session.query(Paper).all()
        for paper in papers:
            if cutoff and (not paper.collected_at or paper.collected_at < cutoff):
                continue
            record = {
                "title": paper.title,
                "abstract": paper.abstract,
                "year": paper.year,
                "journal": paper.journal,
                "venue": paper.venue,
                "doi": paper.doi,
                "source": paper.source,
                "citation_count": paper.citation_count,
                "influential_citation_count": paper.influential_citation_count,
                "is_seminal": paper.is_seminal,
                "topic_keys": [topic.key for topic in paper.topics],
            }
            scorer.score_record(record)
            analyzer.enrich_record(record)
            paper.tier = record.get("tier", 0) or 0
            paper.relevance_score = record.get("relevance_score", 0.0) or 0.0
            paper.is_seminal = paper.is_seminal or bool(record.get("seminal_candidate"))
            updated += 1

    pipeline._refresh_library_indices()
    pipeline.export_all()
    print({"rescored_papers": updated, "collected_after": args.collected_after or None})


if __name__ == "__main__":
    main()
