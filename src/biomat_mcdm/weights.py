"""Pesos dos critérios: subjetivos, objetivos e combinados (eq. 1 de Petković et al. 2025).

    w_j = η · w_j^S + (1 - η) · w_j^O
"""
from __future__ import annotations
import numpy as np


def std_dev_weights(R: np.ndarray) -> np.ndarray:
    """Pesos objetivos pelo método do desvio-padrão sobre a matriz normalizada R.
    w_j^O = σ_j / Σ σ_k
    """
    raise NotImplementedError


def combine_weights(w_subj: np.ndarray, w_obj: np.ndarray, eta: float) -> np.ndarray:
    """Combinação linear com o nível de confiança η ∈ [0, 1]. Deve somar 1."""
    raise NotImplementedError
