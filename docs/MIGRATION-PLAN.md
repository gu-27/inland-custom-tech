# Migration plan: inlandnw.ai to inlandcustomtech.com

Plan only. Nothing here has run. Approve the checklist at the bottom and I will execute it.

Written 2026-10-19 from a live audit of the Cloudflare account, the DNS, and the three
repos.

---

## Where we left off

Last worked 2026-10-19. Phase 1 is done and the new site is live at
https://inland-custom-tech.pages.dev. Nothing in this plan has run, and nothing on
inlandnw.ai has been touched.

The whole thing is blocked on one purchase.

**Next, in order:**

1. **Buy inlandcustomtech.com** at dash.cloudflare.com → Domain Registration.
   Everything else waits on this. See [DOMAIN-AND-EMAIL.md](DOMAIN-AND-EMAIL.md) step 1.
2. **Run `python3 scripts/connect_domain.py`** to attach apex + www and turn on Email
   Routing, then click the Cloudflare verification link and set up Gmail "Send mail as".
3. **Do Stage 0 below.** It fixes things that are broken right now and does not depend on
   the rename, so it can happen the moment you approve it: the `www.inlandnw.ai` 522, the
   unrotated Mead `ADMIN_PASSWORD`, and the dead `inland-nw-ai` Worker.
4. **Then approve Stage 1** and the 301s go in.

Stages 1 through 4 all need your sign-off first. Stage 0 is the only part that is safe to
start before the domain exists.

Two decisions are still open and only you can make them: whether the "Custom AI Tools &
Projects" index and Meeting Brain (items 6 and 7) move, retire, or stay put.

---

## What is actually served today

I probed the live hosts rather than trusting the repos. One thing worth knowing up front:
the `inland-nw-ai` Pages project serves `index.html` for **every** unknown path, so
`inlandnw.ai/anything` returns 200 with the homepage. There are no hidden subpages. The
only real subpath is the Mead one, and that works because a Worker route intercepts it
before Pages sees it.

| # | Item | Served at | Backed by |
|---|---|---|---|
| 1 | Inland NW AI landing page | `inlandnw.ai` | Pages `inland-nw-ai` ← `gu-27/inland-nw-ai` (`docs/`) |
| 2 | Mead x GU Volleyball page | `inlandnw.ai/mead-gu-fall-2026` | Worker `mead-gu-fall-2026-proxy` → Pages `mead-gu-fall-2026` |
| 3 | Follow-up intake form | `inwai-followup.pages.dev/` | `gu-27/inwai-followup` (`public/`) |
| 4 | Follow-up approval portal | `inwai-followup.pages.dev/portal/` | same repo, behind Cloudflare Access |
| 5 | Follow-up API (7 Functions) | `inwai-followup.pages.dev/api/*` | same repo (`functions/api/`), R2 + KV + Claude + Resend |
| 6 | "Custom AI Tools & Projects" index | `gu-27.github.io/inwai-projects/` | `gu-27/inwai-projects` (GitHub Pages) |
| 7 | Meeting Brain | `gu-27.github.io/inwai-projects/meeting-brain/` | same repo |
| 8 | Email `john@inlandnw.ai` | Google Workspace MX on the zone | Google Workspace (paid) |
| 9 | `www.inlandnw.ai` | **broken, returns 522** | proxied DNS with no working origin |
| 10 | Worker `inland-nw-ai` | nothing | no routes, no custom domain, empty body |

Things that do **not** exist, so they need no plan: no forms, no surveys, no Google Forms
or Typeform embeds, no analytics tag, no third-party integrations. The old landing page
links out to exactly two external places: the booking link and the calendar embed, both of
which the new site already carries.

### Two live defects, independent of the rename

- **`www.inlandnw.ai` returns 522.** It has been proxied at Cloudflare with nothing
  behind it. The old landing page's own contact section links to
  `https://www.inlandnw.ai`, so there is a dead link on the live site right now.
- **The Mead page's `ADMIN_PASSWORD` was never rotated** after the October 15 event.

Neither blocks the rename. Both are quick and I would fix them in step 0.

---

## Recommendation per item

| # | Item | Call | Why |
|---|---|---|---|
| 1 | Landing page | **Retire + 301** to `inlandcustomtech.com/` | The new site replaces it outright. Keep the zone so links and email keep working. |
| 2 | Mead page | **Keep on inlandnw.ai** until 2027-01-01, then retire | The event is past. The URL went to 13 families. Moving it breaks their link and buys nothing. |
| 3 | Intake form | **Move** to `inlandcustomtech.com/connect` | It is the lead path and should wear the new brand. |
| 4 | Approval portal | **Move** with it, keep Access-gated | Internal. Moves for free alongside the form. |
| 5 | Follow-up API | **Move** with it | Same Pages project. One cutover, not three. |
| 6 | Tools & Projects index | **Your call.** Default: retire | Old brand, old framing, on GitHub Pages. I cannot tell from the repo whether you still send anyone there. |
| 7 | Meeting Brain | **Your call.** Default: keep where it is | A working tool. Nothing forces it to move. Moving it is cosmetic. |
| 8 | `john@inlandnw.ai` | **Keep** for now | Paid Workspace, and the follow-up system sends from this address via Resend. Changing it is its own project. |
| 9 | `www.inlandnw.ai` | **Fix in step 0**, then fold into the 301 | Broken today. |
| 10 | Worker `inland-nw-ai` | **Delete** after confirming it is dead | No routes, no domains, empty. Almost certainly a leftover. |

### The one real dependency

Item 5 sends mail **from `john@inlandnw.ai`** through Resend. If you move the follow-up
system to the new domain and change the From address, Resend needs
`inlandcustomtech.com` verified with its own DKIM records first. That is free on Resend's
free tier but it is a real step, and getting it wrong sends your follow-ups to spam.

So: move the follow-up system's **URL** in stage 2, and change its **From address** in a
separate stage 3, only once Resend shows the new domain verified. Do not do both at once.

---

## Redirect map

The old site has no real subpaths, so a deep path-for-path map would be fiction. One
blanket redirect plus two carve-outs is the honest answer.

**Cloudflare Redirect Rule** on the `inlandnw.ai` zone. Free plan allows 10; this uses 1.

- Name: `inlandnw.ai to inlandcustomtech.com`
- Expression:

```
(http.host in {"inlandnw.ai" "www.inlandnw.ai"})
and not starts_with(http.request.uri.path, "/mead-gu-fall-2026")
and not starts_with(http.request.uri.path, "/.well-known/")
```

- Then: Static redirect, **301**, to `https://inlandcustomtech.com/`,
  preserve query string **off**.

Why each carve-out matters:

- **`/mead-gu-fall-2026`.** Single Redirects run in `http_request_dynamic_redirect`,
  which is the **first** request-side phase in Cloudflare's ruleset engine. It fires
  ahead of Access checks, Snippets, Cloud Connector, and the Worker route that serves the
  Mead page. Without this clause the blanket redirect wins and the Mead page dies, even
  though its Worker route is still configured and looks healthy in the dashboard. This is
  the single easiest way to break something during this migration.
  Source: https://developers.cloudflare.com/ruleset-engine/reference/phases-list/
- **`/.well-known/`.** Domain-verification and certificate-validation paths. Redirecting
  them can break Google Workspace verification and ACME renewals on a zone you are keeping.

Everything redirects to the root, not to a matching path, because no matching paths exist.
A 301 to a real page beats a 301 to a 404.

When the Mead page retires in January, drop its clause and the rule covers everything.

### What the 301 does not cover

- `inwai-followup.pages.dev/*` keeps working. Cloudflare does not let you 301 a
  `pages.dev` hostname. When item 3 moves, the old URL stays reachable rather than
  redirecting. Update any link you control; there is no server-side fix.
- `gu-27.github.io/inwai-projects/*` is GitHub Pages. If item 6 retires, the only clean
  option is a meta-refresh page or deleting the Pages site.

---

## Checklist to approve

Tick what you want. I will not start any of it until you do.

**Stage 0: fix what is broken now (no dependency on the rename)**
- [ ] Point `www.inlandnw.ai` at the `inland-nw-ai` Pages project so the 522 stops
- [ ] Rotate the Mead page `ADMIN_PASSWORD`
- [ ] Confirm Worker `inland-nw-ai` is dead, then delete it

**Stage 1: cut the brand over (after inlandcustomtech.com is live and verified)**
- [ ] Add the Redirect Rule above on the `inlandnw.ai` zone
- [ ] Verify by hand: `inlandnw.ai/` → 301 → new site; `inlandnw.ai/mead-gu-fall-2026` →
      still 200 and still the Mead page; `inlandnw.ai/.well-known/x` → not redirected
- [ ] Leave Pages project `inland-nw-ai` deployed but unreferenced for 30 days as a rollback
- [ ] Archive `gu-27/inland-nw-ai` on GitHub (read-only, not deleted)

**Stage 2: move the follow-up system (URL only)**
- [ ] Attach `inlandcustomtech.com` to the `inwai-followup` Pages project, or move its
      files into this repo under `site/connect/`. I would pick the second: one project,
      one deploy, one brand.
- [ ] Re-skin the intake form to the Inland Custom Tech brand
- [ ] Re-point the Cloudflare Access policy at the new portal hostname
- [ ] Leave the From address on `john@inlandnw.ai`

**Stage 3: move the sending identity (only after stage 2 is stable)**
- [ ] Verify `inlandcustomtech.com` in Resend, add its DKIM records
- [ ] Wait for Resend to show verified
- [ ] Flip `MAIL_FROM` to `john@inlandcustomtech.com`
- [ ] Send one real test and check it lands in an inbox, not spam

**Stage 4: the leftovers (your call, no deadline)**
- [ ] Decide item 6, "Custom AI Tools & Projects": retire or move
- [ ] Decide item 7, Meeting Brain: leave or move
- [ ] 2027-01-01: retire the Mead page, drop its clause from the redirect rule
- [ ] Decide whether Google Workspace moves to the new domain, or
      `john@inlandnw.ai` just keeps forwarding forever

**Never**
- [ ] Do not delete the `inlandnw.ai` zone. The 301s and the Workspace MX records live on
      it. Deleting it breaks every old link and your email at once.
