"""arXiv 采集器。"""

from __future__ import annotations

import time
from typing import Any, Callable

import feedparser
import httpx

from src.utils.helpers import compact_abstract, load_config, parse_date

from .base import BaseCollector


class ArxivCollector(BaseCollector):
    def __init__(
        self,
        http_client=None,
        settings: dict[str, Any] | None = None,
        sleep_fn: Callable[[float], None] | None = None,
        clock_fn: Callable[[], float] | None = None,
    ):
        super().__init__("arxiv", base_url="https://export.arxiv.org/api/query", http_client=http_client)
        source_policy = (settings or load_config("settings.yaml")).get("collection", {}).get(
            "source_policies",
            {},
        ).get("arxiv", {})
        self.min_interval_seconds = float(source_policy.get("min_interval_seconds", 3.5))
        self.max_retries_on_429 = int(source_policy.get("max_retries_on_429", 2))
        self.base_backoff_seconds = float(source_policy.get("base_backoff_seconds", 8))
        self.sleep_fn = sleep_fn or time.sleep
        self.clock_fn = clock_fn or time.monotonic
        self._last_request_at: float | None = None

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
            response = self._request_with_backoff(client, params=params)
        finally:
            if should_close:
                client.close()

        feed = feedparser.parse(response.text)
        return [self._parse_entry(entry) for entry in feed.entries]

    def _request_with_backoff(
        self,
        client: httpx.Client,
        params: dict[str, Any],
    ) -> httpx.Response:
        last_error: httpx.HTTPStatusError | None = None
        for attempt in range(self.max_retries_on_429 + 1):
            self._respect_min_interval()
            response = client.get(self.base_url, params=params, headers={"User-Agent": "ResearchCollector/0.1"})
            self._last_request_at = self.clock_fn()
            if response.status_code == 429:
                last_error = httpx.HTTPStatusError(
                    "arXiv API rate limited the request.",
                    request=response.request,
                    response=response,
                )
                if attempt == self.max_retries_on_429:
                    break
                self.sleep_fn(self._backoff_seconds(response, attempt))
                continue

            response.raise_for_status()
            return response

        assert last_error is not None
        raise last_error

    def _respect_min_interval(self) -> None:
        if self._last_request_at is None or self.min_interval_seconds <= 0:
            return
        elapsed = self.clock_fn() - self._last_request_at
        if elapsed < self.min_interval_seconds:
            self.sleep_fn(self.min_interval_seconds - elapsed)

    def _backoff_seconds(self, response: httpx.Response, attempt: int) -> float:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return max(float(retry_after), 0.0)
            except ValueError:
                pass
        return self.base_backoff_seconds * (2 ** attempt)

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
