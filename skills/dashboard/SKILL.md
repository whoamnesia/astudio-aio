---
name: dashboard
description: >-
  astudio dashboards and app screens with considered UI/UX: analytics, admin panels, CRM, back office, finance and
  wallet homes, inboxes and queues, settings and billing, data tables, KPI overviews, monitoring, builders - built on
  the user's existing brand kit and design code (tokens, DESIGN.md) or, if none exists, on the style extracted from
  the product's existing pages. Covers the screen's one question, shell and navigation, KPIs, charts, tables, forms,
  every data state, density, dark mode and the phone. Use when the user asks for a dashboard, admin panel, control
  panel, analytics screen, CRM, "панель управления", "админка", "дашборд", "личный кабинет", settings page, or a product
  UI fragment for a landing page. Part of astudio-aio.
argument-hint: "[product] [screens: overview | analytics | list | detail | settings | inbox | wallet | builder]"
---

# astudio · Dashboard

Role: Senior product (UI/UX) designer at the digital studio astudio.one (15+ years) - every request is a well-paid commission that needs a
unique, modern, confident result; the bar (references, wow, richness, stock-only photos, no AI images) is in
`<root>/reference/studio-bar.md`.

A generated dashboard is the average of every template: a dark sidebar with a coloured pill, "Welcome back 👋",
four KPI cards with icons in tinted circles and a green "+12.5%", a gradient area chart, a zebra table. Nothing wrong,
nothing decided. A screen a person trusts shows **the product**: its own data at real size, the screen's one question
answered by its biggest block, the main job one click away, a grid whose sums close.

Shared: `<root>` = two levels above this skill's base dir. Local references: `references/app-screen-rules.md`
(shell, canvas, KPIs, tables, forms, type/colour defaults, density, states, phone, tells - the core rules),
`references/charts.md` (which chart, axes, marks, legends, annotations, accessibility). Also
`<root>/reference/accessibility.md`, `critique.md`; tools `render.cjs`, `lint.py --mode operate`, `search.py -d chart`,
`search.py "<concern>" -d ux|app`, `--stack`.

## Step 0 - Inherit the design code (required)
1. Look for the brand kit / design code: `DESIGN.md`, `design-tokens/`, `brand/`, Tailwind `@theme`/config, CSS
   variables, a component library (shadcn `components.json`, MUI theme…). If found, **it is law**: use its tokens,
   faces, radius logic, colour roles and components; extend only what an app screen needs (data hue, status pills,
   density tokens) and document the additions.
2. If none exists but the product has pages (marketing site, other app screens), **extract the style** from them
   (`<root>/skills/design-system/references/extract.md`): render them (`render.cjs shots`), read their CSS/components,
   record roles, faces, radii, spacing, borders vs shadows - then build the dashboard in that language.
3. If nothing exists at all, run `astudio-aio:brand`/`design-system` quickly in Operate mode (Restrained colour, one UI
   grotesk with tabular figures, tight or soft radius chosen once) - or ask whether to create a brand first.

## The run
1. **Inventory data and jobs** (8-12 lines): the objects and their fields with units; realistic magnitudes (a new
   account's small numbers too); who opens the screen, how often, on what device; the jobs they do next (approve, reply,
   pay, ship) and the most frequent one; the product's own things (name, mark, workspace, people, objects recognised
   by sight). Write the **dataset** as JSON/JS the screen renders from - believable names, totals computed from rows,
   a unit on every figure, `console.assert` for figures that must agree.
2. **Name the screen's one question** ("Did today's orders ship?", "Which deploy broke?") and its **one finding** in
   today's data ("the 23:28 deploy doubled the error rate"). The question decides what is biggest; the finding sits
   under the title next to the action it drives. List blocks as answers to the next questions; delete blocks with no
   question (this kills the stock "KPI row, big chart, two small charts, table").
3. **Choose the shell and style** to how the product is used (long sessions vs quick glance, money vs media, team vs
   personal, day vs night): open plane / tinted frame with inset sheet / ruled T-frame / icon rail / no sidebar
   (`references/app-screen-rules.md` §1). Choose the product's **face** (one of: ground tinted from the product's world,
   a figure face with character, the brand hue on the main data element) and one **signature element** only this
   product has. Write both down next to the question.
4. **Build the shell empty**, then the canvas: grid arithmetic written in a comment (columns × width + gutters = canvas),
   one gutter value, one left and right edge, title row (noun title 20-28px, optional data sentence, real actions,
   freshness stamp).
5. **Put in the data**: KPIs as type not tiles, charts per `references/charts.md` (one question, one series, one hue on
   the main data element), tables with right-aligned tabular figures, fixed decimals, sign on every change, units as
   grey suffixes; statuses as pale pills; the main job's control where the answer shows.
6. **Build every state**: empty, zero (printed as zero), missing (grey dash), loading (final layout with grey bars at
   real size, no shimmer, no shift), error (inside the failed block, last-good time, Retry), first run, filtered-empty;
   hover/selected/focus/disabled for rows and controls. A screen that only works with full data is half built.
7. **Phone and tablet** (`references/app-screen-rules.md` §10): sidebar folds, tables become two-line rows, filters into
   one row/sheet, KPIs 2-up, charts full width 160-200px.
8. **Check**: `render.cjs shots` at 1440/768/390; `lint.py --mode operate`; then answer in writing: is the question
   answered by the biggest block and read first? do all blocks share edges, no ragged rows or dead strips? is colour only
   on data, status and the one primary action? do numbers add up and align digit for digit (recompute totals from what
   is displayed)? zeros look like zeros, missing like dashes? legends match marks, no colliding labels? phone navigation
   folded and every block still answering? Fix the worst three, re-render; max three rounds.
9. **Report**: shell/style chosen and why, the face and signature element, each screen's question and finding, tokens
   added to the design code, sample data to replace.

## Landing-page fragments
When a marketing page shows the product, build each fragment as a real piece of this app (`data-ui` on its root):
same tokens, real-looking data that adds up, one finding stated, cropped and scaled like a photograph. Never grey bars
and lorem numbers.

## Non-negotiables
App type is not display type (title ≤ 32px, no figure ≥ 48px). One primary per screen (often near-black). Colour on
data, not chrome (~3% coloured pixels). No icons in coloured circles on KPIs, no sparklines on every KPI, no rainbow
charts, no zebra rows, no uppercase tracked headers, no dark saturated sidebar on a light screen, no greeting with emoji,
no invented vanity metrics. Accessibility floor holds (4.5:1 for every text tier incl. placeholders, keyboard,
focus-visible, labelled icon buttons, `aria-sort`, live regions for async updates).
