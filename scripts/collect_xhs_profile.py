#!/usr/bin/env python3
"""Collect research-resource leads from a Xiaohongshu profile.

This script uses ordinary browser automation with a user-provided cookie export.
It intentionally avoids API signing, CAPTCHA bypassing, or anti-bot evasion.
Raw captured post text is written under data/social/, which is ignored by git.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_COOKIES = ROOT / ".secrets" / "xhs_cookies.json"
DEFAULT_USER_DATA_DIR = ROOT / ".secrets" / "xhs_chromium_profile"
DEFAULT_OUTPUT_ROOT = ROOT / "data" / "social" / "xiaohongshu"

URL_RE = re.compile(r"https?://[^\s\])}>\"'，。；、]+", re.IGNORECASE)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
ARXIV_RE = re.compile(r"\barXiv\s*[:：]?\s*(\d{4}\.\d{4,5}(?:v\d+)?)\b", re.IGNORECASE)


def slugify(value: str, fallback: str = "item") -> str:
    value = value.strip().lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or fallback


def strip_tracking_query(url: str) -> str:
    """Drop volatile Xiaohongshu query parameters while keeping stable note IDs."""

    parts = urlsplit(url)
    if not parts.scheme:
        return url
    # Keep no xhs query by default. Most xsec_* params are session-like and expire.
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def normalize_url(url: str, base_url: str) -> str:
    absolute = urljoin(base_url, url)
    return strip_tracking_query(absolute)


def extract_note_id(url: str) -> str:
    parts = [part for part in urlsplit(url).path.split("/") if part]
    if len(parts) >= 2 and parts[0] in {"explore", "discovery"}:
        return parts[-1]
    if len(parts) >= 4 and parts[0] == "user" and parts[1] == "profile":
        return parts[3]
    return ""


def load_cookies(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Cookie file must contain a JSON list: {path}")

    cookies: list[dict[str, Any]] = []
    for item in payload:
        if not isinstance(item, dict) or not item.get("name") or "value" not in item:
            continue
        cookie: dict[str, Any] = {
            "name": item["name"],
            "value": item["value"],
            "domain": item.get("domain") or ".xiaohongshu.com",
            "path": item.get("path") or "/",
            "httpOnly": bool(item.get("httpOnly", False)),
            "secure": bool(item.get("secure", False)),
        }
        same_site = item.get("sameSite")
        if isinstance(same_site, str) and same_site.lower() in {"strict", "lax", "none"}:
            cookie["sameSite"] = same_site.capitalize()

        expires = item.get("expirationDate")
        if expires and not item.get("session"):
            try:
                cookie["expires"] = float(expires)
            except (TypeError, ValueError):
                pass
        cookies.append(cookie)
    return cookies


def extract_resource_candidates(text: str) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for match in URL_RE.finditer(text):
        value = match.group(0).rstrip(".,;:，。；：)")
        key = ("url", value)
        if key not in seen:
            candidates.append({"type": "url", "value": value})
            seen.add(key)

    for match in DOI_RE.finditer(text):
        value = match.group(0).rstrip(".,;:，。；：)")
        key = ("doi", value.lower())
        if key not in seen:
            candidates.append({"type": "doi", "value": value, "url": f"https://doi.org/{value}"})
            seen.add(key)

    for match in ARXIV_RE.finditer(text):
        value = match.group(1)
        key = ("arxiv", value.lower())
        if key not in seen:
            candidates.append(
                {"type": "arxiv", "value": value, "url": f"https://arxiv.org/abs/{value}"}
            )
            seen.add(key)
    return candidates


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_resource_markdown(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Xiaohongshu Resource Candidates",
        "",
        "这些条目是从帖子可见文本中自动提取的线索，"
        "不等于已确认资源。",
        "",
    ]
    total = 0
    for row in rows:
        candidates = row.get("resource_candidates") or []
        if not candidates:
            continue
        total += len(candidates)
        title = row.get("title") or row.get("card_title") or row.get("note_id") or "untitled"
        lines.extend(
            [
                f"## {title}",
                "",
                f"- 原帖：{row.get('post_url', '')}",
                f"- 采集时间：{row.get('collected_at', '')}",
                "",
            ]
        )
        for candidate in candidates:
            label = candidate.get("type", "item")
            value = candidate.get("url") or candidate.get("value", "")
            lines.append(f"- `{label}` {value}")
        lines.append("")

    if total == 0:
        lines.append("本轮没有从可见文本中自动识别出 URL/DOI/arXiv 线索。")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def collect_profile_cards(
    page: Any,
    profile_url: str,
    max_notes: int,
    scrolls: int,
    pause_ms: int,
    manual_login_seconds: int = 0,
) -> list[dict[str, Any]]:
    page.goto(profile_url, wait_until="domcontentloaded", timeout=60_000)
    page.wait_for_timeout(4_000)
    if manual_login_seconds > 0:
        print(f"Manual login window open for {manual_login_seconds}s.", file=sys.stderr)
        page.wait_for_timeout(manual_login_seconds * 1000)

    cards: dict[str, dict[str, Any]] = {}
    for _ in range(scrolls + 1):
        found = page.evaluate(
            """
            () => Array.from(document.querySelectorAll(
                [
                  'a[href*="/explore/"]',
                  'a[href*="/discovery/item/"]',
                  'a[href*="/user/profile/"]',
                ].join(',')
              ))
              .map((a) => {
                const href = a.getAttribute('href') || '';
                const img = a.querySelector('img');
                const text = (
                  a.innerText || a.getAttribute('title') || img?.getAttribute('alt') || ''
                ).trim();
                const rect = a.getBoundingClientRect();
                return {
                  href,
                  text,
                  image: img?.currentSrc || img?.src || '',
                  area: Math.round(rect.width * rect.height),
                };
              })
              .filter((x) => x.href && (x.area > 2000 || x.text))
            """
        )
        for item in found:
            url = normalize_url(item["href"], profile_url)
            note_id = extract_note_id(url)
            if not note_id:
                continue
            existing = cards.setdefault(
                note_id,
                {
                    "post_url": url,
                    "_open_url": urljoin(profile_url, item["href"]),
                    "note_id": note_id,
                    "card_title": " ".join((item.get("text") or "").split())[:300],
                    "cover_image": item.get("image") or "",
                },
            )
            text = " ".join((item.get("text") or "").split())[:300]
            if text and (not existing.get("card_title") or len(text) > len(existing["card_title"])):
                existing["card_title"] = text
            if item.get("image") and not existing.get("cover_image"):
                existing["cover_image"] = item["image"]
            if item.get("href") and "xsec_token=" in item["href"]:
                existing["_open_url"] = urljoin(profile_url, item["href"])
        if len(cards) >= max_notes:
            break
        page.mouse.wheel(0, 1800)
        page.wait_for_timeout(pause_ms)

    return list(cards.values())[:max_notes]


def extract_note_detail(context: Any, card: dict[str, Any], pause_ms: int) -> dict[str, Any]:
    post_url = card.get("_open_url") or card["post_url"]
    page = context.new_page()
    try:
        page.goto(post_url, wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_timeout(pause_ms)
        detail = page.evaluate(
            """
            () => {
              const title =
                document.querySelector('h1')?.innerText ||
                document.querySelector('[class*="title"]')?.innerText ||
                document.title ||
                '';
              const body = document.body?.innerText || '';
              const published =
                document.querySelector('time')?.getAttribute('datetime') ||
                document.querySelector('time')?.innerText ||
                '';
              return {
                title: title.trim(),
                visible_text: body.trim(),
                published_at_text: published.trim(),
              };
            }
            """
        )
    finally:
        page.close()

    text = detail.get("visible_text") or ""
    return {
        **{key: value for key, value in card.items() if not key.startswith("_")},
        "title": " ".join((detail.get("title") or card.get("card_title") or "").split())[:300],
        "published_at_text": detail.get("published_at_text", ""),
        "visible_text": text,
        "resource_candidates": extract_resource_candidates(text),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect visible Xiaohongshu profile posts as research leads."
    )
    parser.add_argument("--profile-url", required=True, help="Xiaohongshu profile URL.")
    parser.add_argument("--source-name", default="tabris", help="Stable local source slug.")
    parser.add_argument(
        "--cookies",
        type=Path,
        default=DEFAULT_COOKIES,
        help="Cookie JSON export path.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Output root directory.",
    )
    parser.add_argument("--max-notes", type=int, default=30, help="Maximum notes to collect.")
    parser.add_argument(
        "--scrolls",
        type=int,
        default=10,
        help="Number of profile-page scroll rounds.",
    )
    parser.add_argument("--pause-ms", type=int, default=2500, help="Delay between browser actions.")
    parser.add_argument("--headful", action="store_true", help="Show browser window.")
    parser.add_argument(
        "--manual-login-seconds",
        type=int,
        default=0,
        help="Keep the browser open for manual login before collecting cards.",
    )
    parser.add_argument(
        "--user-data-dir",
        type=Path,
        default=None,
        help="Persistent browser profile directory. Prefer .secrets/xhs_chromium_profile.",
    )
    parser.add_argument(
        "--no-detail",
        action="store_true",
        help="Only collect profile cards, without opening notes.",
    )
    parser.add_argument(
        "--debug-screenshot",
        action="store_true",
        help="Save a screenshot after profile load.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    uses_persistent_profile = args.user_data_dir is not None
    if not args.cookies.exists() and args.manual_login_seconds <= 0 and not uses_persistent_profile:
        raise SystemExit(
            f"Cookie file not found: {args.cookies}\n"
            "Create .secrets/xhs_cookies.json from your browser cookie export first, "
            "or run with --headful --manual-login-seconds 120 "
            f"--user-data-dir {DEFAULT_USER_DATA_DIR}."
        )

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit(
            "Playwright is not installed. Run:\n"
            '  python -m pip install -e ".[social]"\n'
            "  python -m playwright install chromium"
        ) from exc

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = args.output_root / slugify(args.source_name) / timestamp
    debug_dir = output_dir / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)

    cookies = load_cookies(args.cookies) if args.cookies.exists() else []
    rows: list[dict[str, Any]] = []
    collected_at = datetime.now().isoformat(timespec="seconds")

    with sync_playwright() as p:
        browser = None
        if uses_persistent_profile:
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(args.user_data_dir),
                headless=not args.headful,
                locale="zh-CN",
                timezone_id="Asia/Shanghai",
            )
        else:
            browser = p.chromium.launch(headless=not args.headful)
            context = browser.new_context(locale="zh-CN", timezone_id="Asia/Shanghai")
        if cookies:
            context.add_cookies(cookies)
        page = context.new_page()
        try:
            cards = collect_profile_cards(
                page=page,
                profile_url=args.profile_url,
                max_notes=args.max_notes,
                scrolls=args.scrolls,
                pause_ms=args.pause_ms,
                manual_login_seconds=args.manual_login_seconds,
            )
            if args.debug_screenshot:
                page.screenshot(path=debug_dir / "profile_loaded.png", full_page=True)

            if not cards:
                page.screenshot(path=debug_dir / "blocked_or_login.png", full_page=True)
                raise SystemExit(
                    "No note cards found. Cookie may be expired, "
                    "the page may require manual login, "
                    f"or the DOM changed. See {debug_dir / 'blocked_or_login.png'}"
                )

            for index, card in enumerate(cards, start=1):
                row = card
                if not args.no_detail:
                    row = extract_note_detail(context, card, pause_ms=args.pause_ms)
                    time.sleep(max(args.pause_ms / 1000.0, 1.0))
                row.update(
                    {
                        "source": "xiaohongshu",
                        "source_name": args.source_name,
                        "profile_url": strip_tracking_query(args.profile_url),
                        "collected_at": collected_at,
                        "sequence": index,
                    }
                )
                row = {key: value for key, value in row.items() if not key.startswith("_")}
                rows.append(row)
        finally:
            context.close()
            if browser is not None:
                browser.close()

    write_jsonl(output_dir / "notes.jsonl", rows)
    write_resource_markdown(output_dir / "resource_candidates.md", rows)
    summary = {
        "source": "xiaohongshu",
        "source_name": args.source_name,
        "profile_url": strip_tracking_query(args.profile_url),
        "collected_at": collected_at,
        "output_dir": str(output_dir),
        "note_count": len(rows),
        "resource_candidate_count": sum(len(row.get("resource_candidates") or []) for row in rows),
        "no_detail": args.no_detail,
    }
    (output_dir / "run_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
