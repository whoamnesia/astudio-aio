# Direction and taste

How to arrive at a design that belongs to *this* subject instead of the average of every page a model has
seen. Read before any new surface, brand or redesign, together with `studio-bar.md` (role, reference research,
wow first screen, richness floor, images policy). The output of this file is a written **direction contract**
(section 8) that every later step builds against.

## Contents
1. Surface mode decides the ambition
2. Read what is already true
3. Inventory the subject
4. Find the idea (and pass the competitor test)
5. Derive candidate worlds
6. Commit the world: colour strategy, ground, type, shape, motion
7. Calibration: the looks that mean you stopped deciding
8. The direction contract
9. When the brief pins a look

---

## 1. Surface mode decides the ambition

Name the mode from the surface being built, not from the product. A developer tool's landing page is Persuade;
a fashion house's docs are Read.

| Mode | Visitor's success | Examples | Ambition shows as |
|---|---|---|---|
| **Persuade** | decides and acts | landing, marketing site, pricing, campaign, event, restaurant | a committed world, a wow first screen, a rich page (pictures, icons, graphics in every section), a working primary action on the first screen |
| **Operate** | completes a task | dashboard, admin, settings, editor, CRM, app screens | precision, density, calm hierarchy; the world lends only type, palette, density and one signature move |
| **Read** | understands something | docs, articles, help, changelog | measure, structure, wayfinding; staying is a pleasure |
| **Experience** | is inside the work | portfolio, gallery, showcase | the artefact owns the first viewport; chrome recedes |

Hybrid pages are classified per section (a marketing page with an embedded product demo: the page is Persuade,
the demo's insides follow Operate).

## 2. Read what is already true

Before inventing anything, collect:
- **Brand assets:** logo, colours, fonts, existing DESIGN.md / brand book / tokens / Tailwind theme / CSS vars.
  If they exist, they are the world - extend them, do not replace them. A missing DESIGN.md does not mean there
  is no identity; read it from the code and the live product.
- **Product truth:** what it is, who it is for, the one action, the real proof (numbers, customers, photos,
  product UI). Never invent customers, quotes, logos, ratings or statistics.
- **What imagery truly exists:** the client's photos and product screenshots, free stock (Unsplash, Pexels,
  Pixabay - searchable with web access), and what you can draw in code. Never AI-generated images.
- **What the best work in the category looks like:** reference research on Awwwards / Behance (`studio-bar.md` §2)
  or the built-in hero/section library.
- **Stack:** detect from the project (package.json deps, framework config). Never assume one.
- **Language and script:** Cyrillic, Latin, both? This filters fonts and changes line lengths (Russian text runs
  10-20% longer than English).

If the brief is vague, state your reading in one line and proceed. Ask only when a missing fact blocks the work
(no product name, two readings that produce opposite work).

## 3. Inventory the subject

Write 8-12 things that belong to this client and no competitor:
- its **name** and what the name means or sounds like;
- its **place**: address, street, city, neighbourhood, the light and weather, shop-front lettering, materials;
- its **numbers**: seats, minutes, year founded, price, batch size, capacity;
- its **constraint**: open only in winter, by appointment, one batch a month, hand-made, 24/7;
- its **materials and colours**: wood, steel, ceramic glaze, paper stock, the paint of its street;
- its **rituals and hours**: the oven lit at five, the ferry at seven, the Friday release;
- its **artefacts**: ticket, label, receipt, menu, timetable, manual, invoice, packaging, certificate;
- its **output**: what the product produces (a report, a photo, a sound, a meal, a deployment).

This list is where the idea comes from, and it doubles as your image search queries.

## 4. Find the idea

Fill both blanks from the inventory, not from the category:

> On this page, **[something that belongs to the subject]** becomes **[the device the composition uses]**.

Places to look: its output put on the page as material; its object enlarged or cropped into the frame; its name
set so the letters carry the layout; its place shown as the one view that makes you want to be there; its ritual
performed as the scroll; its printed artefact used as the page's structure (a menu that is a real menu, prices as
menu lines); its opposite (borrow the feeling another category owns).

**Subjects are not clichés.** Refuse the category's cheap *execution*, never its *subject*: a coffee shop's page is
full of coffee (photos, crema, beans, cups, the bar) shown in this brand's own way. The 3-second test
(`studio-bar.md` §3) must pass.

**The competitor test.** Put the nearest real competitor in the sentence. If it still works, the idea belongs to
the category ("a loaf of bread" is every bakery; "the seven doors of the street it is named after" is this one).
"Clean and modern" is not an idea.

**One live thing (Persuade/Experience).** Give the page one thing the visitor can do or that differs each visit,
made from the idea and the real content: choose a wood and see the chair; type your name in the foundry's letters;
set the loan and read the real monthly payment; see whether the kitchen is open right now. Rules: real content,
works with a thumb, plain fallback without JS, never blocks reading, one thing - not a playground.

**Operate surfaces** get a **signature element** instead: one element only this product has, built from its own
objects (a deploy timeline for a CI tool, a sell-out strip for a bakery, pace groups as a unit chart for a running
club). The rest of the screen is a clean, standard product.

## 5. Derive candidate worlds (new brand or redesign)

1. Name the product's unique mechanism in one sentence, the audience's real scene (who, where, under what light),
   and what this first surface must prove.
2. Write down the page the category always ships and its predictable opposite - both are the rut.
3. From the audience's cultural world list **seven** concrete visual systems they know by heart (publications,
   notation, signage, packaging, instruments' documentation, identity programmes, places, rituals, pre-web
   artefacts). For each: one line why it resonates and can carry the mechanism, one line how it looks (ground,
   main colours, type voices, the one signature). Spread across at least three material families. On Operate
   surfaces never take the world from the tool the audience operates (a terminal, a cockpit) - it returns as a
   costume.
4. Turn the strongest 2-3 into complete directions and present them (names, palette chips, type, first-viewport
   sketch in words or ASCII, honest risk). Offer the category standard played straight as a quiet alternative;
   never recommend it, never sneak it in. The user picks; then commit fully.

For fast work (the user wants results now) do steps 1-3 privately and present one committed direction with one
line on the alternatives you rejected.

## 6. Commit the world

**Colour strategy - choose before choosing colours:**
- *Restrained*: tinted neutrals + one accent (common on Operate/Read; the accent marks the action and data).
- *Committed*: one saturated colour carries 30-60% of the surface.
- *Full palette*: 3-4 named roles doing real jobs (editorial, kids, cultural).
- *Drenched*: the surface IS the colour; sections are full fields with their own ink.
Persuade and Experience have permission for the bolder strategies. Colour commits at page scale: whole fields,
not accents sprinkled on grey.

**Light or dark** is never picked by category ("dark because dev tool", "light because health"). Write one
sentence of physical scene - who uses this, where, under what light - and let it decide.

**Type** - choose faces like objects from the subject's world (procedure in `typography.md`). Operate and Read
surfaces are well served by workhorse UI faces; Persuade/Experience want faces with a point of view.

**Shape language** must agree with type and brand: pill/rounded = friendly; 8-12px = warm professional; 2-4px =
precise; 0 = technical/serious. One radius logic everywhere (nested radii step down: inner = outer - padding).

**Decoration level:** minimal (type does the work) / intentional (one texture, grain or material) / expressive
(layered depth, pattern). **Motion level:** functional / intentional (one authored moment) / expressive
(choreographed scenes). Persuade and Experience default to **intentional-to-expressive** on both axes; minimal is a
choice the brief must ask for. Check coherence: brutalist + bouncy motion clash; drenched colour + zero decoration
feels unfinished.

**One wow, a rich supporting layer.** The first screen carries the strongest move (`studio-bar.md` §4); every other
section is rich and crafted - pictures, icons, the graphic language, a detail that rewards attention - but none
competes with the hero, and none sits on top of reading text. Before shipping, check two things: remove one
accessory that does no job, and add a visual wherever a section is bare.

## 7. Calibration: the looks that mean you stopped deciding

Generated interfaces cluster regardless of subject. Each is legitimate when the brief asks for it; landing in one
when the axis was free means the self-check failed:

1. **Cream + serif + terracotta**: warm off-white ground (~#F4F1EA), high-contrast or italic serif display,
   rust/clay accent (~#D97757). The "warm editorial" remedy that became the most recognisable AI look.
2. **Near-black + one neon**: #0B0B0B ground, acid green/vermilion/cyan accent, glowing edges and radial halos.
3. **Broadsheet cosplay**: hairline rules everywhere, zero radius, dense columns, tiny tracked mono labels,
   italic display serif.
4. **SaaS card kit**: violet/indigo gradients, three identical icon-in-tinted-circle feature cards, one 12-16px
   radius on everything, the same soft grey shadow, gradient washes, glass panels, pill badge above a centred
   headline, "Get started" + "Learn more".
5. **Template chrome**: tracked uppercase eyebrow above every heading, 01/02/03 numbering on non-sequences,
   meta strings with middle dots, "→" appended to every link, monospace captions as a "technical" costume.

Tests: could someone guess your look from the category alone? From "the category, but avoiding the obvious"?
(The opposite failure counts too: avoiding the category so hard that the subject disappears.)
Either way, rework. A bookish or warm subject does not license cream: book cloth, thread and jackets come in every
saturated colour. Full list of tells and replacements: `anti-slop.md`.

**Removal is not enough.** A page with every tell removed and nothing put in their place is an empty page with good
manners. Fill the space with scale, real pictures of the subject's world, complete content, and whole fields of
colour - never with another ornament.

## 8. The direction contract

Write it before code (in your notes or the project's DESIGN.md draft), ~150 words, six blocks:

```
ROLE:          Senior UI/UX & Web Designer, astudio.one - a well-paid commission, award-level bar
REFERENCES:    3-8 links (Awwwards/Behance) or built-in patterns, and what is taken from each
THESIS:        the one idea this surface owns, and the category-default arrangement it refuses
OWN-WORLD:     palette (named hexes + strategy), type (faces + roles), shape, material - recognisable with content removed
STORY:         what the visitor understands, believes and does, in order
FIRST VIEWPORT: exact composition - what is where, at what scale, where the primary action sits
SIGNATURE:     the wow move of the first screen (live thing / signature element / motion moment)
RICHNESS:      photo set (queries, count), icon set, graphic language (devices from the logo), per-section visual anchor
FINISH:        "done = rendered at 1440/768/390, critiqued, top issues fixed, tokens + DESIGN.md delivered"
```

If a block reads like a mood ("modern, clean, premium"), the direction is not decided yet. The final review audits
the render against this contract.

## 9. When the brief pins a look

The brief wins. Honour pinned aesthetics, eras, materials, fonts and palettes even when they match a calibration
look above - the warning applies only to axes the brief left free. A pinned world pins the world, not its softest
rendition: use its full material range. If a brand requires a device this skill normally refuses (a gradient logo,
a violet primary), keep the brand asset, say so in the delivery notes, and pass `--allow <rule>` to `lint.py`.
