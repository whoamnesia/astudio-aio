# iOS (Human Interface Guidelines, iOS 26 / Liquid Glass)

## Liquid Glass - the 2025+ design language
- A digital meta-material that bends and concentrates light (lensing) and moves like a light liquid: controls flex,
  energise with light on touch, morph between states, and menus pop open from the button that triggered them.
- **Reserved for the navigation/control layer floating above content** (tab bars, toolbars, sidebars, sheets, menus,
  floating buttons). Content (lists, cards, tables) stays in the content layer - glass there muddies hierarchy.
- **Never glass on glass.** Elements on top of glass use fills, transparency and vibrancy, not another glass layer.
- Two variants, never mixed: **Regular** (adaptive, works anywhere, the default) and **Clear** (more transparent, needs a
  dimming layer; only over media-rich content, when dimming won't hurt the content, and the content on it is bold).
- Small glass elements flip light/dark with what is behind them; large ones (menus, sidebars) adapt but don't flip.
- Tint only primary actions (e.g. the one "Checkout" button); tinting everything means nothing stands out - put colour
  in the content layer instead. Use the system tinting, not opaque fills, on glass.
- Avoid content/glass intersections at rest (reposition or scale content). Scroll edge effects (soft by default, hard
  for pinned headers) replace hard dividers where floating UI overlaps content - one per view, never decorative.
- Accessibility modifiers come free with system glass: Reduce Transparency (frostier), Increase Contrast (black/white
  with borders), Reduce Motion (no elastic effects). Custom glass must honour them.
- **Concentricity**: shapes nest around a shared centre - fixed radius, capsule (radius = half height), or concentric
  (radius = parent radius − padding). Corners that feel pinched or flared usually need to be concentric. Near screen
  edges on phones use a capsule with extra margin. Group bar items by function; a primary action (Done) stays separate
  and tinted; don't group a symbol with a text button. Search can be a dedicated bottom tab.
- Remove custom bar backgrounds/borders from pre-26 designs; hierarchy comes from layout and grouping.
- On the web, approximate sparingly: `backdrop-filter: blur(20px) saturate(180%)` + semi-transparent fill + a bright
  1px top edge, only for floating nav over content, with `prefers-reduced-transparency` fallback to solid.

## Layout and navigation
- Targets ≥ 44×44pt; 8pt grid (4pt fine adjustments); support iPhone SE (375pt) to Pro Max (430pt) and landscape.
- Respect safe areas; `.ignoresSafeArea()` only for backgrounds/media.
- Primary actions in the thumb zone; secondary/navigation at the top.
- **Tab bar** for 3-5 top-level sections (never a hamburger on iPhone); large titles on top-level screens collapsing to
  inline on scroll; NavigationStack for drill-down; never override the edge back-swipe; preserve scroll and input state
  across navigation; sheets for scoped tasks (detents, grabber), alerts only for critical info, context menus for
  secondary actions, confirmation dialogs (action sheets) originate from their trigger.

## Type, colour, symbols
- SF Pro (system) with Dynamic Type text styles (Large Title 34, Title 1 28, Title 2 22, Title 3 20, Headline 17
  semibold, Body 17, Callout 16, Subheadline 15, Footnote 13, Caption 12/11); custom fonts must scale with Dynamic Type
  (`UIFontMetrics` / `.font(.custom(_, relativeTo:))`); support accessibility sizes without truncation; minimum 11pt.
- Semantic system colours (label, secondaryLabel, systemBackground, secondarySystemBackground…) with light/dark/
  increased-contrast variants for custom colours; one accent (tint) for interactive elements; never colour alone;
  4.5:1 contrast; Display P3 allowed for vivid brand colours.
- SF Symbols matching text weight and scale; rendering modes (monochrome, hierarchical, palette, multicolour);
  symbol animations for state changes (iOS 17+); preferred glyphs for common actions per the HIG Icons page.

## Patterns
- Onboarding ≤ 3 skippable pages (or none - teach in context); launch screen matches the first screen; skeletons, no
  blocking spinners; feedback = visual + haptic (UIImpactFeedbackGenerator / sensoryFeedback) on the same frame;
  notifications only high-value with clear categories; settings in-app for app-specific options.
- Privacy: ask permission in context, explain before the system prompt, Sign in with Apple if other social logins exist,
  don't require accounts unnecessarily, App Tracking Transparency, Location button for one-time access.
- System integration where valuable: widgets (glanceable), Live Activities, App Shortcuts/Siri, Spotlight, share sheet.

## Accessibility
VoiceOver labels/hints/traits and logical order; Bold Text, Reduce Motion, Increase Contrast, Reduce Transparency,
Switch Control and Full Keyboard Access support; alternatives for every gesture; Dynamic Type to AX5.

## Anti-patterns
Hamburger menus; custom back gestures; hard-coded font sizes; ignoring safe areas; glass everywhere or stacked;
tinting every control; modal for navigation; permission prompts at launch; tiny tap targets; custom controls where
system ones exist without a brand reason.
