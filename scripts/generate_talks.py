from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

import yaml

from talks_utils import SECTION_ORDER, SECTION_SLUGS, slugify, title_case


STANDARD_OBJECTIVES = [
    "TODO: Define the core learning goals for this topic.",
    "TODO: Identify 3–7 key takeaways for residents.",
    "TODO: Clarify what decisions this talk supports.",
]


def extract_headings(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    headings: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            headings.append(line.lstrip("# ").strip())
        elif line.startswith("### "):
            headings.append(line.lstrip("# ").strip())
    return headings


def build_what_this_covers(headings: list[str]) -> list[str]:
    seen = set()
    bullets: list[str] = []
    for heading in headings:
        clean = heading.strip()
        if not clean or clean.lower() in seen:
            continue
        bullets.append(clean)
        seen.add(clean.lower())
        if len(bullets) == 3:
            break
    if not bullets:
        bullets = ["TODO: Summarize key sections from the source notes."]
    return bullets


def format_link(path: str) -> str:
    return quote(path, safe="/")


def format_include(path: str) -> str:
    return f"{{{{< include \"{path}\" >}}}}"


def render_standard_sections() -> list[str]:
    lines = [
        "## Learning objectives",
        *(f"- {item}" for item in STANDARD_OBJECTIVES),
        "",
        "## Bottom line / summary",
        "- TODO: Summarize the highest-yield point.",
        "- TODO: Summarize the second-highest-yield point.",
        "- TODO: Summarize the third-highest-yield point.",
        "- TODO: Summarize the fourth-highest-yield point.",
        "- TODO: Summarize the fifth-highest-yield point.",
        "",
        "## Approach",
        "1. TODO: Outline the initial assessment or decision point.",
        "2. TODO: Outline the next diagnostic or management step.",
        "3. TODO: Outline follow-up or escalation criteria.",
        "",
        "## Red flags / when to escalate",
        "- TODO: List red flags that require urgent escalation.",
        "",
        "## Common pitfalls",
        "- TODO: Capture common errors or missed steps.",
        "",
        "## References",
        "TODO: Add landmark references or guideline citations.",
        "",
    ]
    return lines


def build_markdown_page(
    title: str,
    source_paths: list[str],
    archive_dir: Path,
) -> str:
    headings: list[str] = []
    for source in source_paths:
        headings.extend(extract_headings(archive_dir / source))
    what_this_covers = build_what_this_covers(headings)

    lines = [
        "---",
        f"title: {title}",
        "draft: true",
        "---",
        "",
        "## What this covers",
        *(f"- {bullet}" for bullet in what_this_covers),
        "",
        *render_standard_sections(),
        "## Source notes",
    ]

    for source in source_paths:
        include_path = f"include/source-notes/{source}"
        lines.extend(
            [
                "",
                f"### {title_case(Path(source).stem.replace('-', ' ').replace('_', ' '))}",
                format_include(include_path),
            ]
        )

    lines.extend(
        [
            "",
            "## Source materials",
            *(
                f"- [{source}](" + format_link(f"archive/{source}") + ")"
                for source in source_paths
            ),
            "",
        ]
    )
    return "\n".join(lines)


def build_asset_page(
    title: str,
    source_paths: list[str],
) -> str:
    lines = [
        "---",
        f"title: {title}",
        "draft: true",
        "---",
        "",
        "## Summary",
        "TODO: Summarize the slide/PDF content once curated.",
        "",
        *render_standard_sections(),
        "## Slides and assets",
        *(
            f"- [{source}](" + format_link(f"archive/{source}") + ")"
            for source in source_paths
        ),
        "",
        "## Source materials",
        *(
            f"- [{source}](" + format_link(f"archive/{source}") + ")"
            for source in source_paths
        ),
        "",
    ]
    return "\n".join(lines)


def write_section_index(section_title: str, pages: list[dict], output_path: Path) -> None:
    lines = [
        "---",
        f"title: {section_title}",
        "---",
        "",
        "## Topics",
    ]
    for page in pages:
        relative = Path(page["path"]).name
        lines.append(f"- [{page['title']}]({relative})")
    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def update_quarto_chapters(
    quarto_path: Path,
    chapters_lines: list[str],
) -> None:
    text = quarto_path.read_text(encoding="utf-8")
    marker_start = "  chapters:\n"
    marker_end = "  appendices:"
    start_index = text.find(marker_start)
    end_index = text.find(marker_end)
    if start_index == -1 or end_index == -1 or end_index <= start_index:
        raise SystemExit("Unable to locate chapters block in _quarto.yml")
    indented_lines = [f"  {line}" if line else "" for line in chapters_lines]
    updated = (
        text[: start_index + len(marker_start)]
        + "\n".join(indented_lines)
        + "\n"
        + text[end_index:]
    )
    quarto_path.write_text(updated, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate talk pages from manifest.")
    parser.add_argument(
        "--manifest",
        default="content/manifest.yml",
        help="Manifest path (default: content/manifest.yml)",
    )
    parser.add_argument(
        "--archive",
        default="archive",
        help="Archive directory (default: archive)",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest_path = (root / args.manifest).resolve()
    archive_dir = (root / args.archive).resolve()
    if not manifest_path.exists():
        raise SystemExit(f"Manifest not found: {manifest_path}")
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or []

    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in manifest:
        grouped[entry["dest_page"]].append(entry)

    sections: dict[str, list[dict]] = defaultdict(list)
    for dest_page, entries in grouped.items():
        section = entries[0]["guessed_section"]
        title = entries[0]["title"]
        pages = {
            "path": dest_page,
            "title": title,
            "entries": entries,
            "section": section,
        }
        sections[section].append(pages)

    talks_dir = root / "talks"
    talks_dir.mkdir(parents=True, exist_ok=True)

    section_pages: dict[str, list[dict]] = {}
    for section_name, pages in sections.items():
        pages_sorted = sorted(pages, key=lambda item: item["title"].lower())
        section_pages[section_name] = pages_sorted
        section_slug = SECTION_SLUGS.get(section_name, slugify(section_name))
        section_dir = talks_dir / section_slug
        section_dir.mkdir(parents=True, exist_ok=True)

        for page in pages_sorted:
            dest_path = root / page["path"]
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            entries = page["entries"]
            source_paths = [entry["source_path"] for entry in entries]
            kinds = {entry["kind"] for entry in entries}
            if "markdown" in kinds:
                content = build_markdown_page(page["title"], source_paths, archive_dir)
            else:
                content = build_asset_page(page["title"], source_paths)
            dest_path.write_text(content, encoding="utf-8")

        index_path = section_dir / "index.qmd"
        write_section_index(section_name, pages_sorted, index_path)

    chapter_lines = ["- index.qmd"]
    for section_name, section_slug in SECTION_ORDER:
        if section_name not in section_pages:
            continue
        chapter_lines.append(f"- part: {section_name}")
        chapter_lines.append("  chapters:")
        chapter_lines.append(f"  - talks/{section_slug}/index.qmd")
        for page in section_pages[section_name]:
            chapter_lines.append(f"  - {page['path']}")

    chapters_path = root / "content" / "chapters.yml"
    chapters_path.parent.mkdir(parents=True, exist_ok=True)
    chapters_path.write_text("\n".join(chapter_lines) + "\n", encoding="utf-8")

    update_quarto_chapters(root / "_quarto.yml", chapter_lines)
    print(f"Generated {len(grouped)} talk pages across {len(section_pages)} sections.")


if __name__ == "__main__":
    main()
