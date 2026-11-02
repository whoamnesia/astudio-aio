# AIO pipeline playbook

Detail for each phase of the astudio-aio pipeline. SKILL.md is the map; this is the terrain.

## 1. Brief template (write this down in Phase 0)
```
CLIENT:        name (exact spelling) · what it does in one sentence · city/market · language(s) of the site
AUDIENCE:      who, their situation when they arrive, what they already know (awareness stage)
ONE ACTION:    the thing the site must get them to do (book, buy, call, sign up, download, visit)
PROOF:         real numbers, customers, photos, product UI, awards, guarantees we actually have
PAGES:         home + … (each with its job)
BRAND:         existing logo/colours/fonts/voice to keep · or "new"
ASSETS:        client photos/video/UI · web access for stock + reference research? · (never AI image generation)
STACK:         detected framework or "static HTML/CSS/JS" · hosting constraints
CONSTRAINTS:   deadlines, legal, accessibility level, must-not-look-like
SURFACE MODE:  Persuade / Operate / Read / Experience (per page if mixed)
ASSUMPTIONS:   what I decided without asking (the user can overrule)
```

## 2. Intake questions (pick only what blocks; one AskUserQuestion round)
- Business name + what it does (if missing) - blocks everything.
- Audience + the one action - blocks hierarchy and copy.
- Keep existing brand elements? (logo/colours/fonts) - blocks the logo phase.
- Pages and must-have sections (menu, prices, booking, catalogue, contacts).
- Liked/disliked references (sites, brands) - optional, never required.
Offer "decide for me" as an option. Never ask for CSS values or aesthetic lane names.

## 3. Direction checkpoint format
```
A — <name>  (recommended)
Idea: On this site, <subject thing> becomes <device>.
Palette: #… ground · #… ink · #… accent (strategy: committed)   Type: <display> / <text>   Shape: <radius logic>
First screen: <hero pattern + one sentence>   Signature: <wow move>   References: <2-3 links/patterns>
Pictures: <stock queries / illustration style>   Risk: <honest one-liner>
B — … / C — …
Category standard (played straight) is available if you prefer something familiar.
```

## 4. Phase handoffs (what each phase must produce for the next)
| Phase | Output that the next phase consumes |
|---|---|
| References | `.astudio/references.md`: 5-8 Awwwards/Behance references (or built-in hero/section patterns) with what to take from each |
| Direction | direction contract (with REFERENCES and RICHNESS); inventory; chosen strategy; candidate faces; hero pattern |
| Logo | final SVG mark + lockups (paths only), one-colour versions, small-size cut, favicon set, construction notes, shape language words |
| Brand kit | palette.json (light/dark roles, ramps), brand.spec.json, voice & messaging, imagery rules, brand-book.html |
| Design code | design-tokens/*.tokens.json + tokens.css + tailwind-theme.css, DESIGN.md, component specs (buttons, inputs, cards, nav, states) |
| Assets | stock photo set (6-12, one grade, credits), icon set, graphic language kit (devices, stickers, patterns, illustrations in SVG) |
| Site | pages in the project stack, assets, credits, sample-content list, screenshots + critique log |

## 5. Unattended vs attended
- **Attended** (user is responsive): checkpoints after direction, logo concepts, brand book. Each checkpoint is one
  message with a screenshot/image and a clear recommendation; wait for the answer.
- **Unattended / "don't ask, just deliver"**: make the recommended choice at each checkpoint, record it in the final
  report with the alternatives, and keep going.

## 6. Pulling in sub-skills mid-pipeline
| Signal in the brief | Sub-skill and where it applies |
|---|---|
| Software product, SaaS, app with a UI to show | `dashboard` rules for the product fragments on the landing page (marked `data-ui`) |
| "Mobile-first", app download, most traffic from phones, PWA | `mobile` for the 390px composition, touch, safe areas; app screens if an app is designed too |
| Product/object worth exploring, "3D", configurator, immersive | `3d-elements` for the hero object or a section scene (with a static fallback) |
| Launch campaign, social presence, ads | `banner-design` / `cta-banner` after the site, reusing the tokens |
| Investor/client presentation | `slides` reusing tokens |
| Icon set, social templates, merch, stationery | `design` |

## 7. Redesign of an existing site
Record the before (render + lint), extract what is true (content, routes, forms, brand assets, what works), decide
refresh vs redesign with the user, keep the stack, then run Phases 1-5 with the real content. Report before/after
screenshots and measurements side by side. Never migrate frameworks or styling libraries without being asked.

## 8. Time and scope sense
A one-page landing with a new logo and brand: direction → 3 logo concepts → kit → brand book → page → 2-3 critique
rounds. A multi-page site: build the home page to final quality first, get approval, then derive the other pages from
the same system (do not design every page from scratch; reuse section compositions with page-specific content).
