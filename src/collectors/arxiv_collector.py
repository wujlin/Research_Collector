"""arXiv 采集器。"""

from __future__ import annotations

from typing import Any

import feedparser

from src.utils.helpers import compact_abstract, load_config, parse_date

from .base import BaseCollector


class ArxivCollector(BaseCollector):
    def __init__(self, http_client=None):
        super().__init__("arxiv", base_url="https://export.arxiv.org/api/query", http_client=http_client)

    def collect(
        self,
        query: str = "",
        max_results: int = 25,
        categories: list[str] | None = None,
        sort_by: str = "submittedDate",
        sort_order: str = "descending",
        **_: Any,
    ) -> list[dict[str, Any]]:
        categories = categories or load_config("sources.yaml").get("arxiv_categories", [])
        search_query = self._build_search_query(query, categories)
        params = {
            "search_query": search_query,
            "start": 0,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }

        client = self._get_client()
        should_close = client is not self._client
        try:
            response = client.get(self.base_url, params=params, headers={"User-Agent": "ResearchCollector/0.1"})
            response.raise_for_status()
        finally:
            if should_close:
                client.close()

        feed = feedparser.parse(response.text)
        return [self._parse_entry(entry) for entry in feed.entries]

    @staticmethod
    def _build_search_query(query: str, categories: list[str]) -> str:
        category_query = " OR ".join(f"cat:{category}" for category in categories) if categories else ""
        term_query = f'all:"{query}"' if query else ""
        if category_query and term_query:
            return f"({category_query}) AND {term_query}"
        return category_query or term_query or 'all:"stochastic process"'

    @staticmethod
    def _parse_entry(entry: Any) -> dict[str, Any]:
        published = parse_date(entry.get("published"))
        arxiv_id = entry.get("id", "").rsplit("/", 1)[-1]
        arxiv_id = arxiv_id.split("v", 1)[0]
        pdf_url = ""
        for link in entry.get("links", []):
            if link.get("type") == "application/pdf":
                pdf_url = link.get("href", "")

        return {
            "title": entry.get("title", "").replace("\n", " ").strip(),
            "abstract": compact_abstract(entry.get("summary", "")),
            "authors": [author.get("name", "").strip() for author in entry.get("authors", [])],
            "year": published.year if published else None,
            "publication_date": published.isoformat() if published else "",
            "journal": entry.get("arxiv_journal_ref", "") or "arXiv",
            "venue": "arXiv",
            "doi": entry.get("arxiv_doi"),
            "arxiv_id": arxiv_id,
            "url": entry.get("id", ""),
            "pdf_url": pdf_url,
            "source": "arxiv",
        }
