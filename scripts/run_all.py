"""Corre todos os cenários de data/cenarios.csv nos 3 casos quantitativos (haste, stent, scaffold).

Resultado principal: η = 1 (data/parametros.csv). Cenários de sensibilidade (Q, η, T, C-custo)
partem do cenário A. PRELIMINAR enquanto os valores da base estiverem "A verificar".

Gera:
  results/rankings_cenarios.csv   posição de cada material por caso, cenário, variante e método
  results/monte_carlo.csv         % de 1.º lugar e posição média (MC propriedades e W pesos)
  results/spearman.csv            concordância entre métodos por cenário e variante
  results/resumo_robustez.md      resumo por caso
Uso: python scripts/run_all.py [--n-iter 10000] [--seed 42]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from biomat_mcdm.io import DATA, DecisionProblem, build_problem, load_parametros, load_tissue
from biomat_mcdm.pipeline import METODOS, fmt_pt
from biomat_mcdm.robustness import (com_alvo, com_eta, com_peso, monte_carlo, pct_primeiro,
                                    posicoes, rank_agreement, sem_ordinais)

RESULTS = Path(__file__).resolve().parents[1] / "results"
AVISO = "PRELIMINAR: dados por verificar"
CASOS = {"Haste": "Prótese da anca | Haste femoral", "Stent": "Stent vascular",
         "Scaffold": "Scaffold (regeneração óssea)"}
BASE = "A"  # cenário de partida das análises de sensibilidade
SENTINELAS = (60, 120, 600, 1200)  # meses (opção O1)
ETAS = [round(0.1 * k, 1) for k in range(11)]
ALVOS_HASTE = (14, 15, 17, 20)  # GPa: Petković et al. 2025 (14) e osso cortical 15-20 (tecido.csv)
PESO_CUSTO = {"baixo": 0.01, "elevado": 0.25}
CUSTO = "Custo relativo de material e fabrico (1-5, 5 = mais caro)"
# T-scaffold: alvos alternativos a partir do osso trabecular (tecido.csv); sem referência no
# tecido para o tempo de degradação: fatores de sensibilidade x0,5 e x2 sobre o alvo.
T_SCAFFOLD = {"Resistência à compressão (scaffold)": ("Osso trabecular", "Resistência à compressão"),
              "Módulo de compressão (scaffold)": ("Osso trabecular", "Módulo de Young"),
              "Porosidade": ("Osso trabecular", "Porosidade")}
FATORES_DEGRADACAO = (0.5, 2.0)


def aplica(casos: str, caso: str) -> bool:
    """O cenário aplica-se ao caso? ("Todos", "Todos os quantitativos" ou lista de nomes)."""
    return casos.startswith("Todos") or caso.lower() in casos.lower()


def variantes(codigo: str, caso: str, data_dir: Path = DATA) -> list[tuple[str, DecisionProblem]]:
    """Problemas a ordenar para um cenário (W, M e MC tratam-se à parte)."""
    nome = CASOS[caso]
    base = build_problem(nome, BASE, data_dir)
    if codigo in ("A", "B", "B-bio"):
        return [(codigo, build_problem(nome, codigo, data_dir))]
    if codigo == "R-sentinela":
        return [(f"{s} meses", build_problem(nome, "B", data_dir, {"Tempo de reabsorção": s}))
                for s in SENTINELAS]
    if codigo == "Q":
        return [("sem ordinais", sem_ordinais(base))]
    if codigo == "η":
        return [(f"η = {fmt_pt(e, 1)}", com_eta(base, e)) for e in ETAS]
    if codigo == "T-haste":
        out = [(f"alvo {a} GPa", com_alvo(base, "Módulo de Young", float(a))) for a in ALVOS_HASTE]
        return out + [("módulo como custo", com_alvo(base, "Módulo de Young", None, "cost"))]
    if codigo == "T-scaffold":
        tec = load_tissue(data_dir)
        out = []
        for crit, (tecido, prop) in T_SCAFFOLD.items():
            t = tec[(tec["tecido"] == tecido) & (tec["propriedade"] == prop)].iloc[0]
            for lado in ("min", "max"):
                out.append((f"{crit.split(' (')[0]}: {t[lado]:g}", com_alvo(base, crit, float(t[lado]))))
        j = base.criteria.index("Tempo de degradação")
        for f in FATORES_DEGRADACAO:
            out.append((f"Tempo de degradação: x{fmt_pt(f, 1)}",
                        com_alvo(base, "Tempo de degradação", base.targets[j] * f)))
        return out
    if codigo == "C-custo":
        return [(f"custo {k} ({fmt_pt(v, 2)})", com_peso(base, CUSTO, v)) for k, v in PESO_CUSTO.items()]
    return []


def ranking_linhas(caso: str, cenario: str, variante: str, p: DecisionProblem) -> list[dict]:
    linhas = []
    for m in METODOS:
        pos = posicoes(p.X, p.weights, p.types, p.targets, m)
        linhas += [{"caso": caso, "cenario": cenario, "variante": variante, "metodo": m,
                    "material": a, "posicao": int(r)} for a, r in zip(p.alternatives, pos)]
    return linhas


def spearman_linhas(rk: pd.DataFrame) -> pd.DataFrame:
    """Spearman entre os três métodos para cada caso, cenário e variante."""
    out = []
    for (caso, cen, var), g in rk.groupby(["caso", "cenario", "variante"], sort=False):
        piv = g.pivot(index="material", columns="metodo", values="posicao")
        if len(piv) < 3:
            continue  # com 2 materiais a correlação não tem significado
        for i, a in enumerate(METODOS):
            for b in METODOS[i + 1:]:
                out.append({"caso": caso, "cenario": cen, "variante": var, "par": f"{a}-{b}",
                            "rho": rank_agreement(piv[a], piv[b])})
    return pd.DataFrame(out)


def mc_linhas(caso: str, p: DecisionProblem, n_iter: int, seed: int,
              incerteza_valor_unico: float = 0.0) -> list[dict]:
    linhas = []
    for analise, variar in (("MC propriedades", "propriedades"), ("W pesos ±20 %", "pesos")):
        for m in METODOS:
            r = monte_carlo(p, m, n_iter, seed, variar=variar,
                            incerteza_valor_unico=incerteza_valor_unico)
            for a, pct, med in zip(p.alternatives, pct_primeiro(r), r.mean(axis=0)):
                linhas.append({"caso": caso, "analise": analise, "metodo": m, "material": a,
                               "pct_primeiro": pct, "posicao_media": med, "n_iter": n_iter, "seed": seed,
                               "incerteza_valor_unico": incerteza_valor_unico if variar == "propriedades" else 0.0})
    return linhas


def vencedores(g: pd.DataFrame) -> str:
    return " = ".join(sorted(g[g["posicao"] == 1]["material"]))


def resumo_md(rk: pd.DataFrame, mc: pd.DataFrame, sp: pd.DataFrame, cen: pd.DataFrame,
              n_iter: int, seed: int) -> str:
    """Resumo por caso: vencedores, Monte Carlo, Spearman e onde o vencedor muda."""
    L = [f"# Resumo da robustez ({AVISO})", "",
         f"η = 1 no resultado principal; sensibilidades a partir do cenário {BASE}. "
         f"Monte Carlo: {n_iter} iterações, seed {seed}.", ""]
    if not mc.empty and "incerteza_valor_unico" in mc:
        inc = mc["incerteza_valor_unico"].max()
        if inc:
            L[-2] += (f" No MC propriedades, as propriedades quantitativas com mín. = máx. variam "
                      f"±{fmt_pt(100 * inc, 0)} % à volta do típico (data/parametros.csv).")
    desc = dict(zip(cen["cenario"], cen["descricao"]))
    for caso in CASOS:
        r = rk[rk["caso"] == caso]
        base = {m: vencedores(r[(r["cenario"] == BASE) & (r["metodo"] == m)]) for m in METODOS}
        L += [f"## {caso}", "", f"Vencedor no cenário {BASE}: " +
              "; ".join(f"{m} {v}" for m, v in base.items()), "",
              "### Vencedor por cenário e método", "",
              "| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |", "|---|---|---|---|---|---|"]
        muda = []
        for (c, v), g in r.groupby(["cenario", "variante"], sort=False):
            venc = {m: vencedores(g[g["metodo"] == m]) for m in METODOS}
            s = sp[(sp["caso"] == caso) & (sp["cenario"] == c) & (sp["variante"] == v)]
            rho = fmt_pt(s["rho"].min(), 2) if not s.empty else "n/a"
            nota = " (comparação)" if c == "B-bio" else ""
            L.append(f"| {c}{nota} | {v} | " + " | ".join(venc[m] for m in METODOS) + f" | {rho} |")
            if c not in (BASE, "B-bio"):
                muda += [f"- {c}, {v}, {m}: {base[m]} → {venc[m]}" for m in METODOS if venc[m] != base[m]]
        L += ["", "### Monte Carlo: % de 1.º lugar", ""]
        for analise, g in mc[mc["caso"] == caso].groupby("analise", sort=False):
            piv = g.pivot(index="material", columns="metodo", values="pct_primeiro")[METODOS]
            piv = piv.sort_values("TOPSIS", ascending=False)
            L += [f"**{analise}**", "", "| Material | " + " | ".join(METODOS) + " |", "|---|---|---|---|"]
            L += [f"| {a} | " + " | ".join(f"{fmt_pt(x, 1)} %" for x in row) + " |" for a, row in piv.iterrows()]
            L.append("")
        L += ["### Onde o vencedor muda (face ao cenário " + BASE + ")", ""]
        L += muda if muda else ["- Em nenhum cenário de sensibilidade."]
        L.append("")
    L += ["## Cenários", ""] + [f"- **{k}**: {v}" for k, v in desc.items()] + [""]
    return "\n".join(L)


def correr(n_iter: int = 10_000, seed: int = 42, data_dir: Path = DATA) -> tuple[pd.DataFrame, ...]:
    """Corre tudo; devolve (rankings, monte_carlo, spearman, cenarios). Não grava ficheiros."""
    cen = pd.read_csv(data_dir / "cenarios.csv")
    rk, mc = [], []
    inc = load_parametros(data_dir).get("incerteza_valor_unico", 0.0)
    for caso, nome in CASOS.items():
        for c in cen.itertuples():
            if not aplica(c.casos, caso):
                continue
            for var, p in variantes(c.cenario, caso, data_dir):
                rk += ranking_linhas(caso, c.cenario, var, p)
        if any(aplica(c.casos, caso) for c in cen.itertuples() if c.cenario in ("MC", "W")):
            mc += mc_linhas(caso, build_problem(nome, BASE, data_dir), n_iter, seed, inc)
    rk = pd.DataFrame(rk)
    return rk, pd.DataFrame(mc), spearman_linhas(rk), cen


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--n-iter", type=int, default=10_000)
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()
    rk, mc, sp, cen = correr(a.n_iter, a.seed)
    RESULTS.mkdir(exist_ok=True)
    rk.to_csv(RESULTS / "rankings_cenarios.csv", index=False)
    mc.to_csv(RESULTS / "monte_carlo.csv", index=False)
    sp.to_csv(RESULTS / "spearman.csv", index=False)
    texto = resumo_md(rk, mc, sp, cen, a.n_iter, a.seed)
    (RESULTS / "resumo_robustez.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
