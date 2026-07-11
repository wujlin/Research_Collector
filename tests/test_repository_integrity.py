import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_RE = re.compile(r"!\[[^]]*]\(([^)]+)\)")
PAPER_LINK_RE = re.compile(r"^- \[[^]]+]\(([^)]+\.md)\)", re.MULTILINE)


def test_digest_manifest_matches_repository_files():
    actual = {
        path.relative_to(ROOT / "digests").as_posix()
        for path in (ROOT / "digests").rglob("*.md")
    }
    generated = {
        item["path"]
        for item in json.loads(
            (ROOT / "web" / "public" / "generated" / "digests.json").read_text(encoding="utf-8")
        )
    }

    assert generated == actual


def test_digest_local_images_are_portable_and_exist():
    failures = []
    for note in (ROOT / "digests").rglob("*.md"):
        for target in IMAGE_RE.findall(note.read_text(encoding="utf-8")):
            clean_target = target.split("#", 1)[0].split("?", 1)[0].strip()
            if clean_target.startswith(("http://", "https://", "data:")):
                continue
            destination = (note.parent / clean_target).resolve()
            if not destination.exists():
                failures.append(f"missing: {note.relative_to(ROOT)} -> {clean_target}")
                continue
            try:
                relative = destination.relative_to(ROOT)
            except ValueError:
                continue
            if relative.parts and relative.parts[0] == "pdfs":
                failures.append(f"ignored pdf asset: {note.relative_to(ROOT)} -> {clean_target}")

    assert not failures, "\n".join(failures)


def test_topic_index_paper_links_exist():
    failures = []
    for index_path in (ROOT / "library").rglob("_index.md"):
        for target in PAPER_LINK_RE.findall(index_path.read_text(encoding="utf-8")):
            if not (index_path.parent / target).resolve().exists():
                failures.append(f"{index_path.relative_to(ROOT)} -> {target}")

    assert not failures, "\n".join(failures)
