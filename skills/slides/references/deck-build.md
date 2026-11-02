# Building the HTML deck

## Template
```html
<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Deck — Brand</title>
<link rel="stylesheet" href="../design-tokens/tokens.css">
<link href="https://fonts.googleapis.com/css2?family=…&display=swap&subset=cyrillic" rel="stylesheet">
<style>
  html, body { margin: 0; height: 100%; background: #000; }
  .deck { position: fixed; inset: 0; display: grid; place-items: center; }
  .slide { position: absolute; width: 1920px; height: 1080px; box-sizing: border-box; padding: 96px 120px;
           background: var(--color-ground); color: var(--color-ink); font: 400 28px/1.4 var(--font-body);
           display: none; transform-origin: center; }
  .slide.is-current { display: grid; }
  .slide h2 { font: 600 72px/1.05 var(--font-display); letter-spacing: -.02em; margin: 0; max-width: 22ch; text-wrap: balance; }
  .slide .meta { position: absolute; left: 120px; right: 120px; bottom: 48px; display: flex; justify-content: space-between;
                 font-size: 18px; color: var(--color-muted); }
  .slide.field { background: var(--color-primary); color: var(--color-on-primary); }
  .notes { display: none; }
  body.show-notes .notes { display: block; position: fixed; bottom: 0; left: 0; right: 0; max-height: 30vh; overflow: auto;
         background: #111; color: #eee; font: 16px/1.5 system-ui; padding: 16px 24px; z-index: 9; }
  @media print { @page { size: 1920px 1080px; margin: 0; } html, body { background: none; }
    .deck { position: static; display: block; } .slide { position: relative; display: grid !important; transform: none !important;
    break-after: page; } .notes { display: none !important; } }
  @media (prefers-reduced-motion: no-preference) { .slide.is-current > * { animation: in .5s cubic-bezier(.22,1,.36,1) both; }
    @keyframes in { from { opacity: 0; transform: translateY(12px); } } }
</style></head><body>
<main class="deck" aria-live="polite">
  <section class="slide" data-layout="title">…<aside class="notes">Speaker notes…</aside><div class="meta"><span>Brand</span><span class="n"></span></div></section>
  …
</main>
<script>
const slides = [...document.querySelectorAll('.slide')]; let i = Math.max(0, +location.hash.slice(1) - 1 || 0);
function fit() { const s = Math.min(innerWidth / 1920, innerHeight / 1080); slides.forEach(el => el.style.transform = `scale(${s})`); }
function show(n) { i = Math.max(0, Math.min(slides.length - 1, n)); slides.forEach((el, k) => el.classList.toggle('is-current', k === i));
  slides[i].querySelector('.n') && (slides[i].querySelector('.n').textContent = `${i + 1} / ${slides.length}`); history.replaceState(null, '', '#' + (i + 1)); }
addEventListener('keydown', e => { if (['ArrowRight', 'PageDown', ' '].includes(e.key)) show(i + 1);
  if (['ArrowLeft', 'PageUp'].includes(e.key)) show(i - 1); if (e.key === 'Home') show(0); if (e.key === 'End') show(slides.length - 1);
  if (e.key.toLowerCase() === 'n') document.body.classList.toggle('show-notes'); if (e.key.toLowerCase() === 'f') document.documentElement.requestFullscreen?.(); });
let x0 = null; addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) show(i + (dx < 0 ? 1 : -1)); x0 = null; });
addEventListener('click', e => { if (!e.target.closest('a,button')) show(i + (e.clientX > innerWidth / 2 ? 1 : -1)); });
addEventListener('resize', fit); fit(); show(i);
</script></body></html>
```
For PDF export all slides must be visible: the print CSS shows every `.slide`; run
`node <root>/scripts/render.cjs pdf deck.html --out deck.pdf --width 1920 --height 1080`.

## Layouts (vary them; same positions for headline, logo, page number)
- **Title** - the claim of the whole deck in display type, left-aligned on the ground or a brand field; presenter and
  date small.
- **Statement** - one sentence at 56-72px, lots of air (section openers, the core insight).
- **Claim + chart** - takeaway headline top-left, one chart (≥ 60% of the slide), the key point annotated on the chart.
- **Big number** - one real figure very large with its context line and source.
- **Split** - headline + 2-4 short lines on the left, image/product UI on the right (full-bleed to the edge).
- **Comparison** - two columns or a real table (us vs alternative / before vs after), the winning column emphasised by
  weight, not by colour alone.
- **Process / timeline** - only for real sequences; 3-5 steps with what changes at each.
- **Quote** - real quote with name, role, photo (permission); set as `<blockquote>`, ≤ 25 words.
- **Team** - photos with names, roles and one relevant credential each.
- **Pricing / ask** - the offer or the ask (amount, use of funds, milestones) stated plainly.
- **Section break** - full brand colour field, section title, nothing else.
- **Closing** - the one action (with contact/QR) - not "Thank you / Questions?" alone.

## Charts
Chart.js (pin a version) or inline SVG. Configure: one series (or two max), brand primary on the key series, neutrals
for context, gridlines faint, no legend for one series, direct labels, axis ticks ≥ 16px at 1920, the finding annotated,
animations off under reduced motion. Data real and sourced.

## Typography at presentation scale (1920×1080 canvas)
Display/headlines 56-96px · body 28-36px (never < 24) · labels/data 18-24px · source/footer 16-18px. Two faces max.
Line length ≤ 60 characters. Russian headlines are longer - budget accordingly or use a condensed display face.
