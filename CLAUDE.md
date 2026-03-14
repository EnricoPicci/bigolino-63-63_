# 63-63 Party Website

## Project Overview
A bilingual (IT/EN) single-page static website for a party celebrating four friends born in 1963 turning 63. Hosted on GitHub Pages.

## Architecture
- **Static site** with a build step: content lives in Markdown files, a Python build script generates `index.html`
- **No frameworks**: vanilla HTML, CSS, JavaScript
- **Content/presentation separation**: text in `content/it/*.md` and `content/en/*.md`, layout in `template.html`, styles in `css/style.css`

## Key Files
- `template.html` - HTML structure with `{{placeholder}}` markers
- `content/it/*.md`, `content/en/*.md` - All editable text (Markdown)
- `css/style.css` - All styles (mobile-first responsive)
- `js/main.js` - Language toggle, political spectrum animation, photo gallery
- `scripts/build.py` - Reads content + template, generates `index.html`
- `scripts/test.py` - Validates the generated site
- `scripts/setup.sh` - Installs git pre-commit hook
- `index.html` - GENERATED FILE, do not edit manually

## Build & Deploy
```bash
# First-time setup (installs pre-commit hook)
bash scripts/setup.sh

# Manual build
python3 scripts/build.py

# Manual test
python3 scripts/test.py
```

The pre-commit hook runs `build.py` then `test.py` automatically. GitHub Pages serves `index.html` from the `main` branch.

## Adding Content
- Edit `.md` files in `content/it/` or `content/en/`
- Add images to `pictures/` - the build script auto-discovers them
- Commit and push - the pre-commit hook rebuilds and tests before allowing the commit

## Conventions
- All text content in Markdown, never directly in HTML
- CSS uses custom properties (variables) for the color palette, defined in `:root`
- Color palette: green hills `#4a7c59`, gold prosecco `#d4a843`, cream `#faf8f0`, red `#c0392b`, navy `#2c3e6b`
- Image credits for CC-licensed images are in the footer
- The site must work without JavaScript (content visible, toggle defaults to Italian)
- Mobile-first: base styles for mobile, `@media (min-width: 768px)` for tablet/desktop

## Output Documents
- Generated documents go in `claude-output/`
- If a document is generated as part of processing a prompt file from `prompts-to-generate-app/`, it must have the same numeric prefix as that prompt file (e.g. prompt `08-add_rsvp.md` → output `08-rsvp-setup-guide.md`)

## Testing
Tests verify: all sections present, bilingual content, image references valid, HTML structure correct. Tests run as pre-commit hook and in GitHub Actions.
