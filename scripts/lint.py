#!/usr/bin/env python3
"""astudio lint - scan HTML/CSS/JSX/TSX/Vue/Svelte source for generated-design tells and craft bugs.

Usage: lint.py <files or folders> [--mode persuade|operate] [--allow rule,rule] [--json]

Each finding is FAIL (fix it) or WARN (fix unless you can defend it to a designer in one sentence).
A clean lint does not mean the design is good - it means nothing on this list was found.
Rules are deliberately tied to the brief: pass --allow <rule> when the brand/brief truly asks for it,
and record that decision in the delivery notes. Stdlib only.
"""
import argparse, json, re, sys
from pathlib import Path

EXT = {".html", ".htm", ".css", ".scss", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro", ".mdx"}

# (id, severity, regex, message, modes)  modes: both|persuade|operate
RULES = [
    ("transition-all", "FAIL", r"transition(?:-property)?\s*:\s*all\b|\btransition-all\b", "transition: all - list the exact properties", "both"),
    ("scale-zero-entrance", "FAIL", r"scale\(\s*0\s*\)|\bscale-0\b", "entrance from scale(0) - start at 0.95 + opacity", "both"),
    ("gradient-text", "FAIL", r"background-clip\s*:\s*text|bg-clip-text", "gradient/clipped text - emphasis by weight or size", "both"),
    ("purple-gradient", "WARN", r"(?:from|to|via)-(?:purple|violet|indigo|fuchsia)-\d{3}|linear-gradient\([^)]*(?:#(?:7c3aed|8b5cf6|6366f1|a855f7|9333ea|4f46e5))", "violet/indigo gradient - the first-wave AI look", "both"),
    ("ease-in-ui", "WARN", r"transition[^;{]*\bease-in\b(?!-out)|\bease-in\b(?!-out)[^;]*transition", "ease-in on UI feels sluggish - use ease-out", "both"),
    ("bounce-easing", "WARN", r"cubic-bezier\([^)]*,\s*-?\d*\.?\d+\s*,\s*[^)]*(?:1\.[2-9]|[2-9]\.)|animate-bounce|easeOutBack|elastic\.out|back\.out", "bounce/overshoot easing on interface elements", "both"),
    ("outline-none", "FAIL", r"outline\s*:\s*(?:none|0)\b(?![^}]*focus-visible)|\boutline-none\b(?![^\"']*focus-visible)", "focus outline removed without a visible replacement", "both"),
    ("user-scalable", "FAIL", r"user-scalable\s*=\s*no|maximum-scale\s*=\s*1(?:\.0)?\b", "zoom disabled - accessibility failure", "both"),
    ("h-screen", "WARN", r"\bh-screen\b|height\s*:\s*100vh", "100vh/h-screen jumps on mobile - use 100svh (hero) or 100dvh (app shell)", "both"),
    ("scroll-listener", "WARN", r"addEventListener\(\s*['\"]scroll['\"]", "scroll listener - use IntersectionObserver / ScrollTrigger / animation-timeline", "both"),
    ("emoji-icon", "WARN", r"[\U0001F300-\U0001FAFF☀-➿]", "emoji in markup - never as icons, bullets or nav", "both"),
    ("lorem", "FAIL", r"lorem ipsum|dolor sit amet|John Doe|Jane Doe|Acme(?: Inc| Corp)?\b|example@example\.com", "placeholder content", "both"),
    ("eyebrow-label", "WARN", r"uppercase[^\"'\n]{0,80}tracking-(?:widest|\[0\.[2-9])|text-transform\s*:\s*uppercase[^}]*letter-spacing\s*:\s*0?\.(?:1[5-9]|[2-9])em", "tiny tracked uppercase label (eyebrow/kicker)", "persuade"),
    ("index-numbering", "WARN", r">\s*0[1-9]\s*[/.<]|\(00?[1-9]\)", "01/02/03 index numbering - only for a real sequence", "persuade"),
    ("glow-shadow", "WARN", r"box-shadow\s*:\s*0\s+0\s+\d+px[^;]*(?:rgba?\([^)]*\)|#[0-9a-f]{3,8})(?![^;]*inset)|shadow-\[0_0_\d+px", "zero-offset glow halo - depth needs an offset", "both"),
    ("side-stripe", "WARN", r"border-left\s*:\s*[3-9]px\s+solid|border-l-(?:4|8)\b", "coloured side-stripe on cards/callouts", "both"),
    ("glass-default", "WARN", r"backdrop-filter\s*:\s*blur|backdrop-blur", "backdrop blur - only where it explains a floating layer (nav, sheet)", "both"),
    ("default-font", "WARN", r"font-family\s*:\s*['\"]?(?:Inter|Roboto|Arial|Helvetica|Poppins|Montserrat|Open Sans|Space Grotesk)['\"]?\s*[,;]", "training-data default face - fine for Operate UI body, not as a Persuade display voice", "persuade"),
    ("system-font-display", "WARN", r"font-family\s*:\s*(?:system-ui|-apple-system)\s*[;}]", "system-ui as the whole type voice on a brand page", "persuade"),
    ("copy-buzzword", "WARN", r"\b(?:unlock|unleash|supercharge|seamless(?:ly)?|effortless(?:ly)?|revolutioni[sz]e|elevate your|cutting-edge|next-gen(?:eration)?|all-in-one|world-class|empower)\b", "genre buzzword - say what the product does", "both"),
    ("copy-ru-buzzword", "WARN", r"(?i)\b(?:инновационн\w+|уникальн\w+ решени\w+|высококачественн\w+|индивидуальный подход|широкий спектр|лидер рынка|команда профессионалов)\b", "русские штампы - конкретика вместо лозунгов", "both"),
    ("get-started", "WARN", r">\s*(?:Get started|Learn more|Click here|Submit|Подробнее|Узнать больше|Отправить)\s*<", "generic CTA label - name the outcome", "persuade"),
    ("zebra-table", "WARN", r"nth-child\(\s*(?:even|odd|2n)\s*\)|even:bg-|odd:bg-", "zebra striping - rules and alignment instead", "operate"),
    ("left-numbers", "WARN", r"<td[^>]*>\s*[\$€₽]?\s?\d[\d,.\s]*\s*</td>", "check numeric cells are right-aligned with tabular-nums", "operate"),
    ("img-no-alt", "FAIL", r"<img(?![^>]*\balt=)[^>]*>", "img without alt", "both"),
    ("div-button", "FAIL", r"<(?:div|span)[^>]*\bonClick=|<(?:div|span)[^>]*\bonclick=", "click handler on div/span - use <button> or <a>", "both"),
    ("will-change-global", "WARN", r"\*\s*\{[^}]*will-change|will-change\s*:\s*(?:transform|opacity)[^;]*;[^}]*\}\s*$", "will-change applied broadly", "both"),
    ("ellipsis-dots", "WARN", r"[A-Za-zА-Яа-я]\.\.\.(?!\.)", "three dots - use the ellipsis character …", "both"),
]


def files(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for f in p.rglob("*"):
                if f.suffix.lower() in EXT and "node_modules" not in f.parts and ".astudio" not in f.parts:
                    yield f
        elif p.suffix.lower() in EXT:
            yield p


def scan(path, mode, allow):
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    out = []
    lines = text.splitlines()
    for rid, sev, rx, msg, modes in RULES:
        if rid in allow or (modes != "both" and modes != mode):
            continue
        r = re.compile(rx, re.I | re.M)
        for i, line in enumerate(lines, 1):
            if r.search(line):
                out.append({"file": str(path), "line": i, "rule": rid, "sev": sev, "msg": msg, "src": line.strip()[:120]})
    # file-level checks
    if path.suffix.lower() in (".html", ".htm"):
        # page-level checks also see local stylesheets/scripts the page links to (styles.css, tokens.css, @import)
        page = text
        for href in re.findall(r'<link[^>]+href=["\']([^"\':?#]+\.css)', text) + re.findall(r'<script[^>]+src=["\']([^"\':?#]+\.js)', text):
            try:
                linked = (path.parent / href).resolve()
                page += "\n" + linked.read_text(encoding="utf-8", errors="ignore")
                for imp in re.findall(r'@import\s+(?:url\()?["\']([^"\':?#]+\.css)', page):
                    page += "\n" + (linked.parent / imp).read_text(encoding="utf-8", errors="ignore")
            except Exception:
                pass
        text = page
        if "prefers-reduced-motion" not in text and re.search(r"@keyframes|animation\s*:|gsap|transition", text):
            out.append({"file": str(path), "line": 0, "rule": "no-reduced-motion", "sev": "FAIL", "msg": "motion without a prefers-reduced-motion alternative", "src": ""})
        if '<html' in text and not re.search(r'<html[^>]*\blang=', text):
            out.append({"file": str(path), "line": 0, "rule": "html-lang", "sev": "FAIL", "msg": "<html> without lang", "src": ""})
        if '<head' in text and 'name="viewport"' not in text and "name='viewport'" not in text:
            out.append({"file": str(path), "line": 0, "rule": "viewport-meta", "sev": "FAIL", "msg": "missing viewport meta", "src": ""})
        if re.search(r"<head", text) and ":focus-visible" not in text and "focus-visible" not in text:
            out.append({"file": str(path), "line": 0, "rule": "focus-style", "sev": "WARN", "msg": "no :focus-visible style found", "src": ""})
        if "::selection" not in text and "<style" in text:
            out.append({"file": str(path), "line": 0, "rule": "browser-surfaces", "sev": "WARN", "msg": "selection/scrollbar/caret not themed - browser defaults show", "src": ""})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--mode", choices=["persuade", "operate"], default="persuade")
    ap.add_argument("--allow", default="")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    allow = {x.strip() for x in a.allow.split(",") if x.strip()}
    res = []
    for f in files(a.paths):
        res += scan(f, a.mode, allow)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        for r in res:
            loc = f"{r['file']}:{r['line']}" if r["line"] else r["file"]
            print(f"{r['sev']:4} {loc}  [{r['rule']}] {r['msg']}" + (f"\n       {r['src']}" if r["src"] else ""))
        fails = sum(r["sev"] == "FAIL" for r in res)
        print(f"\n{len(res)} findings, FAIL={fails}" if res else "lint: no findings")
    sys.exit(1 if any(r["sev"] == "FAIL" for r in res) else 0)


if __name__ == "__main__":
    main()
