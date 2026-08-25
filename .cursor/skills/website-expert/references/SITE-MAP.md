# Site map — Walter's Home Improvement

## Public pages

```text
index.html       Home
  ├─ #hero       Hero + primary CTAs (call / estimate)
  ├─ contact teaser / free estimate band
  ├─ stats / trust bar
  ├─ #services   Service cards
  ├─ featured projects / trust content
  ├─ contact details + hours
  └─ CTA band + sticky call + footer

gallery.html     Project gallery
  ├─ category filter buttons
  ├─ #galleryGrid items (data-category, data-index)
  └─ #lightbox controls

reviews.html     Testimonials + external review platform cards
faq.html         Accordion FAQ + CTA
estimate.html    Free estimate form + contract PDF download
```

## Shared files

| Path | Role |
|------|------|
| `styles.css` | Global design system + component styles |
| `nav.js` | Mobile hamburger menu |
| `images/` | Logos, gallery photos, media |
| `Logo.png` | Brand asset |
| `Dads New Contract 2026_Updatd February.pdf` | Downloadable contract from estimate page |

## Tooling (not public site chrome)

- `enhance_*.py`, `batch_enhance_gallery.py`, `convert_images.py`, `check_missing_images.py`, `remove_missing_images.py`
- `demo_enhancements.py`, `enhance_gallery.bat`, `install_pillow.bat`
- Docs: `*_README.md`, `*_GUIDE.md`
- `test_email.html` — EmailJS test harness

## Navigation model

Public nav links:

1. Home → `index.html` / `#hero` (on home)
2. Services → `index.html#services` or `#services` on home
3. Reviews → `reviews.html`
4. Gallery → `gallery.html`
5. FAQ → `faq.html`
6. Get Estimate → `estimate.html`

## Brand CTAs

- Primary conversion: `estimate.html`
- Urgency / mobile: `tel:+14438295946`
- Secondary office: `tel:+14105576116`
- Email: `mailto:whoward45@gmail.com`
