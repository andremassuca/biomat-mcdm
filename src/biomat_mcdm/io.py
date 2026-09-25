"""Leitura dos dados e construção da matriz de decisão (implementado)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

_TYPE_MAP = {"Benefício": "benefit", "Custo": "cost", "Alvo": "target"}


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
    mat = pd.read_csv(data_dir / "materiais.csv")
    crit = pd.read_csv(data_dir / "criterios.csv")
    mat["caso_componente"] = mat["caso"]
    anca = mat["caso"] == "Prótese da anca"
    mat.loc[anca & mat["componente"].str.startswith("Haste"), "caso_componente"] = "Prótese da anca | Haste femoral"
    mat.loc[anca & mat["componente"].str.startswith("Par"), "caso_componente"] = "Prótese da anca | Par articular"
    return mat, crit


def build_problem(case: str, scenario: str = "A", data_dir: Path = DATA) -> DecisionProblem:
    """Constrói o problema para um caso (valor de `caso_componente` em criterios.csv).

    scenario "A": só materiais em uso clínico; "B": inclui investigação e bioabsorvíveis retirados.
    Materiais com estatuto "Excluído" nunca entram (ficam só para a discussão).
    Nota: par articular e implante dentário são SEMIQUANTITATIVOS (ordinais > 50 % do peso);
    o MCDM quantitativo principal é para haste, stent e scaffold.
    Critérios estritos e critérios sem dados para todas as alternativas são ignorados aqui
    (a triagem trata dos estritos; índices derivados como σy/E calculam-se à parte).
    """
    mat, crit = load_data(data_dir)
    m = mat[mat["caso_componente"] == case]
    m = m[~m["estatuto"].str.startswith("Excluído")]  # ex.: Nitinol (autoexpansível) nunca entra no ranking
    if scenario == "A":
        m = m[m["estatuto"].str.startswith("Clínico")
              & ~m["estatuto"].str.contains("abandonado", case=False)]
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
