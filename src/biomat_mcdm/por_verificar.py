"""Valores "A verificar" ordenados pela influência no resultado (tarefa 12).

Para cada célula (material, critério) que ainda está "A verificar", o valor típico varia
±delta (por omissão ±20 %) com tudo o resto fixo; regista-se quanto muda o C do TOPSIS
desse material e se o vencedor do TOPSIS muda. As células com mais influência são as que
vale a pena verificar primeiro.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from biomat_mcdm.io import DATA, DecisionProblem, build_problem, load_data
from biomat_mcdm.methods.topsis import topsis
from biomat_mcdm.robustness import e_ordinal


def por_verificar(estado: str | float) -> bool:
    """True se o estado da base ainda é "A verificar" (inclui "A verificar (derivado)")."""
    return isinstance(estado, str) and estado.startswith("A verificar")


def estados_do_problema(case: str, problem: DecisionProblem, data_dir: Path = DATA) -> dict:
    """{(material, critério): (estado, fonte)} para as células do problema que têm linha na base.

    Em linguagem simples: vai buscar a data/materiais.csv o estado e a referência de cada valor
    usado no problema. Células sem linha ou com linha sem valor numérico (ex.: tempo de
    reabsorção dos stents permanentes, preenchido com o pior valor observado, opção O2) ficam
    de fora: esse valor é uma hipótese de modelação, não um dado a verificar.
    """
    mat, _ = load_data(data_dir)
    m = mat[(mat["caso_componente"] == case) & mat["material"].isin(problem.alternatives)
            & mat["propriedade"].isin(problem.criteria) & mat[["min", "max"]].notna().all(axis=1)]
    return {(r.material, r.propriedade): (r.estado, r.referencia) for r in m.itertuples()}


def influencia_celulas(problem: DecisionProblem, estados: dict, delta: float = 0.2) -> pd.DataFrame:
    """Influência de cada célula "A verificar" no TOPSIS (valor típico ±delta, resto fixo).

    Em linguagem simples: mexe num valor de cada vez e vê quanto o resultado se mexe.
    Colunas: material, criterio, tipo, tipico, estado, fonte, dC_material (maior variação
    absoluta do C do próprio material), dC_max (maior variação do C de qualquer material),
    muda_vencedor (o vencedor do TOPSIS muda em +delta ou -delta), novo_vencedor.
    """
    if not 0 < delta < 1:
        raise ValueError("delta tem de estar em ]0, 1[")
    X = problem.X
    args = (problem.weights, problem.types, problem.targets)
    c0 = topsis(X, *args)
    venc0 = int(np.argmax(c0))
    linhas = []
    for i, a in enumerate(problem.alternatives):
        for j, crit in enumerate(problem.criteria):
            estado, fonte = estados.get((a, crit), (None, None))
            if not por_verificar(estado):
                continue
            dmat, dmax, novo = 0.0, 0.0, None
            for f in (1 - delta, 1 + delta):
                Xv = X.copy()
                Xv[i, j] = X[i, j] * f
                c = topsis(Xv, *args)
                dmat = max(dmat, abs(c[i] - c0[i]))
                dmax = max(dmax, float(np.max(np.abs(c - c0))))
                if int(np.argmax(c)) != venc0 and novo is None:
                    novo = problem.alternatives[int(np.argmax(c))]
            tipo = "ordinal" if e_ordinal(crit) else ("derivado" if "derivado" in str(estado) else "quantitativo")
            linhas.append({"material": a, "criterio": crit, "tipo": tipo, "tipico": X[i, j],
                           "estado": estado, "fonte": fonte, "dC_material": dmat, "dC_max": dmax,
                           "muda_vencedor": novo is not None, "novo_vencedor": novo or ""})
    df = pd.DataFrame(linhas, columns=["material", "criterio", "tipo", "tipico", "estado", "fonte",
                                       "dC_material", "dC_max", "muda_vencedor", "novo_vencedor"])
    return df.sort_values(["muda_vencedor", "dC_material", "dC_max"], ascending=False, ignore_index=True)


def tabela_caso(case: str, cenarios: tuple[str, ...] = ("A", "B"), delta: float = 0.2,
                data_dir: Path = DATA) -> pd.DataFrame:
    """Ponto de entrada por caso: células "A verificar" do cenário A e, dos outros cenários,
    só as que não entram no A. Coluna extra: cenario. Ordem única por caso (influência)."""
    partes, vistas = [], set()
    for cen in cenarios:
        p = build_problem(case, cen, data_dir)
        df = influencia_celulas(p, estados_do_problema(case, p, data_dir), delta)
        df = df[[(r.material, r.criterio) not in vistas for r in df.itertuples()]]
        vistas |= set(zip(df["material"], df["criterio"]))
        partes.append(df.assign(cenario=cen))
    return pd.concat(partes, ignore_index=True).sort_values(
        ["muda_vencedor", "dC_material", "dC_max"], ascending=False, ignore_index=True)


def vencedor_topsis(problem: DecisionProblem) -> str:
    """Material em 1.º lugar no TOPSIS com os valores típicos."""
    return problem.alternatives[int(np.argmax(topsis(problem.X, problem.weights, problem.types,
                                                     problem.targets)))]

