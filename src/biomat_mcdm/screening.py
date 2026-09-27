"""Fase 1: triagem por critérios estritos (passa/falha), com registo do que foi eliminado e porquê.

Três tipos de regra estrita em data/criterios.csv (tipo "Estrito"):
  - numérica (alvo "≥ 2", "<= 5", ...): avaliada com os dados da base, no pior caso do
    intervalo (mín. para "≥", máx. para "≤"), porque a segurança não é compensável;
  - categórica pelo estatuto: materiais com estatuto "Excluído (...)" na base (ex.: Nitinol,
    autoexpansível) são eliminados, com o estatuto como motivo;
  - qualitativa (alvo em texto, sem dados): não elimina ninguém; fica no registo como
    "não avaliado (avaliação qualitativa no texto)".
Um material sem dados para uma regra numérica não é eliminado: fica "não avaliado (sem dados)".
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from biomat_mcdm.io import DATA, load_data

_OPS = {"≥": ">=", ">=": ">=", "≤": "<=", "<=": "<=", "=": "==", "==": "=="}
_RE_NUM = re.compile(r"^\s*(≥|>=|≤|<=|==|=)\s*(-?\d+(?:[.,]\d+)?)\s*$")
COLUNAS_REGISTO = ["material", "criterio", "regra", "valor", "resultado", "motivo"]


@dataclass(frozen=True)
class StrictRule:
    """Uma regra estrita: critério, texto do alvo e, se for numérica, operador e limite."""
    criterio: str
    alvo: str
    op: str | None = None
    limite: float | None = None

    @property
    def numerica(self) -> bool:
        return self.op is not None


def parse_rule(criterio: str, alvo: str) -> StrictRule:
    """Lê o alvo de uma regra estrita.

    Em linguagem simples: "≥ 2" vira (">=", 2.0); um alvo em texto ("Aprovado",
    "Avaliação qualitativa") fica como regra qualitativa, sem operador.
    """
    m = _RE_NUM.match(str(alvo))
    if not m:
        return StrictRule(criterio, str(alvo))
    return StrictRule(criterio, str(alvo), _OPS[m.group(1)], float(m.group(2).replace(",", ".")))


def _cumpre(valor: float, op: str, limite: float) -> bool:
    return {">=": valor >= limite, "<=": valor <= limite, "==": valor == limite}[op]


def apply_strict(materials: pd.DataFrame, rules: list[StrictRule]) -> tuple[list[str], pd.DataFrame]:
    """Aplica as regras estritas a um caso; devolve (aprovados, registo).

    Em linguagem simples: um material é eliminado se falhar qualquer regra, sem que um bom
    desempenho noutros critérios o possa salvar. O registo diz, para cada material e regra,
    se foi aprovado, eliminado ou não avaliado, e porquê: é a tabela da triagem do relatório.

    `materials` está no formato longo da base (colunas material, estatuto, propriedade,
    min, max), só com o caso em causa.
    """
    materiais = list(dict.fromkeys(materials["material"]))
    estatuto = materials.drop_duplicates("material").set_index("material")["estatuto"]
    linhas, eliminados = [], set()

    for mat in materiais:
        if str(estatuto[mat]).startswith("Excluído"):
            eliminados.add(mat)
            linhas.append([mat, "Estatuto na base", "não 'Excluído'", None, "eliminado", estatuto[mat]])

    for r in rules:
        if not r.numerica:
            for mat in materiais:
                linhas.append([mat, r.criterio, r.alvo, None, "não avaliado",
                               "avaliação qualitativa no texto"])
            continue
        dados = materials[materials["propriedade"] == r.criterio].set_index("material")
        for mat in materiais:
            if mat not in dados.index or dados.loc[mat, ["min", "max"]].isna().all():
                linhas.append([mat, r.criterio, r.alvo, None, "não avaliado", "sem dados na base"])
                continue
            lo, hi = dados.loc[mat, "min"], dados.loc[mat, "max"]
            valor = float(lo if r.op == ">=" else hi if r.op == "<=" else lo)
            if r.op == "==" and lo != hi:
                ok = False
                motivo = f"intervalo {lo:g}-{hi:g} não é igual a {r.limite:g}"
            else:
                ok = _cumpre(valor, r.op, r.limite)
                pior = {">=": "mínimo", "<=": "máximo", "==": "valor"}[r.op]
                motivo = f"{pior} do intervalo = {valor:g}; regra {r.op} {r.limite:g}"
            if not ok:
                eliminados.add(mat)
            linhas.append([mat, r.criterio, r.alvo, valor, "aprovado" if ok else "eliminado", motivo])

    aprovados = [m for m in materiais if m not in eliminados]
    return aprovados, pd.DataFrame(linhas, columns=COLUNAS_REGISTO)


def screen_case(case: str, data_dir: Path = DATA) -> tuple[list[str], pd.DataFrame]:
    """Triagem de um caso (valor de `caso_componente`), com as regras estritas de criterios.csv."""
    mat, crit = load_data(data_dir)
    m = mat[mat["caso_componente"] == case]
    if m.empty:
        raise ValueError(f"caso sem materiais: {case!r}")
    c = crit[(crit["caso_componente"] == case) & (crit["tipo"] == "Estrito")]
    rules = [parse_rule(k, a) for k, a in zip(c["criterio"], c["alvo"])]
    return apply_strict(m, rules)
