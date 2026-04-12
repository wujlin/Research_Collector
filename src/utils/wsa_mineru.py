"""Path planning helpers for running MinerU on WSA and syncing outputs back."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable


@dataclass(frozen=True)
class ExtractionJob:
    local_pdf: Path
    relative_pdf: Path
    local_output_dir: Path
    remote_pdf: PurePosixPath
    remote_output_parent: PurePosixPath
    remote_result_dir: PurePosixPath


def discover_pdfs(inputs: Iterable[Path]) -> list[Path]:
    """Expand file and directory inputs into a sorted, deduplicated PDF list."""
    found: list[Path] = []
    seen: set[Path] = set()
    for raw_path in inputs:
        path = raw_path.expanduser().resolve()
        if path.is_dir():
            candidates = sorted(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and candidate.suffix.lower() == ".pdf"
            )
        elif path.is_file() and path.suffix.lower() == ".pdf":
            candidates = [path]
        else:
            raise FileNotFoundError(f"PDF input not found or not a PDF: {path}")
        for candidate in candidates:
            if candidate not in seen:
                seen.add(candidate)
                found.append(candidate)
    return found


def make_project_relative_path(pdf_path: Path, project_root: Path) -> Path:
    """Return a stable relative path for remote staging."""
    try:
        return pdf_path.relative_to(project_root)
    except ValueError:
        parent_name = pdf_path.parent.name or "external"
        return Path("_external") / parent_name / pdf_path.name


def build_local_output_dir(pdf_path: Path) -> Path:
    """Place MinerU output beside the source PDF."""
    return pdf_path.parent / f"{pdf_path.stem}.mineru"


def plan_extraction_jobs(
    pdf_paths: Iterable[Path],
    project_root: Path,
    remote_run_root: PurePosixPath,
) -> list[ExtractionJob]:
    jobs: list[ExtractionJob] = []
    for pdf_path in pdf_paths:
        relative_pdf = make_project_relative_path(pdf_path, project_root)
        relative_posix = PurePosixPath(relative_pdf.as_posix())
        remote_pdf = remote_run_root / "in" / relative_posix
        remote_output_parent = remote_run_root / "out" / relative_posix.parent / f"{pdf_path.stem}.mineru"
        remote_result_dir = remote_output_parent / pdf_path.stem
        jobs.append(
            ExtractionJob(
                local_pdf=pdf_path,
                relative_pdf=relative_pdf,
                local_output_dir=build_local_output_dir(pdf_path),
                remote_pdf=remote_pdf,
                remote_output_parent=remote_output_parent,
                remote_result_dir=remote_result_dir,
            )
        )
    return jobs
