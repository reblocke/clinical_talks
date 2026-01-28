from __future__ import annotations

import argparse
import re
from pathlib import Path


FENCE_RE = re.compile(r"^(```|~~~)")


def normalize_heading_line(line: str) -> tuple[str, int]:
    prefix = ""
    rest = line
    quote_match = re.match(r"^(>+)(\s*)(.*)$", line)
    if quote_match:
        prefix = quote_match.group(1) + quote_match.group(2)
        rest = quote_match.group(3)

    if not rest.startswith("#"):
        return line, 0

    count = 0
    while count < len(rest) and rest[count] == "#":
        count += 1
    if count == 0 or count > 6:
        return line, 0

    if count < len(rest) and not rest[count].isspace():
        updated = f"{prefix}{rest[:count]} {rest[count:]}"
        return updated, 1
    return line, 0


def normalize_markdown(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out_lines: list[str] = []
    in_fence = False
    changes = 0
    for line in lines:
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        updated, delta = normalize_heading_line(line)
        out_lines.append(updated)
        changes += delta
    return "\n".join(out_lines) + "\n", changes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create normalized copies of archive markdown files."
    )
    parser.add_argument(
        "--archive",
        default="archive",
        help="Archive directory (default: archive)",
    )
    parser.add_argument(
        "--output",
        default="include/source-notes",
        help="Output directory for normalized markdown (default: include/source-notes)",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    archive_dir = (root / args.archive).resolve()
    output_dir = (root / args.output).resolve()
    if not archive_dir.exists():
        raise SystemExit(f"Archive directory not found: {archive_dir}")

    written = 0
    normalized = 0
    for path in sorted(archive_dir.rglob("*.md")):
        rel = path.relative_to(archive_dir)
        dest = output_dir / rel
        text = path.read_text(encoding="utf-8", errors="ignore")
        updated, changes = normalize_markdown(text)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(updated, encoding="utf-8")
        written += 1
        normalized += changes

    print(f"Processed {written} file(s), normalized {normalized} heading line(s).")


if __name__ == "__main__":
    main()
