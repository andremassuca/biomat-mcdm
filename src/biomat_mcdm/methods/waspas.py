"""WASPAS estendido com critérios-alvo (secção 2.7, eqs. 9-16 de Petković et al. 2025).

O WASPAS usa uma normalização própria (eqs. 9-13), diferente da do TOPSIS (eq. 2).
Caso de fronteira que o artigo não escreve: quando o alvo coincide com o máximo da coluna
usa-se a eq. 9 (como benefício) e quando coincide com o mínimo a eq. 10 (como custo).
Esta regra reproduz os 15 Q_i publicados dos casos de estudo 1 e 2 (diferença < 1e-5);
ver tests/test_reproduce_petkovic.py.
"""
from __future__ import annotations
import numpy as np

from biomat_mcdm.normalization import reference_value


def normalize_waspas(X: np.ndarray, types: list[str], targets: list[float | None]) -> np.ndarray:
    """Normaliza a matriz (m, n) com as eqs. 9-13; r_ij ∈ [0, 1], 1 = melhor.

    Em linguagem simples: cada coluna é posta numa escala de 0 a 1.
      - benefício (eq. 9):          r = x / máx
      - custo (eq. 10):             r = mín / x
      - alvo abaixo de todos (11):  r = 1 - (x - T) / máx
      - alvo acima de todos (12):   r = 1 - (T - x) / T
      - alvo no meio (13):          r = 1 - |x - T| / (máx - mín)
      - alvo igual ao máx. ou ao mín.: como benefício ou custo (ver docstring do módulo).
    """
    X = np.asarray(X, float)
    R = np.empty_like(X)
    for j, t in enumerate(types):
        x = X[:, j]
        lo, hi = x.min(), x.max()
        T = reference_value(x, t, targets[j])
        if t == "benefit" or (t == "target" and T == hi):
            R[:, j] = x / hi                                  # eq. 9
        elif t == "cost" or (t == "target" and T == lo):
            R[:, j] = lo / x                                  # eq. 10
        elif T < lo:
            R[:, j] = 1 - (x - T) / hi                        # eq. 11
        elif T > hi:
            R[:, j] = 1 - (T - x) / T                         # eq. 12
        else:
            R[:, j] = 1 - np.abs(x - T) / (hi - lo)           # eq. 13
    return R


def waspas(X: np.ndarray, weights: np.ndarray, types: list[str],
           targets: list[float | None], lam: float = 0.5) -> np.ndarray:
    """Devolve Q_i (eq. 16); maior Q = melhor.

    Em linguagem simples: junta duas formas de somar o desempenho de cada material, a soma
    pesada (eq. 14, WSM) e o produto pesado (eq. 15, WPM), na proporção λ : (1 - λ).
    O artigo usa λ = 0,5. Atenção: um r_ij = 0 anula o produto.
    """
    if not 0 <= lam <= 1:
        raise ValueError("λ tem de estar entre 0 e 1")
    R = normalize_waspas(X, types, targets)
    w = np.asarray(weights, float)
    q1 = (R * w).sum(axis=1)                                  # eq. 14
    q2 = np.prod(R ** w, axis=1)                              # eq. 15
    return lam * q1 + (1 - lam) * q2                          # eq. 16
