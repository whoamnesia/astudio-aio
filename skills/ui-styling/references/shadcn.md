# shadcn/ui with astudio tokens

shadcn/ui is copy-in components built on Radix (or Base UI) + Tailwind. Components live in your repo
(`components/ui/*`), so they are yours to restyle.

## Setup
```bash
npx shadcn@latest init          # creates components.json, lib/utils.ts (cn), CSS variables
npx shadcn@latest add button input label dialog dropdown-menu sheet tabs table sonner form
```
Search the ecosystem before writing a custom component (shadcn registry, community registries) - but review code
before adding a registry item.

## Map astudio roles to shadcn variables
shadcn expects these variables (Tailwind v4 projects define them in `:root`/`.dark` and map with `@theme inline`).
Point them at astudio roles so one source drives both:
```css
:root {
  --background: var(--color-ground);      --foreground: var(--color-ink);
  --card: var(--color-raised);            --card-foreground: var(--color-ink);
  --popover: var(--color-raised);         --popover-foreground: var(--color-ink);
  --primary: var(--color-primary);        --primary-foreground: var(--color-on-primary);
  --secondary: var(--color-surface);      --secondary-foreground: var(--color-ink);
  --muted: var(--color-surface);          --muted-foreground: var(--color-muted);
  --accent: var(--color-primary-subtle);  --accent-foreground: var(--color-ink);
  --destructive: var(--color-danger);
  --border: var(--color-border);          --input: var(--color-control-border);   --ring: var(--color-focus);
  --radius: 0.5rem;
}
```
(If tokens.css already switches light/dark on `[data-theme]` / `prefers-color-scheme`, these aliases follow
automatically; shadcn's `.dark` class can be mapped with `@custom-variant dark (&:where(.dark, .dark *))` or by
setting `data-theme` alongside.)

## Restyling rules
- Change variants in the component file (`cva` variants) to match the design code: radius logic, heights, the one
  primary, focus ring, motion tokens. Delete variants the product does not use.
- Keep Radix behaviour (focus management, keyboard, aria) - restyle, don't rebuild.
- Popover/dropdown content: `origin-[var(--radix-popover-content-transform-origin)]` for origin-aware scaling; dialogs
  stay centred.
- Toasts with Sonner: position consistent with the layout, durations 4-6s, action buttons for undo.
- Forms: shadcn Form (react-hook-form + zod) - FormLabel visible, FormDescription as helper, FormMessage below the field;
  validate on blur; focus first error on submit.
- Data tables: TanStack Table + shadcn Table; right-align numeric columns, `tabular-nums`, sortable headers with
  `aria-sort`, sticky header, empty/loading/error states.
- Don't ship the default zinc look unchanged - it is the "kit face". Apply the brand's type, radius logic and colour
  roles, and give the product one signature element.
