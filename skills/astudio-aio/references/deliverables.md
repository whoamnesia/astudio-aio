# Deliverables and final report

## Folder layout (in the user's project)
```
brand/
  logo/            <name>-symbol.svg, <name>-horizontal.svg, <name>-stacked.svg, -black/-white/-mono variants,
                   <name>-small.svg (16-32px cut), web/ (favicon.ico, PNG icons, site.webmanifest, head-snippet.html)
  logo-concepts/   the three concepts + concepts sheet (kept for the record)
  palette.json     light/dark role sets + ramps (palette.py)
  brand.spec.json  input to tokens.py
  brand-book.html  the brand kit page (logo usage, palette, type, voice, imagery, components, applications)
  DESIGN.md        the design code (also copied to the project root if the project has none)
design-tokens/
  <name>.tokens.json   W3C DTCG 2025.10
  tokens.css           CSS custom properties, light + dark
  tailwind-theme.css   Tailwind v4 entry (only if the project uses Tailwind)
site/ (or the project's own src/app/pages)
  index.html, styles.css, main.js, assets/…   (static default)
.astudio/
  shots/            screenshots + report.json from render.cjs (can be gitignored)
  critique.md       the rounds of critique (optional)
```

## DESIGN.md skeleton (the design code)
```markdown
# Design code: <Brand>
## 1. Atmosphere            mood, density, the idea in one sentence, surface mode
## 2. Colour roles          descriptive name (#HEX) - role - where used; light and dark tables; contrast notes
## 3. Typography            faces + roles + source/licence + Cyrillic support; scale (min-max px); tracking/leading rules
## 4. Shape & depth         radius logic, borders vs tone steps, shadows (what floats), concentric nesting
## 5. Layout                grid, margins, anchor lines, section rhythm, breakpoints, max widths
## 6. Components            buttons (variants/sizes/states), inputs, cards/panels, nav, badges, dialogs - specs + do/don't
## 7. Motion                tokens, the signature move, entrances, feedback, reduced-motion behaviour
## 8. Imagery & icons       photo direction, treatments, icon set + stroke, illustration rules
## 9. Voice                 3 traits (we are / we are not), CTA vocabulary, error/empty tone, RU/EN rules
## 10. Do / Don't           the 8-12 rules that keep the brand from drifting (including the anti-slop items it bans)
```
Write it from the built result, not before building (a rulebook written before the build gets defended against reality).

## Final report (keep it short; the files are the deliverable)
```
## What I made
- Logo: <type, idea in one sentence> → brand/logo/
- Brand kit + design code: palette (<strategy>), <display>/<text> faces, tokens → brand/, design-tokens/, DESIGN.md
- Site: <pages> in <stack> → <path>. Preview: open site/index.html (or `npx serve site`)
## The idea
On this site, <X> becomes <Y>. Signature: <live thing / move>.
## Quality
Final critique: design _ · usability _ · creativity _ · content _ → _ (round n). Still short: <honest list>.
Checks run: render 1440/768/390 (FAIL 0), reduced-motion render, lint (FAIL 0), contrast table. Not run: <…, why>.
## Replace before launch
Sample content: <list>. Images standing in for client photos: <list>. Wiring needed: <forms, links>.
## Credits
<title — creator — licence — source — where credited>
## Next
Banners / ad creatives from this brand · slides · dashboard · mobile app screens.
```
Do not claim checks you did not run. Do not round scores up.
