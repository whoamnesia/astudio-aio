#!/usr/bin/env python3
"""astudio logo kit - audit, test sheet, colour variants and web icon set for SVG logos.

Commands
  logo_kit.py audit a.svg [b.svg ...]
        structure checks: viewBox, live <text>, rasters, filters/masks, colour count, gradients, strokes,
        coordinate bloat, missing <title>. Score /100 with FAIL/WARN items.
  logo_kit.py concepts a.svg b.svg c.svg --names A B C --colors "#E0592A/#14161C" "#..." "#..." [--lockups la.svg lb.svg lc.svg] [--recommend C]
        client-facing concept sheet: each concept in black (form) and in a proposed colour pairing, app icon, 32/16px
  logo_kit.py sheet a.svg [b.svg ...] --out preview.html [--names "A" "B"] [--brand "#hex"] [--lockups l1.svg ...]
        HTML test sheet: size ladder 16-256 px, light/dark/brand grounds, one-colour black and white,
        squint blur, mirror and 180-degree readings, browser-tab / app-icon / header / card / avatar contexts.
        Render it with: node render.cjs shots preview.html --widths 1440 --no-full
  logo_kit.py variants mark.svg --out dir [--mono "#hex"] [--icon-bg "#hex"] [--icon-fg "#fff"] [--name brand]
        writes <name>-color/-black/-white/-mono.svg, <name>-app-icon.svg (symbol at 64% on a 22.5%-radius tile),
        <name>-favicon.svg (adapts to dark mode)
  logo_kit.py webicons favicon-source.svg --out dir [--name brand] [--bg "#hex"]
        PNGs 16/32/48/180/192/512 (needs render.cjs + Playwright), favicon.ico, site.webmanifest, <head> snippet
Stdlib (+ Pillow for .ico if installed).
"""
import argparse, base64, html, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COLOR_ATTR = re.compile(r'(fill|stroke|stop-color)\s*=\s*"(#[0-9a-fA-F]{3,8}|rgb[^"]*|[a-zA-Z]+)"')
COLOR_STYLE = re.compile(r'(fill|stroke|stop-color)\s*:\s*(#[0-9a-fA-F]{3,8}|rgb\([^)]*\)|[a-zA-Z]+)')


def read(p):
    return Path(p).read_text(encoding="utf-8")


def colours(svg):
    vals = [v for _, v in COLOR_ATTR.findall(svg)] + [v for _, v in COLOR_STYLE.findall(svg)]
    return sorted({v.lower() for v in vals if v.lower() not in ("none", "transparent", "currentcolor", "inherit")})


def audit(path):
    s = read(path)
    items, score = [], 100

    def add(sev, msg, pts):
        nonlocal score
        items.append((sev, msg)); score -= pts
    vb = re.search(r'viewBox\s*=\s*"([\d.\s-]+)"', s)
    if not vb:
        add("FAIL", "no viewBox - mark will not scale predictably", 20)
    else:
        x, y, w, h = map(float, vb.group(1).split())
        if abs(w - h) > 1 and "lockup" not in str(path).lower() and "horizontal" not in str(path).lower():
            add("WARN", f"symbol viewBox not square ({w:g}x{h:g}) - fine for lockups, not for symbols/app icons", 3)
    if re.search(r"<text\b", s):
        add("FAIL", "live <text> - letterforms must be outlined paths in a master file", 20)
    if re.search(r"<image\b|data:image/(png|jpe?g|webp)", s):
        add("FAIL", "embedded raster - a logo master is vector only", 20)
    if re.search(r"<filter\b|filter\s*=|feGaussianBlur|feDropShadow", s):
        add("FAIL", "SVG filter (blur/shadow/glow) - not reproducible in print, embroidery or one colour", 15)
    if re.search(r"<mask\b|<clipPath\b", s):
        add("WARN", "mask/clipPath - bake into paths for the master (tools and cutters handle them poorly)", 5)
    g = len(re.findall(r"<(linear|radial)Gradient\b", s))
    if g:
        add("WARN", f"{g} gradient(s) - keep a flat-colour master alongside; the mark must work in one colour", 5)
    c = colours(s)
    if len(c) > 3:
        add("WARN", f"{len(c)} colours ({', '.join(c[:6])}) - more than 3 weakens recall and reproduction", 8)
    if re.search(r'stroke-width|stroke\s*=\s*"(?!none)', s):
        add("WARN", "strokes present - expand to outlines for the master or verify scaling", 3)
    if re.search(r"\d+\.\d{4,}", s):
        add("WARN", "coordinates with 4+ decimals - round to 0-2 decimals (bloat hides misalignment)", 3)
    if not re.search(r"<title\b", s):
        add("WARN", "no <title> - add one for accessibility", 2)
    if re.search(r"transform\s*=\s*\"[^\"]*(rotate|matrix|skew)", s):
        add("WARN", "rotate/matrix/skew transforms - apply them to coordinates", 2)
    n_paths = len(re.findall(r"<(path|circle|rect|ellipse|polygon|line|polyline)\b", s))
    dlen = sum(len(m) for m in re.findall(r'\sd="([^"]*)"', s))
    if n_paths > 25 or dlen > 6000:
        add("WARN", f"complex mark ({n_paths} shapes, {dlen} path chars) - check it survives 16 px; consider a small-size cut", 5)
    return max(0, score), items, c


def variants(path, out, mono=None, icon_bg=None, icon_fg="#FFFFFF", name=None):
    s = read(path)
    name = name or Path(path).stem
    out = Path(out); out.mkdir(parents=True, exist_ok=True)

    def recolor(svg, col):
        svg = COLOR_ATTR.sub(lambda m: f'{m.group(1)}="{col}"' if m.group(2).lower() not in ("none", "transparent") else m.group(0), svg)
        svg = COLOR_STYLE.sub(lambda m: f"{m.group(1)}:{col}" if m.group(2).lower() not in ("none", "transparent") else m.group(0), svg)
        if not COLOR_ATTR.search(svg) and not COLOR_STYLE.search(svg):
            svg = svg.replace("<svg", f'<svg fill="{col}"', 1)
        return svg
    files = {f"{name}-color.svg": s, f"{name}-black.svg": recolor(s, "#000000"), f"{name}-white.svg": recolor(s, "#FFFFFF")}
    if mono:
        files[f"{name}-mono.svg"] = recolor(s, mono)
    vb = re.search(r'viewBox\s*=\s*"([\d.\s-]+)"', s)
    x, y, w, h = map(float, vb.group(1).split()) if vb else (0, 0, 256, 256)
    inner = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", s, flags=re.S)
    if icon_bg:
        fg_inner = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", recolor(s, icon_fg), flags=re.S)
        scale = 0.64 * 512 / max(w, h)
        tx = (512 - w * scale) / 2 - x * scale
        ty = (512 - h * scale) / 2 - y * scale
        files[f"{name}-app-icon.svg"] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><title>{name} app icon</title>'
                                        f'<rect width="512" height="512" rx="115" fill="{icon_bg}"/>'
                                        f'<g transform="translate({tx:.2f} {ty:.2f}) scale({scale:.4f})">{fg_inner}</g></svg>')
    dark_inner = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", recolor(s, "#FFFFFF"), flags=re.S)
    files[f"{name}-favicon.svg"] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {w:g} {h:g}">'
                                   f'<style>.d{{display:none}}@media (prefers-color-scheme:dark){{.l{{display:none}}.d{{display:inline}}}}</style>'
                                   f'<g class="l">{inner}</g><g class="d">{dark_inner}</g></svg>')
    for f, v in files.items():
        (out / f).write_text(v, encoding="utf-8")
        print("wrote", out / f)


def data_uri(path):
    return "data:image/svg+xml;base64," + base64.b64encode(Path(path).read_bytes()).decode()


def sheet(paths, out, names=None, brand="#1F2937", lockups=None):
    names = names or [Path(p).stem for p in paths]
    lockups = lockups or []
    css = """
    body{margin:0;font:14px/1.4 system-ui,sans-serif;background:#f4f4f2;color:#111}
    .c{padding:32px 40px;border-bottom:1px solid #ddd}.c h2{margin:0 0 4px;font-size:22px}.c p{margin:0 0 20px;color:#555}
    .row{display:flex;gap:28px;align-items:flex-end;flex-wrap:wrap;margin-bottom:22px}
    .cell{display:flex;flex-direction:column;align-items:center;gap:6px}.cell small{color:#777;font-size:11px}
    .tile{display:grid;place-items:center;border-radius:10px}.tile img{display:block}
    .lt{background:#fff}.dk{background:#111}.br{background:var(--brand)}.ph{background:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2240%22 height=%2240%22><rect width=%2240%22 height=%2240%22 fill=%22%23999%22/><path d=%22M0 40L40 0%22 stroke=%22%23bbb%22 stroke-width=%2214%22/></svg>')}
    .blk img{filter:brightness(0)}.wht img{filter:brightness(0) invert(1)}
    .blur img{filter:blur(3px)}.mir img{transform:scaleX(-1)}.rot img{transform:rotate(180deg)}
    .px img{image-rendering:pixelated}
    .tab{display:flex;align-items:center;gap:8px;background:#dee1e6;border-radius:8px 8px 0 0;padding:8px 12px;width:220px}
    .tab span{font-size:12px;color:#333;white-space:nowrap;overflow:hidden}
    .app{width:120px;height:120px;border-radius:27px;display:grid;place-items:center;box-shadow:0 4px 12px rgba(0,0,0,.15)}
    .hdr{display:flex;align-items:center;justify-content:space-between;background:#fff;width:520px;padding:14px 20px;border-radius:8px}
    .hdr nav{display:flex;gap:16px;color:#555;font-size:13px}
    .card{width:336px;height:192px;background:#fff;border-radius:6px;box-shadow:0 6px 20px rgba(0,0,0,.12);padding:22px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between}
    .avatar{width:110px;height:110px;border-radius:50%;overflow:hidden;display:grid;place-items:center}
    """
    blocks = []
    for p, n in zip(paths, names):
        u = data_uri(p)
        ladder = "".join(f'<div class="cell"><div class="tile lt px" style="padding:6px"><img alt="" src="{u}" width="{s}" height="{s}"></div><small>{s}px</small></div>' for s in (16, 24, 32, 48, 64, 128, 256))
        grounds = "".join(f'<div class="cell"><div class="tile {cls}" style="width:150px;height:150px"><img alt="" src="{u}" width="96" height="96"></div><small>{lbl}</small></div>'
                          for cls, lbl in (("lt", "light"), ("dk", "dark (colour)"), ("br", "brand ground"), ("ph", "busy photo"),
                                           ("lt blk", "one colour black"), ("dk wht", "one colour white"), ("lt blur", "squint test"),
                                           ("lt mir", "mirror"), ("lt rot", "rotated 180°")))
        ctx = (f'<div class="cell"><div class="tab"><img alt="" src="{u}" width="16" height="16"><span>{html.escape(n)} — home</span></div><small>browser tab 16px</small></div>'
               f'<div class="cell"><div class="app br"><img alt="" src="{u}" width="76" height="76" style="filter:brightness(0) invert(1)"></div><small>app icon</small></div>'
               f'<div class="cell"><div class="avatar br"><img alt="" src="{u}" width="70" height="70" style="filter:brightness(0) invert(1)"></div><small>circular avatar</small></div>'
               f'<div class="cell"><div class="hdr"><img alt="" src="{u}" height="32"><nav><span>Product</span><span>Pricing</span><span>Contact</span></nav></div><small>site header</small></div>'
               f'<div class="cell"><div class="card"><img alt="" src="{u}" width="56" height="56"><div style="font-size:12px;color:#444">{html.escape(n)}<br>hello@brand.com</div></div><small>business card</small></div>')
        blocks.append(f'<section class="c"><h2>{html.escape(n)}</h2><p>{html.escape(str(p))}</p><div class="row">{ladder}</div>'
                      f'<div class="row">{grounds}</div><div class="row">{ctx}</div></section>')
    for l in lockups:
        u = data_uri(l)
        blocks.append(f'<section class="c"><h2>Lockup: {html.escape(Path(l).stem)}</h2><div class="row">'
                      + "".join(f'<div class="cell"><div class="tile {c}" style="padding:24px"><img alt="" src="{u}" height="{h}"></div><small>{h}px tall · {c}</small></div>'
                                for c, h in (("lt", 24), ("lt", 48), ("dk wht", 48), ("br wht", 64), ("lt", 120))) + "</div></section>")
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>Logo test sheet</title><style>:root{{--brand:{brand}}}{css}</style></head><body><h1 style="padding:24px 40px 0;margin:0">Logo test sheet</h1>{"".join(blocks)}</body></html>')
    Path(out).write_text(doc, encoding="utf-8")
    print("wrote", out, "- render: node", HERE / "render.cjs", "shots", out, "--widths 1440 --no-full  (or open in a browser)")


def _recolor(svg, col):
    svg = COLOR_ATTR.sub(lambda m: f'{m.group(1)}="{col}"' if m.group(2).lower() not in ("none", "transparent") else m.group(0), svg)
    svg = COLOR_STYLE.sub(lambda m: f"{m.group(1)}:{col}" if m.group(2).lower() not in ("none", "transparent") else m.group(0), svg)
    if not COLOR_ATTR.search(svg) and not COLOR_STYLE.search(svg):
        svg = svg.replace("<svg", f'<svg fill="{col}"', 1)
    return svg


def _uri(svg_text):
    return "data:image/svg+xml;base64," + base64.b64encode(svg_text.encode()).decode()


def concepts(paths, out, names=None, colors=None, lockups=None, title="Logo concepts", recommend=None):
    """Client-facing concept sheet: each concept in black (form) and in a proposed colour pairing (fg/bg)."""
    names = names or [Path(p).stem for p in paths]
    colors = colors or []
    lockups = lockups or []
    cards = []
    for i, (p, n) in enumerate(zip(paths, names)):
        src = Path(p).read_text(encoding="utf-8")
        fg, bg = (colors[i].split("/") + ["#FFFFFF"])[:2] if i < len(colors) else ("#111111", "#FFFFFF")
        black, colour, white = _uri(_recolor(src, "#111111")), _uri(_recolor(src, fg)), _uri(_recolor(src, bg))
        lk = Path(lockups[i]).read_text(encoding="utf-8") if i < len(lockups) and lockups[i] else None
        lk_black = f'<img alt="" src="{_uri(_recolor(lk, "#111111"))}" style="height:56px;max-width:100%">' if lk else ""
        lk_col = f'<img alt="" src="{_uri(_recolor(lk, fg))}" style="height:56px;max-width:100%">' if lk else ""
        rec = ' <b class="rec">recommended</b>' if recommend and n == recommend else ""
        cards.append(f'''<section class="cc{' r' if rec else ''}"><h2>{html.escape(n)}{rec}</h2>
<div class="pair"><div class="t lt"><img alt="" src="{black}" width="120" height="120">{lk_black}</div>
<div class="t" style="background:{bg}"><img alt="" src="{colour}" width="120" height="120">{lk_col}</div></div>
<div class="ctx"><div class="app" style="background:{bg}"><img alt="" src="{colour}" width="62" height="62"></div>
<div class="app" style="background:{fg}"><img alt="" src="{white}" width="62" height="62"></div>
<div class="small" style="background:{bg}"><img alt="" src="{colour}" width="32" height="32"><img alt="" src="{colour}" width="16" height="16"></div>
<code>{html.escape(fg)} on {html.escape(bg)}</code></div></section>''')
    css = """body{margin:0;font:14px/1.45 system-ui,sans-serif;background:#efefec;color:#111}h1{margin:0;padding:28px 32px 8px;font-size:24px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:20px;padding:16px 32px 32px}
.cc{background:#fff;border-radius:14px;padding:20px;display:grid;gap:14px}.cc.r{outline:3px solid #111}.cc h2{margin:0;font-size:18px}
.rec{font-size:12px;background:#111;color:#fff;border-radius:99px;padding:2px 8px;margin-left:6px;vertical-align:middle}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:10px}.t{border-radius:10px;min-height:220px;display:grid;place-items:center;gap:12px;padding:18px}
.lt{background:#f6f6f4}.ctx{display:flex;align-items:center;gap:16px}.app{width:84px;height:84px;border-radius:19px;display:grid;place-items:center}
.small{display:flex;gap:10px;align-items:end;padding:10px;border-radius:10px;border:1px solid #e3e3e0}code{color:#555;font-size:12px}"""
    doc = (f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(title)}</title><style>{css}</style></head><body><h1>{html.escape(title)}</h1><div class="grid">{"".join(cards)}</div></body></html>')
    Path(out).write_text(doc, encoding="utf-8")
    print("wrote", out, "- render: node", HERE / "render.cjs", "shots", out, "--widths 1440")


def webicons(src, out, name="brand", bg=None):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    sizes = "16,32,48,180,192,512"
    r = subprocess.run(["node", str(HERE / "render.cjs"), "svg", str(src), "--sizes", sizes, "--out", str(out)] + (["--bg", bg] if bg else []),
                       capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    stem = Path(src).stem
    try:
        from PIL import Image
        imgs = [Image.open(out / f"{stem}-{s}.png") for s in (16, 32, 48)]
        imgs[0].save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=imgs[1:])
        print("wrote", out / "favicon.ico")
    except Exception as e:
        print("favicon.ico skipped (needs Pillow + PNGs):", e)
    manifest = {"name": name, "short_name": name, "icons": [
        {"src": f"/{stem}-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": f"/{stem}-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": f"/{stem}-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
        "theme_color": bg or "#ffffff", "background_color": bg or "#ffffff", "display": "standalone"}
    (out / "site.webmanifest").write_text(json.dumps(manifest, indent=2))
    head = (f'<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" href="/{name}-favicon.svg" type="image/svg+xml">\n'
            f'<link rel="apple-touch-icon" href="/{stem}-180.png">\n<link rel="manifest" href="/site.webmanifest">')
    (out / "head-snippet.html").write_text(head)
    print("wrote site.webmanifest, head-snippet.html\n" + head)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("audit"); a1.add_argument("svgs", nargs="+")
    a2 = sub.add_parser("sheet"); a2.add_argument("svgs", nargs="+"); a2.add_argument("--out", default="logo-test-sheet.html")
    a2.add_argument("--names", nargs="*"); a2.add_argument("--brand", default="#1F2937"); a2.add_argument("--lockups", nargs="*")
    a5 = sub.add_parser("concepts"); a5.add_argument("svgs", nargs="+"); a5.add_argument("--out", default="logo-concepts.html")
    a5.add_argument("--names", nargs="*"); a5.add_argument("--colors", nargs="*", help='per concept "fg/bg", e.g. "#E0592A/#14161C"')
    a5.add_argument("--lockups", nargs="*"); a5.add_argument("--title", default="Logo concepts"); a5.add_argument("--recommend")
    a3 = sub.add_parser("variants"); a3.add_argument("svg"); a3.add_argument("--out", default="logo-kit")
    a3.add_argument("--mono"); a3.add_argument("--icon-bg"); a3.add_argument("--icon-fg", default="#FFFFFF"); a3.add_argument("--name")
    a4 = sub.add_parser("webicons"); a4.add_argument("svg"); a4.add_argument("--out", default="logo-kit/web"); a4.add_argument("--name", default="brand"); a4.add_argument("--bg")
    a = ap.parse_args()
    if a.cmd == "audit":
        for p in a.svgs:
            sc, items, cols = audit(p)
            print(f"== {p}: {sc}/100  colours: {', '.join(cols) or 'inherit'}")
            for sev, m in items:
                print(f"  {sev:4} {m}")
            if not items:
                print("  clean structure - now LOOK at it at 16px and 512px")
    elif a.cmd == "sheet":
        sheet(a.svgs, a.out, a.names, a.brand, a.lockups)
    elif a.cmd == "concepts":
        concepts(a.svgs, a.out, a.names, a.colors, a.lockups, a.title, a.recommend)
    elif a.cmd == "variants":
        variants(a.svg, a.out, a.mono, a.icon_bg, a.icon_fg, a.name)
    else:
        webicons(a.svg, a.out, a.name, a.bg)


if __name__ == "__main__":
    main()
