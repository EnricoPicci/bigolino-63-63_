# Cloudflare Web Analytics — Setup Guide for 63-63

## Overview

Cloudflare Web Analytics is a free, privacy-first analytics service. It works on any website (no need to use Cloudflare as your DNS or CDN). It does **not** use cookies, so no GDPR cookie banner is required.

**What you get**: a dashboard at cloudflare.com showing page views, unique visitors, top pages, countries, devices, and referrers.

**What you don't get**: a visible counter on the page itself (stats are only in the Cloudflare dashboard).

---

## Step 1: Create a Cloudflare account

1. Go to [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)
2. Enter your email and a password
3. Verify your email address
4. You now have a free Cloudflare account — no credit card needed

---

## Step 2: Set up Web Analytics for your site

1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/)
2. In the left sidebar, click **Analytics & Logs** → **Web Analytics**
3. Click **Add a site**
4. Enter your site hostname: `bigolino-63-63.it`
5. A confirmation box appears — select it to confirm, then click **Done**
6. You're back on the Web Analytics page. Your site now appears as a card.
7. Click **"Manage site"** on that card
8. The JavaScript snippet is shown here. It looks like this:

```html
<!-- Cloudflare Web Analytics -->
<script defer src='https://static.cloudflareinsights.com/beacon.min.js'
  data-cf-beacon='{"token": "YOUR_TOKEN_HERE"}'>
</script>
<!-- End Cloudflare Web Analytics -->
```

9. **Copy this snippet** — you'll need it in the next step

---

## Step 3: Add the snippet to template.html

Open `template.html` and paste the snippet **just before** the closing `</body>` tag, right after the existing `<script>` tag:

```html
<script src="js/main.js"></script>

<!-- Cloudflare Web Analytics -->
<script defer src='https://static.cloudflareinsights.com/beacon.min.js'
  data-cf-beacon='{"token": "YOUR_TOKEN_HERE"}'>
</script>
<!-- End Cloudflare Web Analytics -->
</body>
</html>
```

Replace `YOUR_TOKEN_HERE` with the actual token from step 2.

---

## Step 4: Rebuild and deploy

```bash
# Rebuild the site
python3 scripts/build.py

# Run the tests
python3 scripts/test.py

# Commit and push
git add template.html index.html
git commit -m "Add Cloudflare Web Analytics"
git push
```

The pre-commit hook will rebuild and test automatically, but you can also run the commands manually first to verify.

---

## Step 5: Verify it works

1. Wait a few minutes after deploying
2. Visit your site in a browser
3. Go back to the Cloudflare dashboard → **Web Analytics**
4. You should see your first page view appear within a few minutes

---

## Viewing your stats

- Log in to [https://dash.cloudflare.com/](https://dash.cloudflare.com/)
- Go to **Analytics & Logs** → **Web Analytics**
- Select your site
- You'll see:
  - **Page views** — total and over time
  - **Unique visitors** — deduplicated (without cookies, based on IP + user agent hashing)
  - **Top pages** — which pages get the most visits (main page vs. Tomba Brion, etc.)
  - **Countries** — where your visitors are coming from
  - **Devices** — mobile vs. desktop
  - **Referrers** — how visitors found your site (e.g., WhatsApp link, direct, etc.)

---

## Notes

- **Privacy**: The script does not use cookies, does not track users across sites, and does not collect personal data. No GDPR consent banner needed.
- **Performance**: The `beacon.min.js` script is ~6KB gzipped and loaded with `defer`, so it won't slow down page rendering.
- **Cost**: Completely free, no usage limits.
- **No visible counter**: If you later want a visible "N visitors" counter on the page itself, you'd need to combine this with another approach (e.g., GoatCounter or hits.sh) since Cloudflare doesn't expose a public counter API.
