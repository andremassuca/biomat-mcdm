"""Resultado preliminar da haste femoral com TOPSIS, WASPAS e VIKOR (PRELIMINAR).

Os valores de data/materiais.csv ainda estão "A verificar"; este resultado serve para
discutir o método, não para tirar conclusões sobre os materiais. η = 1 (só pesos subjetivos).

Gera:
  results/haste_preliminar.csv          (tabela completa, cenários A e B)
  results/haste_preliminar.md           (posições lado a lado e Spearman, em Markdown)
  results/figures/haste_preliminar.png / .svg
Uso: python scripts/haste_preliminar.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import pandas as pd

from biomat_mcdm.io import DecisionProblem, build_problem
from biomat_mcdm.pipeline import METODOS, fmt_pt, rank_all_methods, spearman_methods

CASO = "Prótese da anca | Haste femoral"
RESULTS = Path(__file__).resolve().parents[1] / "results"
AVISO = "PRELIMINAR: dados por verificar"
TIPO_PT = {"benefit": "benefício", "cost": "custo", "target": "alvo"}
TITULO_CEN = {"A": "Cenário A: só clínicos", "B": "Cenário B: inclui investigação"}
TEXTO, TEXTO_2 = "#0b0b0b", "#52514e"
# Rampa sequencial de uma só tonalidade (azul): posição 1 = mais escuro
RAMPA = LinearSegmentedColormap.from_list("azul", ["#1f5fb0", "#dbe8f7"])


def cor_texto(rgba: tuple[float, ...]) -> str:
    """Texto branco sobre fundo escuro e preto sobre fundo claro (luminância relativa WCAG)."""
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgba[:3]]
    lum = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    # escolhe o que dá maior contraste: branco (1,05 / (L + 0,05)) ou preto ((L + 0,05) / 0,05)
    return "white" if 1.05 / (lum + 0.05) > (lum + 0.05) / 0.05 else TEXTO


def calcular(cenario: str) -> tuple[pd.DataFrame, pd.DataFrame, DecisionProblem]:
    """Posições dos três métodos e matriz de Spearman para um cenário, ordenado por TOPSIS."""
    p = build_problem(CASO, cenario)
    df = rank_all_methods(p).sort_values("pos_TOPSIS").reset_index(drop=True)
    return df, spearman_methods(df), p


def criterios_md(p: DecisionProblem) -> str:
    """Lista de critérios, tipos, alvos e pesos, com vírgula decimal."""
    partes = []
    for c, t, a, w in zip(p.criteria, p.types, p.targets, p.weights):
        alvo = "" if a is None else f" {fmt_pt(a, 0) if float(a).is_integer() else fmt_pt(a, 2)}"
        partes.append(f"{c} ({TIPO_PT[t]}{alvo}, peso {fmt_pt(w, 2)})")
    return "; ".join(partes)


def tabela_md(cenario: str, df: pd.DataFrame, rho: pd.DataFrame, p: DecisionProblem) -> list[str]:
    """Secção Markdown de um cenário: critérios, posições lado a lado e Spearman."""
    linhas = [f"## {TITULO_CEN[cenario]}", "", "Critérios e pesos (η = 1): " + criterios_md(p), "",
              "| Material | TOPSIS (C) | WASPAS (Q) | VIKOR (P, menor = melhor) |", "|---|---|---|---|"]
    for r in df.itertuples():
        linhas.append(f"| {r.material} | {r.pos_TOPSIS}.º ({fmt_pt(r.C_TOPSIS)}) | "
                      f"{r.pos_WASPAS}.º ({fmt_pt(r.Q_WASPAS)}) | {r.pos_VIKOR}.º ({fmt_pt(r.P_VIKOR)}) |")
    linhas += ["", "Correlação de Spearman entre as posições:", "",
               "| | " + " | ".join(METODOS) + " |", "|---|---|---|---|"]
    for m in METODOS:
        linhas.append(f"| {m} | " + " | ".join(fmt_pt(rho.loc[m, n], 2) for n in METODOS) + " |")
    return linhas + [""]


def figura(resultados: dict[str, tuple[pd.DataFrame, pd.DataFrame]]) -> plt.Figure:
    """Grelha de posições (material x método), um painel por cenário."""
    fig, eixos = plt.subplots(1, len(resultados), figsize=(11, 3.9))
    for ax, (cen, (df, rho)) in zip(eixos, resultados.items()):
        pos = df[[f"pos_{m}" for m in METODOS]].to_numpy()
        n = len(df)
        ax.imshow(pos, cmap=RAMPA, vmin=1, vmax=n, aspect="auto")
        for i in range(n):
            for j in range(3):
                ax.text(j, i, f"{pos[i, j]}.º", ha="center", va="center", fontsize=10,
                        color=cor_texto(RAMPA((pos[i, j] - 1) / (n - 1))))
        # separadores de 2 px na cor da superfície entre as células
        for k in range(1, 3):
            ax.axvline(k - 0.5, color="white", linewidth=2)
        for k in range(1, n):
            ax.axhline(k - 0.5, color="white", linewidth=2)
        ax.set_xticks(range(3), METODOS)
        ax.set_yticks(range(n), df["material"])
        ax.xaxis.tick_top()
        ax.tick_params(colors=TEXTO_2, labelsize=9, length=0)
        for lado in ax.spines.values():
            lado.set_visible(False)
        r = rho.to_numpy()[np.triu_indices(3, 1)]
        ax.set_title(f"{TITULO_CEN[cen]}\nSpearman entre métodos: {fmt_pt(r.min(), 2)} a {fmt_pt(r.max(), 2)}",
                     fontsize=10, color=TEXTO, loc="left", pad=22)
    fig.suptitle(f"Posição da haste femoral por método, η = 1 ({AVISO})",
                 fontsize=11, color=TEXTO, x=0.01, ha="left")
    fig.tight_layout()
    return fig


def main() -> None:
    resultados, linhas = {}, [f"# Haste femoral: TOPSIS, WASPAS e VIKOR ({AVISO})", ""]
    tabelas = []
    for cen in ("A", "B"):
        df, rho, p = calcular(cen)
        resultados[cen] = (df, rho)
        linhas += tabela_md(cen, df, rho, p)
        tabelas.append(df.assign(cenario=cen))
    RESULTS.mkdir(exist_ok=True)
    pd.concat(tabelas).to_csv(RESULTS / "haste_preliminar.csv", index=False)
    (RESULTS / "haste_preliminar.md").write_text("\n".join(linhas), encoding="utf-8")
    fig = figura(resultados)
    (RESULTS / "figures").mkdir(parents=True, exist_ok=True)
    for ext in ("png", "svg"):
        fig.savefig(RESULTS / "figures" / f"haste_preliminar.{ext}", dpi=300,
                    metadata={"Date": None} if ext == "svg" else None)
    plt.close(fig)
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
