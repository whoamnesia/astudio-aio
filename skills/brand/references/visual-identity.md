# Visual identity system

## 1. Logo usage (from the logo kit)
Variants (horizontal, stacked, symbol, wordmark; colour, reversed, mono), clear space from a logo element, minimum
sizes, approved backgrounds, misuse examples, co-branding. See `<root>/skills/logotype/references/kit.md` §1-2.

## 2. Colour
Roles and proportions (`<root>/reference/color.md`). Document as a table: descriptive name (#HEX · RGB · OKLCH) ·
role · where used · contrast against its usual ground. Include dark-mode values. Optional for print: CMYK and Pantone
suggestions marked "verify with printer". Colour strategy named (Restrained / Committed / Full / Drenched) with the
share rules. Section field colours with their own inks when the brand uses fields.

## 3. Typography
Faces with roles, source and licence, weights used, Cyrillic support; the fluid scale (min-max px per step);
tracking/leading per step; paragraph measure; numerals (tabular for data); case rules; language-specific typography.
Extending a thin brand typeface: keep the brand face for display; add a complementary text face that matches its shape
logic (geometric with geometric, humanist with humanist); never a third family.

## 4. Shape language and depth
| Shape | Tone | Typical use |
|---|---|---|
| pill / fully round | friendly, approachable | consumer, health, kids, social |
| 8-12px | warm professional | SaaS, productivity, B2B |
| 2-4px | precise, structured | enterprise, finance, data |
| 0 | technical, serious, editorial | dev tools, security, industrial, fashion |
Read the logo: its corners and terminals set the radius logic. Larger surfaces read sharper - modals/large cards may
take a larger radius than buttons; wells/background regions smaller. Nested radius = outer − padding (concentric).
Depth: decide borders OR tone steps OR shadows per layer; shadows only for what floats (menus, dialogs, popovers);
brand-tinted shadow colour (`hsla(<brand hue> 15% 5% / α)`), never pure black glows.

## 5. Iconography
One library + one stroke weight + one corner style matching the shape language: thin 1-1.5px (refined, luxury,
editorial), regular 2px (general product), bold 2.5-3px (consumer, accessibility-first), filled (status, mobile nav).
Standard glyphs for solved concepts; verb icons only on actions; pin the package version. Custom icons follow the
logo's construction grid.

## 6. Imagery and graphic devices
Photo direction: subject (the real product, place, people at work), light (natural/hard/studio), colour treatment
(untouched / one grade / duotone in brand colours), crop ratios, what never to show (staged stock handshakes,
generic laptops). Illustration (if any): one style derived from the brand's geometry, palette-limited. Graphic device:
a pattern, crop, frame or motif built from the logo (e.g. the mark's cut repeated as a section divider shape, the
counter as a mask for photos) - one device, used with discipline. Motion signature: how the brand moves (from
`reference/motion.md`), e.g. "panels open like the logo's fold, 600ms expo-out".

## 7. Auditing and extending an existing brand
- Read the guide's scope: print-first guides break on screens (pale greys at 2:1, unlicensable webfonts, hairlines).
- A deviation in the live product that a screen constraint explains (contrast, licence, rendering) is a finding - the
  guide needs updating. A deviation nothing explains is drift - the product needs correcting. Test per value.
- Older and newer pages from different design eras: the newest are the best evidence of current intent (confirm with
  the user); migrate old toward new, never average eras.
- Two or three independent occurrences of a treatment = a pattern: name it, tokenise it, document it.
- For software you cannot rewrite: logo + brand hue + typeface buy most of the recognition; map them onto existing
  variables (Bootstrap/Sass/Tailwind) before touching components.

## 8. Brand applications (pick those relevant to the business)
Web/app: favicon, app icon, header, OG/social images, email signature and header, social avatars and covers.
Office: business card, letterhead, envelope, invoice, presentation template, email template.
Retail/hospitality: signage, storefront decal, menu, packaging, labels, cups/bags, uniforms, receipts.
Events: badge, lanyard, banner, roll-up, stage screen, tickets. Vehicles, merch (t-shirt, tote, stickers).
`search.py "<application>" -d brand-application` lists 50 deliverables with specs.
