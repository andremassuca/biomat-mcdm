"""Testes unitários do VIKOR abrangente (a reprodução do artigo está em
test_reproduce_petkovic.py)."""
import numpy as np
import pytest

from biomat_mcdm.methods.vikor import compromise_set, vikor


def test_S_e_R_pelas_eqs_17_18():
    X = np.array([[1.0, 10], [3, 20], [5, 30]])
    w = np.array([0.4, 0.6])
    out = vikor(X, w, ["benefit", "target"], [None, 15])
    A = np.array([5 - 1, 30 - 10])
    T = np.array([5, 15])
    E = w * (1 - np.exp(-np.abs(X - T) / A))
    assert out["S"] == pytest.approx(E.sum(1))
    assert out["R"] == pytest.approx(E.max(1))


def test_P_entre_0_e_1_e_ideal_tem_P_0():
    X = np.array([[5.0, 1], [3, 2], [1, 3]])
    out = vikor(X, np.array([0.5, 0.5]), ["benefit", "cost"], [None, None])
    assert out["P"].min() == pytest.approx(0)
    assert out["P"].max() == pytest.approx(1)
    assert np.argmin(out["P"]) == 0


def test_P_so_com_R_quando_S_constante():
    # 1.º ramo da eq. 19. Construção: E = (a, a), (b, 0), (0, b) com 2a = b, logo S igual
    # para as três e R diferente. Com A = 1: b = 0,5 (1 - e^-1); a exige d0 = -ln((1 + e^-1) / 2).
    d0 = -np.log((1 + np.exp(-1)) / 2)
    X = np.array([[1 - d0, 1 - d0], [0.0, 1.0], [1.0, 0.0]])
    out = vikor(X, np.array([0.5, 0.5]), ["benefit", "benefit"], [None, None])
    assert np.ptp(out["S"]) == pytest.approx(0, abs=1e-12)
    R = out["R"]
    assert out["P"] == pytest.approx((R - R.min()) / (R.max() - R.min()))


def test_tudo_igual_da_P_0():
    X = np.array([[1.0, 2], [1, 2]])
    out = vikor(X, np.array([0.5, 0.5]), ["benefit", "cost"], [None, None])
    assert out["P"] == pytest.approx([0, 0])


@pytest.mark.parametrize("v", [-0.1, 1.1])
def test_v_fora_de_0_1_da_erro(v):
    with pytest.raises(ValueError):
        vikor(np.array([[1.0], [2]]), np.array([1.0]), ["benefit"], [None], v=v)


def test_compromisso_c1_e_c2_cumpridas():
    P = np.array([0.0, 0.6, 1.0])
    S = np.array([0.1, 0.5, 0.9])
    R = np.array([0.1, 0.5, 0.9])
    assert compromise_set(S, R, P) == [0]


def test_compromisso_so_c2_falha():
    P = np.array([0.0, 0.6, 1.0])
    S = np.array([0.5, 0.1, 0.9])   # o 1.º por P não é o melhor em S
    R = np.array([0.5, 0.1, 0.9])   # nem em R
    assert compromise_set(S, R, P) == [0, 1]


def test_compromisso_c1_falha():
    # m = 5 -> limiar 1/4 = 0,25
    P = np.array([0.0, 0.1, 0.2, 0.3, 1.0])
    S = R = np.arange(5, dtype=float)
    assert compromise_set(S, R, P) == [0, 1, 2]
