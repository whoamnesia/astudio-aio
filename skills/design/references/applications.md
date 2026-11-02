# Brand applications, social sets, print, posters, patterns

## Stationery (print specs)
| Item | Size | Notes |
|---|---|---|
| Business card | 90×50 mm (RU/EU) · 85×55 (EU) · 3.5×2 in (US) | +3 mm bleed, 4 mm safe margin; text ≥ 7-8 pt; logo + name + role + one or two contacts; back = brand field or pattern |
| Letterhead | A4 210×297 mm | logo top-left, contacts in footer, 20 mm margins; Word/Google Docs template if needed |
| Envelope | DL 110×220 mm / C4 | logo + return address |
| Email signature | ~600px wide HTML table, inline styles | logo PNG 2× hosted, name, role, phone, site; no images-only signatures |
| Menu | A4/A3 or DL; or screen | full items with prices, allergens, real names; type hierarchy for sections; one page per category for large menus |
| Badge / lanyard | 86×54 mm (CR80) / 100×140 mm | name large (≥ 24 pt), readable at 2 m |
| Sticker / label | per die-cut | 2 mm bleed, cut line as a separate spot layer note |
Build each at proportional pixel size in HTML/CSS (e.g. 1 mm = 10 px for a preview), export PDF with `render.cjs pdf`
at the physical aspect; note to the user: final print files need CMYK conversion, 300 dpi images, outlined fonts or
embedded fonts, and a printer proof.

## Social media sets
- Templates for recurring post types (announcement, quote, product, tip/carousel slide, event, story with poll space):
  one grid and type system per ratio (1:1, 4:5, 9:16), editable text regions, brand colour fields, the graphic device.
- Carousels: cover slide = hook headline; inner slides one idea each, consistent position; last slide = CTA; slide
  numbers only when it is a sequence.
- Profile kit: avatar (logo symbol on brand field, survives circle crop), covers per platform (banner-design), highlight
  covers (simple glyphs from the icon set).
- Export each at platform size (`search.py "<platform>" -d banner`), 2× for retina previews if needed.

## Packaging and labels
Hierarchy: brand → product name → variant/flavour (colour-coded system) → key claim → legal/required info (ingredients,
weight, barcode, manufacturer, certification marks - exact data from the client). Dieline from the printer; bleed and
safe areas; contrast for small legal text; mockups only as illustrations.

## Signage and environment
Readable at distance: cap height ≈ 1 cm per 3-5 m viewing distance (rule of thumb); high contrast; logo + one message;
wayfinding pictograms from the icon set; illuminated vs non-illuminated colour notes.

## Merch
T-shirt print area ~30×40 cm chest / 8-10 cm logo for left chest; tote; stickers; mugs - limited colours (screen print
cost per colour), the mark or a pattern from the device, avoid fine hairlines (min ~1 mm lines in print).

## Posters and one-pagers
Poster = one idea readable from 3 m: dominant image or type, headline, essential info (date, place, price, QR), brand
mark; build at A-ratio in HTML (e.g. 2480×3508 px for A4 at 300 dpi preview), export PDF/PNG. One-pager (sales sheet,
product sheet): headline claim, 3-4 proof blocks, visuals of the product, CTA/contacts; print and screen versions.

## Patterns and illustrations from the graphic device
- Pattern: repeat a unit derived from the logo's construction (its arc, cut, counter) on a grid with controlled scale and
  density; SVG `<pattern>` or tiled background; test at small and large scales and as one colour.
- Illustration style: shapes from the brand's geometry, palette-limited (2-4 roles + neutrals), consistent stroke and
  corner logic with the icon set, one light direction. Spot illustrations for empty states and onboarding in the same
  style. Never clip-art or generic "blob people" by default.

## Mockups
Draw in HTML/CSS (CSS perspective, shadows that match a single light source) or composite onto licensed photos (record
licences). Label as mockups. Industry-relevant contexts only.
