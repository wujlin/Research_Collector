"""论文相关性与层级评分。"""

from __future__ import annotations

import math
from typing import Any

from src.utils.helpers import load_config, normalize_whitespace, utc_now


class RelevanceScorer:
    def __init__(self, sources_config: str = "sources.yaml"):
        self.sources_config = load_config(sources_config)
        self._journal_index = self._build_journal_index(self.sources_config["journal_tiers"])

    def score_record(self, record: dict[str, Any]) -> dict[str, Any]:
        tier_level, tier_weight = self._match_tier(record)
        citation_count = int(record.get("citation_count", 0) or 0)
        influential_count = int(record.get("influential_citation_count", 0) or 0)
        year = int(record.get("year", 0) or 0)
        topic_count = len(record.get("topic_keys", []))
        abstract_length = len(record.get("abstract", "") or "")

        age = max(0, utc_now().year - year) if year else 12
        recency_score = max(0.0, 24 - min(age, 12) * 2)
        citation_score = min(24.0, math.log10(citation_count + 1) * 10.0)
        influence_score = min(12.0, math.log10(influential_count + 1) * 8.0)
        topic_score = min(18.0, topic_count * 5.0)
        abstract_score = min(8.0, abstract_length / 120.0)
        seminal_bonus = 10.0 if record.get("is_seminal") else 0.0
        preprint_bonus = 4.0 if record.get("source") == "arxiv" and age <= 2 else 0.0
        tier_score = float(tier_weight) * 2.0

        record["tier"] = tier_level
        record["tier_weight"] = tier_weight
        record["venue_quality"] = self.describe_venue_quality(record, tier_level)
        record["relevance_score"] = round(
            min(
                100.0,
                recency_score
                + citation_score
                + influence_score
                + topic_score
                + abstract_score
                + tier_score
                + seminal_bonus
                + preprint_bonus,
            ),
            2,
        )
        return record

    @staticmethod
    def describe_venue_quality(record: dict[str, Any], tier_level: int) -> str:
        journal = normalize_whitespace(record.get("journal", "")).lower()
        venue = normalize_whitespace(record.get("venue", "")).lower()
        source = normalize_whitespace(record.get("source", "")).lower()
        if source == "arxiv" or journal in {"arxiv", "arxiv.org"} or venue == "arxiv":
            return "preprint"
        if tier_level == 1:
            return "top_tier"
        if tier_level == 2:
            return "high_quality"
        if tier_level == 3:
            return "solid_domain"
        return "unranked"

    def _match_tier(self, record: dict[str, Any]) -> tuple[int, int]:
        venue_candidates = [
            normalize_whitespace(record.get("journal", "")).lower(),
            normalize_whitespace(record.get("venue", "")).lower(),
        ]
        doi = normalize_whitespace(record.get("doi", "")).lower()

        for candidate in venue_candidates:
            if not candidate:
                continue
            if candidate in self._journal_index:
                return self._journal_index[candidate]

        for key, value in self._journal_index.items():
            normalized_key = normalize_whitespace(key).lower()
            if not normalized_key:
                continue
            if doi and normalized_key and normalized_key in doi:
                return value
        return (1 if record.get("source") == "arxiv" else 0, 2 if record.get("source") == "arxiv" else 0)

    @staticmethod
    def _build_journal_index(journal_tiers: dict[str, Any]) -> dict[str, tuple[int, int]]:
        index: dict[str, tuple[int, int]] = {}
        for tier_name, tier_data in journal_tiers.items():
            tier_level = 0 if tier_name == "preprint" else int(tier_name.split("_")[-1])
            tier_weight = int(tier_data["weight"])
            for journal in tier_data.get("journals", []):
                names = [journal["name"], *journal.get("aliases", [])]
                for name in names:
                    index[normalize_whitespace(name).lower()] = (tier_level, tier_weight)
        return index
