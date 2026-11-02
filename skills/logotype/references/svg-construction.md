# Building logos in SVG

Turn a concept into clean, production-grade SVG by hand: geometric, minimal, easy for printers, developers and vector
editors.

## 1. File conventions
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="t">
  <title id="t">Harbor logo</title>
  <path fill="#0F7C80" fill-rule="evenodd" d="…"/>
</svg>
```
- Integer canvas: 256×256 (or 512) for symbols; lockups keep height 256, width follows (`0 0 960 256`).
- Consistent padding (4-8% inside the viewBox) or tight crop with clear space defined in the guidelines - be
  consistent across the set.
- Integer or ≤ 2-decimal coordinates. `<title>`. Meaningful ids (`symbol`, `wordmark`) and `<g>` groups so lockups can be
  recomposed. One file per variant with predictable names (`brand-horizontal-color.svg`, `brand-symbol-black.svg`).

## 2. Think in primitives first
Write the construction in words before path data: "circle r=96 at (128,128); remove a 45° wedge upper-right; a dot
r=28 sits in the gap". "Letter M from three 40-unit bars; middle vertex rises to y=96; outer stems extend 4 units below
baseline for overshoot". Pick a unit (8 or 16 on a 256 canvas) and snap key dimensions to it. Keep a list of the radii
and angles you use and reuse them.
Use `<circle>`, `<ellipse>`, `<rect rx>`, `<polygon>` for primitives while designing; `<path>` for everything else and
for the final merged silhouette.

## 3. Clean paths
- Commands: M, L/H/V, A (elliptical arc - perfect for circle segments), C (cubic), Q, Z. Uppercase = absolute.
- Arcs for circular geometry: `A r r 0 largeArc sweep x y` (semicircle cap: `M64 128 A64 64 0 0 1 192 128`).
- Béziers for organic curves: anchors at extrema with horizontal/vertical handles; a quarter circle as a cubic uses
  handle length ≈ 0.5523 × r.
- Few anchors - every extra point is a chance for a wobble.
- Exact angles from trigonometry: 30°/60° offsets use 0.5 and 0.866; 45° equal x and y. Never 44° or 2° off vertical.
- Smooth corners (anti bone effect): extend the curve so curvature ramps up - start ~1.3 × s before the corner with
  handles ~0.6 × s (squircle-like), instead of a plain arc meeting a straight line.
- Close filled paths with Z.

## 4. Negative space and compound shapes
- Outer contour and holes in **one path** with `fill-rule="evenodd"`:
  `<path fill-rule="evenodd" d="M128 16 A112 112 0 1 1 127.9 16 Z M128 80 A48 48 0 1 0 128.1 80 Z"/>`
  This is what makes one-colour, reversed and embroidered versions work - a white shape painted over a coloured shape
  turns into a solid blob in one colour.
- Design the hidden figure (arrow, letter) first, then the positive shapes around it.
- Avoid `<mask>`/`<clipPath>` in the master; bake geometry into paths. Merge touching same-colour shapes into one path
  (no hairline seams).

## 5. Strokes vs fills
Explore with strokes (`stroke-linecap="round"`, `stroke-linejoin="round"`); in the master, construct the outlined
geometry directly (offset by half the stroke width) or keep strokes inside the scaled viewBox and flag them in the
handover for "Outline Stroke + Unite" in a vector editor (Inkscape CLI can do it:
`inkscape logo.svg --actions="select-all;object-stroke-to-path;path-union;export-plain-svg;export-filename:out.svg;export-do"`).
Monoline marks that must read at 24px: stroke ≥ ~8% of the mark width.

## 6. Letterforms
Final logos never depend on installed fonts. Prefer constructing letters geometrically as paths (consistent stem width,
overshoot on round letters, horizontals slightly thinner than verticals, optical spacing - equal *areas* between
letters, not equal distances). If starting from a font, the licence must allow logo use (Google Fonts OFL does);
outline it, then customise one or two letters for ownership. For exploration `<text>` is acceptable if flagged.
Wordmark spacing: round-to-round pairs closest, straight-to-straight furthest; check "LT", "AV", "ra", "ry" pairs;
optical alignment of overhanging letters at the left edge.

## 7. Colour, gradients, variants
Exact HEX from the palette, attributes on elements (`fill="#…"`) rather than `<style>` blocks; `currentColor` for a
UI-friendly one-colour variant. Gradients only with a flat master alongside (`gradientUnits="userSpaceOnUse"` with
explicit coordinates). Variant set: color, black, white (slightly thinned for irradiation), mono-<brand>; lockups
horizontal / stacked / symbol / wordmark; app icon = symbol at ~60-70% of a rounded tile (iOS-style radius ≈ 22.5%);
favicon = small-size cut. `logo_kit.py variants` automates the colour swaps and the app/favicon wrappers.

## 8. Recipes (starting points - add the concept's twist)
```svg
<!-- Open ring (exploration stroke) -->
<path fill="none" stroke="#111" stroke-width="32" stroke-linecap="round" d="M201.5 54.5 A104 104 0 1 0 232 128"/>
<!-- App tile, 22% radius -->
<rect width="256" height="256" rx="56" fill="#0F7C80"/>
<!-- Equilateral triangle centred on its box (nudge up a few units: its centroid sits low) -->
<polygon points="128,40 229.6,216 26.4,216" fill="#111"/>
<!-- Letter A as a symbol: flat apex, 1:2 slopes, constant 48-unit stroke, counter as a real hole -->
<path fill="#111" fill-rule="evenodd" d="M104 32H152L248 224H200L184 192H72L56 224H8Z M96 144H160L128 80Z"/>
<!-- Speech bubble = circle + tail, merged -->
<path fill="#111" d="M128 24A104 104 0 1 1 61.6 208L28 236L37.9 180A104 104 0 0 1 128 24Z"/>
```

## 9. Never in a master file
`<text>` · `<image>`/embedded PNG · filters (blur, shadow, glow) · many masks/clipPaths · deep nested transforms
(apply them to coordinates; one wrapper translate/scale is fine) · 20+ colours or many gradients · micro-details
< 1/64 of size · near-miss angles · editor metadata and 6-decimal coordinates.

## 10. Validate
`logo_kit.py audit` after every significant iteration (score ≥ 90, no FAIL), then the test sheet and real renders.
