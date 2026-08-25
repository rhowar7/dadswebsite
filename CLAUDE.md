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

The site is being migrated to GoDaddy cPanel hosting at
`www.waltershomeimprovement.com`. `.htaccess`, `robots.txt` and `sitemap.xml`
target that host and domain — **`.htaccess` does nothing on GitHub Pages**, and
a `robots.txt` in a Pages *project* repo is served at `/dadswebsite/robots.txt`
and never read by crawlers. Absolute URLs in the pages name the GoDaddy domain,
so publishing to Pages and to GoDaddy are not equivalent.

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
hand-copied into all seven pages, so a nav change is seven edits. Concretely:

- The phone number appears ~38 times as `tel:+14438295946` and ~32 times as the
  display string `(443) 829-5946`. **Changing it means searching for both
  forms** across every `.html`.
- Footers have drifted before — index/service-areas carry a rich three-column
  footer, the rest a two-line stub. Check all seven when touching either.

Prefer adding a shared class in `styles.css` over another inline copy.

### CSS lives in three places

1. `styles.css` — the shared stylesheet.
2. Page-local `<style>` blocks in the `<head>` of `estimate.html`, `faq.html`,
   `gallery.html` and `reviews.html`. Gallery's lightbox and filter styling
   lives here, invisible from `styles.css`.
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

The only page with a third-party dependency: EmailJS from jsDelivr, loaded
`defer` and initialised lazily on first send. This is deliberate — as a
blocking script it sat ahead of the inline script that binds every handler, so
a slow or blocked CDN meant no working form at all.

The form is `novalidate` with no `action`, so all validation is hand-rolled and
a JS failure would otherwise submit a GET with the customer's details in the
query string; a `<noscript>` block hides the form and directs to the phone
number instead. Validation collects invalid fields into an array, writes a
per-field message into a `role="alert"` element, and focuses the first one. A
send failure must keep the form and its contents and show `#formError` — never
hide the form, which discards the lead.

`to_email` is passed as a template parameter. Do not remove it without first
confirming the EmailJS template's To field has been hardcoded, or leads stop
arriving.

### images/

335 files, only ~127 referenced. Presence in `images/` does not mean a page
uses it. Check with a grep across the HTML before assuming a file is live or
safe to delete. Roughly 60% of gallery photos are small (~206px) Facebook
downloads displayed larger than their true size; resizing cannot fix that, only
re-exporting from originals can.

## Deploying

The deployable site is a curated subset of the repo, not the whole thing. The
root also holds one-off Python image scripts, `.bat` wrappers and internal `.md`
guides — **anything placed in the web root is publicly served**, so these must
be excluded from any upload. Build the package by copying the seven `.html`
files, `styles.css`, `nav.js`, `robots.txt`, `sitemap.xml`, `.htaccess`, and
only the images the pages actually reference.

The image scripts themselves are unreliable history: several are duplicates of
each other, and they were run without Pillow installed, which silently produced
byte-identical copies rather than optimised images. Do not trust them as
evidence that any image was processed.
