# -*- coding: utf-8 -*-
"""Genera un montaje PNG de páginas/diapositivas de un PDF para revisión visual.

Uso: python -I preview.py archivo.pdf --pages 1-12 --out preview.png [--cols 4] [--dpi 55]
"""
import argparse
import pymupdf
from PIL import Image


def parse_pages(s, n):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-"); out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return [p for p in out if 1 <= p <= n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--pages", default="1-12")
    ap.add_argument("--out", default="preview.png")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--dpi", type=int, default=55)
    a = ap.parse_args()
    d = pymupdf.open(a.pdf)
    pages = parse_pages(a.pages, len(d))
    ims = []
    for p in pages:
        px = d[p - 1].get_pixmap(dpi=a.dpi)
        ims.append(Image.frombytes("RGB", (px.width, px.height), px.samples))
    w = max(i.width for i in ims); h = max(i.height for i in ims)
    rows = (len(ims) + a.cols - 1) // a.cols
    m = Image.new("RGB", (w * a.cols, h * rows), "white")
    for i, im in enumerate(ims):
        m.paste(im, ((i % a.cols) * w, (i // a.cols) * h))
    m.save(a.out)
    print("%s: %d páginas totales; montaje de %d en %s" % (a.pdf, len(d), len(ims), a.out))


if __name__ == "__main__":
    main()
