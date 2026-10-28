# -*- coding: utf-8 -*-
"""Renderer PPTX 16:9 editable (formas, texto, tablas e imágenes nativas)."""
import math, os, re, tempfile
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Cm, Pt, Emu
from PIL import Image, ImageDraw
import nwcommon as C
from nwcommon import label, section_title, numbered, fmt_date

W, H = 33.867, 19.05
MX = 1.7                 # margen lateral (como el histórico KRON002: banda de título 1,7 cm)
CW = W - 2 * MX          # ancho útil
TOP, BOT = 3.4, 17.5     # zona de contenido
BAND = "F2F2F2"          # banda gris de título (estilo histórico)
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


def col(h):
    return RGBColor.from_string(h)


def gradient_bg(path, w=1920, h=1080):
    """Fondo de portada: azul marino -> azul marca, con acento beige."""
    im = Image.new("RGB", (w, h))
    px = im.load()
    c1, c2, c3 = C.rgb(C.NAVY), C.rgb(C.BLUE), C.rgb(C.BEIGE)
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.65 + (1 - y / h) * 0.35)
            t = max(0.0, min(1.0, t))
            r = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
            px[x, y] = r
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle([0, h - 14, w, h], fill=c3 + (255,))
    im.save(path)
    return path


class Deck:
    def __init__(self, content):
        self.c = content
        self.m = content["meta"]
        self.lang = self.m["lang"]
        self.p = Presentation()
        self.p.slide_width, self.p.slide_height = Cm(W), Cm(H)
        self.blank = self.p.slide_layouts[6]
        self.n = 0
        self.fig_n = 0
        with Image.open(C.logo("normawind-horizontal-positive.png")) as im:
            self.logo_ar = im.width / im.height

    def L(self, k):
        return label(self.lang, k)

    # ---------- primitivas ----------
    def new(self):
        self.n += 1
        return self.p.slides.add_slide(self.blank)

    def rect(self, s, x, y, w, h, fill, line=None):
        sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Cm(x), Cm(y), Cm(w), Cm(h))
        sh.fill.solid(); sh.fill.fore_color.rgb = col(fill)
        if line: sh.line.color.rgb = col(line); sh.line.width = Pt(0.75)
        else: sh.line.fill.background()
        sh.shadow.inherit = False
        return sh

    def text(self, s, x, y, w, h, txt, size=14, color=C.INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             italic=False, spacing=None, line=None):
        tb = s.shapes.add_textbox(Cm(x), Cm(y), Cm(w), Cm(h))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = anchor
        lines = txt if isinstance(txt, list) else [txt]
        for i, t in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            if spacing is not None: p.space_after = Pt(spacing)
            if line: p.line_spacing = line
            self.runs(p, t, size, color, bold, italic)
        return tb

    def runs(self, p, t, size, color, bold=False, italic=False, sc=False):
        for tok in INLINE.split(str(t)):
            if not tok: continue
            b, i = bold, italic
            if tok.startswith("**"): tok, b = tok[2:-2], True
            elif tok.startswith("*"): tok, i = tok[1:-1], True
            r = p.add_run(); r.text = tok
            f = r.font; f.size = Pt(size); f.bold = b; f.italic = i; f.name = C.FONT_PPTX; f.color.rgb = col(color)
            if sc: r._r.get_or_add_rPr().set("cap", "small")

    def bullets(self, s, x, y, w, h, items, size=14, numbered=False, color=C.INK):
        tb = s.shapes.add_textbox(Cm(x), Cm(y), Cm(w), Cm(h))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        for i, it in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(9)
            mark = ("%d.  " % (i + 1)) if numbered else "•  "
            r = p.add_run(); r.text = mark; r.font.size = Pt(size); r.font.color.rgb = col(color); r.font.name = C.FONT_PPTX
            self.runs(p, it, size, color)
        return tb

    def pic_fill(self, s, path, x, y, w, h):
        """Imagen que cubre el rectángulo (recorta lo que sobra)."""
        with Image.open(path) as im:
            ar = im.width / im.height
        pic = s.shapes.add_picture(path, Cm(x), Cm(y), Cm(w), Cm(h))
        if w / h > ar:  # imagen más alta que la caja: recorta arriba/abajo
            k = (1 - (ar / (w / h))) / 2; pic.crop_top = pic.crop_bottom = k
        else:
            k = (1 - ((w / h) / ar)) / 2; pic.crop_left = pic.crop_right = k
        return pic

    def pic_fit(self, s, path, x, y, w, h, align="center"):
        with Image.open(path) as im:
            ar = im.width / im.height
        if w / h > ar:
            ph, pw = h, h * ar
        else:
            pw, ph = w, w / ar
        px = x + (w - pw) / 2 if align == "center" else x
        py = y + (h - ph) / 2 if align == "center" else y
        s.shapes.add_picture(path, Cm(px), Cm(py), Cm(pw), Cm(ph))
        return pw, ph

    def footer(self, s):
        """Pie discreto: código a la izquierda; a la derecha nº de página y logo NORMAWIND pequeño."""
        m = self.m
        left = " · ".join(x for x in (m.get("code"), C.doc_short_title(m)) if x)
        self.text(s, MX, 18.2, 20, 0.5, left, 8, "8A929C")
        lh = 0.6; lw = lh * self.logo_ar
        s.shapes.add_picture(C.logo("normawind-horizontal-positive.png"), Cm(W - MX - lw), Cm(18.05), height=Cm(lh))
        self.text(s, W - MX - lw - 1.7, 18.2, 1.4, 0.5, str(self.n), 8, "8A929C", align=PP_ALIGN.RIGHT)
        if m.get("example"):
            self.text(s, 20, 18.2, W - MX - lw - 1.9 - 20, 0.5, self.L("example"), 8, C.BAD, bold=True, align=PP_ALIGN.RIGHT)

    def logo_side(self, s, cx, cy, length=6.84):
        """Logo NORMAWIND horizontal girado 90° en la franja derecha del borde (sustituye a la barra taupe del histórico)."""
        h = length / self.logo_ar
        pic = s.shapes.add_picture(C.logo("normawind-horizontal-positive.png"), Cm(cx - length / 2), Cm(cy - h / 2), Cm(length), Cm(h))
        pic.rotation = 90

    def band(self, s, txt, y=1.1, h=1.2, size=20):
        """Banda gris con título en versalitas (patrón del histórico)."""
        sh = self.rect(s, MX, y, CW, h, BAND)
        tf = sh.text_frame; tf.margin_left = Cm(0.35); tf.vertical_anchor = MSO_ANCHOR.MIDDLE; tf.word_wrap = True
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
        self.runs(p, txt, size, C.INK, sc=True)
        return sh

    def title(self, s, kicker, title):
        self.band(s, ("%s  –  %s" % (kicker, title)) if kicker else title, size=20 if len(title) < 50 else 17)

    # ---------- slides fijos ----------
    def cover(self):
        """Portada clara: título a la izquierda, panel de imagen a la derecha, cliente y logo abajo."""
        s = self.new(); m = self.m
        pw = 11.9; px = W - pw - 2.2
        self.pic_fill(s, C._abs(self.c, m["cover_image"]) if m.get("cover_image") else C.photo("cover_turbine_bw.jpg"), px, 0, pw, H)
        self.logo_side(s, 32.78, 15.0)
        tb = s.shapes.add_textbox(Cm(2.4), Cm(2.2), Cm(16.6), Cm(9.5))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        title = m["title"]
        lines = [(C.type_name(self.lang, m.get("doc_type", "")).upper(), 36, 22), (title.upper(), 22 if len(title) < 60 else 18, 18)]
        if m.get("subtitle"):
            lines.append((m["subtitle"].upper(), 16, 18))
        loc = " – ".join(x for x in (m.get("project"), m.get("location")) if x)
        if loc:
            lines.append((loc.upper(), 16, 4))
        lines.append((fmt_date(m.get("date"), self.lang).upper(), 16, 0))
        for i, (t, sz, after) in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(after)
            self.runs(p, t, sz, C.NAVY if i == 0 else C.INK, bold=(i < len(lines) - 1))
        self.text(s, 2.7, 14.3, 2.0, 0.6, self.L("client").upper() + ":", 9, C.INK)
        if m.get("client_logo"):
            self.pic_fit(s, C._abs(self.c, m["client_logo"]), 4.74, 12.97, 5.21, 2.93, "left")
            if m.get("client"):
                self.text(s, 4.54, 15.0, 9, 0.6, m["client"].upper(), 7, C.INK)
        elif m.get("client"):
            self.text(s, 4.74, 14.1, 12, 0.9, m["client"], 14, C.INK, bold=True)
        s.shapes.add_picture(C.logo("normawind-positive.png"), Cm(7.79), Cm(16.89), width=Cm(2.72))
        if m.get("example"):
            self.text(s, 2.4, 0.8, 16.6, 0.7, self.L("example"), 11, C.BAD, bold=True)

    def control(self):
        s = self.new(); m = self.m
        self.title(s, None, self.L("revision_history"))
        revs = m["revisions"]
        y = 4.2
        y += self.table(s, MX, y, 22, [self.L("version"), self.L("date"), self.L("changes")],
                        [[r["version"], fmt_date(r["date"], self.lang), r["changes"]] for r in revs], [2.5, 3.3, 16.2], size=11, plain=True) + 1.0
        y += self.table(s, MX, y, 22, [self.L("authors"), self.L("validated_by")],
                        [[", ".join(m.get("authors", [])) or "-", m.get("validated_by", "-")]], [11, 11], size=11, plain=True) + 1.0
        rows = [[self.L("document_name"), m.get("doc_name") or m["title"]], [self.L("reference"), m.get("code", "-")],
                [self.L("version"), m.get("version")], [self.L("date"), fmt_date(m.get("date"), self.lang)]]
        self._tbl(s, MX, y, 22, None, rows, [1, 2.2], 11, kv=True, plain=True)
        self.footer(s)

    def index(self, secs):
        s = self.new()
        self.title(s, None, self.L("contents"))
        items = [(n, section_title(self.lang, sec)) for n, lv, sec in numbered(secs) if lv == 1]
        half = math.ceil(len(items) / 2) if len(items) > 8 else len(items)
        for k, chunk in enumerate((items[:half], items[half:])):
            if not chunk: continue
            x = MX + 0.5 + k * 15.5
            for i, (n, t) in enumerate(chunk):
                y = 4.0 + i * 1.3
                self.text(s, x, y, 1.2, 1.0, n, 16, C.BLUE, bold=True)
                self.text(s, x + 1.4, y, 13.2, 1.0, t, 16, C.INK)
        self.footer(s)

    def divider(self, num, title):
        """Separador de sección: banda gris a media altura."""
        s = self.new()
        self.band(s, "%s  ·  %s" % (num, title), y=8.3, h=1.5, size=24)
        self.footer(s)

    def closing(self):
        """Contraportada = misma retícula que la portada (foto a la derecha, barra taupe), con logo y contacto."""
        s = self.new(); m = self.m
        pw = 11.93; px = W - pw - 2.2
        s.shapes.add_picture(C.photo("closing_team_bw.png"), Cm(px), 0, Cm(pw), Cm(H))
        self.logo_side(s, 32.92, 15.29)
        s.shapes.add_picture(C.logo("normawind-positive.png"), Cm(5.49), Cm(5.16), width=Cm(7.83))
        addr = self.L("address").split(" · ")  # [dirección, ciudad, tel, web]
        left = [addr[0], addr[1]] if len(addr) >= 4 else [addr[0]]
        right = addr[2:] if len(addr) >= 4 else []
        self.text(s, 5.49, 10.36, 3.6, 1.6, left, 12, "7F7F7F")
        if right:
            self.text(s, 9.1, 10.36, 4.8, 1.6, right, 12, "7F7F7F")
        if m.get("contact"):
            self.text(s, 5.49, 12.4, 8.4, 1.0, m["contact"], 12, "7F7F7F")
        if m.get("powered_by_emd"):
            self.text(s, 5.49, 16.0, 4.0, 0.6, "WindPRO", 9, "7F7F7F")
            s.shapes.add_picture(C.logo("emd-black.png"), Cm(5.49), Cm(16.6), height=Cm(0.9))

    # ---------- tablas ----------
    @staticmethod
    def _borders(cell, color, sides):
        """Bordes de celda (sides: subconjunto de 'LRTB'); el resto sin línea."""
        from lxml import etree
        tcPr = cell._tc.get_or_add_tcPr()
        ns = "http://schemas.openxmlformats.org/drawingml/2006/main"
        for tag in ("lnL", "lnR", "lnT", "lnB"):
            for old in tcPr.findall("{%s}%s" % (ns, tag)): tcPr.remove(old)
        for k, side in enumerate("LRTB"):
            ln = etree.Element("{%s}ln%s" % (ns, side), w="6350" if side in sides else "0")
            if side in sides:
                sf = etree.SubElement(ln, "{%s}solidFill" % ns); etree.SubElement(sf, "{%s}srgbClr" % ns, val=color)
            else:
                etree.SubElement(ln, "{%s}noFill" % ns)
            tcPr.insert(k, ln)

    def _tbl(self, s, x, y, w, header, rows, widths, size=11, kv=False, total=False, plain=False):
        tot = float(sum(widths)); cw = [w * v / tot for v in widths]
        n = len(rows) + (0 if kv else 1)
        rh = lambda r: 0.55 + 0.52 * max(1, max(math.ceil(len(str(c)) * size * 0.0185 / max(cw[j] - 0.4, 1)) for j, c in enumerate(r)))
        heights = ([] if kv else [0.85]) + [rh(r) for r in rows]
        gs = s.shapes.add_table(n, len(cw), Cm(x), Cm(y), Cm(w), Cm(sum(heights)))
        tbl = gs.table
        tblPr = gs._element.graphic.graphicData.tbl.tblPr
        for a in ("bandRow", "firstRow"):
            tblPr.set(a, "0")
        for j, v in enumerate(cw):
            tbl.columns[j].width = Cm(v)
        for i, hh in enumerate(heights):
            tbl.rows[i].height = Cm(hh)

        def fill(cell, txt, bg, fg, bold=False, align=PP_ALIGN.LEFT, sides="B", bcol="D5DAE1"):
            cell.fill.solid(); cell.fill.fore_color.rgb = col(bg)
            cell.margin_left = cell.margin_right = Cm(0.25); cell.margin_top = cell.margin_bottom = Cm(0.08)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]; p.alignment = align
            self.runs(p, txt, size, fg, bold)
            self._borders(cell, bcol, sides)

        from render_docx import is_num
        r0 = 0
        if not kv:
            for j, h in enumerate(header):
                numcol = j > 0 and all(is_num(r[j]) for r in rows)
                al = PP_ALIGN.CENTER if numcol else PP_ALIGN.LEFT
                if plain:  # control de versiones: cabecera gris, bordes finos
                    fill(tbl.cell(0, j), h, "D9D9D9", C.INK, True, al, "LRTB", "7F7F7F")
                else:      # cabecera de color + subrayado, como las tablas del histórico
                    fill(tbl.cell(0, j), h, C.NAVY, "FFFFFF", True, al, "B", C.NAVY)
            r0 = 1
        for i, r in enumerate(rows):
            for j, v in enumerate(r):
                if kv:
                    if plain:
                        fill(tbl.cell(i, j), v, "D9D9D9" if j == 0 else "FFFFFF", C.INK, j == 0, sides="LRTB", bcol="7F7F7F")
                    else:
                        fill(tbl.cell(i, j), v, BAND if j == 0 else "FFFFFF", C.NAVY if j == 0 else C.INK, j == 0)
                else:
                    numcol = j > 0 and all(is_num(rr[j]) for rr in rows)
                    is_tot = total and i == len(rows) - 1
                    al = PP_ALIGN.CENTER if numcol else PP_ALIGN.LEFT
                    if plain:
                        fill(tbl.cell(i + r0, j), v, "FFFFFF", C.INK, False, al, "LRTB", "7F7F7F")
                    else:  # sin cebra; fila total / destacada en azul claro
                        fill(tbl.cell(i + r0, j), v, C.PALEBLUE if is_tot else "FFFFFF", C.NAVY if is_tot else C.INK, is_tot, al)
        return sum(heights)

    def table(self, s, x, y, w, header, rows, widths=None, size=11, total=False, plain=False):
        return self._tbl(s, x, y, w, header, rows, widths or [1] * len(header), size, total=total, plain=plain)

    def kv(self, s, x, y, w, rows, size=12):
        return self._tbl(s, x, y, w, None, rows, [1, 2.2], size, kv=True)

    # ---------- contenido ----------
    def kpis(self, s, x, y, w, items):
        n = len(items); gap = 0.4; cw = (w - gap * (n - 1)) / n
        for i, it in enumerate(items):
            cx = x + i * (cw + gap)
            self.rect(s, cx, y, cw, 2.5, "FFFFFF", "BFC6CF")
            self.rect(s, cx, y, cw, 0.1, C.NAVY)
            val = str(it["value"]) + ((" " + it["unit"]) if it.get("unit") else "")
            self.text(s, cx + 0.3, y + 0.35, cw - 0.6, 1.2, val, 24 if len(val) < 14 else 18, C.NAVY, bold=True)
            self.text(s, cx + 0.3, y + 1.6, cw - 0.6, 0.8, it["label"], 11, C.GREY)

    def callout(self, s, x, y, w, spec):
        """Recuadro con borde fino y texto en cursiva (como las notas del histórico); el color indica el tipo."""
        kind = spec.get("kind", "info")
        c, bg = {"info": ("7F7F7F", "FFFFFF"), "warn": (C.WARN, "FFF8E8"), "ok": (C.OK, "EEF8F2"), "bad": (C.BAD, "FDF0EE")}[kind]
        txt = ("**%s**  " % spec["title"] if spec.get("title") else "") + spec["text"]
        h = self.call_h(spec, w)
        sh = self.rect(s, x, y, w, h, bg, c); sh.line.width = Pt(1.25)
        self.text(s, x + 0.4, y + 0.3, w - 0.8, h - 0.4, txt, 13, C.INK, italic=True)
        return h

    def call_h(self, spec, w):
        txt = (spec["title"] + "  " if spec.get("title") else "") + spec["text"]
        return 0.7 + 0.58 * max(1, math.ceil(len(txt) * 13 * 0.0185 / (w - 0.8)))

    def tlines(self, txt, w, size):
        cpl = max(8, w / (size * 0.0185))
        return max(1, math.ceil(len(str(txt)) / cpl))

    def flat(self, blocks):
        """Convierte bloques en elementos: ('text', block, altura_cm, ancho_ref) o ('vis', block)."""
        out = []
        for b in blocks:
            if "p" in b: out.append(("text", b))
            elif "bullets" in b or "numbered" in b: out.append(("text", b))
            elif "subheading" in b: out.append(("text", b))
            elif "callout" in b: out.append(("call", b))
            elif "kpis" in b: out.append(("kpi", b))
            elif "table" in b or "keyvalue" in b or "figure" in b: out.append(("vis", b))
        return out

    def text_h(self, b, w, size):
        if "p" in b: return self.tlines(b["p"], w, size) * size * 0.0353 * 1.22 + 0.35
        if "subheading" in b: return 1.2
        items = b.get("bullets") or b.get("numbered")
        return sum(self.tlines(i, w - 0.9, size) * size * 0.0353 * 1.22 + 0.25 for i in items)

    def draw_text(self, s, b, x, y, w, size):
        if "p" in b:
            h = self.text_h(b, w, size); self.text(s, x, y, w, h, b["p"], size); return h
        if "subheading" in b:
            self.text(s, x, y, w, 0.9, b["subheading"], size + 2, C.INK, bold=True); return 1.3
        items = b.get("bullets") or b.get("numbered")
        h = self.text_h(b, w, size)
        self.bullets(s, x, y, w, h, items, size, numbered="numbered" in b); return h

    def vis_split(self, b, max_rows=9):
        """Divide tablas largas en trozos."""
        if "table" in b and len(b["table"]["rows"]) > max_rows:
            t = b["table"]; chunks = [t["rows"][i:i + max_rows] for i in range(0, len(t["rows"]), max_rows)]
            return [{"table": dict(t, rows=ch, caption=(t.get("caption") if k == 0 else None))} for k, ch in enumerate(chunks)]
        return [b]

    def draw_vis(self, s, b, x, y, w, h):
        if "figure" in b:
            f = b["figure"]; self.fig_n += 1
            cap = ("%s %d. %s" % (self.L("figure"), self.fig_n, f["caption"])) if f.get("caption") else None
            ch = 0.7 if cap else 0
            pw, ph = self.pic_fit(s, f["path"], x, y, w, h - ch - 0.1, "center")
            if cap: self.text(s, x, y + ph + 0.15 if False else y + (h - ch - 0.1 - ph) / 2 + ph + 0.12, w, 0.6, cap, 10, C.GREY, italic=True, align=PP_ALIGN.CENTER)
        elif "table" in b:
            t = b["table"]; yy = y
            if t.get("caption"):
                self.text(s, x, yy, w, 0.6, t["caption"], 11, C.GREY, italic=True); yy += 0.8
            nc = len(t["header"])
            size = 14 if nc <= 3 else (13 if nc <= 4 else (12 if nc <= 6 else 10))
            if nc <= 3 and not t.get("widths"):
                w = min(w, 8.5 * nc)  # tablas estrechas: no estirarlas a todo el ancho
            th = self.table(s, x, yy, w, t["header"], t["rows"], t.get("widths"), size, total=bool(t.get("total_row")))
            if t.get("source"):
                self.text(s, x, yy + th + 0.15, w, 0.5, "%s: %s" % (self.L("source"), t["source"]), 9, C.GREY, italic=True)
        elif "keyvalue" in b:
            k = b["keyvalue"]; yy = y
            if k.get("caption"):
                self.text(s, x, yy, w, 0.6, k["caption"], 11, C.GREY, italic=True); yy += 0.8
            self.kv(s, x, yy, min(w, 20), k["rows"], 14)

    def content(self, kicker, title, blocks):
        els = []
        for k, b in self.flat(blocks):
            if k == "vis":
                for piece in self.vis_split(b): els.append(("vis", piece))
            else:
                els.append((k, b))
        if not els:
            return
        slides, cur = [], {"kpi": None, "text": [], "call": [], "vis": []}

        def flush():
            nonlocal cur
            if cur["kpi"] or cur["text"] or cur["call"] or cur["vis"]:
                slides.append(cur)
            cur = {"kpi": None, "text": [], "call": [], "vis": []}

        TW = 12.5  # ancho columna texto cuando hay visual
        TS, FS = 16, 18  # tamaño de texto con visual / sin visual (más contenido por lámina, como el histórico)

        def small_tab(v):
            return ("keyvalue" in v) or ("table" in v and len(v["table"]["rows"]) <= 7 and len(v["table"]["header"]) <= 3)

        for k, b in els:
            if k == "kpi":
                if cur["kpi"]: flush()
                cur["kpi"] = b["kpis"]
            elif k == "call":
                cur["call"].append(b["callout"])
            elif k == "text":
                sz = TS if cur["vis"] else FS
                w_ = TW if cur["vis"] else W - 2 * MX
                used = sum(self.text_h(x, w_, sz) for x in cur["text"])
                avail = (BOT - TOP) - (3.0 if cur["kpi"] else 0) - 1.8 * len(cur["call"])
                if used + self.text_h(b, w_, sz) > avail: flush()
                cur["text"].append(b)
            elif k == "vis":
                if cur["vis"]:
                    one = cur["vis"][0]
                    pair = (len(cur["vis"]) == 1 and not cur["text"] and (
                        ("figure" in b and "figure" in one) or
                        ("figure" in b and small_tab(one)) or ("figure" in one and small_tab(b))))
                    if not pair: flush()
                cur["vis"].append(b)
        flush()
        for sl in slides:
            s = self.new(); self.title(s, kicker, title)
            y = TOP
            if sl["kpi"]:
                self.kpis(s, MX, y, W - 2 * MX, sl["kpi"]); y += 3.0
            vis, text = sl["vis"], sl["text"]
            cwid = W - 2 * MX
            ch = [self.call_h(c, cwid) for c in sl["call"]]
            # con visual, los callouts se anclan abajo; sin visual, fluyen tras el texto
            reserve = (sum(ch) + 0.3 * len(ch) + 0.2) if (sl["call"] and vis) else 0
            area_h = BOT - y - reserve
            end_y = y
            if vis and text:
                ty = y
                for b in text:
                    ty += self.draw_text(s, b, MX, ty, TW, TS)
                self.draw_vis(s, vis[0], MX + TW + 1.0, y, cwid - TW - 1.0, area_h)
            elif vis:
                if len(vis) == 2:
                    tw_ = 12.5
                    small = [small_tab(v) for v in vis]
                    ws = [tw_ if small[0] else cwid - tw_ - 0.8, tw_ if small[1] else cwid - tw_ - 0.8]
                    if not any(small):
                        ws = [(cwid - 0.8) / 2] * 2
                    xx = MX
                    for v, ww in zip(vis, ws):
                        self.draw_vis(s, v, xx, y, ww, area_h); xx += ww + 0.8
                else:
                    self.draw_vis(s, vis[0], MX, y, cwid, area_h)
            elif text:
                n_items = sum(len(b.get("bullets") or b.get("numbered") or [1]) for b in text)
                total_h = sum(self.text_h(b, cwid, FS) for b in text)
                if total_h > area_h * 0.85 and n_items > 6:  # dos columnas
                    half = max(1, len(text) // 2)
                    cw = (cwid - 1.0) / 2
                    ty = y
                    for b in text[:half]: ty += self.draw_text(s, b, MX, ty, cw, TS)
                    end_y = ty; ty = y
                    for b in text[half:]: ty += self.draw_text(s, b, MX + cw + 1.0, ty, cw, TS)
                    end_y = max(end_y, ty)
                else:
                    ty = y
                    for b in text: ty += self.draw_text(s, b, MX, ty, cwid, FS)
                    end_y = ty
            cy = (BOT - reserve + 0.2) if vis else (end_y + 0.3)
            for c, hh in zip(sl["call"], ch):
                self.callout(s, MX, cy, cwid, c); cy += hh + 0.3
            self.footer(s)

    def build(self):
        secs = self.c["sections"]
        self.cover(); self.control(); self.index(secs)
        for n, lv, node in numbered(secs):
            if lv != 1:
                continue
        for i, sec in enumerate(secs, 1):
            title = section_title(self.lang, sec)
            subs = sec.get("subsections", []) or []
            if len(subs) >= 2:
                self.divider(i, title)
            if sec["blocks"]:
                self.content(None, title, sec["blocks"])
            for j, sub in enumerate(subs, 1):
                st = sub.get("title") or section_title(self.lang, sub)
                self.content(title, st, sub["blocks"])
        self.closing()
        return self.p


def render(content, out_path):
    Deck(content).build().save(out_path)
    return out_path
