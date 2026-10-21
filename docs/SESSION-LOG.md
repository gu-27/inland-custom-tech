# Session log

Newest first. One entry per working session: what changed, what state it is in, and what
the next person has to decide. If you are returning cold, read the top entry, then
[EVIDENCE.md](EVIDENCE.md), then [../CLAUDE.md](../CLAUDE.md).

---

## 2026-10-21 (later): polish pass on the pathway redesign

**State: still on `pathway`, preview redeployed, not merged. Production is unchanged.**

John asked for the redesign to be finished and made "really professional and clean." No
new claims about John were added. Every change is layout, trimming, or rewording of copy
already on the page.

### What changed

- **Your path is about 900px shorter on desktop.** Each track is now one card holding a
  timeline (dot per step, thin connecting line, "Learn more" on the right) instead of five
  boxed cards with arrows. Dimmed steps get a hollow dot and a grey title. Intro line is
  now "Every step is shown here. Pick a tab to see a typical path."
- **Who we help:** one button per card ("See your path"). The three extra "Schedule"
  buttons are gone; that action is already in the header, hero, close band, and contact.
- **Hero:** shorter lede, the Local/Experienced/Personable row removed (the values strip
  sits right below it), secondary button now "See How It Works" to `#path`. Fixed a grid
  bug that cut the "Sound familiar?" rule about 100px short; the C mark was resized to
  match.
- **About:** paragraphs tightened. "Selected work" is now a five-item list with bold
  labels. The 100% / INW / Free stats and the three pillars were removed as filler.
- **Contact:** "Book a Free Discovery Call" renamed to "Book your free consultation" to
  match the rest of the site. Phone and service area fill the empty left column. The
  button under the calendar is now a secondary "Open the booking page" fallback. Email is
  still left off because inlandcustomtech.com is not registered.
- **Service pages:** real breadcrumb (Home / Your path / Step). The "Example coming soon"
  sections on Free Consultation and Implement were removed. "literally" cut on Evaluate.

### Checked

No overflow at 390 or 1440, no console errors, tabs still dim six steps on Enterprise,
every `services/` link resolves, no em dashes.

The four open questions in the entry below are unchanged and still waiting on John.

---

## 2026-10-21: evidence audit and the "Your path" redesign

**State: on a branch, deployed to preview, not merged. Production is unchanged.**

### Where things are

| | |
|---|---|
| Branch | `pathway`, pushed |
| Preview | <https://pathway.inland-custom-tech.pages.dev> |
| Production | <https://inland-custom-tech.pages.dev>, still the old page on `main` |
| Screenshots | `~/Desktop/inland-pathway-review/`, eight PNGs, desktop and mobile on each tab |

The Pages project is direct upload, not git connected. Pushing a branch deploys nothing.
The preview exists because it was deployed on purpose:

```sh
wrangler pages deploy site --project-name=inland-custom-tech --branch=pathway
```

Any branch that is not `main` lands as a preview. Only `main` is production.

### What changed

**Part 1, the evidence audit.** All 93 repos in the `gu-27` org were read, plus the local
checkouts in `~/projects` and `cv/cv.json`. The result is [EVIDENCE.md](EVIDENCE.md): one
entry per project with what it is, what John did, which pathway steps it proves, which
persona it fits, the source, and a PUBLIC-OK or ASK-JOHN flag. CLAUDE.md rule 6 now
requires checking it before any claim about John goes on the site.

**Part 2, the home page.** The services matrix and the "How it works" tabs are gone. One
`#path` section replaces both: Free Consultation, Explain, then two parallel tracks for
Technology and People & Culture. A persona toggle rewrites each card's line and fades the
steps that persona does not usually need. Nothing is hidden and Free Consultation stays
highlighted on every tab. Nine service pages were added under `site/services/`, one per
step, each ending in the same booking action.

Pricing is gone, including the nav link and the `$0` stat in About.

### Three structural changes to know about

1. **Booking URLs moved to `site/js/site.js`.** Ten pages need them now, so "one place"
   could no longer mean "inside index.html". CLAUDE.md rule 3 was updated to match.
2. **Service pages share `site/services/service.css`.** Still no build step. Inlining the
   same 6KB nine times was the worse option.
3. **The three "Who we help" buttons pointed at the deleted `#matrix`.** They now go to
   `#path` and preselect that persona's tab. Their text changed from "Learn More" to
   "See your path".

### What was checked

- No horizontal overflow at 390 or 1440, measured with `documentElement.scrollWidth`.
- Tabs work with arrow keys, Home and End, with a roving tabindex and `aria-selected`.
  The panel's `aria-labelledby` follows the selected tab.
- With JavaScript off the section renders complete on General.
- All nine service pages return 200 and all three booking buttons on each resolve to the
  calendar URL.
- No dead anchors, no console errors.
- Dimmed cards de-emphasize the border and the number, not the text color, so contrast
  still passes.

One known quirk: `.html` links 308-redirect to extensionless URLs on Cloudflare Pages.
Harmless, and it keeps the files openable straight from disk. Change the links only if
the redirect hop starts to bother you.

### Open, and waiting on John

Four answers block specific claims. The detail is in EVIDENCE.md under "TODOs for John".

1. **The startup.** `cv.json` says CEO, Moea Technologies, Inc., 2020-present, and
   nothing more. There is **no computer vision and no mobile app anywhere in the org**.
   The only spatial audio is `gu-27/ams`, which never mentions Moea. The startup line was
   deliberately left out of every "Why John" block rather than published unverified.
   **To add it:** each page in `site/services/` carries a `PENDING JOHN` comment marking
   the exact spot. Nine files, one paragraph each.
2. **Dependable HVAC.** Named as a client site. It is not in the org and not on this
   machine. Where does it live, and may it be named?
3. **May pro teams be named?** 43 engagements with 35 organizations are in `gscg-brain`,
   some NDA-flagged. All off the site until a list is approved.
4. **May the client sites be named?** `first-call-tax`, `inland-nw-tax`, `lawngest-yard`.

### To finish this

```sh
git checkout pathway
# make any changes John asks for
wrangler pages deploy site --project-name=inland-custom-tech --branch=pathway  # re-preview
# only when John says so:
git checkout main && git merge pathway && git push
wrangler pages deploy site --project-name=inland-custom-tech                   # production
```

Do not merge or deploy to production without John saying so.

### Still true from before this session

`inlandcustomtech.com` is still not registered. The Phase 2 migration in
[MIGRATION-PLAN.md](MIGRATION-PLAN.md) is still planned and still not approved. Nothing
in this session touched `gu-27/inland-nw-ai` or inlandnw.ai.
