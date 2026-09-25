"""WASPAS estendido (secção 2.7, eqs. 9-16 de Petković et al. 2025).

Nota: o WASPAS estendido usa uma normalização própria (eqs. 9-13), diferente da do TOPSIS.
    Q_i = λ · Σ r_ij w_j + (1 - λ) · Π r_ij^w_j,  com λ = 0.5 por defeito
"""
from __future__ import annotations
import numpy as np


def normalize_waspas(X: np.ndarray, types: list[str], targets: list[float | None]) -> np.ndarray:
    raise NotImplementedError


def waspas(X: np.ndarray, weights: np.ndarray, types: list[str],
           targets: list[float | None], lam: float = 0.5) -> np.ndarray:
    """Devolve Q_i (maior = melhor). Atenção: r_ij = 0 anula o produto (WPM)."""
    raise NotImplementedError
