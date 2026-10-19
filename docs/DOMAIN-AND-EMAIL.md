# Domain and email setup

Status as of 2026-10-19: **inlandcustomtech.com is not registered yet.** Nothing below has
run. The site is live at https://inland-custom-tech.pages.dev.

Everything here is free. No paid Cloudflare feature is used.

---

## Step 1. Buy the domain (you, 3 minutes)

1. Go to https://dash.cloudflare.com → **Domain Registration** → **Register Domains**.
2. Search `inlandcustomtech.com`, add it, check out. A `.com` is about $11 a year.
3. Registrar domains land in your account as a zone automatically. There is no nameserver
   step and no waiting for a transfer.

When it is done, say so and I will run step 2 and step 3.

---

## Step 2. Connect the domain to the site (me, scripted)

`scripts/connect_domain.py` does this. It attaches both hostnames to the Pages project
`inland-custom-tech`:

- `inlandcustomtech.com` (apex)
- `www.inlandcustomtech.com`

Because the zone is in the same Cloudflare account, Cloudflare creates the DNS records
itself. Certificates issue in a few minutes.

If the API path fails for any reason, here is the dashboard version:

1. dash.cloudflare.com → **Workers & Pages** → **inland-custom-tech** → **Custom domains**.
2. **Set up a custom domain** → type `inlandcustomtech.com` → **Continue** →
   **Activate domain**.
3. Repeat for `www.inlandcustomtech.com`.
4. Wait for both to read **Active**. Five minutes is normal.

### Decide: which hostname is canonical

I recommend the apex, `inlandcustomtech.com`, with `www` redirecting to it. That matches
the Open Graph tag already in the page and the address on the business card.

To make `www` redirect instead of serving a duplicate site: dash → zone
`inlandcustomtech.com` → **Rules** → **Redirect Rules** → **Create rule**.

- Name: `www to apex`
- If: `Hostname` `equals` `www.inlandcustomtech.com`
- Then: **Dynamic** redirect, 301, expression
  `concat("https://inlandcustomtech.com", http.request.uri.path)`, preserve query string on.

Free plan allows 10 redirect rules. This uses one.

---

## Step 3. Email: john@inlandcustomtech.com → your Gmail

Cloudflare Email Routing forwards incoming mail for free. It does not send. Sending is
handled by Gmail in step 4.

`scripts/connect_domain.py` also enables Email Routing, adds the MX and SPF records,
registers your Gmail as a destination, and creates the forwarding rule.

**One click is yours and cannot be scripted:** Cloudflare emails your Gmail a verification
link for the destination address. Open it and click **Verify**. Until you do, nothing
forwards.

Dashboard version if you prefer to watch it happen:

1. dash → zone `inlandcustomtech.com` → **Email** → **Email Routing** → **Get started**.
2. Custom address: `john` · Action: **Send to an email** · Destination: your Gmail address.
3. **Create and continue** → Cloudflare adds the MX and TXT records for you → **Add records
   and finish**.
4. Check Gmail for "Verify your email address" from Cloudflare. Click the link.

Add a catch-all so nothing bounces: Email Routing → **Routing rules** → **Catch-all
address** → enable → **Send to an email** → your Gmail.

---

## Step 4. Send mail as john@inlandcustomtech.com from Gmail (you, 5 minutes)

Gmail needs an SMTP server to send through. Cloudflare does not provide one. Use Gmail's
own, which is free and allowed: you authenticate as yourself and set the From address.

You need an **App Password**, which requires 2-Step Verification on your Google account.

### 4a. Make an App Password

1. https://myaccount.google.com/security → turn on **2-Step Verification** if it is off.
2. https://myaccount.google.com/apppasswords
3. App name: `Inland Custom Tech mail`. **Create**.
4. Copy the 16-character password. Google shows it once.

### 4b. Add the alias in Gmail

1. Gmail → gear icon → **See all settings** → **Accounts and Import**.
2. **Send mail as** → **Add another email address**.
3. Name: `John Correia` · Email address: `john@inlandcustomtech.com`
4. **Uncheck "Treat as an alias."** This keeps replies threading correctly and stops Gmail
   rewriting the From address.
5. **Next Step**.
6. SMTP Server: `smtp.gmail.com` · Port: `587` · Username: your full Gmail address ·
   Password: the 16-character App Password · **Secured connection using TLS**.
7. **Add Account**.
8. Gmail sends a confirmation code to `john@inlandcustomtech.com`. Cloudflare forwards it
   back to your inbox. Paste the code, or click the link in the message.

### 4c. Make it the default (optional)

**Accounts and Import** → **Send mail as** → click **make default** next to
`john@inlandcustomtech.com`. Also set "When replying to a message" to **Reply from the
same address the message was sent to**.

### 4d. Check it

Send a message from the new alias to a non-Gmail address. Confirm the From line reads
`john@inlandcustomtech.com` and that a reply lands back in your inbox.

---

## Deliverability note

Mail sent this way leaves Google's servers with Cloudflare's SPF record on the domain.
The script sets SPF to `v=spf1 include:_spf.google.com include:relay.mailchannels.net ~all`,
which authorizes Google sending and Cloudflare forwarding. If mail lands in spam, the fix
is a DKIM record, and that needs Google Workspace on the domain, which is paid. Start
without it. Forwarded-and-replied mail from a personal Gmail is normally fine at this
volume.

---

## One thing only you can change

The Google appointment schedule is still **named "Inland NW AI Scheduler"**. That name
renders inside the booking embed on the new site, so a visitor books an Inland Custom
Tech consultation on a scheduler branded with the old name.

Google Calendar (web) → **Appointment schedules** → open the schedule → rename it to
`Inland Custom Tech` → **Save**. The URL does not change, so nothing in the repo needs
editing.

---

## What this does not touch

`inlandnw.ai` keeps its Google Workspace MX records and its live site. Nothing here
changes `john@inlandnw.ai`. See [MIGRATION-PLAN.md](MIGRATION-PLAN.md).
