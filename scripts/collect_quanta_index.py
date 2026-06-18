#!/usr/bin/env python3
"""Collect a metadata-only index of Quanta Magazine articles.

The script intentionally does not mirror full article text. It uses Quanta's
robots.txt-advertised sitemap for URL discovery, then reads each public article
page in memory to extract structured metadata.
"""

from __future__ import annotations

import argparse
import csv
import html as html_lib
import json
import re
import sys
import time
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from xml.etree import ElementTree

import httpx


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


SITEMAP_URL = "https://www.quantamagazine.org/sitemap.xml"
ARCHIVE_URL = "https://www.quantamagazine.org/archive/"
DEFAULT_OUTPUT_DIR = ROOT / "data" / "quanta"
DEFAULT_USER_AGENT = "ResearchCollector/0.1 (+metadata-only; contact: local research index)"
ARTICLE_URL_RE = re.compile(r"^https://www\.quantamagazine\.org/(?P<slug>.+)-(?P<date>\d{8})/$")
JSON_LD_RE = re.compile(
    r"<script[^>]+type=[\"']application/ld\+json[\"'][^>]*>(?P<body>.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    no_tags = TAG_RE.sub(" ", value)
    return SPACE_RE.sub(" ", html_lib.unescape(no_tags)).strip()


def strip_quanta_suffix(title: str) -> str:
    return re.sub(r"\s*\|\s*Quanta Magazine\s*$", "", title).strip()


def fetch_text(client: httpx.Client, url: str, retries: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            response = client.get(url)
            response.raise_for_status()
            return response.text
        except Exception as exc:  # noqa: BLE001 - report final network failure cleanly
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}") from last_error


def sitemap_urls(xml_text: str) -> list[dict[str, str]]:
    root = ElementTree.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[dict[str, str]] = []
    for node in root.findall("sm:url", ns):
        loc = node.findtext("sm:loc", default="", namespaces=ns).strip()
        lastmod = node.findtext("sm:lastmod", default="", namespaces=ns).strip()
        match = ARTICLE_URL_RE.match(loc)
        if not match:
            continue
        urls.append(
            {
                "url": loc,
                "slug": match.group("slug"),
                "url_date": match.group("date"),
                "sitemap_lastmod": lastmod,
                "discovery_sources": ["sitemap"],
            }
        )
    return sorted(urls, key=lambda item: item["url_date"], reverse=True)


def seed_from_url(url: str, source: str) -> dict[str, Any] | None:
    match = ARTICLE_URL_RE.match(url)
    if not match:
        return None
    return {
        "url": url,
        "slug": match.group("slug"),
        "url_date": match.group("date"),
        "sitemap_lastmod": "",
        "discovery_sources": [source],
    }


def merge_seed(target: dict[str, dict[str, Any]], seed: dict[str, Any]) -> None:
    url = seed["url"]
    if url not in target:
        target[url] = dict(seed)
        return
    existing = target[url]
    if seed.get("sitemap_lastmod") and not existing.get("sitemap_lastmod"):
        existing["sitemap_lastmod"] = seed["sitemap_lastmod"]
    sources = list(existing.get("discovery_sources") or [])
    for source in seed.get("discovery_sources") or []:
        if source not in sources:
            sources.append(source)
    existing["discovery_sources"] = sources


def extract_article_urls(html: str) -> list[str]:
    urls: list[str] = []
    for match in re.finditer(r"href=[\"'](?P<href>[^\"']+-\d{8}/)[\"']", html):
        href = html_lib.unescape(match.group("href"))
        if href.startswith("/"):
            href = f"https://www.quantamagazine.org{href}"
        if ARTICLE_URL_RE.match(href):
            urls.append(href)
    return list(dict.fromkeys(urls))


def parse_archive_date(value: str, fallback_url_date: str) -> str:
    value = clean_text(value)
    if value:
        try:
            return datetime.strptime(value, "%B %d, %Y").date().isoformat()
        except ValueError:
            pass
    return iso_date_from_url_date(fallback_url_date)


def extract_first(pattern: str, text: str) -> str:
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return clean_text(match.group("body")) if match else ""


def extract_archive_records(html: str) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    starts = [match.start() for match in re.finditer(r"<div class='card clearfix", html)]
    starts.append(len(html))
    for start, end in zip(starts, starts[1:], strict=False):
        chunk = html[start:end]
        url_match = re.search(r"href=[\"'](?P<url>https://www\.quantamagazine\.org/[^\"']+-\d{8}/)[\"']", chunk)
        if not url_match:
            continue
        url = html_lib.unescape(url_match.group("url"))
        seed = seed_from_url(url, "archive")
        if not seed:
            continue
        title = extract_first(r"<h3[^>]+card__title[^>]*>(?P<body>.*?)</h3>", chunk)
        if not title:
            title = extract_first(r"<span[^>]+screen-reader-text[^>]*>(?P<body>.*?)</span>", chunk)
        kicker = extract_first(r"<div[^>]+card__kicker[^>]*>(?P<body>.*?)</div>", chunk)
        date_text = extract_first(r"<div[^>]+card-date[^>]*>.*?<div[^>]*>(?P<body>.*?)</div>", chunk)
        description = extract_first(r"<div[^>]+card__excerpt[^>]*>(?P<body>.*?)</div>", chunk)
        authors = extract_byline_authors(chunk)
        image_match = re.search(r"<img[^>]+src=[\"'](?P<src>[^\"']+)[\"']", chunk, re.IGNORECASE)
        image = html_lib.unescape(image_match.group("src")) if image_match else ""
        category, category_label = normalize_category(
            [],
            title=title,
            kicker=f"{kicker} {title} {description}",
        )
        records[url] = {
            "title": title or seed["slug"].replace("-", " ").title(),
            "url": url,
            "slug": seed["slug"],
            "url_date": seed["url_date"],
            "published": parse_archive_date(date_text, seed["url_date"]),
            "modified": "",
            "sitemap_lastmod": "",
            "discovery_sources": ["archive"],
            "publisher": "Quanta Magazine",
            "source_type": "web_article",
            "authors": authors,
            "category": category,
            "category_label": category_label,
            "kicker": kicker,
            "article_kind": kicker or category,
            "breadcrumbs": [],
            "description": description,
            "canonical": url,
            "image": image,
            "domain": urlparse(url).netloc,
            "metadata_source": "archive_card",
        }
    return records


def archive_urls(
    client: httpx.Client,
    archive_url: str = ARCHIVE_URL,
    max_pages: int = 0,
    delay: float = 0.05,
    records_by_url: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    seeds: dict[str, dict[str, Any]] = {}
    page = 1
    while True:
        if max_pages and page > max_pages:
            break
        url = archive_url if page == 1 else archive_url.rstrip("/") + f"/page/{page}/"
        response = client.get(url)
        if response.status_code == 404:
            break
        response.raise_for_status()
        page_urls = extract_article_urls(response.text)
        if not page_urls:
            break
        if records_by_url is not None:
            records_by_url.update(extract_archive_records(response.text))
        for article_url in page_urls:
            seed = seed_from_url(article_url, "archive")
            if seed:
                merge_seed(seeds, seed)
        if page % 25 == 0:
            print(f"Scanned archive page {page}; archive URLs={len(seeds)}", flush=True)
        page += 1
        if delay > 0:
            time.sleep(delay)
    print(f"Scanned archive pages through {page - 1}; archive URLs={len(seeds)}", flush=True)
    return sorted(seeds.values(), key=lambda item: item["url_date"], reverse=True)


def extract_meta(html: str, key: str, attr: str = "name") -> str:
    pattern = re.compile(
        rf"<meta\s+[^>]*{attr}=[\"']{re.escape(key)}[\"'][^>]*content=[\"'](?P<value>.*?)[\"'][^>]*>",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(html)
    if not match:
        pattern = re.compile(
            rf"<meta\s+[^>]*content=[\"'](?P<value>.*?)[\"'][^>]*{attr}=[\"']{re.escape(key)}[\"'][^>]*>",
            re.IGNORECASE | re.DOTALL,
        )
        match = pattern.search(html)
    return clean_text(match.group("value")) if match else ""


def extract_json_ld(html: str, url: str) -> dict[str, Any]:
    for match in JSON_LD_RE.finditer(html):
        body = html_lib.unescape(match.group("body")).strip()
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            continue
        candidates: list[dict[str, Any]] = []
        if isinstance(payload, dict):
            graph = payload.get("@graph")
            if isinstance(graph, list):
                candidates.extend(item for item in graph if isinstance(item, dict))
            candidates.append(payload)
        elif isinstance(payload, list):
            candidates.extend(item for item in payload if isinstance(item, dict))

        for item in candidates:
            item_url = str(item.get("url") or item.get("@id") or "")
            if item_url.rstrip("/") == url.rstrip("/") and (
                item.get("datePublished") or item.get("author") or item.get("breadcrumb")
            ):
                return item

        for item in candidates:
            if item.get("datePublished") or item.get("author"):
                return item
    return {}


def normalize_authors(author_field: Any) -> list[str]:
    authors: list[str] = []
    if isinstance(author_field, dict):
        name = clean_text(str(author_field.get("name", "")))
        if name:
            authors.append(name)
    elif isinstance(author_field, list):
        for item in author_field:
            if isinstance(item, dict):
                name = clean_text(str(item.get("name", "")))
            else:
                name = clean_text(str(item))
            if name:
                authors.append(name)
    elif isinstance(author_field, str):
        authors.append(clean_text(author_field))
    return list(dict.fromkeys(authors))


def breadcrumb_parts(item: dict[str, Any]) -> list[str]:
    breadcrumb = item.get("breadcrumb")
    elements: list[Any] = []
    if isinstance(breadcrumb, dict):
        elements = breadcrumb.get("itemListElement") or []
    parts: list[str] = []
    for element in elements:
        if not isinstance(element, dict):
            continue
        name = clean_text(str(element.get("name", "")))
        if name:
            parts.append(name)
    return parts


def infer_category_from_text(text: str) -> str:
    lowered = f" {text.lower()} "
    if any(
        token in lowered
        for token in [
            " computer",
            " algorithm",
            " cryptography",
            " artificial intelligence",
            " ai ",
            " machine learning",
            " complexity",
            " quantum computing",
        ]
    ):
        return "Computer Science"
    if any(
        token in lowered
        for token in [
            " math",
            " mathematical",
            " geometry",
            " number theory",
            " topology",
            " combinatorics",
            " algebra",
            " probability",
            " logic",
            " proof",
        ]
    ):
        return "Mathematics"
    if any(
        token in lowered
        for token in [
            " physics",
            " quantum",
            " cosmology",
            " particle",
            " black hole",
            " astrophysics",
            " astronomy",
            " condensed matter",
            " gravity",
            " earth science",
            " chemistry",
            " climate",
            " volcano",
        ]
    ):
        return "Physics"
    if any(
        token in lowered
        for token in [
            " biology",
            " evolution",
            " gene",
            " genomics",
            " genetics",
            " neuro",
            " neuroscience",
            " cell",
            " microbiology",
            " developmental biology",
            " origins of life",
            " ecology",
            " virus",
        ]
    ):
        return "Biology"
    return ""


def normalize_category(parts: list[str], title: str = "", kicker: str = "") -> tuple[str, str]:
    raw = parts[1] if len(parts) >= 2 else ""
    if raw and title and raw.strip().lower() == title.strip().lower():
        raw = ""
    for part in parts:
        lowered = part.lower()
        if "computer science" in lowered:
            return "Computer Science", raw
        if "mathematics" in lowered or "math news" in lowered:
            return "Mathematics", raw
        if "physics" in lowered:
            return "Physics", raw
        if "biology" in lowered:
            return "Biology", raw
    inferred = infer_category_from_text(kicker)
    if inferred:
        return inferred, raw
    return raw or "Uncategorized", raw


def iso_date_from_url_date(value: str) -> str:
    if len(value) != 8 or not value.isdigit():
        return ""
    return f"{value[:4]}-{value[4:6]}-{value[6:8]}"


def extract_kicker(html: str) -> str:
    match = re.search(
        r"<div[^>]+post__title__kicker[^>]*>(?P<body>.*?)</div>",
        html,
        re.IGNORECASE | re.DOTALL,
    )
    return clean_text(match.group("body")) if match else ""


def extract_byline_authors(html: str) -> list[str]:
    start = html.find("post__title__author-date")
    end = html.find("post__title__meta", start if start >= 0 else 0)
    scope = html[start:end] if start >= 0 and end > start else html
    authors = [
        clean_text(match.group("body"))
        for match in re.finditer(
            r"<span[^>]+class=[\"'][^\"']*byline__author[^\"']*[\"'][^>]*>(?P<body>.*?)</span>",
            scope,
            re.IGNORECASE | re.DOTALL,
        )
    ]
    return [author for author in dict.fromkeys(authors) if author]


def extract_link_rel(html: str, rel: str) -> str:
    pattern = re.compile(
        rf"<link\s+[^>]*rel=[\"']{re.escape(rel)}[\"'][^>]*href=[\"'](?P<value>.*?)[\"'][^>]*>",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(html)
    if not match:
        pattern = re.compile(
            rf"<link\s+[^>]*href=[\"'](?P<value>.*?)[\"'][^>]*rel=[\"']{re.escape(rel)}[\"'][^>]*>",
            re.IGNORECASE | re.DOTALL,
        )
        match = pattern.search(html)
    return clean_text(match.group("value")) if match else ""


def parse_article_html(html: str, seed: dict[str, str]) -> dict[str, Any]:
    url = seed["url"]
    item = extract_json_ld(html, url)
    breadcrumbs = breadcrumb_parts(item)
    title = strip_quanta_suffix(clean_text(str(item.get("name", ""))))
    if not title:
        title = strip_quanta_suffix(extract_meta(html, "og:title", attr="property"))
    if not title:
        title = seed["slug"].replace("-", " ").title()

    description = clean_text(str(item.get("description", "")))
    if not description:
        description = extract_meta(html, "description")
    if not description:
        description = extract_meta(html, "og:description", attr="property")

    published = clean_text(str(item.get("datePublished", "")))
    if not published:
        published = extract_meta(html, "article:published_time", attr="property")
    if not published:
        published = iso_date_from_url_date(seed.get("url_date", ""))
    modified = clean_text(str(item.get("dateModified", "")))
    if not modified:
        modified = seed.get("sitemap_lastmod", "")

    canonical = extract_link_rel(html, "canonical")
    og_image = extract_meta(html, "og:image", attr="property")
    kicker = extract_kicker(html)
    category, category_label = normalize_category(breadcrumbs, title=title, kicker=kicker)
    article_kind = kicker or category
    authors = normalize_authors(item.get("author"))
    html_authors = extract_byline_authors(html)
    if len(html_authors) > len(authors):
        authors = html_authors

    return {
        "title": title,
        "url": url,
        "slug": seed["slug"],
        "url_date": seed["url_date"],
        "published": published,
        "modified": modified,
        "sitemap_lastmod": seed.get("sitemap_lastmod", ""),
        "discovery_sources": seed.get("discovery_sources") or [],
        "publisher": "Quanta Magazine",
        "source_type": "web_article",
        "authors": authors,
        "category": category,
        "category_label": category_label,
        "kicker": kicker,
        "article_kind": article_kind,
        "breadcrumbs": breadcrumbs,
        "description": description,
        "canonical": canonical,
        "image": og_image,
        "domain": urlparse(url).netloc,
    }


def existing_digest_urls() -> dict[str, str]:
    mapping: dict[str, str] = {}
    digest_root = ROOT / "digests"
    if not digest_root.exists():
        return mapping
    url_re = re.compile(r"https://www\.quantamagazine\.org/[^\s)]+")
    for path in digest_root.rglob("*.md"):
        if "workflow" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in url_re.finditer(text):
            url = match.group(0).rstrip(".,\"'")
            rel = str(path.relative_to(ROOT))
            old = mapping.get(url)
            if old is None or ("workflow/" in old and "workflow/" not in rel):
                mapping[url] = rel
    return mapping


def normalize_record(
    record: dict[str, Any],
    seed: dict[str, Any] | None,
    digest_map: dict[str, str],
) -> dict[str, Any]:
    normalized = dict(record)
    url = normalized.get("url", "")
    if seed:
        normalized["slug"] = normalized.get("slug") or seed.get("slug", "")
        normalized["url_date"] = normalized.get("url_date") or seed.get("url_date", "")
        if seed.get("sitemap_lastmod") and not normalized.get("sitemap_lastmod"):
            normalized["sitemap_lastmod"] = seed.get("sitemap_lastmod", "")
        sources = list(normalized.get("discovery_sources") or [])
        for source in seed.get("discovery_sources") or []:
            if source not in sources:
                sources.append(source)
        normalized["discovery_sources"] = sources
    if not normalized.get("published"):
        normalized["published"] = iso_date_from_url_date(str(normalized.get("url_date") or ""))
    title = str(normalized.get("title") or "")
    category = str(normalized.get("category") or "")
    if (
        not category
        or category == "Uncategorized"
        or (title and category.strip().lower() == title.strip().lower())
    ):
        category, category_label = normalize_category(
            normalized.get("breadcrumbs") or [],
            title=title,
            kicker=f"{normalized.get('kicker') or ''} {title} {normalized.get('description') or ''}",
        )
        normalized["category"] = category
        if not normalized.get("category_label"):
            normalized["category_label"] = category_label
    normalized["local_digest"] = digest_map.get(url, normalized.get("local_digest", ""))
    return normalized


def read_existing_records(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if not isinstance(data, list):
        return {}
    records: dict[str, dict[str, Any]] = {}
    for item in data:
        if isinstance(item, dict) and isinstance(item.get("url"), str):
            records[item["url"]] = item
    return records


def write_json(path: Path, records: list[dict[str, Any]]) -> None:
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fields = [
        "title",
        "published",
        "authors",
        "category",
        "kicker",
        "description",
        "url",
        "local_digest",
        "sitemap_lastmod",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "title": record.get("title", ""),
                    "published": record.get("published", ""),
                    "authors": "; ".join(record.get("authors") or []),
                    "category": record.get("category", ""),
                    "kicker": record.get("kicker", ""),
                    "description": record.get("description", ""),
                    "url": record.get("url", ""),
                    "local_digest": record.get("local_digest", ""),
                    "sitemap_lastmod": record.get("sitemap_lastmod", ""),
                }
            )


def year_from_record(record: dict[str, Any]) -> str:
    published = str(record.get("published") or record.get("url_date") or "")
    return published[:4] if len(published) >= 4 else "unknown"


def write_markdown(path: Path, records: list[dict[str, Any]], collected_at: str) -> None:
    years = Counter(year_from_record(record) for record in records)
    categories = Counter(record.get("category") or "Uncategorized" for record in records)
    kinds = Counter(record.get("article_kind") or "Uncategorized" for record in records)
    lines: list[str] = [
        "---",
        'title: "Quanta Magazine Article Index"',
        'source_type: "web_article_index"',
        'publisher: "Quanta Magazine"',
        f'collected: "{collected_at}"',
        f"count: {len(records)}",
        "---",
        "",
        "# Quanta Magazine Article Index",
        "",
        "Metadata-only index collected from Quanta Magazine's public sitemap and archive cards.",
        "Full article text is not mirrored here.",
        "",
        "## Summary",
        "",
        f"- Total article-like dated URLs: {len(records)}",
        f"- Records with local digest already present: {sum(1 for r in records if r.get('local_digest'))}",
        "",
        "## By Year",
        "",
    ]
    for year, count in sorted(years.items(), reverse=True):
        lines.append(f"- {year}: {count}")
    lines.extend(["", "## By Main Category", ""])
    for category, count in categories.most_common():
        lines.append(f"- {category}: {count}")
    lines.extend(["", "## By Kicker / Article Kind", ""])
    for kind, count in kinds.most_common(30):
        lines.append(f"- {kind}: {count}")
    lines.extend(["", "## Articles", ""])
    for record in records:
        authors = "; ".join(record.get("authors") or [])
        published = str(record.get("published") or "")[:10]
        category = record.get("category") or ""
        kicker = record.get("kicker") or ""
        digest = record.get("local_digest") or ""
        description = record.get("description") or ""
        lines.append(f"### {record.get('title', '')}")
        lines.append("")
        lines.append(f"- URL: {record.get('url', '')}")
        if published:
            lines.append(f"- Published: {published}")
        if authors:
            lines.append(f"- Author(s): {authors}")
        if category:
            lines.append(f"- Category: {category}")
        if kicker and kicker != category:
            lines.append(f"- Kicker: {kicker}")
        if digest:
            lines.append(f"- Local digest: `{digest}`")
        if description:
            lines.append(f"- Description: {description}")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_workflow_note(path: Path, records: list[dict[str, Any]], collected_at: str) -> None:
    years = Counter(year_from_record(record) for record in records)
    categories = Counter(record.get("category") or "Uncategorized" for record in records)
    latest = records[:20]
    lines = [
        "---",
        'title: "Quanta Magazine Full-Site Metadata Collection"',
        'digest_type: "resource_index"',
        f'date: "{collected_at}"',
        "---",
        "",
        "# Quanta Magazine Full-Site Metadata Collection",
        "",
        "This is a metadata-only collection pass. It indexes URLs, titles, authors, dates, tags/categories and short descriptions; it does not mirror article bodies.",
        "",
        "## Artifacts",
        "",
        "- JSON: `data/quanta/quanta_articles.json`",
        "- CSV: `data/quanta/quanta_articles.csv`",
        "- Markdown index: `data/quanta/quanta_index.md`",
        "",
        "## Summary",
        "",
        f"- Total article-like dated URLs: {len(records)}",
        f"- Existing local digests matched: {sum(1 for r in records if r.get('local_digest'))}",
        f"- Year range: {min(years) if years else 'n/a'}-{max(years) if years else 'n/a'}",
        "",
        "## Main Categories",
        "",
    ]
    for category, count in categories.most_common():
        lines.append(f"- {category}: {count}")
    lines.extend(["", "## Latest 20", ""])
    for record in latest:
        title = record.get("title", "")
        url = record.get("url", "")
        published = str(record.get("published") or "")[:10]
        category = record.get("category") or ""
        lines.append(f"- {published} | {category} | [{title}]({url})")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect Quanta Magazine metadata index")
    parser.add_argument("--sitemap-url", default=SITEMAP_URL)
    parser.add_argument("--archive-url", default=ARCHIVE_URL)
    parser.add_argument(
        "--discovery",
        choices=["sitemap", "archive", "both"],
        default="both",
        help="URL discovery source",
    )
    parser.add_argument("--max-archive-pages", type=int, default=0)
    parser.add_argument("--archive-delay", type=float, default=0.05)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--limit", type=int, default=0, help="Only fetch first N article URLs")
    parser.add_argument("--delay", type=float, default=0.2, help="Delay between article requests")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--refresh", action="store_true", help="Re-fetch records already in JSON")
    parser.add_argument(
        "--fetch-detail-pages",
        action="store_true",
        help="Fetch every article page to enrich archive-card metadata",
    )
    parser.add_argument("--no-workflow-note", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "quanta_articles.json"
    csv_path = output_dir / "quanta_articles.csv"
    md_path = output_dir / "quanta_index.md"
    log_path = output_dir / "quanta_collection_errors.json"
    existing = read_existing_records(json_path)
    digest_map = existing_digest_urls()
    collected_at = datetime.now(UTC).date().isoformat()

    headers = {"User-Agent": DEFAULT_USER_AGENT}
    timeout = httpx.Timeout(args.timeout, connect=10.0)
    limits = httpx.Limits(max_keepalive_connections=4, max_connections=8)
    records_by_url: dict[str, dict[str, Any]] = {}
    archive_record_cache: dict[str, dict[str, Any]] = {}
    errors: list[dict[str, str]] = []

    with httpx.Client(
        headers=headers,
        timeout=timeout,
        follow_redirects=True,
        trust_env=False,
        limits=limits,
    ) as client:
        seeds_by_url: dict[str, dict[str, Any]] = {}
        if args.discovery in {"sitemap", "both"}:
            sitemap_text = fetch_text(client, args.sitemap_url)
            for seed in sitemap_urls(sitemap_text):
                merge_seed(seeds_by_url, seed)
        if args.discovery in {"archive", "both"}:
            for seed in archive_urls(
                client,
                archive_url=args.archive_url,
                max_pages=args.max_archive_pages,
                delay=args.archive_delay,
                records_by_url=archive_record_cache,
            ):
                merge_seed(seeds_by_url, seed)
        seeds = sorted(seeds_by_url.values(), key=lambda item: item["url_date"], reverse=True)
        if args.limit:
            seeds = seeds[: args.limit]
        total = len(seeds)
        print(f"Discovered {total} article-like dated URLs")

        for index, seed in enumerate(seeds, start=1):
            url = seed["url"]
            if not args.refresh and url in existing:
                record = normalize_record(existing[url], seed, digest_map)
                records_by_url[url] = record
                continue
            if not args.fetch_detail_pages and url in archive_record_cache:
                record = normalize_record(archive_record_cache[url], seed, digest_map)
                record["collected_at"] = collected_at
                records_by_url[url] = record
                if index % 50 == 0 or index == total:
                    print(f"Fetched/loaded {index}/{total}; errors={len(errors)}")
                continue
            try:
                html = fetch_text(client, url)
                record = parse_article_html(html, seed)
                record["collected_at"] = collected_at
                record = normalize_record(record, seed, digest_map)
                records_by_url[url] = record
            except Exception as exc:  # noqa: BLE001 - keep the long run moving
                errors.append({"url": url, "error": str(exc)})
            if index % 50 == 0 or index == total:
                print(f"Fetched/loaded {index}/{total}; errors={len(errors)}")
            if args.delay > 0:
                time.sleep(args.delay)

    ordered = sorted(
        records_by_url.values(),
        key=lambda record: (str(record.get("published") or ""), str(record.get("url_date") or "")),
        reverse=True,
    )
    write_json(json_path, ordered)
    write_csv(csv_path, ordered)
    write_markdown(md_path, ordered, collected_at)
    write_json(log_path, errors)
    if not args.no_workflow_note:
        workflow_path = ROOT / "digests" / collected_at / "workflow" / "quanta-resource-index.md"
        write_workflow_note(workflow_path, ordered, collected_at)

    summary = {
        "records": len(ordered),
        "errors": len(errors),
        "json": str(json_path.relative_to(ROOT)),
        "csv": str(csv_path.relative_to(ROOT)),
        "markdown": str(md_path.relative_to(ROOT)),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
