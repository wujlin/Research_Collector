#!/usr/bin/env python3
"""启动定时任务，或手动执行某个 job。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.scheduler.runner import SchedulerRunner


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Research Collector 定时任务管理")
    parser.add_argument(
        "--run-once",
        choices=["daily-arxiv", "weekly-full", "monthly"],
        default="",
        help="立即执行一个 job，而不是启动常驻 scheduler",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    runner = SchedulerRunner()
    if args.run_once == "daily-arxiv":
        runner.run_daily_arxiv()
    elif args.run_once == "weekly-full":
        runner.run_weekly_full()
    elif args.run_once == "monthly":
        runner.run_monthly_youtube_and_digest()
    else:
        runner.serve()


if __name__ == "__main__":
    main()
