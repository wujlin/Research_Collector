"""基于关键词的主题分类器。"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from src.utils.helpers import (
    build_topic_index,
    flatten_topics,
    get_topic_ancestor_keys,
    load_config,
    normalize_whitespace,
)


@dataclass(slots=True)
class TopicMatch:
    key: str
    parent_key: str | None
    score: float
    display_name: str


class TopicClassifier:
    """用 topics.yaml 的关键词做轻量分类。"""

    def __init__(self, topics_config: str = "topics.yaml"):
        self.taxonomy = load_config(topics_config)
        self.settings = load_config("settings.yaml")
        self.entries = flatten_topics(self.taxonomy)
        self.topic_index = build_topic_index(self.taxonomy)
        self.negative_keywords = [
            keyword.lower()
            for keyword in self.settings.get("filtering", {}).get("negative_keywords", [])
        ]

    def classify(
        self,
        title: str,
        abstract: str,
        top_k: int = 3,
    ) -> list[TopicMatch]:
        title_text = normalize_whitespace(title).lower()
        abstract_text = normalize_whitespace(abstract).lower()
        normalized_title = self._normalize_keyword_text(title_text)
        normalized_abstract = self._normalize_keyword_text(abstract_text)
        combined = f"{title_text} {abstract_text}".strip()
        normalized_combined = self._normalize_keyword_text(combined)

        matches: list[TopicMatch] = []
        for entry in self.entries:
            score = 0.0
            for keyword in entry.get("keywords", []):
                keyword_text = self._normalize_keyword_text(keyword)
                title_hits = self._count_keyword_hits(keyword_text, normalized_title)
                abstract_hits = self._count_keyword_hits(keyword_text, normalized_abstract)
                combined_hits = self._count_keyword_hits(keyword_text, normalized_combined)
                if title_hits:
                    score += 2.5 * title_hits
                if abstract_hits:
                    score += 1.0 * abstract_hits
                if combined_hits > 1:
                    score += 0.5
            if score > 0:
                matches.append(
                    TopicMatch(
                        key=entry["key"],
                        parent_key=entry["parent_key"],
                        score=score,
                        display_name=entry["display_name"],
                    )
                )

        matches.sort(key=lambda item: item.score, reverse=True)
        return matches[:top_k]

    def classify_record(self, record: dict[str, Any], top_k: int = 3) -> dict[str, Any]:
        title = record.get("title", "")
        abstract = record.get("abstract", "")
        negative_hits = self._find_negative_keywords(title, abstract)
        if negative_hits:
            record["topic_keys"] = []
            record["topic_scores"] = {}
            record["negative_keyword_hits"] = negative_hits
            record["is_irrelevant"] = True
            record["excluded_reason"] = f"negative_keywords:{', '.join(negative_hits)}"
            return record

        matches = self.classify(title, abstract, top_k=top_k)
        topic_keys: list[str] = []
        for match in matches:
            if match.key not in topic_keys:
                topic_keys.append(match.key)
            for ancestor_key in get_topic_ancestor_keys(match.key, self.topic_index):
                if ancestor_key not in topic_keys:
                    topic_keys.append(ancestor_key)
        record["topic_keys"] = topic_keys
        record["topic_scores"] = {match.key: round(match.score, 2) for match in matches}
        record["negative_keyword_hits"] = []
        record["is_irrelevant"] = False
        return record

    def _find_negative_keywords(self, title: str, abstract: str) -> list[str]:
        text = f"{normalize_whitespace(title)} {normalize_whitespace(abstract)}".lower()
        return [keyword for keyword in self.negative_keywords if keyword in text]

    @staticmethod
    def _normalize_keyword_text(value: str) -> str:
        value = normalize_whitespace(value).lower()
        value = re.sub(r"[^a-z0-9]+", " ", value)
        return normalize_whitespace(value)

    @staticmethod
    def _count_keyword_hits(keyword: str, text: str) -> int:
        if not keyword or not text:
            return 0
        pattern = r"\b" + r"\s+".join(re.escape(part) for part in keyword.split()) + r"\b"
        return len(re.findall(pattern, text))
