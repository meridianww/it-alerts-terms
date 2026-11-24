# Meridian IT Alerts: SMS terms and privacy policy

Public pages for the "Meridian IT Alerts" text message program run by Meridian Worldwide Transportation Group. The program sends automated IT system alerts to Meridian employees and IT contractors who have agreed to receive them.

- [SMS Terms and Conditions](https://meridianww.github.io/it-alerts-terms/terms.html)
- [Privacy Policy](https://meridianww.github.io/it-alerts-terms/privacy.html)
- [Consent form (PDF)](https://meridianww.github.io/it-alerts-terms/consent-form.pdf): the form each person signs before receiving any message

To change the wording, edit `build.py`, run `python -I build.py <contact email> .` and commit the HTML files.

If the consent form changed, print `consent-form.html` to `consent-form.pdf` again (Letter size, no headers or footers, one page) and commit it too. With Edge: `msedge --headless=new --no-pdf-header-footer --user-data-dir=<empty folder> --print-to-pdf=consent-form.pdf <file URL of consent-form.html>`.
