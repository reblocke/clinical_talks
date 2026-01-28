from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from talks_utils import (
    SECTION_SLUGS,
    guess_section,
    normalize_presentation_stem,
    slugify,
    title_case,
)


EXT_KIND_MAP = {
    ".md": "markdown",
    ".qmd": "markdown",
    ".rmd": "markdown",
    ".ppt": "slides",
    ".pptx": "slides",
    ".pdf": "pdf",
    ".doc": "doc",
    ".docx": "doc",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".gif": "image",
    ".svg": "image",
    ".xlsx": "other",
    ".xls": "other",
}


def read_markdown_title(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    for line in text.splitlines():
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return None


def guess_title(path: Path, kind: str, raw_title: str | None) -> str:
    if raw_title:
        return title_case(raw_title)
    stem = path.stem
    if "Presentations" in path.parts and kind in {"slides", "pdf", "doc", "other"}:
        stem = normalize_presentation_stem(stem)
    stem = stem.replace("_", " ").replace("-", " ")
    return title_case(stem)


def build_manifest(archive_dir: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    seen_pages: dict[str, str] = {}
    for path in sorted(archive_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.name.startswith(".DS_"):
            continue
        ext = path.suffix.lower()
        kind = EXT_KIND_MAP.get(ext, "other")
        raw_title = read_markdown_title(path) if kind == "markdown" else None
        title = guess_title(path, kind, raw_title)
        topic_slug = slugify(title)
        if path.stem.lower() == "index":
            title = "Archive Index"
            topic_slug = "archive-index"
        rel_path = path.relative_to(archive_dir)
        section_guess = guess_section(
            " ".join([rel_path.as_posix(), title]),
            list(rel_path.parts),
        )
        section_slug = SECTION_SLUGS.get(section_guess, slugify(section_guess))
        dest_page = f"talks/{section_slug}/{topic_slug}.qmd"
        rel_path = rel_path.as_posix()
        notes = ""
        if dest_page in seen_pages:
            notes = f"duplicate candidate with {seen_pages[dest_page]}"
        else:
            seen_pages[dest_page] = rel_path
        entries.append(
            {
                "source_path": rel_path,
                "ext": ext.lstrip("."),
                "kind": kind,
                "guessed_topic": title,
                "guessed_section": section_guess,
                "dest_page": dest_page,
                "title": title,
                "notes": notes,
            }
        )
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description="Build archive manifest.")
    parser.add_argument(
        "--archive",
        default="archive",
        help="Path to archive directory (default: archive)",
    )
    parser.add_argument(
        "--output",
        default="content/manifest.yml",
        help="Output manifest path (default: content/manifest.yml)",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    archive_dir = (root / args.archive).resolve()
    if not archive_dir.exists():
        raise SystemExit(f"Archive directory not found: {archive_dir}")
    output_path = (root / args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest(archive_dir)
    with output_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(manifest, handle, sort_keys=False, allow_unicode=True)
    print(f"Wrote {len(manifest)} entries to {output_path}")


if __name__ == "__main__":
    main()
