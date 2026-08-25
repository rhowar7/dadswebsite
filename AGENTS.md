# Walter's Home Improvement — Agent Instructions

This repo is the marketing website for **Walter's Home Improvement** (`waltersimprovement.com`), a family-owned home remodeling business in Jarrettsville, Maryland.

## Stack

- Static HTML / CSS / vanilla JS (no framework, no bundler, no build step)
- Shared stylesheet: `styles.css`
- Shared mobile nav: `nav.js`
- Assets: `images/`, root `Logo.png`, contract PDF at repo root
- Preview: open HTML files directly in a browser (or any static file server)

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Home — hero, services, trust/stats, contact CTAs |
| `gallery.html` | Project photo gallery + lightbox + category filters |
| `reviews.html` | Customer reviews + review-site links |
| `faq.html` | FAQ accordion |
| `estimate.html` | Free estimate form (EmailJS) + contract download |
| `test_email.html` | EmailJS testing helper (not a public marketing page) |

## Brand & business facts (do not invent alternatives)

- Business name: Walter's Home Improvement
- Tagline themes: family owned, 46+ years, licensed & insured, free estimates
- Mobile: `(443) 829-5946` → `tel:+14438295946`
- Home office: `(410) 557-6116` → `tel:+14105576116`
- Email: `whoward45@gmail.com`
- Address: 3867 Colwyn Drive, Jarrettsville, MD 21084
- Hours: 7:00 AM – 8:00 PM, 7 days a week
- Service areas: Jarrettsville, Forest Hill, Bel Air, Aberdeen, Havre de Grace, surrounding MD
- Primary services: roofing, bathrooms, kitchens, windows, decks & porches, painting, siding, flooring, and related home improvement

## Design system

CSS variables in `styles.css` `:root`:

- `--navy` `#1a3660`, `--navy-dark` `#112347`, `--navy-light` `#2a5298`
- `--gold` `#d4a017`
- `--off-white` `#f4f6fa`, `--gray` `#6b7280`, `--gray-light` `#e5e9f2`
- `--radius` `8px`, `--shadow`, `--transition`

Reuse existing classes (`.navbar`, `.btn`, `.btn-primary`, `.btn-outline`, `.section-title`, `.section-label`, `.cta-band`, form classes, gallery classes). Prefer extending `styles.css` over large new inline style blocks.

## Conventions

1. Keep shared chrome consistent: sticky navy navbar, hamburger (`#hamburger` / `#navLinks`), footer, sticky mobile call button where present.
2. Every public page loads `styles.css` and `nav.js`.
3. Mark the current page with `class="active"` on the matching nav link.
4. Preserve SEO: unique `<title>`, meta description, and structured data where already present.
5. Prefer semantic HTML and accessible labels/`alt` text; gallery images should keep descriptive alts.
6. Mobile-first: test around ~375px and desktop; hamburger breakpoint is 768px in `nav.js` / CSS.
7. Do not introduce React/Vue, npm build tooling, or CSS frameworks unless explicitly asked.
8. Do not change phone, email, address, or licensing claims without an explicit request.
9. Image enhancement Python scripts (`enhance_*.py`, etc.) are tooling — keep them separate from public page edits unless asked.
10. Prefer small, page-scoped edits over repo-wide refactors.

## Workflow

- Match layout/spacing/typography to the closest existing page (`index.html` is the visual reference).
- Put shared styles in `styles.css`; keep page-only CSS in a `<style>` block only when truly page-specific (gallery/faq already do this).
- After UI changes, sanity-check navbar, footer links, CTAs, and mobile menu.
- When adding a page, update nav links on **all** public pages.
