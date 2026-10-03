"""Testes de scripts/run_all.py com poucas iterações (o script carrega-se pelo caminho)."""
import importlib.util
from pathlib import Path

import pytest

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "run_all.py"
spec = importlib.util.spec_from_file_location("run_all", CAMINHO)
ra = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ra)


@pytest.fixture(scope="module")
def saida():
    return ra.correr(n_iter=20, seed=42)


@pytest.mark.parametrize("casos, caso, esperado", [
    ("Todos", "Haste", True), ("Todos os quantitativos", "Stent", True),
    ("Haste, stent, scaffold", "Scaffold", True), ("Stent", "Haste", False), ("Haste", "Haste", True)])
def test_aplica(casos, caso, esperado):
    assert ra.aplica(casos, caso) is esperado


def test_variantes_por_cenario():
    assert len(ra.variantes("η", "Haste")) == 11
    assert len(ra.variantes("T-haste", "Haste")) == 5
    assert len(ra.variantes("R-sentinela", "Stent")) == 4
    assert len(ra.variantes("T-scaffold", "Scaffold")) == 8
    assert len(ra.variantes("C-custo", "Scaffold")) == 2
    assert [v for v, _ in ra.variantes("P-foco", "Stent")] == ["direta", "direta + indireta"]
    (rot, p), = ra.variantes("O-orçamento", "Stent")
    assert "Pt-Cr" in rot and "Pt-Cr" not in p.alternatives
    assert ra.variantes("MC", "Haste") == []


def test_todos_os_cenarios_de_cenarios_csv_entram(saida):
    rk, mc, sp, cen = saida
    esperados = set(cen["cenario"]) - {"W", "M", "MC"}  # W e MC no monte_carlo.csv; M no spearman.csv
    assert esperados <= set(rk["cenario"])
    assert set(mc["analise"]) == {"MC propriedades", "W pesos ±20 %"}
    assert set(rk["caso"]) == {"Haste", "Stent", "Scaffold"}


def test_b_bio_so_no_stent_e_sem_spearman(saida):
    rk, _, sp, _ = saida
    assert set(rk[rk["cenario"] == "B-bio"]["caso"]) == {"Stent"}
    assert sp[sp["cenario"] == "B-bio"].empty


def test_monte_carlo_percentagens_somam_pelo_menos_100(saida):
    _, mc, _, _ = saida
    soma = mc.groupby(["caso", "analise", "metodo"])["pct_primeiro"].sum()
    assert (soma >= 100 - 1e-9).all()
    assert {"pct_segundo", "pct_terceiro"} <= set(mc.columns)
    assert (mc[["pct_primeiro", "pct_segundo", "pct_terceiro"]].sum(axis=1) <= 100 + 1e-9).all()


def test_pontuacoes_tem_os_tres_casos_e_dois_cenarios():
    pt = ra.pontuacao_linhas()
    assert set(pt["caso"]) == {"Haste", "Stent", "Scaffold"}
    assert set(pt["cenario"]) == {"A", "B"}
    assert {"C_TOPSIS", "Q_WASPAS", "P_VIKOR", "pos_TOPSIS", "pos_Borda", "pontos_Borda"} <= set(pt.columns)
    um = pt[(pt["caso"] == "Stent") & (pt["cenario"] == "A")]
    assert sorted(um["pos_TOPSIS"]) == [1, 2, 3, 4]


def test_resumo_tem_as_seccoes(saida):
    rk, mc, sp, cen = saida
    texto = ra.resumo_md(rk, mc, sp, cen, 20, 42)
    assert "PRELIMINAR: dados por verificar" in texto
    for caso in ("Haste", "Stent", "Scaffold"):
        assert f"## {caso}" in texto
    assert "Onde o vencedor muda" in texto
    assert "% de 1.º lugar" in texto


def test_p_foco_aumenta_o_peso_do_problema_e_soma_1():
    base = ra.build_problem(ra.CASOS["Scaffold"], "A")
    (_, d), (_, di) = ra.variantes("P-foco", "Scaffold")
    j = base.criteria.index("Porosidade")
    k = base.criteria.index("Módulo de compressão (scaffold)")
    assert d.weights.sum() == pytest.approx(1) and di.weights.sum() == pytest.approx(1)
    assert d.weights[j] > base.weights[j] and d.weights[k] < base.weights[k]  # módulo é indireto
    assert di.weights[k] > d.weights[k]


def test_semiquantitativos_a_parte():
    sq = ra.semiquantitativos_linhas()
    assert set(sq["caso"]) == {"Par articular", "Implante dentário"}
    par = sq[sq["caso"] == "Par articular"]
    assert set(zip(par["cenario"], par["variante"])) == {("A", "A"), ("P-foco", "direta"),
                                                         ("P-foco", "direta + indireta")}
    dent = sq[sq["caso"] == "Implante dentário"]
    assert ("Valor", "Ti-Zr: corrosão 4") in set(zip(dent["cenario"], dent["variante"]))
    texto = "\n".join(ra.semiquantitativos_md(sq))
    assert texto.count("SEMIQUANTITATIVO") == 2
