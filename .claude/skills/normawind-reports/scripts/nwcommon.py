# -*- coding: utf-8 -*-
"""Núcleo común: marca, traducciones, carga del contenido y gráficos."""
import os, re, hashlib
from pathlib import Path
import yaml

SKILL = Path(__file__).resolve().parent.parent
LOGOS = SKILL / "assets" / "logos"

# ---- Marca (extraída de los logotipos oficiales) ----
NAVY = "103870"
BLUE = "1868D0"
SKY = "5FA8F0"
TAUPE = "A89080"
BEIGE = "E8DCCB"
INK = "1F2933"
GREY = "5B6470"
LIGHT = "F3F5F8"
PALEBLUE = "DCE8F8"
OK, WARN, BAD = "2E8B57", "D98E04", "C0392B"
SERIES = [BLUE, NAVY, TAUPE, SKY, "6B7B8C", "C9B8A6"]
FONT = "Calibri"
FONT_PPTX = "Abadi Extra Light"  # fuente del histórico KRON002 (solo PPTX)

LANGS = ("en", "es", "ca")

_strings = None
_types = None


def strings():
    global _strings
    if _strings is None:
        _strings = yaml.safe_load((SKILL / "data" / "strings.yaml").read_text(encoding="utf-8"))
    return _strings


def report_types():
    global _types
    if _types is None:
        _types = yaml.safe_load((SKILL / "data" / "report_types.yaml").read_text(encoding="utf-8"))
    return _types


def label(lang, key):
    return strings()["labels"][key][lang]


def type_name(lang, type_id):
    return strings()["types"].get(type_id, {}).get(lang, type_id)


def section_title(lang, sec):
    if sec.get("title"):
        return sec["title"]
    return strings()["sections"][sec["id"]][lang]


def rgb(hexstr):
    return tuple(int(hexstr[i:i + 2], 16) for i in (0, 2, 4))


def logo(name):
    return str(LOGOS / name)


def photo(name):
    """Fotografías de portada/contraportada (assets/photos, tomadas del histórico KRON002)."""
    return str(LOGOS.parent / "photos" / name)


def rgb_tuple(h):
    return rgb(h)


# ---- Carga y normalización del contenido ----
def load_content(path):
    path = Path(path).resolve()
    c = yaml.safe_load(path.read_text(encoding="utf-8"))
    c["_dir"] = path.parent
    meta = c.setdefault("meta", {})
    meta.setdefault("lang", "es")
    if meta["lang"] not in LANGS:
        raise SystemExit("meta.lang debe ser uno de %s" % (LANGS,))
    meta.setdefault("date", "")
    meta["date"] = str(meta["date"])
    meta.setdefault("version", "V01")
    meta.setdefault("authors", [])
    meta.setdefault("revisions", [{"version": meta["version"], "date": meta["date"],
                                   "changes": label(meta["lang"], "first_version")}])
    for s in c.get("sections", []):
        _prep_blocks(c, s)
        for sub in s.get("subsections", []):
            _prep_blocks(c, sub)
    c.setdefault("sections", [])
    return c


def _abs(c, p):
    if not p:
        return p
    p = Path(p)
    return str(p if p.is_absolute() else (c["_dir"] / p).resolve())


def _prep_blocks(c, node):
    out = []
    for b in node.get("blocks", []) or []:
        if "chart" in b:
            from nwcharts import make_chart
            b = {"figure": {"path": make_chart(b["chart"], c["meta"]["lang"]),
                            "caption": b["chart"].get("caption", ""),
                            "width_cm": b["chart"].get("width_cm", 15)}}
        elif "figure" in b:
            b["figure"]["path"] = _abs(c, b["figure"]["path"])
        out.append(b)
    node["blocks"] = out


def numbered(sections):
    """Devuelve [(num, level, node)] con numeración 1, 1.1."""
    res = []
    for i, s in enumerate(sections, 1):
        res.append((str(i), 1, s))
        for j, sub in enumerate(s.get("subsections", []) or [], 1):
            res.append(("%d.%d" % (i, j), 2, sub))
    return res


def sub_title(sub):
    return sub.get("title", "")


def doc_short_title(meta):
    return meta.get("short_title") or meta.get("title", "")


def fmt_date(d, lang):
    """2026-10-28 -> 28/10/2026 (formato único para los tres idiomas)."""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", str(d))
    return "%s/%s/%s" % (m.group(3), m.group(2), m.group(1)) if m else str(d)
