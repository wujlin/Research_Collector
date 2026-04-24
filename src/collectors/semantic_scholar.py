"""Semantic Scholar 采集器。"""

from __future__ import annotations

import time
from typing import Any, Callable

import httpx

from src.utils.helpers import compact_abstract, get_env, load_config, parse_date

from .base import BaseCollector


class SemanticScholarCollector(BaseCollector):
    def __init__(
        self,
        http_client=None,
        settings: dict[str, Any] | None = None,
        sleep_fn: Callable[[float], None] | None = None,
        clock_fn: Callable[[], float] | None = None,
    ):
        super().__init__(
            "semantic_scholar",
            base_url="https://api.semanticscholar.org/graph/v1/paper/search",
            http_client=http_client,
        )
        source_policy = (settings or load_config("settings.yaml")).get("collection", {}).get(
            "source_policies",
            {},
        ).get("semantic_scholar", {})
        self.use_in_all_runs_without_api_key = bool(
            source_policy.get("use_in_all_runs_without_api_key", False)
        )
        self.min_interval_seconds = float(source_policy.get("min_interval_seconds", 1.1))
        self.max_retries_on_429 = int(source_policy.get("max_retries_on_429", 2))
        self.base_backoff_seconds = float(source_policy.get("base_backoff_seconds", 4))
        self.limit_without_api_key = int(source_policy.get("limit_without_api_key", 10))
        self.sleep_fn = sleep_fn or time.sleep
        self.clock_fn = clock_fn or time.monotonic
        self._last_request_at: float | None = None

    def has_api_key(self) -> bool:
        return bool(get_env("SEMANTIC_SCHOLAR_API_KEY"))

    def should_skip_default_run(self) -> bool:
        return not self.has_api_key() and not self.use_in_all_runs_without_api_key

    def collect(
        self,
        query: str = "",
        limit: int = 20,
        year_from: int | None = None,
        **_: Any,
    ) -> list[dict[str, Any]]:
        api_key = get_env("SEMANTIC_SCHOLAR_API_KEY")
        headers = {"User-Agent": "ResearchCollector/0.1"}
        if api_key:
            headers["x-api-key"] = api_key
        else:
            limit = min(limit, self.limit_without_api_key)

        params = {
            "query": query or "non-equilibrium statistical mechanics generative modeling",
            "limit": limit,
            "fields": (
                "paperId,title,abstract,year,authors,venue,journal,url,externalIds,"
                "citationCount,influentialCitationCount,publicationDate"
            ),
        }
        if year_from:
            params["year"] = f"{year_from}-"

        client = self._get_client()
        should_close = client is not self._client
        try:
            payload = self._request_with_backoff(client, params=params, headers=headers)
        finally:
            if should_close:
                client.close()

        return [self._parse_item(item) for item in payload.get("data", [])]

    def _request_with_backoff(
        self,
        client: httpx.Client,
        params: dict[str, Any],
        headers: dict[str, str],
    ) -> dict[str, Any]:
        last_error: httpx.HTTPStatusError | None = None
        for attempt in range(self.max_retries_on_429 + 1):
            self._respect_min_interval()
            response = client.get(self.base_url, params=params, headers=headers)
            self._last_request_at = self.clock_fn()
            if response.status_code == 429:
                last_error = httpx.HTTPStatusError(
                    "Semantic Scholar API rate limited the request.",
                    request=response.request,
                    response=response,
                )
                if attempt == self.max_retries_on_429:
                    break
                self.sleep_fn(self._backoff_seconds(response, attempt))
                continue

            response.raise_for_status()
            return response.json()

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
    def _parse_item(item: dict[str, Any]) -> dict[str, Any]:
        external_ids = item.get("externalIds") or {}
        publication_date = parse_date(item.get("publicationDate"))
        journal = ""
        if item.get("journal"):
            journal = item["journal"].get("name", "")

        return {
            "title": item.get("title", ""),
            "abstract": compact_abstract(item.get("abstract", "")),
            "authors": [author.get("name", "").strip() for author in item.get("authors", [])],
            "year": item.get("year"),
            "publication_date": publication_date.isoformat() if publication_date else "",
            "journal": journal,
            "venue": item.get("venue", ""),
            "doi": external_ids.get("DOI"),
            "arxiv_id": external_ids.get("ArXiv"),
            "semantic_scholar_id": item.get("paperId"),
            "url": item.get("url", ""),
            "citation_count": item.get("citationCount", 0),
            "influential_citation_count": item.get("influentialCitationCount", 0),
            "source": "semantic_scholar",
        }
