#!/usr/bin/env python3
"""astudio palette - OKLCH colour engine: ramps, semantic light/dark systems, contrast checks.

Commands
  palette.py contrast FG BG [FG BG ...]          WCAG 2.x contrast ratio + AA/AAA verdicts
  palette.py ramp HEX [--name primary]           11-step tonal ramp (50..950) with contrast vs white/black
  palette.py system --primary HEX [--accent HEX] [--neutral-chroma 0.012] [--ground light|dark|both]
                    [--style restrained|committed] [--css out.css] [--json out.json]
        Builds a complete semantic colour system (ground, surface, ink, muted, border, primary,
        on-primary, accent, success, warning, danger, info, focus, selection) for light and dark,
        nudging lightness until every text role reaches 4.5:1 and every UI role 3:1.
  palette.py info HEX                            hex -> rgb, hsl, oklch

Why OKLCH: equal lightness steps look equally light across hues, so ramps and dark themes stay
balanced without hand-tuning. Stdlib only.
"""
import argparse, json, math, sys

# ---------- conversions ----------

def hex2rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"bad hex: {h}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb2hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)


def s2l(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def l2s(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def rgb2oklab(rgb):
    r, g, b = (s2l(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def oklab2rgb(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(l2s(c) if c >= 0 else -l2s(-c) for c in (r, g, bb))


def rgb2oklch(rgb):
    L, a, b = rgb2oklab(rgb)
    C = math.hypot(a, b)
    H = math.degrees(math.atan2(b, a)) % 360
    return L, C, H


def in_gamut(rgb, eps=1e-4):
    return all(-eps <= c <= 1 + eps for c in rgb)


def oklch2rgb(L, C, H):
    """Gamut-map by reducing chroma (keeps hue and lightness)."""
    L = max(0, min(1, L))
    lo, hi = 0.0, C
    rgb = oklab2rgb((L, C * math.cos(math.radians(H)), C * math.sin(math.radians(H))))
    if in_gamut(rgb):
        return tuple(max(0, min(1, c)) for c in rgb)
    for _ in range(24):
        mid = (lo + hi) / 2
        rgb = oklab2rgb((L, mid * math.cos(math.radians(H)), mid * math.sin(math.radians(H))))
        if in_gamut(rgb):
            lo = mid
        else:
            hi = mid
    rgb = oklab2rgb((L, lo * math.cos(math.radians(H)), lo * math.sin(math.radians(H))))
    return tuple(max(0, min(1, c)) for c in rgb)


def oklch_hex(L, C, H):
    return rgb2hex(oklch2rgb(L, C, H))


def css_oklch(hexv):
    L, C, H = rgb2oklch(hex2rgb(hexv))
    return f"oklch({L * 100:.1f}% {C:.3f} {H:.1f})"

# ---------- contrast ----------

def lum(hexv):
    r, g, b = (s2l(c) for c in hex2rgb(hexv))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    return ("AAA" if r >= 7 else "AA" if r >= 4.5 else "AA-large/UI" if r >= 3 else "FAIL")

# ---------- builders ----------

RAMP_L = {50: .975, 100: .945, 200: .89, 300: .82, 400: .72, 500: .63, 600: .54, 700: .46, 800: .38, 900: .30, 950: .22}


def ramp(hexv):
    L0, C0, H = rgb2oklch(hex2rgb(hexv))
    out = {}
    for step, L in RAMP_L.items():
        # chroma peaks mid-ramp, falls toward white/black (perceptually natural)
        k = 1 - abs(L - 0.6) / 0.6
        C = max(0.0, C0 * (0.35 + 0.65 * k))
        out[step] = oklch_hex(L, C, H)
    return out


def fit_text(fg_L, C, H, bg, target, direction):
    """Move lightness in `direction` (-1 darker, +1 lighter) until contrast >= target."""
    L = fg_L
    for _ in range(200):
        hx = oklch_hex(L, C, H)
        if contrast(hx, bg) >= target:
            return hx
        L += 0.005 * direction
        if L < 0 or L > 1:
            break
    return oklch_hex(max(0, min(1, L)), C, H)


def on_color(bg):
    w, k = contrast("#FFFFFF", bg), contrast("#111111", bg)
    return "#FFFFFF" if w >= k else "#111111"


def system(primary, accent=None, neutral_chroma=0.012, mode="light", style="restrained"):
    Lp, Cp, Hp = rgb2oklch(hex2rgb(primary))
    Hn = Hp
    nc = neutral_chroma
    T = {}
    if mode == "light":
        T["ground"] = oklch_hex(0.985, nc * 0.6, Hn)
        T["surface"] = oklch_hex(0.955 if style == "restrained" else 0.94, nc, Hn)
        T["raised"] = "#FFFFFF"
        T["ink"] = oklch_hex(0.22, nc * 1.5, Hn)
        T["muted"] = fit_text(0.52, nc * 1.5, Hn, T["surface"], 4.6, -1)
        T["border"] = fit_text(0.86, nc, Hn, T["ground"], 1.25, -1)
        T["control-border"] = fit_text(0.72, nc, Hn, T["ground"], 3.0, -1)
        prim = primary if contrast(primary, T["ground"]) >= 3 else fit_text(Lp, Cp, Hp, T["ground"], 3.0, -1)
        T["primary"] = prim
        T["primary-hover"] = oklch_hex(rgb2oklch(hex2rgb(prim))[0] - 0.06, Cp, Hp)
        T["primary-text"] = fit_text(rgb2oklch(hex2rgb(prim))[0], Cp, Hp, T["ground"], 4.6, -1)
        T["on-primary"] = on_color(prim)
        T["primary-subtle"] = oklch_hex(0.95, Cp * 0.25, Hp)
        sem = {"success": 150, "warning": 75, "danger": 27, "info": 245}
        for k, h in sem.items():
            T[k] = fit_text(0.55 if k != "warning" else 0.62, 0.15, h, T["ground"], 4.6, -1)
            T[k + "-subtle"] = oklch_hex(0.955, 0.035, h)
            T["on-" + k + "-subtle"] = fit_text(0.40, 0.12, h, T[k + "-subtle"], 4.6, -1)
        T["selection"] = oklch_hex(0.90, Cp * 0.35, Hp)
    else:
        T["ground"] = oklch_hex(0.16, nc * 0.8, Hn)
        T["surface"] = oklch_hex(0.205, nc, Hn)
        T["raised"] = oklch_hex(0.25, nc, Hn)
        T["ink"] = oklch_hex(0.94, nc * 0.6, Hn)
        T["muted"] = fit_text(0.70, nc, Hn, T["surface"], 4.6, +1)
        T["border"] = oklch_hex(0.30, nc, Hn)
        T["control-border"] = fit_text(0.45, nc, Hn, T["ground"], 3.0, +1)
        prim_L = max(Lp, 0.68)
        prim = fit_text(prim_L, min(Cp, 0.17), Hp, T["ground"], 3.0, +1)
        T["primary"] = prim
        T["primary-hover"] = oklch_hex(rgb2oklch(hex2rgb(prim))[0] + 0.05, min(Cp, 0.17), Hp)
        T["primary-text"] = fit_text(rgb2oklch(hex2rgb(prim))[0], min(Cp, 0.17), Hp, T["ground"], 4.6, +1)
        T["on-primary"] = on_color(prim)
        T["primary-subtle"] = oklch_hex(0.26, Cp * 0.35, Hp)
        sem = {"success": 150, "warning": 75, "danger": 25, "info": 245}
        for k, h in sem.items():
            T[k] = fit_text(0.72, 0.14, h, T["ground"], 4.6, +1)
            T[k + "-subtle"] = oklch_hex(0.25, 0.045, h)
            T["on-" + k + "-subtle"] = fit_text(0.80, 0.12, h, T[k + "-subtle"], 4.6, +1)
        T["selection"] = oklch_hex(0.35, Cp * 0.5, Hp)
    if accent:
        La, Ca, Ha = rgb2oklch(hex2rgb(accent))
        T["accent"] = accent if contrast(accent, T["ground"]) >= 3 else fit_text(La, Ca, Ha, T["ground"], 3.0, -1 if mode == "light" else +1)
        T["on-accent"] = on_color(T["accent"])
    T["focus"] = T["primary"] if contrast(T["primary"], T["ground"]) >= 3 else T["ink"]
    return T


def report(T):
    pairs = [("ink", "ground", 4.5), ("ink", "surface", 4.5), ("muted", "ground", 4.5), ("muted", "surface", 4.5),
             ("primary-text", "ground", 4.5), ("on-primary", "primary", 4.5), ("primary", "ground", 3.0),
             ("control-border", "ground", 3.0), ("focus", "ground", 3.0),
             ("success", "ground", 4.5), ("warning", "ground", 4.5), ("danger", "ground", 4.5), ("info", "ground", 4.5)]
    if "accent" in T:
        pairs += [("on-accent", "accent", 4.5), ("accent", "ground", 3.0)]
    rows = []
    for fg, bg, need in pairs:
        r = contrast(T[fg], T[bg])
        rows.append((fg, bg, round(r, 2), need, "ok" if r >= need else "LOW"))
    return rows


def to_css(light, dark, prefix="color"):
    def block(T, ind="  "):
        return "\n".join(f"{ind}--{prefix}-{k}: {v};" for k, v in T.items())
    out = [":root {", "  color-scheme: light;", block(light), "}"]
    if dark:
        out += ['@media (prefers-color-scheme: dark) {', '  :root:not([data-theme="light"]) {', "    color-scheme: dark;",
                block(dark, "    "), "  }", "}", ':root[data-theme="dark"] {', "  color-scheme: dark;", block(dark), "}"]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("contrast"); c.add_argument("colors", nargs="+")
    r = sub.add_parser("ramp"); r.add_argument("hex"); r.add_argument("--name", default="brand")
    i = sub.add_parser("info"); i.add_argument("hex")
    s = sub.add_parser("system")
    s.add_argument("--primary", required=True); s.add_argument("--accent")
    s.add_argument("--neutral-chroma", type=float, default=0.012)
    s.add_argument("--ground", choices=["light", "dark", "both"], default="both")
    s.add_argument("--style", choices=["restrained", "committed"], default="restrained")
    s.add_argument("--css"); s.add_argument("--json")
    a = ap.parse_args()

    if a.cmd == "contrast":
        cs = a.colors
        if len(cs) % 2:
            sys.exit("give FG BG pairs")
        for fg, bg in zip(cs[::2], cs[1::2]):
            v = contrast(fg, bg)
            print(f"{fg} on {bg}: {v:.2f}:1  {verdict(v)}")
    elif a.cmd == "info":
        rgb = hex2rgb(a.hex)
        L, C, H = rgb2oklch(rgb)
        print(f"{a.hex.upper()}  rgb({', '.join(str(round(x*255)) for x in rgb)})  oklch({L*100:.1f}% {C:.3f} {H:.1f})"
              f"  vs white {contrast(a.hex,'#FFFFFF'):.2f}  vs black {contrast(a.hex,'#000000'):.2f}")
    elif a.cmd == "ramp":
        for k, v in ramp(a.hex).items():
            print(f"--{a.name}-{k}: {v};  /* {css_oklch(v)} | on-white {contrast(v,'#FFFFFF'):.2f} | on-black {contrast(v,'#000000'):.2f} */")
    elif a.cmd == "system":
        light = system(a.primary, a.accent, a.neutral_chroma, "light", a.style) if a.ground in ("light", "both") else None
        dark = system(a.primary, a.accent, a.neutral_chroma, "dark", a.style) if a.ground in ("dark", "both") else None
        for name, T in (("LIGHT", light), ("DARK", dark)):
            if not T:
                continue
            print(f"== {name}")
            for k, v in T.items():
                print(f"  {k:24s} {v}  {css_oklch(v)}")
            print("  -- contrast checks")
            for fg, bg, rr, need, ok in report(T):
                print(f"  {fg:>16s} on {bg:<8s} {rr:>5}:1 (need {need}) {ok}")
        css = to_css(light or dark, dark if light else None)
        if a.css:
            open(a.css, "w").write(css + "\n"); print(f"wrote {a.css}")
        if a.json:
            json.dump({"light": light, "dark": dark, "ramp_primary": ramp(a.primary),
                       **({"ramp_accent": ramp(a.accent)} if a.accent else {})}, open(a.json, "w"), indent=2)
            print(f"wrote {a.json}")


if __name__ == "__main__":
    main()
