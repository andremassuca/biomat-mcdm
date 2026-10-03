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
# Critérios em que um material sem valor recebe o PIOR valor observado nos outros (opção O2):
# os stents permanentes não reabsorvem; "não reabsorver é pelo menos tão mau como o pior
# bioabsorvível". Limitação: subestima o caso permanente (ver NOTAS_METODOLOGICAS.md).
PIOR_OBSERVADO = {("Stent vascular", "Tempo de reabsorção")}


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
    X_tipico: np.ndarray | None = None  # (m, n) valores típicos da base (None = ponto médio)

    @property
    def X(self) -> np.ndarray:
        """Matriz com os valores usados nos métodos: o típico da base ou, sem ele, o ponto médio."""
        if self.X_tipico is not None:
            return np.asarray(self.X_tipico, float)
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


def load_parametros(data_dir: Path = DATA) -> dict[str, float]:
    """Parâmetros de desenho de data/parametros.csv como {nome: valor} (ex.: eta)."""
    p = pd.read_csv(data_dir / "parametros.csv")
    return {r.parametro: float(r.valor) for r in p.itertuples()}


def load_problemas(data_dir: Path = DATA) -> pd.DataFrame:
    """Mapa problema crítico → critérios (data/problemas_criticos.csv).

    Em linguagem simples: para cada caso, diz que critérios respondem ao problema crítico
    indicado pelo professor e se a ligação é direta ou indireta.
    """
    return pd.read_csv(data_dir / "problemas_criticos.csv")


def criterios_do_problema(case: str, ligacoes: tuple[str, ...] = ("direta",),
                          data_dir: Path = DATA) -> list[str]:
    """Critérios ligados ao problema crítico de um caso, só com as ligações pedidas.

    Devolve o nome da propriedade, como em DecisionProblem.criteria (sem "(só cenário B)").
    """
    m = load_problemas(data_dir)
    m = m[(m["caso_componente"] == case) & m["ligacao"].isin(ligacoes)]
    return list(dict.fromkeys(m["criterio"].str.replace(r" \(só cenário B\)", "", regex=True)))


def _pior_observado(sub: pd.DataFrame, tipo: str, alvo: float | None) -> float:
    """Pior valor observado num critério: o mais afastado do alvo, o maior (custo) ou o menor (benefício)."""
    vals = pd.concat([sub["min"], sub["max"]]).dropna().to_numpy(float)
    if tipo == "Alvo":
        return float(vals[np.argmax(np.abs(vals - alvo))])
    return float(vals.max() if tipo == "Custo" else vals.min())


def build_problem(case: str, scenario: str = "A", data_dir: Path = DATA,
                  valor_em_falta: dict[str, float] | None = None) -> DecisionProblem:
    """Constrói o problema para um caso (valor de `caso_componente` em criterios.csv).

    scenario "A": só materiais em uso clínico; "B": inclui investigação e bioabsorvíveis retirados;
    "B-bio": só os bioabsorvíveis do cenário B (classe "biodegradável"), para comparação.
    Critérios marcados "(só cenário B)" só entram em B e B-bio.
    Critérios em PIOR_OBSERVADO: materiais sem valor recebem o pior valor observado, ou o valor
    dado em `valor_em_falta` ({propriedade: valor}), usado na análise de sensibilidade (O1).
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
    elif scenario == "B-bio":
        m = m[m["classe"].fillna("").str.contains("biodegradável", case=False)]
    elif scenario != "B":
        raise ValueError(f"cenário desconhecido: {scenario!r} (use 'A', 'B' ou 'B-bio')")
    c = crit[(crit["caso_componente"] == case) & (crit["tipo"] != "Estrito")].copy()
    if scenario == "A":
        c = c[~c["criterio"].str.contains(r"\(só cenário B\)", regex=True)]
    c["prop"] = c["criterio"].str.replace(r" \(só cenário B\)", "", regex=True)

    alts = list(dict.fromkeys(m["material"]))
    cols_min, cols_max, cols_tip, keep = [], [], [], []
    for _, cr in c.iterrows():
        sub = m[m["propriedade"] == cr["prop"]].set_index("material")
        sub = sub[sub[["min", "max"]].notna().all(axis=1)]
        sub = sub.assign(tipico=sub["tipico"].fillna((sub["min"] + sub["max"]) / 2))
        fora = sub[(sub["tipico"] < sub["min"] - 1e-9) | (sub["tipico"] > sub["max"] + 1e-9)]
        if not fora.empty:
            raise ValueError(f"típico fora de [mín., máx.] em {cr['prop']!r}: {list(fora.index)}")
        if (case, cr["prop"]) in PIOR_OBSERVADO and not sub.empty and len(sub) < len(alts):
            alvo = float(cr["alvo"]) if cr["tipo"] == "Alvo" else None
            v = (valor_em_falta or {}).get(cr["prop"], _pior_observado(sub, cr["tipo"], alvo))
            falta = pd.DataFrame({"min": v, "max": v, "tipico": v}, index=[a for a in alts if a not in sub.index])
            sub = pd.concat([sub[["min", "max", "tipico"]], falta])
        if sub.empty or len(sub) < len(alts):
            continue
        keep.append(cr)
        cols_min.append(sub.loc[alts, "min"].to_numpy(float))
        cols_max.append(sub.loc[alts, "max"].to_numpy(float))
        cols_tip.append(sub.loc[alts, "tipico"].to_numpy(float))

    w = np.array([float(k["peso"]) for k in keep])
    return DecisionProblem(
        alternatives=alts,
        criteria=[k["prop"] for k in keep],
        X_min=np.array(cols_min).T,
        X_max=np.array(cols_max).T,
        X_tipico=np.array(cols_tip).T,
        types=[_TYPE_MAP[k["tipo"]] for k in keep],
        targets=[float(k["alvo"]) if k["tipo"] == "Alvo" else None for k in keep],
        weights=w / w.sum(),  # renormaliza se algum critério foi excluído
    )
