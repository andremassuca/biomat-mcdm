"""TOPSIS estendido (critérios-alvo) — passos 1-8 da secção 2.6 de Petković et al. 2025."""
from __future__ import annotations
import numpy as np


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
    raise NotImplementedError


def rank(scores: np.ndarray, higher_is_better: bool = True) -> np.ndarray:
    """Converte pontuações em posições (1 = melhor)."""
    raise NotImplementedError
