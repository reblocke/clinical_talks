# Clinical Talks — Codex instructions

## Project intent
Maintain the existing resident-facing Clinical Talks Quarto site, with one topic per page. The initial port from `intro_clin_research` is complete; use that sibling only as a reference when a requested change needs it.

For content-generation work, `archive/` supplies source notes, `include/source-notes/` contains normalized copies, and `content/manifest.yml` / `content/chapters.yml` record page and navigation mappings. The commands under “Generate / update talk pages” in `README.md` can overwrite generated sections; inspect the affected source and requested scope before invoking them.

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
- Do not change remote state, push, or publish releases unless explicitly asked. Read-only repository inspection is allowed.
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

## Workflow
- Inspect the working state and preserve unrelated edits. Continue within the requested scope; ask only when target changes conflict or a material decision is unresolved.
- An implementation request includes local source edits, relevant rendering/inspection, and fixing regressions caused by the change. Do not stop after the first implementation if those steps remain.
- For prose edits, inspect the affected page and links and run `git diff --check`. Render the affected `.qmd` page when content or layout changes need visual verification.
- For site configuration, navigation, or shared-template changes, use `quarto check` and `quarto render`, then inspect affected pages and navigation in the browser. Keep publishing separate from local validation.
- Use generation scripts only for requested generation work; ordinary page edits do not require rebuilding the source manifest or repopulating all talks.

## Definition of done
- Requested pages/configuration are updated and applicable local checks pass; report missing Quarto/runtime prerequisites explicitly.
- Affected navigation and links work; `archive/` remains intact.
- Update `README.md` when preview/build commands, adding-talk instructions, or source locations change.
