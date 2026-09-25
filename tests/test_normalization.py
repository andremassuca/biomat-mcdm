"""Valores esperados calculados à mão com a eq. (2) — servem de especificação."""
import numpy as np
import pytest
from biomat_mcdm.normalization import normalize_column, normalize_matrix, reference_value

X = np.array([[110, 550, 4.43],
              [200, 300, 8.00],
              [ 60, 350, 5.70]], float)
TYPES = ["target", "benefit", "cost"]
TARGETS = [17, None, None]
R_EXPECTED = np.array([[0.491803, 1.0, 1.0],
                       [0.0,      0.0, 0.0],
                       [0.765027, 0.2, 0.644258]])


def test_reference_values():
    assert reference_value(X[:, 1], "benefit") == 550
    assert reference_value(X[:, 2], "cost") == 4.43
    assert reference_value(X[:, 0], "target", 17) == 17


def test_target_column():
    # E = 110, 200, 60 GPa com alvo 17 GPa (osso): o de 60 GPa deve ser o melhor
    r = normalize_column(X[:, 0], "target", 17)
    assert r == pytest.approx(R_EXPECTED[:, 0], abs=1e-5)
    assert r.argmax() == 2


def test_matrix():
    assert normalize_matrix(X, TYPES, TARGETS) == pytest.approx(R_EXPECTED, abs=1e-5)


def test_range_0_1():
    R = normalize_matrix(X, TYPES, TARGETS)
    assert R.min() >= 0 and R.max() <= 1
