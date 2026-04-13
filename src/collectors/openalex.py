"""OpenAlex 采集器。"""

from __future__ import annotations

from typing import Any

from src.utils.helpers import compact_abstract, get_env, parse_date

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
        api_key = get_env("OPENALEX_API_KEY")
        params = {
            "search": query or "score-based diffusion non-equilibrium statistical physics",
            "per-page": per_page,
            "sort": "publication_date:desc",
        }
        if api_key:
            params["api_key"] = api_key
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
            "authors": _parse_authors(item.get("authorships", [])),
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


def _parse_authors(authorships: list[dict[str, Any]]) -> list[dict[str, str]]:
    authors: list[dict[str, str]] = []
    for authorship in authorships:
        author = authorship.get("author", {}) or {}
        name = (author.get("display_name") or "").strip()
        if not name:
            continue

        institutions = authorship.get("institutions", []) or []
        institution_names = [
            (institution.get("display_name") or "").strip()
            for institution in institutions
            if (institution.get("display_name") or "").strip()
        ]
        raw_affiliations = [
            value.strip()
            for value in (authorship.get("raw_affiliation_strings") or [])
            if isinstance(value, str) and value.strip()
        ]
        affiliation_values = institution_names or raw_affiliations
        seen: set[str] = set()
        affiliation_parts: list[str] = []
        for value in affiliation_values:
            lowered = value.lower()
            if lowered in seen:
                continue
            seen.add(lowered)
            affiliation_parts.append(value)
        affiliation = "; ".join(affiliation_parts[:2])

        openalex_id = (author.get("id") or "").rsplit("/", 1)[-1]
        payload = {
            "name": name,
            "affiliation": affiliation,
        }
        if openalex_id:
            payload["openalex_id"] = openalex_id
        authors.append(payload)
    return authors
