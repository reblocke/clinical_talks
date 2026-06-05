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

## Repository Notes

### Project Status

No manuscript version is expected. Teaching text and slides are repository-authored unless otherwise noted; check third-party images before reuse.

### Data and Reuse

Teaching materials; verify no copyrighted images beyond fair-use/owned

### Workflow

Quarto render or README workflow

### Dependencies

Repo lockfiles/requirements

### Citation

No publication DOI is assigned to this repository. Cite the GitHub repository URL and the commit or release used.

### License

MIT License for repository code; see `LICENSE`. Third-party and publisher materials remain under their original terms.

### Contact

Maintainer: Brian W. Locke (`@reblocke`). Use GitHub issues or pull requests for repository-specific questions when the repository is public.
