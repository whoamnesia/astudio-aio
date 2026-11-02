---
name: mobile
description: >-
  astudio mobile design: professional mobile versions of websites (a real 390px composition, touch, safe areas,
  native-feeling web: no tap delay, stuck hover, iOS input zoom, 100vh jumps) and complete mobile app design for iOS
  (HIG, Liquid Glass, SF Symbols, Dynamic Type), Android (Material 3 / M3 Expressive, dynamic colour) and cross-platform
  (React Native/Expo, Flutter, SwiftUI, Jetpack Compose, PWA) - navigation, screens, flows, onboarding, gestures,
  motion, haptics, accessibility and app icons, using the project's brand kit/design code. Use when the user asks for a
  mobile version, mobile-first site, app design, iOS/Android screens, "мобильная версия", "адаптив под телефон",
  "дизайн мобильного приложения", "экраны приложения", "сделай чтобы на телефоне было удобно", or a PWA. Part of astudio-aio.
argument-hint: "[mobile-web | ios | android | cross-platform] [screens or page]"
---

# astudio · Mobile

Role: Senior mobile UI/UX designer at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

The phone is the source of truth. A mobile version is a second composition, not the desktop squeezed; an app follows
its platform's conventions so people already know how to use it, and expresses the brand through type, colour, shape,
motion and one signature element.

Shared: `<root>` = two levels above this skill's base dir. Inherit the brand kit/design code (`DESIGN.md`,
`design-tokens/`, `brand/`) - if none, run `astudio-aio:brand`/`design-system` in a compact pass or extract from the
existing product. Local references: `references/mobile-web.md` (native-feel fixes, baseline), `references/ios.md`
(HIG + Liquid Glass), `references/android.md` (Material 3 Expressive), `references/app-design.md` (navigation, screen
patterns, flows, onboarding, cross-platform, app icons), `references/app-rules-checklist.md` (pre-delivery checklist).
Database: `search.py "<concern>" -d app` and `--stack react-native|flutter|swiftui|jetpack-compose`.

## A. Mobile version of a website
1. Render the current site at 390 and 768 (`render.cjs shots --widths 390,768`) - or the desktop design if new.
2. Recompose for 390 (`<root>/reference/layout.md` §9): one dominant thing on the first screen; title + supporting line
   + primary action in view; re-authored headline breaks (≤ 2 lines at ~32-40px); portrait crops (`<picture>` /
   `object-position`); navigation as wordmark + one action + a labelled menu sheet; sections stack with their own
   rhythm (72-112px gaps); tables → cards/two-line rows; long rows scroll inside their frame with a visible cut.
3. Apply the native-feel baseline (`references/mobile-web.md`): viewport-fit=cover + safe areas, `svh`/`dvh`,
   16px inputs, `touch-action: manipulation`, tap highlight off + real `:active` states, hover gated by
   `(hover:hover) and (pointer:fine)`, overscroll containment in sheets, `theme-color` per scheme, correct
   `inputmode`/`autocomplete`/`enterkeyhint`.
4. Thumb zone: primary actions reachable in the lower half; sticky bottom CTA only when it is the page's one action
   (with safe-area padding) and it never covers content or focus.
5. Verify at 360, 390, 430 and 768 widths, portrait and landscape; reduced motion; check every screenshot; say which
   behaviours need a real device (sticky hover, keyboard, rubber-banding).

## B. Mobile app design
1. **Brief**: platform(s), stack (native or cross-platform), audience and context of use (one-handed, on the move,
   glance vs long session), the core jobs, what must work offline, notifications value.
2. **Information architecture**: 3-5 top-level destinations (tab bar / navigation bar), what lives one level deeper,
   which tasks are modal (sheets) vs pushed screens. Map the main flows (onboarding → first success → habit loop).
3. **Platform decision**: iOS conventions (`references/ios.md`), Android conventions (`references/android.md`), or a
   shared design system that respects both (shared anatomy and behaviour, platform-specific chrome: back gesture,
   navigation, controls, type). Never ship iOS chrome on Android or vice versa.
4. **Design language**: tokens adapted to platform roles (iOS semantic colours / M3 colour roles generated from the
   brand seed), type mapped to Dynamic Type styles / M3 type roles (sp units), shape (iOS concentric continuous corners
   / M3 shape scale), motion (springs; M3 Expressive motion physics), haptics for confirmations and errors.
5. **Screens**: build the key screens with every state (`references/app-design.md` §3) as hi-fi HTML mockups in device
   frames (390×844 iPhone, 412×915 Android) using the tokens - or as real code in the project's stack (SwiftUI, Compose,
   RN/Expo, Flutter). Render and look at each.
6. **Checklist**: `references/app-rules-checklist.md` + accessibility (VoiceOver/TalkBack order and labels, Dynamic Type
   to accessibility sizes, 44pt/48dp targets, contrast in both themes, reduced motion/transparency).
7. **App icon**: from the logo's symbol (`logo_kit.py variants --icon-bg`), optically sized in the platform shape,
   no text, tested at 29-1024px and on light/dark/tinted home screens.

## Non-negotiables
Never disable zoom; never hamburger-only navigation on iOS phone apps; never override system back gestures; touch
targets 44pt (iOS) / 48dp (Android); labels on navigation bar items; safe areas respected; light and dark themes both
designed; permission requests in context with a reason first; skeletons instead of blocking spinners; every gesture has
a visible alternative; test on real hardware where behaviour depends on it, and say what you could not verify.
