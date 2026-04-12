"""通用工具函数"""

from __future__ import annotations

import json
import os
import re
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

CANONICAL_DAILY_DIGEST_FILES: dict[str, str] = {
    "paper_queue": "paper-queue.md",
    "study_guide": "study-guide.md",
    "collection_review": "collection-review.md",
    "weekly": "weekly.md",
    "monthly": "monthly.md",
}


def get_project_root() -> Path:
    """获取项目根目录（通过向上查找 pyproject.toml）"""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "pyproject.toml").exists():
            return parent
    return Path.cwd()


def load_config(config_name: str) -> dict[str, Any]:
    """加载 config/ 目录下的 YAML 配置文件。"""
    config_path = get_project_root() / "config" / config_name
    with open(config_path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def get_env(key: str, default: str = "") -> str:
    """获取环境变量，自动加载 .env。"""
    load_dotenv(get_project_root() / ".env")
    return os.getenv(key, default)


def ensure_data_dirs() -> None:
    """确保项目输出目录存在。"""
    root = get_project_root()
    for relative in [
        "data",
        "data/cache",
        "digests",
        "digests/shared",
        "library",
        "pdfs",
        "youtube",
        "youtube/playlists",
        "youtube/notes",
        "youtube/slides",
        "youtube/transcripts",
        "knowledge_map",
        "web/public/generated",
    ]:
        (root / relative).mkdir(parents=True, exist_ok=True)


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_title(value: str) -> str:
    value = normalize_whitespace(value).lower()
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    return normalize_whitespace(value)


def slugify(value: str, max_length: int = 80) -> str:
    value = normalize_whitespace(value).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value[:max_length].rstrip("-")


def parse_date(value: Any) -> date | None:
    """宽松解析日期。"""
    if value is None or value == "":
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m", "%Y/%m", "%Y"):
        try:
            parsed = datetime.strptime(text, fmt)
            if fmt == "%Y":
                return date(parsed.year, 1, 1)
            if fmt in {"%Y-%m", "%Y/%m"}:
                return date(parsed.year, parsed.month, 1)
            return parsed.date()
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def parse_datetime(value: Any) -> datetime | None:
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime.combine(value, datetime.min.time())
    text = str(value).strip()
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        parsed = parse_date(text)
        if parsed is None:
            return None
        return datetime.combine(parsed, datetime.min.time())


def compact_abstract(text: str, limit: int = 1200) -> str:
    text = normalize_whitespace(text)
    return text[:limit].rstrip() if len(text) > limit else text


def utc_now() -> datetime:
    """返回去掉 tzinfo 的 UTC 时间戳，兼容 SQLite 的 DateTime 列。"""
    return datetime.now(UTC).replace(tzinfo=None)


def dump_json(path: Path | str, payload: Any) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False),
        encoding="utf-8",
    )


def dated_digest_dir(base_dir: Path | str, date_str: str) -> Path:
    return Path(base_dir) / date_str


def dated_digest_path(base_dir: Path | str, date_str: str, file_name: str) -> Path:
    return dated_digest_dir(base_dir, date_str) / file_name


def canonical_digest_path(base_dir: Path | str, date_str: str, digest_kind: str) -> Path:
    file_name = CANONICAL_DAILY_DIGEST_FILES.get(digest_kind)
    if not file_name:
        raise ValueError(f"Unknown digest kind: {digest_kind}")
    return dated_digest_path(base_dir, date_str, file_name)


def extract_date_prefix(path: Path | str) -> str:
    path_obj = Path(path)
    for candidate in [path_obj.parent.name, path_obj.name]:
        match = re.match(r"(?P<date>\d{4}-\d{2}-\d{2})", candidate)
        if match:
            return match.group("date")
    return ""


def flatten_topics(taxonomy: dict[str, Any]) -> list[dict[str, Any]]:
    """将 topics.yaml 递归扁平化为便于分类器和导出器使用的结构。"""
    entries: list[dict[str, Any]] = []

    def walk(
        node_key: str,
        node_data: dict[str, Any],
        parent_key: str | None,
        depth: int,
    ) -> None:
        children = node_data.get("subtopics", {})
        entries.append(
            {
                "key": node_key,
                "display_name": node_data["display_name"],
                "description": node_data.get("description", ""),
                "keywords": node_data.get("keywords", []),
                "parent_key": parent_key,
                "depth": depth,
                "is_leaf": not children,
            }
        )
        for child_key, child_data in children.items():
            walk(f"{node_key}/{child_key}", child_data, node_key, depth + 1)

    for root_key, root_data in taxonomy.items():
        walk(root_key, root_data, parent_key=None, depth=0)

    return entries


def build_topic_index(taxonomy: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """构建 topic key 到条目的索引。"""
    return {entry["key"]: entry for entry in flatten_topics(taxonomy)}


def get_topic_ancestor_keys(
    topic_key: str,
    topic_index: dict[str, dict[str, Any]],
) -> list[str]:
    """返回从近到远的祖先 key 列表。"""
    ancestors: list[str] = []
    current = topic_index.get(topic_key)
    while current and current.get("parent_key"):
        parent_key = current["parent_key"]
        ancestors.append(parent_key)
        current = topic_index.get(parent_key)
    return ancestors
