---
name: brand
description: >-
  astudio brand kit and brand identity: positioning, messaging, voice and tone, visual identity (logo usage,
  colour system, typography, imagery, iconography, shape language), the design code handoff and a rendered HTML
  brand book. Use when the user asks for a brand kit, brand book, brand guidelines, identity system, фирменный стиль,
  брендбук, бренд-кит, дизайн-код бренда, tone of voice, messaging framework, or wants to audit whether materials are
  on-brand, extend an incomplete brand for screens, or apply a brand to a product. Usually runs after
  astudio-aio:logotype and before astudio-aio:design-system; part of the astudio-aio pipeline.
argument-hint: "[create | extend | audit | apply] [brand name]"
---

# astudio · Brand

Role: Senior brand designer and strategist at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

A brand kit is not decoration; it is the visual and verbal argument for why the brand exists, specified tightly
enough that anyone (or any agent) can produce on-brand work without asking. Output: strategy one-pager, voice guide,
colour and type systems with numbers, imagery and icon rules, logo usage, a rendered **brand book page**, and the
inputs the design-system skill turns into tokens.

Shared: `<root>` = two levels above this skill's base dir (`${CLAUDE_PLUGIN_ROOT}`). Read `<root>/reference/
direction.md` (world, colour strategy, calibration), `color.md`, `typography.md`, `copy.md`, `imagery.md`. Tools:
`palette.py`, `search.py`, `tokens.py`, `render.cjs`. Local references: `references/strategy-voice.md`,
`references/visual-identity.md`, `references/brand-book.md`.

## Modes
- **Create** (new brand): strategy → world → visual identity → voice → brand book. Needs a logo (run
  `astudio-aio:logotype` first, or design the identity around a provisional wordmark and flag it).
- **Extend** (brand exists but is incomplete for screens - e.g. print-only guide, one font weight, no dark mode): keep
  every confirmed asset; add what screens need (UI text face, semantic roles, dark palette, states, motion). Treat print
  values that fail on screen (pale grey text, unlicensable webfont) as findings: propose the screen-safe sibling and say
  why. Read the existing product's deviations as evidence, not errors (`references/visual-identity.md` §7).
- **Audit**: check materials/pages against the brand: palette compliance, type, logo usage, voice, contrast. Report
  findings with evidence and one fix each.
- **Apply**: produce on-brand assets/pages using the kit (route to banner-design, slides, ui-styling as needed).

## Create workflow
1. **Strategy one-pager** (`references/strategy-voice.md` §1): mission, audience and their situation, positioning
   statement, the one promise, proof points (real only), personality (3 traits as "we are / we are not"), what the
   brand must never look or sound like.
2. **World and direction** (`reference/direction.md`): subject inventory, candidate worlds, colour strategy,
   ground from the use scene, shape language matching the logo, decoration and motion levels. Write the direction
   contract. Present 2-3 directions when the brand is new and the user is available.
3. **Colour system**: pick 1 primary (+ optional accent) from the subject's world, then
   `python3 <root>/scripts/palette.py system --primary "#…" [--accent "#…"] --json brand/palette.json --css brand/palette.css`.
   Read the contrast table; keep the hue, adjust lightness only. Add brand-specific fields (e.g. section field colours
   with their inks) if the strategy is Committed/Drenched. Proportion rule written down (ground/ink/accent shares).
4. **Typography**: procedure in `reference/typography.md` §5 - verify family, weights, licence, **Cyrillic** if needed
   (`search.py "<shape words>" -d google-fonts --cyrillic`). Roles: display, text, optional mono; the scale min/max;
   tracking/leading rules; Russian typography rules if the brand writes in Russian.
5. **Shape, depth, icons, imagery** (`references/visual-identity.md`): radius logic from the logo's geometry, borders
   vs tone steps, which things float (shadow), one icon library + stroke, photo direction and treatment, illustration
   rules, pattern/graphic device derived from the mark.
6. **Voice and messaging** (`references/strategy-voice.md` §2-4): voice chart, tone by context (marketing, product UI,
   errors, success, support), vocabulary (CTA verbs, words we never use), sample rewrites before/after - in the brand's
   language(s).
7. **Brand spec for tokens**: write `brand/brand.spec.json` (`tokens.py init` for the template; `colors_from:
   "palette.json"`) and hand off to `astudio-aio:design-system` (or run `tokens.py build` directly).
8. **Brand book page** (`references/brand-book.md`): build `brand/brand-book.html` with the brand's own tokens and
   faces, render it (`render.cjs shots brand/brand-book.html`), look, fix, and show it. This page is both the
   deliverable and the proof the system works.
9. **DESIGN.md**: write or update the project's design code (skeleton in
   `<root>/skills/astudio-aio/references/deliverables.md`).

## Rules
- Real assets only: never invent logos, customers, testimonials or awards for the brand book.
- Every colour has a role and a contrast value; every face has a licence and a source; every rule has a reason.
- Brand-tinted neutrals, not pure greys; status colours distinct from the brand primary.
- The brand book must pass the same anti-slop review as any page (`reference/anti-slop.md`) - no eyebrow labels,
  no generic card grid of swatches with drop shadows; let the brand's own world structure the page.
- When the guide's medium (print) differs from the work's (screen), the guide is evidence, not law: propose screen
  fixes and document them as findings for the brand owner.
