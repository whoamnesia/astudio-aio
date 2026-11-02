# Logo kit, guidelines, presentation, redesign, critique

## 1. Kit contents
```
brand/logo/
  <brand>-symbol-color.svg / -black / -white / -mono      symbol only
  <brand>-horizontal-color.svg / -black / -white            symbol + wordmark side by side
  <brand>-stacked-color.svg / -black / -white               symbol above wordmark
  <brand>-wordmark-color.svg / -black / -white
  <brand>-small.svg                                         simplified 16-32px cut
  <brand>-app-icon.svg, <brand>-favicon.svg (dark-aware)
  png/   512, 1024, 2048 + transparent social avatars 400×400
  web/   favicon.ico, 16/32/48/180/192/512 PNG, site.webmanifest, head-snippet.html
  logo-guidelines.html                                      one-page usage guide (render to PDF with render.cjs pdf)
```
Lockup rules: relative sizes locked (wordmark cap height = a stated fraction of symbol height), gap = a unit of the
mark (e.g. one counter width), optical vertical centring of wordmark to symbol.

## 2. Guidelines one-pager
- **Clear space** defined by an element of the logo (e.g. the height of the symbol's counter or the wordmark's x-height)
  on all sides.
- **Minimum size**: digital (px) for full lockup and symbol; print (mm).
- **Colour**: HEX, RGB, CMYK (approx.), Pantone suggestion (verify), approved backgrounds with the right variant
  (colour on light, white on brand/dark, black/white mono when colour is unavailable).
- **Misuse** (show 6 small examples): stretched, rotated, recoloured off-palette, effects added (shadow/glow/gradient),
  rearranged elements, busy background without container, outlined, cropped.
- **Co-branding**: equal visual weight, divider line, both clear spaces respected.
- **File guide**: which file for which use (web SVG, print PDF/EPS from a vector editor, social PNG, app icon).

## 3. Presentation board
Build in HTML/CSS and render (render.cjs shots/element). A strong board has rhythm, not equally loud panels:
1. Cover - the mark large with the wordmark, lots of negative space.
2. Construction - grid/geometry/negative-space logic showing why the mark exists.
3. Digital application - website header, app icon on a home screen, browser tab, social avatar.
4. Essence - one short tagline set large.
5. Colour - swatches with roles and contrast values.
6. Typography - the wordmark's family or the paired brand faces in a specimen.
7. Physical application - relevant to the business: cup/bag/menu (café), card/letterhead (consultancy), packaging
   label (product), signage/storefront (retail), badge/lanyard (events), vehicle livery (logistics).
8. Image direction - a crop of the brand's world (found or drawn).
9. System detail - icon row, pattern made from the mark, UI chips.
Mockups are drawn in CSS (shapes, perspective transforms, the logo applied) or composited on licensed photos; label
them as mockups. Industry-relevant beats generic.

## 4. Redesign / refresh
Audit equity first: what do customers recognise (colour, shape, a letter, the name's treatment)? Choose:
- **Refresh** (keep equity, fix craft): simplify details, fix geometry and spacing, modernise letterforms, add a
  small-size cut, rationalise colours.
- **Evolution** (keep one recognisable trait, rebuild the rest).
- **Rebrand** (new mark - only when the old one carries negative or no equity, or the business changed).
Show old vs new side by side at the same sizes and contexts; explain what was kept and why.

## 5. Critique (scorecard 1-5 each)
Idea (one sentence, ownable) · Distinction (vs category) · Simplicity (survives 16px, squint) · Relevance (fits
adjectives without literalism) · Craft (geometry, optical corrections, spacing, junctions) · Versatility (one colour,
reversed, lockups, app icon) · Timelessness (concept over effect). For each score < 4: the concrete problem and the
fix ("the counter of the 'a' closes at 24px - widen from 6 to 10 units"). End with the single highest-leverage change.

## 6. Presenting in chat
Show the image first; keep text short; one honest risk per concept; one recommendation; one question (pick / adjust /
build the kit). Never dump all variants before a direction is chosen.
