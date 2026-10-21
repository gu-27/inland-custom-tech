# Inland Custom Tech

Read this first, every session.

Spokane technology consultancy. Build, Consult, Train across Automation, Analytics, and
AI. Owner: John Correia. Full brand rules live in [BRAND.md](BRAND.md). This file is the
short version plus the repo rules.

**Returning cold?** Read [docs/SESSION-LOG.md](docs/SESSION-LOG.md) first. It says what
state the work is in and what is waiting on John.

## What this repo is

A small static storefront. No build step, no framework, no dependencies. A home page with
inline CSS, ten service pages sharing one stylesheet, and a short script on each.

```
site/          deployable root (Cloudflare Pages serves this directory)
  index.html   the home page
  js/site.js   booking URLs + the wiring that applies them. Loaded by every page
  services/    one page per step of "Your path", plus service.css
  img/         favicons, og-image, headshot, logo SVG
brand/logos/   master logo and icon files (SVG + PNG)
print/         business card PDF and preview
docs/EVIDENCE.md  what John has actually built, and what may be published
BRAND.md       full brand rules, source of truth
```

The home page is still one file with inline CSS. The service pages share
`services/service.css` rather than repeating it nine times.

## Hard rules

1. **Do not touch `gu-27/inland-nw-ai` or inlandnw.ai from this repo.** That is the old
   Inland NW AI site. It stays live during the rename. Migration is a separate approved
   plan.
2. **Do not retype the logo.** The wordmark is outlined vector in the SVGs and in the
   inline `<svg class="logo">` in `index.html`. Copy the paths, never re-set the type.
3. **Booking URLs live in one place:** the `SITE` object in `site/js/site.js`, loaded by
   the home page and by every service page. `scheduleUrl` feeds every `a[data-schedule]`
   button. `calendarEmbedUrl` feeds the `iframe[data-cal-embed]`. The markup carries the
   same values so the pages still work with JS off. Change both spots or change neither.
4. **No new fonts, no new colors.** The palette below is closed. No tan, no green, no
   tinted backgrounds, no gradients, no textures.
5. **No robot, brain, or circuit imagery.** AI lives in the services, not the visuals.
6. **Back every claim about John with evidence.** Before making any claim about John's
   experience on the site, check [docs/EVIDENCE.md](docs/EVIDENCE.md) and the `gu-27`
   repos for support. If none exists, ask John. Never invent. Items flagged ASK-JOHN in
   that file stay off the site until he approves them, and no client, pro team, student,
   or Gonzaga project may be named. Gonzaga roles are plain text only: no logos, no
   Gonzaga branding.
7. **No prices on this site.** The pricing section was removed on purpose. The offer is
   the free consultation, and nothing else carries a number.

## Palette

| Token | Hex | Use |
|---|---|---|
| black | `#141413` | Headings, body text, buttons, logo |
| graphite | `#262624` | Dark bands only: values strip, closing CTA |
| orange | `#D97757` | The logo dot, "Custom", primary buttons, key headline words, dots, highlighted boxes in the Your path flow (black text on orange) |
| paper | `#FAF9F6` | Main background (A) |
| stone | `#ECEAE5` | Alternating section background (B) |
| muted | `#3D3C39` | Body copy |
| soft | `#6B6A65` | Small labels |
| hairline | `#E3E0D9` | Thin borders |

Orange text only at 28px and up. Small orange text fails contrast on light backgrounds.
Primary buttons are orange fill with black text, never white text.

## Type

**Manrope** (Google Fonts) for everything, weights 400 to 800.

- Headlines: 800, letter-spacing about `-.045em`. The emphasized half of a headline is
  either orange or weight 400, not both.
- Section titles: `clamp(38px, 6vw, 72px)` with a 3px black rule above.
- Labels: 12 to 13px, 800, uppercase, letter-spacing `.14em`, preceded by a small orange
  dot.

## Section rhythm

Alternate paper (A) and stone (B) down the page. Graphite is punctuation, used twice:
the values strip and the closing CTA band. Current order:

```
hero paper · [graphite strip] · who stone · path paper ·
[graphite close] · about stone · contact paper · footer stone
```

Service pages run their own short rhythm: hero paper · blocks stone · why john paper ·
example stone · [graphite close] · footer stone. A page with no real example drops the
example section entirely. Never publish an "example coming soon" placeholder.

Adding a section means taking the next ground in the alternation. Do not add a third
graphite band.

## Components

- Buttons: primary is orange fill with black text, 12px radius. Secondary is a 2px black
  outline.
- Cards: 2px black border, 20px radius, no fill on light backgrounds.
- The open C with the orange dot is the thread. It repeats as the hero mark, the section
  dots, the step numbers, and the label bullets.

## Voice

Warm, plain, jargon-free. A capable neighbor, not a faceless tech firm. Lead with the
customer's problem, not the technology.

- Say what a thing does. Do not sell it.
- No em dashes. Use a period, a comma, a colon, or parentheses.
- Short sentences. One idea each.
- Cut "leverage", "seamless", "robust", "holistic", "cutting-edge", "solutions provider".
- Headline pattern: a plain statement, with the second half carrying the emphasis.
  "Technology, made simple." "Find your starting point." "Let's figure it out together."

## Contact facts

John Correia · Founder · Builder · Trainer · Consultant
(509) 795-0112 · john@inlandcustomtech.com · inlandcustomtech.com
Spokane · Coeur d'Alene · Inland Northwest
Booking: https://calendar.app.google/bfwvT6jSwvPMqio67

## Deploy

Cloudflare Pages project `inland-custom-tech`, serving `site/`.

```
wrangler pages deploy site --project-name=inland-custom-tech
```

Check a change at a real phone width before shipping. Headless Chrome on macOS ignores
`--window-size`, so screenshotting at 390 captures a 485px layout and looks broken when
it is not. Load the page in a 390px iframe and measure
`documentElement.scrollWidth` instead.
