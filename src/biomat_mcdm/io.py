"""Leitura dos dados e construção da matriz de decisão (implementado)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from biomat_mcdm.indices import sigma_y_over_e

DATA = Path(__file__).resolve().parents[2] / "data"

_TYPE_MAP = {"Benefício": "benefit", "Custo": "cost", "Alvo": "target"}
SO_PERMANENTES_EM_A = {"Stent vascular"}  # casos em que o cenário A exclui os bioabsorvíveis


@dataclass
class DecisionProblem:
    """Um problema de decisão pronto para os métodos MCDM."""
    alternatives: list[str]          # m materiais
    criteria: list[str]              # n critérios
    X_min: np.ndarray                # (m, n) limites inferiores
    X_max: np.ndarray                # (m, n) limites superiores
    types: list[str]                 # "benefit" | "cost" | "target"
    targets: list[float | None]      # valor-alvo (só para "target")
    weights: np.ndarray              # (n,) pesos subjetivos propostos

    @property
    def X(self) -> np.ndarray:
        """Matriz com valores típicos (ponto médio)."""
        return (self.X_min + self.X_max) / 2


def load_data(data_dir: Path = DATA) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Lê materiais e critérios; acrescenta os índices derivados (σy/E do stent)."""
    mat = pd.read_csv(data_dir / "materiais.csv")
    crit = pd.read_csv(data_dir / "criterios.csv")
    derivados = sigma_y_over_e(mat)
    if not derivados.empty:
        mat = pd.concat([mat, derivados], ignore_index=True)
    mat["caso_componente"] = mat["caso"]
    anca = mat["caso"] == "Prótese da anca"
    mat.loc[anca & mat["componente"].str.startswith("Haste"), "caso_componente"] = "Prótese da anca | Haste femoral"
    mat.loc[anca & mat["componente"].str.startswith("Par"), "caso_componente"] = "Prótese da anca | Par articular"
    return mat, crit


def load_tissue(data_dir: Path = DATA) -> pd.DataFrame:
    """Propriedades de referência dos tecidos (osso cortical, trabecular, mandibular)."""
    return pd.read_csv(data_dir / "tecido.csv")


def build_problem(case: str, scenario: str = "A", data_dir: Path = DATA) -> DecisionProblem:
    """Constrói o problema para um caso (valor de `caso_componente` em criterios.csv).

    scenario "A": só materiais em uso clínico; "B": inclui investigação e bioabsorvíveis retirados.
    No stent (SO_PERMANENTES_EM_A), o cenário A exclui também os bioabsorvíveis (classe
    "biodegradável"): A = 316L, L605, MP35N, Pt-Cr; B = A + Mg WE43 e PLLA.
    Antes disso aplica a triagem estrita (screening.screen_case): materiais eliminados
    (estatuto "Excluído", regras numéricas como segurança iónica ≥ 2) nunca entram.
    Nota: par articular e implante dentário são SEMIQUANTITATIVOS (ordinais > 50 % do peso);
    o MCDM quantitativo principal é para haste, stent e scaffold.
    Critérios estritos e critérios sem dados para todas as alternativas são ignorados aqui
    (a triagem trata dos estritos; índices derivados como σy/E calculam-se à parte).
    """
    from biomat_mcdm.screening import screen_case  # import local: screening importa io

    mat, crit = load_data(data_dir)
    m = mat[mat["caso_componente"] == case]
    aprovados, _ = screen_case(case, data_dir)  # triagem estrita (ex.: Nitinol, MoM)
    m = m[m["material"].isin(aprovados)]
    if scenario == "A":
        m = m[m["estatuto"].str.startswith("Clínico")
              & ~m["estatuto"].str.contains("abandonado", case=False)]
        if case in SO_PERMANENTES_EM_A:  # stent: bioabsorvíveis só no cenário B
            m = m[~m["classe"].fillna("").str.contains("biodegradável", case=False)]
    c = crit[(crit["caso_componente"] == case) & (crit["tipo"] != "Estrito")].copy()
    c["prop"] = c["criterio"].str.replace(r" \(só cenário B\)", "", regex=True)

    alts = list(dict.fromkeys(m["material"]))
    cols_min, cols_max, keep = [], [], []
    for _, cr in c.iterrows():
        sub = m[m["propriedade"] == cr["prop"]].set_index("material")
        if sub.empty or len(sub) < len(alts) or sub[["min", "max"]].isna().any().any():
            continue
        keep.append(cr)
        cols_min.append(sub.loc[alts, "min"].to_numpy(float))
        cols_max.append(sub.loc[alts, "max"].to_numpy(float))

    w = np.array([float(k["peso"]) for k in keep])
    return DecisionProblem(
        alternatives=alts,
        criteria=[k["prop"] for k in keep],
        X_min=np.array(cols_min).T,
        X_max=np.array(cols_max).T,
        types=[_TYPE_MAP[k["tipo"]] for k in keep],
        targets=[float(k["alvo"]) if k["tipo"] == "Alvo" else None for k in keep],
        weights=w / w.sum(),  # renormaliza se algum critério foi excluído
    )
