from __future__ import annotations

import argparse
import os
import re
import zipfile
from pathlib import Path
from urllib.parse import quote
import xml.etree.ElementTree as ET

import yaml

from talks_utils import title_case


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+(.*)$")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"\bhttps?://\S+")

RED_FLAG_KEYWORDS = (
    "red flag",
    "warning",
    "urgent",
    "emerg",
    "unstable",
    "shock",
    "escalat",
)

PITFALL_KEYWORDS = (
    "pitfall",
    "avoid",
    "error",
    "mistake",
    "don't",
    "do not",
    "missed",
    "beware",
    "caution",
)


def clean_text(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`+", "", text)
    text = re.sub(r"\*\*?", "", text)
    text = re.sub(r"_+", "", text)
    text = re.sub(r"=+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_front_matter(lines: list[str]) -> list[str]:
    if not lines or lines[0].strip() != "---":
        return lines
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[idx + 1 :]
    return lines


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def dedupe_preserve(items: list[str]) -> list[str]:
    seen = set()
    result: list[str] = []
    for item in items:
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


def extract_markdown_data(text: str) -> dict[str, list[str]]:
    lines = strip_front_matter(text.splitlines())
    headings: list[str] = []
    bullets: list[str] = []
    paragraphs: list[str] = []
    links: list[str] = []
    para_buffer: list[str] = []

    def flush_paragraph() -> None:
        if not para_buffer:
            return
        paragraph = clean_text(" ".join(para_buffer))
        if paragraph:
            paragraphs.append(paragraph)
        para_buffer.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            continue

        for _, link in MD_LINK_RE.findall(stripped):
            links.append(link.rstrip(").,;:"))
        for link in URL_RE.findall(stripped):
            links.append(link.rstrip(").,;:"))

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            flush_paragraph()
            heading_text = clean_text(heading_match.group(2))
            if heading_text:
                headings.append(heading_text)
            continue

        bullet_match = BULLET_RE.match(stripped)
        if bullet_match:
            flush_paragraph()
            bullet_text = clean_text(bullet_match.group(1))
            if bullet_text:
                bullets.append(bullet_text)
            continue

        para_buffer.append(stripped)

    flush_paragraph()
    return {
        "headings": headings,
        "bullets": bullets,
        "paragraphs": paragraphs,
        "links": links,
    }


def build_learning_objectives(
    title: str,
    headings: list[str],
    bullets: list[str],
    paragraphs: list[str],
) -> list[str]:
    candidates: list[str] = []
    title_lower = title.lower()
    for heading in headings:
        if heading.lower() == title_lower:
            continue
        if heading.lower() in {"references", "source notes", "source materials"}:
            continue
        candidates.append(heading)
    if len(candidates) < 3:
        candidates.extend(bullets)
    if len(candidates) < 3:
        candidates.extend(paragraphs)
    return dedupe_preserve([clean_text(item) for item in candidates if item])[:7]


def build_summary(paragraphs: list[str], bullets: list[str]) -> list[str]:
    summary: list[str] = []
    for paragraph in paragraphs:
        for sentence in split_sentences(paragraph):
            cleaned = clean_text(sentence)
            if len(cleaned) < 20:
                continue
            summary.append(cleaned)
            if len(summary) >= 5:
                return summary
    for bullet in bullets:
        cleaned = clean_text(bullet)
        if cleaned:
            summary.append(cleaned)
        if len(summary) >= 5:
            break
    return dedupe_preserve(summary)[:5]


def build_approach(headings: list[str], bullets: list[str]) -> list[str]:
    steps: list[str] = []
    for bullet in bullets:
        cleaned = clean_text(bullet)
        if cleaned.lower().startswith("note:"):
            continue
        steps.append(cleaned)
        if len(steps) >= 5:
            break
    if len(steps) < 3:
        for heading in headings:
            cleaned = clean_text(heading)
            if cleaned:
                steps.append(cleaned)
            if len(steps) >= 3:
                break
    return dedupe_preserve(steps)[:7]


def extract_keyword_lines(
    candidates: list[str], keywords: tuple[str, ...], max_items: int
) -> list[str]:
    matches: list[str] = []
    for line in candidates:
        lowered = line.lower()
        if any(keyword in lowered for keyword in keywords):
            matches.append(clean_text(line))
        if len(matches) >= max_items:
            break
    return dedupe_preserve(matches)[:max_items]


def extract_references(links: list[str]) -> list[str]:
    cleaned = [clean_text(link).rstrip(").,;:") for link in links]
    return dedupe_preserve([link for link in cleaned if link])[:10]


def relpath_for_source(dest_path: Path, archive_dir: Path, source: str) -> str:
    target = archive_dir / source
    rel = os.path.relpath(target, dest_path.parent)
    return Path(rel).as_posix()


def build_markdown_page(
    title: str,
    draft: bool,
    source_paths: list[str],
    archive_dir: Path,
    dest_path: Path,
) -> str:
    headings: list[str] = []
    bullets: list[str] = []
    paragraphs: list[str] = []
    links: list[str] = []
    for source in source_paths:
        source_path = archive_dir / source
        try:
            text = source_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        data = extract_markdown_data(text)
        headings.extend(data["headings"])
        bullets.extend(data["bullets"])
        paragraphs.extend(data["paragraphs"])
        links.extend(data["links"])

    what_this_covers = build_learning_objectives(title, headings, bullets, paragraphs)[:3]
    learning_objectives = build_learning_objectives(title, headings, bullets, paragraphs)
    summary = build_summary(paragraphs, bullets)
    approach = build_approach(headings, bullets)
    red_flags = extract_keyword_lines(
        bullets + paragraphs, RED_FLAG_KEYWORDS, max_items=5
    )
    pitfalls = extract_keyword_lines(
        bullets + paragraphs, PITFALL_KEYWORDS, max_items=5
    )
    references = extract_references(links)

    lines = [
        "---",
        f"title: {title}",
        f"draft: {'true' if draft else 'false'}",
        "---",
        "",
        "## What this covers",
    ]
    if what_this_covers:
        lines.extend(f"- {item}" for item in what_this_covers)
    else:
        lines.append("- TODO: Summarize key sections from the source notes.")
    lines.extend(
        [
            "",
            "## Learning objectives",
        ]
    )
    if learning_objectives:
        lines.extend(f"- {item}" for item in learning_objectives[:7])
    else:
        lines.extend(
            [
                "- TODO: Define the core learning goals for this topic.",
                "- TODO: Identify 3–7 key takeaways for residents.",
                "- TODO: Clarify what decisions this talk supports.",
            ]
        )

    lines.extend(["", "## Bottom line / summary"])
    if summary:
        lines.extend(f"- {item}" for item in summary)
    else:
        lines.extend(
            [
                "- TODO: Summarize the highest-yield point.",
                "- TODO: Summarize the second-highest-yield point.",
                "- TODO: Summarize the third-highest-yield point.",
                "- TODO: Summarize the fourth-highest-yield point.",
                "- TODO: Summarize the fifth-highest-yield point.",
            ]
        )

    lines.extend(["", "## Approach"])
    if approach:
        for idx, item in enumerate(approach, start=1):
            lines.append(f"{idx}. {item}")
    else:
        lines.extend(
            [
                "1. TODO: Outline the initial assessment or decision point.",
                "2. TODO: Outline the next diagnostic or management step.",
                "3. TODO: Outline follow-up or escalation criteria.",
            ]
        )

    lines.extend(["", "## Red flags / when to escalate"])
    if red_flags:
        lines.extend(f"- {item}" for item in red_flags)
    else:
        lines.append("- TODO: List red flags that require urgent escalation.")

    lines.extend(["", "## Common pitfalls"])
    if pitfalls:
        lines.extend(f"- {item}" for item in pitfalls)
    else:
        lines.append("- TODO: Capture common errors or missed steps.")

    lines.extend(["", "## References"])
    if references:
        lines.extend(f"- {item}" for item in references)
    else:
        lines.append("TODO: Add landmark references or guideline citations.")

    lines.append("")
    lines.append("## Source notes")
    for source in source_paths:
        include_path = relpath_for_source(
            dest_path, archive_dir.parent / "include" / "source-notes", source
        )
        lines.extend(
            [
                "",
                f"### {title_case(Path(source).stem.replace('-', ' ').replace('_', ' '))}",
                f'{{{{< include "{include_path}" >}}}}',
            ]
        )

    lines.extend(["", "## Source materials"])
    for source in source_paths:
        link_path = relpath_for_source(dest_path, archive_dir, source)
        lines.append(f"- [{source}]({quote(link_path, safe='/')})")
    lines.append("")
    return "\n".join(lines)


def slide_sort_key(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def extract_pptx_slides(path: Path) -> list[list[str]]:
    slides: list[list[str]] = []
    try:
        with zipfile.ZipFile(path) as handle:
            slide_files = [
                name
                for name in handle.namelist()
                if name.startswith("ppt/slides/slide") and name.endswith(".xml")
            ]
            for slide_file in sorted(slide_files, key=slide_sort_key):
                try:
                    xml = handle.read(slide_file)
                except KeyError:
                    slides.append([])
                    continue
                try:
                    root = ET.fromstring(xml)
                except ET.ParseError:
                    slides.append([])
                    continue
                slide_lines: list[str] = []
                for paragraph in root.iterfind(".//{*}p"):
                    texts = [t.text for t in paragraph.iterfind(".//{*}t") if t.text]
                    if not texts:
                        continue
                    line = clean_text("".join(texts))
                    if line:
                        slide_lines.append(line)
                slides.append(dedupe_preserve(slide_lines))
    except OSError:
        return []
    return slides


def build_slide_summary(slides: list[list[str]], max_items: int = 12) -> list[str]:
    summary: list[str] = []
    for slide in slides:
        if slide:
            summary.append(clean_text(slide[0]))
        if len(summary) >= max_items:
            break
    if len(summary) < max_items:
        for slide in slides:
            for line in slide[1:]:
                summary.append(clean_text(line))
                if len(summary) >= max_items:
                    break
            if len(summary) >= max_items:
                break
    return dedupe_preserve(summary)[:max_items]


def build_slide_page(
    title: str,
    draft: bool,
    source_paths: list[str],
    archive_dir: Path,
    dest_path: Path,
) -> str:
    slides: list[list[str]] = []
    for source in source_paths:
        if not source.lower().endswith(".pptx"):
            continue
        pptx_path = archive_dir / source
        slides = extract_pptx_slides(pptx_path)
        if slides:
            break

    summary = build_slide_summary(slides)
    learning_objectives = summary[:5]
    bottom_line = summary[:5]

    lines = [
        "---",
        f"title: {title}",
        f"draft: {'true' if draft else 'false'}",
        "---",
        "",
        "## Summary",
    ]
    if summary:
        lines.extend(f"- {item}" for item in summary)
    else:
        lines.append("TODO: Summarize the slide/PDF content once curated.")

    if slides:
        lines.extend(["", "## Slide outline"])
        for idx, slide in enumerate(slides, start=1):
            lines.append(f"### Slide {idx}")
            if slide:
                lines.extend(f"- {item}" for item in slide)
            else:
                lines.append("- TODO: No text extracted from this slide.")
        lines.append("")

    lines.extend(["", "## Learning objectives"])
    if learning_objectives:
        lines.extend(f"- {item}" for item in learning_objectives)
    else:
        lines.extend(
            [
                "- TODO: Define the core learning goals for this topic.",
                "- TODO: Identify 3–7 key takeaways for residents.",
                "- TODO: Clarify what decisions this talk supports.",
            ]
        )

    lines.extend(["", "## Bottom line / summary"])
    if bottom_line:
        lines.extend(f"- {item}" for item in bottom_line)
    else:
        lines.extend(
            [
                "- TODO: Summarize the highest-yield point.",
                "- TODO: Summarize the second-highest-yield point.",
                "- TODO: Summarize the third-highest-yield point.",
                "- TODO: Summarize the fourth-highest-yield point.",
                "- TODO: Summarize the fifth-highest-yield point.",
            ]
        )

    lines.extend(
        [
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
            "## Slides and assets",
        ]
    )

    for source in source_paths:
        link_path = relpath_for_source(dest_path, archive_dir, source)
        lines.append(f"- [{source}]({quote(link_path, safe='/')})")

    lines.extend(["", "## Source materials"])
    for source in source_paths:
        link_path = relpath_for_source(dest_path, archive_dir, source)
        lines.append(f"- [{source}]({quote(link_path, safe='/')})")
    lines.append("")
    return "\n".join(lines)


def read_front_matter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def main() -> None:
    parser = argparse.ArgumentParser(description="Populate talk pages from archive.")
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
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    manifest_path = (root / args.manifest).resolve()
    archive_dir = (root / args.archive).resolve()
    if not manifest_path.exists():
        raise SystemExit(f"Manifest not found: {manifest_path}")
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or []

    grouped: dict[str, list[dict]] = {}
    for entry in manifest:
        grouped.setdefault(entry["dest_page"], []).append(entry)

    updated = 0
    for dest_page in sorted(grouped.keys()):
        dest_path = (root / dest_page).resolve()
        entries = grouped[dest_page]
        kinds = {entry["kind"] for entry in entries}
        source_paths = [entry["source_path"] for entry in entries]
        front_matter = read_front_matter(dest_path) if dest_path.exists() else {}
        title = str(front_matter.get("title") or entries[0]["title"])
        draft = bool(front_matter.get("draft", True))

        if "markdown" in kinds:
            content = build_markdown_page(
                title=title,
                draft=draft,
                source_paths=source_paths,
                archive_dir=archive_dir,
                dest_path=dest_path,
            )
        else:
            content = build_slide_page(
                title=title,
                draft=draft,
                source_paths=source_paths,
                archive_dir=archive_dir,
                dest_path=dest_path,
            )

        if not args.dry_run:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_text(content, encoding="utf-8")
        updated += 1

    print(f"Updated {updated} talk page(s).")


if __name__ == "__main__":
    main()
