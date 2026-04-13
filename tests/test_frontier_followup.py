from scripts.generate_frontier_followup import (
    Candidate,
    load_author_affiliation_registry,
    is_must_read_eligible,
    summarize_author_affiliation_signal,
    load_venue_reputation_registry,
    venue_reputation_status,
)
from src.processors.importance_ranker import ImportanceRanker


def build_candidate(
    title: str,
    venue_quality: str,
    venue_reputation: str,
    importance_score: float = 70.0,
    author_signal: str = "strong_match",
) -> Candidate:
    return Candidate(
        paper_id=1,
        title=title,
        journal="Example Journal",
        year=2026,
        url="https://example.com",
        topics=["stochastic_analysis/path_foundations/brownian_motion"],
        importance_score=importance_score,
        importance_bucket="keep",
        venue_quality=venue_quality,
        venue_reputation=venue_reputation,
        tier=0,
        authors=["Jane Doe"],
        author_signal=author_signal,
        author_signal_reason="team signal",
        author_affiliations=["Department of Physics, Princeton University"],
        fit_reason="fit",
        reproduction_reason="repro",
    )


def test_venue_reputation_registry_maps_checked_venues():
    registry, default_status = load_venue_reputation_registry()

    assert venue_reputation_status("Physical Review Letters", "", registry, default_status) == "trusted"
    assert venue_reputation_status("Scientific Reports", "", registry, default_status) == "cautious"
    assert (
        venue_reputation_status(
            "International Journal of Information Technology and Computer Science",
            "",
            registry,
            default_status,
        )
        == "weak"
    )


def test_must_read_requires_trusted_venue_or_strong_preprint():
    ranker = ImportanceRanker()

    trusted = build_candidate("Trusted venue paper", "top_tier", "trusted")
    cautious = build_candidate("Cautious venue paper", "solid_domain", "cautious")
    weak = build_candidate("Weak venue paper", "unranked", "weak")
    preprint = build_candidate("Strong preprint paper", "preprint", "unreviewed", importance_score=68.0)

    assert is_must_read_eligible(trusted, ranker) is True
    assert is_must_read_eligible(cautious, ranker) is False
    assert is_must_read_eligible(weak, ranker) is False
    assert is_must_read_eligible(preprint, ranker) is True


def test_must_read_rejects_weak_author_signal_even_for_trusted_venue():
    ranker = ImportanceRanker()
    weak_team = build_candidate("Trusted venue but weak team fit", "top_tier", "trusted", author_signal="weak_match")

    assert is_must_read_eligible(weak_team, ranker) is False


def test_author_affiliation_signal_prefers_topic_aligned_reputable_groups():
    registry = load_author_affiliation_registry()
    status, reason = summarize_author_affiliation_signal(
        ["statistical_physics/non_equilibrium_dynamics/nonequilibrium"],
        ["Department of Physics, Princeton University"],
        registry,
    )

    assert status == "strong_match"
    assert "Strong institution" in reason


def test_author_affiliation_signal_keeps_generic_academic_groups_as_unknown():
    registry = load_author_affiliation_registry()
    status, reason = summarize_author_affiliation_signal(
        ["statistical_physics/non_equilibrium_dynamics/nonequilibrium"],
        ["Hebrew University of Jerusalem"],
        registry,
    )

    assert status == "unknown"
    assert "Academic affiliation metadata" in reason


def test_author_affiliation_signal_marks_explicitly_off_topic_groups_as_weak():
    registry = load_author_affiliation_registry()
    status, reason = summarize_author_affiliation_signal(
        ["statistical_physics/non_equilibrium_dynamics/nonequilibrium"],
        ["School of Dentistry, Example University"],
        registry,
    )

    assert status == "weak_match"
    assert "explicitly off-topic" in reason
