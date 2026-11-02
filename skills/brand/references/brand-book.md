# The brand book page

`brand/brand-book.html` - a single responsive page built **with the brand's own tokens and faces** that documents the
system and proves it works. It is a designed artefact, not a form: let the brand's world structure it.

## Sections (in this order, each with a real heading)
1. **Cover** - the logo large on the brand's ground, the promise in one line, version/date small.
2. **The idea** - positioning in two sentences + the direction's thesis; one image of the brand's world.
3. **Logo** - primary lockup; variants (horizontal/stacked/symbol/wordmark) on light, dark and brand grounds;
   construction diagram (SVG overlay of the grid/circles); clear space shown with the measuring element; minimum sizes;
   misuse grid (6 small crossed examples, drawn with CSS transforms/filters on the real SVG).
4. **Colour** - each role as a field (not a tiny chip) with name, HEX/RGB/OKLCH, role, contrast on its ground (computed
   with palette.py; write the values in); light and dark sets; proportion bar showing the shares; do/don't pairs.
5. **Typography** - display and text faces in a real specimen using brand copy (not "Aa" and the alphabet alone): the
   scale from display to caption with sizes at 390 and 1440, leading/tracking notes; Cyrillic specimen if relevant;
   licence and source.
6. **Shape, space and depth** - radius logic demonstrated on real components; spacing scale; elevation levels.
7. **Components** - buttons (primary/secondary/text/destructive; default/hover/focus/disabled/loading), input with
   label/helper/error, a card/panel, navigation, a badge/status pill - live HTML using tokens.
8. **Iconography and imagery** - the icon set at sizes, photo direction with 2-4 sample images (found/credited or the
   client's), treatments, the graphic device.
9. **Voice** - voice chart, tone by context, CTA vocabulary, before/after rewrites.
10. **Motion** - the signature move demonstrated (respects reduced motion), tokens table.
11. **Applications** - 3-6 mockups relevant to the business, drawn in HTML/CSS (business card, app icon on a home
    screen, storefront sign, social post, email header…), labelled as mockups.
12. **Downloads / files** - list of files in `brand/` and `design-tokens/` with what each is for.

## Build rules
- Import `design-tokens/tokens.css` (or palette.css until tokens exist); no raw hex in components.
- Inline the logo SVGs so colour variants are real files, not CSS filters, where possible.
- Same anti-slop and accessibility rules as any page; render at 1440 and 390, look, fix.
- Optional PDF: `node <root>/scripts/render.cjs pdf brand/brand-book.html --out brand/brand-book.pdf --width 1440 --height 900`
  (add `@media print` page breaks per section).
