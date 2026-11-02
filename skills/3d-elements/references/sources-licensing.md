# Free 3D sources, licences and the asset pipeline

Full list with notes: `python3 <root>/scripts/search.py "<object>" -d 3d-source -n 8` (data/3d-sources.csv).

## Sources (use in this order of licence safety)
| Source | What | Licence |
|---|---|---|
| Poly Haven (polyhaven.com) | realistic models, **HDRIs** (lighting), PBR textures | CC0 |
| ambientCG (ambientcg.com) | PBR materials, HDRIs | CC0 |
| Kenney (kenney.nl) | consistent low-poly kits, game-like props | CC0 |
| Quaternius (quaternius.com) | low-poly, often rigged + animated characters/environments | CC0 |
| 3dicons (3dicons.co) | 3D-styled icon renders + sources | CC0 |
| Smithsonian Open Access 3D (3d.si.edu) | scanned museum objects | CC0 items only |
| Poly Pizza (poly.pizza) | low-poly anything | CC0 or CC-BY per model |
| Sketchfab (downloadable, license-filtered) | huge variety | CC0 / CC-BY per model (avoid NC, ND, NoAI tags) |
| Khronos glTF Sample Assets | reference PBR models | per model (CC0/CC-BY) |
| NASA 3D Resources | space models | free under NASA media guidelines; no endorsement, no insignia as branding |
| pmndrs market (market.pmnd.rs) | R3F-ready GLBs, materials | mostly CC0 - check item |
| Spline Community | remixable Spline scenes | per file |
| Mixamo | character rigs/animations | free with Adobe account; no redistribution of raw files |
| Fab free content | high-quality props | Fab Standard License - read for web use |

## Licence rules
- CC0: use freely, credit appreciated. CC-BY: credit visibly (title, author, licence, link) - in a credits section or
  footer. CC-BY-SA: share-alike - avoid for commercial brand work. NC (non-commercial), ND (no derivatives), "NoAI" -
  do not use for client work. Unknown licence → don't use it, say so.
- Record every asset in the report: title — author — licence — source URL — where credited — modifications made.
- A found model represents "a chair", not the client's chair; label it as illustrative if it could be mistaken.

## Pipeline (model → web)
1. Download glTF/GLB (preferred) or FBX/OBJ → convert to GLB (Blender export, or `gltf-transform` CLI).
2. Inspect: scale (1 unit = 1 m), pivot at the base/centre, up axis Y, single-sided where possible, materials PBR
   (metallicRoughness), no hidden heavy meshes.
3. Optimise (review and pin the tool version in the project first):
   `npx @gltf-transform/cli optimize in.glb out.glb --compress meshopt --texture-compress webp --texture-size 2048`
   (or `--compress draco`; KTX2/UASTC for GPU-compressed textures where quality matters).
4. Budget check: file size, triangles, texture count/size, draw calls (`renderer.info`).
5. HDRI: 1k-2k `.hdr`/`.exr` from Poly Haven for lighting (`RGBELoader`/`EXRLoader` + PMREM, or drei `<Environment>`),
   background off unless the HDRI *is* the scene.
6. Poster still: render the final framing to PNG/WebP (screenshot the canvas via render.cjs element) as the loading and
   no-WebGL fallback.
