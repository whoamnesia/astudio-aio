# App screen rules

Distilled from a measured study of 23 real product screens (17 light, 6 dark) plus tested house rules. Numbers are the
study's medians/ranges unless marked house rule.

## What separates real screens from generated ones
1. Colour goes on data, not chrome - median ~3% coloured pixels; 12 of 23 have no filled primary button.
2. KPIs are type, not tiles - no icon circles, no sparklines on KPIs (0 of 23).
3. Surfaces are flat - 17 of 23 cards have no shadow; separation by a 1px line or one tone step.
4. No hero header - title median 24px; 9 screens have nothing over 16px (breadcrumb names the page).
5. Charts carry little chrome - single series has no legend; 3-7 faint gridlines or none.
6. Navigation recedes - active item a neutral grey pill or brighter label; a coloured left bar once in 23.
7. Tables are rules and alignment - no zebra, no header bands, numbers right-aligned.
8. Honest data states - zeros print as zeros, missing as a grey dash, empty sections keep their frame.
Quiet is the start, not the goal: in blind tests clean-but-thin screens lost to richer ones. Every block the brief
names shows its header and first rows on a 1440×900 first screen; the product is named in the shell; the main job has a
control; colour on a change says good/bad.

## 1. Shell
| Shell | What | Use for |
|---|---|---|
| Open plane | labelled sidebar on the page ground (or 1-2% off), no top bar | personal/team homes, simple tools |
| Tinted frame + white sheet | sidebar and top bar share a tinted ground (#f6f6f6-#f9fbfc); the page is a white sheet inset 8px, radius 10-16, 1px edge, no shadow | B2B analytics, dev platforms, builders |
| Ruled T-frame | 210-240px sidebar + 64px top bar on one ground, divided by 1px rules; workspace switcher at the top bar's right | dense pro tools, often dark |
| Icon rail | 50-60px unlabelled rail, 15-18px icons, tooltip + accessible name each | ≤ 5 destinations, width-hungry screens |
| No sidebar | 46-48px top bar over a centred 1088-1208px column | reports, viewers, few destinations |
Sidebar: 224-240px; rows 32px hit on 34px pitch (roomy 40-52); 16px outline icons ~1.5px stroke; labels 14px/400;
active = neutral grey pill (#e9e9e9-#ededed, radius ~8) on light, brightness (#bbb → #fff) on dark; groups by 12-13px
sentence-case grey labels (never uppercase) or hairlines; utilities at the bottom; workspace switcher at top. **The
product's mark and name at the top** (a simple monogram/symbol in the accent, never a black square with a letter). Counts
on nav items only for queues needing action with a clear noun ("Requests 5"). Nav items are screens, not anchors.
Top bar (optional): 44-51px light / 64px with rule; must hold something real (search with shortcut hint, switcher,
object name). A floating button only if it is the one primary and covers nothing.

## 2. Canvas and title
- Fluid canvas with 24-40px side padding (content ~1120-1312px) or centred 1100-1250px. Top offset to title 20-36px.
- **One gutter** value horizontally and vertically (16 typical). One left edge from header to last row.
- Grid arithmetic closes (`3×372 + 2×17 = 1152`); choose the column count from the item count (4 KPIs → 4 columns);
  a lone card spans; cards in a row share a bottom edge (balance by content, stack, or pin only an action/total to
  the foot); a stretched card never shows a blank band > 40px; narrow tables (≤ 5 columns) don't span 1300px.
- Title: one `h1`, a noun ("Analytics", the project's name), 18-32px (median 24) at 600-700; optional 14-16px grey
  sentence about the data (the finding, the period) - never about the interface; actions on the right only when real;
  freshness stamp "Updated 16:09" + refresh.
- Date range at page level OR per card, never both. Underline tabs on a full-width 1px rule (indicator 2px); segmented
  control as wide as its options; control height 32-36px; scope left (date, filters), utilities right.

## 3. KPIs
- Default: one container split by 1px dividers into equal columns, label above value; or each headline number inside the
  card that explains it. 1-6 per row (median 3-4).
- Values 16-40px (mode 24), labels 12-16px grey sentence case; value ≈ 1.7× label; regular weight is common - bold for
  money only. The answer figure (balance, net worth) 30-36px and ≥ 1.3× siblings; nothing larger elsewhere.
- No icon in coloured circle, no sparkline, no tinted tile. Units as smaller grey suffix ("5 m 24 s", "12 /20").
- Deltas optional, 10-15px, with the window in words ("vs prior 30 days"). **Colour says good or bad, not up or down**
  (latency/errors/cost/churn rising = negative). Zero or undefined change is grey; from zero write "+4 (new)".
- One figure, one place (not repeated in a legend beside it). KPIs may double as chart series tabs (selected: 2px rule
  or active fill; unselected values stay in ink, never grey).

## 4. Tables and lists
- Rows 36-53px single-line (median 45); two-line rows with media 56-92 (media + 24-32); key-value rows 21-32.
- Header 11-14px grey regular sentence case, no fill band, usually no rule (if one, it is the strongest line).
- No zebra; dividers optional, 1px, 3-7% darker than surface. Pick one divider extent per screen.
- Numbers right-aligned, tabular figures, fixed decimals per metric (money 2, % 1-2, counts 0), thousands separators,
  sign on every change, no space after currency (or locale format: 1 500 ₽). Identity column widest, never the one cut.
  Dates ISO in comparisons, words for recency. IDs mono, truncated ~8 chars + copy icon. Two measures can stack in one
  cell on one right edge.
- Ink only on identity and the key number; the rest grey. Missing = grey dash; real zero printed.
- Status: one mark per row - pale tint + dark text of the same hue (15-28px tall, 11-14px/500), or a 6px dot + ink label;
  saturated white-text pills only for a rare call to action. Chips never squeeze (`flex:none; white-space:nowrap`).
- Media: 16px logos, 24-32px avatars, 48px in two-line rows; one fixed media slot so text starts on one edge.
- No pagination on overviews: cap 4-6 rows + "View all" + total. Full list screens: total above, sticky header,
  "1-50 of 1,284" paging or load more.
- Row actions: none, a kebab, or (when the row needs doing) a visible ghost button/text action in a fixed trailing
  column at a constant pitch. Checkboxes only with bulk actions. Hover/selected: 1px outline or darker border; in a
  list driving a detail pane, selected row takes the nav's active fill.
- Calendars/timelines: people column 160-220px; faint day lines, weekends a tone darker, today a 1px line in the data
  hue; bars 20-24px; each booking kind has its own mark (fill, hatch, outline, dashed for pending).

## 5. Forms and settings
Label above (14px/500), field 38-40px (radius 8-10, 1px #e5e7eb-ish border, white even on grey panels), 16px between
fields, toggles 28-33px wide with semantic green or near-black "on". Disabled controls stay legible and say why.
Settings: label column (~450px: title + grey description) beside a panel (~700px, flat tint, radius 16); sections split
by a full-width rule with 32px air; destructive actions last in their own section with the consequence in words and a
confirmation naming the object; one view per area (each sidebar item its own view); one save model per view (autosave
with "Saved" stamp, or one Save per panel); show what the setting produces (preview of the email/invoice/notification).

## 6. Buttons
Controls 27-40px tall (median 34, 32 common); one filled primary per screen, usually near-black (#1d1f20) or inverted
white on dark; secondary white with 1px border; tertiary text. Controls in a row share a height.

## 7. Type and colour defaults
- One grotesk carries the screen; a second face only with one job (mono for IDs/figures). Title 24 · KPI 24 · card
  title 16 (500-600) · body/cells 14 · labels/meta 12 · axis 12 · pills 11-12 (floor 11). Weights ~3; 700 does one job.
  Tabular figures on every number (verify the face has them). Sentence case.
- Light grounds: white cards on #f9fafb, or grey panels on white, or a framed sheet. Sidebar never dark/saturated on a
  light screen. Lines: card edge ~#eaeaea, row rules #efefef-#f4f4f4, control borders ~#d1d5db. Text tiers ~#111 /
  ~#5f6368 / ≥ #6b6b6b (every tier ≥ 4.5:1 incl. placeholders). Accent on data (or actions) only - one accent family.
- Dark grounds: #000 / #111 / #171719 (no navy/slate); surfaces +1 lightness step; structural lines ~22-31 levels above
  ground; interactive outlines brighter; text #fff / ~#b4b4b4 / ~#949494 (two greys that read apart); status as hue on a
  dark tint of itself; when the accent is green, positive = the accent.
- Edges: a border OR a shadow, never both; shadows only on floating layers (menus, popovers, composer, dialog).
  Radius bimodal: tight 4-8px or soft 16-24px (avoid 11-12); controls follow cards; nested radii step down.
- Icons outline, 14-20px, grey, never in saturated circles.
- Default tokens (light/dark) to start from when the design code has none:
```css
:root { --ground:#f9fafb; --surface:#fff; --raised:#f9f9f9; --active:#eee; --border:#e8e8e8; --rule:#f2f2f2;
  --control:#d1d5db; --text:#111; --muted:#5f6368; --faint:#6b6b6b; --primary:#1d1f20;
  --positive:#247b50; --pill-positive-bg:#dcfae5; --pill-positive-ink:#04250e;
  --negative:#c4242a; --pill-negative-bg:#ffedea; --pill-negative-ink:#831c1e;
  --pill-warning-bg:#fffbeb; --pill-warning-ink:#92400e; --grid:#e5e5e5;
  --radius-card:8px; --radius-control:6px; --radius-chip:4px; --gap:16px; --card-pad:20px;
  --control-height:32px; --row-height:48px; --fs-title:24px; --fs-kpi:24px; --fs-body:14px; --fs-small:12px; }
:root[data-theme=dark] { --ground:#000; --surface:#111; --raised:#222; --active:#222; --border:#1a1a1a; --rule:#161616;
  --control:#444; --text:#fff; --muted:#b4b4b4; --faint:#949494; --primary:#fff;
  --positive:#3fc07a; --pill-positive-bg:#172a1d; --pill-positive-ink:#3fc07a;
  --negative:#e5566f; --pill-negative-bg:#2c1a20; --pill-negative-ink:#e5566f; --grid:#2b2b2b; }
```
Map these onto the brand's roles when a design code exists (ground/surface/ink/muted/border/primary/danger/success).

## 8. Density
Sparse (6-25 data points: homes, settings): padding 20-24, rows 56-92, body 14-16. Medium (25-50: analytics, finance,
lists): rows 44-56, padding 16-24. Dense (~120: monitoring, research, long sessions): body 13, list rows 28, table rows
42, framed with generous outer air. Density moves three settings together (pitch, padding, type). Placed space reads
calm; leftover space (grid that doesn't fit the data, empty column, half-empty top bar, stretched card) reads unfinished.
Design for the account's real data size as well as the hoped-for one.

## 9. States
Real zero printed ("$0", "0%"); missing = small grey dash (never a 24px "--"); counts recompute per filter; an empty side
card shows reference data ("Nothing sold out yet - last Sunday: …"); red is a signal (one red mark per object max);
empty section keeps frame + header + one sentence spanning the block (+ add link); empty chart draws its zero line;
first run keeps frame/title and puts the first action where data will appear (setup progress at true %); loading = final
layout with flat grey bars at real size; error inside the failed block with last-good time + Retry; stale data = stamp +
refresh or a quiet notice; limits as a bar at true ratio with both ends labelled ("12.7k of 20.0k").

## 10. Phone and tablet (house rules)
Sidebar → 48px top bar with screen name + menu sheet (nav, switcher, account) + one action, or a bottom bar of 4-5
labelled destinations. Margins 16-20; targets ≥ 44px; data 14px, sublines ≥ 12. Title stays (20-24px); header actions
into a kebab except the primary. Filters → one chip row or a Filters sheet; the first list row in the top 60% of the
screen. KPIs → 2-column grid (even count after a full-width lead) or label-left/value-right list. ≤ 1 row of controls
above a chart; charts full width 160-200px, 3-4 x labels, legend dots above. Tables → two-line rows below ~640px (identity
+ key number on line 1; other fields grey on line 2; action right) - fields move, never vanish; a table that must stay a
table scrolls in its own frame with a fixed first column. Blocks with actions move up (low stock + Reorder becomes a
summary row above the list). Multi-pane: one region at a time; back returns to the list at its scroll. Tablet 641-1100:
sidebar folds, tables keep 4-5 columns with sublines.

## 11. Tells → replacements
dark/tinted sidebar + coloured pill + left bar → sidebar on the ground, neutral pill · "Welcome back, Alex 👋" → noun
title · 4 KPI cards with icon circles → divided container, label over value · green "+12.5%" pill everywhere → delta in
words with window, grey for zero · sparkline on every KPI → trend in its own chart · KPI 36-48px bold brand colour →
24-30px ink · gradient smoothed area chart with dots → 2px straight line, no fill or ≤ 14% tint · rainbow palette → one
hue per chart, ≤ 4 hues per screen · gridlines every 20px + legend for one series → 3-5 faint lines, no legend · fat donut
with slice labels → thin ring + legend-as-table · 16-24px radius + border + big shadow → border or tone step · zebra +
uppercase headers + checkbox/avatar/chip/kebab on every row → rules, alignment, one status mark · left-aligned
proportional numbers → right-aligned tabular · saturated chips with white text → pale tint + dark text · accent on every
button → near-black primary · empty top bar with bell + avatar → none, or search/switcher · pagination under 5 rows →
capped rows + View all · Inter on #f8f8f8 with white 12px cards and no hue on data → one face from the brief + one
signature element.
