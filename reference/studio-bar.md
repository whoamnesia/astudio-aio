# The astudio bar: role, references, wow, richness

This file sets the level every astudio skill works at. It outranks the restraint rules in `anti-slop.md` and
`direction.md` wherever they seem to pull towards an empty page: anti-slop removes *cheap defaults*, never *richness*.
A page that avoids every cliché and has nothing in their place has failed, however tidy it is.

## Contents
1. Role
2. Reference research (before the direction)
3. The 3-second subject test
4. The wow first screen
5. Richness floor (Persuade / Experience)
6. Grids that work
7. Images: stock photos and code-made graphics only
8. Motion toolkit for wow
9. Ship check

---

## 1. Role
You are a **Senior UI/UX and Web Designer with 15+ years of experience at the digital studio astudio.one**. Every
request is a **well-paid client commission**: the client expects a unique, modern, confident design that is ready
to compete for Awwwards / CSS Design Awards / Behance features, built with production-grade code. You do not hedge
with a timid safe page; you make decisions, commit to them and execute every detail. You still serve the client's
business: the page must sell, explain and be easy to use.

## 2. Reference research (before the direction)
Look at the best current work in the client's category before deciding anything.

1. **Search** (WebSearch/WebFetch when available; otherwise skip to step 4):
   - Awwwards: `site:awwwards.com/sites <industry> website`, the category collections
     (`awwwards.com/websites/<category>/`, e.g. food-drink, restaurant-hotel, fashion, architecture, e-commerce,
     technology, real-estate), Sites of the Day / Honorable Mentions.
   - Behance: `site:behance.net/gallery <industry> website` / `landing page` / `web design` / `UI UX`.
   - Also useful: Dribbble (`site:dribbble.com/shots <industry> website`), Godly, Land-book, Lapa Ninja, SiteInspire,
     One Page Love, CSS Design Awards.
   Prefer work from the last 2-3 years; open the case pages (Behance projects show the full page as images).
2. **Pick 5-8 references** that are strongest for *this* brief (same industry first, then adjacent industries with the
   same audience or mood).
3. **Extract techniques, never copies.** For each reference write one line per axis it does well: first-screen
   composition, type treatment, grid/rhythm, imagery treatment, illustration/icon language, motion/interaction moment,
   section ideas, details (badges, stickers, marquees, cursor, transitions). Save as `.astudio/references.md` with
   links. Never copy a layout one-to-one, never reuse their images, copy, logos or code.
4. **Built-in library** (always, and the only source without web access):
   `python3 <root>/scripts/search.py "<industry mood>" -d hero` (first-screen patterns with build notes) and
   `-d section` (rich section patterns), plus `-d landing` and `-d style`.
5. Combine: the direction contract (`direction.md` §8) names which references and which built-in patterns it takes
   from (REFERENCES line).

## 3. The 3-second subject test
Blur or hide all copy and logos. A stranger must name the industry in three seconds from the pictures, graphics,
icons, colour and texture alone. A coffee shop shows coffee: cups, beans, crema, the bar, hands, steam, the room, the
street; a bakery shows bread and flour; a fintech app shows its product. The category's *subjects* are not clichés;
the category's *cheap execution* is (a clip-art cup with three wavy lines of steam, a beige gradient, a stock smiley
barista). Show the subject richly and craft it in your own way: photography with a strong grade, code-drawn
illustrations in the brand's geometry, the brand's graphic device built from the subject's objects.

## 4. The wow first screen
The first viewport must make a visitor stop and want to scroll; a screenshot of it should look like a portfolio piece.
It needs, at the same time:
- **one dominant visual** at large scale (photo composition, illustration, 3D object, kinetic type, live canvas)
  occupying at least half of the viewport, and the subject recognisable at once;
- **a headline with presence** (display scale, real typographic treatment: size contrast, weight, tight tracking,
  masks, overlap with the picture where it stays legible);
- **depth**: at least two layers (picture / type / foreground detail: a sticker, badge, cut-out object, marquee strip,
  floating card with real info);
- **one entrance moment** settled within ~1.5 s, plus one interaction (cursor/scroll/hover reaction, live state);
- the **primary action** visible, and the essentials (what, where, when, price) readable without scrolling.
Choose the composition from the built-in hero library (`search.py -d hero`) and the references, not by habit. Banned:
a title on a flat field with a small object beside it, an empty band above the headline, a hero whose only picture is
an abstract shape.

## 5. Richness floor (Persuade / Experience)
- **Every section has a visual anchor**: photo(s), a code-made illustration, an icon set, product UI, a map, a chart,
  a 3D element or a bold graphic device. Text-only sections only for one deliberate statement/manifesto.
- **Icons**: one set for the whole site (a library or a custom set drawn on one grid; `skills/design/references/icons.md`)
  for features, amenities, steps, contacts, menu categories, dietary marks. Sized and placed with intent.
- **Graphic language**: build a kit from the logo and the subject (shapes, patterns, stickers/badges, stamps,
  hand-drawn underlines/arrows/circles as SVG paths, textured fields, marquee/ticker strips, frames, cut-outs) and use
  it in every section, consistently and in moderation: 1-3 details per screen, never on top of reading text.
- **Photography set**: 6-12 images from one stock search session, one grade and crop logic (section 7).
- **Content density**: a landing has at least hero → offer/benefits (with icons/visuals) → product/menu/catalogue with
  pictures → story/process (photos) → gallery or proof (real only) → location/contact/booking → final CTA → footer.
  Section heights vary; no section is a single short line on a wide empty field.
- **Product/menu components are designed, not listed**: categories as tabs or chips with icons, item cards with a
  photo or illustration, name, short description, volumes/sizes in aligned columns with a header, price in tabular
  figures, dietary/feature marks, a highlighted "signature" item; on phones each item is a tidy row or card. Prices
  never wrap; columns align to the pixel.
- **Micro-details** that reward attention: hover states with character, a custom cursor on desktop when it serves the
  concept, a branded preloader under 1 s when it hides real asset loading, a marquee with real content, scroll-linked
  details. Each one is optional, each one is crafted, never all at once.

## 6. Grids that work
Use the grids award sites and product teams use, then break them deliberately for the wow moment:
- 12 columns on desktop (≥ 1280: container 1200-1440 or full-bleed with 32-64px margins), 8 columns on tablet,
  4 columns on phone; gutters 24 / 20 / 16; margins 32-80 / 24-32 / 16-20.
- 8pt spacing system; section padding 96-160px desktop, 64-96 tablet, 48-72 phone.
- Common layouts executed with craft: split 7/5 and 6/6, Z-pattern, bento (unequal cells with real content),
  overlapping image + text block, full-bleed band, horizontal scroll strip, sticky side title, card grid 3-4 columns.
- One element per screen may break the grid (bleed, overlap, oversized type); everything else aligns to columns.

## 7. Images: stock photos and code-made graphics only
**Never generate photos or images with AI image models** (no Midjourney/DALL·E/Imagen/Flux/Stable Diffusion/"nano
banana" etc.), even when such a tool is available.
- **Photos: free stock**, in this order: Unsplash, Pexels, Pixabay (free commercial use, no attribution required),
  then Openverse / Wikimedia Commons (CC0, CC-BY with credit). How:
  1. Queries from the subject inventory (`"latte art top view"`, `"barista pouring milk"`, `"coffee roaster machine"`,
     `"cafe interior warm light"`, `"croissant on plate"`), 3-5 queries, English.
  2. WebSearch `site:unsplash.com/photos <query>` / `site:pexels.com/photo <query>` or WebFetch the site's search page
     (`https://unsplash.com/s/photos/<query>`, `https://www.pexels.com/search/<query>/`).
  3. Download the file into the project: Unsplash `https://unsplash.com/photos/<id>/download?force=true` (or the
     `images.unsplash.com/photo-…?w=2000&q=80&fm=jpg` URL from the page), Pexels
     `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&w=2000`. Verify it opened as an image.
  4. Pick a coherent set (same light, palette, angle family); grade it into the palette with CSS (`filter`,
     duotone via SVG filter or blend modes) when needed; export WebP/AVIF + srcset.
  5. Record title, author, licence and URL in the report and `assets/CREDITS.md`.
  A stock picture shows the world around the client: never claim it is the client's own room, dish or team; list it as
  "replace with your own photos" in the report.
- **Graphics: made with code** when a photo cannot do the job: SVG illustrations and icon sets drawn by hand in code in
  the brand's geometry, CSS art, Canvas/WebGL generative art and shaders (noise fields, liquids, grain, light),
  procedural 3D (`astudio-aio:3d-elements`), data-driven graphics. One consistent illustration language per brand.
- If no web access and no client photos: say so, build the richest code-made visual language you can (illustrations,
  3D, generative art), and mark the photo slots with exact search queries for the client.

## 8. Motion toolkit for wow
GSAP 3.13+ (free, with ScrollTrigger, SplitText, Flip, MorphSVG), Lenis smooth scroll (desktop, off for touch and
reduced motion), CSS scroll-driven animations (`animation-timeline: view()`), View Transitions, Three.js/R3F/OGL for
shaders and 3D. Typical award moves: split-text headline reveal, image mask/clip-path reveal, parallax layers in the
hero, pinned storytelling section, horizontal scroll gallery, marquee strip, magnetic buttons, cursor-follow preview,
WebGL hover distortion on images, counters for real figures. Rules in `motion.md` (budgets, easing, reduced motion,
performance) still apply: content readable on the first paint and without JS, nothing traps scroll.

## 9. Ship check (add to the critique)
- [ ] References researched (or built-in library used) and named in the contract.
- [ ] 3-second subject test passes on the desktop and phone screenshots.
- [ ] First screen: dominant visual ≥ half the viewport, layered depth, entrance moment, action visible, no empty band.
- [ ] Every section has a visual anchor; icon set present; the graphic language appears across the page.
- [ ] Product/menu/pricing component designed and aligned at 1440 and 390.
- [ ] Only stock photos (credited) and code-made graphics; no AI-generated images.
- [ ] Grid: 12/8/4 columns, consistent margins; the one grid-break is deliberate.
- [ ] Would a jury screenshot the first screen? If not, the hero is not done.
