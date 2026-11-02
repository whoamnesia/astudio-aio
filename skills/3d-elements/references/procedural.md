# Original 3D in code

When no honest free asset fits, or the object must be ownable, build it.

## 1. Choose the lightest technique that achieves the look
| Look | Technique | Cost |
|---|---|---|
| Card/tile depth, tilt, flip, cube, orbit | CSS 3D transforms (`perspective`, `transform-style: preserve-3d`, `rotateX/Y`, `translateZ`) | tiny, no WebGL |
| Isometric illustration, extruded type look | SVG with three tonal faces (light/mid/dark of a brand hue) on an isometric grid (30°) | tiny |
| 3D-looking icons/renders | render once (Three.js offline or 3dicons CC0) → WebP/AVIF images | small |
| Abstract hero form (blob, torus knot, stacked discs, folded ribbon, crystal) | Three.js primitives + MeshPhysical/standard material + HDRI | medium |
| Living background field (noise, gradient mesh, waves, grain) | full-screen fragment shader on a plane | medium (per-pixel - keep it simple) |
| Particles, point clouds, the logo dissolving | `THREE.Points` with BufferGeometry, custom shader | medium |
| Extruded logo / 3D wordmark | SVGLoader → `ExtrudeGeometry` (bevel) | medium |

## 2. Extruded logo (from the astudio logo SVG)
```js
import { SVGLoader } from 'three/addons/loaders/SVGLoader.js';
const data = new SVGLoader().parse(svgText);           // the logotype skill's master SVG (paths only)
const group = new THREE.Group();
for (const path of data.paths) {
  const shapes = SVGLoader.createShapes(path);          // respects holes (evenodd)
  const geo = new THREE.ExtrudeGeometry(shapes, { depth: 24, bevelEnabled: true, bevelThickness: 3, bevelSize: 2, bevelSegments: 4, curveSegments: 24 });
  group.add(new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: path.color, roughness: .35, metalness: .1 })));
}
group.scale.set(.01, -.01, .01);                        // SVG y-down → three y-up; centre with Box3 afterwards
```
A coin/medal treatment: extrude the symbol onto a cylinder face (CylinderGeometry with rim), slow ambient rotation
(reduced motion: still at 20°), env-mapped metal. Keep the logo's proportions; never distort the mark.

## 3. Abstract forms that carry an idea
Derive the form from the subject inventory (direction.md): a bakery's dough fold → a soft folded ribbon (TubeGeometry
along a curve with MeshPhysical sheen); a logistics route → a line extruded along the real route; a sound product → a
waveform lathe (LatheGeometry from audio-like points); finance → stacked discs at real proportions of the data.
Generic floating spheres and blob gradients are the 3D version of slop - give the form a reason.

## 4. Shader background (keep it calm)
```glsl
// fragment: slow 2-colour noise field in brand tones; uTime advances only when visible and motion is allowed
uniform float uTime; uniform vec3 uA; uniform vec3 uB; varying vec2 vUv;
float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453); }
float noise(vec2 p){ vec2 i=floor(p), f=fract(p); vec2 u=f*f*(3.-2.*f);
  return mix(mix(hash(i),hash(i+vec2(1,0)),u.x), mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),u.x), u.y); }
void main(){ float n = noise(vUv*3. + uTime*.03) * .6 + noise(vUv*7. - uTime*.02) * .4;
  gl_FragColor = vec4(mix(uA, uB, smoothstep(.2,.8,n)), 1.); }
```
Run at reduced resolution for full-screen fields (render target at 0.5 scale or CSS-scaled canvas), cap DPR at 1.5, stop
when off-screen. Text over it needs ≥ 4.5:1 everywhere the field moves - test the darkest/lightest frames.

## 5. CSS 3D card tilt (no WebGL)
```css
.tilt { perspective: 900px; } .tilt__card { transform-style: preserve-3d; transition: transform 300ms cubic-bezier(.22,1,.36,1); }
.tilt__card .layer { transform: translateZ(40px); }
@media (prefers-reduced-motion: reduce) { .tilt__card { transform: none !important; } }
```
```js
card.addEventListener('pointermove', e => { const r = card.getBoundingClientRect();
  const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
  card.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 10}deg)`; });
card.addEventListener('pointerleave', () => card.style.transform = '');
```
Only on fine pointers; ±6-12° max; one tilted element per view, not every card.

## 6. Isometric SVG
30° isometric: x-axis to (cos30, sin30) = (0.866, 0.5). Draw top face lightest, left mid, right darkest from one brand
hue via palette.py ramp (e.g. 300 / 500 / 700). Consistent light direction across the whole page.
