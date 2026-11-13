# Inland Custom Tech: brand rules

Spokane technology consultancy serving the Inland Northwest. Build, Consult, Train across Automation, Analytics, and AI.
Voice: warm, plain, jargon-free. A capable neighbor, not a faceless tech firm. Lead with the customer's problem.

## Positioning
- Claude-first, not Claude-only: "Experience with Copilot and ChatGPT. Deep implementation with Claude." Keep this low on the page; the top stays simple and human.
- Services scale with the client: personal, small business, team, organization (e.g. personal automation through enterprise automation).
- Packaged offers: Knowledge Kit, Startup Kit, Automation Starter. No prices on the site.

## Name and taglines
- Name: **Inland Custom Tech** (domain: inlandcustomtech.com). Formerly Inland NW AI (inlandnw.ai).
- Primary tagline / hero: **Technology, made simple.** ("made simple." is the emphasized half.)
- Secondary lines: "Technology, built around you." · "Custom tech for the Inland Northwest." · "What could your tech do for you?"

## Logo
- Mark: an open **C** with an orange **dot** fitted into its opening. The C is the work; the dot is the client. Never rotate the C, recolor the dot, or add effects.
- Wordmark: Manrope. "Inland" and "Tech" regular (400); **"Custom" extra-bold (800) in orange**.
- Files (`brand/logos/`):
  - `ict-logo.svg/.png`: black tile + black wordmark, for light backgrounds
  - `ict-logo-reverse.svg/.png`: off-white tile + off-white wordmark, for black/graphite backgrounds
  - `ict-icon.svg`, `icon-512.png`, `apple-touch-icon.png`, `favicon.svg`, `favicon-32.png`
  - `social-avatar.svg/.png` (circle-safe), `og-image.png` (1200×630 link preview)
- Logo type is outlined in the SVGs. Do not retype it.

## Color
| Token | Hex | Use |
|---|---|---|
| black | `#141413` | Logo, business card front, headings, body text |
| graphite | `#262624` | Dark "punctuation" bands only (values strip, closing CTA page) |
| orange | `#D97757` | The dot, "Custom", primary buttons (black text on orange), key words in headlines, step numbers, small dots |
| paper (off-white) | `#FAF9F6` | Main background (A) |
| stone | `#ECEAE5` | Alternating section background (B) |
| muted text | `#3D3C39` | Body copy |
| soft text | `#6B6A65` | Small labels |
| hairline | `#E3E0D9` | Thin borders |

Rules:
- **Section rhythm:** the site reads like a printed document. Each section is a rounded paper page (28px radius, 20px on phones) on a stone desk, 16px apart, with a running head ("Inland Custom Tech" left, page number right). Graphite is used twice only: the values strip and the closing CTA. No tan, no green, no tinted backgrounds.
- Orange text only at large sizes (headlines ~28px+). Small orange text fails contrast on light backgrounds.
- No gradients, no textures, no robot/brain/circuit imagery. AI lives in the services, not the visuals.

## Type
- **Manrope** (Google Fonts) for everything. Headlines 800 with tight tracking (about -0.045em); emphasized half of a headline either orange or weight 400.
- Section titles: very large (≈38–72px), each with a 3px black rule above.
- Labels: 12–13px, 800, uppercase, letter-spacing .14em, preceded by a small orange dot.

## Components (see `site/index.html` for the reference implementation)
- Buttons: primary = orange fill, black text, 12px radius; secondary = 2px black outline.
- Cards: 2px black border, 20px radius, no fill on light backgrounds.
- Hero: headline and buttons on the left, three lanes on the right (Automation, Analytics, AI). Each lane is a black-outlined card with a small diagram on a stone panel: black strokes, soft-gray dashed lines for manual or optional steps, orange for the outcome.
- Diagrams: drawn in the palette only. Solid black = the path that works; dashed soft gray = the old or optional way; one orange element = the result. The open C stands in for "your knowledge" in AI diagrams, never a brain.
- Third-party tool marks ("Built with" section): one color only, soft gray `#6B6A65`, with Claude set apart in orange. Use official marks from the company or a vetted source; where a brand's rules forbid recoloring (Google, Microsoft, OpenAI), show the name in type instead. Never redraw a logo. Say "Built with", never "Powered by".
- Business card: front black with large reverse logo + "Technology, made simple."; back off-white with name, title line, 3px rule, phone/email/web/region. See `print/`.

## Contact facts
- John Correia · Founder · Builder · Trainer · Consultant
- (509) 795-0112 · john@inlandcustomtech.com · inlandcustomtech.com
- Spokane · Coeur d'Alene · Inland Northwest
- Booking link currently used on the site: https://calendar.app.google/bfwvT6jSwvPMqio67
