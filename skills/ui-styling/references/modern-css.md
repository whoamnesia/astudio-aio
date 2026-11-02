# Modern CSS toolkit (baseline-available 2025-2026)

Prefer platform features over JS and libraries.

## Layout
- **Grid**: `grid-template-columns: repeat(12, minmax(0,1fr))`; `subgrid` to align card internals across a row;
  `grid-template-areas` for page shells; `auto-fit, minmax(min(100%, 18rem), 1fr)` for responsive card rows.
- **Container queries**: `.card-wrap { container-type: inline-size; }  @container (width > 32rem) { .card { … } }`;
  units `cqi`/`cqb` for type that scales with its container.
- **Logical properties**: `margin-inline`, `padding-block`, `inset-inline-start` (RTL-ready).
- **`:has()`**: parent/state styling without JS (`.field:has(input:invalid) label { … }`, `body:has(dialog[open])`).
- **Anchor positioning**: `anchor-name: --trigger; position-anchor: --trigger; top: anchor(bottom);
  position-try-fallbacks: flip-block;` for tooltips/menus that stay attached (progressive: provide a fallback).
- **Popover API**: `<div popover id="m">` + `<button popovertarget="m">` - top layer, light dismiss, no JS.
- **`<dialog>`** with `showModal()` for modals (focus trap and top layer built in); `::backdrop` for the scrim.
- **Viewport units**: `svh` (smallest - heroes), `dvh` (dynamic - app shells), `lvh`.

## Type
`clamp()` fluid sizes; `text-wrap: balance` (headings) and `pretty` (paragraphs); `font-optical-sizing: auto`;
variable font axes `font-variation-settings` / `font-stretch`; `hanging-punctuation: first` (Safari); `hyphens: auto`
with `lang`; `font-variant-numeric: tabular-nums`; `text-box: trim-both cap alphabetic` (trims leading for optical
alignment where supported); `initial-letter` for drop caps (progressive).

## Colour
`oklch()` and `color-mix(in oklch, var(--color-primary) 85%, black)` for states; relative colour syntax
`oklch(from var(--brand) calc(l + .1) c h)`; `light-dark(#fff, #111)` with `color-scheme: light dark`;
`accent-color` for checkboxes/radios/range; `scrollbar-color`.

## Motion
`@starting-style` for enter animations; `transition-behavior: allow-discrete` to animate `display`/`overlay` for
popovers and dialogs; scroll-driven animations `animation-timeline: view()` / `scroll()` inside `@supports`; View
Transitions (`document.startViewTransition`, cross-document `@view-transition { navigation: auto; }`);
`linear()` easing for spring-like curves; `prefers-reduced-motion` / `prefers-reduced-transparency` /
`prefers-contrast` media queries.

## Interaction
`(hover: hover) and (pointer: fine)` gates hover styles; `pointer: coarse` enlarges targets; `touch-action:
manipulation`; `overscroll-behavior: contain` on sheets; `scroll-snap-type` for carousels; `scroll-margin-top` for
anchored headings under sticky headers; `inert` on content behind a modal; `field-sizing: content` for auto-growing
textareas.

## Performance
`content-visibility: auto` + `contain-intrinsic-size` for long below-fold sections; `loading="lazy"`, `decoding="async"`,
`fetchpriority`; `font-display: swap`; avoid large `backdrop-filter` and animated `filter` on big surfaces.

## Browser surfaces (the cheap signal of craft)
```css
::selection { background: var(--color-selection); color: var(--color-ink); }
:root { caret-color: var(--color-primary); accent-color: var(--color-primary); scrollbar-color: var(--color-control-border) transparent; }
:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
a { text-underline-offset: .18em; text-decoration-thickness: .07em; }
```
