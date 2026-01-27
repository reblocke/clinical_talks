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
1. Create a new stub in `talks/<slug>.qmd` using the standard template.
2. Add the new page to the `book.chapters` list in `_quarto.yml`.
3. Link any source materials from `archive/` in the talk’s “Source materials” section.

## Source materials
Raw notes, slides, and PDFs live in `archive/`. Treat these as source-of-truth inputs and
avoid rewriting or deleting them during the initial port.
