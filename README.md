# Inland Custom Tech

Storefront site for Inland Custom Tech, a Spokane technology consultancy.
Static HTML, no build step.

Live: https://inland-custom-tech.pages.dev (custom domain inlandcustomtech.com pending)

## Layout

| Path | What |
|---|---|
| `site/` | Deployable root. Cloudflare Pages serves this directory. |
| `site/index.html` | The home page: markup, CSS, and the persona toggle script. |
| `site/js/site.js` | Booking URLs, in one place, loaded by every page. |
| `site/services/` | One page per step of "Your path", plus the shared `service.css`. |
| `site/img/` | Favicons, Open Graph image, headshot. |
| `brand/logos/` | Master logo and icon files, SVG and PNG. |
| `print/` | Business card print PDF and preview. |
| `BRAND.md` | Brand rules. Source of truth. |
| `CLAUDE.md` | Short brand summary and repo rules for AI sessions. |
| `docs/DOMAIN-AND-EMAIL.md` | Connecting inlandcustomtech.com and setting up email. |
| `docs/MIGRATION-PLAN.md` | Plan for moving off inlandnw.ai. Not yet approved. |
| `docs/EVIDENCE.md` | What John has actually built, and what may be said about it publicly. |
| `scripts/connect_domain.py` | Runs the Cloudflare side of the domain and email setup. |

## Editing

Booking URLs live in the `SITE` object in `site/js/site.js`. Everything else is edited in
place. Read `CLAUDE.md` before changing anything visual, and `docs/EVIDENCE.md` before
writing any claim about John's experience.

## Deploy

```sh
wrangler pages deploy site --project-name=inland-custom-tech
```

## Related

`gu-27/inland-nw-ai` is the previous Inland NW AI site at inlandnw.ai. It stays live
during the rename. Nothing here changes it.
