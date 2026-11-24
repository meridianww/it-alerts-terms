#!/usr/bin/env python3
"""Builds the three public pages for the Meridian IT Alerts text message program.
Usage: python -I build.py <contact email> <out folder>
Plain HTML, no scripts, no outside resources."""
import html
import os
import sys

COMPANY = "Meridian Worldwide Transportation Group"
PROGRAM = "Meridian IT Alerts"
UPDATED = "November 23, 2026"

CSS = """
:root { --ink:#1b2430; --muted:#566170; --line:#d9dee5; --bg:#ffffff; --link:#0b5cad; }
@media (prefers-color-scheme: dark) { :root { --ink:#e8ecf1; --muted:#a6b0bd; --line:#364150; --bg:#141a22; --link:#7db8f5; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:17px/1.6 -apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
main { max-width:720px; margin:0 auto; padding:32px 16px 64px; }
header p { color:var(--muted); margin:0 0 4px; font-size:15px; }
h1 { font-size:28px; line-height:1.25; margin:0 0 6px; }
h2 { font-size:19px; margin:28px 0 6px; }
p { margin:0 0 12px; }
a { color:var(--link); }
nav, footer { border-top:1px solid var(--line); margin-top:36px; padding-top:16px; color:var(--muted); font-size:15px; }
ul { padding-left:22px; margin:0 0 12px; }
"""


def page(title, body, contact):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | {html.escape(COMPANY)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<header>
<p>{html.escape(COMPANY)}</p>
<h1>{html.escape(title)}</h1>
<p>Last updated: {UPDATED}</p>
</header>
{body.strip()}
<nav>
<a href="terms.html">SMS Terms and Conditions</a> &nbsp;|&nbsp; <a href="privacy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="index.html">About this program</a>
</nav>
<footer>
{html.escape(COMPANY)} &middot; Questions: <a href="mailto:{html.escape(contact)}">{html.escape(contact)}</a>
</footer>
</main>
</body>
</html>
"""


def build(contact):
    c = f'<a href="mailto:{html.escape(contact)}">{html.escape(contact)}</a>'
    terms = f"""
<h2>1. Program</h2>
<p>&ldquo;{PROGRAM}&rdquo; is a text message program run by {COMPANY} (&ldquo;Meridian&rdquo;).</p>
<h2>2. What we send</h2>
<p>Automated alerts about the status of Meridian&rsquo;s servers and business applications. Examples: an application that has stopped responding, a server drive that is running low on space, or a failed software deployment. We also send a message when the problem is resolved.</p>
<p>The program is for Meridian employees and IT contractors who have agreed to receive these alerts. It is not offered to customers or the public, and it carries no marketing.</p>
<h2>3. Message frequency</h2>
<p>Message frequency varies with system events.</p>
<h2>4. Cost</h2>
<p>Message and data rates may apply. Meridian does not charge for these messages.</p>
<h2>5. How to stop</h2>
<p>Reply <strong>STOP</strong> to any message. You will receive one message confirming that you have been removed, and no further alerts. Reply <strong>START</strong> to rejoin.</p>
<h2>6. Help</h2>
<p>Reply <strong>HELP</strong> to any message, or email {c}.</p>
<h2>7. Carriers</h2>
<p>Mobile carriers are not liable for delayed or undelivered messages.</p>
<h2>8. Privacy</h2>
<p>See the <a href="privacy.html">{PROGRAM} Privacy Policy</a>.</p>
<h2>9. Changes</h2>
<p>We may update these terms. The date at the top of this page shows the latest version.</p>
"""
    privacy = f"""
<p>This policy covers the &ldquo;{PROGRAM}&rdquo; text message program run by {COMPANY} (&ldquo;Meridian&rdquo;). The program sends IT system alerts to Meridian employees and IT contractors who have agreed to receive them.</p>
<h2>What we collect</h2>
<ul>
<li>Your name</li>
<li>Your mobile phone number</li>
<li>The record of your agreement to receive alerts</li>
<li>Delivery records for the messages we send you</li>
</ul>
<h2>How we use it</h2>
<p>Only to send you IT system alerts, to manage the alert list, and to keep a record of consent.</p>
<h2>Who we share it with</h2>
<p>Our text messaging provider and the mobile carriers, solely to deliver the messages.</p>
<p>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Text messaging opt-in data and consent will not be shared with any third parties.</p>
<h2>How long we keep it</h2>
<p>For as long as you are on the alert list, and for four years afterwards as a record of consent.</p>
<h2>Your choices</h2>
<p>Reply <strong>STOP</strong> to any message to leave the program, or reply <strong>HELP</strong> for help. To see, correct or delete the information we hold about you, email {c}.</p>
<h2>Changes</h2>
<p>We may update this policy. The date at the top of this page shows the latest version.</p>
<p>See also the <a href="terms.html">{PROGRAM} SMS Terms and Conditions</a>.</p>
"""
    index = f"""
<p>{PROGRAM} is a text message program that sends automated IT system alerts to {COMPANY} employees and IT contractors who have agreed to receive them. It is not offered to customers or the public.</p>
<ul>
<li><a href="terms.html">SMS Terms and Conditions</a></li>
<li><a href="privacy.html">Privacy Policy</a></li>
</ul>
<p>Message frequency varies. Message and data rates may apply. Reply STOP to any message to opt out, or HELP for help.</p>
"""
    return {"terms.html": page(f"{PROGRAM}: SMS Terms and Conditions", terms, contact),
            "privacy.html": page(f"{PROGRAM}: Privacy Policy", privacy, contact),
            "index.html": page(PROGRAM, index, contact)}


if __name__ == "__main__":
    contact, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for name, text in build(contact).items():
        with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(name, len(text))
