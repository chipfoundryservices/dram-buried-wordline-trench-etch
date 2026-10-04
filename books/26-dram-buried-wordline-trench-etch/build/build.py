#!/usr/bin/env python3
"""Assemble Book 26 into HTML and EPUB; tables/figures come from sim results."""
import csv, glob, html, math, os, re, zipfile, uuid
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "out")
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(ROOT, "figures"), exist_ok=True)
TITLE = "DRAM Buried Word-Line Trench Etch"

PARTS = {1: "Part I — Foundations", 5: "Part II — Trench Etch Physics",
         9: "Part III — Process Integration",
         13: "Part IV — Measurement, Control and Outlook"}


def load(name):
    return [{k: float(v) for k, v in r.items()}
            for r in csv.DictReader(open(os.path.join(ROOT, "sim", name)))]


TR = load("transport_results.csv")
ET = load("etch_results.csv")
SS = [0.0, 0.01, 0.05, 0.2, 1.0]
SIG = [2.0, 4.0, 8.0]


def fmt(x):
    return f"{x:.4f}" if x >= 1e-3 else f"{x:.1e}"


def g(x):
    return f"{x:g}"


def table(head, body):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in body)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


def t_neutral():
    return table(["AR"] + [f"s={g(s)}" for s in SS],
                 [[g(r["AR"])] + [fmt(r[f"n_s{s}"]) for s in SS] for r in TR])


def t_ion():
    return table(["AR"] + [f"σ={g(s)}°" for s in SIG] + ["neutral s=0.05", "ion σ=4° / neutral s=0.05"],
                 [[g(r["AR"])] + [fmt(r[f"i_sig{s}"]) for s in SIG] + [fmt(r["n_s0.05"]),
                  f"{r['i_sig4.0']/r['n_s0.05']:.2f}"] for r in TR])


def t_valid():
    return table(["AR", "MC, s=1", "exact √(1+AR²)−AR", "difference"],
                 [[g(r["AR"]), fmt(r["n_s1.0"]), fmt(r["los_exact"]),
                   f"{r['n_s1.0']-r['los_exact']:+.4f}"] for r in TR])


def t_etch():
    rows = [r for r in ET if abs(r["t"] - round(r["t"])) < 1e-6]
    return table(["t / t₀", "Si depth (nm)", "Si rate / R₀", "oxide depth (nm)",
                  "oxide rate / R₀", "fin height (nm)"],
                 [[g(r["t"]), f"{r['d_Si']:.1f}", f"{r['R_Si']:.3f}", f"{r['d_SiO2']:.1f}",
                   f"{r['R_SiO2']:.3f}", f"{r['d_SiO2']-r['d_Si']:+.1f}"] for r in rows])


def svg_plot(series, title, xlabel, ylabel, logx=False, logy=False):
    W, H, L, R, T, B = 620, 380, 70, 20, 30, 55
    xs = [p[0] for _, pts in series for p in pts]
    ys = [p[1] for _, pts in series for p in pts if not logy or p[1] > 0]
    fx = math.log10 if logx else (lambda v: v)
    fy = math.log10 if logy else (lambda v: v)
    x0, x1 = fx(min(xs)), fx(max(xs))
    if logy:
        y0, y1 = math.floor(math.log10(min(ys))), math.ceil(math.log10(max(ys)))
        yt = [(10**e, f"1e{e}") for e in range(y0, y1 + 1)]
    else:
        top = max(ys); step = 10 ** math.floor(math.log10(top))
        if top / step < 3: step /= 2
        y0, y1 = 0.0, math.ceil(top / step) * step
        yt = [(k * step, g(round(k * step, 6))) for k in range(int(round(y1 / step)) + 1)]
    px = lambda x: L + (fx(x) - x0) / (x1 - x0) * (W - L - R)
    py = lambda y: T + (y1 - fy(max(y, 10**y0) if logy else y)) / (y1 - y0) * (H - T - B)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="12">',
         f'<rect width="{W}" height="{H}" fill="white"/>',
         f'<text x="{W/2}" y="18" text-anchor="middle" font-weight="bold">{title}</text>']
    for v, lab in yt:
        y = py(v)
        o.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" stroke="#ddd"/>'
                 f'<text x="{L-6}" y="{y+4:.1f}" text-anchor="end">{lab}</text>')
    ticks = sorted(set(xs)) if len(set(xs)) <= 12 else [v for v in range(0, int(max(xs)) + 1, 2)]
    for x in ticks:
        o.append(f'<line x1="{px(x):.1f}" x2="{px(x):.1f}" y1="{T}" y2="{H-B}" stroke="#eee"/>'
                 f'<text x="{px(x):.1f}" y="{H-B+16}" text-anchor="middle">{g(x)}</text>')
    o.append(f'<rect x="{L}" y="{T}" width="{W-L-R}" height="{H-T-B}" fill="none" stroke="#444"/>')
    o.append(f'<text x="{(L+W-R)/2}" y="{H-12}" text-anchor="middle">{xlabel}</text>')
    o.append(f'<text transform="translate(16 {(T+H-B)/2}) rotate(-90)" text-anchor="middle">{ylabel}</text>')
    cols = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#555"]
    for i, (name, pts) in enumerate(series):
        c = cols[i % len(cols)]
        d = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
        dash = ' stroke-dasharray="6 3"' if ("ion" in name or "oxide" in name or "exact" in name) else ""
        o.append(f'<polyline points="{d}" fill="none" stroke="{c}" stroke-width="2"{dash}/>')
        o.append(f'<rect x="{W-R-170}" y="{T+8+i*16}" width="12" height="3" fill="{c}"/>'
                 f'<text x="{W-R-152}" y="{T+14+i*16}">{name}</text>')
    o.append("</svg>")
    return "\n".join(o)


def fig_neutral():
    s = [(f"neutral s={g(v)}", [(r["AR"], r[f"n_s{v}"]) for r in TR]) for v in SS]
    return ("Figure 4.1", "Fraction of neutrals entering the trench that reach the floor, by sticking coefficient s. The s = 1 curve is the exact line-of-sight limit.",
            svg_plot(s, "Neutral delivery to the trench floor", "aspect ratio", "floor fraction", logy=True))


def fig_ion():
    s = [(f"ion σ={g(v)}°", [(r["AR"], r[f"i_sig{v}"]) for r in TR]) for v in SIG]
    s.append(("neutral s=0.05", [(r["AR"], r["n_s0.05"]) for r in TR]))
    return ("Figure 5.1", "Ion delivery to the floor for three angular spreads, against the neutral fraction for s = 0.05. Ions fall off far more slowly; this asymmetry drives everything in Chapter 7.",
            svg_plot(s, "Ions versus neutrals", "aspect ratio", "floor fraction"))


def fig_depth():
    s = [("Si depth", [(r["t"], r["d_Si"]) for r in ET]),
         ("oxide depth", [(r["t"], r["d_SiO2"]) for r in ET]),
         ("fin height ×5", [(r["t"], max(0.0, 5 * (r["d_SiO2"] - r["d_Si"]))) for r in ET])]
    return ("Figure 7.1", "Depth histories of silicon (neutral-limited) and STI oxide (ion-limited) in a 20 nm trench. Oxide starts slower but overtakes near 53 nm; the gap is the saddle-fin height (shown ×5).",
            svg_plot(s, "Depth versus time, 20 nm word-line trench", "time t / t₀", "depth (nm)"))


def figure_html(f, name):
    label, cap, svg = f()
    open(os.path.join(ROOT, "figures", name + ".svg"), "w").write(svg)
    return f'<figure>{svg}<figcaption><b>{label}.</b> {cap}</figcaption></figure>'


def subst(md):
    rep = {"{{TABLE:neutral}}": t_neutral, "{{TABLE:ion}}": t_ion,
           "{{TABLE:valid}}": t_valid, "{{TABLE:etch}}": t_etch,
           "{{FIG:neutral}}": lambda: figure_html(fig_neutral, "neutral_vs_ar"),
           "{{FIG:ion}}": lambda: figure_html(fig_ion, "ion_vs_neutral"),
           "{{FIG:depth}}": lambda: figure_html(fig_depth, "depth_history")}
    for k, v in rep.items():
        if k in md:
            md = md.replace(k, "\n\n" + v() + "\n\n")
    return md


def read(p):
    return open(p, encoding="utf-8").read()


# ---- collect sections: (id, label, title, markdown)
secs = [("front", "", "Preface", read(os.path.join(ROOT, "frontmatter.md")))]
for p in sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md"))):
    n = int(os.path.basename(p).split("-")[0])
    md = read(p)
    secs.append((f"ch{n:02d}", str(n), md.splitlines()[0].lstrip("# ").strip(), md))
for p in sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md"))):
    L = os.path.basename(p)[0]
    md = read(p)
    secs.append((f"app{L}", L, md.splitlines()[0].lstrip("# ").strip(), md))
secs.append(("glossary", "", "Glossary", read(os.path.join(ROOT, "backmatter", "glossary.md"))))

# ---- index
plain = {s[0]: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s[3])) for s in secs}
def ref(sid):
    return sid[2:].lstrip("0") if sid.startswith("ch") else ("App. " + sid[3:] if sid.startswith("app") else None)
idx = {}
for line in read(os.path.join(ROOT, "backmatter", "index_terms.txt")).splitlines():
    if not line.strip():
        continue
    term, *pats = line.split("|")
    hits = []
    for sid, text in plain.items():
        r = ref(sid)
        if r and any(re.search(re.escape(p), text, re.I) for p in pats):
            hits.append((sid, r))
    idx[term] = hits
idx_md = "# Index\n\n" + "\n\n".join(
    f"**{t}** — " + ", ".join(f'<a href="#{sid}">{r}</a>' for sid, r in h)
    for t, h in sorted(idx.items(), key=lambda kv: kv[0].lower()) if h) + "\n"
secs.append(("index", "", "Index", idx_md))

md_ext = ["tables", "fenced_code", "sane_lists"]
bodies = {}
for sid, lab, title, md in secs:
    bodies[sid] = markdown.markdown(subst(md), extensions=md_ext)

CSS = """body{font:17px/1.6 Georgia,serif;max-width:46em;margin:2em auto;padding:0 1em;color:#222}
h1{border-bottom:2px solid #333;padding-bottom:.2em;margin-top:2.5em}h2{margin-top:1.8em}
table{border-collapse:collapse;margin:1em 0;font:14px sans-serif}td,th{border:1px solid #bbb;padding:3px 8px;text-align:right}
th{background:#eee}td:first-child,th:first-child{text-align:left}blockquote{border-left:4px solid #999;margin:1em 0;padding:.2em 1em;color:#444}
code,pre{background:#f3f3f3;font-size:14px}pre{padding:.7em;overflow-x:auto}figure{margin:1.5em 0}figure svg{width:100%;height:auto}
figcaption{font:14px sans-serif;color:#444}.part{font:700 1.1em sans-serif;text-transform:uppercase;letter-spacing:.1em;margin-top:4em;color:#555}"""

# ---- HTML
toc = ["<h1>Contents</h1><ul>"]
for sid, lab, title, _ in secs:
    if sid.startswith("ch") and int(sid[2:]) in PARTS:
        toc.append(f'<li><b>{PARTS[int(sid[2:])]}</b></li>')
    toc.append(f'<li><a href="#{sid}">{title}</a></li>')
toc.append("</ul>")
parts_html = []
for sid, lab, title, _ in secs:
    pre = ""
    if sid.startswith("ch") and int(sid[2:]) in PARTS:
        pre = f'<div class="part">{PARTS[int(sid[2:])]}</div>'
    parts_html.append(f'{pre}<section id="{sid}">{bodies[sid]}</section>')
doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title>'
       f'<meta name="viewport" content="width=device-width,initial-scale=1"><style>{CSS}</style></head><body>'
       + parts_html[0] + "".join(toc) + "".join(parts_html[1:]) + "</body></html>")
open(os.path.join(OUT, "book26-dram-buried-wordline-trench-etch.html"), "w", encoding="utf-8").write(doc)

# ---- EPUB
def xhtml(title, body):
    body = re.sub(r"<(br|hr|img)([^>]*?)(?<!/)>", r"<\1\2/>", body)
    return ('<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
            f'<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" href="style.css"/></head>'
            f'<body>{body}</body></html>')

epub = os.path.join(OUT, "book26-dram-buried-wordline-trench-etch.epub")
uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "dram-buried-wordline-trench-etch/book26"))
with zipfile.ZipFile(epub, "w") as z:
    z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip")
    z.writestr("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
    items, spine, nav = [], [], []
    for sid, lab, title, _ in secs:
        fn = f"{sid}.xhtml"
        z.writestr("OEBPS/" + fn, xhtml(title, re.sub(r'href="#(\w+)"', r'href="\1.xhtml"', bodies[sid])), zipfile.ZIP_DEFLATED)
        items.append(f'<item id="{sid}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{sid}"/>')
        nav.append(f'<li><a href="{fn}">{html.escape(title)}</a></li>')
    z.writestr("OEBPS/nav.xhtml", '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>Contents</title></head><body><nav epub:type="toc"><h1>Contents</h1><ol>' + "".join(nav) + "</ol></nav></body></html>", zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", f'<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="id">{uid}</dc:identifier><dc:title>{TITLE}</dc:title><dc:language>en</dc:language><meta property="dcterms:modified">2026-10-04T00:00:00Z</meta></metadata><manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="css" href="style.css" media-type="text/css"/>' + "".join(items) + "</manifest><spine>" + "".join(spine) + "</spine></package>", zipfile.ZIP_DEFLATED)
words = sum(len(t.split()) for t in plain.values())
print(f"built {len(secs)} sections, ~{words} words -> {OUT}")
