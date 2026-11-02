# Android (Material 3 and M3 Expressive)

## M3 Expressive (2025+)
The most researched Material update (46 studies, 18,000+ participants): expressive design uses **colour, shape, size,
motion and containment** to make key actions stand out and group like elements. In eye-tracking, people found key UI
elements up to 4× faster (e.g. a larger Send button just above the keyboard in a secondary colour), and age gaps in
finding elements largely disappeared. It is preferred across ages (strongest 18-24). But context matters: breaking
familiar patterns (an unlabelled helter-skelter playlist, removing action labels) hurt usability - expressive tactics
sit on top of standard patterns, never replace them; a strong minority prefers calmer versions; start from user needs.
Tactics: bigger and more varied shapes (the expanded shape library, shape morphing), emphasised type for key moments,
richer colour roles, containment to group, spring-based motion physics (spatial and effects springs), new components
(floating toolbar, button groups, split buttons, expressive progress indicators, FAB menu).

## Theming
- Dynamic colour from the wallpaper (Android 12+) as the default, with a static fallback scheme generated from the brand
  seed via Material Theme Builder; never hand-pick individual tones; never hard-code hex in components.
- Colour roles: primary/onPrimary, primaryContainer/onPrimaryContainer, secondary(+Container), tertiary(+Container),
  surface + surface container levels (lowest…highest), onSurface/onSurfaceVariant, outline/outlineVariant, error(+
  Container), inverseSurface (snackbars). Every foreground uses the matching `on` role.
- Light and dark always; dark uses tonal surface elevation, not pure #000; offer System/Light/Dark in settings.
- Brand expression through primary/tertiary seeds, shape scale, typography, motion - while honouring dynamic colour.

## Navigation and layout
- Navigation bar (bottom) for 3-5 destinations with labels always visible; navigation rail on medium widths; navigation
  drawer for many destinations/large screens; top app bar tied to scroll behaviour; one FAB per screen for the primary
  action; predictive back (`OnBackInvokedCallback` / Compose `BackHandler`), correct Up vs Back.
- Window size classes: compact (< 600dp), medium (600-840), expanded (> 840): list-detail and supporting-pane layouts;
  content not full-width on tablets; foldable hinge respected.
- Edge-to-edge with proper insets (status, navigation, IME); 8dp grid; touch targets ≥ 48×48dp.

## Typography
Roboto Flex / brand face via M3 type roles (display L/M/S 57/45/36, headline 32/28/24, title 22/16/14, body 16/14/12,
label 14/12/11) in **sp**; test at 200% font scale; body ≥ 12sp (14-16 recommended), labels ≥ 11sp.

## Components and patterns
Snackbars for non-critical feedback (with undo), dialogs only for critical interruptions, bottom sheets for secondary
tasks, chips for filters, cards only as units of content; skeletons; notification channels per type with appropriate
importance; permissions in context with rationale and graceful degradation; Photo Picker instead of storage permission;
widgets with Glance and dynamic colour; app shortcuts; deep links for public content.

## Accessibility
contentDescription on every interactive element; TalkBack order; 48dp targets; 4.5:1 text contrast; never colour alone;
Switch Access and keyboard; gesture alternatives; swipe-to-dismiss undoable.

## Anti-patterns
Hard-coded colours; dp for text; custom bottom nav instead of NavigationBar; icon-only nav bar; dialogs for
non-critical info; multiple FABs; overriding onBackPressed; < 48dp targets; permission at launch; pure black dark theme;
full-width content on tablets; iOS chrome on Android.
