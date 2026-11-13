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
- Production is live at inlandcustomtech.com (refresh shipped 2026-11-12). Production deploys only by merging to `main`. Never deploy to production without John saying so. The leftover `pathway` branch is fully merged; delete it or ignore it, don't build on it.

## Area map

| Area | What it covers | Openness | Why |
|---|---|---|---|
| UI | `site/index.html` inline CSS, `site/services/service.css`, components | **visual refresh** | The palette, type and rhythm are fixed by BRAND.md, so a pass can only improve execution: spacing, responsive behavior, contrast on small labels, consistency between the home page and the service pages. Moving the inline home-page CSS onto `tokens.css` is in scope. |
| Content | Copy on 11 pages, `docs/EVIDENCE.md` | **hands off** | Every sentence about John is evidence-gated and several are waiting on his answers. Copy changes are his. |
| Data | `site/js/site.js` (booking URLs), `docs/EVIDENCE.md` | **hands off** | Two sources of truth that CLAUDE.md protects. |
| Auth | none | n/a | Public site, no gates. |
| Deployment | Cloudflare Pages project `inlandcustomtech`, Git-connected to this repo: `main` is production, other branches get preview URLs, output `site/`, no build. www → apex by a zone Redirect Rule. No `_headers` or `_redirects` exist. | **refactor**, with a plan | Git-connected since 2026-11-12 (John's call). Remaining scope: optional `_headers`, the `.html` redirect quirk, and deleting the old direct-upload project. |

## Known debt

- `docs/EVIDENCE.md` lists four People & Culture steps; the site has five (Design added 2026-10-21).
- Four claims are waiting on John (startup line, Dependable HVAC, pro teams, client sites). Each service page carries a `PENDING JOHN` comment at the spot.
- ~~`inlandcustomtech.com` is not registered.~~ Registered 2026-11-12 in John's Cloudflare account and attached to the Pages project (apex and www). Production deploy of PR #2 went out the same night by dashboard upload.
- The home page is one file with inline CSS; the service pages share `service.css`. Two places to change a style. Since 2026-11-12 both read their values from `site/tokens.css` (a copy of `gu-27/knowledge/foundations/tokens/ict.css`), so values live in one place; the rules are still in two.
- `claude-skills/inwai-brand.md` in another repo still describes the old Inland NW AI brand and lists prices. Not this repo's file, but a model reading both could be misled.

## Audit log

| Date | Model | Scope | Outcome |
|---|---|---|---|
| 2026-11-12 | claude-opus-5-5 (subagent) | triage | 4 UI items and 1 deployment item would benefit; responsive, accessibility and fonts fine. See `gu-27/knowledge/audit/pilots/inland-custom-tech/2026-11-12-triage.md` |
| 2026-11-12 | claude-opus-5-5 | ui | On `range-spectrum`, not yet a PR: `site/tokens.css` added from foundations and linked on all 11 pages; local `:root` values removed (`--hair`→`--rule`, `--sans`→`--font-body`, `--max`→`--wide` 1100px); off-palette `#D6D3CC`, `--sand`, `--white` removed; orange text under 28px removed (nav hover, closing-band labels); dead CSS removed; service closing band and section padding matched to the home page. |
| 2026-11-12 | claude-opus-5-5 | architecture | Deploys moved to GitHub: new Pages project `inlandcustomtech` connected to `gu-27/inland-custom-tech` (main = production, branch previews); domain and www moved off the old direct-upload project `inland-custom-tech`, which stays as a frozen backup. |
