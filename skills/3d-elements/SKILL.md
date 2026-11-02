---
name: 3d-elements
description: >-
  astudio 3D in web design: add 3D models, objects, scenes and effects into an existing or new design exactly where the
  user wants them - using only free, properly licensed assets (Poly Haven, Kenney, Quaternius, Poly Pizza, Sketchfab
  CC0/CC-BY, Smithsonian, NASA, 3dicons, pmndrs market…) or fully original procedural 3D built in code (Three.js / React
  Three Fiber geometry and shaders, CSS 3D transforms, SVG pseudo-3D) - matched to the brand's design code, performant
  on phones, accessible, with static fallbacks. Use when the user asks for 3D, a 3D hero, a rotating product/logo,
  interactive object, configurator, WebGL/Three.js/R3F/Spline scene, shader background, "добавь 3D", "3D-модель на
  сайт", "объёмный логотип", "3D-элементы", "интерактивная 3D-сцена". Part of astudio-aio.
argument-hint: "[what object/scene] [where on the page] [interaction]"
---

# astudio · 3D elements

Role: Senior 3D & creative web developer at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

3D earns its place when it shows something better than a picture can: an object the visitor can turn, a product
explained by moving it, a material that reacts, a scene that carries the page's idea. It fails when it is a slow,
decorative screensaver. Decide that first.

Shared: `<root>` = two levels above this skill's base dir. Inherit the design code (DESIGN.md / tokens) for colours,
materials, light mood and motion curves. Local references: `references/sources-licensing.md` (free asset sources,
licences, credits, pipeline), `references/threejs-r3f.md` (scene recipes: vanilla Three.js and R3F, GLB loading,
lighting/HDRI, materials, interaction, scroll), `references/procedural.md` (original 3D in code: geometry, shaders,
CSS 3D, SVG pseudo-3D, 3D logo), `references/performance-a11y.md` (budgets, fallbacks, reduced motion). Database:
`search.py "<object or style>" -d 3d-source`, `search.py "<concern>" --stack threejs`.

## Decide (before any code)
1. **Purpose** in one line: what does 3D show that a still can't? (turn the product; see the material; feel the place;
   play with the logo). No answer → recommend a strong photograph or drawn illustration instead and say why.
2. **Placement and size**: exactly where the user asked (hero object, section scene, card accent, background field,
   logo mark, configurator). Respect the layout: text never sits on top of busy 3D; leave a calm region or move text.
3. **Interaction**: none (ambient, very subtle) / pointer-reactive (tilt, parallax ≤ a few degrees) / drag-to-rotate
   (OrbitControls with limits) / scroll-driven (camera or object tied to scroll, linear, locked to scrollbar) /
   configurator (materials/colours/parts switchable, with plain HTML controls). One interaction model per scene.
4. **Asset route**:
   - *Free model* matching the brief → find it (`references/sources-licensing.md`), check licence (CC0 preferred;
     CC-BY requires visible credit; avoid NC/ND/"NoAI"), download into the project, record title/author/licence/URL.
   - *Original* → build procedurally (`references/procedural.md`): abstract forms, the logo extruded, product-like
     primitives, particles, shader fields - the default when no honest free asset fits or the object must be ownable.
   - *Spline* when the user already uses it or wants designer-editable scenes (embed via `@splinetool/runtime`).
   Never pass off a found model as the client's real product.
5. **Stack**: plain page → Three.js (ES modules from a pinned CDN or npm); React → React Three Fiber + drei; quick
   designer scenes → Spline; tiny decorative depth → CSS 3D / SVG (no WebGL at all).

## Build
1. Match the brand: colours from tokens (convert to linear correctly - set `colorSpace`), materials that fit the world
   (matte clay, brushed metal, frosted glass, paper), lighting mood (soft studio HDRI from Poly Haven, or 1 key + fill +
   rim), background transparent or the page ground so the canvas melts into the layout.
2. Scene recipe from `references/threejs-r3f.md`: renderer with `setPixelRatio(min(dpr, 2))`, `outputColorSpace` sRGB,
   ACES/AgX tone mapping, resize handling, `setAnimationLoop`, pause when off-screen (IntersectionObserver) or tab hidden,
   dispose on unmount.
3. Optimise assets: GLB with Draco or Meshopt compression, KTX2/WebP textures sized to screen use, baked lighting/AO
   where possible, instancing for repeats, total hero 3D payload target ≤ ~2-3 MB, triangles ≤ ~100-300k for a hero on
   mobile (`references/performance-a11y.md`).
4. Loading: show the static poster (a rendered still of the scene, same composition) immediately; fade the canvas in
   when ready - never a blank hole or a blocking preloader. Errors and no-WebGL → the poster stays.
5. Accessibility: the canvas is decorative (`aria-hidden`) or has a text alternative describing what it shows;
   interactions also available via buttons/keyboard (rotate left/right, reset, next material); focusable controls
   outside the canvas; `prefers-reduced-motion` → static pose (no auto-rotate, no scroll-scrub); never trap scroll.
6. Integrate with motion: entrance via the page's curves (expo-out), GSAP ScrollTrigger for scroll scenes (scrub
   linear), no competing animations around it.

## Verify
`node <root>/scripts/render.cjs shots <page> --widths 1440,390` (WebGL renders in headless Chromium; if the canvas is
blank in the screenshot, check console errors in report.json); test with `--reduced-motion`; measure FPS/draw calls
(`renderer.info`) and payload; check the phone composition; confirm credits are on the page (footer/credits section) for
CC-BY assets. Report: purpose, asset sources + licences, performance numbers, fallbacks, what to replace.
