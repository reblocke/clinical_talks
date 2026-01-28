# Clinical Talks

Resident-facing clinical talk outlines built with Quarto.

## Preview locally
1. Install Quarto (https://quarto.org/).
2. Run `quarto preview` from the repo root.

## Render for publishing
- Run `quarto render` to build the HTML book into `docs/`.
- GitHub Pages is configured to publish from `docs/` on `main`.
- Keep `.nojekyll` at the repo root when publishing.

## Add a new talk page
1. Add source material under `archive/` (markdown notes, slides, PDFs).
2. Regenerate the manifest with `python3 scripts/build_manifest.py`.
3. Regenerate pages + navigation with `python3 scripts/generate_talks.py`.
4. Review the generated page in `talks/<section>/<slug>.qmd` for accuracy.

## Archive manifest + tooling
- `content/manifest.yml` inventories archive materials and their destination pages.
- `content/chapters.yml` mirrors the current book structure for review.
- `scripts/build_manifest.py` and `scripts/generate_talks.py` keep the site reproducible.

## Source materials
Raw notes, slides, and PDFs live in `archive/`. Treat these as source-of-truth inputs and
avoid rewriting or deleting them during the initial port.
