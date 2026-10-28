# -*- coding: utf-8 -*-
"""Renderer HTML autónomo (un solo archivo, imágenes en base64, responsive, con estilos de impresión)."""
import base64, html, mimetypes, re
import nwcommon as C
from nwcommon import label, section_title, numbered, fmt_date

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")

CSS = """
:root{--navy:#%(NAVY)s;--blue:#%(BLUE)s;--sky:#%(SKY)s;--taupe:#%(TAUPE)s;--beige:#%(BEIGE)s;--ink:#%(INK)s;--grey:#%(GREY)s;
--light:#%(LIGHT)s;--pale:#%(PALEBLUE)s;--ok:#%(OK)s;--warn:#%(WARN)s;--bad:#%(BAD)s;--bg:#fff;--line:#D9DEE5}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Calibri,'Segoe UI',Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.55;font-size:16px}
.hero{background:linear-gradient(135deg,var(--navy),var(--blue));color:#fff;padding:36px 6vw 56px;border-bottom:6px solid var(--beige)}
.hero img.logo{height:44px;display:block;margin-bottom:56px}
.hero .kicker{color:var(--sky);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.85rem}
.hero h1{font-size:clamp(1.9rem,4.2vw,3rem);line-height:1.1;margin:.4em 0 .3em;max-width:22em}
.hero .sub{color:var(--beige);font-size:1.2rem}
.hero .meta{display:flex;flex-wrap:wrap;gap:8px 32px;margin-top:28px;font-size:.95rem}
.hero .meta b{display:block;color:var(--beige);font-size:.72rem;letter-spacing:.08em;text-transform:uppercase}
.tag{display:inline-block;background:#ffffff22;border:1px solid #ffffff66;border-radius:4px;padding:2px 10px;font-weight:700;margin-top:18px}
.layout{display:grid;grid-template-columns:260px minmax(0,1fr);gap:0 48px;max-width:1240px;margin:0 auto;padding:0 5vw}
nav.toc{position:sticky;top:0;align-self:start;max-height:100vh;overflow:auto;padding:32px 0}
nav.toc h2{font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin:0 0 12px}
nav.toc a{display:block;color:var(--ink);text-decoration:none;padding:5px 0 5px 12px;border-left:3px solid var(--line);font-size:.93rem}
nav.toc a.l2{padding-left:26px;font-size:.86rem;color:var(--grey)}
nav.toc a:hover,nav.toc a.on{border-left-color:var(--blue);color:var(--blue)}
main{padding:32px 0 80px;max-width:860px}
h2.sec{color:var(--navy);font-size:1.7rem;margin:2.2em 0 .5em;padding-bottom:.25em;border-bottom:2px solid var(--blue)}
h3.sub{color:var(--navy);font-size:1.25rem;margin:1.6em 0 .4em}
h4{color:var(--blue);margin:1.2em 0 .3em}
h2.sec .n,h3.sub .n{color:var(--blue);margin-right:.5em}
p{margin:.6em 0}
ul,ol{padding-left:1.3em}
li{margin:.25em 0}
li::marker{color:var(--blue)}
figure{margin:1.4em 0;text-align:center}
figure img{max-width:100%%;height:auto;border:1px solid var(--line);border-radius:4px}
figcaption,caption{color:var(--grey);font-style:italic;font-size:.88rem;margin-top:.4em}
.tw{overflow-x:auto;margin:1.2em 0}
table{border-collapse:collapse;width:100%%;font-size:.93rem}
caption{caption-side:top;text-align:left;margin:0 0 .4em}
th{background:var(--navy);color:#fff;text-align:left;padding:8px 10px;font-weight:700}
td{padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even) td{background:var(--light)}
tr.total td{background:var(--pale)!important;font-weight:700}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
table.kv th{background:var(--pale);color:var(--navy);width:32%%}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:1.4em 0}
.kpi{background:var(--light);border-top:4px solid var(--blue);padding:14px 16px;border-radius:0 0 6px 6px}
.kpi .v{font-size:1.7rem;font-weight:700;color:var(--blue);line-height:1.1}
.kpi .v small{font-size:.8rem;color:var(--grey);font-weight:400}
.kpi .l{color:var(--grey);font-size:.85rem;margin-top:4px}
.callout{border-left:5px solid var(--blue);background:#EAF2FC;padding:12px 16px;margin:1.2em 0;border-radius:0 6px 6px 0}
.callout.warn{border-color:var(--warn);background:#FFF4DD}.callout.ok{border-color:var(--ok);background:#E3F4EA}.callout.bad{border-color:var(--bad);background:#FBE6E3}
.callout b.t{margin-right:.4em}
.src{color:var(--grey);font-size:.8rem;font-style:italic;margin-top:-.6em}
.ctrl{margin-top:2.2em}
footer.pg{border-top:1px solid var(--line);color:var(--grey);font-size:.82rem;padding:18px 6vw;text-align:center}
footer.pg img{height:28px;vertical-align:middle;margin-right:10px}
@media(max-width:900px){.layout{grid-template-columns:1fr}nav.toc{position:static;max-height:none;padding:16px 0}}
@media print{.hero{-webkit-print-color-adjust:exact;print-color-adjust:exact}nav.toc{display:none}.layout{display:block;padding:0 12mm}
 h2.sec{break-after:avoid}figure,table,.kpis,.callout{break-inside:avoid}th,.kpi,.callout,tr.total td{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 @page{size:A4;margin:14mm}}
""" % {k: getattr(C, k) for k in ("NAVY", "BLUE", "SKY", "TAUPE", "BEIGE", "INK", "GREY", "LIGHT", "PALEBLUE", "OK", "WARN", "BAD")}


def e(s):
    return html.escape(str(s))


def rich(t):
    out = []
    for tok in INLINE.split(str(t)):
        if tok.startswith("**"): out.append("<strong>%s</strong>" % e(tok[2:-2]))
        elif tok.startswith("*") and len(tok) > 2: out.append("<em>%s</em>" % e(tok[1:-1]))
        else: out.append(e(tok))
    return "".join(out)


def b64(path):
    mt = mimetypes.guess_type(path)[0] or "image/png"
    return "data:%s;base64,%s" % (mt, base64.b64encode(open(path, "rb").read()).decode())


class Page:
    def __init__(self, content):
        self.c = content; self.m = content["meta"]; self.lang = self.m["lang"]; self.fig = 0; self.tab = 0

    def L(self, k): return label(self.lang, k)

    def block(self, b):
        if "p" in b: return "<p>%s</p>" % rich(b["p"])
        if "bullets" in b: return "<ul>%s</ul>" % "".join("<li>%s</li>" % rich(i) for i in b["bullets"])
        if "numbered" in b: return "<ol>%s</ol>" % "".join("<li>%s</li>" % rich(i) for i in b["numbered"])
        if "subheading" in b: return "<h4>%s</h4>" % e(b["subheading"])
        if "figure" in b:
            f = b["figure"]; self.fig += 1
            cap = ""
            if f.get("caption"):
                cap = "<figcaption>%s %d. %s%s</figcaption>" % (self.L("figure"), self.fig, e(f["caption"]),
                      (" (%s: %s)" % (self.L("source"), e(f["source"]))) if f.get("source") else "")
            return '<figure><img src="%s" alt="%s">%s</figure>' % (b64(f["path"]), e(f.get("caption", "")), cap)
        if "table" in b:
            from render_docx import is_num
            t = b["table"]; self.tab += 1
            cap = "<caption>%s %d. %s</caption>" % (self.L("table"), self.tab, e(t["caption"])) if t.get("caption") else ""
            nums = [j > 0 and all(is_num(r[j]) for r in t["rows"]) for j in range(len(t["header"]))]
            th = "".join('<th class="%s">%s</th>' % ("num" if nums[j] else "", e(h)) for j, h in enumerate(t["header"]))
            rows = []
            for i, r in enumerate(t["rows"]):
                tot = t.get("total_row") and i == len(t["rows"]) - 1
                rows.append('<tr class="%s">%s</tr>' % ("total" if tot else "", "".join(
                    '<td class="%s">%s</td>' % ("num" if nums[j] else "", rich(v)) for j, v in enumerate(r))))
            src = '<p class="src">%s: %s</p>' % (self.L("source"), e(t["source"])) if t.get("source") else ""
            return '<div class="tw"><table>%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s' % (cap, th, "".join(rows), src)
        if "keyvalue" in b:
            k = b["keyvalue"]; cap = ""
            if k.get("caption"):
                self.tab += 1; cap = "<caption>%s %d. %s</caption>" % (self.L("table"), self.tab, e(k["caption"]))
            return '<div class="tw"><table class="kv">%s<tbody>%s</tbody></table></div>' % (
                cap, "".join("<tr><th>%s</th><td>%s</td></tr>" % (e(a), rich(v)) for a, v in k["rows"]))
        if "kpis" in b:
            return '<div class="kpis">%s</div>' % "".join(
                '<div class="kpi"><div class="v">%s%s</div><div class="l">%s</div></div>' % (
                    e(i["value"]), (" <small>%s</small>" % e(i["unit"])) if i.get("unit") else "", e(i["label"])) for i in b["kpis"])
        if "callout" in b:
            c = b["callout"]
            return '<div class="callout %s">%s%s</div>' % (c.get("kind", "info"),
                   ('<b class="t">%s</b>' % e(c["title"])) if c.get("title") else "", rich(c["text"]))
        return ""

    def build(self):
        m = self.m; secs = self.c["sections"]; nm = {id(n): k for k, lv, n in numbered(secs)}
        toc, body = [], []
        for k, lv, n in numbered(secs):
            t = n.get("title") or section_title(self.lang, n)
            toc.append('<a class="%s" href="#s%s">%s&nbsp; %s</a>' % ("l2" if lv == 2 else "", k.replace(".", "_"), k, e(t)))
        for s in secs:
            k = nm[id(s)]
            body.append('<section><h2 class="sec" id="s%s"><span class="n">%s</span>%s</h2>' % (k, k, e(section_title(self.lang, s))))
            body += [self.block(b) for b in s["blocks"]]
            for sub in s.get("subsections", []) or []:
                kk = nm[id(sub)]
                body.append('<h3 class="sub" id="s%s"><span class="n">%s</span>%s</h3>' % (kk.replace(".", "_"), kk, e(sub.get("title") or section_title(self.lang, sub))))
                body += [self.block(b) for b in sub["blocks"]]
            body.append("</section>")
        # fix ids with dots
        revs = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (e(r["version"]), e(fmt_date(r["date"], self.lang)), e(r["changes"])) for r in m["revisions"])
        meta = [(self.L("client"), m.get("client")), (self.L("project"), m.get("project")), (self.L("location"), m.get("location")),
                (self.L("reference"), m.get("code")), (self.L("version"), m.get("version")), (self.L("date"), fmt_date(m.get("date"), self.lang))]
        meta_h = "".join("<div><b>%s</b>%s</div>" % (e(a), e(b)) for a, b in meta if b)
        tag = '<div class="tag">%s</div>' % e(self.L("example")) if m.get("example") else ""
        ctrl = ('<section class="ctrl"><h2 class="sec">%s</h2><div class="tw"><table><thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>'
                '<div class="tw"><table class="kv"><tbody><tr><th>%s</th><td>%s</td></tr><tr><th>%s</th><td>%s</td></tr></tbody></table></div></section>') % (
            e(self.L("revision_history")), e(self.L("version")), e(self.L("date")), e(self.L("changes")), revs,
            e(self.L("authors")), e(", ".join(m.get("authors", [])) or "-"), e(self.L("validated_by")), e(m.get("validated_by", "-")))
        logo = b64(C.logo("normawind-horizontal-negative.png"))
        logo_pos = b64(C.logo("normawind-horizontal-positive.png"))
        clogo = ('<img class="logo" style="background:#fff;padding:8px 14px;border-radius:6px;height:56px;margin:0 0 0 auto" src="%s" alt="">' % b64(C._abs(self.c, m["client_logo"]))) if m.get("client_logo") else ""
        out = """<!doctype html>
<html lang="%(lang)s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title><style>%(css)s</style></head><body>
<header class="hero"><div style="display:flex;align-items:flex-start"><img class="logo" src="%(logo)s" alt="NORMAWIND">%(clogo)s</div>
<div class="kicker">%(type)s</div><h1>%(title)s</h1>%(sub)s<div class="meta">%(meta)s</div>%(tag)s</header>
<div class="layout"><nav class="toc"><h2>%(contents)s</h2>%(toc)s</nav><main>%(body)s%(ctrl)s</main></div>
<footer class="pg"><img src="%(logo_pos)s" alt="">%(addr)s<br>%(conf)s</footer>
<script>
const links=[...document.querySelectorAll('nav.toc a')];
const io=new IntersectionObserver(es=>{es.forEach(en=>{if(en.isIntersecting){links.forEach(l=>l.classList.toggle('on',l.getAttribute('href')==='#'+en.target.id))}})},{rootMargin:'0px 0px -75%% 0px'});
document.querySelectorAll('h2.sec[id],h3.sub[id]').forEach(h=>io.observe(h));
</script></body></html>""" % dict(
            lang=self.lang, title=e(m["title"]), css=CSS, logo=logo, clogo=clogo, type=e(C.type_name(self.lang, m.get("doc_type", ""))),
            sub=('<div class="sub">%s</div>' % e(m["subtitle"])) if m.get("subtitle") else "", meta=meta_h, tag=tag,
            contents=e(self.L("contents")), toc="".join(toc), body="\n".join(body), ctrl=ctrl, logo_pos=logo_pos,
            addr=e(self.L("address")), conf=e(self.L("confidential")))
        # unificar ids: s1_1 en toc y headings
        out = re.sub(r'id="s(\d+)\.(\d+)"', r'id="s\1_\2"', out)
        out = re.sub(r'id="s(\d+)"', r'id="s\1"', out)
        return out


def render(content, out_path):
    open(out_path, "w", encoding="utf-8").write(Page(content).build())
    return out_path
