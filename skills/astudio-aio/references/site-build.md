# Building the site

How to turn the direction contract, the brand kit and the copy deck into pages. Read with `reference/studio-bar.md`
(the bar: wow first screen, richness floor, grids, stock + code images), `layout.md`, `typography.md`, `color.md`,
`motion.md`, `imagery.md` and the `ui-styling` skill for the implementation layer.

## 1. Stack decision
- Existing project: use its framework, styling method (Tailwind v3/v4, CSS modules, styled-components, plain CSS),
  component library and conventions. Check the dependency file before adding anything. No migrations unasked.
- Greenfield with no stated stack: a static site (`index.html` + `styles.css` + `main.js`, other pages as `.html`) that
  opens from the file system and deploys anywhere; tokens from `design-tokens/tokens.css`; Google Fonts link; no build
  step. If the user wants React/Next/Astro, scaffold that instead and use `tailwind-theme.css`.
- Single-file deliverable requested: inline CSS/JS, keep it under a few hundred KB, images as files beside it.

## 2. Order of work (build still first)
0. **Assets first**: download the stock photo set (`studio-bar.md` §7), choose the icon set, draw the graphic
   language kit in SVG (stickers/badges, patterns, illustrations, dividers from the logo's geometry). A page cannot
   be rich if its assets are decided last.
1. **Tokens** in place (CSS vars). Everything downstream references tokens only. Grid: 12/8/4 columns.
2. **Skeleton**: semantic HTML (header/nav/main/sections/footer), one `h1`, a heading per section, skip link.
3. **Hero exactly as FIRST VIEWPORT** at 1440 and 390, built from a hero pattern (`search.py -d hero`) and the
   references: dominant visual ≥ half the viewport, layered depth (picture / type / foreground detail), a headline with
   presence, one real primary button, essentials readable. No empty band above or below the headline.
4. **Each section from its own composition** (`search.py -d section`) carrying the idea (pricing and footer
   included), each with a visual anchor (photo, illustration, icons, UI, map, 3D). Neighbours differ.
5. **Imagery** per `reference/imagery.md`; credits recorded.
6. **The live thing** (Persuade) or **signature element** (Operate fragment) with real content and a no-JS fallback.
7. **States**: hover (behind `(hover:hover)`), focus-visible, active, disabled, loading, empty, error; form validation.
8. **Browser surfaces themed**: `::selection`, caret-color, scrollbar colours, focus ring, link underline offset,
   `theme-color` meta per scheme, favicon set from the logo kit.
9. **Meta**: `<title>`, description, canonical, Open Graph image (1200×630 from banner-design), `lang`, JSON-LD only
   for real data (LocalBusiness hours/address, Product price, FAQPage for a real FAQ).
10. Gate → look → fix → motion → look again (SKILL.md Phase 4).

## 3. Hero compositions (choose from the idea and the hero library `search.py -d hero`, not by habit)
- **Name as monument**: the name set very large across the width, description and action docked at an edge.
- **Object hero**: the product/object large (photo, 3D, drawn), text docked beside it on an off-centre line.
- **Full-bleed place**: one photograph of the place/moment, text in its calm region with a scrim, action visible.
- **Statement + proof**: a two-line claim and the proof beside it (the interface at work, a real number, a demo).
- **Artefact as page**: the subject's printed thing is the structure (a menu, a ticket, a label, a timetable).
- **Live hero**: the live thing itself is the first screen (configurator, calculator, availability).
Avoid by default: centred headline + subtitle + two buttons + screenshot; headline left + screenshot right + badge row;
a hero that is only a mood with no title.

## 4. Section compositions (vary between neighbours)
split (text one side, picture the other) · full-bleed picture with docked caption · statement (one large paragraph) ·
list/index (rows with preview on hover/focus) · mosaic (unequal pictures, aligned bottoms) · table (real comparison) ·
strip (horizontal row scrolling inside its frame) · pinned story (heading holds while items pass, ≤ 3 screens) ·
colour field chapter · figures (2-4 real numbers set large, each with its context) · timeline/steps (only a real
sequence) · FAQ as the real questions in the page's voice · contact as the real map/address set large.

## 5. Common page types - what they must contain
- **Restaurant / café**: what and where + hours in the first screen with a mouth-watering visual (coffee/food/the
  room: stock photos with one grade, or the client's); benefits with icons; the full menu as a designed component
  (category tabs with icons, item photos or illustrations, sizes in aligned columns, prices in tabular figures,
  signature item highlighted); the craft/process with photos; an atmosphere gallery; booking or call; location with a
  stylised map, entrance photo, hours table with today highlighted, route buttons. Graphic language (stickers with
  hours/offers, patterns from the logo, a marquee of menu items) across the page.
- **Product / SaaS**: what it is and who it is for; the product shown working (real UI fragments built per dashboard
  rules); how it works; pricing with what is included; proof beside claims; FAQ of real objections; sign-up.
- **Service business**: the outcome; the services with prices or "from" prices; process; proof (cases with numbers);
  area served; contact/booking.
- **Portfolio / studio**: the work fills the first screen; an index of projects; each case with context, role, result;
  contact. No skills bars, no "passionate about".
- **E-commerce**: category/collection navigation; product cards with real photos, price, variant info; product page
  with gallery, sizes, delivery and returns, add to cart; trust signals that are true.
- **Event**: what, when, where in the first screen (dates large); programme/speakers complete; tickets with prices;
  venue and travel.
- **Real estate / hotel**: the place as a picture; each unit/room with its own details and rate; availability/booking;
  location.

## 6. Code quality floor
- Semantic HTML; buttons are buttons, links are links; forms have labels, autocomplete, correct types/inputmode.
- Mobile-first CSS; `min-height: 100svh` heroes; no horizontal scroll; images with width/height or aspect-ratio,
  AVIF/WebP + srcset, lazy below the fold; fonts subset + display swap; transform/opacity-only motion.
- CSS specificity under control (avoid `.section` vs `.cta` fights over padding); a consistent spacing scale.
- No dead code, no console errors, no placeholder links (`href="#"` only where a real target will be wired - list it).
- Forms without a backend: `mailto:` with a prefilled subject/body, or a clearly marked `#todo` and a note in the
  report. Never fake a payment form.

## 7. Multi-page sites
Finish the home page to final quality and get approval. Then: shared header/footer components, page templates reusing
section compositions with page-specific content, consistent heading/anchor lines, one navigation model, active states.
Render every page at the three widths before delivery.
