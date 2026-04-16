from src.utils.helpers import canonical_digest_path


def test_canonical_digest_path_uses_workflow_subdirectory():
    path = canonical_digest_path("digests", "2026-04-08", "paper_queue")
    assert path.as_posix() == "digests/2026-04-08/workflow/paper-queue.md"


def test_canonical_digest_path_supports_periodic_digests():
    path = canonical_digest_path("digests", "2026-04-08", "weekly")
    assert path.as_posix() == "digests/2026-04-08/workflow/weekly.md"
