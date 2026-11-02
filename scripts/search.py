#!/usr/bin/env python3
"""astudio search - BM25 search over the astudio design-intelligence database.

Usage:
  search.py "<query>" [--domain D] [-n N] [--json] [--cyrillic]
  search.py "<query>" --stack STACK [-n N]
  search.py "<product + industry + mood keywords>" --design-system [-p "Project"] [--cyrillic] [--format md|json]
  search.py --list            # list domains and stacks

Queries are matched against English data. Translate non-English briefs into 2-5
English keywords first (e.g. "кофейня уютная" -> "coffee shop cozy artisan").
Results are recommendations to reason about, never instructions.
Python 3.8+, standard library only.
"""
import argparse, csv, json, math, re, sys
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

DOMAINS = {
    "style": ("styles.csv", ["Style Category", "Aliases", "Keywords", "Best For", "Type", "AI Prompt Keywords"],
              ["Style Category", "Type", "Keywords", "Primary Colors", "Secondary Colors", "Effects & Animation", "Best For",
               "Do Not Use For", "Accessibility", "Performance", "Complexity", "CSS/Technical Keywords",
               "Implementation Checklist", "Design System Variables", "Status"]),
    "color": ("colors.csv", ["Product Type", "Notes"],
              ["Product Type", "Primary", "On Primary", "Secondary", "On Secondary", "Accent", "On Accent", "Background",
               "Foreground", "Card", "Card Foreground", "Muted", "Muted Foreground", "Border", "Destructive", "Ring", "Notes"]),
    "product": ("products.csv", ["Product Type", "Keywords", "Primary Style Recommendation", "Key Considerations"],
                ["Product Type", "Keywords", "Primary Style Recommendation", "Secondary Styles", "Landing Page Pattern",
                 "Dashboard Style (if applicable)", "Color Palette Focus", "Key Considerations"]),
    "reasoning": ("ui-reasoning.csv", ["UI_Category", "Style_Priority", "Color_Mood", "Typography_Mood"],
                  ["UI_Category", "Recommended_Pattern", "Style_Priority", "Color_Mood", "Typography_Mood", "Key_Effects",
                   "Anti_Patterns", "Severity"]),
    "typography": ("typography.csv", ["Font Pairing Name", "Category", "Mood/Style Keywords", "Best For", "Heading Font", "Body Font"],
                   ["Font Pairing Name", "Category", "Heading Font", "Body Font", "Mood/Style Keywords", "Best For",
                    "Google Fonts URL", "Notes"]),
    "google-fonts": ("google-fonts.csv", ["Family", "Category", "Stroke", "Classifications", "Keywords"],
                     ["Family", "Category", "Classifications", "Styles", "Variable Axes", "Subsets", "Popularity Rank", "Google Fonts URL"]),
    "landing": ("landing.csv", ["Pattern Name", "Aliases", "Keywords", "Conversion Optimization", "Section Order"],
                ["Pattern Name", "Section Order", "Primary CTA Placement", "Color Strategy", "Recommended Effects", "Conversion Optimization"]),
    "ux": ("ux-guidelines.csv", ["Category", "Issue", "Description", "Platform"],
           ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]),
    "app": ("app-interface.csv", ["Category", "Issue", "Keywords", "Description"],
            ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]),
    "chart": ("charts.csv", ["Data Type", "Keywords", "Best Chart Type", "When to Use", "When NOT to Use"],
              ["Data Type", "Best Chart Type", "Secondary Options", "When to Use", "When NOT to Use", "Data Volume Threshold",
               "Color Guidance", "Accessibility Notes", "A11y Fallback", "Library Recommendation"]),
    "icons": ("icons.csv", ["Category", "Icon Name", "Keywords", "Best For", "Library"],
              ["Category", "Icon Name", "Library", "Import Code", "Usage", "Best For", "Style"]),
    "motion": ("motion.csv", ["Category", "Intensity Tier", "Keywords", "Trigger"],
               ["Category", "Intensity Tier", "Trigger", "Duration", "Easing", "GSAP Snippet", "Framework Notes", "Do", "Don't", "Performance Notes"]),
    "react": ("react-performance.csv", ["Category", "Issue", "Keywords", "Description"],
              ["Category", "Issue", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]),
    "logo-style": ("logo/styles.csv", ["Style Name", "Category", "Keywords", "Best For"],
                   ["Style Name", "Category", "Keywords", "Primary Colors", "Typography", "Effects", "Best For", "Avoid For", "Complexity"]),
    "logo-industry": ("logo/industries.csv", ["Industry", "Keywords", "Recommended Styles", "Common Symbols", "Mood"],
                      ["Industry", "Recommended Styles", "Primary Colors", "Typography", "Common Symbols", "Mood", "Best Practices", "Avoid"]),
    "logo-color": ("logo/colors.csv", ["Palette Name", "Category", "Keywords", "Psychology", "Best For"],
                   ["Palette Name", "Primary Hex", "Secondary Hex", "Accent Hex", "Background Hex", "Text Hex", "Psychology", "Best For", "Avoid For"]),
    "icon-style": ("logo/icon-styles.csv", ["name", "description", "best_for", "keywords"],
                   ["name", "description", "stroke_width", "fill", "best_for"]),
    "brand-application": ("logo/brand-applications.csv", None, None),
    "banner": ("banner-sizes.csv", ["platform", "format", "use", "keywords"],
               ["platform", "format", "width", "height", "ratio", "safe_zone", "max_file", "notes"]),
    "3d-source": ("3d-sources.csv", ["name", "type", "license", "keywords", "best_for"],
                  ["name", "url", "type", "license", "attribution", "formats", "best_for", "notes"]),
    "hero": ("hero-patterns.csv", ["Pattern", "Keywords", "Best For", "Wow Mechanism"],
             ["Pattern", "Best For", "Composition", "Wow Mechanism", "Build", "Assets", "Mobile", "Fallback", "Avoid"]),
    "section": ("section-patterns.csv", ["Section", "Keywords", "Best For", "Composition"],
                ["Section", "Best For", "Composition", "Visual Anchor", "Details", "Mobile", "Avoid"]),
    "slide-strategy": ("slides/strategies.csv", ["strategy_name", "keywords", "goal", "audience"],
                       ["strategy_name", "slide_count", "structure", "goal", "tone", "narrative_arc", "emotion_arc"]),
    "slide-copy": ("slides/copy.csv", ["formula_name", "keywords", "use_case", "slide_type"],
                   ["formula_name", "components", "use_case", "example_template", "emotion_trigger"]),
    "slide-layout": ("slides/layouts.csv", None, None),
    "slide-chart": ("slides/charts.csv", None, None),
}

AUTO = {
    "color": "color palette hex shade tint brand-color",
    "typography": "font pairing typeface heading body serif sans",
    "google-fonts": "google font family variable weight cyrillic",
    "style": "style aesthetic glassmorphism brutalism minimal neumorphism bento retro look",
    "landing": "landing hero section cta conversion funnel pricing testimonial",
    "ux": "accessibility a11y focus keyboard form error validation touch navigation loading scroll",
    "chart": "chart graph visualization axis legend trend bar line pie",
    "icons": "icon icons lucide phosphor glyph",
    "motion": "animation gsap scroll reveal stagger parallax transition easing",
    "product": "saas ecommerce app platform startup marketplace service",
    "logo-style": "logo mark wordmark monogram emblem lettermark",
    "banner": "banner cover header ad size instagram facebook youtube story display",
    "3d-source": "3d model glb gltf hdri texture asset",
    "hero": "hero first screen above the fold wow header intro",
    "section": "section block menu gallery faq footer pricing contacts",
    "react": "react nextjs rerender memo suspense bundle",
}

TOKEN = re.compile(r"[a-zа-яё0-9#]+", re.I)

# Query-side synonym expansion so everyday briefs reach the right rows.
SYNONYMS = {
    "coffee": "cafe bakery", "coffeeshop": "cafe bakery", "barista": "cafe", "espresso": "cafe",
    "restaurant": "food restaurant dining", "bar": "restaurant brewery", "pizza": "restaurant food",
    "shop": "ecommerce store", "store": "ecommerce", "boutique": "ecommerce luxury fashion",
    "clinic": "medical healthcare", "doctor": "medical healthcare", "dentist": "dental",
    "bank": "banking finance", "crypto": "fintech crypto web3", "ai": "ai chatbot",
    "school": "education course", "courses": "online course elearning", "gym": "fitness",
    "hotel": "hotel hospitality", "travel": "travel tourism", "realty": "real estate property",
    "agency": "agency creative marketing", "portfolio": "portfolio personal", "startup": "saas startup",
    "lawyer": "legal law", "cosmetics": "beauty spa", "salon": "beauty spa salon", "kids": "children childcare kids",
    "game": "gaming game", "music": "music streaming", "event": "event conference", "wedding": "wedding event",
    "dashboard": "dashboard analytics admin", "admin": "admin dashboard", "crm": "crm client management",
}


def tok(s):
    return [t.lower() for t in TOKEN.findall(s or "") if len(t) > 1]


def expand(q):
    extra = [SYNONYMS[t] for t in tok(q) if t in SYNONYMS]
    return q + " " + " ".join(extra)


def load(fname):
    p = DATA / fname
    if not p.exists():
        return []
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))


class BM25:
    def __init__(self, docs, k1=1.4, b=0.75):
        self.docs = [tok(d) for d in docs]
        self.k1, self.b = k1, b
        self.avg = sum(map(len, self.docs)) / max(1, len(self.docs))
        df = Counter(t for d in self.docs for t in set(d))
        n = len(self.docs)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}
        self.tf = [Counter(d) for d in self.docs]

    def score(self, q):
        qt = tok(q)
        out = []
        for i, d in enumerate(self.docs):
            s = 0.0
            for t in qt:
                f = self.tf[i].get(t, 0)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * len(d) / self.avg))
            out.append(s)
        return out


def search(domain, query, n=3, rows=None, filt=None):
    fname, scols, ocols = DOMAINS[domain]
    rows = rows if rows is not None else load(fname)
    if filt:
        rows = [r for r in rows if filt(r)]
    if not rows:
        return []
    scols = scols or list(rows[0].keys())
    ocols = ocols or [c for c in rows[0].keys() if c.lower() not in ("no", "id")]
    if domain == "style":
        rows = [r for r in rows if r.get("Status", "active") != "deprecated"]
    # first search column is the row's identity - weight it x3
    bm = BM25([" ".join([r.get(scols[0], "")] * 3 + [r.get(c, "") for c in scols]) for r in rows])
    sc = bm.score(expand(query))
    ranked = sorted(range(len(rows)), key=lambda i: -sc[i])
    res = []
    for i in ranked[:n]:
        if sc[i] <= 0:
            break
        res.append({"_score": round(sc[i], 2), **{c: rows[i].get(c, "") for c in ocols if rows[i].get(c)}})
    return res


def detect(query):
    q = set(tok(query))
    best, bs = "style", 0
    for d, kw in AUTO.items():
        s = len(q & set(kw.split()))
        if s > bs:
            best, bs = d, s
    return best


def fonts_by_family():
    return {r["Family"].lower(): r for r in load("google-fonts.csv")}


def cyr_ok(family, fam=None):
    fam = fam or fonts_by_family()
    r = fam.get(family.lower().strip())
    if not r:
        return None
    return "cyrillic" in subsets(r)


def subsets(r):
    return {x.strip() for x in r.get("Subsets", "").split("|")}


def design_system(query, project=None, cyrillic=False):
    product = (search("product", query, 1) or [{}])[0]
    ptype = product.get("Product Type", "")
    reasoning = (search("reasoning", ptype or query, 1) or [{}])[0]
    color = (search("color", ptype or query, 1) or [{}])[0]
    style_q = " ".join([product.get("Primary Style Recommendation", ""), query])
    styles = search("style", style_q, 2)
    landing = (search("landing", product.get("Landing Page Pattern", "") or query, 1) or [{}])[0]
    fam = fonts_by_family()
    typo_q = " ".join([reasoning.get("Typography_Mood", ""), query])
    filt = None
    if cyrillic:
        filt = lambda r: bool(cyr_ok(r["Heading Font"], fam)) and bool(cyr_ok(r["Body Font"], fam))
    typos = search("typography", typo_q, 3, filt=filt)
    for t in typos:
        t["cyrillic"] = {"heading": cyr_ok(t.get("Heading Font", ""), fam), "body": cyr_ok(t.get("Body Font", ""), fam)}
    motion = search("motion", reasoning.get("Key_Effects", "") + " scroll reveal parallax split text", 2)
    heroes = search("hero", query + " " + ptype, 3)
    sections = search("section", query + " " + ptype, 5)
    return {"project": project or "Untitled", "query": query, "product": product, "reasoning": reasoning,
            "palette": color, "styles": styles, "typography": typos, "landing": landing, "motion": motion,
            "heroes": heroes, "sections": sections,
            "note": "Starting points from the database. Run the anti-default check (reference/direction.md) and the studio bar (reference/studio-bar.md) and verify "
                    "contrast with palette.py before committing. Database fonts are frequently training-data defaults - "
                    "treat them as a fallback, not the answer, for Persuade surfaces."}


def md_design_system(ds):
    L = [f"# Design system draft: {ds['project']}", f"_Query: {ds['query']}_", ""]
    p, r = ds["product"], ds["reasoning"]
    if p:
        L += ["## Product match", f"- Type: **{p.get('Product Type','')}**",
              f"- Recommended style: {p.get('Primary Style Recommendation','')} (alt: {p.get('Secondary Styles','')})",
              f"- Landing pattern: {p.get('Landing Page Pattern','')}",
              f"- Dashboard style: {p.get('Dashboard Style (if applicable)','')}",
              f"- Considerations: {p.get('Key Considerations','')}", ""]
    if r:
        L += ["## Reasoning", f"- Color mood: {r.get('Color_Mood','')}", f"- Typography mood: {r.get('Typography_Mood','')}",
              f"- Key effects: {r.get('Key_Effects','')}", f"- **Anti-patterns:** {r.get('Anti_Patterns','')}", ""]
    c = ds["palette"]
    if c:
        L += ["## Palette (semantic roles)", "| Role | Hex |", "|---|---|"]
        for k in ["Primary", "On Primary", "Secondary", "Accent", "On Accent", "Background", "Foreground", "Card",
                  "Muted", "Muted Foreground", "Border", "Destructive", "Ring"]:
            if c.get(k):
                L.append(f"| {k} | {c[k]} |")
        L += [f"_Notes: {c.get('Notes','')}_", ""]
    if ds["styles"]:
        L += ["## Style candidates"]
        for s in ds["styles"]:
            L += [f"### {s.get('Style Category','')}", f"- Keywords: {s.get('Keywords','')}",
                  f"- Effects: {s.get('Effects & Animation','')}", f"- Best for: {s.get('Best For','')}",
                  f"- Avoid for: {s.get('Do Not Use For','')}", f"- Checklist: {s.get('Implementation Checklist','')}", ""]
    if ds["typography"]:
        L += ["## Typography candidates"]
        for t in ds["typography"]:
            cy = t.get("cyrillic", {})
            L += [f"- **{t.get('Heading Font','')} / {t.get('Body Font','')}** ({t.get('Font Pairing Name','')}) - "
                  f"{t.get('Mood/Style Keywords','')}; Cyrillic: heading={cy.get('heading')}, body={cy.get('body')}"]
        L.append("")
    if ds.get("heroes"):
        L += ["## First-screen (wow) candidates - see reference/studio-bar.md §4"]
        for h in ds["heroes"]:
            L += [f"- **{h.get('Pattern','')}** - {h.get('Composition','')} Wow: {h.get('Wow Mechanism','')}"]
        L.append("")
    if ds.get("sections"):
        L += ["## Rich section patterns"]
        for x in ds["sections"]:
            L += [f"- **{x.get('Section','')}** - {x.get('Composition','')} (visual anchor: {x.get('Visual Anchor','')})"]
        L.append("")
    l = ds["landing"]
    if l:
        L += ["## Page pattern", f"- {l.get('Pattern Name','')}: {l.get('Section Order','')}",
              f"- CTA placement: {l.get('Primary CTA Placement','')}", f"- Conversion: {l.get('Conversion Optimization','')}", ""]
    L += ["## Caveat", ds["note"]]
    return "\n".join(L)


def fmt(results):
    out = []
    for i, r in enumerate(results, 1):
        out.append(f"--- [{i}] score={r.pop('_score')}")
        for k, v in r.items():
            out.append(f"{k}: {v}")
    return "\n".join(out) if out else "No match. Retry once with narrower English keywords or an explicit --domain."


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--domain", "-d", choices=sorted(DOMAINS))
    ap.add_argument("--stack", "-s")
    ap.add_argument("-n", type=int, default=3)
    ap.add_argument("--design-system", action="store_true")
    ap.add_argument("-p", "--project")
    ap.add_argument("--cyrillic", action="store_true", help="only fonts with Cyrillic subset")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        print("domains:", ", ".join(sorted(DOMAINS)))
        print("stacks:", ", ".join(sorted(p.stem for p in (DATA / "stacks").glob("*.csv"))))
        return
    if not a.query:
        ap.error("query required")
    if a.design_system:
        ds = design_system(a.query, a.project, a.cyrillic)
        print(json.dumps(ds, ensure_ascii=False, indent=2) if a.json else md_design_system(ds))
        return
    if a.stack:
        rows = load(f"stacks/{a.stack}.csv")
        if not rows:
            sys.exit(f"Unknown stack '{a.stack}'. Use --list.")
        DOMAINS["_stack"] = (None, ["Category", "Guideline", "Description", "Do", "Don't"],
                             ["Category", "Guideline", "Description", "Do", "Don't", "Code Good", "Code Bad", "Severity", "Docs URL"])
        res = search("_stack", a.query, a.n, rows=rows)
    else:
        d = a.domain or detect(a.query)
        filt = None
        if a.cyrillic and d == "google-fonts":
            filt = lambda r: "cyrillic" in subsets(r)
        if a.cyrillic and d == "typography":
            fam = fonts_by_family()
            filt = lambda r: bool(cyr_ok(r["Heading Font"], fam)) and bool(cyr_ok(r["Body Font"], fam))
        res = search(d, a.query, a.n, filt=filt)
        if not a.json:
            print(f"[domain: {d}]")
    print(json.dumps(res, ensure_ascii=False, indent=2) if a.json else fmt(res))


if __name__ == "__main__":
    main()
