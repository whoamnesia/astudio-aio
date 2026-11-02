# Tailwind CSS v4

## Setup
```bash
npm i -D tailwindcss @tailwindcss/vite        # Vite
npm i -D tailwindcss @tailwindcss/postcss     # Next.js / PostCSS
```
```js
// vite.config.ts
import tailwindcss from '@tailwindcss/vite'; export default { plugins: [tailwindcss()] }
// postcss.config.mjs
export default { plugins: { '@tailwindcss/postcss': {} } }
```
```css
/* app.css */
@import "tailwindcss";
@import "./design-tokens/tailwind-theme.css";  /* or paste its :root + @theme blocks here (remove its own @import) */
```
v4 is CSS-first: no `tailwind.config.js` needed. Content detection is automatic (`@source "../packages/ui"` to add
paths). Upgrade from v3: `npx @tailwindcss/upgrade`.

## Theme
```css
@theme {                       /* creates utilities AND :root variables */
  --font-display: "Unbounded", system-ui, sans-serif;   /* font-display */
  --text-hero: clamp(3rem, 1rem + 9vw, 9rem);           /* text-hero */
  --radius-card: 16px;                                   /* rounded-card */
  --ease-out-strong: cubic-bezier(.22,1,.36,1);          /* ease-out-strong */
  --breakpoint-3xl: 120rem;                              /* 3xl: */
}
@theme inline {                /* utilities that point at runtime variables (theme switching) */
  --color-ground: var(--ds-ground);                      /* bg-ground, text-ground, border-ground… */
}
```
- Namespaces: `--color-*`, `--font-*`, `--text-*` (with optional `--text-*--line-height`), `--font-weight-*`,
  `--tracking-*`, `--leading-*`, `--breakpoint-*`, `--container-*`, `--spacing` (single base, `p-4` = 4×), `--radius-*`,
  `--shadow-*`, `--inset-shadow-*`, `--drop-shadow-*`, `--blur-*`, `--perspective-*`, `--aspect-*`, `--ease-*`,
  `--animate-*`.
- Reset a namespace: `--color-*: initial;` then define only the brand roles (prevents off-palette utilities).
- Dark mode: default is `prefers-color-scheme`. Class/attribute toggle:
  `@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));`
- Custom utilities: `@utility content-auto { content-visibility: auto; }`. Custom variants: `@custom-variant`.
- `@layer base { … }` for element defaults (body font, selection, focus ring).

## Useful v4 utilities
`text-balance`/`text-pretty` · `size-*` · `min-h-svh`/`min-h-dvh` · container queries `@container` + `@md:…` ·
`not-*`, `in-*`, `has-*`, `group-has-*`, `peer-*` variants · `starting:` (for @starting-style) · `inert:` ·
`motion-safe:`/`motion-reduce:` · `forced-colors:` · `pointer-coarse:`/`pointer-fine:` · `field-sizing-content` ·
`scheme-dark`/`scheme-light` · 3D transforms (`rotate-x-*`, `perspective-*`, `transform-3d`) · `bg-linear-to-r`,
`bg-radial`, `bg-conic` (use sparingly).

## Patterns
```html
<!-- Button with all states -->
<button class="inline-flex h-10 items-center gap-2 rounded-md bg-primary px-4 text-sm font-semibold text-on-primary
  transition-[background-color,transform] duration-150 ease-out hover:bg-primary-hover active:scale-[.97]
  focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus
  disabled:cursor-not-allowed disabled:opacity-60">Book a table</button>

<!-- Responsive split that becomes a stack -->
<section class="grid gap-8 px-4 md:grid-cols-12 md:px-8">
  <h2 class="text-balance font-display text-4xl md:col-span-5">Rooms</h2>
  <div class="md:col-span-7">…</div>
</section>
```
Avoid: `h-screen` (use `min-h-svh`), arbitrary colours, `transition-all`, `animate-bounce`, stacking ten utilities
for something a token should name.
