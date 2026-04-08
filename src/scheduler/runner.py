"""APScheduler 定时任务。"""

from __future__ import annotations

import subprocess
from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler

from src.pipeline import CollectionPipeline
from src.utils.helpers import load_config


class SchedulerRunner:
    def __init__(self):
        self.settings = load_config("settings.yaml")
        self.pipeline = CollectionPipeline()
        self.scheduler = BlockingScheduler(timezone="UTC")

    def configure(self) -> BlockingScheduler:
        collection_cfg = self.settings["collection"]
        self.scheduler.add_job(
            self.run_daily_arxiv,
            trigger="cron",
            hour=collection_cfg["daily_arxiv_hour"],
            minute=collection_cfg["daily_arxiv_minute"],
            id="daily_arxiv",
            replace_existing=True,
        )
        self.scheduler.add_job(
            self.run_weekly_full,
            trigger="cron",
            day_of_week=collection_cfg["weekly_full_day"],
            hour=collection_cfg["weekly_full_hour"],
            minute=0,
            id="weekly_full",
            replace_existing=True,
        )
        self.scheduler.add_job(
            self.run_monthly_youtube_and_digest,
            trigger="cron",
            day=collection_cfg["monthly_youtube_day"],
            hour=collection_cfg["monthly_youtube_hour"],
            minute=0,
            id="monthly_youtube",
            replace_existing=True,
        )
        return self.scheduler

    def run_daily_arxiv(self) -> None:
        self.pipeline.collect(source="arxiv", run_exports=True)
        self._maybe_auto_commit("daily arxiv update")

    def run_weekly_full(self) -> None:
        self.pipeline.collect(source="all", run_exports=True)
        self._maybe_auto_commit("weekly full collection")

    def run_monthly_youtube_and_digest(self) -> None:
        self.pipeline.collect(source="youtube", run_exports=False)
        self.pipeline.export_all(digest_period="monthly")
        self._maybe_auto_commit("monthly youtube and digest update")

    def serve(self) -> None:
        self.configure()
        self.scheduler.start()

    def _maybe_auto_commit(self, reason: str) -> None:
        if not self.settings.get("git", {}).get("auto_commit", False):
            return

        root = Path(__file__).resolve().parents[2]
        tracked_paths = ["library", "youtube", "knowledge_map", "digests", "data", "web/public/generated"]
        status = subprocess.run(
            ["git", "status", "--porcelain", "--", *tracked_paths],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        if not status.stdout.strip():
            return

        subprocess.run(["git", "add", *tracked_paths], cwd=root, check=False)
        message = f"{self.settings['git']['commit_message_prefix']} {reason}"
        subprocess.run(["git", "commit", "-m", message], cwd=root, check=False)
