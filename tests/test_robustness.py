"""Testes de robustness.py."""
import numpy as np
import pytest

from biomat_mcdm.io import DecisionProblem, build_problem
from biomat_mcdm.robustness import (alargar_valores_unicos, com_alvo, com_eta, com_peso, monte_carlo,
                                    pct_primeiro, posicoes, rank_agreement, sample_matrix, sample_weights,
                                    sem_ordinais)


def problema():
    X_min = np.array([[9.0, 1], [4, 2], [1, 3]])
    X_max = np.array([[11.0, 1], [6, 2], [2, 3]])
    return DecisionProblem(["A", "B", "C"], ["c1", "c2 (ordinal 1-5)"], X_min, X_max,
                           ["benefit", "cost"], [None, None], np.array([0.6, 0.4]))


def test_amostra_dentro_do_intervalo_e_fixa_onde_min_igual_max():
    p = problema()
    rng = np.random.default_rng(0)
    for dist in ("uniform", "triangular"):
        X = sample_matrix(p.X_min, p.X_max, rng, dist)
        assert np.all((X >= p.X_min) & (X <= p.X_max))
        assert np.allclose(X[:, 1], [1, 2, 3])


def test_pesos_perturbados_somam_1_e_ficam_perto():
    w = np.array([0.5, 0.3, 0.2])
    s = sample_weights(w, np.random.default_rng(1), spread=0.2)
    assert s.sum() == pytest.approx(1)
    assert np.all(np.abs(s / w - 1) < 0.5)


@pytest.mark.parametrize("metodo", ["TOPSIS", "WASPAS", "VIKOR"])
def test_monte_carlo_forma_reprodutivel_e_dominante_ganha_sempre(metodo):
    p = problema()
    r1 = monte_carlo(p, metodo, n_iter=50, seed=42)
    r2 = monte_carlo(p, metodo, n_iter=50, seed=42)
    assert r1.shape == (50, 3)
    assert np.array_equal(r1, r2)
    assert pct_primeiro(r1)[0] == 100  # A domina em todas as amostras


def test_monte_carlo_nos_pesos():
    r = monte_carlo(problema(), "TOPSIS", n_iter=20, seed=1, variar="pesos")
    assert r.shape == (20, 3)


@pytest.mark.parametrize("kw", [{"n_iter": 0}, {"variar": "outra"}])
def test_monte_carlo_argumentos_invalidos(kw):
    with pytest.raises(ValueError):
        monte_carlo(problema(), "TOPSIS", **{"n_iter": 5, **kw})


def test_metodo_desconhecido_da_erro():
    p = problema()
    with pytest.raises(ValueError):
        posicoes(p.X, p.weights, p.types, p.targets, "AHP")


def test_pct_primeiro_e_spearman():
    r = np.array([[1, 2, 3], [2, 1, 3], [1, 3, 2], [1, 2, 3]])
    assert pct_primeiro(r) == pytest.approx([75, 25, 0])
    assert rank_agreement([1, 2, 3], [1, 2, 3]) == pytest.approx(1)
    assert rank_agreement([1, 2, 3], [3, 2, 1]) == pytest.approx(-1)


def test_sem_ordinais_retira_e_renormaliza():
    q = sem_ordinais(problema())
    assert q.criteria == ["c1"]
    assert q.weights == pytest.approx([1.0])


def test_com_eta_1_mantem_os_pesos_e_0_usa_os_objetivos():
    p = build_problem("Prótese da anca | Haste femoral", "A")
    assert com_eta(p, 1).weights == pytest.approx(p.weights)
    assert not np.allclose(com_eta(p, 0).weights, p.weights)


def test_com_alvo_e_como_custo():
    p = build_problem("Prótese da anca | Haste femoral", "A")
    j = p.criteria.index("Módulo de Young")
    assert com_alvo(p, "Módulo de Young", 14).targets[j] == 14
    c = com_alvo(p, "Módulo de Young", None, "cost")
    assert c.types[j] == "cost" and c.targets[j] is None


def test_com_peso_fixa_e_redistribui():
    p = problema()
    q = com_peso(p, "c1", 0.25)
    assert q.weights == pytest.approx([0.25, 0.75])
    with pytest.raises(ValueError):
        com_peso(p, "c1", 1.0)


def test_alargar_valores_unicos_so_nas_celulas_quantitativas_com_min_igual_max():
    p = problema()  # c1: intervalos 9-11, 4-6, 1-2; c2 ordinal com min = max
    X_min = p.X_min.copy()
    X_min[0, 0] = X_max0 = p.X_max[0, 0]  # A em c1 passa a valor único (11)
    q = alargar_valores_unicos(DecisionProblem(p.alternatives, p.criteria, X_min, p.X_max,
                                               p.types, p.targets, p.weights), 0.10)
    assert q.X_min[0, 0] == pytest.approx(X_max0 * 0.9)
    assert q.X_max[0, 0] == pytest.approx(X_max0 * 1.1)
    assert np.allclose(q.X_min[1:, 0], p.X_min[1:, 0]) and np.allclose(q.X_max[1:, 0], p.X_max[1:, 0])
    assert np.allclose(q.X_min[:, 1], p.X_min[:, 1]) and np.allclose(q.X_max[:, 1], p.X_max[:, 1])
    with pytest.raises(ValueError):
        alargar_valores_unicos(p, 1.0)


def test_monte_carlo_com_incerteza_de_valor_unico_varia_so_nas_propriedades():
    X = np.array([[5.0, 1], [5.2, 2]])  # c1 com valor único e quase empatado
    p = DecisionProblem(["A", "B"], ["c1", "c2 (ordinal 1-5)"], X, X.copy(),
                        ["benefit", "benefit"], [None, None], np.array([0.9, 0.1]))
    fixo = monte_carlo(p, "TOPSIS", n_iter=200, seed=3)
    assert (fixo == fixo[0]).all()  # sem incerteza: sempre o mesmo ranking
    com = monte_carlo(p, "TOPSIS", n_iter=200, seed=3, incerteza_valor_unico=0.10)
    assert 0 < pct_primeiro(com)[0] < 100  # com ±10 % a ordem de A e B passa a mudar
    pesos = monte_carlo(p, "TOPSIS", n_iter=20, seed=3, variar="pesos", incerteza_valor_unico=0.10)
    assert pesos.shape == (20, 2)
