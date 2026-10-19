#!/usr/bin/env python3
"""Connect inlandcustomtech.com to Cloudflare Pages and turn on Email Routing.

Run only after the domain is registered at Cloudflare Registrar.
Safe to re-run: every step checks state before it writes.

    python3 scripts/connect_domain.py
    python3 scripts/connect_domain.py --dry-run
    python3 scripts/connect_domain.py --dest someone@gmail.com

Auth: CLOUDFLARE_API_TOKEN if set, otherwise the wrangler OAuth token in
~/.wrangler/config/default.toml. Needs pages:write and email_routing:write.
Standard library only.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.cloudflare.com/client/v4"
ACCOUNT = "5e5d08c34682034b8be2bf834877cb24"
DOMAIN = "inlandcustomtech.com"
PROJECT = "inland-custom-tech"
DEST = "johnnycorreia27@gmail.com"
LOCAL_PART = "john"


def token():
    t = os.environ.get("CLOUDFLARE_API_TOKEN")
    if t:
        return t
    path = os.path.expanduser("~/.wrangler/config/default.toml")
    try:
        with open(path, encoding="utf-8") as fh:
            m = re.search(r'oauth_token\s*=\s*"([^"]+)"', fh.read())
    except OSError:
        m = None
    if not m:
        sys.exit("No Cloudflare credentials. Set CLOUDFLARE_API_TOKEN or run `wrangler login`.")
    return m.group(1)


TOKEN = None


def call(method, path, body=None):
    """Return (ok, result, [messages]). Never raises on an API-level error."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method)
    req.add_header("Authorization", "Bearer " + TOKEN)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            payload = json.load(e)
        except Exception:
            return False, None, ["HTTP %s" % e.code]
    except urllib.error.URLError as e:
        return False, None, ["network: %s" % e.reason]
    msgs = [m.get("message", "?") for m in (payload.get("errors") or [])]
    return bool(payload.get("success")), payload.get("result"), msgs


def say(s):
    print("\n== %s" % s)


def ok(s):
    print("   ok   %s" % s)


def warn(s):
    print("   WARN %s" % s)


def main():
    global TOKEN
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", default=DOMAIN)
    ap.add_argument("--project", default=PROJECT)
    ap.add_argument("--account", default=ACCOUNT)
    ap.add_argument("--dest", default=DEST, help="Gmail address that receives forwarded mail")
    ap.add_argument("--local-part", default=LOCAL_PART)
    ap.add_argument("--dry-run", action="store_true", help="report state, write nothing")
    a = ap.parse_args()
    TOKEN = token()
    dry = a.dry_run
    todo = []

    def write(method, path, body, label):
        if dry:
            print("   DRY  would %s %s" % (method, path))
            return False
        good, _, msgs = call(method, path, body)
        (ok if good else warn)(label if good else "%s: %s" % (label, "; ".join(msgs)))
        return good

    # -------------------------------------------------------------- preflight
    say("Preflight")
    good, result, msgs = call("GET", "/zones?name=%s" % a.domain)
    if not good:
        sys.exit("   FAIL zone lookup: %s" % "; ".join(msgs))
    if not result:
        warn("%s is not a zone in this Cloudflare account yet." % a.domain)
        warn("Register it at dash.cloudflare.com > Domain Registration, then re-run.")
        return 1
    zone = result[0]["id"]
    ok("zone %s = %s" % (a.domain, zone))

    good, result, msgs = call("GET", "/accounts/%s/pages/projects/%s" % (a.account, a.project))
    if not good:
        sys.exit("   FAIL pages project %s: %s" % (a.project, "; ".join(msgs)))
    ok("pages project %s" % result["name"])

    # --------------------------------------------------------- custom domains
    say("Custom domains on %s" % a.project)
    dpath = "/accounts/%s/pages/projects/%s/domains" % (a.account, a.project)
    _, result, _ = call("GET", dpath)
    have = {d["name"] for d in (result or [])}
    for host in (a.domain, "www." + a.domain):
        if host in have:
            ok("%s already attached" % host)
        else:
            write("POST", dpath, {"name": host}, "attached %s" % host)

    if not dry:
        _, result, _ = call("GET", dpath)
        for d in (result or []):
            print("   %-34s %s" % (d["name"], d.get("status")))
        print("   (certificates take a few minutes to reach 'active')")

    # ---------------------------------------------------------- email routing
    say("Email Routing on %s" % a.domain)
    _, result, _ = call("GET", "/zones/%s/email/routing" % zone)
    if (result or {}).get("status") == "ready":
        ok("already enabled")
    else:
        write("POST", "/zones/%s/email/routing/enable" % zone, {},
              "enabled (Cloudflare added the MX and TXT records)")

    say("Destination address %s" % a.dest)
    apath = "/accounts/%s/email/routing/addresses" % a.account
    _, result, _ = call("GET", apath + "?per_page=50")
    state = {d["email"]: d.get("verified") for d in (result or [])}
    if state.get(a.dest):
        ok("already verified")
    elif a.dest in state:
        warn("registered but NOT verified yet")
        todo.append("Click the Cloudflare verification link in %s" % a.dest)
    else:
        if write("POST", apath, {"email": a.dest}, "added %s" % a.dest):
            todo.append("Click the Cloudflare verification link now in %s" % a.dest)

    addr = "%s@%s" % (a.local_part, a.domain)
    say("Forwarding rule %s -> %s" % (addr, a.dest))
    rpath = "/zones/%s/email/routing/rules" % zone
    _, result, _ = call("GET", rpath + "?per_page=50")
    exists = any(m.get("value") == addr
                 for r in (result or []) for m in (r.get("matchers") or []))
    if exists:
        ok("rule already exists")
    else:
        write("POST", rpath, {
            "name": "%s to gmail" % a.local_part,
            "enabled": True,
            "matchers": [{"type": "literal", "field": "to", "value": addr}],
            "actions": [{"type": "forward", "value": [a.dest]}],
        }, "rule created")

    say("Catch-all -> %s" % a.dest)
    write("PUT", rpath + "/catch_all", {
        "name": "catch-all",
        "enabled": True,
        "matchers": [{"type": "all"}],
        "actions": [{"type": "forward", "value": [a.dest]}],
    }, "catch-all on")

    say("Left for you")
    todo.append('Gmail "Send mail as": docs/DOMAIN-AND-EMAIL.md step 4')
    todo.append("Optional www -> apex redirect rule: docs/DOMAIN-AND-EMAIL.md step 2")
    for i, t in enumerate(todo, 1):
        print("   %d. %s" % (i, t))
    return 0


if __name__ == "__main__":
    sys.exit(main())
