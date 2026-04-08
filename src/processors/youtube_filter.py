"""YouTube 资源主题过滤器。"""

from __future__ import annotations

import re
from typing import Any

from src.processors.classifier import TopicClassifier
from src.utils.helpers import normalize_whitespace


class YouTubeFilter:
    def __init__(self, settings_config: str = "settings.yaml", topics_config: str = "topics.yaml"):
        self.classifier = TopicClassifier(topics_config=topics_config)
        settings = self.classifier.settings
        youtube_cfg = settings.get("filtering", {}).get("youtube", {})
        self.positive_keywords = [keyword.lower() for keyword in youtube_cfg.get("positive_keywords", [])]
        self.negative_keywords = [keyword.lower() for keyword in youtube_cfg.get("negative_keywords", [])]
        self.min_query_token_hits = int(youtube_cfg.get("min_query_token_hits", 2))
        self.min_positive_keyword_hits = int(youtube_cfg.get("min_positive_keyword_hits", 1))

    def evaluate(self, resource: dict[str, Any]) -> dict[str, Any]:
        title = resource.get("title", "")
        description = resource.get("description", "")
        text = self._normalize_text(" ".join([title, description, resource.get("channel_name", "")]))

        negative_hits = [keyword for keyword in self.negative_keywords if self._contains_keyword(text, keyword)]
        if negative_hits:
            return {
                "keep": False,
                "resolved_topic_key": "",
                "detected_topic_keys": [],
                "negative_keyword_hits": negative_hits,
                "positive_keyword_hits": [],
                "query_token_hits": 0,
                "reason": f"negative_keywords:{', '.join(negative_hits)}",
            }

        classified = self.classifier.classify_record({"title": title, "abstract": description})
        if classified.get("is_irrelevant"):
            hits = classified.get("negative_keyword_hits", [])
            return {
                "keep": False,
                "resolved_topic_key": "",
                "detected_topic_keys": [],
                "negative_keyword_hits": hits,
                "positive_keyword_hits": [],
                "query_token_hits": 0,
                "reason": f"classifier_negative:{', '.join(hits)}" if hits else "classifier_negative",
            }

        detected_topic_keys = classified.get("topic_keys", [])
        positive_hits = [keyword for keyword in self.positive_keywords if self._contains_keyword(text, keyword)]
        query_token_hits = 0
        if resource.get("query_source") == "search_terms":
            query_token_hits = self._count_query_token_hits(resource.get("matched_query", ""), text)

        keep = bool(
            detected_topic_keys
            or len(positive_hits) >= self.min_positive_keyword_hits
            or query_token_hits >= self.min_query_token_hits
        )

        return {
            "keep": keep,
            "resolved_topic_key": self._resolve_topic_key(resource, detected_topic_keys),
            "detected_topic_keys": detected_topic_keys,
            "negative_keyword_hits": [],
            "positive_keyword_hits": positive_hits,
            "query_token_hits": query_token_hits,
            "reason": "topic_or_keyword_match" if keep else "no_topic_or_keyword_match",
        }

    def _resolve_topic_key(self, resource: dict[str, Any], detected_topic_keys: list[str]) -> str:
        configured_topic = resource.get("topic_key", "")
        if configured_topic.count("/") == 2:
            return configured_topic
        for topic_key in detected_topic_keys:
            if topic_key.count("/") == 2:
                return topic_key
        return configured_topic

    def _count_query_token_hits(self, query: str, text: str) -> int:
        if not query:
            return 0
        tokens = [
            token for token in self._normalize_text(query).split()
            if len(token) >= 4 and token not in {"with", "lecture", "talk", "talks", "model", "models"}
        ]
        return sum(1 for token in tokens if re.search(rf"\b{re.escape(token)}\b", text))

    @staticmethod
    def _contains_keyword(text: str, keyword: str) -> bool:
        normalized_keyword = YouTubeFilter._normalize_text(keyword)
        if not normalized_keyword:
            return False
        pattern = r"\b" + r"\s+".join(re.escape(part) for part in normalized_keyword.split()) + r"\b"
        return bool(re.search(pattern, text))

    @staticmethod
    def _normalize_text(value: str) -> str:
        value = normalize_whitespace(value).lower()
        value = re.sub(r"[^a-z0-9]+", " ", value)
        return normalize_whitespace(value)
