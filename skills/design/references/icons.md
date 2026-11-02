# Icon design system

## First: do you need custom icons?
For product UI, a mature open library is usually better (Lucide, Phosphor, Tabler, Heroicons, Material Symbols, SF
Symbols on iOS): complete, consistent, accessible, maintained. Design custom icons when the brand needs ownable
pictograms (marketing, wayfinding, packaging, a signature product set) or concepts no library covers - then match the
chosen library's metrics if they will sit together.

## Grid and metrics
- Canvas 24×24 (UI) with 2px padding → live area 20×20; also 16 (dense), 32/48 (marketing). Design on 24, check at
  16-20 and 48.
- Keylines: circle ⌀20, square 18×18, portrait rectangle 16×20, landscape 20×16 - shapes of different geometry look the
  same size when they follow keylines (optical sizing).
- Stroke: one weight for the set (1.5px refined, 2px standard, 2.5px bold/accessibility); round or square caps and joins
  decided once from the brand's shape language; corner radius consistent (e.g. 2px on 24 grid).
- Pixel fit: horizontal/vertical strokes on whole or half pixels so they render crisp at 1×.
- Styles: outline (UI default), filled (selected states, mobile nav, small sizes), duotone (marketing; second tone at
  ~30% or a brand tint), rounded/sharp variants. One style per hierarchy level; filled = active/selected, outline = rest
  is a common, clear pairing. Database: `search.py "<style>" -d icon-style`.

## Drawing rules (SVG)
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none"
     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>
</svg>
```
`currentColor` so icons inherit text colour; no hard-coded fills in UI icons; few anchors; exact angles (0/45/90°, 30/60°
where the brand uses them); simplify metaphors to the essential silhouette; consistent visual weight (a filled dot
balances a thin outline); standard metaphors for solved concepts (home, search, settings, user, bell, trash, plus,
close, chevrons, share, download, edit, filter, calendar, cart). Check each at 16px - if it mushes, remove detail.

## Accessibility and delivery
Decorative icons `aria-hidden="true"`; meaningful standalone icons get `role="img"` + `<title>` or a visually hidden
label; icon-only buttons are labelled on the button. Meaningful icons ≥ 3:1 contrast. Deliver: individual optimised SVGs
(`<name>.svg`, kebab-case), a sprite (`<symbol id>` + `<use href>`), a React component set if the project uses React,
PNG exports only where needed, and an overview sheet (all icons at 24 and 48, light and dark).
