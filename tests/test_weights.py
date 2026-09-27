"""Testes unitários de weights.py (a reprodução dos pesos publicados está em
test_reproduce_petkovic.py)."""
import numpy as np
import pytest

from biomat_mcdm.weights import combine_weights, std_dev_weights


def test_pesos_objetivos_somam_1_e_sao_positivos():
    X = np.array([[1.0, 10, 5], [2, 20, 5.5], [4, 15, 6]])
    w = std_dev_weights(X, ["benefit", "cost", "target"])
    assert w.sum() == pytest.approx(1)
    assert np.all(w > 0)


def test_coluna_constante_recebe_peso_zero():
    X = np.array([[1.0, 3], [2, 3], [3, 3]])
    w = std_dev_weights(X, ["benefit", "benefit"])
    assert w[1] == 0
    assert w[0] == pytest.approx(1)


def test_mais_dispersao_mais_peso():
    X = np.array([[1.0, 9], [5, 10], [10, 11]])
    w = std_dev_weights(X, ["benefit", "benefit"])
    assert w[0] > w[1]


def test_custo_usa_min_sobre_x():
    x = np.array([1.0, 2, 4])
    X = np.column_stack([x, np.array([2.0, 2, 3])])
    w = std_dev_weights(X, ["cost", "benefit"])
    s_custo = (x.min() / x).std()
    s_benef = (X[:, 1] / X[:, 1].max()).std()
    assert w[0] == pytest.approx(s_custo / (s_custo + s_benef))


def test_valores_nao_positivos_dao_erro():
    with pytest.raises(ValueError):
        std_dev_weights(np.array([[0.0, 1], [1, 2]]), ["benefit", "benefit"])


def test_tipo_desconhecido_da_erro():
    with pytest.raises(ValueError):
        std_dev_weights(np.array([[1.0], [2]]), ["outro"])


def test_todas_as_colunas_constantes_da_erro():
    with pytest.raises(ValueError):
        std_dev_weights(np.array([[1.0, 2], [1, 2]]), ["benefit", "cost"])


@pytest.mark.parametrize("eta, esperado", [(1, [0.7, 0.3]), (0, [0.2, 0.8]), (0.5, [0.45, 0.55])])
def test_combinacao_com_eta(eta, esperado):
    w = combine_weights(np.array([0.7, 0.3]), np.array([0.2, 0.8]), eta)
    assert w == pytest.approx(esperado)
    assert w.sum() == pytest.approx(1)


@pytest.mark.parametrize("eta", [-0.1, 1.1])
def test_eta_fora_de_0_1_da_erro(eta):
    with pytest.raises(ValueError):
        combine_weights(np.array([0.5, 0.5]), np.array([0.5, 0.5]), eta)


def test_pesos_que_nao_somam_1_dao_erro():
    with pytest.raises(ValueError):
        combine_weights(np.array([0.5, 0.6]), np.array([0.5, 0.5]), 0.5)
