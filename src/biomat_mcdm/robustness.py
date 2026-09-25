"""Análise de robustez: Monte Carlo sobre propriedades e pesos + concordância entre métodos."""
from __future__ import annotations
import numpy as np


def sample_matrix(X_min: np.ndarray, X_max: np.ndarray, rng: np.random.Generator,
                  dist: str = "uniform") -> np.ndarray:
    """Amostra uma matriz de decisão dentro de [X_min, X_max] ("uniform" ou "triangular")."""
    raise NotImplementedError


def sample_weights(w: np.ndarray, rng: np.random.Generator, spread: float = 0.2) -> np.ndarray:
    """Perturba os pesos (ex.: ±20 %, ou Dirichlet centrada em w) e renormaliza."""
    raise NotImplementedError


def monte_carlo(problem, method, n_iter: int = 10_000, seed: int = 42) -> np.ndarray:
    """Corre o método n_iter vezes. Devolve matriz (n_iter, m) de posições.
    Métrica principal para o poster: % de iterações em que cada material fica em 1.º lugar.
    """
    raise NotImplementedError


def rank_agreement(rank_a: np.ndarray, rank_b: np.ndarray) -> float:
    """Correlação de Spearman entre dois rankings (scipy.stats.spearmanr)."""
    raise NotImplementedError
