import httpx
import pytest

from src.collectors.arxiv_collector import ArxivCollector
from src.collectors.openalex import OpenAlexCollector
from src.collectors.semantic_scholar import SemanticScholarCollector
from src.collectors.youtube_collector import YouTubeCollector


def test_arxiv_collector_parses_feed():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>http://arxiv.org/abs/2011.13456v2</id>
        <published>2021-01-01T00:00:00Z</published>
        <title>Score-Based Generative Modeling through Stochastic Differential Equations</title>
        <summary>Abstract body</summary>
        <author><name>Yang Song</name></author>
        <link title="pdf" href="http://arxiv.org/pdf/2011.13456v2" type="application/pdf" />
      </entry>
    </feed>"""

    transport = httpx.MockTransport(lambda request: httpx.Response(200, text=xml))
    collector = ArxivCollector(http_client=httpx.Client(transport=transport))
    records = collector.collect(query="score", categories=["cs.LG"], max_results=1)

    assert records[0]["arxiv_id"] == "2011.13456"
    assert records[0]["authors"] == ["Yang Song"]
    assert records[0]["pdf_url"].endswith("2011.13456v2")


def test_arxiv_collector_retries_after_429():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>http://arxiv.org/abs/2501.00001v1</id>
        <published>2025-01-01T00:00:00Z</published>
        <title>Retry works for arXiv</title>
        <summary>Abstract body</summary>
        <author><name>Retry Tester</name></author>
        <link title="pdf" href="http://arxiv.org/pdf/2501.00001v1" type="application/pdf" />
      </entry>
    </feed>"""
    responses = iter(
        [
            httpx.Response(429, headers={"Retry-After": "0"}),
            httpx.Response(200, text=xml),
        ]
    )
    sleep_calls: list[float] = []
    transport = httpx.MockTransport(lambda request: next(responses))
    collector = ArxivCollector(
        http_client=httpx.Client(transport=transport),
        settings={
            "collection": {
                "source_policies": {
                    "arxiv": {
                        "min_interval_seconds": 0,
                        "max_retries_on_429": 1,
                        "base_backoff_seconds": 0,
                    }
                }
            }
        },
        sleep_fn=sleep_calls.append,
    )

    records = collector.collect(query="retry", categories=["cs.LG"], max_results=1)

    assert records[0]["arxiv_id"] == "2501.00001"
    assert sleep_calls == [0.0]


def test_arxiv_collector_respects_min_interval_between_requests():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>http://arxiv.org/abs/2011.13456v2</id>
        <published>2021-01-01T00:00:00Z</published>
        <title>Score-Based Generative Modeling through Stochastic Differential Equations</title>
        <summary>Abstract body</summary>
        <author><name>Yang Song</name></author>
        <link title="pdf" href="http://arxiv.org/pdf/2011.13456v2" type="application/pdf" />
      </entry>
    </feed>"""
    sleep_calls: list[float] = []
    clock_values = iter([0.0, 1.0, 4.0])
    transport = httpx.MockTransport(lambda request: httpx.Response(200, text=xml))
    collector = ArxivCollector(
        http_client=httpx.Client(transport=transport),
        settings={
            "collection": {
                "source_policies": {
                    "arxiv": {
                        "min_interval_seconds": 3.5,
                        "max_retries_on_429": 0,
                        "base_backoff_seconds": 0,
                    }
                }
            }
        },
        sleep_fn=sleep_calls.append,
        clock_fn=lambda: next(clock_values),
    )

    collector.collect(query="score", categories=["cs.LG"], max_results=1)
    collector.collect(query="score", categories=["cs.LG"], max_results=1)

    assert sleep_calls == [pytest.approx(2.5)]


def test_semantic_scholar_collector_parses_json():
    payload = {
        "data": [
            {
                "paperId": "abc123",
                "title": "A framework for the use of generative modelling in non-equilibrium statistical mechanics",
                "abstract": "Abstract",
                "year": 2024,
                "authors": [{"name": "Karl Friston"}],
                "venue": "arXiv",
                "journal": {"name": "arXiv"},
                "url": "https://arxiv.org/abs/2406.11630",
                "externalIds": {"ArXiv": "2406.11630"},
                "citationCount": 12,
                "influentialCitationCount": 3,
                "publicationDate": "2024-06-17",
            }
        ]
    }
    transport = httpx.MockTransport(lambda request: httpx.Response(200, json=payload))
    collector = SemanticScholarCollector(http_client=httpx.Client(transport=transport))
    records = collector.collect(query="non-equilibrium", limit=1)

    assert records[0]["semantic_scholar_id"] == "abc123"
    assert records[0]["arxiv_id"] == "2406.11630"
    assert records[0]["citation_count"] == 12


def test_semantic_scholar_collector_retries_after_429(monkeypatch: pytest.MonkeyPatch):
    responses = iter(
        [
            httpx.Response(429, headers={"Retry-After": "0"}),
            httpx.Response(
                200,
                json={
                    "data": [
                        {
                            "paperId": "retry123",
                            "title": "Retry works",
                            "abstract": "Abstract",
                            "year": 2025,
                            "authors": [{"name": "Tester"}],
                            "venue": "arXiv",
                            "journal": {"name": "arXiv"},
                            "url": "https://arxiv.org/abs/2501.00001",
                            "externalIds": {"ArXiv": "2501.00001"},
                            "citationCount": 1,
                            "influentialCitationCount": 0,
                            "publicationDate": "2025-01-01",
                        }
                    ]
                },
            ),
        ]
    )
    transport = httpx.MockTransport(lambda request: next(responses))
    collector = SemanticScholarCollector(
        http_client=httpx.Client(transport=transport),
        settings={
            "collection": {
                "source_policies": {
                    "semantic_scholar": {
                        "max_retries_on_429": 1,
                        "base_backoff_seconds": 0,
                        "limit_without_api_key": 10,
                        "use_in_all_runs_without_api_key": False,
                    }
                }
            }
        },
        sleep_fn=lambda _: None,
    )
    monkeypatch.delenv("SEMANTIC_SCHOLAR_API_KEY", raising=False)
    records = collector.collect(query="retry", limit=1)

    assert records[0]["semantic_scholar_id"] == "retry123"


def test_semantic_scholar_default_run_is_skipped_without_api_key(monkeypatch: pytest.MonkeyPatch):
    collector = SemanticScholarCollector(
        settings={
            "collection": {
                "source_policies": {
                    "semantic_scholar": {
                        "use_in_all_runs_without_api_key": False,
                    }
                }
            }
        }
    )
    monkeypatch.delenv("SEMANTIC_SCHOLAR_API_KEY", raising=False)

    assert collector.should_skip_default_run() is True


def test_openalex_collector_reconstructs_abstract():
    payload = {
        "results": [
            {
                "id": "https://openalex.org/W123",
                "display_name": "Flow Matching for Generative Modeling",
                "abstract_inverted_index": {"Flow": [0], "Matching": [1], "works": [2]},
                "authorships": [{"author": {"display_name": "Yaron Lipman"}}],
                "publication_year": 2023,
                "publication_date": "2023-01-01",
                "primary_location": {"source": {"display_name": "ICLR"}},
                "doi": "https://doi.org/10.0000/example",
                "best_oa_location": {"pdf_url": "https://example.com/paper.pdf"},
                "cited_by_count": 5,
            }
        ]
    }
    transport = httpx.MockTransport(lambda request: httpx.Response(200, json=payload))
    collector = OpenAlexCollector(http_client=httpx.Client(transport=transport))
    records = collector.collect(query="flow", per_page=1)

    assert records[0]["openalex_id"] == "W123"
    assert records[0]["abstract"] == "Flow Matching works"
    assert records[0]["doi"] == "10.0000/example"


def test_openalex_collector_passes_api_key(monkeypatch: pytest.MonkeyPatch):
    seen_params: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen_params.update(dict(request.url.params))
        return httpx.Response(200, json={"results": []})

    monkeypatch.setenv("OPENALEX_API_KEY", "test-openalex-key")
    transport = httpx.MockTransport(handler)
    collector = OpenAlexCollector(http_client=httpx.Client(transport=transport))
    collector.collect(query="flow", per_page=1)

    assert seen_params.get("api_key") == "test-openalex-key"


def test_youtube_collector_preserves_query_metadata():
    item = {
        "id": "video123",
        "snippet": {
            "title": "Max Welling on Variational Inference",
            "channelTitle": "Original Channel",
            "channelId": "channel123",
            "description": "A talk on variational inference and generative models.",
            "publishedAt": "2026-04-08T00:00:00Z",
        },
        "contentDetails": {"duration": "PT12M"},
        "statistics": {"viewCount": "1234"},
    }

    record = YouTubeCollector._parse_video(
        item,
        topic_key="bridges/thermodynamic_inference/variational_free_energy",
        matched_query="Max Welling variational inference",
        channel_label="Max Welling Talks",
        query_source="search_terms",
    )

    assert record["channel_name"] == "Max Welling Talks"
    assert record["matched_query"] == "Max Welling variational inference"
    assert record["query_source"] == "search_terms"
