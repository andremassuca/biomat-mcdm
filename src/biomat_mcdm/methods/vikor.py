"""VIKOR abrangente com critérios-alvo (secção 2.8, eqs. 17-20 de Petković et al. 2025).

    S_i = Σ_j w_j (1 - exp(-|x_ij - T_j| / A_j))              (17)
    R_i = max_j w_j (1 - exp(-|x_ij - T_j| / A_j))            (18)
    A_j = max{x_j^max, T_j} - min{x_j^min, T_j}
    P_i: eq. 19 (menor P = melhor)

O artigo diz A_j = 1 "para valores normalizados"; como os dados entram em bruto, usa-se
sempre o intervalo. Esta escolha reproduz os 15 P_i publicados dos casos 1 e 2.
"""
from __future__ import annotations
import numpy as np

from biomat_mcdm.normalization import reference_value


def vikor(X: np.ndarray, weights: np.ndarray, types: list[str],
          targets: list[float | None], v: float = 0.5) -> dict[str, np.ndarray]:
    """Devolve {"S": ..., "R": ..., "P": ...}; menor é melhor nos três.

    Em linguagem simples: para cada material mede-se a distância ao valor ideal (T) em cada
    critério, numa escala de 0 a 1 que cresce depressa ao início (exponencial).
      - S soma essas distâncias pesadas (desempenho do conjunto, "maioria dos critérios");
      - R guarda só a pior (o "arrependimento" individual);
      - P mistura S e R, cada um posto entre 0 e 1, na proporção v : (1 - v) (eq. 19).
    O artigo usa v = 0,5.
    """
    if not 0 <= v <= 1:
        raise ValueError("v tem de estar entre 0 e 1")
    X = np.asarray(X, float)
    w = np.asarray(weights, float)
    T = np.array([reference_value(X[:, j], t, targets[j]) for j, t in enumerate(types)])
    A = np.maximum(X.max(axis=0), T) - np.minimum(X.min(axis=0), T)
    A = np.where(A == 0, 1.0, A)  # coluna constante e igual a T: distância 0 em todas
    E = w * (1 - np.exp(-np.abs(X - T) / A))
    S = E.sum(axis=1)                                         # eq. 17
    R = E.max(axis=1)                                         # eq. 18
    s_min, s_max, r_min, r_max = S.min(), S.max(), R.min(), R.max()
    s_const, r_const = np.isclose(s_max, s_min), np.isclose(r_max, r_min)
    if s_const and r_const:
        P = np.zeros_like(S)
    elif s_const:
        P = (R - r_min) / (r_max - r_min)                     # eq. 19, 1.º ramo
    elif r_const:
        P = (S - s_min) / (s_max - s_min)                     # eq. 19, 2.º ramo
    else:
        P = (S - s_min) / (s_max - s_min) * v + (R - r_min) / (r_max - r_min) * (1 - v)
    return {"S": S, "R": R, "P": P}


def compromise_set(S: np.ndarray, R: np.ndarray, P: np.ndarray) -> list[int]:
    """Solução de compromisso (passo 6, eq. 20): índices das alternativas propostas.

    Em linguagem simples: o 1.º por P só é proposto sozinho se tiver vantagem suficiente
    sobre o 2.º (C1: diferença em P ≥ 1/(m - 1)) e se também for o melhor em S ou em R (C2).
      - C1 e C2 cumpridas: só o 1.º;
      - só C2 falha: o 1.º e o 2.º;
      - C1 falha: todos os que ficam a menos de 1/(m - 1) do 1.º em P.
    """
    P = np.asarray(P, float)
    m = len(P)
    if m < 2:
        return [0] * m
    ordem = np.argsort(P, kind="stable")
    a1, a2 = int(ordem[0]), int(ordem[1])
    limiar = 1 / (m - 1)
    c1 = P[a2] - P[a1] >= limiar
    c2 = S[a1] == np.min(S) or R[a1] == np.min(R)
    if c1 and c2:
        return [a1]
    if c1:
        return [a1, a2]
    return [int(i) for i in ordem if P[i] - P[a1] < limiar]
