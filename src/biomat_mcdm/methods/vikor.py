"""VIKOR abrangente (secção 2.8 de Petković et al. 2025).

    S_i = Σ w_j (1 - exp(-|x_ij - T_j| / A_j))
    R_i = max_j [ w_j (1 - exp(-|x_ij - T_j| / A_j)) ]
    Q_i combina S e R com v (tipicamente 0.5).  MENOR Q = melhor.

Lê a secção 2.8 do artigo para a definição exata de A_j e de Q_i antes de implementar.
"""
from __future__ import annotations
import numpy as np


def vikor(X: np.ndarray, weights: np.ndarray, types: list[str],
          targets: list[float | None], v: float = 0.5) -> dict[str, np.ndarray]:
    """Devolve {"S": ..., "R": ..., "Q": ...}."""
    raise NotImplementedError
