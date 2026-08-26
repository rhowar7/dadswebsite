# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static marketing website for Walter's Home Improvement, a home-improvement
contractor in Jarrettsville, Maryland. The site's job is to produce phone calls
and estimate requests from local homeowners; weigh changes against that.

Plain HTML/CSS/JS. No build step, no package manager, no framework, no test
framework in the repo.

## Branches — read this before doing anything

- **`main` is the live branch.** GitHub Pages serves it at
  `https://rhowar7.github.io/dadswebsite/`.
- **`master` is stale and abandoned**, 15 commits behind `main`. It is the
  original single commit. Branching from it, or auditing it, produces work that
  does not apply to the real site. Always confirm with
  `git merge-base --is-ancestor origin/main HEAD` before starting.

The production site is GitHub Pages serving `main` at the custom domain
`https://www.waltershomeimprovement.com` (the `CNAME` file in the repo root is
what binds the domain — do not delete or edit it). With the custom domain the
site serves at the domain root, so `robots.txt` and `sitemap.xml` work as
crawlers expect and the absolute URLs in the pages are correct.
**`.htaccess` is inert on Pages** — it is kept only for a possible move to
GoDaddy cPanel hosting (its https/www canonicalization is handled by Pages
itself; its `/faq.html` 301 does not run, so that URL 404s). DNS lives in the
owner's GoDaddy account: four apex A records to GitHub Pages plus
`CNAME www -> rhowar7.github.io`.

## Running and verifying

```bash
python3 -m http.server 8080          # serve the repo root; open http://127.0.0.1:8080
```

There is no test runner. Verify changes by driving a real browser — Chromium is
available at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, and
`playwright-core` can be installed into a scratch directory (not into this
repo — it has no `package.json` and should not gain one).

What is worth asserting, because each has broken here before: no `pageerror` on
any page; no 4xx for any local asset; the gallery lightbox opens on click *and*
on Enter/Space; the estimate form blocks a malformed email and an incomplete
phone; a failed send leaves the form and its contents intact.

`python3` with Pillow handles image work. Nothing else is installed by default.

## Architecture

### Everything is duplicated per page

There are no includes, partials or templates. The navbar and footer are
hand-copied into all six pages, so a nav change is six edits. Concretely:

- The phone number appears ~38 times as `tel:+14438295946` and ~32 times as the
  display string `(443) 829-5946`. **Changing it means searching for both
  forms** across every `.html`.
- The footer is now identical on all six pages and its layout lives in
  `styles.css` (`.footer-grid`, `.footer-col`, `.footer-bottom`), so a styling
  change is one CSS edit. The *markup* is still hand-copied six times — a
  content change (a new link, changed hours) is still six edits. Only
  `index.html` differs: its Services link is `#services`, the others
  `index.html#services`.

Prefer adding a shared class in `styles.css` over another inline copy.

### CSS lives in three places

1. `styles.css` — the shared stylesheet.
2. Page-local `<style>` blocks in the `<head>` of `gallery.html` and
   `reviews.html`. Gallery's lightbox and filter styling lives here, invisible
   from `styles.css`.
3. Inline `style=""` attributes — pervasive, ~222 on `index.html` alone, where
   whole grid layouts are built inline. **Media queries cannot reach inline
   styles**, so a responsive fix applied in `styles.css` will silently fail on
   any element styled inline. Check which of the three governs an element
   before editing.

`.btn-outline` is white-on-transparent and only legible over the dark hero;
`.btn-outline-navy` is its light-background counterpart. Using the wrong one
produces invisible buttons.

### gallery.html

122 hand-maintained `.gallery-item` divs, each one line, categorised by
`data-category` (`bathrooms`, `kitchens`, `decks`, `siding`, `other`) and
filtered client-side by toggling a `.hidden` class.

**The grid serves thumbnails, the lightbox serves originals.** Photos wider
than 700px have a 500px copy in `images/thumbs/`; the tile's `src` points at
the thumbnail and `data-full` at the original. `showCurrent()` reads
`data-full` first and only falls back to `currentSrc` for the smaller photos
that never got a thumbnail. **If you add a photo, either give it both
attributes or leave it un-thumbnailed — a `src` pointing at a thumbnail with
no `data-full` shows a blurry image in the lightbox.** Regenerate with the
same recipe: Pillow, `ImageOps.exif_transpose`, 500px wide, quality 82,
progressive. Every tile also carries `width`/`height` so the grid does not
shift as photos load.

Two ordering constraints in the inline script, both of which have caused real
breakage:

- **The lightbox markup must precede the script.** The script resolves
  `#lightbox`, `#lightboxClose` etc. at parse time; if the markup comes after,
  every lookup is `null` and the binding throws, killing the rest of the script
  so clicking any photo does nothing.
- **The `?filter=` deep-link handler must run last**, after `let current` is
  initialised. It calls `applyFilter`, which assigns `current`; running it
  earlier hits the temporal dead zone and throws on any `?filter=` URL only —
  so the plain page still looks fine.

Tiles are `div`s with `role="button" tabindex="0"` and hand-wired Enter/Space
handling; they are not real buttons. The lightbox manages focus (moves in,
traps Tab across its three controls, restores on close) and reuses
`img.currentSrc` so opening a photo does not refetch it.

### estimate.html

Six fields — name, phone, work type, town/ZIP, email, description — of which
the first four are required. Email is deliberately optional: a contractor calls
back, and demanding an address costs leads. `timeline` and the old
"Online Form / Call Now" tab switcher were removed for the same reason. Keep
the field count down; every field added is a lead lost.

**No third-party script.** The form posts JSON to Formspree
(`https://formspree.io/f/xgawggqe`) with `fetch`. The previous EmailJS
integration failed silently in production for months — its Gmail OAuth token
expired, EmailJS returned `412 Gmail_API: Invalid grant`, and because EmailJS
only relays and never stores, every lead in that window ceased to exist.
Formspree records the submission before emailing it, so a delivery failure is
recoverable from its dashboard. Do not reintroduce a CDN-loaded form library.

The payload uses human-readable keys (`Name`, `Phone`, `Work needed`,
`Town or ZIP`, `Details`) because Formspree prints them verbatim as the labels
in the email. A field literally named `email` sets Reply-To, and is omitted
entirely when the customer leaves it blank. `_subject` sets the subject line;
`_gotcha` is a hidden spam trap Formspree honours.

The form carries a real `action` and `method="POST"`, so it still submits
correctly if the page's JavaScript never runs — that is why the `<noscript>`
block no longer hides it. It is also `novalidate`, so all validation is
hand-rolled: invalid fields are collected into an array, each gets a message
in a `role="alert"` element, and the first is focused. A send failure must keep
the form and its contents and show `#formError` — never hide the form, which
discards the lead.

### images/

335 files plus `images/thumbs/` (38 generated gallery thumbnails), only ~127
originals referenced. Presence in `images/` does not mean a page
uses it. Check with a grep across the HTML before assuming a file is live or
safe to delete. Roughly 60% of gallery photos are small (~206px) Facebook
downloads displayed larger than their true size; resizing cannot fix that, only
re-exporting from originals can.

## Deploying

The owner has given standing approval to deploy small changes — copy tweaks,
fixes, anything the suites cover — without asking each time, provided the
browser suites pass first. Anything structural (new pages, changed services or
pricing, the form's wiring) still gets confirmed before it goes live.

Deploying is merging to `main` — GitHub Pages publishes it automatically within
a couple of minutes. Note that **the whole repo is published**, including the
one-off Python image scripts, `.bat` wrappers and internal `.md` guides in the
root (and this file); anything genuinely sensitive must not live on `main`.

If the site ever moves to cPanel-style hosting, the upload package is a curated
subset, not the whole repo: the six `.html` files, `styles.css`, `nav.js`,
`robots.txt`, `sitemap.xml`, `.htaccess`, `CNAME` excluded, and only the images
the pages actually reference.

The image scripts themselves are unreliable history: several are duplicates of
each other, and they were run without Pillow installed, which silently produced
byte-identical copies rather than optimised images. Do not trust them as
evidence that any image was processed.
