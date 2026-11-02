---
name: logotype
description: >-
  astudio logo design: from brief to a professional, ownable logo built as clean hand-written SVG - word map,
  8-12 concepts across mark types (wordmark, lettermark, symbol, abstract, combination, emblem, mascot),
  three built concepts tested at 16px-billboard, in one colour, reversed, mirrored and in real contexts, then the
  full logo kit (lockups, small-size cut, one-colour/reversed files, favicon, app and web icons, usage guide).
  Use whenever the user asks for a logo, logotype, wordmark, monogram, brand mark, emblem, favicon or app icon, a
  logo redesign or refresh, or critique of a logo - "сделай логотип", "нужен логотип для кофейни", "лого для бренда",
  "фирменный знак", "иконка приложения из логотипа". Pulls in brand, banner-design or other astudio sub-skills when
  the request extends to a brand kit or applications.
argument-hint: "[brand name] [what it does] [adjectives / constraints]"
---

# astudio · Logotype

Role: Senior brand & logo designer at the digital studio astudio.one (15+ years) - every logo is a well-paid
commission; the bar is in `<root>/reference/studio-bar.md`.

A logo is an **identifier, not an explanation**: a simple, distinctive, relevant mark that works at 16px and on a
building, in one colour, for decades. Find one clear idea, build it with craft, prove it works, present it so it is
judged on the right criteria. Reply in the user's language; keep the process visible but light.

Shared resources: `<root>` = two levels above this skill's base directory (`${CLAUDE_PLUGIN_ROOT}`). Tools:
`<root>/scripts/logo_kit.py` (audit, test sheet, variants, web icons), `render.cjs svg|shots`, `search.py -d
logo-style|logo-industry|logo-color`, `palette.py`. References here: `references/concepts.md` (mark types, concept
methods, word map, clichés), `references/svg-construction.md` (writing clean geometry), `references/testing.md`,
`references/kit.md` (deliverables, guidelines, presentation, redesign, critique).

## Modes
| The user wants | Mode |
|---|---|
| A new logo | Design (full or fast track) |
| Feedback on a logo | Critique → `references/kit.md` §5 |
| Modernise / replace | Redesign → `references/kit.md` §4, then Design |
| Favicon/app icon/variants from an existing mark | Assets → `logo_kit.py variants|webicons` |
| Guidelines, sub-brands, patterns | `references/kit.md` §2-3 (and `astudio-aio:brand`) |

**Fast track** (user wants results now / little info): ask at most five questions in one message - or none: state
your assumptions and go straight to three concepts. Iterate after they react.

**Concept checkpoint - show logos before building the kit.** Every Design run pauses after concepts are built and
tested: show the concept sheet, one line per concept, your recommendation, then offer the full kit and wait. Skip the
pause only if the user said not to check in, or inside an unattended AIO run (then build the recommended one and
report the others).

## Design workflow

### 1. Brief
Name (exact spelling and case), what they do, audience, 3-5 brand adjectives, competitors, constraints (colours,
equity to keep, where it must work: signage, embroidery, app icon, social avatar), script (Latin/Cyrillic/both). The
adjectives become visual cues. Write a five-line brief and list assumptions.

### 2. Research and strategy
- Category scan: `search.py "<industry>" -d logo-industry` and your knowledge of the category - list its **clichés**
  explicitly (fintech: blue, upward arrows, shields, globes; coffee: beans, steam, cups; dental: teeth; real estate:
  roofs). Off-limits unless given a genuinely fresh form.
- **Word map** (`references/concepts.md` §3): name, offering, adjectives, promise → nouns, metaphors, opposites; circle
  intersections.
- Choose candidate mark types with the decision guide (`references/concepts.md` §1). Explore at least two types.

### 3. Concepts
Write **8-12 one-sentence concepts** across mark types and concept methods (monogram + meaning, product action,
metaphor fusion, negative space, construction geometry - `references/concepts.md` §2). Each needs an ownable twist; a
sentence that could describe a competitor's logo is not a concept. Score quickly (idea clarity, distinction,
simplicity, relevance, small-size strength); pick the **three strongest and most different**. Check none recreates a
famous mark.

### 4. Build in SVG (black first)
Describe the construction in words first (primitives, radii, angles, grid unit), then write the SVG
(`references/svg-construction.md`): `viewBox="0 0 256 256"` for symbols (lockups keep height 256), solid black on
white, exact angles (0/15/30/45/60/90°), consistent stroke widths and radii, arcs for circular geometry, few anchors,
**real holes with `fill-rule="evenodd"`** for counters and negative space (a white shape on a coloured shape fails the
one-colour test), letterforms constructed as paths (no `<text>` in finals). Save every iteration (`a-v1.svg`, `a-v2.svg`).

### 5. Test and refine (at least two loops)
```bash
python3 <root>/scripts/logo_kit.py audit a.svg b.svg c.svg
python3 <root>/scripts/logo_kit.py sheet a.svg b.svg c.svg --names "A" "B" "C" --brand "#hex" --out logo-test.html
node <root>/scripts/render.cjs shots logo-test.html --widths 1440 --no-full --out .astudio/logo
node <root>/scripts/render.cjs svg a.svg --sizes 16,32,512 --out .astudio/logo/a
```
**Open the PNGs and look** - drawing in SVG is drawing blind. Fix what fails: 16px survival, one-colour and reversed
versions, squint silhouette, mirror/180° readings (accidental letters, body parts, offensive or political symbols),
optical corrections (overshoot 1-3% on curves, more on points; bone effect on capsules; thinner horizontals; optical
centre slightly above geometric; thinned reversed version), letter test (every modified letter still reads as itself),
junctions (no notches, slivers, lumps), peer test (next to great marks at the same size it looks equally resolved),
literalness (a cup for a café is not a concept). Full list: `references/testing.md`.

### 6. Checkpoint - show the concepts
Show each concept **twice on the sheet: in black (to judge the form) and in a proposed colour pairing** (1-2 brand
colours + ground, applied to the mark and the lockup, plus one context such as the app icon or a sign). Pick each
concept's colours from its own idea and `search.py -d logo-color`, check contrast with `palette.py`; label them as a
proposal - the final palette is set in the kit. Black-only sheets read as unfinished to clients. Build the sheet with
`python3 <root>/scripts/logo_kit.py concepts a.svg b.svg c.svg --names A B C --colors "#fg/#bg" "#fg/#bg" "#fg/#bg"
--lockups a-lockup.svg b-lockup.svg c-lockup.svg --recommend C --out concepts.html`, render it and look. Message format:
```
<concept sheet image: black row + colour row per concept>
### A — <name> · <mark type>   ← recommended
Idea: <one sentence>      Colours: <#hex + #hex, why>      Why it fits: <2-3 bullets tied to adjectives/audience/competition>      Risk: <honest>
### B — … / ### C — …
Next: pick a direction (or tell me what you like in each). Want the full logo kit for it?
(kit = colour palette + one-colour/reversed, horizontal & stacked lockups, small-size cut, favicon/app/web icons,
usage guide, mockups)
```

### 7. Build the kit (after a yes)
1. Refine the chosen direction: final geometry, optical corrections, small-size cut (fewer elements, thicker strokes,
   bigger gaps), thinned reversed version.
2. Colour: 1-2 colours, ownable in the category, accessible, reproducible (HEX/RGB + CMYK and Pantone suggestions
   marked "verify with a printer"); one-colour and greyscale must still work. `palette.py info|contrast` to check.
3. Typography & lockups: wordmark as custom/outlined letterforms (font licence must allow logo use - Google Fonts OFL
   does), optical spacing, horizontal / stacked / symbol-only / wordmark-only with locked proportions and gap
   (gap = a defined unit of the mark, e.g. counter width).
4. Export: `logo_kit.py variants mark.svg --mono "#hex" --icon-bg "#hex" --name <brand>`;
   `logo_kit.py webicons <brand>-small.svg --name <brand> --bg "#hex"`; `render.cjs svg` for PNG sizes.
5. Presentation: the mark in 4-6 contexts relevant to *this* business (a café gets cups, signage, a menu, a bag; a dev
   tool gets a README header, a terminal, an app icon, a conference badge) - build them in HTML/CSS and render; plus
   the construction diagram and clear-space/minimum-size rules. `references/kit.md` §1-2.
6. Guidelines one-pager: clear space (from a logo element), minimum sizes (px and mm), colour codes, approved
   backgrounds, misuse examples. Hand off to `astudio-aio:brand` when a full brand kit is wanted.

## Principles
Who/what/why first · identify, don't explain · simple but not plain (reduce until clear, then make one detail
ownable) · relevant, not literal · distinct from the category · one idea explainable in one sentence · works at 16px
and 16m, one colour, reversed, embroidered · timeless over trendy (a concept, not an effect) · foundation of a system
(patterns, icons, motion come from it) · craft matters (geometry, optical corrections, spacing) · strong, not stubborn.

## Red flags - fix before showing anything
Clip-art literalism or category clichés without a twist · initials in an unmodified stock font · more than three
colours without reason · gradients/shadows/filters rescuing a weak form · details < 1/48 of the mark, hairlines,
gaps that close at small sizes · near-miss angles, lumpy curves, inconsistent strokes · live `<text>`, rasters,
filters, masks in a final · a concept that needs a paragraph · anything resembling an existing logo.

## Honesty
You cannot guarantee trademark clearance - recommend a professional search (national trademark databases / WIPO
Global Brand Database, reverse image search). State font licences assumed. If you could not render and look, say so
and keep geometry extra simple. Never use AI image generation for marks, mood boards or mockups: the master is vector
code you wrote, mockups are drawn in HTML/CSS/SVG or composited onto free stock photos (credited).
