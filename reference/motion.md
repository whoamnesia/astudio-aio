# Motion

Motion is the last pass - a static page that needs animation to look finished is not finished. Every animation must
answer "why does this move?": spatial continuity, state change, feedback, explanation, preventing a jarring change,
or the page's one signature moment.

## Contents
1. Should this animate at all? (frequency gate)
2. Tokens: curves and durations
3. Budget per surface
4. Recipes (CSS-first)
5. Springs and gestures
6. Scroll-driven motion and GSAP
7. Reduced motion
8. Performance
9. Tells

## 1. Frequency gate
| How often seen | Decision |
|---|---|
| 100+ times/day (keyboard actions, command palette, typing) | no animation, ever |
| tens of times (hover, list navigation, tabs) | remove or keep tiny (≤ 150ms, colour/opacity) |
| occasional (menus, modals, drawers, toasts) | standard animation |
| rare / first time (onboarding, celebration, hero load) | can take its time and delight |

## 2. Tokens
```css
:root {
  --ease-out:   cubic-bezier(.22, 1, .36, 1);     /* entrances, moving hovers, UI < 600ms */
  --ease-expo:  cubic-bezier(.16, 1, .3, 1);      /* reveals ≥ 800ms, line rises, openings */
  --ease-in-out:cubic-bezier(.76, 0, .24, 1);     /* things travelling on screen, wipes, panels */
  --ease-drawer:cubic-bezier(.32, .72, 0, 1);     /* iOS-like sheets/drawers */
  --ease-exit:  cubic-bezier(.55, .055, .675, .19);/* leaving for good, short */
  --t-press: 140ms; --t-hover: 180ms; --t-ui: 240ms; --t-modal: 320ms; --t-reveal: 800ms; --t-open: 1200ms;
  --stagger-item: 60ms; --stagger-line: 90ms;
}
```
- Entering/leaving: ease-out (movement starts the instant the eye arrives). Moving between two places: ease-in-out.
  Colour/opacity hover: `ease`. Constant travel (marquee, progress, spinners): linear. **Never ease-in on UI** - it
  delays the first frames, the exact moment the user watches.
- Durations: press 100-160ms; tooltip 125-200; dropdown/popover 150-250; modal/drawer 200-500; UI over 300ms needs a
  reason; reveals 600-1000; picture openings 1100-1600. Exit ≈ 60-70% of enter.
- Staggers: 30-80ms between items, 75-120ms between lines, 20-40ms between characters (only for 1-3 word headings).
  At most 4 steps in a sequence.
- Overshoot/bounce only when a gesture threw the element (a flick); never on menus or buttons.
- Personality matters: a playful product may be a bit springier; a professional dashboard crisp and fast.

## 3. Budget per surface
**Persuade/Experience page:** one signature move (masked headline rise, image shutter, scaling wordmark, pinned
story, index with preview, opening window, ink-fill statement, rolling figures...) chosen from the subject; section
entrances choreographed per content type (list arrives row by row, picture opens from a mask, figure counts up once)
staggered 60-90ms, rising 12-32px, fired once at ~85% viewport; feedback on every control; moving pictures muted,
with posters, paused off-screen. Load sequence: ≤ 4-5 elements, settled by ~1.5s, content painted on the first frame.
Award-level extras allowed when crafted for the brand (`studio-bar.md` §8): parallax layers, pinned story (≤ 3
screens), horizontal gallery, marquee of real items, magnetic buttons, a custom cursor on fine pointers, Lenis
smooth scroll on desktop, a branded preloader < 1 s only while real assets load. Never: scroll that traps, content
hidden until an animation finishes, gates.
**Operate screen:** motion is feedback only - press, hover, focus, menu/sheet opening from its trigger, a row arriving,
skeleton → content without layout shift. Nothing performs an entrance.
**Mobile app:** spatial transitions (push/pop direction, sheets from the bottom, shared-element continuity), springs
for gestures, haptics paired on the same frame for meaningful moments.

## 4. Recipes
Gate hidden states so content shows without JS: `<script>document.documentElement.classList.add('js')</script>`.

```css
/* Press feedback (any pressable) */
.btn { transition: transform var(--t-press) var(--ease-out), background-color var(--t-hover) ease; }
.btn:active { transform: scale(.97); }
@media (hover: hover) and (pointer: fine) { .btn:hover { background: var(--color-primary-hover); } }

/* Enter without JS state (popovers, toasts) */
.toast { transition: opacity 300ms var(--ease-out), transform 300ms var(--ease-out);
  @starting-style { opacity: 0; transform: translateY(8px); } }

/* Origin-aware popover (not for modals - those stay centred) */
.popover { transform-origin: var(--transform-origin, top left); }
.popover[data-state=closed] { opacity: 0; transform: scale(.96); }

/* Masked headline line rise (author the line breaks) */
.lines .line { display: block; overflow: hidden; padding-bottom: .08em; margin-bottom: -.08em; }
@media (prefers-reduced-motion: no-preference) {
  .js .lines [data-line] { display: block; transform: translateY(105%);
    animation: rise 900ms var(--ease-expo) forwards; animation-delay: calc(var(--i) * 100ms + 120ms); }
}
@keyframes rise { to { transform: none; } }

/* Reveal once on scroll */
@media (prefers-reduced-motion: no-preference) {
  .js [data-reveal] { opacity: 0; transform: translateY(24px);
    transition: opacity 700ms var(--ease-out), transform 900ms var(--ease-out); }
  .js [data-reveal].is-in { opacity: 1; transform: none; }
}
```
```js
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }),
  { rootMargin: '0px 0px -12% 0px', threshold: .1 });
document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));
```
```css
/* Image shutter */
.shutter { overflow: clip; }
@media (prefers-reduced-motion: no-preference) {
  .js .shutter { clip-path: inset(0 0 100% 0); transition: clip-path 1100ms var(--ease-in-out); }
  .js .shutter img { transform: scale(1.12); transition: transform 1500ms cubic-bezier(.33,1,.68,1); }
  .js .shutter.is-in { clip-path: inset(0); } .js .shutter.is-in img { transform: none; }
}
/* Scroll-linked drift, CSS only (static where unsupported) */
@supports (animation-timeline: view()) { @media (prefers-reduced-motion: no-preference) {
  .drift { animation: drift linear both; animation-timeline: view(); animation-range: entry 0% exit 100%; }
  @keyframes drift { from { transform: translateY(-4%) } to { transform: translateY(4%) } } } }
```
Notes: `overflow: hidden` creates a scroll container that breaks `view()` timelines - use `overflow: clip`. Hold-to-
confirm: slow linear fill while pressed (2s), snappy release (200ms ease-out). Crossfades that look like two objects
swapping: add `filter: blur(2px)` mid-transition. Never animate from `scale(0)` - start at 0.95 + opacity 0.
CSS transitions are interruptible (good for rapidly re-triggered UI); keyframes restart from zero.
Page-to-page: View Transitions API, ≤ 480ms, off under reduced motion.

## 5. Springs and gestures
- Springs for anything a user can touch or interrupt: drags, sheets, swipes. They start from the current value and
  keep velocity when re-targeted. Apple-style params: damping 1.0 (no bounce) by default; ~0.8 only after a flick.
  Motion: `{ type: 'spring', bounce: 0, duration: .4 }`; momentum: `bounce: .2`.
- Respond on pointer-down, not click; track 1:1 with the finger respecting the grab offset; `setPointerCapture`.
- Dismiss on velocity (> ~0.11 px/ms) as well as distance; project momentum to choose the snap point.
- Rubber-band at boundaries instead of hard stops; ignore extra touch points mid-drag.
- Native CSS springs: `linear()` easing approximates a spring curve when JS is not wanted.
- In Motion (Framer), `x`/`y` shorthands animate on the main thread; use a full `transform` string or CSS for
  predetermined animations under load.

## 6. Scroll-driven motion and GSAP
GSAP 3.13+ is free including all plugins (ScrollTrigger, SplitText, Flip, MorphSVG, ScrollSmoother).
```js
gsap.registerPlugin(ScrollTrigger);
const mm = gsap.matchMedia();
mm.add('(prefers-reduced-motion: no-preference)', () => {
  gsap.from('[data-rise]', { y: 24, opacity: 0, duration: .8, ease: 'expo.out', stagger: .08,
    scrollTrigger: { trigger: '[data-rise]', start: 'top 85%', once: true } });
  gsap.to('.hero-media', { yPercent: 8, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
});
```
- Scroll-linked = linear and locked to the scrollbar (scrub true, or 0.3-0.8 smoothing at most).
- Pins cost length: ≤ 2 held stages per page, ~1 screen per step, ≤ 3 screens per stage, every held screen carries
  text. Parallax travel < 8% of the element; scale between 0.94 and 1.15.
- Smooth-scroll libraries (Lenis) optional, off for touch and reduced motion; never let the page keep sliding after
  the hand stops.
- In React use `useGSAP()` (from `@gsap/react`) for automatic cleanup; in SPAs kill ScrollTriggers on unmount.
- Motion budget: ≤ 3 scroll-triggered pattern families per page and one primary wow peak.

## 7. Reduced motion
`prefers-reduced-motion: reduce` = fewer and gentler, not zero: keep opacity/colour changes that aid comprehension,
drop travel, scale, parallax, autoplay and elastic effects. Write hidden states inside
`@media (prefers-reduced-motion: no-preference)` so the reduced page is simply the finished page. Also honour
`prefers-reduced-transparency` (frost/solidify glass) and `prefers-contrast: more`. Autoplay motion > 5s needs
pause/stop. Loops pause off-screen (IntersectionObserver) and when the tab is hidden.

## 8. Performance
- Animate only `transform`, `opacity` (and small `clip-path`/`filter`). Never width/height/top/left/margin/padding
  (accordion `grid-template-rows` is the accepted exception).
- Do not drive many children from one changing CSS variable on a parent; set transforms on the moving element.
- `will-change` only right before an animation, removed after. Blur ≤ 8px animated, never on large surfaces.
- No scroll listeners for animation - IntersectionObserver, ScrollTrigger or `animation-timeline`.
- Measure once, animate via transform (FLIP) instead of reading layout every frame.
- Test at DPR 2 on a production build; dev servers lie.

## 9. Tells
Same fade-up on every block; a dozen hero entrances; hover lift on every card; bounce easing; meaningless loops
(pulsing dots, floating shapes, shimmer); reveals that never fire leaving blank bands; content held at low opacity;
motion crossing text being read; long preloaders and scroll-jacked tours. (The opposite tell: a Persuade page with
no motion moment at all.)
