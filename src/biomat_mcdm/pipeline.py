"""Ponto de entrada por caso: corre os três métodos sobre um problema de decisão.

Serve os scripts (resultados preliminares, futuro scripts/run_all.py) e a futura app.
Funções puras: recebem dados, devolvem tabelas; não escrevem ficheiros.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from biomat_mcdm.io import DecisionProblem
from biomat_mcdm.methods.topsis import rank, topsis
from biomat_mcdm.methods.vikor import vikor
from biomat_mcdm.methods.waspas import waspas

METODOS = ["TOPSIS", "WASPAS", "VIKOR"]


def rank_all_methods(problem: DecisionProblem, weights: np.ndarray | None = None) -> pd.DataFrame:
    """Devolve uma tabela com a pontuação e a posição de cada material nos três métodos.

    Em linguagem simples: aplica TOPSIS (C, maior = melhor), WASPAS (Q, maior = melhor) e
    VIKOR (P, menor = melhor) aos mesmos dados e pesos, e põe os resultados lado a lado.
    Sem `weights`, usa os pesos do problema (η = 1, só subjetivos).
    Colunas: material, C_TOPSIS, Q_WASPAS, P_VIKOR, pos_TOPSIS, pos_WASPAS, pos_VIKOR.
    """
    w = problem.weights if weights is None else np.asarray(weights, float)
    X, t, a = problem.X, problem.types, problem.targets
    C = topsis(X, w, t, a)
    Q = waspas(X, w, t, a)
    P = vikor(X, w, t, a)["P"]
    return pd.DataFrame({
        "material": problem.alternatives,
        "C_TOPSIS": C, "Q_WASPAS": Q, "P_VIKOR": P,
        "pos_TOPSIS": rank(C), "pos_WASPAS": rank(Q), "pos_VIKOR": rank(P, higher_is_better=False),
    })


def spearman_methods(df: pd.DataFrame) -> pd.DataFrame:
    """Matriz 3 x 3 da correlação de Spearman entre as posições dos três métodos.

    Em linguagem simples: 1 quer dizer que dois métodos ordenam os materiais exatamente da
    mesma forma; valores mais baixos querem dizer mais desacordo.
    """
    pos = df[[f"pos_{m}" for m in METODOS]].to_numpy()
    rho = np.ones((3, 3))
    for i in range(3):
        for j in range(i + 1, 3):
            rho[i, j] = rho[j, i] = spearmanr(pos[:, i], pos[:, j])[0]
    return pd.DataFrame(rho, index=METODOS, columns=METODOS)


def fmt_pt(x: float, casas: int = 3) -> str:
    """Número com vírgula decimal (português), ex.: fmt_pt(0.2) -> '0,200'."""
    return f"{x:.{casas}f}".replace(".", ",")
