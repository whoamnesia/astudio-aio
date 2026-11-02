# App design: structure, screens, flows

## 1. Information architecture
- Top-level destinations 3-5 (tab/nav bar); everything else one or two levels deep. A destination is a place users
  return to (Home, Search, Library, Inbox, Profile), not an action.
- Push for drill-down (hierarchy), sheet for a scoped task (compose, filter, edit), full-screen modal only for
  immersive or blocking flows (camera, checkout, onboarding).
- Search reachable from the top level (a tab on iOS 26, a search bar/top app bar on Android) with recent/suggested queries.
- Deep links for every important screen; state restoration on relaunch.

## 2. Core flows to design explicitly
Onboarding (value first; ≤ 3 skippable screens or contextual hints; permissions in context) → sign up/in (Sign in with
Apple/Google, passkeys, magic link/OTP with `one-time-code` autofill; never force an account before value) → first
success (the shortest path to the core job, with sample content clearly labelled) → the habit loop (the screen people
open daily: what changed, what to do next) → notifications (opt-in after value, categories, quiet hours) → settings,
account, deletion (account deletion in-app is required by both stores) → error/offline recovery.

## 3. Screen patterns and their states
| Screen | Must have | States |
|---|---|---|
| Home / feed | what's new for me, the next action, pull-to-refresh | loading skeleton, empty (first run), offline, error, end of feed |
| List | search/filter, sorting, swipe actions with visible alternatives | empty, no results (with clear filters), loading more, error |
| Detail | the object large, primary action in thumb zone, share | loading, missing/deleted, permission denied |
| Create/edit | autosave or explicit save, validation inline, keyboard-aware layout | unsaved changes on dismiss, error, success |
| Checkout/payment | order summary, Apple/Google Pay first, clear total, trust details | processing, declined (specific reason), success receipt |
| Profile/settings | grouped lists, destructive actions last and separated | signed out, sync issues |
| Chat/messages | composer above keyboard, send button prominent (M3 Expressive finding), read state | sending, failed (retry), empty conversation |
| Media player | large artwork, scrubber with time, persistent mini-player | buffering, offline, no permission |
| Map | list/sheet companion with magnitudes, recentre, filters | location denied, no results |
Every screen: loading, empty, error, offline, long content, large text, dark mode.

## 4. Mobile visual language from the brand
- Tokens → platform roles: brand primary → iOS tint / M3 seed; neutrals → system backgrounds or M3 surfaces; status
  colours preserved; dark variants designed.
- Type: brand display face only for large titles/moments (scaled with Dynamic Type), system/text face for UI; sp/pt units.
- Shape: iOS continuous corners and concentric nesting / M3 shape scale (extra-small 4 … extra-large 28, full).
- Motion: springs (iOS: damping 1.0 default, response ~0.3-0.4; M3 Expressive spatial/effects springs); shared-element
  transitions between list and detail; sheets with drag-to-dismiss and velocity; haptics with causality, harmony (same
  frame as the visual) and utility (only meaningful moments).
- One signature element from the product's world (e.g. a ritual animation on completion, a distinctive progress shape).

## 5. Mockups and hand-off
- Hi-fi HTML mockups: device frames at 390×844 (iPhone 15/16/17), 430×932 (Pro Max), 412×915 (Pixel); status bar,
  safe areas, home indicator drawn; real content; both themes. Render each frame with `render.cjs element`.
- Code: SwiftUI (NavigationStack, TabView, .sheet, .glassEffect for custom floating controls), Jetpack Compose
  (Material3 + dynamic colour), React Native/Expo (Expo Router, react-native-reanimated, expo-haptics, safe-area-
  context, platform-specific navigation), Flutter (Material 3 + Cupertino adaptive widgets). Database:
  `search.py "<concern>" --stack swiftui|jetpack-compose|react-native|flutter`.
- Specs per screen: layout grid, spacing, type styles, colour roles, components and states, gestures, motion values,
  accessibility labels and order.

## 6. App icon
From the logo symbol: no text, simple silhouette, optically sized (~60-70% of the tile), works on light, dark and
tinted (iOS 18+ tinted/dark icon variants; iOS 26 layered icons via Icon Composer), Android adaptive icon (foreground
108dp with 66dp safe zone + background layer, monochrome layer for themed icons). Export: iOS 1024px master; Android
512px Play Store + adaptive layers. Test at small sizes on real wallpapers.

## 7. PWA
Manifest (name, icons 192/512 + maskable, theme/background colour, display standalone), service worker for offline
shell, install prompt after value, standalone-mode safe areas and status bar, no browser-only UI (back button in-app).
