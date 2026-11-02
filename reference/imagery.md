# Imagery and assets

A rich, recognisable page is built from real pictures of the subject plus a code-made graphic language. One dominant
image per screen leads; supporting images, icons and graphics fill the page so no section is bare
(`studio-bar.md` §5).

**Hard rule: never generate photos or images with AI image models** (Midjourney, DALL·E, Imagen, Flux, Stable
Diffusion, "nano banana" or any other), even if such a tool is available in the session. Photos come from the client
or from free stock; everything else is drawn with code.

## Order of preference
1. **The project's own** photos, product shots, real product UI.
2. **Free stock photos and videos** of the subject's world: Unsplash, Pexels, Pixabay (free commercial use, no
   attribution required), Coverr / Pexels / Pixabay video; then Openverse and Wikimedia Commons (CC0 / CC-BY /
   public domain), museum open-access (The Met, Art Institute of Chicago, Rijksmuseum - CC0), old maps and engravings.
   Search procedure in `studio-bar.md` §7: 3-5 English queries from the subject inventory, download into the project,
   one coherent set of 6-12 images with one grade, record title / author / licence / URL in `assets/CREDITS.md` and
   the report. A stock picture shows the world around the client - never present it as the client's own product,
   room, dish or team; list it for replacement with real photos.
3. **Drawn in code** - illustrations, icon sets, patterns, stickers, maps, generative art (Canvas/WebGL shaders),
   procedural 3D - in one consistent graphic language built from the logo's geometry and the subject's objects, in
   the palette's real colours. Crafted, layered, with depth: not clip-art, not doodles, not shape-assembled stand-ins
   for photographic subjects.
4. **Type and colour alone** - only when the brief asks for a type-led page; a physical business always shows its
   subject.

Software products: the strongest picture is the product itself - build interface fragments in HTML/CSS as a real
piece of the app (real-looking data that adds up, one finding stated), marked `data-ui`, cropped like a photograph.
Never grey bars and lorem numbers.

## Treatment
- Same crop ratios and one grade across the page; square corners unless the direction says otherwise.
- Hero media covers ≥ ~50% of the first screen (photo, illustration, 3D or live canvas) - see `studio-bar.md` §4.
- Nothing lies on top of a headline; text over a photo needs a calm region or a scrim.
- Video: muted, looped, `playsinline`, poster frame, < ~2MB hero, paused off-screen and under reduced motion; prefer
  `<video>` over GIF.
- Performance: `width`/`height` or `aspect-ratio` on every image (CLS), AVIF/WebP with `srcset`/`sizes`,
  `loading="lazy"` below the fold, `fetchpriority="high"` on the hero image, a ground colour sampled from the image so a
  slow load opens onto its own colour.

## Icons
Every Persuade page has an icon system (features, amenities, steps, contacts, menu categories, dietary marks).
One library, one stroke weight, one corner style (Lucide, Phosphor, Tabler, Heroicons, Material Symbols; SF Symbols on
iOS). Standard glyphs for solved concepts (gear settings, magnifier search, bell notifications, trash delete). Icons
only where scanning pays off (nav, status, row types); text labels when the meaning isn't instant. Never emoji as
icons. Decorative icons `aria-hidden`; icon-only buttons labelled. Pin the icon package version.
Database: `search.py "<concept>" -d icons`.

## Licences in one line each
CC0 / public domain: free, no credit needed. CC-BY: free with credit. CC-BY-SA: credit + share-alike (avoid for brand
assets). CC-NC: no commercial use (avoid for client work). Unsplash/Pexels licences: free commercial use, no
redistribution as a stock collection. Google Fonts (OFL): free incl. logos. When unsure, do not use it and say so.

## Reporting
List every found picture/clip with title, creator, licence, source URL and where its credit sits; which drawings and
stock images stand in for client photography; and every sample content item to replace before launch.
