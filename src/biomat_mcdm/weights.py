"""Pesos dos critérios: subjetivos, objetivos e combinados (eq. 1 de Petković et al. 2025).

    w_j = η · w_j^S + (1 - η) · w_j^O

Os pesos objetivos vêm do método do desvio-padrão (secção 2.4). O artigo não diz sobre que
matriz se calcula o desvio-padrão; a normalização usada aqui foi reconstituída a partir dos
pesos publicados para η = 0,7; 0,8; 0,9 nos casos de estudo 1 (Tabela A2) e 2 (Tabela A3),
que reproduz com diferença máxima de 0,0005 (arredondamento a 3 casas):
    benefício e alvo:  x_ij / max_i x_ij
    custo:             min_i x_ij / x_ij
Ver tests/test_reproduce_petkovic.py.
"""
from __future__ import annotations
import numpy as np


def std_dev_weights(X: np.ndarray, types: list[str]) -> np.ndarray:
    """Pesos objetivos pelo método do desvio-padrão.

    Em linguagem simples: um critério em que os materiais são muito diferentes entre si
    ajuda mais a distingui-los, por isso recebe mais peso. Cada coluna é primeiro posta na
    mesma escala (dividida pelo máximo; nos critérios de custo, o mínimo dividido pelo
    valor), depois mede-se a dispersão (desvio-padrão) e os pesos são as dispersões
    divididas pela sua soma.

        w_j^O = σ_j / Σ_k σ_k

    Uma coluna com todos os valores iguais recebe peso 0.
    """
    X = np.asarray(X, float)
    if X.ndim != 2 or X.shape[1] != len(types):
        raise ValueError("X tem de ser (m, n) com um tipo por coluna")
    if np.any(X <= 0):
        raise ValueError("o método do desvio-padrão usado aqui exige valores positivos")
    cols = []
    for j, t in enumerate(types):
        x = X[:, j]
        if t in ("benefit", "target"):
            cols.append(x / x.max())
        elif t == "cost":
            cols.append(x.min() / x)
        else:
            raise ValueError(f"tipo de critério desconhecido: {t!r}")
    sigma = np.column_stack(cols).std(axis=0)  # ddof não importa: os pesos são normalizados
    if sigma.sum() == 0:
        raise ValueError("todas as colunas são constantes: pesos objetivos indefinidos")
    return sigma / sigma.sum()


def combine_weights(w_subj: np.ndarray, w_obj: np.ndarray, eta: float) -> np.ndarray:
    """Combinação linear com o nível de confiança η ∈ [0, 1] (eq. 1).

    Em linguagem simples: η diz quanto confiamos nos pesos que o decisor escolheu.
    η = 1 usa só os pesos subjetivos; η = 0 usa só os objetivos; valores intermédios
    misturam os dois na proporção η : (1 - η). Se os dois vetores somam 1, o resultado
    também soma 1.
    """
    if not 0 <= eta <= 1:
        raise ValueError("η tem de estar entre 0 e 1")
    w_subj = np.asarray(w_subj, float)
    w_obj = np.asarray(w_obj, float)
    if w_subj.shape != w_obj.shape:
        raise ValueError("os dois vetores de pesos têm de ter o mesmo tamanho")
    for nome, w in (("subjetivos", w_subj), ("objetivos", w_obj)):
        if np.any(w < 0) or abs(w.sum() - 1) > 1e-3:
            raise ValueError(f"os pesos {nome} têm de ser ≥ 0 e somar 1")
    return eta * w_subj + (1 - eta) * w_obj
