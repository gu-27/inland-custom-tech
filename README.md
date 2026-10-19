# Inland Custom Tech

Storefront site for Inland Custom Tech, a Spokane technology consultancy.
Static HTML, no build step.

Live: https://inland-custom-tech.pages.dev (custom domain inlandcustomtech.com pending)

## Layout

| Path | What |
|---|---|
| `site/` | Deployable root. Cloudflare Pages serves this directory. |
| `site/index.html` | The whole site: markup, CSS, and a short script. |
| `site/img/` | Favicons, Open Graph image, headshot. |
| `brand/logos/` | Master logo and icon files, SVG and PNG. |
| `print/` | Business card print PDF and preview. |
| `BRAND.md` | Brand rules. Source of truth. |
| `CLAUDE.md` | Short brand summary and repo rules for AI sessions. |

## Editing

Booking URLs live in the `SITE` object at the bottom of `site/index.html`. Everything
else is edited in place. Read `CLAUDE.md` before changing anything visual.

## Deploy

```sh
wrangler pages deploy site --project-name=inland-custom-tech
```

## Related

`gu-27/inland-nw-ai` is the previous Inland NW AI site at inlandnw.ai. It stays live
during the rename. Nothing here changes it.
