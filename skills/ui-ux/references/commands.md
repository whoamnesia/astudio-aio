# Refinement playbooks

Each playbook preserves the product's identity, content and behaviour; it changes presentation. Render before and
after every playbook.

## polish - final quality pass before shipping
Triage in order: (1) broken/blocked tasks, misleading state, inaccessible paths; (2) missing loading/empty/error/
success/disabled/permission states; (3) flow, hierarchy, responsive and design-system drift; (4) visual and motion
inconsistencies; (5) code and asset cleanup. Classify each drift: missing token / one-off implementation (replace with
the shared component) / conceptual mismatch / local defect - fix at the narrowest correct level. Check optical
alignment (not only mathematical), consistent same-role typography, icon family and stroke, image aspect ratios,
focus order, touch targets, browser surfaces themed, console clean, no layout shift. Walk the whole path with mouse,
keyboard and touch.

## bolder - amplify a safe or bland design
Find the one thing that should be memorable and make it win: scale contrast up (display ≥ 4-6× body), commit colour
at page scale (a full field section, a Committed strategy), replace the stock hero with a composition from the idea,
give the type a face with a point of view, add one signature move. Do not add ornaments (gradients, glows, blobs) -
boldness is scale, colour fields, real pictures and committed type. Keep usability floor intact.

## quieter - tone down an aggressive design
Reduce competing accents to one; collapse font sizes to ≤ 5; remove decorative effects (glow, gradients, shadows on
resting elements, multiple animations); increase whitespace between groups, not inside them; lower motion to feedback
plus one moment; desaturate secondary colours; keep the brand's signature.

## distill - strip to essence
List every element and ask what job it does; cut elements without a job, merge duplicates, move secondary actions into
menus or secondary pages, shorten copy by 30% and keep cutting while it improves, reduce the number of containers
(cards, borders) - group by space instead. One primary action per screen.

## harden - production readiness
Empty, zero, loading, error, offline, slow network, permission-denied, partial data, very long and very short content
(names, numbers, translations - Russian runs ~15% longer, German ~30%), RTL if relevant, 200% zoom, reduced motion,
high contrast, keyboard-only, screen reader names, double-submit prevention, unsaved-changes guard, timeouts with retry,
error boundaries, input limits stated beside fields, locale-aware number/date/currency formatting (`Intl`).

## typeset - improve typography
Choose/verify faces (typography.md §5), set a scale with few far-apart steps, fix measure (45-75ch), leading,
tracking per size, heading balance and authored breaks, numerals (tabular in data), quotes/dashes (EN and RU rules),
paragraph spacing, link underline styling. Check loaded fonts actually render.

## colorize - add strategic colour to a monochrome UI
Pick the strategy (Restrained/Committed/Full/Drenched) by mode; one hue first; put it on the primary action, the key
data element, selection and focus; consider one full colour field section on Persuade pages; tint neutrals slightly with
the hue; verify every pair with palette.py; never colour as the only carrier of meaning.

## layout - fix spacing, rhythm, hierarchy
One focal point per screen; 2-3 anchor lines; spacing scale on a 4px base; section gaps > inner gaps; heading closer to
its content than to the previous section; equal margins; close holes (picture, bigger main element, or remove space);
vary section compositions; align bottoms of rows.

## clarify - UX copy
Labels name things in users' words; buttons name outcomes; errors say what happened and how to fix it; empty states
invite the first action; one term per concept; remove instructions that a better control would make unnecessary;
Russian UI rules (copy.md §7).

## adapt - other devices
Design the 390px composition deliberately (crops, breaks, nav sheet), tablet band 641-1100, touch targets 44px,
`(hover:hover)` gating, safe areas, `svh/dvh`, tables → two-line rows, filters → sheet/chips, sidebars → top/bottom bar.
Hand off to `astudio-aio:mobile` for app-level work.

## onboard - first-run and activation
Keep the frame and title on an empty first screen; put the first action where data will appear; a setup checklist at
its true percentage; sample data clearly labelled; progressive disclosure of advanced features; celebrate the first
success briefly (peak-end); never block with a multi-page tour (max 3 skippable steps).

## delight - personality where it earns its place
Delight follows from getting everything else right. Candidates: one well-made signature interaction, a considered
empty state in the brand's voice, a satisfying completion moment, a small easter egg that never blocks. Respect
frequency (no delight on actions done 100× a day) and reduced motion.
