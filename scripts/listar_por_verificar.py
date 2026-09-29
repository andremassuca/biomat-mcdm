"""Lista os valores "A verificar" de cada caso quantitativo, por influência no resultado (tarefa 12).

Para cada célula "A verificar" que entra no cenário A (e, do cenário B, as que não entram no A),
o valor típico varia ±20 % com o resto fixo; ordena por mudança do vencedor do TOPSIS e pela
maior variação do C do material. Grava results/por_verificar.md. Não altera data/.

Uso: python scripts/listar_por_verificar.py [--delta 0.2]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from biomat_mcdm.io import DATA, build_problem
from biomat_mcdm.pipeline import fmt_pt
from biomat_mcdm.por_verificar import tabela_caso, vencedor_topsis

RESULTS = Path(__file__).resolve().parents[1] / "results"
CASOS = {"Haste": "Prótese da anca | Haste femoral", "Stent": "Stent vascular",
         "Scaffold": "Scaffold (regeneração óssea)"}


def resumo_md(tabelas: dict[str, pd.DataFrame], delta: float, data_dir: Path = DATA) -> str:
    """Texto em Markdown com uma tabela por caso (só dados)."""
    pct = fmt_pt(100 * delta, 0)
    L = ["# Valores \"A verificar\" por influência no resultado", "",
         f"Cada valor típico varia ±{pct} % com o resto fixo (TOPSIS, η = 1). Ordem: primeiro os que mudam "
         "o vencedor do TOPSIS; depois pela maior variação do C do próprio material (ΔC material). "
         "ΔC máx. = maior variação do C de qualquer material. Cenário B: só as células que não entram no A. "
         "Tipo ordinal: escala 1-5 do trabalho (a variação de ±20 % é só indicativa).", ""]
    for caso, df in tabelas.items():
        venc = {c: vencedor_topsis(build_problem(CASOS[caso], c, data_dir)) for c in df["cenario"].unique()}
        L += [f"## {caso}", "",
              "Vencedor do TOPSIS: " + "; ".join(f"cenário {c}: {v}" for c, v in venc.items()) + ".",
              f"Células a verificar: {len(df)} ({(df['muda_vencedor']).sum()} mudam o vencedor com ±{pct} %).", "",
              "| # | Cenário | Material | Critério | Tipo | Típico | ΔC material | ΔC máx. | Muda vencedor | Fonte atual |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for k, r in enumerate(df.itertuples(), 1):
            muda = f"sim → {r.novo_vencedor}" if r.muda_vencedor else "não"
            fonte = "" if pd.isna(r.fonte) else str(r.fonte).replace("|", ";")
            L.append(f"| {k} | {r.cenario} | {r.material} | {r.criterio} | {r.tipo} | {fmt_pt(r.tipico, 4)} | "
                     f"{fmt_pt(r.dC_material, 3)} | {fmt_pt(r.dC_max, 3)} | {muda} | {fonte} |")
        L.append("")
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--delta", type=float, default=0.2)
    a = ap.parse_args()
    tabelas = {caso: tabela_caso(nome, delta=a.delta) for caso, nome in CASOS.items()}
    RESULTS.mkdir(exist_ok=True)
    texto = resumo_md(tabelas, a.delta)
    (RESULTS / "por_verificar.md").write_text(texto, encoding="utf-8")
    for caso, df in tabelas.items():
        print(f"{caso}: {len(df)} células a verificar, {int(df['muda_vencedor'].sum())} mudam o vencedor")


if __name__ == "__main__":
    main()
