# -*- coding: utf-8 -*-
"""CLI: contenido YAML -> DOCX / PPTX / HTML / PDF con la marca NORMAWIND.

Uso:
  python -I build_report.py contenido.yaml --formats docx,pdf,html --out carpeta
  python -I build_report.py --list-types
"""
import time, argparse, os, re, subprocess, sys, tempfile, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nwcommon as C

PS1 = Path(__file__).resolve().parent / "office_export.ps1"


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")[:60]


def validate(c):
    m = c["meta"]; errs, warns = [], []
    st = C.strings()
    if not m.get("title"): errs.append("meta.title obligatorio")
    t = m.get("doc_type")
    types = C.report_types()
    if t not in types:
        errs.append("meta.doc_type '%s' no existe. Tipos: %s" % (t, ", ".join(types)))
    for s in c["sections"]:
        for node in [s] + list(s.get("subsections", []) or []):
            if "id" in node and node["id"] not in st["sections"]:
                errs.append("sección id '%s' sin traducción en data/strings.yaml" % node["id"])
            if "id" not in node and not node.get("title"):
                errs.append("sección sin id ni title")
            for b in node.get("blocks", []):
                if "figure" in b and not os.path.exists(b["figure"]["path"]):
                    errs.append("imagen no encontrada: %s" % b["figure"]["path"])
    if t in types:
        have = {s.get("id") for s in c["sections"]}
        for sid in types[t]["sections"]:
            if sid.endswith("*") and sid[:-1] not in have:
                warns.append("falta la sección obligatoria '%s' del tipo %s" % (sid[:-1], t))
    return errs, warns


def run_ps(*args):
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(PS1), *args]
    for attempt in (1, 2, 3):  # Office COM a veces falla de forma intermitente (diálogo modal): reintentar
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode == 0:
            return
        time.sleep(3)
    raise RuntimeError((r.stderr or r.stdout).strip()[:600])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content", nargs="?")
    ap.add_argument("--formats", default="")
    ap.add_argument("--out", default=".")
    ap.add_argument("--name", default="")
    ap.add_argument("--list-types", action="store_true")
    ap.add_argument("--no-office", action="store_true", help="no usar Word/PowerPoint (sin PDF, índice se actualiza al abrir)")
    a = ap.parse_args()
    if a.list_types:
        for k, v in C.report_types().items():
            print("%-28s style=%-8s primary=%-5s formats=%s" % (k, v["style"], v["primary"], ",".join(v["formats"])))
        return
    c = C.load_content(a.content)
    errs, warns = validate(c)
    for w in warns: print("AVISO:", w)
    if errs:
        for e in errs: print("ERROR:", e)
        sys.exit(1)
    m = c["meta"]
    tdef = C.report_types()[m["doc_type"]]
    fmts = [f.strip().lower() for f in (a.formats or tdef["primary"]).split(",") if f.strip()]
    out = Path(a.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    base = a.name or "_".join(x for x in (m.get("date", "").replace("-", ""), m.get("code"), slug(m.get("short_title") or m["title"]), m["lang"].upper()) if x)
    style = c.get("style") or tdef["style"]
    made = []

    import render_docx, render_pptx, render_html
    use_office = not a.no_office and sys.platform == "win32"

    if "docx" in fmts or ("pdf" in fmts and style != "deck"):
        p = out / (base + ".docx") if "docx" in fmts else Path(tempfile.gettempdir()) / (base + ".docx")
        render_docx.render(c, str(p), update_toc_on_open=not use_office)
        if "docx" in fmts: made.append(p)
        if use_office:
            pdf = out / (base + ".pdf") if ("pdf" in fmts and style != "deck") else None
            run_ps("-Mode", "word", "-In", str(p), "-Pdf", str(pdf) if pdf else "", "-UpdateFields")
            if pdf: made.append(pdf)
    if "pptx" in fmts or ("pdf" in fmts and style == "deck"):
        p = out / (base + ".pptx") if "pptx" in fmts else Path(tempfile.gettempdir()) / (base + ".pptx")
        render_pptx.render(c, str(p))
        if "pptx" in fmts: made.append(p)
        if "pdf" in fmts and style == "deck" and use_office:
            pdf = out / (base + ".pdf")
            run_ps("-Mode", "ppt", "-In", str(p), "-Pdf", str(pdf)); made.append(pdf)
    if "html" in fmts:
        p = out / (base + ".html"); render_html.render(c, str(p)); made.append(p)
    for p in made:
        print("OK  %s  (%.1f MB)" % (p, p.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
