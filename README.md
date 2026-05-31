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

## LLM and Repository Readiness Notes

### Description
Clinical talks and rendered teaching material

### Instructions
Start with this README, then inspect the files listed under Repository Layout. For computational workflows, run commands from the repository root and avoid committing generated outputs unless a release explicitly calls for them.

### Authors, Funding, and Acknowledgments
Maintainer: Brian W. Locke (`@reblocke`, ORCID 0000-0002-3588-5238). Preserve any project-specific author, funding, and acknowledgment details already listed elsewhere in the repository or accompanying publication.

### Repository Layout
- `.DS_Store`
- `.nojekyll`
- `AGENTS.md`
- `LICENSE`
- `Locke PGR Prediction and Action.pptx`
- `README.md`
- `_quarto.yml`
- `archive/.DS_Store`
- `archive/index.md`
- `archive/medical-education.md`
- `archive/procedure-index.md`
- `content/chapters.yml`
- `content/manifest.yml`
- `docs/.nojekyll`

### Data and Codebook
Teaching materials; verify no copyrighted images beyond fair-use/owned

### Workflow / Script Order
Quarto render or README workflow

### Dependencies / Environment
Repo lockfiles/requirements

### Citation
No publication DOI is assigned to this repository. Cite the GitHub repository URL and the commit or release used.

### License
Repository license status: MIT. See the root license file when present. Third-party and publisher materials remain under their original terms.

### Manuscript Status
No manuscript version expected Teaching text/slides owned where authored; check third-party images

### Contact
Maintainer: Brian W. Locke (`@reblocke`). Use GitHub issues or pull requests for repository-specific questions when the repository is public.
