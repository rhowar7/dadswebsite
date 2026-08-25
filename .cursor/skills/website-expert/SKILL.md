---
name: website-expert
description: Website development playbook for Walter's Home Improvement static site. Use when editing pages, CSS, client JS, gallery, reviews, FAQ, estimate form, SEO, or responsive layout.
icon: code
color: blue
paths:
  - "**/*.html"
  - "**/*.css"
  - "**/*.js"
---

# Website expert skill

Use this playbook when working on the Walter's Home Improvement marketing site.

## Quick context

- Static site: HTML + `styles.css` + `nav.js`
- Brand: navy `#1a3660` / gold `#d4a017`
- Business: Jarrettsville, MD home improvement; 46+ years; licensed & insured
- Contacts: (443) 829-5946, (410) 557-6116, whoward45@gmail.com

Read `@AGENTS.md` and `@.cursor/skills/website-expert/references/SITE-MAP.md` for full structure.

## Playbook

1. **Clarify the page** — home, gallery, reviews, FAQ, estimate, or new page.
2. **Copy the nearest template** — structure, nav active state, footer, CTA band.
3. **Reuse the design system** — CSS variables and existing classes in `styles.css`.
4. **Protect business facts** — phone, email, address, years, ratings, licensing.
5. **Wire shared assets** — `styles.css`, `nav.js`, images under `images/`.
6. **Check mobile** — hamburger IDs, 768px breakpoint, sticky call button if present.
7. **Summarize** — files changed, visual checks remaining, what was left alone.

## Common tasks

### New marketing page
- Duplicate chrome from an existing page
- Add nav links on all public pages
- Add footer quick link if it belongs in site IA
- Unique title + meta description

### Visual / CSS fix
- Prefer editing `styles.css` component rules
- Match spacing/type from `index.html` sections
- Keep gold CTAs on navy bands

### Gallery work
- Preserve `data-category`, `data-index`, lightbox wiring
- Keep lazy-loading and descriptive `alt` text

### Estimate form
- Do not casually rename `name`/`id` fields used by EmailJS
- Keep success/error UX and phone formatting behavior
