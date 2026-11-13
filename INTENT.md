# Inland Custom Tech: intent

> Draft, written 2026-11-12 from CLAUDE.md, BRAND.md, docs/EVIDENCE.md and docs/SESSION-LOG.md. John has not approved it yet. The audit playbook in `gu-27/knowledge/audit/PLAYBOOK.md` says how this file is used.

## Purpose

The public storefront for John's consultancy. A visitor should understand in one screen what the firm does, see that it's a real person they can trust, and book a free hour. Everything on the site serves that one booking.

## Audience

| Who | What they need from it |
|---|---|
| Small business owner in the Inland Northwest | A plain answer to "could this help me?" and a way to ask without a sales pitch |
| Growing company | Where to start, and proof John has built real things |
| Enterprise contact | A credible path with named steps, and assurance about privacy |

## Draws on

```yaml
draws_on:
  - two-halves-of-the-problem
  - privacy-as-structure
  - human-approves
  - curious-problem-solver
```

## Must not change

- The seven hard rules in `CLAUDE.md`. In particular: no prices anywhere, no new fonts or colors, no robot or brain imagery, no claim about John without a line in `docs/EVIDENCE.md`, nothing flagged ASK-JOHN published, no client or team named.
- The logo. Outlined vector, copied from the SVG, never retyped.
- Booking URLs live only in the `SITE` object in `site/js/site.js`, mirrored in markup. Change both or neither.
- `gu-27/inland-nw-ai` and inlandnw.ai are untouched from this repo. The rename migration is a separate approved plan.
- The "Your path" structure: free consultation first, then the Technology track (assess, plan, build, train, sustain) and the People & Culture track (evaluate, plan, design, implement, sustain). Whether "Explain" stays is John's open question, not an audit's.
- The section rhythm: paper pages on a stone desk, graphite used exactly twice on the home page.
- Production is live at inland-custom-tech.pages.dev (shipped 2026-10-22). Never deploy to production without John saying so. The leftover `pathway` branch is fully merged; delete it or ignore it, don't build on it.

## Area map

| Area | What it covers | Openness | Why |
|---|---|---|---|
| UI | `site/index.html` inline CSS, `site/services/service.css`, components | **visual refresh** | The palette, type and rhythm are fixed by BRAND.md, so a pass can only improve execution: spacing, responsive behavior, contrast on small labels, consistency between the home page and the service pages. Moving the inline home-page CSS onto `tokens.css` is in scope. |
| Content | Copy on 11 pages, `docs/EVIDENCE.md` | **hands off** | Every sentence about John is evidence-gated and several are waiting on his answers. Copy changes are his. |
| Data | `site/js/site.js` (booking URLs), `docs/EVIDENCE.md` | **hands off** | Two sources of truth that CLAUDE.md protects. |
| Auth | none | n/a | Public site, no gates. |
| Deployment | Cloudflare Pages direct upload from `site/` via `wrangler pages deploy`. No `_headers` or `_redirects` exist. | **refactor**, with a plan | Direct upload means a commit doesn't deploy, and the SESSION-LOG records a quirk with `.html` redirects. A pass could wire git-connected deploys, but only with a written plan and John's go, since the production URL is live. |

## Known debt

- `docs/EVIDENCE.md` lists four People & Culture steps; the site has five (Design added 2026-10-21).
- Four claims are waiting on John (startup line, Dependable HVAC, pro teams, client sites). Each service page carries a `PENDING JOHN` comment at the spot.
- `inlandcustomtech.com` is not registered. Contact facts in BRAND.md name it anyway.
- The home page is one file with inline CSS; the service pages share `service.css`. Two places to change a style.
- `claude-skills/inwai-brand.md` in another repo still describes the old Inland NW AI brand and lists prices. Not this repo's file, but a model reading both could be misled.

## Audit log

| Date | Model | Scope | Outcome |
|---|---|---|---|
| 2026-11-12 | claude-opus-5-5 (subagent) | triage | 4 UI items and 1 deployment item would benefit; responsive, accessibility and fonts fine. See `gu-27/knowledge/audit/pilots/inland-custom-tech/2026-11-12-triage.md` |
