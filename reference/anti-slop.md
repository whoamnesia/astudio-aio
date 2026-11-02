# Anti-slop registry

A **tell** is a device that makes a design read as generated. Most began as good ideas; they became tells by being
produced by default, everywhere, without a reason. Status: **ban** = refuse unless the brief/brand explicitly
demands it (record the exception); **default-refuse** = a category default you may use only with a stated reason;
**Operate-ok** = normal on working app screens.

`scripts/lint.py` detects many of these in source; the rest need your eyes on the render.

**Read with `studio-bar.md`.** This registry bans cheap *defaults*, not richness. Award-level devices (marquees,
custom cursors, short branded preloaders, scroll storytelling, oversized type, layered collages, stickers, icons,
illustrations) are welcome when they are crafted for this brand and serve the idea. The worst outcome is an "empty
page with good manners": no tells, no pictures, no graphics, no wow.

## Surface

| Tell | Status | Instead |
|---|---|---|
| Gradient-filled text | ban | solid ink; emphasis by weight or size |
| Violet/indigo or blue-to-purple gradient backgrounds and buttons | ban | the committed palette; flat fills |
| Gradient CTA button | ban | one solid colour the palette owns |
| Zero-offset coloured glow / radial halo / spotlight behind the hero | ban | depth has an offset and a soft blur; or a tone step |
| Soft grey shadow under every card; thin border + wide shadow together | ban | a tone step OR a border OR a shadow - never all; shadows only on what floats |
| Glass/backdrop-blur panels as the default surface | default-refuse | one translucent layer where it explains floating (nav over content, sheet) |
| Coloured `border-left` stripe on cards/callouts/alerts | ban | full border, tint, leading icon, or nothing |
| Hard offset shadows (`4px 4px 0`) outside a genuinely neo-brutalist world | ban | a depth system that matches the world |
| Generic decorative blobs, random floating circles, stock wavy dividers | ban | the brand's own graphic device built from the logo and the subject (shapes, patterns, stickers, cut-outs) |
| AI-generated photos or illustrations | ban | free stock photos (credited) and graphics drawn in code (`imagery.md`) |
| Cream ground + terracotta accent (see direction.md §7) | default-refuse | low-chroma stone/bone with deep ink, or a saturated warm field used flat |
| Near-black + one neon accent with glow | default-refuse | true neutral darks, lightness steps, colour on data |
| One medium radius (12-16px) on everything | default-refuse | square or fully round chosen once; radii by surface size |
| Emoji as icons, bullets, nav or headings | ban | a real icon set (one stroke, one weight) or words |
| Icon in a tinted rounded square above every heading/card, identical everywhere | default-refuse | icons from one crafted set, sized and placed by role (inline, large, in a sticker) |
| Clip-art "illustrations" assembled from CSS circles, mismatched SVG doodles | ban | a crafted illustration language drawn in code for this subject, consistent stroke/fill/corners |
| Grey placeholder boxes, fake dashboards of grey bars, lorem ipsum, "John Doe", "Acme" | ban | real content or believable sample content listed for replacement |

## Structure

| Tell | Status | Instead |
|---|---|---|
| Three identical feature cards (icon + bold title + 2 lines), repeated | ban | a composed section from the content; unequal content gets unequal space |
| Stock section order: hero → logos → 3 features → testimonials → pricing → CTA, every section the same height | ban | the order of the argument (copy.md §1); vary composition between neighbours |
| Centred headline + subtitle + two buttons + screenshot below | default-refuse | a hero built from the idea; left-anchored with one centred moment at most |
| Headline left, product screenshot right, badge row under | default-refuse | as above |
| Hero-metric template: big number, small label, stat row, gradient accent | ban | evidence in prose or one committed visual |
| Bento grid of near-identical or empty cells | default-refuse | bento only with real variation per cell |
| Cards inside cards | ban | flatten; group by space and tone |
| Everything centred | ban | left alignment by default, one centred moment |
| Eyebrow / kicker: tiny tracked uppercase label above headings | ban (Persuade) | put the information in the heading or first sentence |
| Pill badge above the hero headline ("New", "Introducing") | ban | say it in the supporting line |
| 01 / 02 / 03 numbering when order carries no meaning | ban | position, scale or words; a real `<ol>` when it is a sequence |
| Monospace labels as a "technical" voice | ban (Persuade) | text face; tabular figures for data; mono only for code/IDs |
| Hairline rules, crop marks, crosshairs, grid lines as ornament | default-refuse | space, tone steps, filled shapes |
| Carousel with no narrative purpose; marquee of client logos or buzzwords | ban | show the important items still; a marquee only with real content (menu items, offers) and brand glyphs |
| Modal for tasks that need neither interruption nor protected focus | default-refuse | inline, side panel or a page |
| Oversized display type with nothing else on the screen | default-refuse | big type works with a picture/object in the same composition (`studio-bar.md` §4) |
| Text-only sections, a hero without a dominant visual, an industry you cannot recognise without reading | ban | a visual anchor in every section; the subject shown (`studio-bar.md` §3-5) |
| Three-plus-line hero headline | ban | ≤ 2 lines at every width (copy.md §2) |
| Only the happy path designed | ban | empty, loading, error, long-content, offline states |
| Dark or light picked by category | ban | from the use scene |

## Type

| Tell | Status | Instead |
|---|---|---|
| Training-data default as the Persuade display voice: Inter, Roboto, Arial, Helvetica, Open Sans, Lato, Montserrat, Poppins, Space Grotesk, Space Mono, Syne, Outfit, Plus Jakarta Sans, Instrument Sans/Serif, DM Sans/Serif, IBM Plex, Geist, Fraunces, Playfair Display, Cormorant, Lora, Crimson, Newsreader | default-refuse | a face chosen from the subject's world (typography.md §5); several are fine as Operate/Read body text |
| system-ui as the whole type voice on a brand page | default-refuse | a real typeface (system UI is right for native apps and dense tools) |
| One styled word in the headline (italic serif / colour / underline) | default-refuse | one face, one colour; the words carry emphasis |
| Nine near-equal font sizes | ban | ≤ 5-6 sizes, far apart |
| Body text in soft grey, < 16px, or < 4.5:1 | ban | full ink, ≥ 16px (Persuade/Read), ≥ 14px (dense Operate) |
| Straight quotes, "...", hyphen as dash | ban | typographic characters (typography.md §7) |

## Copy

| Tell | Instead |
|---|---|
| unlock, unleash, supercharge, seamless, effortless, elevate, empower, streamline, revolutionise, cutting-edge, next-gen, all-in-one, world-class, blazing fast | say what the product does, with a number |
| RU: инновационный, уникальное решение, высококачественный, индивидуальный подход, широкий спектр услуг, команда профессионалов, лидер рынка | конкретика: что, сколько, для кого, за какой срок |
| "Welcome to X", "Meet X", "X, reimagined", "Built for the way you work", "Your all-in-one solution" | a title that says what this is |
| Tricolon slogans ("Fast. Simple. Secure.") and "not just X, it's Y" | one plain sentence |
| "Get started" / "Learn more" / "Submit" / "Подробнее" as the only CTAs | name the outcome: "Book a table", "See plans", "Забронировать столик" |
| Invented social proof: logos, quotes, star rows, "10,000+ teams", "99.9% uptime" | real proof beside the claim, or no claim |
| Em dashes as a habit, performative labels ("Field notes", "Our philosophy") | full stops; plain section names ("Pricing") |

## Motion

| Tell | Instead |
|---|---|
| The same fade-and-rise on every section | one authored moment; entrances that fit what they reveal |
| A dozen staggered hero entrances | ≤ 4 things in the load sequence, settled by ~1.2 s |
| Hover lift/zoom on every card and image | one consistent small response where it carries information |
| Bounce/elastic easing on interface elements | strong ease-out; springs without overshoot unless the gesture threw it |
| Pulsing dots, shimmering text, meaningless infinite loops | loops only with meaning (a sticker turning with scroll, a marquee of real items), paused off-screen and under reduced motion |
| Long preloaders, gates, scroll hijacking that traps the reader | a branded preloader < 1 s only while real assets load; smooth scroll (Lenis) that never traps; a custom cursor only on fine pointers and with the system cursor's affordances |
| `transition: all`, `scale(0)` entrances, `ease-in` on UI | explicit properties, start at 0.95 + opacity, ease-out |
| Reveals that keep content invisible if JS fails | hidden states only under `html.js` and `prefers-reduced-motion: no-preference` |

## Operate surfaces (dashboards, admin, app screens)

Relaxed: 1px borders on cards/tables/controls, row rules, small grey sentence-case labels above values, rows of
identical peer cards (3-6, no icons on top), mono for IDs, pale status pills inside rows, shadows on floating layers.
Still banned there: gradients on grounds/buttons/KPIs, glow/glass, icons in coloured circles on KPIs, sparklines on
every KPI, rainbow charts (>4 hues), zebra striping, uppercase tracked table headers, left-aligned numbers, a hero
header or "Welcome back 👋", a dark/saturated sidebar on a light screen, the accent on chrome. See
`skills/dashboard/references/app-screen-rules.md`.

## Why removal is not enough

The tells were filling a gap where an idea should have been. Remove them and fill the gap with the idea, real
pictures, icons, a crafted graphic language, full content, committed type and colour and one wow moment
(direction.md, studio-bar.md).
