---
name: ui-ux
description: >-
  astudio UI/UX design intelligence for any interface task - designing, building, reviewing, auditing, critiquing,
  polishing or fixing pages, screens and components: hierarchy, layout, typography, colour, spacing, interaction,
  forms, navigation, states, accessibility (WCAG 2.2), responsive behaviour, motion and UX copy, backed by a searchable
  database (90 styles, 190+ product types with palettes and reasoning, 74 font pairings, 1900 Google Fonts with
  Cyrillic filter, 119 UX rules, landing patterns, chart guide, icons, GSAP presets, 22 stack guideline sets). Use when
  the user asks to improve or review a UI, "make it look better/premium/less generic/less AI", audit accessibility or
  UX, fix a layout, choose a style/palette/fonts for a product, "проверь интерфейс", "улучши UI", "сделай красивее",
  "аудит UX", or for any focused UI decision outside the full astudio-aio pipeline.
argument-hint: "[audit | critique | polish | bolder | quieter | fix | choose-style] [target]"
---

# astudio · UI/UX

Role: Senior UI/UX designer at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

Design intelligence for focused interface work. For a whole new site with logo and brand, use `astudio-aio`; for
dashboards `astudio-aio:dashboard`; for mobile/app `astudio-aio:mobile`.

Shared: `<root>` = two levels above this skill's base dir (`${CLAUDE_PLUGIN_ROOT}`). Read on demand:
`<root>/reference/direction.md`, `anti-slop.md`, `typography.md`, `color.md`, `layout.md`, `motion.md`, `copy.md`,
`accessibility.md`, `critique.md`, `tools.md`. Local: `references/ux-rules.md` (the full 10-category rule set),
`references/commands.md` (polish / bolder / quieter / distill / harden / typeset / colorize / layout / clarify / adapt
playbooks).

## Pick the job
| Request | Do |
|---|---|
| "Review / audit / what's wrong" | **Audit** (below) - findings only, no edits unless asked |
| "Make it better / premium / less generic" | Critique → fix the top issues (`references/commands.md` polish/bolder) |
| "Too busy / loud" | quieter / distill |
| "Bland / safe" | bolder / colorize / typeset |
| "Breaks on mobile / tablet" | adapt (+ `astudio-aio:mobile`) |
| "Errors, edge cases, empty states, i18n" | harden |
| "Copy, labels, errors read badly" | clarify (`reference/copy.md` §7) |
| "Which style / palette / fonts for X?" | Database + direction (below) |
| Build a component/page | Design decisions here, implementation via `astudio-aio:ui-styling` |

## Rule priorities (what to check first)
| # | Category | Impact | Must have | Avoid |
|---|---|---|---|---|
| 1 | Accessibility | CRITICAL | 4.5:1 text, alt, keyboard, labels, focus visible | removed focus rings, unlabeled icon buttons |
| 2 | Touch & interaction | CRITICAL | 24px+ targets (44 touch), feedback < 100ms, loading states | hover-only, instant state snaps |
| 3 | Performance | HIGH | sized/lazy images, CLS < 0.1, font loading | layout thrash, animating layout |
| 4 | Style fit | HIGH | style matches product and audience, one icon set | mixing styles, emoji icons, category-default looks |
| 5 | Layout & responsive | HIGH | mobile-first, no horizontal scroll, 1 focal point/screen | fixed widths, disabled zoom |
| 6 | Type & colour | MEDIUM | 16px body, 1.5 leading, semantic tokens | grey-on-grey, raw hex, 9 near sizes |
| 7 | Motion | MEDIUM | purposeful, 150-300ms UI, reduced motion | transition: all, bounce, uniform fades |
| 8 | Forms & feedback | MEDIUM | visible labels, inline errors, helper text | placeholder-as-label, errors only at top |
| 9 | Navigation | HIGH | predictable back, current location, deep links | overloaded nav, broken back |
| 10 | Charts & data | LOW | right chart type, legends, accessible colours | colour-only meaning |
Full rules with rationale: `references/ux-rules.md`; search one at a time: `search.py "error summary validation" -d ux`.

## Audit (findings, evidence, one fix each)
1. Render the target: `node <root>/scripts/render.cjs shots <url|file> --widths 1440,768,390` (and `--reduced-motion`);
   `python3 <root>/scripts/lint.py <src> --mode persuade|operate`. If the target is code you cannot run, read it and say
   which checks could not run.
2. Classify surface mode (direction.md §1). Run the 14 passes on the screenshots (`reference/critique.md` §2).
3. Score: technical audit 0-4 × 5 dimensions (/20) + design score (D/U/C/Ct with caps) + Nielsen heuristics if UX-heavy.
4. Report:
```
Design-specificity verdict: authored for this product, or category-interchangeable? (evidence)
Scores: audit __/20 (a11y _, perf _, theming _, responsive _, integrity _) · design _ · usability _ · creativity _ · content _
What works (2-3, specific)
Priority issues (3-5): [P0-P3] problem — evidence (screenshot/file:line) — why it matters — fix
Systemic patterns (e.g. hard-coded colours in 15 components)
Three changes that would move it most
```
Every finding needs evidence and exactly one correction; delete findings you cannot prove. Then offer to apply fixes.

## Choosing style, palette, fonts for a product
1. Brief → 2-5 English keywords → `python3 <root>/scripts/search.py "<product industry mood>" --design-system -p "<Name>"
   [--cyrillic]` (product match, style candidates, palette roles, font pairings with Cyrillic flags, page pattern,
   anti-patterns). Supplement: `-d style`, `-d color`, `-d typography`, `-d google-fonts --cyrillic`, `-d landing`,
   `-d chart`, `-d icons`, `-d motion`, `--stack <stack>`.
2. Treat results as candidates. Run the subject inventory and calibration check (direction.md) - database fonts and
   palettes are frequently the category defaults; override with the subject's own world for Persuade surfaces.
3. Build the palette with `palette.py system` (contrast auto-fit) and verify faces (licence, weights, Cyrillic).

## Fixing (when asked to apply)
Keep the stack, content and what works. Order: type (faces and scale) → colour (ground/ink/accent proportions) → frame
(margins, rhythm, titles, headings) → states (hover, focus, loading, empty, error) → replace stock components (icon
cards, pill badges, gradient blobs, card grids) with compositions from the content → motion last. Render before and
after; report measurements side by side. Refinement preserves identity; if the concept itself is wrong, say so and
recommend a redesign instead of smuggling one in.
