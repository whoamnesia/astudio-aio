# Component specs and states

Specify only components the product uses. Each spec: purpose, anatomy, variants, sizes, states, tokens, spacing,
behaviour, accessibility, do/don't.

## State model
| State | Trigger | Visual | Notes |
|---|---|---|---|
| default | - | base | |
| hover | pointer over (gate with `@media (hover:hover)`) | slight shift (primary-hover) | never the only affordance |
| focus-visible | keyboard focus | 2px ring in `--color-focus`, 2px offset (≥ 3:1) | never removed |
| active/pressed | pointer down | darker + `scale(.97)` | 100-160ms ease-out |
| disabled | `disabled` / `aria-disabled` | neutral greys, still legible, cursor not-allowed | say why (tooltip/helper) |
| loading | async in progress | spinner/progress replaces icon, label stays ("Saving…"), width fixed | `aria-busy`, block double-submit |
| error | invalid | danger border + message below with icon | `aria-invalid`, `aria-describedby` |
| selected/checked | | filled/check + text change | `aria-pressed`/`aria-checked`/`aria-selected` |
| read-only | | distinct from disabled (normal text, no border) | |
Priority when several apply: disabled > loading > active > focus > hover > default. Interactive states increase
contrast, never decrease it. Transitions list properties explicitly.

## Button
Variants: primary (filled `--color-primary`, `--color-on-primary`), secondary (outline/tonal), ghost/text, destructive
(danger), link. One primary per view. Sizes: sm 32px, md 40px, lg 48px (touch UI: 44px minimum hit area; extend with
padding/pseudo-element if visually smaller). Padding x ≈ 1.5-2× height/3; icon 16-20px with 8px gap; label 1-3 words
naming the outcome. Radius from the brand logic (square or pill decided once; avoid a "soft" default). Loading keeps
width. Icon-only buttons need `aria-label` and a tooltip.

## Input / select / textarea
Label above (14px/500), 8px gap; field height 40px (44-48 touch); 1px `--color-control-border` (≥ 3:1) or filled
surface with a clear focus state; placeholder is an example, not a label (ends with "…"); helper text below, linked by
`aria-describedby`; error text replaces/adds below with icon; required marked in words or an asterisk explained once.
Correct `type`, `inputmode`, `autocomplete`; never block paste; font-size ≥ 16px on mobile (prevents iOS zoom).
Validate on blur, not every keystroke; on submit focus the error summary.

## Card / panel
Use only when the card IS the unit of interaction or content (a product, a project, a plan). Variants: flat (tone step),
outlined (1px border), elevated (shadow - only if it floats or drags). Padding 16-24px; header/content/footer gaps 12-16;
interactive cards: whole card clickable via one link with stretched pseudo-element, hover = subtle border/tone change.
No cards inside cards. Grids of peer cards: equal widths, aligned bottoms, no orphan cell.

## Navigation
Top nav: wordmark, ≤ 5 links, one action; active state visible (weight/underline/indicator, not colour alone); mobile:
labelled menu button → full-screen sheet with focus trap, Escape closes. Sidebar (apps): 224-260px, 32-40px rows,
16px icons, active = neutral pill or brightness; collapses to top bar/bottom nav on phones. Tabs: underline on a
full-width rule, or a segmented control as wide as its options; arrow-key navigation (`role=tablist`).
Breadcrumbs for 3+ levels.

## Dialog / sheet / popover / toast
Dialog sizes sm 384 / md 512 / lg 640 / xl 768 / full on phones; header (title + close), scrollable body, footer
(cancel left/secondary, confirm right/primary; destructive confirm names the object). Focus trapped, initial focus
inside, return focus on close, Escape and backdrop close (unless unsaved changes → confirm). Popovers scale from their
trigger (`transform-origin`), modals from centre. Toasts: polite live region, don't steal focus, 4-6s, pausable on
hover, never the only place for critical info, "Undo" for destructive actions.

## Table / list
Header 12-14px grey sentence case, no fill band; rows 40-56px; numbers right-aligned with tabular figures and fixed
decimals; identity column widest; one status mark per row (pale tint pill + dark text of the same hue); row actions in
a fixed trailing column or kebab; sortable headers with `aria-sort`; empty state keeps the frame + one sentence +
action; loading = skeleton rows at real pitch; below ~640px become two-line rows (never horizontal page scroll).

## Badge / status pill
16-24px tall, 11-13px text at 500, pale tint background with dark text of the same hue (positive #DCFAE5/#04250E,
negative #FFEDEA/#831C1E, notice #FFFBEB/#92400E); neutral states monochrome with a glyph. Never squeeze
(`flex: none; white-space: nowrap`). Never above a heading as an eyebrow.

## Feedback states
Empty: what this is for + first action (no sad illustration by default). Loading: final layout with grey bars at real
sizes, no shimmer gradient, no layout shift when data lands; > 1s show progress; refresh keeps old values + stamp.
Error: inside the block that failed, one sentence (what failed, when last good) + Retry. Success: brief confirmation
near the action.

## Component tokens (only where needed)
```css
:root {
  --button-radius: var(--radius-md); --button-height: 40px;
  --input-height: 40px; --input-border: var(--color-control-border);
  --card-padding: var(--space-6); --card-radius: var(--radius-lg);
  --focus-ring: 0 0 0 2px var(--color-ground), 0 0 0 4px var(--color-focus);
}
```
