# astudio-aio — All-in-One design studio for Claude Code

Author: **astudio** — [astudio.one](https://astudio.one). One plugin, one main skill and 12 sub-skills that take a brief from zero to a finished,
distinctive product: **logo → brand kit + design code → website**, plus dashboards, mobile/app design, 3D elements,
banners, CTA ad creatives, slides and graphic design — with anti-template art direction, a searchable design database
and render-and-critique tooling.

## Установка из GitHub / Install from GitHub

В Claude Code / In Claude Code:
```
/plugin marketplace add whoamnesia/astudio-aio
/plugin install astudio-aio@astudio
```
Перезапустите Claude Code (restart Claude Code). Обновление / update: `/plugin marketplace update astudio`.

## Установка (локально, без GitHub)

1. Скопируйте папку `astudio-aio` к себе на компьютер, например в `~/claude-plugins/astudio-aio`.
2. В Claude Code выполните:
   ```
   /plugin marketplace add ~/claude-plugins/astudio-aio
   /plugin install astudio-aio@astudio
   ```
3. Перезапустите Claude Code. Скиллы появятся в меню `/` как `astudio-aio:astudio-aio`, `astudio-aio:logotype` и т. д.
4. Для рендера и проверки результатов нужен Playwright: `npm i -g playwright && npx playwright install chromium`
   (без него скиллы работают, но не смогут делать скриншоты-проверки и экспорт PNG/PDF). Python 3.8+ нужен для
   `search.py`, `palette.py`, `tokens.py`, `lint.py`, `logo_kit.py`.

## Skills

| Command | What it does |
|---|---|
| `astudio-aio:astudio-aio` | **Main / AIO.** Full pipeline: brief → direction → logo → brand kit + design code → site → render, critique, fix → delivery. Routes to every sub-skill. |
| `astudio-aio:ui-ux` | Design intelligence for any UI task; audit, critique, polish, bolder/quieter, harden; style/palette/font selection from the database. |
| `astudio-aio:design` | Graphic hub: icon sets, social templates, stationery, packaging, merch, posters, patterns. |
| `astudio-aio:brand` | Brand strategy, voice, visual identity, colour/type systems, rendered brand book. |
| `astudio-aio:design-system` | DTCG 2025.10 tokens, CSS variables (light/dark), Tailwind v4 theme, component specs, DESIGN.md; extraction from code. |
| `astudio-aio:ui-styling` | Implementation craft: Tailwind v4, shadcn/ui, modern CSS, React/Next/Vue/Svelte/Astro/static. |
| `astudio-aio:banner-design` | Banners, covers, OG images, display sizes, print — multiple art directions, exact-size export. |
| `astudio-aio:slides` | Persuasive HTML decks with navigation, notes and PDF export. |
| `astudio-aio:logotype` | Logo design in hand-written SVG: concepts, tests (16px…billboard, one colour, mirror), full logo kit and web icons. |
| `astudio-aio:cta-banner` | High-CTR ad creatives: awareness stage, angles, hooks, copy formulas, conversion composition, A/B matrix. |
| `astudio-aio:dashboard` | Dashboards and app screens on the user's design code (or the style of their existing pages). |
| `astudio-aio:3d-elements` | 3D models and scenes from free licensed sources or original procedural 3D; Three.js/R3F/Spline; budgets and fallbacks. |
| `astudio-aio:mobile` | Mobile versions of sites (native feel) and iOS/Android/cross-platform app design. |

## Layout
```
astudio-aio/
  .claude-plugin/plugin.json, marketplace.json
  skills/<13 skills>/SKILL.md + references/
  reference/   shared knowledge: studio-bar (role, references, wow, richness, stock-only images), direction, anti-slop, typography, color, layout, motion, copy, accessibility, imagery, critique, tools
  scripts/     search.py · palette.py · tokens.py · render.cjs · lint.py · logo_kit.py
  data/        design database (styles, products, palettes, fonts incl. Cyrillic flags, UX rules, stacks, logo, slides, banner sizes, 3D sources, hero and section patterns)
  NOTICE.md    third-party sources and licences
```

## Tools quick start
```bash
python3 scripts/search.py "coffee shop cozy artisan" --design-system -p "Bean There" --cyrillic
python3 scripts/palette.py system --primary "#C2410C" --accent "#0F766E" --json brand/palette.json
python3 scripts/tokens.py init > brand/brand.spec.json && python3 scripts/tokens.py build brand/brand.spec.json --out design-tokens
node scripts/render.cjs shots site/index.html --widths 1440,768,390
python3 scripts/lint.py site/ --mode persuade
python3 scripts/logo_kit.py sheet logo-a.svg logo-b.svg --names A B --brand "#C2410C"
```

## Принципы студии
Каждый скилл работает в роли Senior UI/UX и Web-дизайнера студии astudio.one (опыт 15+ лет): заказ = дорогой проект.
Перед дизайном смотрим референсы (Awwwards, Behance), первый экран делаем с вау-эффектом, страница насыщенная:
фото, иконки и графика в каждом разделе. Фото берём только со стоков (Unsplash, Pexels, Pixabay), графику рисуем
кодом; ИИ-генерация изображений не используется. Подробно: `reference/studio-bar.md`.

## Licence
astudio-aio original content © astudio. Reused data keeps its MIT licence; see `NOTICE.md` for all sources.
