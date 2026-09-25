"""Normalização linear com critérios benefício, custo e alvo.

Referência: Jahan et al. (TOPSIS com critérios-alvo), eq. (2) em Petković et al. 2025:

    r_ij = 1 - |x_ij - T_j| / ( max(x_j^max, T_j) - min(x_j^min, T_j) )

onde T_j é:
    - max_i x_ij   para critérios de benefício
    - min_i x_ij   para critérios de custo
    - o valor-alvo para critérios-alvo

Resultado: r_ij ∈ [0, 1], com 1 = melhor desempenho no critério j.
"""
from __future__ import annotations
import numpy as np


def reference_value(column: np.ndarray, ctype: str, target: float | None = None) -> float:
    """Devolve T_j para uma coluna, consoante o tipo ("benefit", "cost", "target")."""
    if ctype == "benefit":
        return float(np.max(column))
    if ctype == "cost":
        return float(np.min(column))
    if ctype == "target":
        if target is None:
            raise ValueError("critério-alvo sem valor-alvo")
        return float(target)
    raise ValueError(f"tipo de critério desconhecido: {ctype!r}")


def normalize_column(column: np.ndarray, ctype: str, target: float | None = None) -> np.ndarray:
    """Aplica a eq. (2) a uma coluna. Cuidado com o denominador nulo (coluna constante)."""
    x = np.asarray(column, float)
    T = reference_value(x, ctype, target)
    # O intervalo inclui o próprio T, por isso |x - T| nunca excede o denominador e r fica em [0, 1].
    denom = max(x.max(), T) - min(x.min(), T)
    if denom == 0:
        # Coluna constante e igual a T: todas as alternativas estão no ótimo.
        return np.ones_like(x)
    return 1 - np.abs(x - T) / denom


def normalize_matrix(X: np.ndarray, types: list[str], targets: list[float | None]) -> np.ndarray:
    """Normaliza a matriz (m, n) coluna a coluna."""
    X = np.asarray(X, float)
    return np.column_stack([normalize_column(X[:, j], types[j], targets[j])
                            for j in range(X.shape[1])])
