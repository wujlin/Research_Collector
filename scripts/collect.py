#!/usr/bin/env python3
"""手动触发采集。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import CollectionPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Research Collector 手动采集入口")
    parser.add_argument(
        "--source",
        default="all",
        choices=["all", "arxiv", "semantic_scholar", "openalex", "youtube"],
        help="选择采集源",
    )
    parser.add_argument("--query", default="", help="覆盖默认搜索词")
    parser.add_argument("--max-results", type=int, default=None, help="每个查询的最大结果数")
    parser.add_argument("--no-exports", action="store_true", help="只采集入库，不更新导出产物")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    pipeline = CollectionPipeline()
    summary = pipeline.collect(
        source=args.source,
        query=args.query,
        max_results=args.max_results,
        run_exports=not args.no_exports,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
