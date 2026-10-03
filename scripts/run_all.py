"""Corre todos os cenários de data/cenarios.csv nos 3 casos quantitativos (haste, stent, scaffold).

Resultado principal: η = 1 (data/parametros.csv). Cenários de sensibilidade (Q, η, T, C-custo, P-foco)
partem do cenário A. PRELIMINAR enquanto os valores da base estiverem "A verificar".

Gera:
  results/rankings_cenarios.csv   posição de cada material por caso, cenário, variante e método
  results/pontuacoes.csv          pontuação (C, Q, P) e posição nos cenários A e B, por método
  results/monte_carlo.csv         % de 1.º, 2.º e 3.º lugar e posição média (MC propriedades e W pesos)
  results/spearman.csv            concordância entre métodos por cenário e variante
  results/resumo_robustez.md      resumo por caso
  results/semiquantitativos.csv   par articular e implante dentário: cenário A, P-foco e sensibilidades (indicação)
Uso: python scripts/run_all.py [--n-iter 10000] [--seed 42]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from biomat_mcdm.io import (DATA, DecisionProblem, build_problem, criterios_do_problema, load_parametros,
                            load_tissue)
from biomat_mcdm.pipeline import METODOS, fmt_pt, rank_all_methods
from biomat_mcdm.robustness import (com_alvo, com_eta, com_foco, com_peso, com_valor, monte_carlo, pct_posicao,
                                    pct_primeiro, posicoes, rank_agreement, sem_ordinais)

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
# P-foco: resultado principal só com as ligações diretas; sensibilidade com direta + indireta.
LIGACOES_FOCO = {"direta": ("direta",), "direta + indireta": ("direta", "indireta")}
# Semiquantitativos (ordinais > 50 % do peso): só indicação, à parte dos casos quantitativos.
SEMIQUANTITATIVOS = {"Par articular": "Prótese da anca | Par articular", "Implante dentário": "Implante dentário"}
# Sensibilidade de um valor ordinal: (rótulo, material, critério, valor).
SENSIBILIDADE_VALOR = {"Implante dentário": [("Ti-Zr: corrosão 4", "Ti-Zr (~15% Zr)",
                                              "Resistência à corrosão em meio oral (ordinal 1-5)", 4.0)]}


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
    if codigo == "P-foco":
        return variantes_foco(nome, base, data_dir)
    return []


def variantes_foco(nome: str, base: DecisionProblem, data_dir: Path = DATA) -> list[tuple[str, DecisionProblem]]:
    """Cenário P-foco: o peso dos critérios do problema crítico multiplicado por fator_foco_problema.

    Em linguagem simples: devolve duas versões do problema, uma em que só os critérios com
    ligação direta ao problema do professor ganham peso, e outra em que ganham também os de
    ligação indireta.
    """
    fator = load_parametros(data_dir).get("fator_foco_problema", 2.0)
    return [(rot, com_foco(base, criterios_do_problema(nome, lig, data_dir), fator))
            for rot, lig in LIGACOES_FOCO.items()]


def semiquantitativos_linhas(data_dir: Path = DATA) -> pd.DataFrame:
    """Casos semiquantitativos: posições no cenário A, nas duas versões do P-foco e nas
    sensibilidades de valores (SENSIBILIDADE_VALOR).

    Em linguagem simples: corre os três métodos no par articular e no implante dentário só
    como indicação, porque a maior parte do peso está em escalas ordinais.
    """
    linhas = []
    for caso, nome in SEMIQUANTITATIVOS.items():
        base = build_problem(nome, BASE, data_dir)
        linhas += ranking_linhas(caso, BASE, BASE, base)
        for var, p in variantes_foco(nome, base, data_dir):
            linhas += ranking_linhas(caso, "P-foco", var, p)
        for rot, material, criterio, valor in SENSIBILIDADE_VALOR.get(caso, []):
            linhas += ranking_linhas(caso, "Valor", rot, com_valor(base, material, criterio, valor))
    return pd.DataFrame(linhas)


def semiquantitativos_md(sq: pd.DataFrame) -> list[str]:
    """Secções do resumo com os casos semiquantitativos, assinaladas como tal."""
    L = []
    for caso, g0 in sq.groupby("caso", sort=False):
        L += [f"## {caso} (SEMIQUANTITATIVO: ordinais > 50 % do peso; só indicação)", "",
              "| Cenário | Variante | " + " | ".join(METODOS) + " |", "|---|---|---|---|---|"]
        for (c, v), g in g0.groupby(["cenario", "variante"], sort=False):
            L.append(f"| {c} | {v} | " + " | ".join(vencedores(g[g["metodo"] == m]) for m in METODOS) + " |")
        L.append("")
    return L


def ranking_linhas(caso: str, cenario: str, variante: str, p: DecisionProblem) -> list[dict]:
    linhas = []
    for m in METODOS:
        pos = posicoes(p.X, p.weights, p.types, p.targets, m)
        linhas += [{"caso": caso, "cenario": cenario, "variante": variante, "metodo": m,
                    "material": a, "posicao": int(r)} for a, r in zip(p.alternatives, pos)]
    return linhas


def pontuacao_linhas(data_dir: Path = DATA) -> pd.DataFrame:
    """Pontuações dos três métodos (C, Q, P) e posições nos cenários A e B de cada caso.

    Em linguagem simples: a tabela de rankings só guarda a posição; esta guarda também a
    pontuação, para se ver quando dois materiais ficam quase empatados.
    """
    partes = []
    for caso, nome in CASOS.items():
        for cen in ("A", "B"):
            df = rank_all_methods(build_problem(nome, cen, data_dir))
            partes.append(df.assign(caso=caso, cenario=cen))
    return pd.concat(partes, ignore_index=True)


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
            for a, pct, p2, p3, med in zip(p.alternatives, pct_primeiro(r), pct_posicao(r, 2),
                                           pct_posicao(r, 3), r.mean(axis=0)):
                linhas.append({"caso": caso, "analise": analise, "metodo": m, "material": a,
                               "pct_primeiro": pct, "pct_segundo": p2, "pct_terceiro": p3,
                               "posicao_media": med, "n_iter": n_iter, "seed": seed,
                               "incerteza_valor_unico": incerteza_valor_unico if variar == "propriedades" else 0.0})
    return linhas


def vencedores(g: pd.DataFrame) -> str:
    return " = ".join(sorted(g[g["posicao"] == 1]["material"]))


def resumo_md(rk: pd.DataFrame, mc: pd.DataFrame, sp: pd.DataFrame, cen: pd.DataFrame,
              n_iter: int, seed: int, sq: pd.DataFrame | None = None) -> str:
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
    if sq is not None and not sq.empty:
        L += semiquantitativos_md(sq)
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
    pontuacao_linhas().to_csv(RESULTS / "pontuacoes.csv", index=False)
    sq = semiquantitativos_linhas()
    sq.to_csv(RESULTS / "semiquantitativos.csv", index=False)
    texto = resumo_md(rk, mc, sp, cen, a.n_iter, a.seed, sq)
    (RESULTS / "resumo_robustez.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
