# Charts on app screens

Database: `search.py "<data shape / question>" -d chart` (25 data types with best chart, when not to use, volume
thresholds, accessibility notes, library suggestions). Draw charts with a library configured to these rules (Chart.js,
ECharts, Recharts, visx, Observable Plot) or hand-written SVG - never a library's defaults, never a picture of a chart.

## Which chart for which question
| Question | Form |
|---|---|
| Is it moving over time? | one line; area only with a fill ≤ 15% |
| How much per period? | columns, square corners (max 4px top radius) |
| How is it distributed? | histogram with equal bins |
| Who ranks? | sorted horizontal bar list; or the row fill as the bar in a one-figure list |
| What share? | thin ring or 100% stacked bar with 2px seams; 5 parts max (else bars) |
| How far to target? | progress bar, both ends labelled, fill = true ratio |
| How much of the plan is used? | a track as long as the plan, spent filled, committed lighter, overrun in negative colour |
| Drift from target per part? | bar per part with a 1px tick at the target (bullet) |
| Where? | map + a list carrying the magnitudes |
| Flow in/out? | columns above/below one zero line, signed captioned axis |
| Who is away when? | people × days timeline, each kind its own mark |
| When in the day vs last time? | rows on a shared axis: grey track, ink dot today, hollow tick comparison |
| Only a few numbers? | no chart - state the numbers |
Pair "per period + running total" once per screen, only when the total crosses a meaningful line.

## One question, one series
One series per chart is the norm (three max). Switch metrics with a control (segmented, dropdown, KPI tabs) instead of
overlaying lines. Plots 112-264px tall (median ~195), aspect 1.8-5.2. A series flat except one event gets ≤ 2/3 width,
~140px height, or a capped range with the off-scale peak labelled. Forecasts are dashed after "today" with the end value
labelled. What the brief asks to see over time is drawn on the first screen.

## Axes and gridlines
3-5 horizontal gridlines, 1px solid (~#e5e5e5 light, #2b2b2b dark), dashed allowed only in chart grids. No y-axis line;
the baseline is the one heavier line. 4-7 y ticks at round even steps, top tick above the maximum, integers for counts,
zero baseline for bars/counts; tick text 11-13px grey, never louder than the data. X labels 4-8, flat (never rotated),
first/last inside the plot, one step all the way; time on a time scale. Never a chart without a scale.

## Marks
Lines 1-3px (median 2), straight segments (smoothing invents values), no point markers except a hover dot. Bars square
or 4px top radius, stacked seams 1-2px. One hue per chart; the accent on the screen's main data element (today's series,
the current period, the breaking margin); neutral series in ink/grey are fine; one subject keeps one hue across the
screen; ≤ 4 hues per screen; status colours only for status.
Legends: none for a single series; otherwise ≤ 5 items as 5-8px dots + 12-14px grey labels in the card header, or a
legend-as-table (dot, name, value, change). Each swatch is the mark it explains (hatched swatch for a hatched bar).
Rings: thin (3-8px stroke on 90-180px), no slice labels, total in the centre or beside, never redundant with a list next
to it. Progress bars 4-24px tall, fully round, both ends labelled, no stub at zero. Tooltips: bare text or a plain box,
label and value on one line, keyboard-reachable.
Annotate the event that matters: a step/spike > ~3× usual change gets a 1px marker and a 12px label naming its cause
("Deploy a3f09c1"); reference lines (budget, SLO) 1px dashed with the label at the end. Labels never collide - rows above
the plot with leader lines; lay out after fonts load.
Short/empty histories drawn honestly: flat zero line, missing bars for empty periods, no padded range, no "No data"
illustration - but don't give one point the screen's largest plot.

## Accessibility
Data marks ≥ 3:1 against the background, labels ≥ 4.5:1; never colour alone (pattern/shape/direct labels); a text
summary (the finding) and a table alternative; keyboard-focusable points with values; `prefers-reduced-motion` disables
chart entrance animation (data readable immediately); locale-aware number/date formatting (`Intl.NumberFormat`).
