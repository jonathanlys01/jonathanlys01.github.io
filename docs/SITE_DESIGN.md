# Personal site design

The personal site uses the released al-folio gems, with a small set of local overrides.
`assets/css/main.scss` holds the palette, typography, responsive layouts, and motion.
`assets/js/site-details.js` progressively adds scroll reveals and keyboard support to
bibliography disclosures. Reduced motion disables entrances and reveals; the background
aquarium also becomes a still frame. Content stays readable without JavaScript.

The homepage's selected work is curated in `_pages/about.md`. Project cards read
front matter from `_projects/`; the complete bibliography remains the source for
Publications and the web CV. Notes use a locally rendered heading and JetBrains Mono. Pages other than the CV and Publications
use a vendored ASCII aquarium (see `assets/js/ascii-sharks/README.md`).

## Downloadable CV

Regenerate the committed PDF after changing `_data/cv.yml` or `_bibliography/papers.bib`:

```sh
# Requires reportlab in the active Python environment and this site's Ruby bundle.
python3 bin/export_cv.py
```

The output is `assets/pdf/jonathan-lys-cv.pdf`. It reads the site's data directly;
there is no second copy of the CV text. Check the rendered PDF after regenerating.

## Local preview and overrides

This is a personal GitHub Pages site, so keep its empty `baseurl`:

```sh
bundle exec jekyll build
python3 -m http.server 4173 --bind 127.0.0.1 --directory _site
```

Review gem overrides with `bundle exec al-folio upgrade overrides audit` when
updating dependencies. `.al-folio-overrides.yml` records the reviewed versions.
