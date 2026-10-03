"""Análise de robustez: Monte Carlo (propriedades e pesos), variantes de cenário e
concordância entre métodos.

Tudo aqui são funções puras sobre um DecisionProblem; scripts/run_all.py junta-as para os
cenários de data/cenarios.csv. O número de iterações do Monte Carlo é um parâmetro (10 000
para os resultados; menos para a app).
"""
from __future__ import annotations

from dataclasses import replace

import numpy as np
from scipy.stats import spearmanr

from biomat_mcdm.io import DecisionProblem
from biomat_mcdm.methods.topsis import rank, topsis
from biomat_mcdm.methods.vikor import vikor
from biomat_mcdm.methods.waspas import waspas
from biomat_mcdm.weights import combine_weights, std_dev_weights


def posicoes(X: np.ndarray, w: np.ndarray, types: list[str], targets: list[float | None],
             metodo: str) -> np.ndarray:
    """Posições (1 = melhor) de cada material com um método ("TOPSIS", "WASPAS" ou "VIKOR")."""
    if metodo == "TOPSIS":
        return rank(topsis(X, w, types, targets))
    if metodo == "WASPAS":
        return rank(waspas(X, w, types, targets))
    if metodo == "VIKOR":
        return rank(vikor(X, w, types, targets)["P"], higher_is_better=False)
    raise ValueError(f"método desconhecido: {metodo!r}")


def sample_matrix(X_min: np.ndarray, X_max: np.ndarray, rng: np.random.Generator,
                  dist: str = "uniform") -> np.ndarray:
    """Uma matriz de decisão sorteada dentro de [X_min, X_max].

    Em linguagem simples: cada propriedade de cada material toma um valor ao acaso dentro do
    seu intervalo da base ("uniform": todos os valores igualmente prováveis; "triangular":
    mais provável perto do ponto médio). Onde mín = máx o valor fica fixo.
    """
    X_min, X_max = np.asarray(X_min, float), np.asarray(X_max, float)
    if dist == "uniform":
        return rng.uniform(X_min, X_max)
    if dist == "triangular":
        largura = X_max - X_min
        u = rng.triangular(0.0, 0.5, 1.0, size=X_min.shape)
        return X_min + u * largura
    raise ValueError(f"distribuição desconhecida: {dist!r}")


def sample_weights(w: np.ndarray, rng: np.random.Generator, spread: float = 0.2) -> np.ndarray:
    """Pesos perturbados: cada peso multiplicado por um fator ao acaso em [1 - spread, 1 + spread],
    depois renormalizados para somar 1."""
    w = np.asarray(w, float)
    p = w * rng.uniform(1 - spread, 1 + spread, size=w.shape)
    return p / p.sum()


def e_ordinal(criterio: str) -> bool:
    """True para os critérios ordinais (escalas 1-5 definidas no trabalho)."""
    return "ordinal" in criterio or "(1-5" in criterio


def alargar_valores_unicos(problem: DecisionProblem, incerteza: float) -> DecisionProblem:
    """Dá um intervalo ±incerteza à volta do típico às células quantitativas com mín. = máx.

    Em linguagem simples: um valor de um único estudo não tem incerteza zero; aqui passa a
    variar, por exemplo, ±10 % (incerteza = 0,10) no Monte Carlo. Os critérios ordinais e as
    células que já têm intervalo ficam como estão.
    """
    if not 0 <= incerteza < 1:
        raise ValueError("incerteza tem de estar em [0, 1)")
    X_min, X_max = np.asarray(problem.X_min, float), np.asarray(problem.X_max, float)
    quantitativo = np.array([not e_ordinal(c) for c in problem.criteria])
    unico = np.isclose(X_min, X_max) & quantitativo[None, :]
    lo, hi = X_min * (1 - incerteza), X_max * (1 + incerteza)
    return replace(problem, X_min=np.where(unico, np.minimum(lo, hi), X_min),
                   X_max=np.where(unico, np.maximum(lo, hi), X_max))


def monte_carlo(problem: DecisionProblem, metodo: str, n_iter: int = 10_000, seed: int = 42,
                variar: str = "propriedades", dist: str = "uniform", spread: float = 0.2,
                incerteza_valor_unico: float = 0.0) -> np.ndarray:
    """Corre o método n_iter vezes; devolve a matriz (n_iter, m) de posições.

    Em linguagem simples: repete o ranking muitas vezes, cada vez com valores sorteados
    ("propriedades": dentro dos intervalos da base; "pesos": pesos perturbados ±spread).
    Com incerteza_valor_unico > 0, as propriedades quantitativas com mín. = máx. variam
    ±incerteza_valor_unico à volta do típico (só em "propriedades").
    A mesma seed dá os mesmos sorteios para os três métodos, para os comparar em igualdade.
    """
    if n_iter < 1:
        raise ValueError("n_iter tem de ser ≥ 1")
    if variar == "propriedades" and incerteza_valor_unico:
        problem = alargar_valores_unicos(problem, incerteza_valor_unico)
    rng = np.random.default_rng(seed)
    out = np.empty((n_iter, len(problem.alternatives)), dtype=int)
    for k in range(n_iter):
        if variar == "propriedades":
            X, w = sample_matrix(problem.X_min, problem.X_max, rng, dist), problem.weights
        elif variar == "pesos":
            X, w = problem.X, sample_weights(problem.weights, rng, spread)
        else:
            raise ValueError(f"variar tem de ser 'propriedades' ou 'pesos', não {variar!r}")
        out[k] = posicoes(X, w, problem.types, problem.targets, metodo)
    return out


def pct_primeiro(ranks: np.ndarray) -> np.ndarray:
    """% de iterações em que cada material fica em 1.º lugar (empates contam para todos)."""
    return 100 * (np.asarray(ranks) == 1).mean(axis=0)


def pct_posicao(ranks: np.ndarray, k: int) -> np.ndarray:
    """% de iterações em que cada material fica na posição k (1 = melhor).

    Em linguagem simples: conta em quantas das simulações cada material ficou em k.º lugar
    e passa a contagem a percentagem. Com k = 1 dá o mesmo que pct_primeiro.
    """
    return 100 * (np.asarray(ranks) == k).mean(axis=0)


def rank_agreement(rank_a: np.ndarray, rank_b: np.ndarray) -> float:
    """Correlação de Spearman entre dois rankings (1 = mesma ordem)."""
    return float(spearmanr(rank_a, rank_b)[0])


# ---------- variantes de cenário (cada uma devolve problemas modificados) ----------

def sem_ordinais(problem: DecisionProblem) -> DecisionProblem:
    """Cenário Q: retira os critérios ordinais (1-5) e renormaliza os pesos."""
    keep = [j for j, c in enumerate(problem.criteria) if not e_ordinal(c)]
    return _subconjunto(problem, keep)


def _subconjunto(problem: DecisionProblem, keep: list[int]) -> DecisionProblem:
    w = problem.weights[keep]
    return replace(problem, criteria=[problem.criteria[j] for j in keep],
                   X_min=problem.X_min[:, keep], X_max=problem.X_max[:, keep],
                   X_tipico=None if problem.X_tipico is None else problem.X_tipico[:, keep],
                   types=[problem.types[j] for j in keep], targets=[problem.targets[j] for j in keep],
                   weights=w / w.sum())


def com_eta(problem: DecisionProblem, eta: float) -> DecisionProblem:
    """Cenário η: pesos combinados (eq. 1) com os pesos objetivos do desvio-padrão."""
    w_obj = std_dev_weights(problem.X, problem.types)
    return replace(problem, weights=combine_weights(problem.weights, w_obj, eta))


def com_alvo(problem: DecisionProblem, criterio: str, alvo: float | None,
             tipo: str = "target") -> DecisionProblem:
    """Cenários T: muda o alvo (ou o tipo, ex.: "cost") de um critério."""
    j = problem.criteria.index(criterio)
    types, targets = list(problem.types), list(problem.targets)
    types[j], targets[j] = tipo, (alvo if tipo == "target" else None)
    return replace(problem, types=types, targets=targets)


def com_peso(problem: DecisionProblem, criterio: str, peso: float) -> DecisionProblem:
    """Fixa o peso de um critério e redistribui o resto proporcionalmente (soma 1)."""
    if not 0 <= peso < 1:
        raise ValueError("peso tem de estar em [0, 1)")
    j = problem.criteria.index(criterio)
    w = problem.weights.copy()
    resto = np.delete(w, j)
    w = np.insert(resto / resto.sum() * (1 - peso), j, peso)
    return replace(problem, weights=w)


def com_foco(problem: DecisionProblem, criterios: list[str], fator: float = 2.0) -> DecisionProblem:
    """Cenário P-foco: multiplica por `fator` o peso dos critérios dados e renormaliza (soma 1).

    Em linguagem simples: dá mais importância aos critérios ligados ao problema crítico do
    dispositivo; os outros critérios perdem peso na mesma proporção. Critérios da lista que
    não existem no problema (ex.: só entram no cenário B) são ignorados.
    """
    if fator <= 0:
        raise ValueError("fator tem de ser positivo")
    idx = [j for j, c in enumerate(problem.criteria) if c in set(criterios)]
    if not idx:
        raise ValueError("nenhum dos critérios do foco existe no problema")
    w = problem.weights.copy()
    w[idx] *= fator
    return replace(problem, weights=w / w.sum())


def com_valor(problem: DecisionProblem, material: str, criterio: str, valor: float) -> DecisionProblem:
    """Sensibilidade de um valor: fixa o valor de um material num critério (mín. = máx. = típico).

    Em linguagem simples: troca uma nota ou um valor da matriz para ver se o resultado muda,
    sem mexer nos dados da base.
    """
    i, j = problem.alternatives.index(material), problem.criteria.index(criterio)
    X_min, X_max = problem.X_min.copy(), problem.X_max.copy()
    X_min[i, j] = X_max[i, j] = valor
    X_tip = None
    if problem.X_tipico is not None:
        X_tip = problem.X_tipico.copy()
        X_tip[i, j] = valor
    return replace(problem, X_min=X_min, X_max=X_max, X_tipico=X_tip)


def com_teto(problem: DecisionProblem, criterio: str, teto: float) -> tuple[DecisionProblem, list[str]]:
    """Cenário O-orçamento: exclui os materiais com valor acima de `teto` num critério (triagem).

    Em linguagem simples: tira da comparação os materiais demasiado caros, sem mexer nos pesos;
    os restantes são ordenados de novo. Devolve o problema reduzido e a lista dos excluídos.
    """
    j = problem.criteria.index(criterio)
    ficam = [i for i in range(len(problem.alternatives)) if problem.X[i, j] <= teto]
    if len(ficam) < 2:
        raise ValueError("o teto deixa menos de dois materiais")
    sai = [a for i, a in enumerate(problem.alternatives) if i not in ficam]
    return replace(problem, alternatives=[problem.alternatives[i] for i in ficam],
                   X_min=problem.X_min[ficam], X_max=problem.X_max[ficam],
                   X_tipico=None if problem.X_tipico is None else problem.X_tipico[ficam]), sai
