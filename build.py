#!/usr/bin/env python3
"""Builds the public pages for the Meridian IT Alerts text message program (terms, privacy, consent form, index).
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
.row { display:flex; gap:28px; margin:0 0 6px; }
.f { flex:1 1 0; }
.f.wide { flex:1.6 1 0; }
.line { display:block; height:34px; border-bottom:1.5px solid var(--ink); }
.f label { display:block; font-size:13px; color:var(--muted); margin-top:3px; }
.consent { display:flex; gap:14px; align-items:flex-start; border:1.5px solid var(--ink); border-radius:4px; padding:14px 16px; margin:8px 0 12px; }
.consent p { margin:0; }
.box { flex:0 0 22px; width:22px; height:22px; border:2px solid var(--ink); margin-top:3px; }
.small { font-size:14px; color:var(--muted); }
.office { border-top:1px dashed var(--line); margin-top:22px; padding-top:6px; }
@page { size: Letter; margin: 0.6in 0.75in; }
@media print {
  :root { --ink:#000000; --muted:#333333; --line:#888888; --bg:#ffffff; --link:#000000; }
  body { font-size:10.5pt; line-height:1.4; }
  main { max-width:none; padding:0; }
  h1 { font-size:18pt; } h2 { font-size:12pt; margin:11pt 0 3pt; } p { margin:0 0 6pt; }
  header p { font-size:9.5pt; } .small { font-size:9pt; } .f label { font-size:8.5pt; }
  .line { height:23pt; } .consent { padding:8pt 10pt; margin:5pt 0 7pt; } .office { margin-top:10pt; }
  nav, footer { display:none; }
  a { text-decoration:none; }
}
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
<a href="terms.html">SMS Terms and Conditions</a> &nbsp;|&nbsp; <a href="privacy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="consent-form.html">Consent form</a> &nbsp;|&nbsp; <a href="index.html">About this program</a>
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
<p>To join, a person completes and signs the <a href="consent-form.pdf">{PROGRAM} consent form</a> and returns it to the Meridian IT department. Nobody is added without a signed form.</p>
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
<li><a href="consent-form.pdf">Consent form (PDF)</a>, the form each person signs before receiving any message</li>
</ul>
<p>Message frequency varies. Message and data rates may apply. Reply STOP to any message to opt out, or HELP for help.</p>
"""
    site = "https://meridianww.github.io/it-alerts-terms"
    form = f"""
<p>Use this form to agree to receive IT system alerts by text message from {COMPANY} (&ldquo;Meridian&rdquo;). The program is for Meridian employees and IT contractors only. Nobody is added to the alert list without a signed form.</p>
<h2>1. About you</h2>
<div class="row">
<div class="f wide"><span class="line"></span><label>Full name (please print)</label></div>
<div class="f"><span class="line"></span><label>Mobile phone number</label></div>
</div>
<div class="row">
<div class="f wide"><span class="line"></span><label>Job title</label></div>
<div class="f"><span class="line"></span><label>Employer (Meridian, or your company)</label></div>
</div>
<h2>2. What you will receive</h2>
<p>Automated text messages from {PROGRAM} about the status of Meridian&rsquo;s servers and business applications. Examples: an application that has stopped responding, a server drive that is running low on space, or a failed software deployment. You will also get one reminder a day while a problem stays open and a message when it is resolved. No marketing messages are sent.</p>
<h2>3. Your agreement to receive text messages</h2>
<div class="consent">
<span class="box"></span>
<p><strong>I agree to receive automated IT system alert text messages from {COMPANY} ({PROGRAM}) at the mobile phone number I wrote above.</strong> Message frequency varies with system events. Message and data rates may apply. Reply STOP to any message to opt out, or HELP for help.</p>
</div>
<p>Tick the box to agree. This agreement is for text messages only. You can withdraw it at any time by replying STOP to any message or by emailing {html.escape(contact)}. Meridian does not share mobile phone numbers or text message consent with third parties or affiliates for marketing or promotional purposes.</p>
<p class="small">SMS Terms and Conditions: {site}/terms.html<br>Privacy Policy: {site}/privacy.html</p>
<h2>4. Signature</h2>
<div class="row">
<div class="f wide"><span class="line"></span><label>Signature</label></div>
<div class="f"><span class="line"></span><label>Date</label></div>
</div>
<p class="small">Return the completed form to the Meridian IT department at {html.escape(contact)}. Meridian keeps it as the record of your consent for as long as you are on the alert list and for four years afterwards.</p>
<div class="office">
<p class="small"><strong>For the IT department</strong></p>
<div class="row">
<div class="f"><span class="line"></span><label>Form received by</label></div>
<div class="f"><span class="line"></span><label>Date received</label></div>
<div class="f"><span class="line"></span><label>Confirmation text sent on</label></div>
</div>
</div>
"""
    return {"consent-form.html": page(f"{PROGRAM}: Text Message Consent Form", form, contact),
            "terms.html": page(f"{PROGRAM}: SMS Terms and Conditions", terms, contact),
            "privacy.html": page(f"{PROGRAM}: Privacy Policy", privacy, contact),
            "index.html": page(PROGRAM, index, contact)}


if __name__ == "__main__":
    contact, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for name, text in build(contact).items():
        with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(name, len(text))
