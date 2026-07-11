# Design Guide — poudel-bibek.github.io

A single reference for the site's visual language. Follow it when adding pages, publications, projects, banner images, or thumbnails so everything stays consistent. Style rules live in `assets/css/extended/zz-bright.css`; this document explains the decisions behind them and how to produce matching assets.

## Contents

- [Design principles](#design-principles)
- [Design tokens](#design-tokens)
- [Typography](#typography)
- [Layout](#layout)
- [Components](#components)
- [Page banner images (hero PNGs)](#page-banner-images-hero-pngs)
- [Thumbnails](#thumbnails)
- [Content formatting conventions](#content-formatting-conventions)
- [File conventions](#file-conventions)

## Design principles

1. **Serious and academic.** The site presents research. White space, restrained color, and a scholarly serif carry that tone. No decoration that doesn't inform.
2. **Reading first.** Line length, line height, and font size are tuned for sustained reading. Any change that makes a paragraph harder to read is wrong, whatever else it improves.
3. **One font system.** Every piece of text on the site uses the same family. No per-page or per-component font exceptions.
4. **Light by default, dark available.** The site loads in light mode; the toggle keeps the stock PaperMod dark palette with an adjusted link accent.
5. **Content is untouched by styling.** Visual changes go in CSS/layout files only — never rewrite content markdown to achieve a visual effect.

## Design tokens

Defined in `assets/css/extended/zz-bright.css` as CSS variables (they override PaperMod's defaults in `themes/PaperMod/assets/css/core/theme-vars.css`).

| Token | Light value | Role |
|---|---|---|
| `--theme` | `#ffffff` | Page background (crisp white) |
| `--entry` | `#ffffff` | Card / entry background |
| `--primary` | `#1a1a1a` | Headings, strong text |
| `--content` | `#262626` | Body text |
| `--secondary` | `#5c5c5c` | Meta text (dates, authors, captions) |
| `--tertiary` | `#f0f0f0` | Hover chips, subtle fills |
| `--border` | `#e6e6e6` | Hairline rules and card borders |
| `--code-bg` | `#f5f5f5` | Inline code background |
| `--accent` | `#0f4c81` | Links and interactive text (deep blue) |
| `--accent` (dark mode) | `#7cb3e8` | Link accent on dark background |

Spacing and geometry (inherited from the theme): `--gap: 24px`, `--content-gap: 20px`, `--radius: 8px`, `--main-width: 800px`, `--nav-width: 1024px`.

Rules of use: never hard-code a hex color in new CSS — reference a token. If a new shade is truly needed, add it as a token first with a comment explaining its role. Dark mode gets overrides only when a token looks wrong there (currently only `--accent`).

## Typography

One family everywhere: **STIX Two Text** (Google Fonts), a serif designed for scientific publishing — Times-compatible metrics, better screen rendering. Fallback stack: `'STIX Two Text', 'Times New Roman', Georgia, serif`. Code uses **IBM Plex Mono**.

Loaded in `layouts/partials/extend_head.html`. Weights: 400 (body), 500 (nav, entry titles), 600 (semibold headings), 700 (page titles), 400 italic.

| Text | Size | Line height |
|---|---|---|
| Post/article body (`.post-content`) | 17px | 1.75 |
| Homepage intro, page introductions | 16.5px | 1.7 |
| Nav menu items | 15px, weight 500 | theme default |
| Headings | theme scale | 1.25 on post titles; letter-spacing −0.01em on h1–h3 |

When adding CSS for a new component, do not declare `font-family` unless overriding a legacy hardcoded stack (as done for `teaching.css` headings) — inherit from `body`.

## Layout

- Content column: 800px max, centered. Nav: 1024px.
- Responsive behavior comes from PaperMod; verified breakpoints: 1440 (desktop), 768 (tablet), 390 (phone). Any new component must reflow at those three widths with no horizontal scroll.
- List pages use the white `--theme` background (the stock gray `--code-bg` list background is overridden).
- The homepage hero (photo + intro) is deliberately *not* a card: no border, no shadow. Post entries on the blog list are cards: 1px `--border`, soft shadow that deepens slightly on hover.

## Components

**Links in content.** Accent color, 1px underline at 30% accent opacity, 3px offset; underline darkens to full accent on hover. This applies to body links, publication/project/teaching link rows (arXiv | Video | Code), and homepage intro links. Never remove underlines from in-content links — color alone is not a sufficient affordance on white.

**Navigation.** Text-only, weight 500; the active page gets weight 600 (plus the theme's underline). No icons in the nav.

**Social icons row.** Left-aligned icons with labels underneath (custom styling in `themes/PaperMod/assets/css/extended/custom.css`). Icons stay `--secondary`, darkening to `--primary` on hover — they intentionally do not use the accent.

**Publication / project / teaching entries.** Composed by custom layouts (`themes/PaperMod/layouts/_default/{publications,projects,teaching}.html`) that split the page markdown on `-------------------` separators. Entry titles are weight-500 headings; meta lines (authors, venue) use `--secondary`; link rows use the accent.

## Page banner images (hero PNGs)

Each section page opens with a wide banner PNG under the page title — a collage of tilted "cards" showing samples of the section's actual content (figures from papers, slide pages, project screenshots).

Current assets:

| Page | File | Size |
|---|---|---|
| Publications | `static/posts/publications/images/publications.png` | 2419 × 750 |
| Projects | `static/posts/projects/images/projects.png` | 2436 × 583 |
| Teaching | `static/teaching/images/teaching.png` | 2436 × 583 |
| Home (profile) | `static/hero.png` | 450 × 450 (circle-cropped by CSS) |

How to make a new or updated banner:

1. **Canvas.** ~2400px wide, 580–750px tall, **transparent background** (RGBA PNG). Transparency is what lets the banner sit on both the white theme and dark mode without a visible box.
2. **Content.** Pick 3–5 representative visuals from the section itself — real paper figures, real slides, real screenshots. Authenticity is the point; don't use stock art or abstract decoration.
3. **Card treatment.** Place each visual on a white rounded-corner card (radius ≈ 20–30px at this resolution) with a small padding margin, a thin light-gray border, and a soft drop shadow (large blur, low opacity, slight downward offset).
4. **Arrangement.** Fan the cards across the full width with slight overlaps and small alternating rotations (±3–8°). Keep the overall silhouette roughly horizontal — the composition should read as one band, not scattered pieces.
5. **Legibility check.** At the rendered width (~800px in the content column) card contents shrink ~3×; text inside the cards should be *suggestive*, not necessarily readable. Avoid tiny high-frequency detail that turns to noise.
6. **Export.** PNG with alpha, no background layer. Keep file size reasonable (< 1.5 MB; use lossless optimization like `pngquant`/`oxipng` if needed).
7. **Both modes.** Preview on white *and* dark backgrounds before committing — white cards with shadows work on both; shadows baked as dark halos do not.

The homepage profile image (`static/hero.png`) is separate: square, ≥ 450 × 450, face centered — the theme circle-crops it, so keep important content away from corners.

## Thumbnails

Publication and project entries show a 350 × 350 thumbnail, referenced from content by tag: `[thumbnail:name]` → `static/posts/{publications,projects}/thumbnails/name.png`.

- Exactly 350 × 350 px, white background (RGB is fine here).
- Use the key figure of the paper/project; crop rather than letterbox.
- The tag name must match the filename (lowercase, hyphens): `[thumbnail:joint-pedestrian]` → `thumbnails/joint-pedestrian.png`.
- `scripts/generate_thumbnails.py` can generate placeholder thumbnails while a real figure is prepared.

## Content formatting conventions

The custom section layouts parse markdown structurally — formatting is meaningful:

- Entries are separated by a line of exactly `-------------------` (19 hyphens).
- Each entry starts with an `####` title line.
- The `[thumbnail:name]` tag goes on its own line right after the title.
- Author lines bold the site owner: `__Bibek Poudel__`.
- Link rows use ` | ` separators: `[arXiv](…) | [Video](…) | [Code](…)`.
- Front matter must not contain duplicate keys (breaks the build on Hugo ≥ 0.146).

## File conventions

- Site-level overrides beat theme files: prefer adding to `layouts/` and `assets/` at the repo root over editing `themes/PaperMod/` (keeps future theme updates painless).
- Custom CSS lives in `assets/css/extended/` — files load alphabetically after all theme CSS, so a `zz-` prefix guarantees last word in the cascade.
- Static assets: lowercase, hyphenated filenames.
- PDFs live in `content/pdfs/…` next to a small `.md` stub that renders them through `layouts/_default/pdf.html`.
