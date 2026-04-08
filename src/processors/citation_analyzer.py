"""轻量引用与桥接信号分析。"""

from __future__ import annotations

from typing import Any


class CitationAnalyzer:
    """在没有完整引用图时，先计算足够实用的 bridge / seminal 信号。"""

    def enrich_record(self, record: dict[str, Any]) -> dict[str, Any]:
        parents = {topic.split("/")[0] for topic in record.get("topic_keys", [])}
        bridge_score = max(0, len(parents) - 1) * 5
        citation_count = int(record.get("citation_count", 0) or 0)
        influential = int(record.get("influential_citation_count", 0) or 0)

        record["bridge_score"] = bridge_score
        record["seminal_candidate"] = bool(record.get("is_seminal")) or (
            citation_count >= 150 or influential >= 30
        )
        return record

    def summarize(self, records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
        sorted_by_citation = sorted(
            records,
            key=lambda item: (
                int(item.get("citation_count", 0) or 0),
                float(item.get("relevance_score", 0.0) or 0.0),
            ),
            reverse=True,
        )
        sorted_by_bridge = sorted(
            records,
            key=lambda item: (
                int(item.get("bridge_score", 0) or 0),
                float(item.get("relevance_score", 0.0) or 0.0),
            ),
            reverse=True,
        )
        return {
            "most_cited": sorted_by_citation[:10],
            "bridge_papers": sorted_by_bridge[:10],
        }
