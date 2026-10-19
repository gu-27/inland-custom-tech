# Inland Custom Tech: brand rules

Spokane technology consultancy serving the Inland Northwest. Build, Consult, Train across Automation, Analytics, and AI.
Voice: warm, plain, jargon-free. A capable neighbor, not a faceless tech firm. Lead with the customer's problem.

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
| graphite | `#262624` | Dark "punctuation" bands only (values strip, closing CTA band), featured price card |
| orange | `#D97757` | The dot, "Custom", primary buttons (black text on orange), key words in headlines, step numbers, small dots |
| paper (off-white) | `#FAF9F6` | Main background (A) |
| stone | `#ECEAE5` | Alternating section background (B) |
| muted text | `#3D3C39` | Body copy |
| soft text | `#6B6A65` | Small labels |
| hairline | `#E3E0D9` | Thin borders |

Rules:
- **Section rhythm:** alternate paper (A) and stone (B). Use graphite only for one or two "stop here" moments. No tan, no green, no tinted backgrounds.
- Orange text only at large sizes (headlines ~28px+). Small orange text fails contrast on light backgrounds.
- No gradients, no textures, no robot/brain/circuit imagery. AI lives in the services, not the visuals.

## Type
- **Manrope** (Google Fonts) for everything. Headlines 800 with tight tracking (about -0.045em); emphasized half of a headline either orange or weight 400.
- Section titles: very large (≈38–72px), each with a 3px black rule above.
- Labels: 12–13px, 800, uppercase, letter-spacing .14em, preceded by a small orange dot.

## Components (see `site/index.html` for the reference implementation)
- Buttons: primary = orange fill, black text, 12px radius; secondary = 2px black outline.
- Cards: 2px black border, 20px radius, no fill on light backgrounds.
- Business card: front black with large reverse logo + "Technology, made simple."; back off-white with name, title line, 3px rule, phone/email/web/region. See `print/`.

## Contact facts
- John Correia · Founder · Builder · Trainer · Consultant
- (509) 795-0112 · john@inlandcustomtech.com · inlandcustomtech.com
- Spokane · Coeur d'Alene · Inland Northwest
- Booking link currently used on the site: https://calendar.app.google/bfwvT6jSwvPMqio67
