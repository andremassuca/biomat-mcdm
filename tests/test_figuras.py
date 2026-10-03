"""Testes das funções de scripts/figuras.py (o script não é um pacote: carrega-se pelo caminho)."""
import importlib.util
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pytest

RAIZ = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("figuras", RAIZ / "scripts" / "figuras.py")
fg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fg)
spec = importlib.util.spec_from_file_location("run_all", RAIZ / "scripts" / "run_all.py")
ra = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ra)


@pytest.fixture(scope="module")
def saida():
    rk, mc, _, _ = ra.correr(n_iter=20, seed=42)
    return rk, mc, ra.pontuacao_linhas()


def test_nomes_curtos():
    assert fg.curto("Liga de Mg WE43 (bioabsorvível)") == "Mg WE43"
    assert fg.curto("Co-Cr L605") == "Co-Cr L605"
    assert fg.curto_celula("Compósito PCL/β-TCP (impressão 3D)") == "PCL/β-TCP"
    assert fg.curto_celula("Co-Cr L605 = Pt-Cr") == "L605 = Pt-Cr"


def test_paleta_cobre_todos_os_materiais_sem_cores_repetidas_no_caso(saida):
    rk, _, _ = saida
    for caso, cores in fg.COR_MATERIAL.items():
        assert len(set(cores.values())) == len(cores)
        assert set(rk[rk["caso"] == caso]["material"]) <= set(cores)
    haste = set(fg.dados_rigidez()[0]["material"])
    assert haste <= set(fg.COR_MATERIAL["Haste"])
    assert fg.cor("Haste", "Aço inox 316L") == fg.cor("Stent", "Aço inox 316L")


def test_rigidez_ordenada_faixa_a_volta_de_1_e_investigacao():
    df, (lo, hi), (e_lo, e_hi) = fg.dados_rigidez()
    assert df["razao_tipica"].is_monotonic_increasing
    assert lo < 1 < hi and e_lo < e_hi
    assert (df["razao_min"] <= df["razao_tipica"]).all() and (df["razao_tipica"] <= df["razao_max"]).all()
    assert df.set_index("material")["investigacao"].to_dict()["Ti-35Nb-7Zr-5Ta (TNZT)"]
    assert not df.set_index("material")["investigacao"].to_dict()["Ti-6Al-4V ELI"]


def test_posicoes_tem_os_tres_metodos_e_um_primeiro(saida):
    rk, _, _ = saida
    t = fg.dados_posicoes(rk, "Stent", "A")
    assert list(t.columns) == fg.METODOS
    assert t["TOPSIS"].iloc[0] == 1
    assert len(t) == 4


def test_empates_topsis_com_limiar():
    pt = pd.DataFrame({"caso": "X", "cenario": "A", "material": list("abcd"),
                       "C_TOPSIS": [0.700, 0.695, 0.600, 0.400]})
    assert fg.empates_topsis(pt, "X", "A") == {"a", "b"}
    assert fg.empates_topsis(pt, "X", "A", limiar=0.001) == set()
    assert fg.empates_topsis(pt, "X", "B") == set()


def test_frase_concordancia():
    def t(w, v):
        return pd.DataFrame({"TOPSIS": [1, 2, 3], "WASPAS": w, "VIKOR": v}, index=list("abc"))
    assert "mesma ordem" in fg.frase_concordancia(t([1, 2, 3], [1, 2, 3]))
    assert "Mesmo vencedor" in fg.frase_concordancia(t([1, 3, 2], [1, 2, 3]))
    assert "não concordam" in fg.frase_concordancia(t([2, 1, 3], [1, 2, 3]))


def test_monte_carlo_percentagens_entre_0_e_100(saida):
    _, mc, _ = saida
    t = fg.dados_monte_carlo(mc, "Haste", "TOPSIS")
    assert list(t.columns) == ["pct_primeiro", "pct_segundo", "pct_terceiro"]
    assert ((t >= 0) & (t <= 100)).all().all()
    assert (t.sum(axis=1) <= 100 + 1e-9).all()
    p = fg.dados_primeiro(mc, "Stent")
    assert list(p.columns) == fg.METODOS and len(p) == 4
    assert p["TOPSIS"].is_monotonic_decreasing


def test_separar_zeros():
    t = pd.DataFrame({"TOPSIS": [60.0, 0.2, 0.0], "WASPAS": [99.0, 1.0, 0.0], "VIKOR": [70.0, 0.0, 0.4]},
                     index=["a", "b", "c"])
    fica, zeros = fg.separar_zeros(t)
    assert fica.index.tolist() == ["a", "b"]
    assert zeros == ["c"]


def test_vencedor_eta_tem_11_valores_por_metodo(saida):
    rk, _, _ = saida
    t = fg.dados_vencedor_eta(rk, "Scaffold")
    assert t.shape == (3, 11)
    assert list(t.columns) == pytest.approx([k / 10 for k in range(11)])
    assert t.notna().all().all()


def test_o_que_muda_resume_os_cenarios():
    def linhas(cen, var, venc):
        return [{"caso": "X", "cenario": cen, "variante": var, "metodo": m, "material": v, "posicao": 1}
                for m, v in zip(fg.METODOS, venc)]
    rk = pd.DataFrame(linhas("A", "A", "aaa") + linhas("Q", "sem ordinais", "aaa")
                      + linhas("η", "η = 0,0", "bab") + linhas("η", "η = 0,5", "baa")
                      + linhas("η", "η = 1,0", "aaa") + linhas("C-custo", "custo elevado (0,25)", "bbb"))
    assert fg.o_que_muda(rk, "X") == "η até 0,5 (TOPSIS, VIKOR); peso do custo elevado"
    so_a = pd.DataFrame(linhas("A", "A", "aaa") + linhas("Q", "sem ordinais", "aaa"))
    assert fg.o_que_muda(so_a, "X") == "nenhum cenário de sensibilidade"


def test_resumo_tem_uma_linha_por_caso(saida):
    rk, mc, _ = saida
    r = fg.dados_resumo(rk, mc)
    assert r["caso"].tolist() == ["Haste", "Stent", "Scaffold"]
    for linha in r.itertuples():
        assert sorted(m for met in linha.vencedores.values() for m in met) == sorted(fg.METODOS)
        assert all(len(v) == 3 for v in linha.monte_carlo.values())
        assert linha.muda


def test_figuras_gravam_png_e_svg(saida, tmp_path):
    rk, mc, pt = saida
    figs = fg.todas(rk, pt, mc)
    assert list(figs) == ["fig_a_rigidez_haste", "fig_b_posicoes", "fig_c_monte_carlo",
                          "fig_c2_monte_carlo_completo", "fig_d_vencedor_eta", "fig_e_resumo",
                          "fig_f_semiquantitativos"]
    for nome, fig in figs.items():
        caminhos = fg.gravar(fig, nome, tmp_path)
        assert [c.suffix for c in caminhos] == [".png", ".svg"]
        assert all(c.stat().st_size > 0 for c in caminhos)
    assert plt.get_fignums() == []


def test_semiquantitativos_notas_de_0_a_1_e_ordem_do_topsis():
    val, nota, pesos = fg.dados_semiquantitativos("Implante dentário")
    assert val.index[0] == "Ti cp grau 4"
    assert ((nota >= 0) & (nota <= 1)).all().all() and sum(pesos) == pytest.approx(1)
    j = "Evidência clínica de osteointegração (ordinal 1-5)"
    assert nota.loc["Ti cp grau 4", j] == 1 and nota.loc["PEEK", j] == 0
    m = "Módulo de Young"  # alvo 15 GPa: o PEEK (3,5) é o mais perto
    assert nota[m].idxmax() == "PEEK"


def test_pct_fig_nao_arredonda_para_100_nem_para_0():
    assert fg.pct_fig(99.99) == "99,99" and fg.pct_fig(100.0) == "100"
    assert fg.pct_fig(0.01) == "0,01" and fg.pct_fig(0.0) == "0" and fg.pct_fig(56.6) == "57"
