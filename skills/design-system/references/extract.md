# Extracting a design system from code or a live site

Record the design language that governs the product, not every value that exists. A rule enters DESIGN.md only with
evidence.

## Repository mode (source available - always preferred)
Trace in this order: existing DESIGN.md / design docs → tokens, themes, CSS variables, Tailwind config/`@theme`,
global styles → shared primitives and their variants (Button, Input, Card…) → representative routes and what they
render → local one-offs. A source counts only if the selected product imports, references or renders it (exclude
legacy, examples, other apps in a monorepo unless used). Resolve aliases to their definitions.
For each candidate record `role → value → source file → scope → recurrence → confidence`. Promote to a token/rule
only when it is a named shared token, a variant of a shared primitive, or the same treatment in ≥ 2-3 independent
places (then name it - two or three occurrences make a pattern). Repetition alone does not prove intent; local styling
does not become a system rule.

## URL mode (no source)
Needs a real browser: inspect DOM, computed styles and loaded stylesheets at desktop and mobile on up to three
representative pages (render.cjs or a browser tool). Promote a value when the computed value and a loaded declaration
or custom property agree, or the same computed value recurs for the same role across samples. Never derive exact
values from screenshots alone; never invent token names, component ownership or rationale; label the document
"reconstructed draft". If no rendered access, ask for screenshots or source - do not write DESIGN.md from HTML text.

## Normalise
Map raw values to the semantic roles (`tokens.md` §2). If two brand colours compete for primary, pick the one with the
highest use on interactive elements. Round type sizes to the nearest modular step only when the source is incoherent,
and say so. Base spacing unit = the most common small padding/margin. Button radius = the most common radius on
buttons/inputs. Check contrast of every text pair and propose fixes as findings (do not silently change brand values).

## Audit output (when asked to review a system)
```
CONTRAST     muted on surface 3.9:1 (need 4.5) → darken to #… (palette.py contrast)
HIERARCHY    3 primary buttons on /settings → 1 primary, 2 secondary
CONSISTENCY  button radius 4/8/12px across 3 components → --button-radius: 8px
DRIFT        14 hard-coded hex values in src/components (list) → map to tokens
STATES       inputs lack disabled + error specs; no focus-visible on cards
SCALE        11 distinct font sizes (12,13,14,15,16,18,20,22,24,28,32) → 7-step scale
```
Order recommendations by reach and correction cost; each finding has evidence (file:line or screenshot) and one fix.
