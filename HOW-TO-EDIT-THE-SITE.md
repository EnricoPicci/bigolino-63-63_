# How to edit the 63-63 website

## Where the texts are

All website texts are in the `content/` folder, with two subfolders:
- `content/it/` - Italian texts
- `content/en/` - English texts

Each section has its own file:

| File (IT) | File (EN) | Section |
|-----------|-----------|---------|
| `hero.md` | `hero.md` | Title and event date |
| `storia.md` | `story.md` | The friendship story |
| `giovanni.md` | `giovanni.md` | Giovanni's profile |
| `enrico.md` | `enrico.md` | Enrico's profile |
| `stefano.md` | `stefano.md` | Stefano's profile |
| `gigio.md` | `gigio.md` | Gigio's profile |
| `spettro-politico.md` | `political-spectrum.md` | The political spectrum |
| `luogo.md` | `venue.md` | The venue and directions |
| `dove-dormire.md` | `where-to-stay.md` | Where to stay |
| `footer.md` | `footer.md` | Footer text |

Files are in **Markdown** format, a simple text format:
- `# Title` = large title
- `## Subtitle` = subtitle
- `**bold**` = **bold**
- `*italic*` = *italic*
- `- item` = bullet list

## How to edit text (from GitHub.com)

1. Go to [github.com](https://github.com) and open the project repository
2. Navigate to the `content/en/` folder (or `content/it/` for Italian)
3. Click on the file you want to edit (e.g., `giovanni.md`)
4. Click the **pencil icon** (Edit this file) at the top right
5. Edit the text
6. Click the green **"Commit changes..."** button
7. Write a short description of your change
8. Click **"Commit changes"**
9. Wait a few minutes: a GitHub Action will automatically rebuild the site

**Important**: remember to edit both the Italian and English files!

## How to add a photo

1. Go to GitHub.com and open the repository
2. Navigate to the `pictures/` folder
3. Click **"Add file"** -> **"Upload files"**
4. Drag and drop the photos you want to add
5. Click **"Commit changes"**
6. The photo will automatically appear in the site gallery

## How to edit locally (for git users)

1. `git pull` (to get latest changes)
2. Edit files in the `content/` folder with any text editor
3. To add photos, copy them to the `pictures/` folder
4. `git add .`
5. `git commit -m "description of changes"`
   - The pre-commit hook will rebuild the site and run tests automatically
   - If tests fail, the commit is blocked and you'll see an error message
6. `git push`

## First-time setup (local workflow only)

```bash
bash scripts/setup.sh
```

This installs the pre-commit hook and verifies everything works.

## What NOT to edit

- `index.html` - Auto-generated. Manual changes will be overwritten.
- `template.html` - HTML structure. Only edit if you know what you're doing.
- `css/style.css` - Styles. Only edit if you want to change the visual design.
- `js/main.js` - JavaScript code. Don't touch.
- `scripts/` - Build and test scripts. Don't touch.
