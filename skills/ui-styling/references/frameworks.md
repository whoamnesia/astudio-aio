# Framework notes

Detailed, current guidelines per stack: `python3 <root>/scripts/search.py "<concern>" --stack <stack>` (react, nextjs,
vue, nuxtjs, nuxt-ui, svelte, astro, angular, laravel, html-tailwind, shadcn, threejs, react-native, flutter,
swiftui, jetpack-compose …). Quick notes:

## Static HTML (astudio default for greenfield sites)
One folder: `index.html`, `styles.css` (imports or inlines tokens.css), `main.js` (module, deferred), `assets/`.
No build step; opens from the file system; deploy anywhere. Progressive enhancement: content and links work without
JS; JS adds the live thing and motion. Use `<script type="module">` and native features (dialog, popover, details).

## Next.js (App Router)
Server Components by default; `"use client"` only for interactive leaves. `next/font/google` (subset `cyrillic` when
needed) and `next/image`. Metadata API for title/description/OG/theme-color (`export const viewport = { themeColor }`).
Tokens in `app/globals.css`. Avoid client-side waterfalls; stream with Suspense; no layout reads during render.
GSAP/Three: dynamic import with `ssr: false` for heavy client-only scenes; `useGSAP` for cleanup.

## React (Vite)
Component per file, props typed, composition over configuration; Motion (`motion/react`) for interactive animation,
CSS for predetermined; React 19: actions/`useOptimistic` for forms, `use` for promises.

## Vue / Nuxt
`<script setup lang="ts">`; scoped styles or Tailwind; `@nuxt/fonts`, `@nuxt/image`; `useHead` for meta; Nuxt UI if
already used (theme via its app config, map to tokens).

## Svelte / SvelteKit
Runes (`$state`, `$derived`, `$props`); built-in transitions (`fly`, `fade`) with reduced-motion checks; `+page.ts`
load functions; `svelte:head` for meta.

## Astro
Islands: ship zero JS by default, `client:visible` for the live thing; `astro:assets` `<Image>`; content collections for
menus/catalogues; view transitions via `<ClientRouter />`.

## Multi-page structure
Shared layout (header/footer), page-level `h1`, consistent section components fed with page data, one CSS entry with
tokens, per-page meta. Generate sitemap/robots for production sites.
