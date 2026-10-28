# -*- coding: utf-8 -*-
"""Gráficos con la paleta NORMAWIND (matplotlib). Se usan desde bloques `chart:` del contenido."""
import hashlib, json, os, tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from nwcommon import SERIES as _S, NAVY, GREY, INK, FONT
SERIES = ["#" + c for c in _S]

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": [FONT, "Arial", "DejaVu Sans"],
    "axes.edgecolor": "#C5CBD3", "axes.labelcolor": "#" + GREY, "xtick.color": "#" + GREY,
    "ytick.color": "#" + GREY, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#E6E9EE", "grid.linewidth": 0.8, "axes.axisbelow": True,
    "font.size": 10,
})


def make_chart(spec, lang):
    """spec: kind (bar|line|stacked|pie|bar_line), labels, series [{name, values}], title, ylabel, xlabel."""
    key = hashlib.md5(json.dumps(spec, sort_keys=True, default=str).encode()).hexdigest()[:10]
    out = os.path.join(tempfile.gettempdir(), "nwchart_%s.png" % key)
    kind = spec.get("kind", "bar")
    labels = spec["labels"]
    series = spec["series"]
    fig, ax = plt.subplots(figsize=(spec.get("w", 7.2), spec.get("h", 3.4)), dpi=200)
    n = len(series)
    if kind == "pie":
        vals = series[0]["values"]
        _, _, autot = ax.pie(vals, labels=labels, colors=SERIES[:len(vals)], autopct="%1.1f%%", startangle=90,
                             wedgeprops={"edgecolor": "white", "linewidth": 1.5}, textprops={"color": "#" + INK, "fontsize": 9})
        for i, t in enumerate(autot):  # texto blanco sobre azul/marino
            if i % 6 in (0, 1):
                t.set_color("white"); t.set_fontweight("bold")
        ax.set_aspect("equal"); ax.grid(False)
    elif kind in ("bar", "stacked"):
        x = range(len(labels))
        if kind == "bar":
            w = 0.8 / n
            for i, s in enumerate(series):
                ax.bar([k + (i - (n - 1) / 2) * w for k in x], s["values"], w * 0.92, label=s["name"], color=SERIES[i % 6])
        else:
            bottom = [0] * len(labels)
            for i, s in enumerate(series):
                ax.bar(x, s["values"], 0.65, bottom=bottom, label=s["name"], color=SERIES[i % 6])
                bottom = [b + v for b, v in zip(bottom, s["values"])]
        ax.set_xticks(list(x)); ax.set_xticklabels(labels)
        ax.grid(axis="x", visible=False)
    elif kind == "line":
        for i, s in enumerate(series):
            ax.plot(labels, s["values"], color=SERIES[i % 6], lw=2.2, marker="o", ms=4, label=s["name"])
    if spec.get("title"):
        ax.set_title(spec["title"], loc="left", fontsize=11, fontweight="bold", color="#" + NAVY)
    if spec.get("ylabel"):
        ax.set_ylabel(spec["ylabel"])
    if spec.get("xlabel"):
        ax.set_xlabel(spec["xlabel"])
    if kind != "pie" and n > 1:
        ax.legend(frameon=False, ncol=n, loc="upper center", bbox_to_anchor=(0.5, -0.14 if not spec.get("xlabel") else -0.25))
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out
