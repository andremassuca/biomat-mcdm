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


def test_resumo_tem_as_seccoes(saida):
    rk, mc, sp, cen = saida
    texto = ra.resumo_md(rk, mc, sp, cen, 20, 42)
    assert "PRELIMINAR: dados por verificar" in texto
    for caso in ("Haste", "Stent", "Scaffold"):
        assert f"## {caso}" in texto
    assert "Onde o vencedor muda" in texto
    assert "% de 1.º lugar" in texto
