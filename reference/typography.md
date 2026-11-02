# Typography

Type is most of what a visitor sees and most of what makes a page look designed or assembled.

## Contents
1. What strong sites measure
2. The scale: few sizes, far apart (fluid with clamp)
3. Setting display type
4. Setting text
5. Choosing faces (a procedure, not a menu)
6. Cyrillic and multilingual
7. Micro-typography - English and Russian
8. Loading fonts
9. Operate screens
10. Mistakes the eye catches and tools do not

## 1. What strong sites measure
From a study of ~200 award-gallery sites (1440 and 390 wide):
- Hero headline median 72px (5vw); top-scored sites ~6vw; largest type on top sites ~8.4vw vs 5vw on weak ones.
- Phone hero median ~40px (32-59).
- Headline ÷ body ≈ 4.3 (top sites 4.7). **Size contrast is the main lever; weight is not** - half of heroes are
  regular weight.
- Typefaces in use: one family 31%, two 45%, three 22%. Two is the practical limit.
- Centred heroes: 39% overall, 52% on weak sites. Left-align by default.

## 2. The scale
Two or three sizes do the visible work; five is the ceiling for a page (Operate screens: 4-9, median 6).
Pick steps that are clearly different. `tokens.py` emits a fluid modular scale; a hand-written equivalent:

```css
:root {
  --step-small:   clamp(0.8125rem, 0.79rem + 0.10vw, 0.875rem);  /* 13-14  captions, legal */
  --step-body:    clamp(1rem,      0.96rem + 0.20vw, 1.125rem);  /* 16-18  paragraphs */
  --step-lead:    clamp(1.25rem,   1.10rem + 0.70vw, 1.625rem);  /* 20-26  supporting line */
  --step-head:    clamp(2rem,      1.30rem + 3.20vw, 4rem);      /* 32-64  section headings */
  --step-display: clamp(3rem,      1rem + 9vw,       9rem);      /* set by the hero composition */
}
```
- Never `font-size: 2.5vw` alone - users cannot zoom it. Always mix a rem term (clamp/calc).
- Ratios: ~1.2 dense/calm UI, ~1.25 most product UI, ~1.333+ expressive pages. Display should be ≥ 4× body on desktop.
- If two sizes look almost the same, make them the same.

## 3. Setting display type (anything over ~40px)
```css
.display { font-size: var(--step-display); line-height: .95; letter-spacing: -.035em;
           text-wrap: balance; max-width: 14ch; margin: 0; font-kerning: normal; }
```
- Tracking tightens as size grows: -0.02 to -0.05em at display, 0 at body, +0.02-0.06em for short all-caps.
  Never below -0.05em. Set tracking per step, not once.
- Leading 0.85-1.05 for display (check descender/ascender collisions below 1.0); all-caps ~0.9.
- Optical alignment: round/diagonal first letters (O, C, A, T, W) look indented - pull left ~0.04-0.06em.
- Viewport-wide lines: size in vw from the character count (`font-size ≈ width ÷ (chars × k)`, k ≈ 0.40 condensed,
  0.50 most faces, 0.58 wide/caps); verify at 390 and 1440; `white-space: nowrap`.
- Never add text-shadow, outline strokes or gradient fills to display type.
- A display face drawn for large sizes must not set body text.

## 4. Setting text
```css
body { font-size: var(--step-body); line-height: 1.55; text-rendering: optimizeLegibility; }
p    { max-width: 65ch; text-wrap: pretty; margin: 0; }  p + p { margin-top: .9em; }
.lead { font-size: var(--step-lead); line-height: 1.35; max-width: 40ch; }
```
- Measure 45-75 characters (66 ideal); multi-column 40-50. Use `ch`/`rem`, never px for measure.
- Leading 1.45-1.6 body; 1.3-1.4 lead; serif body slightly looser than sans.
- Secondary text = same face in a softer ink that still passes 4.5:1 - not a lighter weight, not < 13px.
- Light text on dark looks heavier: drop one weight or add 0.01em tracking and a little leading.
- No centred paragraphs over 3 lines; never justify on the web (no hyphenation control).
- Space above a heading ≥ 2× space below it (headings belong to what follows).

## 5. Choosing faces
1. Name the audience's world (its publications, signage, notation, packaging) and the surface mode.
2. Shortlist three faces per role (display / text / optional mono for code and IDs). Describe each by shape:
   geometric (circular, modern, slightly playful), humanist (warm, readable), grotesque (neutral, efficient), serif
   (authoritative, editorial), slab (sturdy, mechanical), rounded (friendly), condensed (urgent, poster), mono
   (technical - only for real code/data).
3. Exclude the training-data defaults as the Persuade display voice (`anti-slop.md` Type table). They remain fine
   as Operate/Read body faces when chosen on purpose.
4. Verify each candidate: exact family name, required weights, **Cyrillic subset if Russian text appears**, licence
   (Google Fonts = OFL, free for commercial and logo use; Fontshare = ITF FFL, free incl. commercial), loading URL.
   Search the database: `search.py "<shape words>" -d google-fonts --cyrillic`. Never invent a face or URL.
5. Pair by **contrast in role, harmony in personality**: one display + one text, clearly distinct (serif display +
   grotesque text; condensed display + humanist text) or one superfamily for everything. Never two characterful
   display faces together; never a third face for labels.
6. If the user names a face, use it and state any trade-off once.

Faces worth knowing that are not on the default list (verify before use): Google Fonts with Cyrillic - Onest,
Unbounded, Golos Text, Manrope*, Commissioner, Montserrat Alternates, Raleway (avoid as display), Rubik, Literata,
Spectral, PT Serif / PT Sans / PT Mono, Alegreya, Yeseva One, Prata, Oranienbaum, Forum, Old Standard TT, Ruslan
Display, Russo One, Tektur, Jura, Comfortaa, Nunito, Exo 2, Fira Sans, Ubuntu, Arsenal, Brygada 1918, Cuprum,
Days One, Dela Gothic One, Climate Crisis, Bona Nova, Cormorant Garamond (default-refuse as display), EB Garamond.
Fontshare (Latin-focused): Satoshi, General Sans, Clash Grotesk, Cabinet Grotesk, Switzer, Erode, Gambetta, Zodiak.
(*Manrope is common - use with intent.) Short on purpose: a long list of "good fonts" is how convergence happens.

## 6. Cyrillic and multilingual
- Check every face for the `cyrillic` subset (`search.py ... --cyrillic`); a Latin-only display face falls back to
  a system font for Russian words and wrecks the design. Test real Russian copy, not lorem.
- Russian words are longer: budget ~15% more width per line and ~10% fewer characters in a two-line headline.
  Long compounds ("достопримечательности") need `hyphens: auto` with `lang="ru"` in body text, never in headlines.
- Cyrillic letterforms (Ж, Ш, Щ, Ы, Ю) are wide; condensed faces help headlines fit.
- `lang` attribute on `<html>` (and on foreign-language spans) for correct hyphenation, quotes and screen readers.
- Kazakh/Uzbek/Ukrainian need `cyrillic-ext` (Ә, Ғ, Қ, Ң, Ө, Ұ, Ү, Һ, І, Ї, Ґ) - check the subset list.

## 7. Micro-typography
**English:** curly quotes “ ” ‘ ’; apostrophe ’; ellipsis …; en dash for ranges 9–5; em dash sparingly;
non-breaking space between number and unit (`10&nbsp;MB`) and before a short last word of a headline;
`font-variant-numeric: tabular-nums` where numbers align (prices, tables, timers); oldstyle figures suit serif body;
`text-underline-offset: .18em; text-decoration-thickness: .07em` on links; no all-caps beyond ~3 words.

**Russian (always, silently):**
| Rule | Wrong | Right |
|---|---|---|
| Primary quotes guillemets, nested „лапки“ | "текст" | «текст», «„вложенные“» |
| Em dash with spaces, NBSP before it | слово - слово | слово&nbsp;— слово |
| En dash for ranges, no spaces | 10-15 дней | 10–15 дней |
| NBSP after one-letter words and short prepositions | в начале | в&nbsp;начале (в, к, с, о, у, и, а, я, на, по, за, от, до, из) |
| Single-character ellipsis | ... | … |
| Thousands with (thin) non-breaking spaces | 1000000 | 1&nbsp;000&nbsp;000 |
| Decimal comma | 3.14 | 3,14 |
| Ruble after number with NBSP | 1500₽ | 1&nbsp;500&nbsp;₽ |
| Abbreviations | т.д., т.е. | т.&nbsp;д., т.&nbsp;е. |
| Number sign | No. 5, #5 | №&nbsp;5 |
| Ordinals | 1ый | 1-й |
| Dates | 01.11.2026 in prose | 1&nbsp;ноября 2026&nbsp;г. |

In JSX, write the real UTF-8 characters (« » — … and U+00A0) - ` ` inside JSX text renders literally.

## 8. Loading fonts
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;600&family=Unbounded:wght@600&display=swap&subset=cyrillic" rel="stylesheet">
```
- Request only the weights used (2-3 total). `display=swap`; preload the one display font for the hero.
- Fallback stack of the same kind (sans for sans). Frameworks: `next/font/google` or self-hosted `@font-face`.
- After building, `render.cjs shots` reports which families actually rendered - if the face failed, every
  screenshot judgement is void; fix loading first.

## 9. Operate screens
One grotesk (a neo-grotesk or humanist UI face) carries the whole screen; a second face only with one job (mono for
IDs/figures). Page title 18-32px (median 24), card title 14-18, body/cells 13-16 (median 14), labels 11-14, nothing
under 11px. Tabular figures on every number in a table, KPI or live value - verify the face actually has them.
Weights: ~3 per screen; 700 does one job (money or the title). Sentence case; tracking 0 except slightly negative on
large type.

## 10. Mistakes the eye catches
- A headline that passes the 2-line rule but breaks badly (orphan word, split phrase) - author the break with
  `<br>` + `text-wrap: balance`, re-check on the phone.
- Display so tight letters touch, or so loose the word falls apart.
- A confident hero followed by section headings almost as large - keep one size dominant per screen.
- Everything bold. If every line is emphasised, none is.
- Weight change on hover (text reflows).
