"""论文相关性与层级评分。"""

from __future__ import annotations

import math
import re
from typing import Any

from src.utils.helpers import load_config, normalize_whitespace, utc_now

_STRIP_PUNCT_RE = re.compile(r"[^a-z0-9\s]")
_VOLUME_SUFFIX_RE = re.compile(
    r"[,\s]+\d{1,4}\s*[\(,].*$"    # "Physical Review E, 101, 022129 (2020)" → strip from ",101..."
    r"|[,\s]+\d{1,4}\s*$"           # trailing volume number
    r"|\s*\([\d\-]+\)\s*\d*\s*$"    # trailing "(2025)" or "(2025) 053210"
)
_PREPRINT_HOSTS = frozenset([
    "arxiv", "arxiv.org", "arxiv (cornell university)",
    "biorxiv", "biorxiv (cold spring harbor laboratory)",
    "chemrxiv", "medrxiv", "ssrn", "preprints.org",
    "zenodo", "zenodo (cern european organization for nuclear research)",
    "hal", "spire - sciences po institutional repository",
])


def _normalize_venue(name: str) -> str:
    """统一 venue 名称：去标点、压空白、小写。"""
    name = normalize_whitespace(name).lower()
    name = _STRIP_PUNCT_RE.sub(" ", name)
    return normalize_whitespace(name)


class RelevanceScorer:
    def __init__(self, sources_config: str = "sources.yaml"):
        self.sources_config = load_config(sources_config)
        self._journal_index = self._build_journal_index(self.sources_config["journal_tiers"])

    def score_record(self, record: dict[str, Any]) -> dict[str, Any]:
        tier_level, tier_weight = self._match_tier(record)
        citation_count = int(record.get("citation_count", 0) or 0)
        influential_count = int(record.get("influential_citation_count", 0) or 0)
        year = int(record.get("year", 0) or 0)
        topic_count = len(record.get("topic_keys", []))
        abstract_length = len(record.get("abstract", "") or "")

        age = max(0, utc_now().year - year) if year else 12
        recency_score = max(0.0, 24 - min(age, 12) * 2)
        citation_score = min(24.0, math.log10(citation_count + 1) * 10.0)
        influence_score = min(12.0, math.log10(influential_count + 1) * 8.0)
        topic_score = min(18.0, topic_count * 5.0)
        abstract_score = min(8.0, abstract_length / 120.0)
        seminal_bonus = 10.0 if record.get("is_seminal") else 0.0
        preprint_bonus = 4.0 if record.get("source") == "arxiv" and age <= 2 else 0.0
        tier_score = float(tier_weight) * 2.0

        record["tier"] = tier_level
        record["tier_weight"] = tier_weight
        record["venue_quality"] = self.describe_venue_quality(record, tier_level)
        record["relevance_score"] = round(
            min(
                100.0,
                recency_score
                + citation_score
                + influence_score
                + topic_score
                + abstract_score
                + tier_score
                + seminal_bonus
                + preprint_bonus,
            ),
            2,
        )
        return record

    @staticmethod
    def describe_venue_quality(record: dict[str, Any], tier_level: int) -> str:
        journal = normalize_whitespace(record.get("journal", "")).lower()
        venue = normalize_whitespace(record.get("venue", "")).lower()
        source = normalize_whitespace(record.get("source", "")).lower()
        norm_journal = _normalize_venue(journal)
        norm_venue = _normalize_venue(venue)
        if source == "arxiv" or norm_journal in _PREPRINT_HOSTS or norm_venue in _PREPRINT_HOSTS:
            if tier_level >= 1:
                # arXiv 论文已正式发表在已知期刊，按期刊 tier 判定
                if tier_level == 1:
                    return "top_tier"
                if tier_level == 2:
                    return "high_quality"
                return "solid_domain"
            return "preprint"
        if tier_level == 1:
            return "top_tier"
        if tier_level == 2:
            return "high_quality"
        if tier_level == 3:
            return "solid_domain"
        return "unranked"

    def _match_tier(self, record: dict[str, Any]) -> tuple[int, int]:
        raw_journal = normalize_whitespace(record.get("journal", "")).lower()
        raw_venue = normalize_whitespace(record.get("venue", "")).lower()
        norm_journal = _normalize_venue(raw_journal)
        norm_venue = _normalize_venue(raw_venue)

        # 优先对 journal 做全策略匹配（精确→归一化→剥离卷号），
        # 这样 arXiv 论文的 journal_ref 能正确识别出已发表期刊 tier，
        # 而不会被 venue="arXiv" 的预印本 tier 抢先命中。
        best: tuple[int, int] | None = None
        for raw, norm in ((raw_journal, norm_journal), (raw_venue, norm_venue)):
            # 精确匹配
            if raw and raw in self._journal_index:
                hit = self._journal_index[raw]
                if best is None or hit[0] > best[0]:
                    best = hit
                continue
            # 去标点归一化匹配
            if norm and norm in self._journal_index:
                hit = self._journal_index[norm]
                if best is None or hit[0] > best[0]:
                    best = hit
                continue
            # 剥离卷号/年份后缀（arXiv journal_ref 如 "Phys. Rev. E 101, 022129 (2020)"）
            stripped = _VOLUME_SUFFIX_RE.sub("", raw).strip()
            if stripped and stripped != raw:
                stripped_norm = _normalize_venue(stripped)
                if stripped_norm in self._journal_index:
                    hit = self._journal_index[stripped_norm]
                    if best is None or hit[0] > best[0]:
                        best = hit

        if best is not None:
            return best

        # 检查是否为已知预印本平台
        for candidate in (norm_journal, norm_venue):
            if candidate in _PREPRINT_HOSTS:
                return (0, 2)

        # arXiv 来源默认预印本 tier
        if record.get("source") == "arxiv":
            return (0, 2)

        return (0, 0)

    @staticmethod
    def _build_journal_index(journal_tiers: dict[str, Any]) -> dict[str, tuple[int, int]]:
        index: dict[str, tuple[int, int]] = {}
        for tier_name, tier_data in journal_tiers.items():
            tier_level = 0 if tier_name == "preprint" else int(tier_name.split("_")[-1])
            tier_weight = int(tier_data["weight"])
            for journal in tier_data.get("journals", []):
                names = [journal["name"], *journal.get("aliases", [])]
                for name in names:
                    # 存两份：原始小写 + 去标点归一化
                    key_original = normalize_whitespace(name).lower()
                    key_normalized = _normalize_venue(name)
                    index[key_original] = (tier_level, tier_weight)
                    if key_normalized != key_original:
                        index[key_normalized] = (tier_level, tier_weight)
        return index
