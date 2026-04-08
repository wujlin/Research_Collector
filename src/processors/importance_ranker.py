"""面向研究主线的资源重要性排序器。"""

from __future__ import annotations

import math
import re
from datetime import datetime
from typing import Any

from src.utils.helpers import load_config, normalize_whitespace, parse_datetime, utc_now


class ImportanceRanker:
    def __init__(self, settings_config: str = "settings.yaml"):
        ranking = load_config(settings_config).get("ranking", {})
        self.paper_cfg = ranking.get("paper", {})
        self.youtube_cfg = ranking.get("youtube", {})

    def score_paper(self, payload: dict[str, Any]) -> tuple[float, str]:
        text = self._paper_text(payload)
        leaf_topics = [topic for topic in payload.get("topics", payload.get("topic_keys", [])) if topic.count("/") == 2]
        relevance_score = float(payload.get("relevance_score", 0.0) or 0.0)
        citation_count = int(payload.get("citation_count", 0) or 0)
        influential = int(payload.get("influential_citation_count", 0) or 0)
        tier = int(payload.get("tier", 0) or 0)
        venue_text = self._venue_text(payload)
        venue_quality = self.venue_quality_label(payload)

        score = relevance_score * 0.6
        score += min(12.0, math.log10(citation_count + 1) * 5.0)
        score += min(6.0, math.log10(influential + 1) * 4.0)
        score += float(self.paper_cfg.get("venue_tier_bonus", {}).get(str(tier), 0))
        score += self._topic_bonus(leaf_topics, self.paper_cfg.get("priority_topics", {}))
        score += self._keyword_bonus(text, self.paper_cfg.get("priority_keywords", {}))
        score += self._keyword_bonus(venue_text, self.paper_cfg.get("strong_venues", {}))
        score -= self._keyword_bonus(text, self.paper_cfg.get("suspicious_keywords", {}))
        score -= self._keyword_bonus(venue_text, self.paper_cfg.get("weak_venues", {}))

        if payload.get("is_seminal"):
            score += 18.0
        if venue_quality == "preprint":
            score -= float(self.paper_cfg.get("preprint_penalty", 4))
        if venue_quality == "unranked":
            score -= float(self.paper_cfg.get("unranked_venue_penalty", 8))
        if not leaf_topics:
            score -= float(self.paper_cfg.get("no_leaf_topic_penalty", 18))
        if not payload.get("topics") and not payload.get("topic_keys"):
            score -= float(self.paper_cfg.get("no_topic_penalty", 8))
        if payload.get("source") == "openalex" and citation_count == 0:
            score -= float(self.paper_cfg.get("openalex_zero_citation_penalty", 6))

        score = max(0.0, round(score, 2))
        return score, self._paper_bucket(score)

    @staticmethod
    def venue_quality_label(payload: dict[str, Any]) -> str:
        tier = int(payload.get("tier", 0) or 0)
        journal = ImportanceRanker._normalize_text(payload.get("journal", ""))
        venue = ImportanceRanker._normalize_text(payload.get("venue", ""))
        source = ImportanceRanker._normalize_text(payload.get("source", ""))
        if source == "arxiv" or journal in {"arxiv", "arxiv org"} or venue == "arxiv":
            return "preprint"
        if tier == 1:
            return "top_tier"
        if tier == 2:
            return "high_quality"
        if tier == 3:
            return "solid_domain"
        return "unranked"

    def score_youtube(self, payload: dict[str, Any]) -> tuple[float, str]:
        text = self._youtube_text(payload)
        topic_key = payload.get("topic_key", "")
        channel_name = payload.get("channel_name", "")
        view_count = int(payload.get("view_count", 0) or 0)
        published_at = parse_datetime(payload.get("published_at"))

        score = 30.0
        score += float(self.youtube_cfg.get("priority_topics", {}).get(topic_key, 0))
        score += float(self.youtube_cfg.get("priority_channels", {}).get(channel_name, 0))
        score += min(12.0, math.log10(view_count + 1) * 3.5)
        score += self._keyword_bonus(text, self.paper_cfg.get("priority_keywords", {})) * 0.5
        score -= self._keyword_bonus(text, self.paper_cfg.get("suspicious_keywords", {})) * 0.4
        if published_at:
            age_days = max(0, (utc_now() - published_at.replace(tzinfo=None)).days)
            score += max(0.0, 10.0 - min(age_days, 365) / 40.0)

        score = max(0.0, round(score, 2))
        return score, self._youtube_bucket(score)

    def _paper_bucket(self, score: float) -> str:
        if score >= float(self.paper_cfg.get("keep_threshold", 60)):
            return "keep"
        if score >= float(self.paper_cfg.get("review_threshold", 38)):
            return "review"
        return "archive"

    @staticmethod
    def _youtube_bucket(score: float) -> str:
        if score >= 55:
            return "keep"
        if score >= 40:
            return "review"
        return "archive"

    @staticmethod
    def _topic_bonus(topics: list[str], weights: dict[str, Any]) -> float:
        bonuses = sorted((float(weights.get(topic, 0)) for topic in topics), reverse=True)
        return sum(bonuses[:2])

    def _keyword_bonus(self, text: str, weights: dict[str, Any]) -> float:
        total = 0.0
        for keyword, weight in weights.items():
            if self._contains_keyword(text, keyword):
                total += float(weight)
        return total

    @staticmethod
    def _contains_keyword(text: str, keyword: str) -> bool:
        normalized_text = ImportanceRanker._normalize_text(text)
        normalized_keyword = ImportanceRanker._normalize_text(keyword)
        pattern = r"\b" + r"\s+".join(re.escape(part) for part in normalized_keyword.split()) + r"\b"
        return bool(re.search(pattern, normalized_text))

    @staticmethod
    def _normalize_text(value: str) -> str:
        value = normalize_whitespace(value).lower()
        value = re.sub(r"[^a-z0-9]+", " ", value)
        return normalize_whitespace(value)

    @staticmethod
    def _paper_text(payload: dict[str, Any]) -> str:
        topics = " ".join(payload.get("topics", payload.get("topic_keys", [])))
        return f"{payload.get('title', '')} {payload.get('abstract', '')} {topics}"

    @staticmethod
    def _venue_text(payload: dict[str, Any]) -> str:
        return " ".join([payload.get("journal", ""), payload.get("venue", "")])

    @staticmethod
    def _youtube_text(payload: dict[str, Any]) -> str:
        return " ".join(
            [
                payload.get("title", ""),
                payload.get("description", ""),
                payload.get("channel_name", ""),
                payload.get("topic_key", ""),
            ]
        )
