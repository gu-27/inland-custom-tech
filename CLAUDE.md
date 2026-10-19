# Inland Custom Tech

Read this first, every session.

Spokane technology consultancy. Build, Consult, Train across Automation, Analytics, and
AI. Owner: John Correia. Full brand rules live in [BRAND.md](BRAND.md). This file is the
short version plus the repo rules.

## What this repo is

A one-page static storefront. No build step, no framework, no dependencies. One HTML file
with inline CSS and about 20 lines of JS.

```
site/        deployable root (Cloudflare Pages serves this directory)
  index.html the whole site
  img/       favicons, og-image, headshot
brand/logos/ master logo and icon files (SVG + PNG)
print/       business card PDF and preview
BRAND.md     full brand rules, source of truth
```

## Hard rules

1. **Do not touch `gu-27/inland-nw-ai` or inlandnw.ai from this repo.** That is the old
   Inland NW AI site. It stays live during the rename. Migration is a separate approved
   plan.
2. **Do not retype the logo.** The wordmark is outlined vector in the SVGs and in the
   inline `<svg class="logo">` in `index.html`. Copy the paths, never re-set the type.
3. **Booking URLs live in one place:** the `SITE` object at the bottom of
   `site/index.html`. `scheduleUrl` feeds every `a[data-schedule]` button.
   `calendarEmbedUrl` feeds the `iframe[data-cal-embed]`. The markup carries the same
   values so the page still works with JS off. Change both spots or change neither.
4. **No new fonts, no new colors.** The palette below is closed. No tan, no green, no
   tinted backgrounds, no gradients, no textures.
5. **No robot, brain, or circuit imagery.** AI lives in the services, not the visuals.

## Palette

| Token | Hex | Use |
|---|---|---|
| black | `#141413` | Headings, body text, buttons, logo |
| graphite | `#262624` | Dark bands only: values strip, closing CTA, featured price card |
| orange | `#D97757` | The logo dot, "Custom", primary buttons, key headline words, step numbers |
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
hero paper · [graphite strip] · who stone · matrix paper · how stone ·
pricing paper · [graphite close] · about stone · contact paper · footer stone
```

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
