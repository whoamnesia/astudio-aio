# Making the web feel native on phones

Most "janky on mobile" reports are not animation problems - they are a tap delay, a grey flash, a hover that won't let
go, a page that zooms into an input. These bugs do not reproduce in desktop device emulation.

## Symptom table
| Problem | Fix |
|---|---|
| Hover state stuck after tap | wrap hover styles in `@media (hover: hover) and (pointer: fine)` (Tailwind v4 `hover:` already is) |
| Grey/blue flash on tap | `html { -webkit-tap-highlight-color: transparent; }` + give every tappable an `:active` state |
| Wrong height / bottom button under the URL bar | `100dvh` for app shells, `100svh` for heroes (never `100vh`) |
| Page zooms into an input | input/select/textarea font-size ≥ 16px (never `maximum-scale=1`) |
| Tap feels laggy | feedback on press (`:active`, `pointerdown`), `touch-action: manipulation` on controls |
| Pull-to-refresh/rubber band hijacks an app | `html, body { overscroll-behavior: none }` in app-like UIs; `overscroll-behavior: contain` on inner scrollers/sheets |
| Content stops at the notch | `viewport-fit=cover` + `env(safe-area-inset-*)` padding on fixed headers, tab bars, sheets, toasts |
| Long-press selects button text | `user-select: none; -webkit-touch-callout: none` on controls only (never on body text) |
| Carousel scrolls the page vertically | `touch-action: pan-y` on a horizontal gesture surface; or native `scroll-snap-type: x mandatory` |
| Status bar colour mismatched | `<meta name="theme-color" media="(prefers-color-scheme: light|dark)" content="…">` matching the top of the page |
| Keyboard covers the input | `interactive-widget=resizes-content` in the viewport meta; scroll the field into view on focus |
| Right in Chrome emulation, wrong on the phone | test on hardware: dev server on 0.0.0.0, open by LAN IP, Safari Web Inspector / chrome://inspect |

## Baseline (ship before the first component)
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0a0a0a">
```
```css
html { -webkit-tap-highlight-color: transparent; -webkit-text-size-adjust: 100%; }
input, textarea, select { font-size: max(16px, 1rem); }
button, a, [role="button"] { touch-action: manipulation; }
button, [role="button"], .chip, .tab { user-select: none; -webkit-user-select: none; }
.app-header { padding-top: env(safe-area-inset-top); }
.tab-bar, .bottom-cta { padding-bottom: calc(.75rem + env(safe-area-inset-bottom, 0px)); }
@media (hover: hover) and (pointer: fine) { /* all :hover rules */ }
```
Keyboards: `inputmode="numeric|decimal|tel|email|search"`, `type="email|tel|url"`, `autocomplete` tokens
(`one-time-code`, `email`, `tel`, `street-address`, `cc-number`), `autocapitalize="none"` and `autocorrect="off"` on
codes/usernames, `enterkeyhint="send|search|done|next"`.

## Mobile layout rules
- Margins 16-20px; body 16-18px; line length 35-60 characters; headings ≤ 2 lines.
- Targets ≥ 44×44 with ≥ 8px between; extend hit areas with padding/pseudo-elements for small icons.
- Thumb zone: frequent actions in the lower half; destructive actions away from the primary.
- Bottom navigation for app-like web (≤ 5 labelled items); a sticky bottom CTA only for the page's one action.
- Sheets from the bottom for secondary tasks (drag handle, swipe-down + visible close, safe-area padding, focus trap).
- Images: portrait crops, `sizes` correct for 390px, AVIF/WebP, lazy below the fold; avoid heavy video autoplay on
  cellular (`prefers-reduced-data` where supported; poster image).
- Performance on mid-range Android: limit JS, avoid large blur/backdrop filters, cap 3D DPR, test throttled.

## Never ship
`user-scalable=no` / `maximum-scale=1`; ungated `:hover`; `100vh` app shells; press feedback only on click;
`touchmove + preventDefault` to stop scrolling; `user-select: none` on body; `touch-action: none` on something users must
scroll past; `env()` without `viewport-fit=cover`; one `theme-color` for both schemes; UA sniffing for touch; claiming
it's fixed from emulation alone.
