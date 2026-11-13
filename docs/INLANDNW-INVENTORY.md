# inlandnw.ai inventory and triage

Written 2026-11-12 from the repos (read-only) and the 2026-10-19 live audit in
[MIGRATION-PLAN.md](MIGRATION-PLAN.md). Nothing here has run. The calls are proposals for
John to confirm.

The headline: inlandnw.ai itself is one landing page. The "tools" live in other repos and
hosts. Only two of them carry real logic worth moving: the follow-up system and the
anonymizer. Everything else is either already replaced by the new site, a one-off
keepsake, or a demo with no data behind it.

| # | What | Where it lives | Call | Why |
|---|---|---|---|---|
| 1 | Landing page | `gu-27/inland-nw-ai` → inlandnw.ai | **Retire + 301** | Replaced by the new site. Keep the zone for email and links. |
| 2 | Mead × GU volleyball page | `gu-27/mead-gu-fall-2026`, Worker route on inlandnw.ai | **Keep until 2027-01-01, then retire** | Event is past. 13 families hold the link. Rotate its admin password now. |
| 3 | Follow-up system: intake form, approval portal, API | `gu-27/inwai-followup` → inwai-followup.pages.dev | **Keep. Rebrand and move.** | The one real product: Claude drafts, a person approves, then it sends. This becomes the AI layer on top of a free CRM. Move the URL first, change the From address only after Resend verifies the new domain. |
| 4 | Anonymizer | `gu-27/anonymizer` → gu-27.github.io/anonymizer | **Keep as is** | Already shown on the new site. Runs entirely in the browser. Nothing to migrate; add the new brand when convenient. |
| 5 | "Custom AI Tools & Projects" index | `gu-27/inwai-projects` → GitHub Pages | **Retire** | Old brand, "from $149" flat prices (the new site carries no prices), and a product list the Kits now replace. Replace with a one-line redirect page to inlandcustomtech.com. |
| 6 | Meeting Brain | `gu-27/inwai-projects/meeting-brain` | **Retire** | Its data file is empty, so there is nothing to carry over. Its ideas (voice logging, card scan, urgency) are already in the follow-up system's merge design. |
| 7 | Memory Collector demos | `memories-figueira-hamrick`, `keepsake-sites`, `aunt-julie-70`, `zapapps-memorial`, `friend-mothers-memorial` | **Keep private, do not sell** | Personal keepsakes for real people. Not a business product under the new positioning. Leave them where they are. |
| 8 | Group Calendar Planner | `family-calendar` (family-summer-2026-calendar) | **Keep private** | Same: a family tool used as a demo. Fine as a private example, not a listed product. |
| 9 | Thank You Card Studio, Custom Trivia | listed "coming soon" on the index; no repo found for either | **Drop** | Never built. Nothing to move. (The GSCG thank-you sites are a separate, Gonzaga-side pattern.) |
| 10 | `john@inlandnw.ai` | Google Workspace on the inlandnw.ai zone | **Keep for now** | Paid, working, and the follow-up system sends from it. Migrate after the new domain exists and Resend is verified (its own small project). |
| 11 | Old brand skill `inwai-brand.md` | `gu-27/claude-skills` | **Retire** | Describes the rust/teal/Inter brand. The new `inland-custom-tech-brand` skill replaces it. Delete the file or mark it superseded at the top. |
| 12 | `www.inlandnw.ai` (522) and dead Worker `inland-nw-ai` | Cloudflare | **Fix / delete** | Live defects, independent of the rename. Stage 0 in the migration plan. |
| 13 | `inland-nw-tax`, `first-call-tax` | public repos, "Inland NW Tax & Legal" | **Not Inland NW AI. Leave alone.** | A separate tax-and-legal brand (JD + MAccT). Not John's consultancy, so not part of this migration. |

## What this means for the plan

- **Two things move:** the follow-up system (rebranded, URL first, sender second) and the
  anonymizer (cosmetic only).
- **One thing retires with a redirect:** the landing page.
- **One thing waits:** the Mead page until January.
- **Everything else stays private or is deleted.** No data migration is needed anywhere:
  Meeting Brain is empty, the keepsakes stay put, the "coming soon" items never existed.

## Decisions for John

1. Confirm retiring the Tools & Projects index and Meeting Brain (defaults in the October
   plan were "your call").
2. Confirm the keepsake and family tools stay private and off the new site.
3. Say when to run Stage 0 (the 522 fix, the Mead password, the dead Worker). It needs no
   domain and can go today.

Once the domain is bought, the order is: Stage 0 → connect domain and email → move the
follow-up system's URL → verify Resend → switch its From address → 301 the old site.
