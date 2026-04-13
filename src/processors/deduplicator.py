"""跨源去重与记录合并。"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from rapidfuzz import fuzz

from src.utils.helpers import normalize_title, normalize_whitespace


class Deduplicator:
    """基于 DOI / arXiv / 标题相似度的轻量去重器。"""

    def __init__(self, title_threshold: int = 96):
        self.title_threshold = title_threshold

    def deduplicate(self, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
        merged: list[dict[str, Any]] = []
        for record in records:
            if not record.get("title"):
                continue
            existing_index = self._find_duplicate_index(merged, record)
            if existing_index is None:
                merged.append(deepcopy(record))
            else:
                merged[existing_index] = self.merge_records(merged[existing_index], record)
        return merged

    def merge_records(
        self,
        left: dict[str, Any],
        right: dict[str, Any],
    ) -> dict[str, Any]:
        merged = deepcopy(left)
        for field in [
            "title",
            "journal",
            "venue",
            "doi",
            "arxiv_id",
            "semantic_scholar_id",
            "openalex_id",
            "url",
            "pdf_url",
            "publication_date",
            "year",
        ]:
            if not merged.get(field) and right.get(field):
                merged[field] = right[field]

        if len(right.get("abstract", "")) > len(merged.get("abstract", "")):
            merged["abstract"] = right.get("abstract", "")

        merged["citation_count"] = max(
            int(merged.get("citation_count", 0) or 0),
            int(right.get("citation_count", 0) or 0),
        )
        merged["influential_citation_count"] = max(
            int(merged.get("influential_citation_count", 0) or 0),
            int(right.get("influential_citation_count", 0) or 0),
        )
        merged["relevance_score"] = max(
            float(merged.get("relevance_score", 0.0) or 0.0),
            float(right.get("relevance_score", 0.0) or 0.0),
        )
        merged["tier"] = max(int(merged.get("tier", 0) or 0), int(right.get("tier", 0) or 0))
        merged["is_seminal"] = bool(merged.get("is_seminal")) or bool(right.get("is_seminal"))

        merged["authors"] = self._merge_authors(merged.get("authors", []), right.get("authors", []))
        merged["topic_keys"] = sorted(
            set(merged.get("topic_keys", [])) | set(right.get("topic_keys", []))
        )

        sources = {item for item in self._split_sources(merged.get("source", ""))}
        sources.update(self._split_sources(right.get("source", "")))
        merged["source"] = ",".join(sorted(sources))
        return merged

    def _find_duplicate_index(
        self,
        existing: list[dict[str, Any]],
        candidate: dict[str, Any],
    ) -> int | None:
        candidate_title = normalize_title(candidate.get("title", ""))
        candidate_doi = (candidate.get("doi") or "").lower()
        candidate_arxiv = (candidate.get("arxiv_id") or "").lower()

        for index, record in enumerate(existing):
            if candidate_doi and candidate_doi == (record.get("doi") or "").lower():
                return index
            if candidate_arxiv and candidate_arxiv == (record.get("arxiv_id") or "").lower():
                return index

            record_title = normalize_title(record.get("title", ""))
            if not candidate_title or not record_title:
                continue
            if candidate_title == record_title:
                return index
            if fuzz.ratio(candidate_title, record_title) >= self.title_threshold:
                return index
        return None

    @staticmethod
    def _split_sources(value: str) -> list[str]:
        if not value:
            return []
        return [item.strip() for item in value.split(",") if item.strip()]

    @staticmethod
    def _normalize_author(author: Any) -> dict[str, str]:
        if isinstance(author, str):
            return {"name": normalize_whitespace(author), "affiliation": "", "openalex_id": "", "semantic_scholar_id": ""}
        if isinstance(author, dict):
            return {
                "name": normalize_whitespace(str(author.get("name", ""))),
                "affiliation": normalize_whitespace(str(author.get("affiliation", ""))),
                "openalex_id": normalize_whitespace(str(author.get("openalex_id", ""))),
                "semantic_scholar_id": normalize_whitespace(str(author.get("semantic_scholar_id", ""))),
            }
        return {"name": "", "affiliation": "", "openalex_id": "", "semantic_scholar_id": ""}

    @classmethod
    def _merge_authors(cls, left: list[Any], right: list[Any]) -> list[Any]:
        merged: dict[tuple[str, str], dict[str, str]] = {}
        for source in [left or [], right or []]:
            for author in source:
                payload = cls._normalize_author(author)
                if not payload["name"]:
                    continue
                key = (payload["name"].lower(), payload["affiliation"].lower())
                if key not in merged:
                    merged[key] = payload
                    continue
                merged[key]["openalex_id"] = merged[key]["openalex_id"] or payload["openalex_id"]
                merged[key]["semantic_scholar_id"] = (
                    merged[key]["semantic_scholar_id"] or payload["semantic_scholar_id"]
                )

        results = sorted(merged.values(), key=lambda item: (item["name"].lower(), item["affiliation"].lower()))
        if results and all(not item["affiliation"] and not item["openalex_id"] and not item["semantic_scholar_id"] for item in results):
            return [item["name"] for item in results]
        return results
