# DESIGN.md - the design code

DESIGN.md is the source of truth an agent or a person reads before touching the UI. It pairs evocative language
(so the intent survives) with exact values (so the output is reproducible). Keep it current; write it from the built
result.

## Format
Optional YAML front matter with flat, export-safe tokens (compatible with tools that read DESIGN.md front matter):
```yaml
---
name: Bean There
colors:
  ground: "#FFF9F7"
  ink: "#221814"
  primary: "#C2410C"
  on-primary: "#FFFFFF"
typography:
  display: { fontFamily: Unbounded, fontWeight: 600, lineHeight: 0.98 }
  body: { fontFamily: Onest, fontSize: 17px, lineHeight: 1.55 }
rounded: { base: 8px }
spacing: { base: 4px }
---
```
Token names must match `^[a-zA-Z0-9][a-zA-Z0-9-]*$`; typography entries use fontFamily/fontSize/lineHeight/fontWeight/
letterSpacing only. Full tokens live in `design-tokens/*.tokens.json`; the front matter is a summary, not a second schema.

## Body sections
1. **Atmosphere** - the idea in one sentence, mood, density, surface mode(s), the one signature move.
2. **Colour roles** - "Deep Kiln Rust (#C2410C) - primary actions and the one accent per screen; 4.97:1 on ground".
   Light and dark tables; proportion rule; status colours; what colour is never used for.
3. **Typography** - faces, roles, source/licence, Cyrillic support, the scale (min-max px), tracking/leading rules,
   numerals, case, language typography rules.
4. **Shape & depth** - radius logic described physically ("pill-shaped buttons, gently rounded 8px fields, square
   photographs"), border vs tone vs shadow policy, what floats.
5. **Layout** - grid, margins, anchor lines, section rhythm, breakpoints, max widths, density.
6. **Components** - per component: shape, colours (roles), sizes, states, behaviour, do/don't.
7. **Motion** - tokens, signature move, entrance and feedback rules, reduced-motion behaviour.
8. **Imagery & icons** - photo direction and treatment, illustration rules, icon library + stroke.
9. **Voice** - traits, CTA vocabulary, error/empty tone, language rules.
10. **Do / Don't** - 8-12 rules that prevent drift, each with its reason, including the anti-slop items this brand bans
    and any brief-mandated exceptions.

## Style of writing
Descriptive and precise: "Ocean-deep teal (#0F766E)" not "blue"; "sharp, squared-off edges" not "rounded-none"; explain
the why ("tabular figures in prices so columns don't jitter"). Use the same terms everywhere. No marketing prose.
