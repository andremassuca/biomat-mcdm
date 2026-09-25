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
    raise NotImplementedError


def normalize_column(column: np.ndarray, ctype: str, target: float | None = None) -> np.ndarray:
    """Aplica a eq. (2) a uma coluna. Cuidado com o denominador nulo (coluna constante)."""
    raise NotImplementedError


def normalize_matrix(X: np.ndarray, types: list[str], targets: list[float | None]) -> np.ndarray:
    """Normaliza a matriz (m, n) coluna a coluna."""
    raise NotImplementedError
