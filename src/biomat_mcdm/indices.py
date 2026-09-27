"""Índices derivados de propriedades da base (folha Indices do .xlsx).

- σy/E do stent: proxy ao nível do material da deformação elástica na cedência. Em stents
  expansíveis por balão, maior σy/E = mais recuo elástico, por isso é critério de CUSTO.
  Não é o recuo do dispositivo (depende da geometria, dos struts e do processamento).
- E_implante/E_osso da haste: indicador exploratório de stress shielding (1 = igual ao osso
  cortical). Não entra como critério: o módulo já é critério-alvo; serve para tabelas e texto.

Intervalos: o mínimo do índice combina o mínimo do numerador com o máximo do denominador e
vice-versa, para o Monte Carlo cobrir toda a incerteza dos dois valores.
"""
from __future__ import annotations

import pandas as pd

SIGMA_E = "Índice material de recuo elástico σy/E (proxy)"
CASO_STENT = "Stent vascular"


def _intervalo(df: pd.DataFrame, material: str, propriedade: str) -> tuple[float, float] | None:
    s = df[(df["material"] == material) & (df["propriedade"] == propriedade)]
    if s.empty or s[["min", "max"]].isna().any().any():
        return None
    return float(s["min"].iloc[0]), float(s["max"].iloc[0])


def sigma_y_over_e(materials: pd.DataFrame) -> pd.DataFrame:
    """Linhas novas (formato longo da base) com σy/E de cada material do stent.

    Em linguagem simples: divide a tensão de cedência (MPa) pelo módulo de Young (GPa x 1000,
    para ficar nas mesmas unidades); o resultado não tem unidades e é da ordem de 10^-3.
    Um material a que falte um dos dois valores não recebe índice.
    """
    stent = materials[materials["caso"] == CASO_STENT]
    linhas = []
    for mat, grupo in stent.groupby("material", sort=False):
        sy = _intervalo(grupo, mat, "Tensão de cedência")
        e = _intervalo(grupo, mat, "Módulo de Young")
        if sy is None or e is None:
            continue
        base = grupo.iloc[0]
        lo, hi = sy[0] / (e[1] * 1000), sy[1] / (e[0] * 1000)
        linhas.append({
            **{k: base[k] for k in ("caso", "componente", "material", "norma", "classe", "estatuto")},
            "propriedade": SIGMA_E, "unidade": "-", "min": lo, "max": hi, "tipico": (lo + hi) / 2,
            "referencia": "Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py)",
            "notas": "Proxy ao nível do material; maior = mais recuo elástico",
            "estado": "A verificar (derivado)",
        })
    return pd.DataFrame(linhas, columns=materials.columns)


def stiffness_ratio(materials: pd.DataFrame, tissue: pd.DataFrame, case: str = "Prótese da anca",
                    component_prefix: str = "Haste", tecido: str = "Osso cortical") -> pd.DataFrame:
    """Tabela E_implante/E_osso por material (indicador de stress shielding; 1 = igual ao osso).

    Em linguagem simples: quantas vezes o implante é mais rígido do que o osso. Colunas:
    material, E_min, E_max (GPa), razao_min, razao_tipica, razao_max.
    """
    osso = tissue[(tissue["tecido"] == tecido) & (tissue["propriedade"] == "Módulo de Young")]
    if osso.empty:
        raise ValueError(f"sem módulo de Young para {tecido!r} em tecido.csv")
    if osso["unidade"].iloc[0] != "GPa":
        raise ValueError("o módulo do osso tem de estar em GPa")
    eo_lo, eo_hi = float(osso["min"].iloc[0]), float(osso["max"].iloc[0])
    sel = materials[(materials["caso"] == case)
                    & materials["componente"].fillna("").str.startswith(component_prefix)
                    & (materials["propriedade"] == "Módulo de Young")]
    linhas = []
    for r in sel.itertuples():
        linhas.append({"material": r.material, "E_min": r.min, "E_max": r.max,
                       "razao_min": r.min / eo_hi,
                       "razao_tipica": ((r.min + r.max) / 2) / ((eo_lo + eo_hi) / 2),
                       "razao_max": r.max / eo_lo})
    return pd.DataFrame(linhas)
