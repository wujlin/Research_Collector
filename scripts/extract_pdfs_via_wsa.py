#!/usr/bin/env python3
"""Send local PDFs to WSA, extract with MinerU there, and sync results back.

Example:
    export WSA_SSH_PASSWORD='...'
    python scripts/extract_pdfs_via_wsa.py pdfs/2026-04-11 --force
"""

from __future__ import annotations

import argparse
import os
import shlex
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.wsa_mineru import discover_pdfs, plan_extraction_jobs


def get_project_root() -> Path:
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "pyproject.toml").exists():
            return parent
    return Path.cwd()


def build_expect_script() -> str:
    return """
spawn __COMMAND__
expect {
  -re "(?i)yes/no" {
    send "yes\\r"
    exp_continue
  }
  -re "(?i)password:" {
    send "__PASSWORD__\\r"
    exp_continue
  }
  eof
}
set wait_result [wait]
set exit_code [lindex $wait_result 3]
if {$exit_code eq ""} {
  set exit_code 1
}
exit $exit_code
""".strip()


def tcl_literal(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("}", "\\}")
    return "{" + escaped + "}"


def run_expect(command: list[str], password: str, timeout: int) -> None:
    command_literal = " ".join(tcl_literal(item) for item in command)
    script = (
        build_expect_script()
        .replace("__COMMAND__", command_literal)
        .replace("__PASSWORD__", password.replace("\\", "\\\\").replace('"', '\\"'))
    )
    script = f"set timeout {timeout}\n{script}"
    subprocess.run(
        ["expect", "-c", script],
        check=True,
    )


def run_remote_shell(command: str, password: str, remote_host: str, timeout: int) -> None:
    run_expect(
        [
            "ssh",
            "-o",
            "StrictHostKeyChecking=no",
            remote_host,
            f"bash -lc {shlex.quote(command)}",
        ],
        password=password,
        timeout=timeout,
    )


def rsync_to_remote(local_path: Path, remote_path: PurePosixPath, password: str, remote_host: str) -> None:
    run_expect(
        [
            "rsync",
            "-az",
            "-e",
            "ssh -o StrictHostKeyChecking=no",
            str(local_path),
            f"{remote_host}:{remote_path.as_posix()}",
        ],
        password=password,
        timeout=1800,
    )


def rsync_from_remote(remote_path: PurePosixPath, local_path: Path, password: str, remote_host: str) -> None:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    run_expect(
        [
            "rsync",
            "-az",
            "-e",
            "ssh -o StrictHostKeyChecking=no",
            f"{remote_host}:{remote_path.as_posix()}/",
            str(local_path),
        ],
        password=password,
        timeout=1800,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="PDF files or directories to extract")
    parser.add_argument(
        "--remote-host",
        default="jinlin@10.13.12.164",
        help="SSH target for WSA",
    )
    parser.add_argument(
        "--remote-project-root",
        default="/home/jinlin/projects/Research_Collector",
        help="Research_Collector path on WSA",
    )
    parser.add_argument(
        "--api-port",
        type=int,
        default=18000,
        help="MinerU API port on WSA",
    )
    parser.add_argument(
        "--remote-conda-bin",
        default="/home/jinlin/miniconda3/bin/conda",
        help="Absolute conda binary path on WSA",
    )
    parser.add_argument(
        "--password-env",
        default="WSA_SSH_PASSWORD",
        help="Environment variable containing the WSA SSH password",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=7200,
        help="Per-remote-command timeout in seconds",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing local *.mineru output directories",
    )
    parser.add_argument(
        "--keep-remote-artifacts",
        action="store_true",
        help="Keep staged PDFs and MinerU outputs on WSA after syncing back",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if shutil.which("expect") is None:
        raise RuntimeError("`expect` is required for password-based SSH automation.")
    if shutil.which("rsync") is None:
        raise RuntimeError("`rsync` is required to sync PDFs and MinerU outputs.")

    password = os.getenv(args.password_env, "")
    if not password:
        raise RuntimeError(f"Set {args.password_env} before running this script.")

    project_root = get_project_root()
    input_paths = [Path(item) for item in args.inputs]
    pdf_paths = discover_pdfs(input_paths)
    if not pdf_paths:
        raise RuntimeError("No PDF files found from the provided inputs.")

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    remote_run_root = PurePosixPath(args.remote_project_root) / ".wsa_mineru" / "runs" / run_id
    jobs = plan_extraction_jobs(pdf_paths, project_root=project_root, remote_run_root=remote_run_root)

    ensure_api_cmd = (
        f"cd {shlex.quote(args.remote_project_root)} && "
        f"WSA_MINERU_API_PORT={args.api_port} "
        f"WSA_MINERU_CONDA_BIN={shlex.quote(args.remote_conda_bin)} "
        f"bash scripts/wsa_ensure_mineru_api.sh"
    )
    run_remote_shell(ensure_api_cmd, password, args.remote_host, args.timeout)

    for job in jobs:
        if job.local_output_dir.exists():
            if args.force:
                shutil.rmtree(job.local_output_dir)
            else:
                raise RuntimeError(
                    f"Output already exists: {job.local_output_dir}. "
                    "Use --force to overwrite it."
                )

        remote_pdf_dir = job.remote_pdf.parent.as_posix()
        remote_output_parent = job.remote_output_parent.as_posix()
        remote_pdf = job.remote_pdf.as_posix()
        remote_result_dir = job.remote_result_dir.as_posix()

        setup_remote_dirs_cmd = (
            f"mkdir -p {shlex.quote(remote_pdf_dir)} {shlex.quote(remote_output_parent)}"
        )
        run_remote_shell(setup_remote_dirs_cmd, password, args.remote_host, args.timeout)
        rsync_to_remote(job.local_pdf, job.remote_pdf, password, args.remote_host)

        extract_cmd = (
            f"rm -rf {shlex.quote(remote_output_parent)} && "
            f"mkdir -p {shlex.quote(remote_output_parent)} && "
            f"cd {shlex.quote(args.remote_project_root)} && "
            f"CONDA_NO_PLUGINS=true {shlex.quote(args.remote_conda_bin)} run -n dpl mineru "
            f"--api-url http://127.0.0.1:{args.api_port} "
            f"-p {shlex.quote(remote_pdf)} "
            f"-o {shlex.quote(remote_output_parent)}"
        )
        run_remote_shell(extract_cmd, password, args.remote_host, args.timeout)
        rsync_from_remote(PurePosixPath(remote_result_dir), job.local_output_dir, password, args.remote_host)

        if not args.keep_remote_artifacts:
            cleanup_cmd = (
                f"rm -rf {shlex.quote(remote_pdf)} {shlex.quote(remote_output_parent)}"
            )
            run_remote_shell(cleanup_cmd, password, args.remote_host, args.timeout)

        print(f"{job.local_pdf} -> {job.local_output_dir}")


if __name__ == "__main__":
    main()
