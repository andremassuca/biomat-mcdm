"""TOPSIS estendido (critérios-alvo): passos 1-8 da secção 2.6 de Petković et al. 2025."""
from __future__ import annotations
import numpy as np
from scipy.stats import rankdata

from biomat_mcdm.normalization import normalize_matrix


def topsis(X: np.ndarray, weights: np.ndarray, types: list[str],
           targets: list[float | None]) -> np.ndarray:
    """Devolve C_i (proximidade relativa à solução ideal), um valor por alternativa.

    Passos:
      1. R = normalize_matrix(X, types, targets)
      2-3. V = R * w
      4-5. V+ = max por coluna, V- = min por coluna
      6. D+ e D- (distâncias euclidianas)
      7. C = D- / (D+ + D-)
    Maior C = melhor.
    """
    R = normalize_matrix(X, types, targets)
    V = R * np.asarray(weights, float)
    v_pos = V.max(axis=0)
    v_neg = V.min(axis=0)
    d_pos = np.sqrt(((V - v_pos) ** 2).sum(axis=1))
    d_neg = np.sqrt(((V - v_neg) ** 2).sum(axis=1))
    return d_neg / (d_pos + d_neg)


def rank(scores: np.ndarray, higher_is_better: bool = True) -> np.ndarray:
    """Converte pontuações em posições (1 = melhor). Empates ficam com a mesma posição."""
    s = np.asarray(scores, float)
    return rankdata(-s if higher_is_better else s, method="min").astype(int)
