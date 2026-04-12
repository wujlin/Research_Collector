from pathlib import Path, PurePosixPath

from src.utils.wsa_mineru import (
    build_local_output_dir,
    discover_pdfs,
    is_mineru_artifact,
    plan_extraction_jobs,
)


def test_discover_pdfs_expands_directory_and_deduplicates(tmp_path: Path):
    pdf_a = tmp_path / "a.pdf"
    pdf_a.write_text("a", encoding="utf-8")
    pdf_b = tmp_path / "nested" / "b.PDF"
    pdf_b.parent.mkdir()
    pdf_b.write_text("b", encoding="utf-8")
    ignored = tmp_path / "paper.mineru" / "hybrid_auto" / "paper_layout.pdf"
    ignored.parent.mkdir(parents=True)
    ignored.write_text("ignored", encoding="utf-8")

    found = discover_pdfs([tmp_path, pdf_a])

    assert found == [pdf_a.resolve(), pdf_b.resolve()]


def test_build_local_output_dir_places_output_beside_pdf():
    pdf_path = Path("/tmp/pdfs/paper.pdf")
    assert build_local_output_dir(pdf_path) == Path("/tmp/pdfs/paper.mineru")


def test_plan_extraction_jobs_preserves_project_relative_layout(tmp_path: Path):
    project_root = tmp_path / "repo"
    pdf_path = project_root / "pdfs" / "2026-04-11" / "paper.pdf"
    pdf_path.parent.mkdir(parents=True)
    pdf_path.write_text("pdf", encoding="utf-8")

    jobs = plan_extraction_jobs(
        [pdf_path],
        project_root=project_root,
        remote_run_root=PurePosixPath("/home/jinlin/projects/Research_Collector/.wsa_mineru/runs/demo"),
    )

    assert len(jobs) == 1
    job = jobs[0]
    assert job.relative_pdf.as_posix() == "pdfs/2026-04-11/paper.pdf"
    assert job.local_output_dir == pdf_path.parent / "paper.mineru"
    assert job.remote_pdf.as_posix().endswith("/in/pdfs/2026-04-11/paper.pdf")
    assert job.remote_result_dir.as_posix().endswith("/out/pdfs/2026-04-11/paper.mineru/paper")


def test_is_mineru_artifact_detects_outputs():
    assert is_mineru_artifact(Path("/tmp/pdfs/paper.mineru/hybrid_auto/paper_layout.pdf"))
    assert not is_mineru_artifact(Path("/tmp/pdfs/paper.pdf"))
