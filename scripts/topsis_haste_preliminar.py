"""Primeiro resultado TOPSIS da haste femoral com os dados atuais (PRELIMINAR).

Os valores de data/materiais.csv ainda estão "A verificar"; este resultado serve para
discutir o método, não para tirar conclusões sobre os materiais.

Gera:
  results/topsis_haste_preliminar.csv       (tabela completa, cenários A e B)
  results/topsis_haste_preliminar.md        (a mesma tabela em Markdown)
  results/figures/topsis_haste_preliminar.png / .svg
Uso: python scripts/topsis_haste_preliminar.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

from biomat_mcdm.io import build_problem
from biomat_mcdm.methods.topsis import rank, topsis

RESULTS = Path(__file__).resolve().parents[1] / "results"
AVISO = "PRELIMINAR: dados por verificar"
COR = "#2a78d6"
TEXTO, TEXTO_2 = "#0b0b0b", "#52514e"
TIPO_PT = {"benefit": "benefício", "cost": "custo", "target": "alvo"}


def calcular(cenario: str) -> pd.DataFrame:
    p = build_problem("Prótese da anca | Haste femoral", cenario)
    C = topsis(p.X, p.weights, p.types, p.targets)
    df = pd.DataFrame({"cenario": cenario, "material": p.alternatives, "C": C, "posicao": rank(C)})
    return df.sort_values("posicao"), p


def figura(tabelas: dict[str, pd.DataFrame]) -> None:
    fig, eixos = plt.subplots(1, len(tabelas), figsize=(11, 3.6), sharex=True)
    for ax, (cen, df) in zip(eixos, tabelas.items()):
        df = df.iloc[::-1]  # 1.º lugar em cima
        ax.barh(df["material"], df["C"], height=0.55, color=COR)
        for y, c in enumerate(df["C"]):
            ax.text(c + 0.01, y, f"{c:.3f}".replace(".", ","), va="center", fontsize=9, color=TEXTO)
        titulo = "Cenário A: só clínicos" if cen == "A" else "Cenário B: inclui investigação"
        ax.set_title(titulo, fontsize=10, color=TEXTO, loc="left")
        ax.set_xlim(0, 1.1)
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.1f}".replace(".", ",")))
        ax.set_xlabel("Proximidade relativa à solução ideal, C (maior = melhor)", fontsize=9, color=TEXTO_2)
        ax.tick_params(colors=TEXTO_2, labelsize=9, length=0)
        ax.grid(axis="x", color="#e4e3df", linewidth=0.6)
        ax.set_axisbelow(True)
        for lado in ("top", "right", "left"):
            ax.spines[lado].set_visible(False)
        ax.spines["bottom"].set_color("#c9c8c2")
    fig.suptitle(f"TOPSIS com critérios-alvo, haste femoral ({AVISO})",
                 fontsize=11, color=TEXTO, x=0.01, ha="left")
    fig.tight_layout()
    (RESULTS / "figures").mkdir(parents=True, exist_ok=True)
    for ext in ("png", "svg"):
        fig.savefig(RESULTS / "figures" / f"topsis_haste_preliminar.{ext}", dpi=300)
    plt.close(fig)


def main() -> None:
    tabelas, linhas_md = {}, [f"# TOPSIS da haste femoral ({AVISO})", ""]
    for cen in ("A", "B"):
        df, p = calcular(cen)
        tabelas[cen] = df
        linhas_md += [f"## Cenário {cen}", "",
                      "Critérios e pesos: " + "; ".join(
                          f"{c} ({TIPO_PT[t]}{'' if a is None else f' {a:g}'}, peso {w:.2f})"
                          for c, t, a, w in zip(p.criteria, p.types, p.targets, p.weights)), "",
                      "| Posição | Material | C |", "|---|---|---|"]
        linhas_md += [f"| {r.posicao} | {r.material} | {r.C:.3f} |".replace("0.", "0,")  # vírgula decimal
                      for r in df.itertuples()]
        linhas_md.append("")
    pd.concat(tabelas.values()).to_csv(RESULTS / "topsis_haste_preliminar.csv", index=False)
    (RESULTS / "topsis_haste_preliminar.md").write_text("\n".join(linhas_md), encoding="utf-8")
    figura(tabelas)
    print("\n".join(linhas_md))


if __name__ == "__main__":
    main()
