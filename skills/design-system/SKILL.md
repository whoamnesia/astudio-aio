---
name: design-system
description: >-
  astudio design system and design code: three-layer design tokens (primitive → semantic → component) in W3C DTCG
  2025.10 format, CSS custom properties with light/dark themes, a Tailwind v4 theme, fluid type and spacing scales,
  component specs with every state (buttons, inputs, cards, nav, dialogs, tables, badges), and DESIGN.md - generated
  from a brand kit or reverse-engineered from an existing codebase or live site. Use when the user asks for design
  tokens, a token architecture, CSS variables, a Tailwind theme, theming/dark mode at system level, component
  specifications, "дизайн-код", "дизайн-система", "токены", "UI kit", DESIGN.md, or wants hard-coded values replaced
  with tokens. Part of the astudio-aio pipeline (after brand, before the site build).
argument-hint: "[build from brand | extract from code | audit tokens] [path]"
---

# astudio · Design system

Role: Senior design-systems designer at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

The design code turns brand decisions into numbers every screen obeys. Rule: components reference **semantic** tokens
only; semantic tokens reference primitives; primitives hold raw values. Change the semantic layer and the whole
product re-themes.

Shared: `<root>` = two levels above this skill's base dir (`${CLAUDE_PLUGIN_ROOT}`). Tools: `palette.py`, `tokens.py`,
`search.py`, `render.cjs`, `lint.py` (`<root>/reference/tools.md`). Local references: `references/tokens.md`
(architecture, naming, DTCG format), `references/components.md` (specs and states), `references/extract.md` (from code
or URL), `references/design-md.md`.

## Modes
1. **Build from a brand kit** (pipeline): palette.json + faces + shape/motion decisions → tokens → component specs →
   DESIGN.md → a rendered specimen page.
2. **Extract from an existing project** (`references/extract.md`): trace the real tokens, themes, primitives and
   variants the product renders; normalise to the semantic schema; write DESIGN.md describing what governs the product
   (not every value that happens to exist).
3. **Audit / migrate**: find hard-coded colours, sizes, radii, shadows and durations (`lint.py`, grep), map them to
   tokens, propose a migration plan in order of reach, then replace.

## Build workflow
1. **Inputs**: `brand/palette.json` (from `palette.py system --json`), faces (verified, with Cyrillic if needed),
   radius logic, depth policy, motion tokens, density. Missing? Get them from `astudio-aio:brand` or decide with the
   direction contract.
2. **Spec**: `python3 <root>/scripts/tokens.py init > brand/brand.spec.json`; edit name, faces, type min/max sizes and
   ratios (≈1.2 dense UI, 1.25 product, 1.333+ expressive), spacing base (4), radius scale, shadows (what floats), motion.
3. **Build**: `python3 <root>/scripts/tokens.py build brand/brand.spec.json --out design-tokens` → DTCG
   `<brand>.tokens.json`, `tokens.css` (light + dark via `prefers-color-scheme` and `[data-theme]`), and a
   self-contained Tailwind v4 entry `tailwind-theme.css` (use it *instead of* tokens.css in Tailwind projects).
4. **Component layer**: define component tokens and specs for the components the product needs
   (`references/components.md`): variants, sizes, every state (default, hover, focus-visible, active, disabled,
   loading, error, selected), anatomy, spacing, accessibility notes. Add component tokens only where a component must
   be themable independently (`--button-radius: var(--radius-md)`), not for everything.
5. **Specimen page**: build `design-tokens/specimen.html` (or a Storybook/page in their stack) showing colour roles with
   contrast values, the type scale at real sizes, spacing, radii, elevation, motion tokens and every component state
   in light and dark. Render at 1440 and 390, look, fix. This proves the system.
6. **DESIGN.md** (`references/design-md.md`): the human-and-agent-readable design code: atmosphere, roles with hexes,
   type rules, components, layout, motion, imagery, voice, do/don't.
7. **Wire it**: import tokens in the project entry (Next: `app/globals.css`; Vite: `src/index.css`; static: `<link>`),
   map Tailwind/shadcn variables if used (`ui-styling` skill), and run `lint.py` + grep for raw hex in components.

## Rules
- Semantic names describe purpose (`--color-ink`, `--color-surface`, `--space-section`), not value (`--blue-600` in a
  component is a bug). Token names may evoke the product's world (`--ink`, `--parchment`) - someone reading only the
  tokens should guess what product this is.
- One spacing base (4px); one radius logic (concentric nesting); one shadow policy (border OR tone step OR shadow per
  layer); one set of motion curves.
- Dark theme is designed, not inverted: lighter surface steps for depth, adjusted chroma, every pair re-checked.
- Fluid type with `clamp()` and rem (zoomable); nothing below 12px; Operate screens use a tighter fixed UI scale.
- Every interactive component specifies focus-visible and disabled states; targets ≥ 24px (44px on touch).
- Document why, not only what: each rule in DESIGN.md has its reason so later work doesn't "fix" it away.
