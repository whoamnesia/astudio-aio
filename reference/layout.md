# Layout and composition

How a page is put together: hierarchy, grid, margins, rhythm, voids, sections, navigation, endings and the phone.

## Contents
1. Hierarchy first
2. Margins and the grid
3. Where text sits
4. Space: rests versus holes
5. The frame: margins, balance, titles
6. Sections: carry the idea, vary the arrangement
7. Navigation
8. Endings
9. Responsive: the phone is a second composition
10. Spacing and sizing systems
11. How pages fail

## 1. Hierarchy first
Every screen has one focal point - name it before building and make it win through size, contrast, position or the
space around it. Squint: the page should reduce to two or three masses with clear size differences. Many similar
medium masses = nothing leads. Build hierarchy from size + weight + colour together, never size alone. Gestalt does
the grouping: proximity (related things close, unrelated far), similarity, common region, continuity.

## 2. Margins and the grid
```css
:root { --margin: clamp(1rem, 2.2vw, 2rem); --gutter: clamp(.75rem, 1.4vw, 1.5rem); }
.wrap { padding-inline: var(--margin); }
.grid { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--gutter); }
```
- One pair of equal margins and one grid for the whole page; every left edge is a column line.
- Standard grids (`studio-bar.md` §6): 12 columns desktop / 8 tablet / 4 phone, gutters 24/20/16, a 1200-1440px
  container or full-bleed with 32-80px margins. Award sites often let pictures and type run to the edges while text
  sits on the columns. Constrain the *measure* of text (`max-width` in ch), not the page.
- On very wide screens cap at ~1760-1920px or stop vw-type growing with clamp.
- Never draw the grid as decoration; it is felt through alignment.

## 3. Where text sits
- Pick 2-3 anchor lines for the whole page (e.g. margin + column 5) and reuse them. Six left edges = nothing decided.
- Off-centre beats centred: heading in the left third with its paragraph in the far columns; text docked at the edge
  of a picture; two short texts at opposite ends of one baseline.
- Centred is a decision: one axis, wide flanks, one element per screen - not a centred stack of heading, paragraph
  and two buttons.
- Long copy rows: heading left third, body right two-thirds, same split every row.

## 4. Space: rests versus holes
A large empty area is a **rest** when something closes it (the picture, a large headline spanning it, text docked
at both ends) and a **hole** when nothing does. Holes come from: section gaps stretched to 250-760px; text in one
half and nothing in the other; reveals that have not fired; a footer or lone heading stretched to 100vh; pinned
scenes holding nothing; pictures of different heights top-aligned.
Rules: sections 120-240px apart on desktop, 72-112px on phone; gaps between sections clearly larger than gaps inside;
no stretch of plain ground taller than ~half a screen; content present on the first paint; size sections to their
content (`min-height: 100vh` only for sections that truly fill the screen); one deliberate rest per page at most.
When a section looks empty, make the main element bigger or cut the section - do not add ornament.

## 5. The frame
- Left and right page margins equal at every width; the navigation sits on the same margins as content.
- Use the width set up: when text takes one side, the other side holds its picture, second column, list or figure.
- The first screen has one `h1` that says what this is (name + what it does / product + what it is for / event +
  date and place) at display size, ≤ 2 lines, present on the first paint, plus the primary action as a real button.
- Every section the visitor came for opens with a heading that names it ("Rooms", "Prices", "How it works").

## 6. Sections
- The idea reaches the last pixel: pricing, FAQ and footer speak the page's language (a menu-led page sets prices as
  menu lines; a name-led page ends with the name).
- No two neighbours share a layout. Label each section's shape (split, list, full-bleed, mosaic, statement, table,
  strip, index, pinned) - the same word twice in a row is the template showing.
- Alternate dense/empty, image/type, light/dark for rhythm. Break the system once, on purpose.
- A repeated module is for archives (work index, menu, schedule). Elsewhere repetition reads as a kit.
- Short pages are fine. Each section must carry a claim (copy.md).

## 7. Navigation
- Plain form: wordmark, 3-5 text links (single nouns), one action; on the page ground, no bar chrome.
- Fixed navigation must never cover content at any scroll position; check phone screenshots. Floating pill navs are
  where overlap usually happens.
- Phone: wordmark + one action in view; links in a full-screen sheet opened by a labelled button, or moved to the
  footer when there are only three. Navigation takes ≤ ~10% of the desktop first screen, one row on the phone.
- Current location visibly marked; skip link to main content; deep links for important states (URL reflects filters,
  tabs, pagination).

## 8. Endings
End on a designed scene, not a link-column sitemap: the name at full width, the hero repeated inverted, the one
contact fact set as a headline, or one quiet line. Practical facts (address, hours, email, legal) in the text face,
readable size, on the same anchor lines.

## 9. Responsive
- Design 390px as its own page, not the desktop squeezed: re-author line breaks, re-crop images to portrait
  (`object-position` per breakpoint or `<picture>`), keep one dominant thing on the first screen.
- Breakpoints by content, commonly 390 / 768 / 1024 / 1440. Mobile-first CSS. Container queries for components that
  live in several contexts.
- Margins 16-20px on phone; body 16-18px; touch targets ≥ 44px tall (WCAG minimum 24×24 CSS px with spacing).
- No horizontal page scroll ever; a row that must scroll sideways scrolls inside its own frame with a visible cut.
- `min-height: 100svh` for heroes, `100dvh` for app shells; `env(safe-area-inset-*)` with `viewport-fit=cover` for
  fixed bars.
- Tablet (641-1100px) is its own band, not "big phone" or "small desktop".

## 10. Spacing and sizing systems
- 4px base (8pt rhythm). Spacing scale e.g. 4 8 12 16 24 32 48 64 96 128 160 240.
- Density is three settings moved together: row pitch, padding and type size.
- Proportions speak: a 240px sidebar next to full content says "navigation serves content"; a 360px one says "peers".
- z-index scale (0 / 10 dropdown / 20 sticky / 30 overlay / 40 modal / 50 toast) - no arbitrary values.
- Radius: one logic; nested radius = outer radius − padding (concentric); capsules = height/2.

## 11. How pages fail
In a study of weak sites (< 6.8/10): the page is the category's stock template (logo-swap test fails); centred
headline + pill badge + two buttons + screenshot/tile grid; a distinctive hero then stock modules; a default typeface
with no character; text too small or low contrast; legibility lost over busy photos; undersized headline and no focal
point; never says what the thing is; thin content over many screens; sections with no picture; gates; a phone layout that is the
desktop shrunk; fixed elements sitting on content. Even top sites lose points for 9-13px body text, information
hidden behind the concept, the idea running out mid-page, and text over footage without a scrim.
