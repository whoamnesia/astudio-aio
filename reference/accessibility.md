# Accessibility floor (WCAG 2.2 AA)

Accessibility is a fixed boundary, not a style. Build to this floor silently on every surface; do not announce it.

## Perceivable
- Text contrast 4.5:1 (large 3:1); meaningful icons, control borders, focus indicators and chart marks 3:1.
- Never colour alone for meaning - add an icon, text, pattern or position.
- `alt` on every image: describe meaningful images; `alt=""` for decorative ones; icons beside visible text get
  `aria-hidden="true"`; icon-only controls get an accessible name.
- Captions/transcripts for meaningful video/audio; decorative media hidden from assistive tech; no autoplay with sound.
- Text resizes to 200% without loss; layouts reflow at 320 CSS px width without horizontal scroll (except data tables
  and maps in their own frame).
- `lang` on `<html>`; semantic headings in order (one h1, no skipped levels); landmarks (header, nav, main, footer).

## Operable
- Everything works with the keyboard alone in visual order; no keyboard traps; Escape closes overlays.
- Visible `:focus-visible` style on every interactive element (2px outline + offset, ≥ 3:1); never `outline: none`
  without a replacement. Sticky headers, cookie bars and overlays must not hide the focused element.
- Skip link to main content.
- Pointer targets ≥ 24×24 CSS px (or spaced so a 24px circle around each does not overlap another); touch UI 44×44pt
  (iOS) / 48×48dp (Android).
- Every drag, swipe or multi-point gesture has a single-pointer and keyboard alternative.
- Moving/auto-updating content > 5s has pause/stop; carousels stop on focus and under reduced motion; nothing flashes
  > 3 times per second.
- Respect `prefers-reduced-motion` (motion.md §7).
- Do not block paste; allow password managers (`autocomplete` attributes); no cognitive puzzles as the only login.

## Understandable
- Visible labels for every input (placeholder is not a label); helper text linked with `aria-describedby`; required
  fields marked in text, not only colour.
- Errors next to the field, in words, with the fix; `aria-invalid="true"`; after a failed submit, focus the error
  summary (or first invalid field) and keep inline errors.
- Consistent navigation and consistent help placement across pages; don't make users re-enter information within one
  process.
- Predictable: no context change on focus or input alone; links look like links; buttons are `<button>`, navigation is
  `<a href>`.

## Robust
- Native elements before ARIA (`<button>`, `<a>`, `<label>`, `<dialog>`, `<details>`, `<table>`). If a role is used,
  its required states are present (`aria-expanded`, `aria-controls`, `aria-selected`, `aria-pressed`).
- Live updates (toasts, validation, async counts) announced with a polite live region as a complete phrase, without
  moving focus; toasts are never the only place critical information appears.
- Dialogs trap focus while open, set initial focus inside, restore focus to the trigger on close; use established
  primitives (Radix, React Aria, Base UI, native `<dialog>`) for complex widgets rather than hand-rolled behaviour.
- Data tables use `<th>` with scope; sortable columns expose `aria-sort`; charts have a text summary and a table
  alternative.

## Quick test before delivery
Tab through the whole page; zoom to 200%; view at 390px; turn on reduced motion; check dark mode contrast separately;
run `render.cjs shots` (contrast, alt, unlabeled controls, target size) and `lint.py`.
