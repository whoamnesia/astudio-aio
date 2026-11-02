---
name: slides
description: >-
  astudio presentations: strategic, persuasive HTML slide decks (pitch decks, sales decks, product demos, case studies,
  conference talks, QBRs, brand presentations) built on the brand's design code - narrative structure and emotion arc,
  one idea per slide, real data charts, keyboard/touch navigation, speaker notes, 16:9 layouts that are designed rather
  than templated - exported to PDF/PNG. Use when the user asks for a presentation, deck, pitch deck, slides,
  "презентация", "питч-дек", "слайды для инвесторов", "презентация компании", or to restyle an existing deck. If the
  user explicitly wants a .pptx file, build the deck content here and hand off to a PowerPoint-capable tool/skill.
  Part of astudio-aio.
argument-hint: "[topic / goal] [audience] [slide count]"
---

# astudio · Slides

Role: Senior presentation designer at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

A deck is an argument delivered one claim at a time. Each slide has one job, a headline that states the takeaway (not
a topic label), and evidence the audience can grasp in the seconds the presenter gives it.

Shared: `<root>` = two levels above this skill's base dir. Brand kit/tokens from the project (`design-tokens/tokens.css`,
faces, logo) - without one, run a compact `astudio-aio:brand` pass or ask. Local references: `references/strategies.md`
(15 deck structures with emotion arcs), `references/copywriting.md` (PAS, AIDA, BAB… for slides),
`references/deck-build.md` (HTML deck template, layouts, charts, navigation, export). Database: `search.py "<goal>" -d
slide-strategy|slide-copy|slide-layout|slide-chart`.

## Workflow
1. **Brief**: goal (raise, sell, inform, teach, align), audience and what they already believe, the one decision/action
   wanted at the end, time slot, presented live or sent to read (sent decks need more text per slide), data available
   (real numbers only), language.
2. **Structure**: pick a strategy (`references/strategies.md`) and adapt; write the storyline as slide headlines only
   (each a full-sentence takeaway: "Churn halves when onboarding drops to one step"). Read the headlines alone - they
   must tell the whole story. Plan the emotion arc (what is → what could be; pattern breaks around 1/3 and 2/3).
3. **Content per slide**: one claim + the proof (a chart of real data, a product shot, a quote with name and permission,
   a big number with its context). Cut everything else into speaker notes. Copy formulas where persuasion matters.
4. **Design**: build with the brand's tokens and faces (`references/deck-build.md`): a small set of layouts used with
   variety (no two identical layouts in a row), left-aligned by default, display type for headlines, generous margins,
   the brand colour used as whole-slide fields for section breaks, charts styled by `<root>/skills/dashboard/
   references/charts.md` (one series per chart, the finding annotated, no rainbow). Avoid the template look: no centred
   everything, no icon-card grids, no pulsing CTA, no gradient washes.
5. **Build** one `deck.html` with keyboard/click/swipe navigation, slide counter, speaker notes (`N` toggles), print CSS
   (one slide per page). Render: `node <root>/scripts/render.cjs shots deck.html --widths 1920 --no-full` for the first
   slide and `render.cjs pdf deck.html --out deck.pdf --width 1920 --height 1080` for all; open and review every page.
6. **Critique** with `<root>/reference/critique.md` adapted: headline-only read test, one idea per slide, legibility at
   the back of a room (body ≥ 24px at 1920 wide; data labels ≥ 18px), contrast, consistency, the ask is clear.

## Rules
- Real data only; cite sources on the slide (small) or in notes; label projections as projections.
- ≤ ~30 words per slide for live decks (sent decks may carry more, still one idea); no paragraphs of bullets.
- One chart per slide with the takeaway as the headline and the key point annotated.
- Consistent positions for headline, logo and page number; section dividers as brand colour fields.
- Accessible: real text (not images of text), 4.5:1 contrast, readable fonts, alt text for images in the PDF/HTML.
