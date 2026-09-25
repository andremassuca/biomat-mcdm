import numpy as np
import pytest
from biomat_mcdm.methods.topsis import topsis, rank

X = np.array([[110, 550, 4.43],
              [200, 300, 8.00],
              [ 60, 350, 5.70]], float)
W = np.array([0.4, 0.4, 0.2])
TYPES = ["target", "benefit", "cost"]
TARGETS = [17, None, None]


def test_topsis_scores():
    C = topsis(X, W, TYPES, TARGETS)
    assert C == pytest.approx([0.817198, 0.0, 0.510249], abs=1e-5)


def test_rank():
    assert list(rank(np.array([0.817198, 0.0, 0.510249]))) == [1, 3, 2]
