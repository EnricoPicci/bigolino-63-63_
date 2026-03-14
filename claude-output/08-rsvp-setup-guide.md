# RSVP Setup Guide

The website now has an RSVP section (right after the hero). It shows a placeholder iframe that you need to connect to a real Google Form. This document walks you through every step.

---

## Step 1: Create the Google Form

1. Go to [Google Forms](https://docs.google.com/forms/) and sign in
2. Click **Blank form** (or the `+` button)
3. Set the form title: **RSVP - Festa 63-63**
4. Add these fields:

| # | Field            | Type                | Options / Notes                              |
|---|------------------|---------------------|----------------------------------------------|
| 1 | Nome / Name      | Short answer        | Required. Description: "Nome e cognome"      |
| 2 | Email            | Short answer        | Required. Turn on "Response validation" → "Text" → "Email" |
| 3 | Ci sarai? / Will you attend? | Multiple choice | Required. Options: **Si / Yes**, **No**, **Forse / Maybe** |
| 4 | Numero di accompagnatori / Number of guests | Dropdown | Options: **0**, **1**, **2**, **3**, **4+**  |
| 5 | Note             | Paragraph (long answer) | Optional. Description: "Allergie, richieste speciali / Allergies, special requests" |

### Form settings to configure

- Click the **Settings** tab (gear icon at top)
- **Responses** → turn ON "Collect email addresses" if you want Google to capture emails automatically (then you can remove the manual Email field)
- **Presentation** → set a confirmation message, e.g.: *"Grazie! Ci vediamo il 27 giugno. / Thank you! See you on June 27th."*
- **Responses** → turn ON "Get email notifications for new responses" so you get alerts

---

## Step 2: Get the two URLs you need

You need two different URLs from the form: the **embed URL** (for the iframe) and the **regular URL** (for the fallback link).

### 2a. Get the regular form URL

1. Click the **Send** button (top right of the form editor)
2. Click the **link icon** (chain icon, middle tab)
3. Optionally check "Shorten URL"
4. Copy the URL — it looks like:
   ```
   https://docs.google.com/forms/d/e/LONG_ID_HERE/viewform
   ```
   This is your **GOOGLE_FORM_URL**.

### 2b. Get the embed URL

1. Still in the Send dialog, click the **< >** icon (the rightmost tab, "Embed HTML")
2. Google shows you an `<iframe>` snippet. Inside it, find the `src="..."` value. It looks like:
   ```
   https://docs.google.com/forms/d/e/LONG_ID_HERE/viewform?embedded=true
   ```
   This is your **GOOGLE_FORM_EMBED_URL**.

> **Important:** The embed URL is the regular URL with `?embedded=true` appended. If you already have the regular URL, you can just add `?embedded=true` yourself.

---

## Step 3: Update template.html

Open `template.html` and find the RSVP section (around line 38). You need to replace three placeholder strings:

### 3a. Replace the iframe src (line 48)

Find:
```html
src="GOOGLE_FORM_EMBED_URL"
```
Replace with your embed URL:
```html
src="https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?embedded=true"
```

### 3b. Replace both fallback links (lines 54 and 62)

Find both occurrences of:
```html
href="GOOGLE_FORM_URL"
```
Replace each with your regular form URL:
```html
href="https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"
```

There are exactly **2 occurrences** of `GOOGLE_FORM_URL` in the file — one in the `<small>` link below the iframe, and one in the `<noscript>` block.

### Summary of replacements

| Placeholder             | Count | Replace with                                              |
|-------------------------|-------|-----------------------------------------------------------|
| `GOOGLE_FORM_EMBED_URL` | 1     | `https://docs.google.com/forms/d/e/YOUR_ID/viewform?embedded=true` |
| `GOOGLE_FORM_URL`       | 2     | `https://docs.google.com/forms/d/e/YOUR_ID/viewform`      |

---

## Step 4: Adjust iframe height (optional)

The iframe is currently set to `height="800"` (line 49 of `template.html`). After you connect the real form:

1. Open the site locally or on GitHub Pages
2. Check if the form fits without internal scrolling
3. If the form is shorter or longer, change the `800` value:
   - 5 fields → try `700`
   - More fields or longer descriptions → try `900` or `1000`

---

## Step 5: Rebuild and test

```bash
python3 scripts/build.py
python3 scripts/test.py
```

Both should pass. Then open `index.html` in a browser and verify the form loads inside the RSVP section.

---

## Step 6: Commit and push

```bash
git add template.html
git commit -m "Connect RSVP section to Google Form"
git push
```

The pre-commit hook will rebuild `index.html` and run tests automatically.

---

## Where to find responses

- Go to your Google Form → **Responses** tab
- You can view responses in the form itself, or click the green Sheets icon to create a linked Google Sheet for easier tracking
- The Sheet updates in real time as people submit

---

## Quick checklist

- [ ] Google Form created with the fields above
- [ ] Confirmation message set
- [ ] Email notifications turned on
- [ ] `GOOGLE_FORM_EMBED_URL` replaced in `template.html` (1 place)
- [ ] `GOOGLE_FORM_URL` replaced in `template.html` (2 places)
- [ ] iframe height adjusted if needed
- [ ] `python3 scripts/build.py` runs clean
- [ ] `python3 scripts/test.py` passes
- [ ] Form loads correctly in browser
- [ ] Committed and pushed
