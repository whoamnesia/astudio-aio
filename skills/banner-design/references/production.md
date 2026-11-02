# Banner production

## Multi-size HTML template
```html
<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Campaign banners</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600;800&family=Onest:wght@400;600&display=swap&subset=cyrillic" rel="stylesheet">
<link rel="stylesheet" href="../design-tokens/tokens.css">
<style>
  body { margin: 0; padding: 40px; background: #777; display: flex; flex-wrap: wrap; gap: 40px; align-items: flex-start; }
  .banner { position: relative; overflow: hidden; flex: none; background: var(--color-ground); color: var(--color-ink);
            font-family: var(--font-body); container-type: size; }
  .banner h1 { font-family: var(--font-display); font-size: 9cqh; line-height: .95; letter-spacing: -.02em; margin: 0; text-wrap: balance; }
  .banner .cta { display: inline-flex; align-items: center; height: 7cqh; min-height: 44px; padding: 0 4cqw;
                 background: var(--color-primary); color: var(--color-on-primary); font-weight: 600; border-radius: 999px; }
  .guide { position: absolute; inset: 0; pointer-events: none; outline: 2px dashed rgb(255 0 0 / .6); outline-offset: -10%; }
  .export .guide { display: none; }           /* body.export hides safe-zone guides */
  #ig-post   { width: 1080px; height: 1350px; }
  #ig-story  { width: 1080px; height: 1920px; }
  #og        { width: 1200px; height: 630px; }
  #mpu       { width: 300px;  height: 250px; }
</style></head>
<body class="export">
  <section class="banner" id="ig-post">…<div class="guide"></div></section>
  <section class="banner" id="ig-story">…<div class="guide"></div></section>
  <section class="banner" id="og">…<div class="guide"></div></section>
  <section class="banner" id="mpu">…<div class="guide"></div></section>
</body></html>
```
Container query units (`cqh`, `cqw`) let type scale with each canvas; still re-compose per ratio family. Remove
`class="export"` while designing to see the safe-zone guides (set the guide inset per format from the data file).

## Export
```bash
node <root>/scripts/render.cjs element banners.html --selector ".banner" --out out/campaign.png --width 2400 --height 2400 --scale 1
node <root>/scripts/render.cjs element banners.html --selector ".banner" --out out/campaign@2x.png --width 2400 --height 2400 --scale 2
```
The viewport must be larger than the biggest banner. Files are named by each banner's `id`. Open every PNG and check
dimensions, crops, font rendering (fonts loaded? Cyrillic glyphs present?), and that nothing important is in an overlap
zone. Compress: `convert in.png -strip -quality 85 out.jpg` (ImageMagick) or keep PNG for flat graphics; display ads
usually ≤ 150 KB.

## Naming
`out/<campaign>/<format>-<width>x<height>[@2x].png`, date prefix for time-bound campaigns (`261101-ig-post-1080x1350.png`).

## Animated variants
HTML5 banners (GSAP timeline ≤ 15-30s, ≤ 3 loops, end frame = the static banner, clickTag per network spec) or MP4 for
social (render frames with Playwright or build in Remotion/HyperFrames if available). Static fallback always.

## Print
Physical size + 3-5 mm bleed on every side; key content ≥ 5 mm (A-sizes) / 20-50 mm (roll-ups) inside the trim; roll-up
85×200 cm: logo and headline in the top 2/3 (eye level 120-180 cm), nothing vital in the bottom 20 cm. Build at a
proportional pixel size (e.g. 2550×6000 for 85×200 cm at 75 dpi preview), export PDF via `render.cjs pdf` with the
physical aspect, then tell the user: final files need 150-300 dpi at full size and CMYK conversion/proofing by the
printer (RGB brand colours may shift - provide CMYK/Pantone suggestions from the brand kit).
