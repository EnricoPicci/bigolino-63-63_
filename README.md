# 63-63

Website for the "63-63" party: four friends born in 1963 celebrating turning 63.

**Date**: June 27th, 2026 at 19:00
**Place**: Agriturismo da Ottavio, Valdobbiadene (TV)

## Quick start

```bash
# First-time setup
bash scripts/setup.sh

# Build the site
python3 scripts/build.py

# Run tests
python3 scripts/test.py
```

## How to edit content

See [COME-MODIFICARE-IL-SITO.md](COME-MODIFICARE-IL-SITO.md) (Italian) or [HOW-TO-EDIT-THE-SITE.md](HOW-TO-EDIT-THE-SITE.md) (English).

All text content is in the `content/` folder as Markdown files. Edit those files, commit, and push. The site rebuilds automatically.

## Project structure

```
content/          Editable text (Markdown files, IT and EN)
pictures/         Photos (just drop images here)
template.html     HTML structure
css/style.css     Visual design
js/main.js        Interactivity
scripts/          Build, test, and setup scripts
index.html        Generated site (do not edit manually)
```
