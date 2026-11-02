# 3D performance, fallbacks and accessibility

## Budgets (mid-range phone, hero scene)
| Item | Target |
|---|---|
| 3D payload (models + textures + HDRI) | ≤ 2-3 MB compressed (lazy-load anything below the fold) |
| Triangles | ≤ 100-300k visible |
| Draw calls | ≤ 50-100 (merge static meshes, instance repeats, share materials) |
| Textures | ≤ 2048px, KTX2/WebP, only maps you need |
| Pixel ratio | `min(devicePixelRatio, 2)`; full-screen shaders ≤ 1.5 or reduced-resolution buffers |
| Frame time | 16ms at 60Hz; measure on a production build at DPR 2 |
| Post-processing | priced per pixel - bloom/DoF/grain only with a reason, 1-2 passes |
| LCP / CLS | poster image is the LCP candidate (`fetchpriority="high"`); canvas box reserves space (aspect-ratio) |

Measure with `renderer.info` (calls, triangles, textures, programs) after `render()`, Chrome Performance panel, and
`stats-gl` while developing. Common wins: merge static geometry (BufferGeometryUtils.mergeGeometries), InstancedMesh /
BatchedMesh, LOD, frustum culling intact (recompute bounding spheres after edits), bake lighting/AO, avoid
transparent + DoubleSide pairs and multiple `transmission` materials, freeze shadow maps for static scenes, dispose
geometries/materials/textures on unmount, pause the loop off-screen and in hidden tabs, `frameloop="demand"` in R3F
for static scenes, lower DPR via PerformanceMonitor on slow devices.

## Fallback ladder
1. Poster still (same framing) - always present; shown while loading, on error, without WebGL, and under
   `prefers-reduced-data`.
2. Reduced motion - the scene in a static pose; no auto-rotate, parallax or scroll-scrub; controls still work on demand.
3. Low-power devices - lower DPR, disable post-processing and shadows, simplify materials.

## Accessibility
- Decorative canvas: `aria-hidden="true"`, poster `alt=""`. Informative 3D (a product the visitor explores): a text
  description nearby and the key views available as images or steps.
- Every interaction has HTML controls (buttons: rotate left/right, reset view, materials) - focusable, labelled, ≥ 44px
  on touch; keyboard arrows may rotate when the viewer has focus (`tabindex="0"`, visible focus ring, instructions).
- Do not hijack wheel or touch scrolling; never trap focus inside a canvas.
- Motion sickness: avoid large camera moves tied to scroll without reduced-motion alternatives; no flashing; slow loops
  (< 0.2 Hz oscillation) avoided.
- Contrast for any text over or near the scene measured on the actual frames.
