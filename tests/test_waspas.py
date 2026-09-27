"""Testes unitários do WASPAS estendido (a reprodução do artigo está em
test_reproduce_petkovic.py)."""
import numpy as np
import pytest

from biomat_mcdm.methods.waspas import normalize_waspas, waspas

x = np.array([2.0, 4, 8])


def col(t, T=None):
    return normalize_waspas(x[:, None], [t], [T])[:, 0]


def test_eq9_beneficio():
    assert col("benefit") == pytest.approx(x / 8)


def test_eq10_custo():
    assert col("cost") == pytest.approx(2 / x)


def test_eq11_alvo_abaixo_de_todos():
    assert col("target", 1) == pytest.approx(1 - (x - 1) / 8)


def test_eq12_alvo_acima_de_todos():
    assert col("target", 10) == pytest.approx(1 - (10 - x) / 10)


def test_eq13_alvo_no_meio():
    assert col("target", 4) == pytest.approx(1 - np.abs(x - 4) / 6)


def test_alvo_igual_ao_maximo_e_ao_minimo():
    assert col("target", 8) == pytest.approx(col("benefit"))
    assert col("target", 2) == pytest.approx(col("cost"))


def test_valores_entre_0_e_1_e_melhor_vale_1():
    for t, T in [("benefit", None), ("cost", None), ("target", 4)]:
        r = col(t, T)
        assert np.all((r >= 0) & (r <= 1))
        assert r.max() == pytest.approx(1)


def test_lambda_1_e_soma_pesada_e_lambda_0_e_produto_pesado():
    X = np.array([[2.0, 5], [4, 3], [8, 1]])
    w = np.array([0.6, 0.4])
    R = normalize_waspas(X, ["benefit", "cost"], [None, None])
    assert waspas(X, w, ["benefit", "cost"], [None, None], lam=1) == pytest.approx((R * w).sum(1))
    assert waspas(X, w, ["benefit", "cost"], [None, None], lam=0) == pytest.approx(np.prod(R ** w, 1))


def test_dominante_fica_em_primeiro():
    X = np.array([[10.0, 1], [5, 2], [4, 3]])
    q = waspas(X, np.array([0.5, 0.5]), ["benefit", "cost"], [None, None])
    assert np.argmax(q) == 0


@pytest.mark.parametrize("lam", [-0.1, 1.5])
def test_lambda_fora_de_0_1_da_erro(lam):
    with pytest.raises(ValueError):
        waspas(np.array([[1.0], [2]]), np.array([1.0]), ["benefit"], [None], lam=lam)
