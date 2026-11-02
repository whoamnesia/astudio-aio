# Scene recipes: Three.js and React Three Fiber

Pin versions (check the latest stable at build time; examples assume three r17x+ ES modules).

## Vanilla Three.js hero object (static page)
```html
<div class="hero-3d" aria-hidden="true">
  <img class="hero-3d__poster" src="assets/hero-poster.webp" alt="" width="1200" height="1200">
  <canvas class="hero-3d__canvas"></canvas>
</div>
<script type="importmap">{ "imports": { "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
  "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/" } }</script>
<script type="module">
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';

const wrap = document.querySelector('.hero-3d'), canvas = wrap.querySelector('canvas');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
let renderer;
try { renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' }); }
catch { /* no WebGL: poster stays */ }
if (renderer) {
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 100); camera.position.set(0, 0.4, 4);
  const pmrem = new THREE.PMREMGenerator(renderer);
  new RGBELoader().load('assets/studio_small_1k.hdr', t => { scene.environment = pmrem.fromEquirectangular(t).texture; t.dispose(); });
  const group = new THREE.Group(); scene.add(group);
  new GLTFLoader().setMeshoptDecoder(MeshoptDecoder).load('assets/object.glb', g => {
    const m = g.scene; const box = new THREE.Box3().setFromObject(m); const s = 1.6 / box.getSize(new THREE.Vector3()).length();
    m.scale.setScalar(s); m.position.sub(box.getCenter(new THREE.Vector3()).multiplyScalar(s)); group.add(m);
    wrap.classList.add('is-ready');                       /* CSS fades canvas in, poster out */
  });
  const resize = () => { const { width, height } = wrap.getBoundingClientRect();
    renderer.setSize(width, height, false); camera.aspect = width / height; camera.updateProjectionMatrix(); };
  new ResizeObserver(resize).observe(wrap); resize();
  let px = 0, py = 0; wrap.addEventListener('pointermove', e => { const r = wrap.getBoundingClientRect();
    px = (e.clientX - r.left) / r.width - .5; py = (e.clientY - r.top) / r.height - .5; });
  let visible = true; new IntersectionObserver(([e]) => visible = e.isIntersecting).observe(wrap);
  const clock = new THREE.Clock();
  renderer.setAnimationLoop(() => {
    if (!visible || document.hidden) return;
    const t = clock.getElapsedTime();
    if (!reduce) { group.rotation.y += (px * .6 + t * .15 - group.rotation.y) * .05; group.rotation.x += (py * .3 - group.rotation.x) * .05; }
    renderer.render(scene, camera);
  });
}
</script>
<style>
.hero-3d { position: relative; aspect-ratio: 1; }
.hero-3d > * { position: absolute; inset: 0; width: 100%; height: 100%; }
.hero-3d__canvas { opacity: 0; transition: opacity 600ms cubic-bezier(.16,1,.3,1); }
.hero-3d.is-ready .hero-3d__canvas { opacity: 1; } .hero-3d.is-ready .hero-3d__poster { opacity: 0; }
</style>
```

## React Three Fiber
```jsx
import { Canvas } from '@react-three/fiber';
import { Environment, useGLTF, PresentationControls, ContactShadows, Bounds } from '@react-three/drei';
import { Suspense } from 'react';
function Model(props) { const { scene } = useGLTF('/object.glb'); return <primitive object={scene} {...props} />; }
useGLTF.preload('/object.glb');
export default function Hero3D() {
  return (
    <div className="hero-3d" aria-hidden="true">
      <Canvas dpr={[1, 2]} camera={{ fov: 30, position: [0, .4, 4] }} gl={{ antialias: true, alpha: true }}
              frameloop="demand" /* re-render only on change when nothing animates */>
        <Suspense fallback={null}>
          <Environment files="/studio_small_1k.hdr" />
          <PresentationControls global={false} polar={[-.2, .2]} azimuth={[-.6, .6]} snap>
            <Bounds fit clip observe margin={1.1}><Model /></Bounds>
          </PresentationControls>
          <ContactShadows position={[0, -.8, 0]} opacity={.35} blur={2.5} far={2} />
        </Suspense>
      </Canvas>
    </div>
  );
}
```
Next.js: load the component with `dynamic(() => import('./Hero3D'), { ssr: false })` and render the poster in its
place while loading. Use `useFrame` sparingly; `frameloop="demand"` + `invalidate()` for static scenes; `<Detailed>` for
LOD; `<Instances>` for repeats; `<PerformanceMonitor>` to lower DPR on slow devices; `useReducedMotion`-style checks to
disable auto-rotation.

## Lighting and materials
- HDRI environment for realistic PBR (Poly Haven "studio_small", "photo_studio" etc.); or key (directional, warm) +
  fill (hemisphere, cool, low) + rim light. Real-time shadows are expensive - prefer ContactShadows / baked AO.
- Brand colours on materials: `new THREE.Color('#C2410C')` is treated as sRGB and converted; roughness/metalness from
  the world (clay 0.9/0, brushed metal 0.35/1, glossy plastic 0.2/0, glass MeshPhysicalMaterial transmission 1 -
  transmission is costly: one object max).
- Matte/clay looks and toon shading suit illustrated brands; physical glass/metal suits premium products.

## Interaction patterns
- Pointer tilt (ambient, ±10-20°, eased), drag-to-rotate with limits (OrbitControls: `enableZoom=false`,
  `enablePan=false`, polar/azimuth limits, damping), click-to-swap materials (HTML buttons update material colour),
  hotspots (HTML labels via drei `<Html>` or CSS2DRenderer) that are real focusable buttons.
- Scroll-driven: GSAP ScrollTrigger `scrub: true` mapping progress to rotation/camera path; pin ≤ 1-3 screens; every held
  screen carries text; reduced motion → static frames per step.
- Never capture the wheel to rotate a model while the page should scroll (`enableZoom=false`), and keep touch scrolling
  possible (`touch-action: pan-y` on the canvas unless it is a deliberate drag surface with visible controls).

## Spline
```html
<script type="module">import { Application } from 'https://unpkg.com/@splinetool/runtime@1.9.0/build/runtime.js';
const app = new Application(document.getElementById('spline')); await app.load('https://prod.spline.design/<id>/scene.splinecode');</script>
<canvas id="spline" aria-hidden="true"></canvas>
```
Keep the poster fallback; Spline scenes can be heavy - export optimised, limit to one per page; React: `@splinetool/react-spline`.
