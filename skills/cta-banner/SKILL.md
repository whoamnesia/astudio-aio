---
name: cta-banner
description: >-
  astudio CTA banners and ad creatives built for clicks and conversions: offer and audience analysis (awareness stage),
  scroll-stopping hooks, angle variations (pain, desire, proof, identity, contrarian, urgency), headline and CTA copy
  formulas, conversion-focused composition (one focal point, one action, contrast, visual flow to the button), platform
  specs and safe zones for Meta/Instagram, VK, Telegram, TikTok, YouTube, Google Display, Yandex Direct, and an A/B test
  matrix - all on the brand's design code, exported at exact sizes. Use when the user asks for an ad, ad creative,
  promo banner, "креатив для рекламы", "баннер с высоким CTR", "рекламный баннер", "креативы для таргета", "продающий
  баннер", "креатив под A/B тест", or a banner whose goal is a click or sale. Builds on astudio-aio:banner-design.
argument-hint: "[product/offer] [platform] [goal: click | lead | sale | install]"
---

# astudio · CTA banner

Role: Senior performance designer at the digital studio astudio.one (15+ years) - every creative set is a well-paid
commission; the bar is in `<root>/reference/studio-bar.md`.

A high-CTR creative wins the first half-second (stops the scroll), says one thing the viewer cares about in their own
words, and makes the next step obvious. It is honest: no fake scarcity, fake reviews, fake UI buttons or misleading
claims - those raise CTR and destroy conversion, trust and ad accounts.

Shared: `<root>` = two levels above this skill's base dir. Production (HTML template, export, safe zones) comes from
`<root>/skills/banner-design/` (`references/production.md`, `art-direction.md`) and sizes from
`search.py "<platform>" -d banner`. Brand kit/tokens from the project. Local references: `references/conversion.md`
(awareness, angles, hooks, copy formulas, composition for conversion, platform notes), `references/testing.md` (A/B
matrix, naming, what to measure). Copy rules: `<root>/reference/copy.md` §6.

## Workflow
1. **Offer and audience** (ask what is missing, one round): product, the exact offer (price, discount, trial, bonus -
   only real ones), target audience and their situation, awareness stage, platform/placement, goal (click, lead, sale,
   install), landing page (message match matters), brand assets, compliance limits (finance/health/alcohol rules, legal
   marking: for Russia ads need the «Реклама» label + advertiser info/erid per the ad-marking law - leave space).
2. **Strategy**: diagnose the awareness stage → message rules (what to say, what not to); pick the conversion action and
   the single benefit; list objections (price, trust, time, complexity, past failures) and which the creative answers.
3. **Angles**: write 6-10 distinct angles (pain, desire/outcome, proof, identity, contrarian, mechanism, urgency only
   if real, price/value, before/after) with a hook line each. Pick 3-4 most different for production.
4. **Copy per angle**: headline (≤ 7 words, specific - a number, a result, a time), sub-line (≤ 12 words, removes the
   main objection), CTA (verb + outcome: «Получить расчёт», «Забронировать», "Start free trial"), proof element (real
   rating, real number, guarantee). Message-match the landing page headline.
5. **Composition for conversion** (`references/conversion.md` §4): one focal visual (face with gaze toward the CTA,
   product in use, the result), headline in the strongest position, CTA as the highest-contrast element with breathing
   room, visual flow (Z/F pattern) ending at the CTA, brand mark small but present, text compact, readable at thumbnail.
   Add **2-3 accent details** that catch the eye (sticker with the offer fact, hand-drawn underline/circle on the key
   word, an arrow or gaze toward the CTA, a cut-out breaking the frame, a contrast frame - `conversion.md` §4a), without
   overdoing it. Visuals: free stock photos (Unsplash/Pexels/Pixabay, credited) or code-made graphics - never
   AI-generated images.
   Build in HTML per the banner-design template at the platform sizes; keep the brand's tokens and type.
6. **Variants and A/B matrix** (`references/testing.md`): 1 variable at a time per test (hook/angle → visual →
   headline → CTA → colour), name files by angle and variable, 3-5 creatives per ad set.
7. **Export and QA**: `render.cjs element … --scale 2`; open each PNG: thumbnail test (25% size), safe zones/UI
   overlaps, contrast (CTA ≥ 4.5:1 text, button ≥ 3:1 vs ground), legal label space, file size limits.
8. **Deliver**: the creative set, the angle/copy table, the test plan, and what to measure (CTR, CPC, CVR on landing, CPA)
   - CTR alone is not success.

## Rules
- One message, one CTA, one focal point. Benefit over feature. Specific over clever.
- The CTA looks clickable (button shape in the brand's style) but never imitates platform UI or system dialogs.
- Real proof only; urgency only with a real deadline; prices exactly as supplied with conditions visible if required.
- Brand consistency builds recall: same logo position, palette, type across the set; the angle changes, the brand doesn't.
- Mobile-first: most impressions are on phones - design 4:5 / 9:16 first, check the 1:1 and 1.91:1 crops.
