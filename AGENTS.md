# Clinical Talks — Codex instructions

## Project intent
This repository is a Quarto-based set of resident-facing **Clinical Talks**: one topic per page, rendered as an HTML site (and optionally PDF).

### Primary goal (initial port)
Port the **structure** (project layout, Quarto configuration, build/deploy conventions) from the sibling repository `intro_clin_research` into this repository, but retitle the project to **Clinical Talks** and convert the chapter concept into **topic pages** (content can be left as `TODO:` placeholders).

### Secondary goal (subsequent prompts)
Use materials in `archive/` to:
- infer/curate an information architecture (topics → subtopics),
- generate talk pages from source notes,
- create internal links, navigation labels, and a lightweight taxonomy.

## Authority hierarchy
Resolve ambiguity/conflicts in this order:
1. User prompts / implementation tickets in `scripts/`
2. Existing repo configuration and conventions (`_quarto.yml`, `README.md`, etc.)
3. `intro_clin_research` (template/reference only; **do not modify it**)
4. Quarto documentation and standard conventions

## Non‑negotiables and safety
- **No PHI**: Do not add patient-identifiable information. Assume this repo may be public.
- **Treat `archive/` as source material**:
  - Do not delete, rewrite, or “clean up” archive files.
  - Prefer copying excerpts into `.qmd` pages while keeping originals intact.
- Prefer **small, reviewable diffs** over broad refactors.
- Do **not** run commands that change remote state (no `git push`, no `gh`, no release publishing) unless explicitly asked.
- Keep **network access off** by default. Do not fetch external content unless asked.

## Quarto + content conventions

### One page per talk
- Each talk is a standalone `.qmd` file.
- Target structure for each talk page (use placeholders as needed):
  - **Learning objectives** (3–7 bullets)
  - **Bottom line / summary** (5–10 lines)
  - **Approach** (structured evaluation/management steps)
  - **Red flags / when to escalate**
  - **Common pitfalls**
  - **References** (guidelines, landmark papers)
  - Optional: **Source materials** list linking back to the relevant `archive/` paths

Use `TODO:` explicitly whenever a section is intentionally incomplete.

### File naming and stable URLs
- Prefer **kebab-case** filenames for stable slugs (e.g., `talks/hyponatremia.qmd`).
- Do not rename talk files casually. If a rename is necessary:
  - update `_quarto.yml` navigation,
  - update all internal links,
  - preserve redirects where feasible (or document the change).

### Navigation and taxonomy
- Keep navigation human-friendly and consistent:
  - Group talk pages into a few high-level sections (e.g., “Cardio”, “Pulm”, “Renal”, “ID”, “ICU”).
  - Avoid deep nesting until there’s enough content to justify it.
- If tags/categories are introduced, centralize them in a small data file (e.g., `data/topics.yml`) and reference consistently.

## Repository layout expectations
- Quarto project lives at repo root with `_quarto.yml` and `index.qmd`.
- Rendered output should live in `docs/` (GitHub Pages-friendly) if that’s the adopted convention.
- Static assets go in `images/` (and/or `include/` if used by the template).
- `archive/` should be excluded from rendering except for explicit links.

## Workflow expectations (how to work in this repo)
1. Start by checking `git status`. If it isn’t clean, **summarize** and stop unless instructed otherwise.
2. Prefer working on a feature branch for non-trivial changes.
3. Implement the **smallest working Quarto site** first (then expand):
   - Title: **Clinical Talks**
   - `index.qmd` landing page that explains what this is
   - A handful of placeholder topic pages that render successfully
4. Validate locally:
   - `quarto check` (if available)
   - `quarto render`
5. End each milestone with:
   - a short summary of what changed and why,
   - verification commands run + outcomes,
   - a pointer to “Next steps” (optionally in `docs/TODO.md`).

## Definition of done (for the initial port)
- `quarto render` completes successfully.
- Site title is **Clinical Talks**.
- Navigation includes topic pages and builds without broken references.
- `archive/` remains intact and unmodified.
- `README.md` includes:
  - how to preview/build,
  - how to add a new talk page,
  - where source materials live (`archive/`).
