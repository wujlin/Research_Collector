"""OpenAlex 采集器。"""

from __future__ import annotations

from typing import Any

from src.utils.helpers import compact_abstract, parse_date

from .base import BaseCollector


class OpenAlexCollector(BaseCollector):
    def __init__(self, http_client=None):
        super().__init__("openalex", base_url="https://api.openalex.org/works", http_client=http_client)

    def collect(
        self,
        query: str = "",
        per_page: int = 20,
        year_from: int | None = None,
        **_: Any,
    ) -> list[dict[str, Any]]:
        params = {
            "search": query or "score-based diffusion non-equilibrium statistical physics",
            "per-page": per_page,
            "sort": "publication_date:desc",
        }
        if year_from:
            params["filter"] = f"from_publication_date:{year_from}-01-01"

        client = self._get_client()
        should_close = client is not self._client
        try:
            response = client.get(self.base_url, params=params, headers={"User-Agent": "ResearchCollector/0.1"})
            response.raise_for_status()
            payload = response.json()
        finally:
            if should_close:
                client.close()

        return [self._parse_item(item) for item in payload.get("results", [])]

    @staticmethod
    def _parse_item(item: dict[str, Any]) -> dict[str, Any]:
        publication_date = parse_date(item.get("publication_date"))
        source = ((item.get("primary_location") or {}).get("source") or {})
        doi = item.get("doi") or ""
        if doi.startswith("https://doi.org/"):
            doi = doi.removeprefix("https://doi.org/")

        return {
            "title": item.get("display_name", ""),
            "abstract": compact_abstract(_abstract_from_inverted_index(item.get("abstract_inverted_index"))),
            "authors": [
                authorship.get("author", {}).get("display_name", "").strip()
                for authorship in item.get("authorships", [])
                if authorship.get("author", {}).get("display_name")
            ],
            "year": item.get("publication_year"),
            "publication_date": publication_date.isoformat() if publication_date else "",
            "journal": source.get("display_name", ""),
            "venue": source.get("display_name", ""),
            "doi": doi,
            "openalex_id": item.get("id", "").rsplit("/", 1)[-1],
            "url": item.get("id", ""),
            "pdf_url": ((item.get("best_oa_location") or {}).get("pdf_url")) or "",
            "citation_count": item.get("cited_by_count", 0),
            "source": "openalex",
        }


def _abstract_from_inverted_index(inverted_index: dict[str, list[int]] | None) -> str:
    if not inverted_index:
        return ""
    size = max(max(positions) for positions in inverted_index.values()) + 1
    tokens = [""] * size
    for word, positions in inverted_index.items():
        for index in positions:
            tokens[index] = word
    return " ".join(token for token in tokens if token)
