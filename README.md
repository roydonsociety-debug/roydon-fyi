# roydon.fyi

An information portal for residents of Roydon, Essex. Static HTML site, no build step, no dependencies beyond Google Fonts.

Published by Friends of Roydon, an unincorporated residents' association.

---

## Contents

```
.
├── index.html              Home
├── 404.html                Not found
├── about/                  About this site
├── act/                    Take action hub
│   ├── register/             Register of concern form
│   ├── lvrpa/                Email LVRPA (4 variants)
│   ├── natural-england/      Email Natural England (3 variants)
│   ├── mp/                   Email Chris Vince MP (3 variants)
│   ├── parish/               Email Parish Council (3 variants)
│   └── object/               Dormant - activates when application lodged
├── contact/                Contact page
├── css/styles.css          All styling
├── downloads/              Briefings (.docx) and HMLR PDF
├── js/templates.js         Email variant picker
├── privacy/                Privacy policy
├── temple-farm/            Campaign hub
│   ├── briefing/             Residents' briefing (web)
│   ├── the-case/             Plain English 800-word version
│   ├── timeline/             Dated public record
│   └── evidence/             Source documents
├── thanks/                 Post-form-submission landing
├── build.py                Build script that generated all pages
└── README.md               This file
```

## Preview locally

```bash
cd path/to/site
python3 -m http.server 8000
```

Open `http://localhost:8000` in your browser. Pages should look identical to how they will appear on roydon.fyi.

---

## Deploy to Cloudflare Pages (recommended)

Cloudflare Pages is free, serves over HTTPS, includes unlimited bandwidth, and integrates cleanly with `.fyi` domains. Total time end-to-end: about 30 minutes.

### Step 1. Push the site to GitHub

1. Create a new repo on github.com — call it `roydon-fyi`. Make it public (Cloudflare Pages can also deploy from private repos but public is simpler).
2. Sign in to the GitHub account using `roydonsociety@gmail.com`.
3. Push the contents of this folder to the repo:

```bash
cd path/to/site
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/roydon-fyi.git
git push -u origin main
```

### Step 2. Connect Cloudflare Pages

1. Sign up for a free Cloudflare account at cloudflare.com (use `roydonsociety@gmail.com`).
2. From the dashboard, go to **Workers & Pages → Create application → Pages → Connect to Git**.
3. Authorise GitHub and pick the `roydon-fyi` repo.
4. Build settings:
   - **Framework preset:** None
   - **Build command:** (leave blank)
   - **Build output directory:** `/` (the root)
5. Click **Save and Deploy**.

After about 30 seconds, the site is live at `roydon-fyi.pages.dev` (or similar). Test it.

### Step 3. Connect the roydon.fyi domain

1. In Cloudflare Pages, open the project, go to **Custom domains → Set up a domain → roydon.fyi**.
2. Cloudflare will give you two DNS records to add at your registrar. Typically a CNAME or two A records. Note them down.
3. Log in to whichever registrar you bought roydon.fyi from. Navigate to DNS settings for the domain.
4. Add the records Cloudflare gave you.
5. Back in Cloudflare, click **Verify**. DNS propagation usually takes 5-30 minutes.

Once verified, `https://roydon.fyi` is live. The site has free HTTPS automatically.

### Step 4. Set up email forwarding

If you haven't already, set up forwarding for `info@roydon.fyi` and `chair@roydon.fyi` (or whatever variants you want) at your registrar. Each forwards to `roydonsociety@gmail.com`. This makes formal emails from the domain land in your existing Gmail.

To send *from* `info@roydon.fyi` in Gmail:
1. Gmail → Settings → Accounts and Import → Send mail as → Add another email address.
2. Add `info@roydon.fyi`, treat as alias.
3. Use the SMTP server provided by your domain registrar's forwarding service (varies by registrar — Namecheap, ImprovMX, Cloudflare Email Routing all work).

---

## Set up the register of concern form

The register page (`/act/register/`) contains a placeholder where the form should be embedded. To activate it:

1. Sign in to forms.google.com on the `roydonsociety@gmail.com` account.
2. Click **+ Blank** to create a new form.
3. Title it: **Register of concern — Temple Farm**.
4. Add the following questions:
   - **Full name** — short answer, required
   - **Full address including postcode** — short answer, required
   - **Email address (optional)** — short answer, optional, response validation set to email
   - **Why this matters to you (optional)** — paragraph, optional
   - **Consent** — checkbox with a single option: "I am happy for my name and address to be cited in submissions to planning bodies on Temple Farm", required
5. In the form settings (cog icon), under **Presentation**:
   - Set confirmation message to: "Thank you. Your concern has been registered."
   - Tick "Show link to submit another response" — uncheck it.
6. Click **Send**, then the embed icon `<>`.
7. Copy the iframe HTML.
8. Open `act/register/index.html`.
9. Find the comment block starting `<!-- TO ENABLE THE FORM`.
10. Replace the placeholder `<div>` with the iframe HTML.
11. Commit and push. Cloudflare Pages will redeploy automatically.

Submissions land in a private Google Sheet linked to the form. Only you (signed into the campaign Gmail) can see it.

---

## How content is generated

Every HTML file in this repo was generated by `build.py`. If you want to edit content:

**Quick edits.** Open the relevant HTML file directly and edit the markup. Commit and push.

**Larger edits or new pages.** Edit `build.py` and re-run:

```bash
python3 build.py
```

This rewrites all HTML pages from the single source of truth. Useful for changing the masthead, the footer, or any boilerplate that appears across pages.

---

## Adding a new email template variant

Each action page has 3 or 4 email template variants. To add a new one, edit `build.py`:

1. Find the relevant list (e.g. `LVRPA_VARIANTS`).
2. Add a new dict with `"subject"` and `"body"` keys.
3. Re-run `python3 build.py`.
4. Commit and push.

The variant picker in `js/templates.js` will pick from the new pool randomly on each page load.

---

## When a planning application is lodged

The most important page on the site becomes `/act/object/`. To activate it:

1. Edit `act/object/index.html` (or the relevant section in `build.py`).
2. Replace the "Currently dormant" panel with:
   - Application reference number
   - Case officer name and email at EFDC
   - Direct link to EFDC planning portal page
   - Consultation deadline (e.g. "Objections must be submitted by 5pm on 14 June 2026")
   - A countdown to the deadline (a few lines of JavaScript can do this)
   - 3 or 4 pre-drafted objection email templates following the same pattern as the LVRPA / NE / MP pages
3. Move the "Object" tile on `/act/index.html` to the top of the grid and remove the `disabled` class.
4. Add a timeline entry on `/temple-farm/timeline/`.
5. Add a news entry on the homepage.
6. Commit and push.

If the campaign mailing list is in place, send a notification email to everyone on the register of concern with their consent ticked.

---

## Notes on the design

- **Typography:** Fraunces (display, variable serif) and Manrope (body, geometric sans), both from Google Fonts.
- **Colours:** Parchment background (#F7F3EA), forest green accent (#2D4A2B, matching Lee Valley), brick red for urgent items (#A8392B).
- **Layout:** Editorial / newspaper-style. Sticky masthead, issue line under it, generous whitespace, hairline rules separating sections.
- **No tracking, no analytics, no cookies.** The site weighs under 200KB and loads in under a second.

---

## Maintenance

Run by Friends of Roydon. To pass maintenance to a new volunteer, share access to:
1. The `roydonsociety@gmail.com` Gmail account.
2. The Cloudflare account (or invite as a collaborator on the Pages project).
3. The GitHub repo (add as collaborator).
4. The domain registrar account (for DNS changes and renewal).

The whole stack is reproducible from this repo plus the credentials above.

---

## Licence

The content (text, briefings, evidence) is free for non-commercial use by Roydon residents and Friends of Roydon. Attribution to roydon.fyi appreciated.

The site framework (HTML, CSS, JS, build script) is provided as-is for community / civic use.
