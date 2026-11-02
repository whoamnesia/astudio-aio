#!/usr/bin/env node
/* astudio render - look at what you built. Headless Chromium via Playwright.

Commands
  node render.cjs shots <url|file.html> [--widths 1440,768,390] [--out dir] [--no-full] [--reduced-motion]
       Screenshots (first screen + full page) per width, and a JSON report of measurable problems:
       horizontal overflow, h1 count, headings > 2 lines, text < 12px, missing alt, low-contrast text
       on flat backgrounds, fonts that failed to load, unlabeled buttons, images without size.
  node render.cjs element <file.html> --selector ".banner" --out banner.png [--scale 2] [--width 1600 --height 900]
       Exact-size PNG of one element (banners, social images, OG cards).
  node render.cjs svg <file.svg> [--sizes 16,32,64,180,512] [--out dir] [--bg transparent|#fff]
       Rasterise an SVG logo/icon at exact pixel sizes.
  node render.cjs pdf <file.html> --out deck.pdf [--width 1920 --height 1080]
       Print an HTML deck/one-pager to PDF (one page per .slide when present).

Requires Playwright with Chromium (`npm i -D playwright && npx playwright install chromium`).
If it is missing, the command prints how to install it and exits 2 - say so instead of claiming checks ran.
*/
const fs = require('fs');
const path = require('path');

function loadPW() {
  for (const m of ['playwright', 'playwright-core', '@playwright/test']) {
    try { return require(m); } catch (_) {}
  }
  try { return require(require.resolve('playwright', { paths: [process.cwd()] })); } catch (_) {}
  console.error('Playwright not found. Install: npm i -D playwright && npx playwright install chromium');
  process.exit(2);
}

function args(argv) {
  const o = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const k = a.slice(2);
      const n = argv[i + 1];
      if (n === undefined || n.startsWith('--')) o[k] = true; else { o[k] = n; i++; }
    } else o._.push(a);
  }
  return o;
}

function toURL(target) {
  if (/^https?:|^file:/.test(target)) return target;
  return 'file://' + path.resolve(target);
}

async function launch(pw) {
  const opts = {};
  if (fs.existsSync('/opt/pw-browsers/chromium')) {
    // preinstalled browser in some sandboxes; harmless elsewhere
  }
  try { return await pw.chromium.launch(opts); }
  catch (e) { return await pw.chromium.launch({ ...opts, args: ['--no-sandbox'] }); }
}

const AUDIT = () => {
  const out = { issues: [], stats: {} };
  const push = (sev, rule, detail) => out.issues.push({ sev, rule, detail });
  const vw = document.documentElement.clientWidth;
  if (document.documentElement.scrollWidth > vw + 1) push('FAIL', 'horizontal-overflow', `scrollWidth ${document.documentElement.scrollWidth} > ${vw}`);
  const h1 = document.querySelectorAll('h1');
  if (h1.length !== 1) push(h1.length ? 'WARN' : 'FAIL', 'h1-count', `${h1.length} h1 elements`);
  const all = [...document.querySelectorAll('body *')];
  const visible = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0; };
  let tiny = 0, sizes = new Set();
  const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p[3] === undefined ? 1 : p[3] }; };
  const lum = ({ r, g, b }) => { const f = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const bgOf = el => { let e = el; while (e) { const s = getComputedStyle(e); if (s.backgroundImage && s.backgroundImage !== 'none') return null; const c = parse(s.backgroundColor); if (c && c.a > 0.95) return c; e = e.parentElement; } return { r: 255, g: 255, b: 255, a: 1 }; };
  let lowC = [];
  for (const el of all) {
    if (!visible(el)) continue;
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (!hasText) continue;
    const s = getComputedStyle(el);
    const fs = parseFloat(s.fontSize); sizes.add(Math.round(fs));
    if (fs < 12) tiny++;
    const fg = parse(s.color), bg = bgOf(el);
    if (fg && bg) {
      const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
      const large = fs >= 24 || (fs >= 18.66 && +s.fontWeight >= 700);
      if (ratio < (large ? 3 : 4.5)) lowC.push(`${el.tagName.toLowerCase()} "${el.textContent.trim().slice(0, 30)}" ${ratio.toFixed(2)}:1`);
    }
  }
  if (tiny) push('WARN', 'text-under-12px', `${tiny} text elements`);
  if (lowC.length) push('FAIL', 'low-contrast', lowC.slice(0, 8).join(' | ') + (lowC.length > 8 ? ` (+${lowC.length - 8})` : ''));
  out.stats.fontSizes = [...sizes].sort((a, b) => a - b);
  if (sizes.size > 9) push('WARN', 'too-many-font-sizes', `${sizes.size} distinct sizes`);
  for (const h of document.querySelectorAll('h1,h2,h3')) {
    if (!visible(h)) continue;
    const lh = parseFloat(getComputedStyle(h).lineHeight) || parseFloat(getComputedStyle(h).fontSize) * 1.2;
    const lines = Math.round(h.getBoundingClientRect().height / lh);
    if (lines > 2) push('WARN', 'heading-over-2-lines', `${h.tagName} "${h.textContent.trim().slice(0, 40)}" ~${lines} lines`);
  }
  const imgs = [...document.images];
  const noAlt = imgs.filter(i => !i.hasAttribute('alt')).length;
  if (noAlt) push('FAIL', 'img-missing-alt', `${noAlt} images`);
  const noSize = imgs.filter(i => !i.getAttribute('width') && !getComputedStyle(i).aspectRatio.includes('/')).length;
  if (noSize) push('WARN', 'img-no-dimensions', `${noSize} images without width/height or aspect-ratio (CLS)`);
  const broken = imgs.filter(i => i.complete && i.naturalWidth === 0).length;
  if (broken) push('FAIL', 'img-broken', `${broken} images failed to load`);
  const unl = [...document.querySelectorAll('button, a[href], [role=button]')].filter(b => visible(b) && !(b.innerText.trim() || b.getAttribute('aria-label') || b.getAttribute('aria-labelledby') || b.getAttribute('title'))).length;
  if (unl) push('FAIL', 'unlabeled-control', `${unl} buttons/links without accessible name`);
  const small = [...document.querySelectorAll('button, a[href], input, select, [role=button]')].filter(b => { if (!visible(b)) return false; const r = b.getBoundingClientRect(); return r.width < 24 || r.height < 24; }).length;
  if (small) push('WARN', 'target-under-24px', `${small} interactive targets smaller than 24x24`);
  out.stats.fontsLoaded = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, '')).filter((v, i, a) => a.indexOf(v) === i);
  out.stats.fontsFailed = [...document.fonts].filter(f => f.status === 'error').map(f => f.family.replace(/"/g, ''));
  if (out.stats.fontsFailed.length) push('FAIL', 'font-failed', out.stats.fontsFailed.join(', '));
  // richness: every top-level section should carry a visual anchor (img/picture/video/svg/canvas/model or a background image)
  const sections = [...document.querySelectorAll('main > section, main > div > section, body > section, [data-section]')].filter(visible);
  const box = e => { const r = e.getBoundingClientRect(); return Math.min(r.width, r.height); };
  const hasVisual = s => s.querySelector('img, picture, video, canvas, model-viewer, iframe') ||
    [...s.querySelectorAll('svg')].some(v => box(v) >= 120) ||                       // an illustration / graphic
    [...s.querySelectorAll('svg')].filter(v => box(v) >= 18).length >= 3 ||          // an icon set in use
    [s, ...s.querySelectorAll('*')].some(e => { const b = getComputedStyle(e).backgroundImage; return b && b !== 'none' && /url\(/.test(b); });
  const bare = sections.filter(s => !hasVisual(s) && s.getBoundingClientRect().height > 160);
  out.stats.sections = sections.length; out.stats.sectionsWithoutVisual = bare.length;
  if (bare.length) push('WARN', 'section-without-visual', bare.slice(0, 6).map(s => '#' + (s.id || s.getAttribute('aria-labelledby') || s.className.toString().split(' ')[0] || 'section')).join(', ') + ' - add a photo, illustration, icons or graphic (studio-bar.md §5)');
  const icons = document.querySelectorAll('svg, i[class*="icon"], [class*="icon"] svg, img[src$=".svg"]').length;
  out.stats.svgAndIcons = icons;
  out.stats.pageHeight = document.documentElement.scrollHeight;
  out.stats.screens = +(document.documentElement.scrollHeight / innerHeight).toFixed(1);
  return out;
};

async function shots(pw, o) {
  const target = o._[1];
  if (!target) throw new Error('shots needs a url or file');
  const widths = String(o.widths || '1440,768,390').split(',').map(Number);
  const outDir = o.out || '.astudio/shots';
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await launch(pw);
  const report = { target, widths: {} };
  for (const w of widths) {
    const h = w <= 480 ? 844 : w <= 1024 ? 1024 : 900;
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, reducedMotion: o['reduced-motion'] ? 'reduce' : 'no-preference', isMobile: w <= 480, hasTouch: w <= 480 });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e.message || e)));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await page.goto(toURL(target), { waitUntil: 'networkidle', timeout: 45000 }).catch(e => errors.push('load: ' + e.message));
    await page.evaluate(() => document.fonts && document.fonts.ready);
    // trigger scroll-reveals, then return to top
    await page.evaluate(async () => { const H = document.documentElement.scrollHeight; for (let y = 0; y < H; y += innerHeight * 0.6) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } scrollTo(0, 0); await new Promise(r => setTimeout(r, 400)); });
    const fold = path.join(outDir, `w${w}-fold.png`);
    await page.screenshot({ path: fold });
    const files = [fold];
    if (!o['no-full']) { const full = path.join(outDir, `w${w}-full.png`); await page.screenshot({ path: full, fullPage: true }); files.push(full); }
    const audit = await page.evaluate(AUDIT);
    audit.consoleErrors = errors.slice(0, 10);
    if (errors.length) audit.issues.push({ sev: 'WARN', rule: 'console-errors', detail: errors.slice(0, 3).join(' | ') });
    report.widths[w] = { files, ...audit };
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'report.json'), JSON.stringify(report, null, 2));
  let fails = 0;
  for (const [w, r] of Object.entries(report.widths)) {
    console.log(`\n== ${w}px  (${r.stats.screens} screens, sizes ${r.stats.fontSizes.join('/')}, fonts: ${r.stats.fontsLoaded.join(', ') || 'none loaded'})`);
    r.files.forEach(f => console.log('  shot:', f));
    for (const i of r.issues) { console.log(`  ${i.sev.padEnd(4)} ${i.rule}: ${i.detail}`); if (i.sev === 'FAIL') fails++; }
    if (!r.issues.length) console.log('  no measurable issues');
  }
  console.log(`\nreport: ${path.join(outDir, 'report.json')}  FAIL=${fails}`);
  console.log('Now OPEN the screenshots and critique them - passing checks does not mean the design is good.');
}

async function element(pw, o) {
  const file = o._[1];
  const browser = await launch(pw);
  const ctx = await browser.newContext({ viewport: { width: +(o.width || 1600), height: +(o.height || 1200) }, deviceScaleFactor: +(o.scale || 1) });
  const page = await ctx.newPage();
  await page.goto(toURL(file), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts && document.fonts.ready);
  const sel = o.selector || 'body';
  const els = await page.$$(sel);
  if (!els.length) throw new Error(`selector ${sel} not found`);
  const out = o.out || 'element.png';
  if (els.length === 1) { await els[0].screenshot({ path: out, omitBackground: !!o.transparent }); console.log('wrote', out, await els[0].boundingBox()); }
  else {
    const dir = out.replace(/\.png$/, ''); fs.mkdirSync(dir, { recursive: true });
    for (let i = 0; i < els.length; i++) { const id = (await els[i].getAttribute('id')) || `item-${i + 1}`; const f = path.join(dir, `${id}.png`); await els[i].screenshot({ path: f, omitBackground: !!o.transparent }); const b = await els[i].boundingBox(); console.log('wrote', f, `${Math.round(b.width)}x${Math.round(b.height)}`); }
  }
  await browser.close();
}

async function svg(pw, o) {
  const file = o._[1];
  const sizes = String(o.sizes || '16,32,64,180,512').split(',').map(Number);
  const outDir = o.out || path.join(path.dirname(file), 'png');
  fs.mkdirSync(outDir, { recursive: true });
  const src = fs.readFileSync(file, 'utf8');
  const b64 = Buffer.from(src).toString('base64');
  const browser = await launch(pw);
  const base = path.basename(file, '.svg');
  for (const s of sizes) {
    const ctx = await browser.newContext({ viewport: { width: s, height: s }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const bg = o.bg && o.bg !== 'transparent' ? o.bg : 'transparent';
    await page.setContent(`<html><body style="margin:0;background:${bg}"><img src="data:image/svg+xml;base64,${b64}" style="width:${s}px;height:${s}px;object-fit:contain;display:block"></body></html>`);
    await page.waitForTimeout(50);
    const f = path.join(outDir, `${base}-${s}.png`);
    await page.screenshot({ path: f, omitBackground: bg === 'transparent', clip: { x: 0, y: 0, width: s, height: s } });
    console.log('wrote', f);
    await ctx.close();
  }
  await browser.close();
}

async function pdf(pw, o) {
  const file = o._[1];
  const browser = await launch(pw);
  const page = await browser.newPage();
  await page.goto(toURL(file), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  const w = +(o.width || 1920), h = +(o.height || 1080);
  await page.pdf({ path: o.out || 'out.pdf', width: `${w}px`, height: `${h}px`, printBackground: true });
  console.log('wrote', o.out || 'out.pdf');
  await browser.close();
}

(async () => {
  const o = args(process.argv.slice(2));
  const cmd = o._[0];
  if (!cmd || o.help) { console.log(fs.readFileSync(__filename, 'utf8').split('*/')[0]); return; }
  const pw = loadPW();
  try {
    if (cmd === 'shots') await shots(pw, o);
    else if (cmd === 'element') await element(pw, o);
    else if (cmd === 'svg') await svg(pw, o);
    else if (cmd === 'pdf') await pdf(pw, o);
    else throw new Error('unknown command ' + cmd);
  } catch (e) { console.error('render error:', e.message); process.exit(1); }
})();
