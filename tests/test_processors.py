from src.processors.citation_analyzer import CitationAnalyzer
from src.processors.classifier import TopicClassifier
from src.processors.deduplicator import Deduplicator
from src.processors.importance_ranker import ImportanceRanker
from src.processors.relevance_scorer import RelevanceScorer
from src.processors.youtube_filter import YouTubeFilter


def test_deduplicator_merges_cross_source_records():
    deduplicator = Deduplicator()
    records = [
        {
            "title": "Score-Based Generative Modeling through Stochastic Differential Equations",
            "abstract": "A long abstract",
            "authors": ["Yang Song"],
            "doi": "",
            "arxiv_id": "2011.13456",
            "source": "arxiv",
            "citation_count": 10,
        },
        {
            "title": "Score-Based Generative Modeling Through Stochastic Differential Equations",
            "abstract": "A much longer abstract that should win when merging.",
            "authors": ["Yang Song", "Ben Poole"],
            "doi": "",
            "arxiv_id": "2011.13456",
            "source": "semantic_scholar",
            "citation_count": 100,
        },
    ]

    merged = deduplicator.deduplicate(records)

    assert len(merged) == 1
    assert merged[0]["citation_count"] == 100
    assert "semantic_scholar" in merged[0]["source"]
    assert "Ben Poole" in merged[0]["authors"]


def test_classifier_detects_sde_and_diffusion_topics():
    classifier = TopicClassifier()
    record = classifier.classify_record(
        {
            "title": "Score-Based Generative Modeling through Stochastic Differential Equations",
            "abstract": "We introduce reverse-time SDEs and probability flow ODEs for score-based generation.",
        }
    )

    assert "ai_for_physics/generative_dynamics/sde_generative" in record["topic_keys"]
    assert "ai_for_physics/generative_dynamics" in record["topic_keys"]
    assert "ai_for_physics" in record["topic_keys"]


def test_classifier_rejects_negative_keywords():
    classifier = TopicClassifier()
    record = classifier.classify_record(
        {
            "title": "Methods for Molecular Recognition Computing",
            "abstract": "A mutagenesis and protein-ligand screening workflow.",
        }
    )

    assert record["is_irrelevant"] is True
    assert "molecular recognition" in record["negative_keyword_hits"]
    assert record["topic_keys"] == []


def test_classifier_does_not_match_ness_inside_consciousness():
    classifier = TopicClassifier()
    record = classifier.classify_record(
        {
            "title": "Quantum-Inspired Approaches to Consciousness",
            "abstract": "This article discusses consciousness and cognitive science.",
        }
    )

    assert "statistical_physics/non_equilibrium_dynamics/nonequilibrium" not in record["topic_keys"]


def test_relevance_scorer_and_citation_analyzer_enrich_record():
    scorer = RelevanceScorer()
    analyzer = CitationAnalyzer()
    record = {
        "title": "Nonequilibrium Equality for Free Energy Differences",
        "abstract": "A classic fluctuation theorem result for nonequilibrium work.",
        "journal": "Physical Review Letters",
        "year": 1997,
        "citation_count": 4500,
        "influential_citation_count": 500,
        "topic_keys": ["statistical_physics/fluctuation_theorems", "statistical_physics"],
        "source": "openalex",
    }

    scorer.score_record(record)
    analyzer.enrich_record(record)

    assert record["tier"] == 1
    assert record["relevance_score"] > 40
    assert record["seminal_candidate"] is True


def test_relevance_scorer_does_not_match_science_inside_computer_science():
    scorer = RelevanceScorer()
    record = {
        "title": "A PINN paper",
        "abstract": "Brownian motion and stochastic dynamics.",
        "journal": "International Journal of Information Technology and Computer Science",
        "year": 2026,
        "citation_count": 0,
        "influential_citation_count": 0,
        "topic_keys": ["stochastic_analysis/path_foundations/brownian_motion"],
        "source": "openalex",
    }

    scorer.score_record(record)

    assert record["tier"] == 0
    assert record["venue_quality"] == "unranked"


def test_importance_ranker_penalizes_suspicious_uncategorized_items():
    ranker = ImportanceRanker()
    keep_score, keep_bucket = ranker.score_paper(
        {
            "title": "PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration",
            "abstract": "A physics-informed neural network for Brownian motion and stochastic dynamics.",
            "topics": [
                "stochastic_analysis/path_foundations/brownian_motion",
                "ai_for_physics/physics_informed_modeling/physics_informed_generative",
            ],
            "relevance_score": 70,
            "citation_count": 0,
            "influential_citation_count": 0,
            "is_seminal": False,
            "source": "openalex",
            "tier": 0,
            "journal": "International Journal of Information Technology and Computer Science",
            "venue": "International Journal of Information Technology and Computer Science",
        }
    )
    low_score, low_bucket = ranker.score_paper(
        {
            "title": "Open-Source Molecular Docking and AI-Augmented Structure-Based Drug Design",
            "abstract": "A review of molecular docking workflows for drug discovery.",
            "topics": [],
            "relevance_score": 52,
            "citation_count": 0,
            "influential_citation_count": 0,
            "is_seminal": False,
            "source": "openalex",
            "tier": 0,
            "journal": "",
            "venue": "",
        }
    )

    assert keep_score > low_score
    assert keep_bucket == "keep"
    assert low_bucket == "archive"


def test_importance_ranker_prefers_stronger_venue_when_other_signals_match():
    ranker = ImportanceRanker()
    strong_score, _ = ranker.score_paper(
        {
            "title": "Ergodicity in stochastic systems",
            "abstract": "A study of ergodicity and stochastic dynamics.",
            "topics": ["stochastic_analysis/stochastic_dynamics/sde_theory"],
            "relevance_score": 52,
            "citation_count": 0,
            "influential_citation_count": 0,
            "is_seminal": False,
            "source": "openalex",
            "tier": 3,
            "journal": "Scientific Reports",
            "venue": "Scientific Reports",
        }
    )
    weak_score, _ = ranker.score_paper(
        {
            "title": "Ergodicity in stochastic systems",
            "abstract": "A study of ergodicity and stochastic dynamics.",
            "topics": ["stochastic_analysis/stochastic_dynamics/sde_theory"],
            "relevance_score": 52,
            "citation_count": 0,
            "influential_citation_count": 0,
            "is_seminal": False,
            "source": "openalex",
            "tier": 0,
            "journal": "International Journal of Information Technology and Computer Science",
            "venue": "International Journal of Information Technology and Computer Science",
        }
    )

    assert strong_score > weak_score


def test_youtube_filter_rejects_playlist_noise_without_topic_signal():
    youtube_filter = YouTubeFilter()
    verdict = youtube_filter.evaluate(
        {
            "title": "Lecture 18: Applying Data Science and Artificial Intelligence to Managing Biomedical Portfolios",
            "description": "A lecture on financing rare diseases and biomedical portfolios.",
            "channel_name": "MIT OpenCourseWare",
            "topic_key": "stochastic_analysis/stochastic_dynamics/sde_numerics",
            "matched_query": "18.S096 Topics in Mathematics with Applications in Finance",
            "query_source": "relevant_playlists",
        }
    )

    assert verdict["keep"] is False
    assert "biomedical portfolios" in verdict["negative_keyword_hits"]


def test_youtube_filter_keeps_search_term_match_for_targeted_frontier_video():
    youtube_filter = YouTubeFilter()
    verdict = youtube_filter.evaluate(
        {
            "title": "Max Welling on Variational Inference and Generative Models",
            "description": "A research talk on variational inference, free energy, and generative models for physics.",
            "channel_name": "Max Welling Talks",
            "topic_key": "bridges/thermodynamic_inference/variational_free_energy",
            "matched_query": "Max Welling variational inference",
            "query_source": "search_terms",
        }
    )

    assert verdict["keep"] is True
    assert verdict["resolved_topic_key"] == "bridges/thermodynamic_inference/variational_free_energy"
