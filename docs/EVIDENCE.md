# Evidence library

Real proof of John's work, so every claim on the site can point at something specific.

Built 2026-10-21 from a read-only pass over all 93 repositories in the `gu-27` GitHub
org, plus the local checkouts in `~/projects`. Nothing here is invented. Where a fact
could not be found, it is written as a **TODO** and marked, not guessed.

## How to use this file

Before writing any claim about John's experience on the site, find it here. If it is not
here, ask John. See the standing rule in [CLAUDE.md](../CLAUDE.md).

**Pathway steps** are the ones on the site:
Explain · Assess · Plan · Build · Train · Sustain, plus the People & Culture track
(Evaluate · Plan · Implement · Sustain).

**Personas:** Small Business · Growing Company · Enterprise.

**Sensitivity:**

- **PUBLIC-OK** safe to describe on the site as written here.
- **ASK-JOHN** names a client, a pro team, a student, or Gonzaga, or touches
  confidential material. Do not publish until John approves it.

A note on the two rules that overlap. The audit rule flags anything naming Gonzaga as
ASK-JOHN. The publishing rule allows John's own Gonzaga roles in plain text, with no
logos and no Gonzaga branding. So: "MIS professor who researches how people adopt
technology" and "directs a student consulting group at Gonzaga" are fine. Describing a
specific Gonzaga project, department, course, or deliverable is ASK-JOHN.

---

## Confirmed by John in chat, 2026-10-21

John stated these directly while reviewing the redesign. They are now PUBLIC-OK in the
exact wording below, which is what the home page "Areas of expertise" grid uses. Do not
strengthen them (no "groundbreaking", no company name).

- **Interactive audio design:** a high-quality working prototype combining computer
  vision, computer engineering, audio engineering, audio design, and app development.
- **Patent development:** John holds a patent on that same audio system and has a
  second patent pending (corrected by John later the same day). Site wording: "A patent
  on that same audio system, with a second patent pending."
- **Dissertation:** the behavioral side of problematic social media use, and mitigating it
  with mindfulness. Consistent with the CV's mindfulness and "dark side of IT" talks.
- **Training:** from technology basics up to the behavioral side of adoption.

This does **not** settle TODO 1 in full. Moea is still unnamed, the role and the mobile
app claim are still unconfirmed, and the PENDING JOHN comments on the service pages are
still open.

## TODOs for John

These block specific claims the site wants to make.

1. **The startup. Name, role, and what you built.**
   The CV in `~/projects/cv/cv.json` lists **CEO, Moea Technologies, Inc., 2020-present**,
   sourced to the September 2024 CV. That is the only record anywhere in the repos. There
   is **no description of what Moea built**, and **no computer vision work of any kind**
   in any `gu-27` repo. The only spatial audio work found is `gu-27/ams` (below), which
   never mentions Moea.
   **Needed:** is Moea the company? Is "CEO" the role you want on the site? What were the
   mobile apps, and what did the computer vision do? Until you answer, the site cannot say
   "computer vision" or "mobile apps" at all.
2. **Dependable HVAC.** You named it as a client site. It does not exist in the `gu-27`
   org and there is no local folder for it. Where does it live, and may it be named?
3. **May pro teams be named?** `gscg-brain` records 43 engagements with 35 organizations,
   including MLB, NBA, NFL, NHL, MLS, WNBA and NWSL clubs. All of it is ASK-JOHN until you
   say otherwise, and some of it is NDA-flagged in the records themselves.
4. **May the small-business sites be named?** `first-call-tax`, `inland-nw-tax`,
   `lawngest-yard` look like real client work. Confirm they are clients, and whether each
   one consents to being named or shown.

---

## 1. Deep technical work

### AMS, a spatial audio platform

- **What it is:** a cloud platform for spatial (Ambisonic) audio at live venues. Edge
  devices capture audio, stream it to the cloud, and teams discover, clip, and share
  binaural moments through a web app and an embeddable, token-gated player.
- **What John did:** wrote the founding architecture plan and built it. Python edge agent
  (PortAudio, GStreamer for AES67), FastAPI and SQLAlchemy backend, PostgreSQL,
  ffmpeg and numpy for audio processing, binaural rendering in the browser. The
  source-agnostic ingest design (everything becomes segments) is his call, recorded with
  the trade-off.
- **Proves:** Plan, Build.
- **Persona:** Enterprise.
- **Source:** `gu-27/ams` (private). `PLAN.md` is the approved contract.
- **Sensitivity:** **PUBLIC-OK** for the technical description. No client is named in the
  repo. Do not claim it is deployed at a venue: the repo does not say that.

### Moea Technologies

- **Status:** TODO 1 above. Do not write anything about it yet.
- **Source:** `~/projects/cv/cv.json`, professional experience, sourced to the Sept 2024 CV.
- **Sensitivity:** **ASK-JOHN.**

---

## 2. Analytics platforms and dashboards

### MLB theme night attendance analysis

- **What it is:** a dashboard measuring the attendance lift from theme nights across all
  30 MLB teams, 2024 to 2025.
- **What John did:** built the whole pipeline. Two scrapers (per-game attendance from the
  ESPN API, promotions from the MLB Stats API), a SQLite database, an export step to JSON,
  and a single-file dashboard with no build step.
- **Proves:** Assess, Build.
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/mlb_themenights` (private).
- **Sensitivity:** **ASK-JOHN.** The README names the pro team the engagement was for.
  The method (scrape two public APIs, join them, measure lift) is describable without the
  client.

### NCAA sports analytics program dashboard

- **What it is:** an interactive dashboard of 35 NCAA sports analytics and sports science
  degree programs. Overview charts, a bubble map, a sortable directory, curriculum
  comparison, and a per-school explorer.
- **What John did:** collected and filtered the data, then built the dashboard as one
  self-contained HTML file with embedded JSON and Plotly from a CDN.
- **Proves:** Assess, Build.
- **Persona:** Small Business, Growing Company.
- **Source:** `gu-27/sports_analytics_dashboard` (public), live at
  `gu-27.github.io/sports_analytics_dashboard`.
- **Sensitivity:** **PUBLIC-OK.** Public data, no client.

### Venue experience map

- **What it is:** a React app mapping every zone, experience, and attraction inside a
  major-league ballpark, with field research notes attached to each zone.
- **What John did:** built it for a student consulting team to use in the field and to
  present from.
- **Proves:** Build.
- **Persona:** Enterprise.
- **Source:** `gu-27/Mariners_Map` (private).
- **Sensitivity:** **ASK-JOHN.** Names a pro team and involves students.

### Strategy and roster planning boards

- **What it is:** two internal tools. An organizational strategy dashboard, and a
  drag-and-drop roster planning board arranged by role and class year.
- **What John did:** built both, then later folded them into a single platform so there
  was one place to maintain instead of three.
- **Proves:** Build, Sustain.
- **Persona:** Growing Company.
- **Source:** `gu-27/gscg_priorities_dashboard`, `gu-27/gscg_roster` (both private).
- **Sensitivity:** **ASK-JOHN.** Student and organizational data.

---

## 3. Automation and AI applications

### Follow-up automation with human approval

- **What it is:** a lead intake form that drafts a follow-up with AI, holds it for a human
  to review, and only then sends it.
- **What John did:** built the whole loop on Cloudflare Pages Functions, R2 and KV, with
  no framework and no build step. The invariants are written into the repo: secrets are
  never served to the browser, the public endpoint has a daily spend cap, the review
  portal sits behind access control, and **nothing sends automatically**.
- **Proves:** Build, Sustain.
- **Persona:** Small Business, Growing Company.
- **Source:** `gu-27/inwai-followup` (private). John's own business.
- **Sensitivity:** **PUBLIC-OK.** This is the clearest "AI that does not act on its own"
  example on the list.

### AI courseware platform

- **What it is:** an AI companion for digital textbooks. A tutor chatbot grounded in the
  actual chapter text, AI grading that an instructor must approve before a student sees
  anything, and an engagement dashboard.
- **What John did:** built it. FastAPI and React, and it is built local-first: the whole
  thing runs on one laptop with **no cloud accounts and no AI keys**, because a built-in
  mock answers from the chapter text. Real models and cloud hosting are a configuration
  switch, not a rewrite.
- **Proves:** Plan, Build, Train.
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/ai-textbook-platform` (private).
- **Sensitivity:** **ASK-JOHN** to name the university or the course. The platform itself
  and the two design decisions (human approves before anything ships, boots with no keys)
  are describable without either.

### Research operating system

- **What it is:** a two-repo system for AI-assisted, human-directed academic research:
  literature review, journal strategy, drafting.
- **What John did:** designed and built it. Every citation is verified or flagged, a human
  approves everything that ships, and every model is a swappable client. Includes a
  working bridge to a reference manager and an evidence store.
- **Proves:** Plan, Build.
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/research-brain` (private).
- **Sensitivity:** **ASK-JOHN.** Private, and it involves a co-author.

### Meeting Brain

- **What it is:** a meeting-notes tool page under the Inland NW AI projects site.
- **What John did:** built the page and the data shape.
- **Sensitivity:** **PUBLIC-OK**, but **do not use it as an example.** `meetings.json` is
  empty. It is a shell, not a shipped tool. Noted here so nobody mistakes it for proof.
- **Source:** `gu-27/inwai-projects` (public).

---

## 4. Privacy-first builds

This group is the evidence behind the site's "your data stays private" note. It is not a
slogan here. In each case the privacy is a property of how the thing is built, not a
promise in a policy.

### Anonymizer

- **What it is:** a tool that strips identifying information out of documents before they
  go to an AI, and puts it back afterward.
- **What John did:** built it as one HTML file with no build step, no dependencies, and
  **zero network requests**. Files never leave the machine. It works opened straight from
  disk.
- **Proves:** Build, Train.
- **Persona:** Small Business, Growing Company, Enterprise.
- **Source:** `gu-27/anonymizer` (public), live at `gu-27.github.io/anonymizer`.
- **Sensitivity:** **PUBLIC-OK.** The strongest publishable privacy example.

### Sensitive-document review assistant

- **What it is:** a locally hosted tool for reviewing confidential personnel packets with
  AI help.
- **What John did:** built it so the sensitive documents never leave the machine in
  identifiable form. An anonymization engine strips personal information before any cloud
  call, and de-anonymization happens locally.
- **Proves:** Build.
- **Persona:** Enterprise.
- **Source:** `gu-27/packet_review` (private).
- **Sensitivity:** **ASK-JOHN.** Describing the pattern is fine. Naming the institution,
  the committee, or the document type is not.

### Single-file tool under a hard constraint

- **What it is:** a browser tool that answers a complicated eligibility question and fills
  out a form, built for an office that required that ID numbers never leave the user's
  machine.
- **What John did:** met the requirement structurally rather than with a policy. One HTML
  file with everything inlined: no backend, no CDN, no fonts, no analytics, nothing to
  request. It runs with the network cable unplugged. Tested with Node's built-in runner
  and a real-Chrome smoke test.
- **Proves:** Assess, Plan, Build.
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/catalog-petition` (private).
- **Sensitivity:** **ASK-JOHN.** Names a university office and concerns student records.

---

## 5. Websites and apps for small businesses and families

### Rental property listing system

- **What it is:** a set of property listing pages plus one portfolio page that shows every
  home at once.
- **What John did:** built a small system instead of four separate pages. Facts live in
  one `photos.json` per property, a Python script retouches the photos and renders the
  page, and the portfolio page pulls its card photos from the property repos directly, so
  the two can never disagree. Per-room rent is computed, so it cannot contradict the
  headline. Push to deploy.
- **Proves:** Build, Sustain.
- **Persona:** Small Business.
- **Source:** `gu-27/402-mission`, `gu-27/1945-astor`, `gu-27/1608-astor`,
  `gu-27/rentals`. John's own rental business (JC Investment Properties, LLC, owner since
  2005, per the CV).
- **Sensitivity:** **PUBLIC-OK.** His own business, and the pages are already public.

### Small-business websites

- **What it is:** marketing sites for a tax and legal practice and a lawn care business.
- **What John did:** built them.
- **Proves:** Build.
- **Persona:** Small Business.
- **Source:** `gu-27/first-call-tax`, `gu-27/inland-nw-tax`, `gu-27/lawngest-yard`
  (all public), `gu-27/jc-investments-rentals`.
- **Sensitivity:** **ASK-JOHN.** See TODO 4. Confirm these are clients and whether they
  can be named.

### Event page with signup and organizer view

- **What it is:** a public event page with a family signup form and a private organizer
  view, for a high school team's trip to a college game.
- **What John did:** built it on Cloudflare Pages Functions and D1, static with no build
  step. It ran a real event: 13 families, 27 people.
- **Proves:** Build.
- **Persona:** Small Business.
- **Source:** `gu-27/mead-gu-fall-2026` (private).
- **Sensitivity:** **ASK-JOHN.** Names a school, a university, and involves families.

### Accessibility build

- **What it is:** a Morse code learning site for a family member who operates her computer
  with a single head switch.
- **What John did:** built the trainer, the guides, and the hub. Any key or any press acts
  as the switch, the calibration is treated as untouchable, and the trainer works offline
  as a single file.
- **Proves:** Explain, Build, Train.
- **Persona:** Small Business.
- **Source:** `gu-27/christy-morsecode` (private), live publicly.
- **Sensitivity:** **ASK-JOHN.** Names a family member and her disability. Ask before any
  use, including an anonymous version.

### Community resource site

- **What it is:** free tools for people affected by the August 2026 Spokane fires. No
  accounts, no lead capture, no analytics.
- **What John did:** built it, then deliberately held it back from launch until every
  external fact in it is verified. It sits on a review URL, marked noindex, on purpose.
- **Proves:** Build.
- **Persona:** Small Business.
- **Source:** `gu-27/spokanefire` (private).
- **Sensitivity:** **PUBLIC-OK** to describe the approach. **Do not link it or call it
  live**: it is not launched, and that is a deliberate gate.

### Mapping tool over public data

- **What it is:** a map of every WDFW private-lands hunting property in Washington, with
  boundaries, parking, access points and safety zones.
- **What John did:** built the scraper, the refresh workflow, and the map. The password
  gate fails closed: until the secret is set the site returns 503, so it is never served
  unprotected.
- **Proves:** Build.
- **Persona:** Small Business.
- **Source:** `gu-27/wa-hunt-map` (private).
- **Sensitivity:** **PUBLIC-OK.** Public agency data, personal project.

---

## 6. Products built as products

### White-label memorial site platform

- **What it is:** a memorial site product. One codebase, deployed once, that reads a
  per-memorial config at runtime. Each memorial gets its own instance: its own data repo,
  its own Cloudflare Worker, its own storage bucket.
- **What John did:** designed the tenancy model and built it. Families submit memories and
  photos, the family curates them, and the site exports keepsakes as PDF, slideshow and QR.
  Personal information is treated as a first-class concern in the architecture, and there
  is a demo mode that runs with no backend at all.
- **Proves:** Plan, Build, Sustain.
- **Persona:** Growing Company.
- **Source:** `gu-27/zapapps-memorial`, `gu-27/keepsake-sites`, `gu-27/zapapps-console`
  (all private).
- **Sensitivity:** **ASK-JOHN.** Live instances carry real honoree and family names. The
  platform architecture is describable without naming any instance.

### Multi-tenant operations console

- **What it is:** a registry and monitoring console sitting above every deployed instance.
  The owner sees everything, each customer sees only their own, and each instance reports
  live health.
- **What John did:** built it, and wrote down honestly that the current gate is a soft
  client-side one with real security enforced server-side per instance.
- **Proves:** Build, Sustain.
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/zapapps-console` (private).
- **Sensitivity:** **PUBLIC-OK** for the architecture. Customer names are ASK-JOHN.

---

## 7. Training, adoption, and culture

This is the People & Culture evidence. It is the thinnest group in publishable form,
because nearly all of it is Gonzaga work.

### Decision exercises for non-technical audiences

- **What it is:** two interactive in-class exercises. In one, participants act as a CEO
  who has just acquired two million customer records without consent and must choose and
  defend a course of action. In the other, a leadership team (CEO, CIO, Legal, PR,
  Operations) works a live ransomware attack through five phases to a pay-or-refuse
  decision with two outcome paths.
- **What John did:** designed and built both, for an audience assumed to have no technical
  background.
- **Proves:** Explain, Train, and the culture track (Evaluate, Implement).
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/privacy-exercise`, `gu-27/ransomware_exercise` (private).
- **Sensitivity:** **ASK-JOHN** for the course context. The exercise format itself is
  generic and is the best Train evidence available for Enterprise.

### Teaching a pipeline end to end

- **What it is:** a teaching site that walks one running business question all the way
  from a database to a published dashboard: Extract, Load, Shape, Visualize, Combine,
  Publish, Critique.
- **What John did:** built it, and computed every number on it from the underlying data
  rather than writing figures by hand.
- **Proves:** Explain, Train.
- **Persona:** Growing Company.
- **Source:** `gu-27/gorge-viz` (private).
- **Sensitivity:** **ASK-JOHN.** Course and university context.

### Reusable AI working standards

- **What it is:** a structured library of skill definitions and lessons learned that keep
  AI sessions consistent across projects.
- **What John did:** wrote and maintains it, refined through real work.
- **Proves:** Train, Sustain.
- **Persona:** Growing Company, Enterprise.
- **Source:** `gu-27/agent-skills-library` (private), `gu-27/claude-skills` (public).
- **Sensitivity:** **PUBLIC-OK** as a description. Individual skill files reference
  clients and are not for publication.

### Adoption research

- **What it is:** peer-reviewed research on how people actually adopt and use technology.
  Published in MIS Quarterly, ACM Transactions on Management Information Systems, Journal
  of Information Systems, and others. Topics include measuring technology constructs that
  have gone stale, computer self-efficacy, security behavior, and privacy decisions in
  fitness technology.
- **Proves:** Explain, Assess, and the culture track.
- **Persona:** all three.
- **Source:** `~/projects/cv/cv.json`, seven peer-reviewed papers, 2018 to 2023.
- **Sensitivity:** **PUBLIC-OK.** Published work, already public. This is what backs
  "researches how people adopt technology" in the Why John block.

---

## 8. Directing a student consulting group

- **What it is:** a student-run sports business consultancy at Gonzaga that runs like a
  small company: roles with playbooks, a project lifecycle, recruiting, client
  engagements, and a knowledge base built so that what the group learns outlives the
  students who cycle through.
- **What John did:** he is the faculty director (2023 to present, per the CV). He built
  the institutional knowledge system behind it: structured records for people, clients and
  projects; a sensitivity tier model that decides what may be stored at all; generated
  artifacts with drift guards so nothing is hand-edited into disagreement; and the public
  and internal sites that read from it.
- **Scale, from the records:** 43 engagements across 11 semesters (2022 to 2026) with 35
  organizations, across MLB, NBA, NFL, NHL, MLS, WNBA and NWSL, plus arenas, agencies and
  brands. Some records carry an NDA flag.
- **Proves:** Explain, Assess, Plan, Build, Train, Sustain, and the whole culture track.
  This is the only item in the library that proves every step.
- **Persona:** Enterprise.
- **Source:** `gu-27/gscg-brain`, `gu-27/gscg`, plus about fifteen related repos
  (dashboards, rosters, thank-you sites, photo galleries).
- **Sensitivity:** **ASK-JOHN**, all of it. Students, clients, pro teams, Gonzaga, and
  NDA-flagged records. John's role title in plain text is fine. **No client or team may be
  named until John approves a list.**

---

## 9. Institutional work for a university

Grouped because the flag is the same for every item.

- A 49-site branding and access audit, delivered as a working page and a matching PDF,
  both rendered from one source of truth (`gu-27/gu-web-review`).
- A curriculum redesign communicated as a public site (`gu-27/MIS`), and the redesign
  itself, led 2025 to 2026 and launching Fall 2026 (per the CV).
- A standards framework for how student organizations operate, with tiers of engagement
  (`gu-27/SBA-Student-ExternalClubs`, now served from `gu-sba`).
- A proposal site making the case for AI licenses across a school, with governance,
  success measures and open questions (`gu-27/sba-claude-2026-proposal`).
- A strategic initiative presented to senior leadership in two parallel versions, detailed
  and presentation (`gu-27/GU_Sports`).
- A reusable Astro theme with a brand token system for department sites
  (`gu-27/GU_Branded_Web_Template`).
- A partnership design with an outside institute (`gu-27/emi-sba`).
- A research and practice record on mindfulness-based experiential learning
  (`gu-27/mbel`).

- **Proves:** collectively Explain, Assess, Plan, Build, and the culture track.
- **Persona:** Enterprise.
- **Sensitivity:** **ASK-JOHN**, every item. Gonzaga is named throughout, and the brand
  audit lists protected URLs.

---

## 10. Breadth, as a fact rather than a claim

John keeps an index of every site he has deployed. It currently lists **74 deployed
sites** across Cloudflare Pages, GitHub Pages and Netlify, grouped by category and
colour-coded by access level.

- **Source:** `gu-27/correia27`, `stuff/sites.json` (read 2026-10-21, 74 entries).
- **Sensitivity:** **PUBLIC-OK** to say "74 sites deployed" with the date. The index
  itself is gated and the list names clients, so **do not link it and do not reproduce
  it**.

---

## What the evidence does not support

Say none of these on the site until the gap is closed.

- **Computer vision.** No evidence in any repo. TODO 1.
- **Mobile apps.** No mobile app repo exists. Everything found is web or Python. TODO 1.
- **Client results, numbers, or outcomes.** No repo records a measured client outcome.
  The only hard numbers found are internal counts (43 engagements, 74 sites, 13 families
  at one event), and the two usable ones are cited above.
- **Testimonials or named references.** None exist.
- **Certifications or vendor credentials.** None in the CV beyond the degrees and the
  two early telecommunications certificates.
- **Team size.** Everything found was built by John.
