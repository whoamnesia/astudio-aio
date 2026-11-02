# Colour

How to build a palette that looks decided rather than tinted, and stays accessible in light and dark.

## Contents
1. Roles before swatches
2. Proportion
3. Building the system with palette.py (OKLCH)
4. Brand-tinted neutrals, states and semantics
5. Surfaces without lines or shadows
6. Colour fields
7. Dark themes
8. Colour with photographs
9. Contrast rules
10. Colour psychology - a weak signal, used carefully

## 1. Roles before swatches
A palette is not a set of chips - it is roles. Every colour in the build references a role token; a raw hex in a
component is a second palette starting.

```
ground          most of the surface (page background)
surface         one tone step from ground: panels, fields, tiles
raised          cards/popovers that float (often white on light)
ink             main text and strongest marks
muted           secondary text - still ≥ 4.5:1 on ground AND surface
border          structural lines (≈1.2:1 on light)     control-border   form controls (≥ 3:1)
primary         the action colour (≥ 3:1 vs ground as a shape)   primary-text  primary used as text (≥ 4.5:1)
on-primary      text on primary (≥ 4.5:1)               primary-subtle   tinted backgrounds
accent / on-accent (optional second hue with one job)
success / warning / danger / info  (+ -subtle backgrounds + on-*-subtle text)
focus, selection
```
Name the humble roles too (the off-white behind cards, hairlines) - an unnamed role gets filled by a framework
default, which is how an off-brand grey ends up painting most pixels.

## 2. Proportion
- Ground 70-90% of a screen; ink for text and maybe one inverted section; accent **under ~5%** of any screen - the
  action plus at most one recurring detail. An accent in ten places means nothing.
- Classic 60/30/10 (dominant neutral / secondary tone / accent) is a fine default for Restrained work.
- The accent is not for headings, icons, bullets or borders unless the direction says so. Headlines are ink.
- Operate screens: ~3% coloured pixels median; colour goes on data, status and the one primary action, not chrome.
- Buttons can be neutral (black/white) - 52% of award sites use neutral buttons.

## 3. Building the system with palette.py
OKLCH keeps equal lightness steps looking equally light across hues, so ramps and dark themes balance without
hand-tuning.

```bash
python3 <root>/scripts/palette.py system --primary "#C2410C" --accent "#0F766E" --json palette.json --css palette.css
python3 <root>/scripts/palette.py ramp "#C2410C" --name brand      # 50..950 tonal ramp
python3 <root>/scripts/palette.py contrast "#736661" "#F8EEEA"     # check any pair
```
`system` builds light and dark role sets, nudging lightness until every text role reaches 4.5:1 and every UI role
3:1, and prints a contrast table - read it. Then feed `palette.json` to `tokens.py build` (design-system skill).
Keep the brand hue; adjust only lightness/chroma to pass. If the brand primary cannot pass as text, use it for
shapes/fills and a darker `primary-text` sibling for text links.

Hover/active: shift OKLCH lightness ~-0.06 (light theme) / +0.05 (dark). Never pick state colours independently.

## 4. Brand-tinted neutrals, states and semantics
- Greys tinted with the brand hue at very low chroma (0.005-0.02) feel intentional; pure #666/#eee feel generic.
- Avoid pure #000 on #fff for long text (halation) - near-black ink (~#111-#222) on off-white is calmer and still AAA.
- Semantic hues: success ~150°, warning ~75°, danger ~25°, info ~245°. Align their lightness/chroma so they carry
  equal visual weight; warning reads brighter - darken it a step. A muted brand gets slightly muted semantics.
- If the brand primary is orange/red, warning or danger must be visibly distinct (shift hue or use the -subtle pair).
- Status colour always ships with an icon or word - never colour alone.
- Disabled = neutral greys (not brand tints) and still legible (≥ 3:1 for the label is a good floor) with a reason.

## 5. Surfaces without lines or shadows (Persuade)
A surface is told apart from the ground by tone: 2-6 OKLCH lightness points is enough. Do not nest panels in
panels. If a panel does not read, add padding or space before adding a second tone. A thick bar (≥ 4px) can be a
deliberate graphic element; a decorative 1px hairline usually is not. (Operate screens may use 1px borders.)

## 6. Colour fields
Changing the whole ground per section is the strongest colour move: it replaces dividers, cards and background
decoration at once. Fields meet edge to edge with a hard line; nothing fades. Each field has its own ink (never
`muted` grey on a coloured field - use the field's ink at full or ~70% strength if it passes). Neighbouring fields
differ in lightness, not just hue. Order them like chapters: open strong, rest, surprise, close.

## 7. Dark themes
- `color-scheme: dark` on the root (form controls and scrollbars follow); `<meta name="theme-color">` per scheme.
- Ground is a deep tinted neutral (OKLCH L ~0.14-0.18), ink a soft light (~0.94), not #fff on #000 unless the
  direction is deliberately stark. No navy/slate by reflex - tint from the brand hue at low chroma.
- Depth from lighter surface steps (+0.04-0.05 L each), never glows. Saturated colours get lighter and slightly less
  chromatic in dark mode; recheck every pair - never assume light values carry over.
- Muted text is where dark themes fail: check it against the actual surface.
- Use one weight lighter than on light themes for body text.
- Provide both themes when the product is an app or tool; a marketing page may ship one ground chosen by the use
  scene.

## 8. Colour with photographs
When photographs carry the colour, the interface stays neutral and takes its ink from the darkest tone in the
imagery. Do not wash photos in brand colour - leave them, or apply one treatment to every image (all duotone, all
greyscale). Text over a photo needs a calm region or a neutral scrim (30-55% black/ink) over the text area only.
A flat field sampled from a photo (its sky, its shadow) ties a section to the image.

## 9. Contrast rules (WCAG 2.2)
| Element | Minimum |
|---|---|
| Body text, placeholders, secondary text | 4.5:1 (AAA 7:1) |
| Large text (≥ 24px, or ≥ 18.66px bold) | 3:1 |
| UI components, icons that carry meaning, focus indicators, input borders | 3:1 against adjacent colours |
| Data lines/bars vs background | 3:1; data labels 4.5:1 |
Text over images or gradients cannot be measured by tools - check the screenshot. Do not lower text opacity to
"soften" it without re-measuring. Hover and focus states increase contrast, never reduce it.

## 10. Colour psychology - a weak signal
Associations exist (blue trust/finance/health, green growth/eco, red energy/food/urgency, black luxury/authority,
purple creative/premium, orange friendly/energetic, yellow optimism/attention) but they are cultural, contested and
the reason every bank is blue. Use them to avoid miscues (red-dominant healthcare, appetite-suppressing blue for
food), not to choose the palette. The palette comes from the subject's own materials and world (direction.md):
the glaze of the café's cups, the paint of its street, the landscape outside the window. Database palettes
(`search.py "<product>" -d color`) are fallbacks when the subject gives nothing.
