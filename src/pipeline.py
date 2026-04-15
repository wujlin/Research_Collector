"""端到端采集与导出流水线。"""

from __future__ import annotations

from typing import Any

from src.collectors.arxiv_collector import ArxivCollector
from src.collectors.openalex import OpenAlexCollector
from src.collectors.semantic_scholar import SemanticScholarCollector
from src.collectors.youtube_collector import YouTubeCollector
from src.exporters.digest import DigestExporter
from src.exporters.knowledge_graph import KnowledgeGraphExporter
from src.exporters.reading_list import ReadingListExporter
from src.exporters.web_snapshot import WebSnapshotExporter
from src.processors.citation_analyzer import CitationAnalyzer
from src.processors.classifier import TopicClassifier
from src.processors.deduplicator import Deduplicator
from src.processors.importance_ranker import ImportanceRanker
from src.processors.relevance_scorer import RelevanceScorer
from src.processors.youtube_filter import YouTubeFilter
from src.storage.database import Database
from src.storage.markdown_store import MarkdownStore
from src.utils.helpers import ensure_data_dirs, flatten_topics, load_config


class CollectionPipeline:
    def __init__(self, db_path: str | None = None):
        ensure_data_dirs()
        settings = load_config("settings.yaml")
        storage_cfg = settings["storage"]
        self.settings = settings
        self.sources_cfg = load_config("sources.yaml")
        self.youtube_cfg = load_config("youtube_channels.yaml")
        self.query_profiles = load_config("query_profiles.yaml")
        self.taxonomy = load_config("topics.yaml")

        self.database = Database(db_path or storage_cfg["database_path"])
        self.markdown_store = MarkdownStore(storage_cfg["library_dir"])
        self.deduplicator = Deduplicator()
        self.classifier = TopicClassifier()
        self.relevance_scorer = RelevanceScorer()
        self.citation_analyzer = CitationAnalyzer()
        self.importance_ranker = ImportanceRanker()
        self.youtube_filter = YouTubeFilter()
        self.reading_list_exporter = ReadingListExporter()
        self.digest_exporter = DigestExporter(storage_cfg["digest_dir"])
        self.knowledge_graph_exporter = KnowledgeGraphExporter()
        self.web_snapshot_exporter = WebSnapshotExporter()

        self.collectors = {
            "arxiv": ArxivCollector(),
            "semantic_scholar": SemanticScholarCollector(),
            "openalex": OpenAlexCollector(),
            "youtube": YouTubeCollector(),
        }

    def collect(
        self,
        source: str = "all",
        query: str = "",
        max_results: int | None = None,
        run_exports: bool = True,
        continue_on_error: bool = True,
    ) -> dict[str, Any]:
        self.database.init_topics_from_yaml("config/topics.yaml")
        self.markdown_store.ensure_directory_structure("config/topics.yaml")

        sources = list(self.collectors.keys()) if source == "all" else [source]
        summary: dict[str, Any] = {
            "sources": {},
            "papers_processed": 0,
            "youtube_processed": 0,
            "errors": [],
        }

        for source_name in sources:
            if source_name not in self.collectors:
                raise ValueError(f"Unknown source: {source_name}")
            collector = self.collectors[source_name]
            source_policy = self.settings.get("collection", {}).get("source_policies", {}).get(source_name, {})
            if source_policy and source_policy.get("enabled") is False:
                log_id = self.database.log_collection(source_name)
                message = f"Skipped because {source_name} is disabled in config."
                self.database.update_collection_log(log_id, status="skipped", error_message=message)
                summary["sources"][source_name] = {
                    "processed": 0,
                    "status": "skipped",
                    "reason": "disabled_in_config",
                }
                continue
            if (
                source == "all"
                and source_name == "semantic_scholar"
                and isinstance(collector, SemanticScholarCollector)
                and collector.should_skip_default_run()
            ):
                log_id = self.database.log_collection(source_name)
                message = "Skipped in all-source run because SEMANTIC_SCHOLAR_API_KEY is not configured."
                self.database.update_collection_log(log_id, status="skipped", error_message=message)
                summary["sources"][source_name] = {
                    "processed": 0,
                    "status": "skipped",
                    "reason": "missing_api_key",
                }
                continue

            log_id = self.database.log_collection(source_name)
            try:
                if source_name == "youtube":
                    count = self._collect_youtube(query=query, max_results=max_results)
                    summary["youtube_processed"] += count
                    summary["sources"][source_name] = {"processed": count, "status": "success"}
                    self.database.update_collection_log(
                        log_id,
                        status="success",
                        papers_found=count,
                        papers_added=count,
                    )
                    continue

                processed = self._collect_papers(source_name, query=query, max_results=max_results)
                summary["papers_processed"] += len(processed)
                summary["sources"][source_name] = {"processed": len(processed), "status": "success"}
                self.database.update_collection_log(
                    log_id,
                    status="success",
                    papers_found=len(processed),
                    papers_added=len(processed),
                )
            except Exception as exc:
                self.database.update_collection_log(log_id, status="failed", error_message=str(exc))
                summary["sources"][source_name] = {
                    "processed": 0,
                    "status": "failed",
                    "error": str(exc),
                }
                summary["errors"].append({"source": source_name, "error": str(exc)})
                if not continue_on_error:
                    raise

        self._refresh_library_indices()

        if run_exports:
            self.export_all()

        summary["stats"] = self.database.get_stats()
        return summary

    def export_all(self, digest_period: str = "weekly") -> None:
        export_cfg = self.settings["export"]
        self.reading_list_exporter.export(
            self.database,
            limit=export_cfg["reading_list_size"],
        )
        days = 30 if digest_period == "monthly" else 7
        self.digest_exporter.export(
            self.database,
            period=digest_period,
            days=days,
            paper_limit=export_cfg["digest_paper_count"],
        )
        self.knowledge_graph_exporter.export(self.database)
        self.web_snapshot_exporter.export_all(self.database)

    def _collect_papers(
        self,
        source_name: str,
        query: str = "",
        max_results: int | None = None,
    ) -> list[dict[str, Any]]:
        collector = self.collectors[source_name]
        query_profiles = self.query_profiles.get(source_name, [])
        per_query_limits = self.settings.get("collection", {}).get("per_query_limits", {})
        limit = max_results or min(
            int(per_query_limits.get(source_name, 10)),
            int(self.settings["filtering"]["max_papers_per_run"]) // max(1, len(query_profiles) or 1),
        )
        queries = [query] if query else query_profiles
        raw_records: list[dict[str, Any]] = []
        query_errors: list[Exception] = []

        for item_query in queries:
            kwargs: dict[str, Any] = {}
            if source_name == "arxiv":
                kwargs["categories"] = self.sources_cfg.get("arxiv_categories", [])
                kwargs["max_results"] = limit
            elif source_name == "semantic_scholar":
                kwargs["limit"] = limit
                kwargs["year_from"] = self.settings["filtering"]["min_year"]
            elif source_name == "openalex":
                kwargs["per_page"] = limit
                kwargs["year_from"] = self.settings["filtering"]["min_year"]
            try:
                raw_records.extend(collector.collect(query=item_query, **kwargs))
            except Exception as exc:
                query_errors.append(exc)
                continue

        if not raw_records and query_errors:
            raise query_errors[-1]

        records = self.deduplicator.deduplicate(raw_records)
        processed: list[dict[str, Any]] = []
        for record in records:
            self.classifier.classify_record(record)
            self.relevance_scorer.score_record(record)
            self.citation_analyzer.enrich_record(record)
            if not self._passes_filters(record):
                continue
            paper = self.database.add_paper(record)
            markdown_path = self.markdown_store.save_paper(paper)
            self.database.update_paper_markdown_path(paper.id, markdown_path)
            processed.append(record)

        return processed

    def _collect_youtube(self, query: str = "", max_results: int | None = None) -> int:
        collector = self.collectors["youtube"]
        limit = max_results or 4
        resources = collector.collect(
            query=query,
            max_results=limit,
            channels=self.youtube_cfg.get("channels"),
        )
        kept = 0
        for resource in resources:
            verdict = self.youtube_filter.evaluate(resource)
            if not verdict["keep"]:
                continue
            resource["topic_key"] = verdict["resolved_topic_key"] or resource.get("topic_key", "")
            resource.pop("matched_query", None)
            resource.pop("query_source", None)
            score, bucket = self.importance_ranker.score_youtube(resource)
            if bucket == "archive":
                continue
            self.database.add_youtube_resource(resource)
            kept += 1
        return kept

    def _passes_filters(self, record: dict[str, Any]) -> bool:
        filtering = self.settings["filtering"]
        if record.get("is_irrelevant"):
            return False

        min_year = filtering.get("min_year", 0)
        if record.get("year") and int(record["year"]) < min_year:
            return False

        if float(record.get("relevance_score", 0.0) or 0.0) < filtering["relevance_threshold"]:
            return False

        if record.get("source") != "arxiv" and int(record.get("citation_count", 0) or 0) < filtering["min_citations"]:
            return False
        return True

    def _refresh_library_indices(self) -> None:
        for entry in flatten_topics(self.taxonomy):
            self.markdown_store.write_topic_index(
                topic_key=entry["key"],
                display_name=entry["display_name"],
                description=entry.get("description", ""),
                papers=self.database.get_papers_by_topic(entry["key"], limit=200),
            )
        self.markdown_store.write_master_index(self.taxonomy)
