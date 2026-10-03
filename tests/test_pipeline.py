"""Testes do ponto de entrada por caso (pipeline.py)."""
import numpy as np
import pytest

from biomat_mcdm.io import DecisionProblem, build_problem
from biomat_mcdm.pipeline import fmt_pt, rank_all_methods, spearman_methods


def problema_pequeno():
    X = np.array([[10.0, 1], [5, 2], [1, 3]])
    return DecisionProblem(alternatives=["A", "B", "C"], criteria=["c1", "c2"],
                           X_min=X, X_max=X, types=["benefit", "cost"],
                           targets=[None, None], weights=np.array([0.5, 0.5]))


def test_colunas_e_dominante_em_primeiro_nos_tres_metodos():
    df = rank_all_methods(problema_pequeno())
    assert list(df.columns) == ["material", "C_TOPSIS", "Q_WASPAS", "P_VIKOR",
                                "pos_TOPSIS", "pos_WASPAS", "pos_VIKOR"]
    assert df.loc[0, ["pos_TOPSIS", "pos_WASPAS", "pos_VIKOR"]].tolist() == [1, 1, 1]


def test_pesos_explicitos_substituem_os_do_problema():
    p = problema_pequeno()
    a = rank_all_methods(p)
    b = rank_all_methods(p, weights=np.array([0.9, 0.1]))
    assert not np.allclose(a["C_TOPSIS"], b["C_TOPSIS"])


def test_spearman_simetrica_com_diagonal_1():
    rho = spearman_methods(rank_all_methods(problema_pequeno()))
    assert rho.shape == (3, 3)
    assert np.allclose(np.diag(rho), 1)
    assert np.allclose(rho, rho.T)


def test_spearman_com_ordens_iguais_da_1():
    rho = spearman_methods(rank_all_methods(problema_pequeno()))
    assert rho.to_numpy() == pytest.approx(np.ones((3, 3)))


@pytest.mark.parametrize("x, casas, esperado", [(0.2, 3, "0,200"), (0.7444, 3, "0,744"), (1, 2, "1,00")])
def test_fmt_pt_usa_virgula(x, casas, esperado):
    assert fmt_pt(x, casas) == esperado


def test_haste_cenarios_A_e_B_correm():
    for cen, n in (("A", 5), ("B", 6)):
        df = rank_all_methods(build_problem("Prótese da anca | Haste femoral", cen))
        assert len(df) == n
        for m in ("TOPSIS", "WASPAS", "VIKOR"):
            assert sorted(df[f"pos_{m}"]) == list(range(1, n + 1))


def test_consenso_borda_soma_pontos_e_desempata_pelo_topsis():
    import pandas as pd
    from biomat_mcdm.pipeline import consenso_borda
    df = pd.DataFrame({"material": ["X", "Y", "Z"], "pos_TOPSIS": [2, 1, 3],
                       "pos_WASPAS": [1, 2, 3], "pos_VIKOR": [1, 2, 3]})
    out = consenso_borda(df).set_index("material")
    assert out.loc["X", "pontos_Borda"] == 1 + 2 + 2 and out.loc["Y", "pontos_Borda"] == 2 + 1 + 1
    assert out.loc["X", "pos_Borda"] == 1 and out.loc["Z", "pos_Borda"] == 3
    empate = pd.DataFrame({"material": ["X", "Y"], "pos_TOPSIS": [2, 1], "pos_WASPAS": [1, 2], "pos_VIKOR": [1, 2]})
    e = consenso_borda(empate.iloc[:, :3].assign(pos_VIKOR=[2, 1])).set_index("material")
    assert e.loc["Y", "pos_Borda"] == 1  # 1 + 0 + 1 = 2 contra 0 + 1 + 0 = 1
