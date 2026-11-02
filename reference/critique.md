# Look, critique, fix

Passing a linter means nothing banned was measured; it does not mean the work is good. Judge the render, never the
code - you wrote the code and will read your intentions into it.

## Contents
1. The loop
2. Fourteen passes on the screenshots
3. Score (Awwwards-weighted) and caps
4. Writing the critique
5. Fix order
6. Technical audit (0-4 × 5 dimensions)
7. Heuristic review (Nielsen, Laws of UX)
8. Reviewing an existing product (audit mode)
9. Fresh-eyes review with a subagent

## 1. The loop
1. `node <root>/scripts/render.cjs shots <page> --widths 1440,768,390` (add `--reduced-motion` once).
2. `python3 <root>/scripts/lint.py <src> --mode persuade|operate`.
3. Open every screenshot (Read the PNGs). Run the passes below. Write the critique (section 4).
4. Fix the top three problems in fix order. Re-render. Max three rounds; stop early when a stranger would notice
   nothing. If you cannot render (no browser), say so and critique the code carefully - never claim checks you did
   not run.

## 2. Fourteen passes (each on its own)
1. **One second, then five.** What did you see? Exactly one answer. In five seconds can a stranger say what this is,
   for whom, and what to do?
2. **Squint.** Two or three masses with clear size differences, or many medium ones?
3. **Cover the logo.** Could this be a competitor's page or another industry's? Does the idea reach pricing, FAQ and
   footer?
4. **Edges.** Count distinct left x-positions of text blocks - 2-3 composed, 6 = placed one at a time.
5. **Space and frame.** Related close, unrelated far; section gaps > inner gaps; holes vs rests; equal margins; no
   half-empty sections; no blank stretch > half a screen.
6. **Type.** Display ≥ 3-4× body; ≤ 5 sizes; no orphan words; measure ≤ 75ch; no long centred paragraphs.
7. **Colour.** Name the proportions; accent on the action and ≤ 1 other thing.
8. **Images.** Real pictures doing jobs (show the thing, set the place, prove the claim)? Shared crops and grade? Any
   grey box, stretched photo or fake screen?
9. **Sameness.** One word per section layout - repeats in a row?
10. **Phone.** Its own composition with its own crops and breaks? First screen still one clear thing?
11. **Fullness.** Each desktop screen a composed poster, or a narrow grey column with dead ground?
12. **Substance.** Every section the brief asked for complete and readable? Primary action a real button on screen one?
13. **Collisions.** Anything over a headline or button at any scroll position? Anything off the phone edge?
14. **Competitor and live thing.** Does the idea survive the competitor test? Name the live thing/signature element.
15. **Wow.** Would a jury screenshot the first screen? Dominant visual ≥ half the viewport, layered depth, a headline
    with presence, an entrance moment, no empty band (`studio-bar.md` §4).
16. **Subject in three seconds.** Blur the copy: is the industry obvious from pictures, graphics and icons alone?
17. **Richness.** List each section with its visual anchor (photo / illustration / icons / UI / map / 3D). Any section
    with none? Is the icon set present? Does the graphic language appear beyond the hero? Are product/menu/pricing
    components designed and aligned at 1440 and 390?
Operate screens replace 8, 11, 14, 15 and 16 with: is the screen's one question answered by its biggest block; do numbers add
up and align; is colour only on data/status/the primary action; is the main job one click away; do all states exist.

## 3. Score and caps
Four criteria 1-10: **design 40%** (composition, type, colour, imagery, craft), **usability 30%** (orientation in 3s,
readable, obvious actions, honest mobile), **creativity 20%** (an idea stated in one sentence, carried through),
**content 10%** (specific, true, edited). `overall = .4D + .3U + .2C + .1Ct`. Real award sites land 7.5-8.0; if your
first score is 9, re-score as a juror who did not build it.
Caps (override arithmetic): any render/lint FAIL → overall ≤ 6.0. Three-line headline, eyebrow labels, mono labels,
01/02/03 numbering, decorative gradient, resting shadow or ornamental hairline visible → ≤ 6.5. Fails the
cover-the-logo pass → creativity ≤ 6. Idea passes for the competitor → creativity ≤ 7. Placeholder content →
content ≤ 5. Missing requested section → content ≤ 6. No real primary button on the first screen → usability ≤ 7.
No clear title in five seconds → usability ≤ 6. Unequal margins / half-empty section / blank stretch → design ≤ 6.5.
Anything covering a headline → usability ≤ 6. Blank band where a reveal failed → usability ≤ 5.
No dominant visual on the first screen, or an empty band in it → design ≤ 6 and creativity ≤ 6. Industry not
recognisable in three seconds without copy → creativity ≤ 5. A Persuade section without a visual anchor → design
≤ 6.5 (each further one −0.5). Misaligned or wrapping prices in a menu/pricing component → design ≤ 6.5. Any
AI-generated image → overall ≤ 5.

## 4. Writing the critique
```
ROUND n
Seen in one second: …
Idea (one sentence): …
Live thing / signature element: …
Layout words by section: hero=… / …
Scores: design _ · usability _ · creativity _ · content _ → overall _._   Caps: …
Top three problems (most visible first) - screenshot, problem, fix:
1. …
```
Name problems like a designer to a colleague: "the supporting paragraph starts 40px left of the headline's edge", not
"could be more polished".

## 5. Fix order (later items cannot rescue earlier ones)
1 idea → 2 hierarchy (one dominant element per screen) → 3 composition (edges, spacing, section variety, holes) →
4 typography → 5 imagery → 6 colour proportion → 7 detail (states, focus, alignments, phone) → 8 motion.
When removing something leaves a gap, close the gap with content: a real picture, an illustration from the brand's
graphic language, an icon set, enlarged type with an image - never a random ornament, and never leave it empty.

## 6. Technical audit (0-4 each, /20)
| Dimension | 0 | 4 |
|---|---|---|
| Accessibility | fails WCAG A | AA fully met |
| Performance | layout thrash, unoptimised everything | lean: images sized/lazy, fonts subset, transform-only motion, CLS < 0.1, LCP < 2.5s |
| Theming | hard-coded values everywhere | full semantic tokens, both themes correct |
| Responsive | desktop only | fluid at all widths, 44px touch targets, gestures work under touch |
| Implementation integrity | systemic drift, stock template | coherent product-specific system |
Bands: 18-20 excellent, 14-17 good, 10-13 acceptable, 6-9 poor, 0-5 critical. Tag each issue **P0** blocking (task
cannot be completed, data loss, inaccessible path), **P1** major (WCAG AA violation, significant difficulty), **P2**
minor, **P3** polish. Keep P3s few.

## 7. Heuristic review
Nielsen's 10, scored 0-4 (most real interfaces 20-32/40; mark n/a with a reason and renormalise): visibility of system
status; match with the real world; user control and freedom; consistency and standards; error prevention; recognition
over recall; flexibility and efficiency; aesthetic and minimalist design; error recognition and recovery; help.
Useful laws while reviewing: Fitts (big, close targets for frequent actions), Hick (fewer choices per decision),
Jakob (people expect your site to work like others), Miller/working memory (chunk, don't make users remember),
Doherty (respond < 400ms), Tesler (complexity moves, it doesn't vanish - absorb it in the system), Peak-End (design
the best moment and the ending), Von Restorff (the one different thing is remembered - make it the action),
Serial position (first and last items remembered), Zeigarnik (show progress on unfinished tasks), Goal-gradient
(motivation rises near the goal - show it), Aesthetic-usability effect (beauty buys patience, not a pass on
function), Proximity/Similarity/Common region/Prägnanz (gestalt grouping).
Trunk test for every page: where am I, what's here, what can I do, how do I get back?

## 8. Reviewing an existing product
Record the before (render + lint into `.astudio/before`), read the code (framework, styling method, components, what
must survive: routes, forms, data, brand assets). A review stops at findings: design-specificity verdict, scores,
3-5 priority issues (P0-P3, why it matters, concrete fix), what works, and the three changes that would move the page
most. Every finding needs evidence (screenshot or file:line) and one correction; delete findings you cannot prove.
For a restyle/redesign keep the stack and content, change type → colour → frame → states → stock components, then
render the after and report before/after side by side.

## 9. Fresh-eyes review
When subagents are available, the final review is done by a fresh agent with no build history: give it the brief,
the direction contract, the screenshot paths and this file, and ask for the section 4 write-up and P0-P3 list. A
reviewer that inherits your transcript inherits your optimism. Without subagents, step out of the build context and
run the passes as a stranger.
