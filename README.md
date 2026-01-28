# Clinical Talks

Resident-facing clinical talk pages built with Quarto.

Site: https://reblocke.github.io/clinical_talks/

## Repo layout (current)
- `index.qmd`: landing page
- `_quarto.yml`: site config + navigation
- `talks/`: one `.qmd` per talk (generated + editable)
- `archive/`: raw source notes (do not modify)
- `include/source-notes/`: normalized markdown copies of `archive/` used for rendering
- `content/manifest.yml`: inventory of archive files → talk pages
- `content/chapters.yml`: derived nav structure
- `docs/`: rendered site output (GitHub Pages)

## Preview locally
1. Install Quarto: https://quarto.org/
2. From repo root, run:
   - `quarto preview`

## Render for publishing
- `quarto render` builds the site into `docs/`.
- GitHub Pages publishes from `docs/` on `main`.
- Keep `.nojekyll` at the repo root.

## Generate / update talk pages
When you add or change source material in `archive/`:
1. Rebuild the manifest:
   - `python3 scripts/build_manifest.py`
2. Regenerate talk pages + navigation:
   - `python3 scripts/generate_talks.py`
3. Normalize archive markdown (fix heading spacing, etc.):
   - `python3 scripts/normalize_archive_markdown.py`
4. Populate talk pages with draft content:
   - `python3 scripts/populate_talks.py`

Notes:
- Talk pages remain editable; re-running scripts will overwrite generated sections.
- Source notes at the bottom of each talk are included from `include/source-notes/`.

## Scripts (summary)
- `scripts/build_manifest.py`: index archive files into `content/manifest.yml`
- `scripts/generate_talks.py`: create talk pages + update navigation
- `scripts/normalize_archive_markdown.py`: clean heading formatting (without touching `archive/`)
- `scripts/populate_talks.py`: draft talk content from archive notes and PPTX slide text

## Source materials
Raw notes, slides, and PDFs live in `archive/`. Treat these as source-of-truth inputs and
avoid rewriting or deleting them. The site renders normalized copies from
`include/source-notes/` to keep headings Quarto-friendly.
