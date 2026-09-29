"""Testes de por_verificar.py e de scripts/listar_por_verificar.py."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

from biomat_mcdm.io import DecisionProblem
from biomat_mcdm.por_verificar import influencia_celulas, por_verificar, tabela_caso

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "listar_por_verificar.py"
spec = importlib.util.spec_from_file_location("listar_por_verificar", CAMINHO)
lpv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lpv)


def problema():
    # A ganha por pouco em c1; c2 ordinal
    X = np.array([[10.0, 3], [9.5, 3], [5.0, 3]])
    return DecisionProblem(["A", "B", "C"], ["c1", "c2 (ordinal 1-5)"], X, X.copy(),
                           ["benefit", "benefit"], [None, None], np.array([0.9, 0.1]))


def test_estados_a_verificar():
    assert por_verificar("A verificar") and por_verificar("A verificar (derivado)")
    assert not por_verificar("Verificado") and not por_verificar("Verificado (derivado)")
    assert not por_verificar(float("nan")) and not por_verificar(None)


def test_so_celulas_a_verificar_e_ordem_por_influencia():
    p = problema()
    estados = {("A", "c1"): ("A verificar", "f1"), ("B", "c1"): ("A verificar", "f2"),
               ("C", "c1"): ("A verificar", "f3"), ("A", "c2 (ordinal 1-5)"): ("Verificado", "f4")}
    df = influencia_celulas(p, estados, 0.2)
    assert len(df) == 3  # a célula verificada fica de fora
    assert df.iloc[0]["muda_vencedor"]  # A -20 % ou B +20 % troca o 1.º lugar
    assert set(df[df["muda_vencedor"]]["material"]) == {"A", "B"}
    assert not df[df["material"] == "C"]["muda_vencedor"].iloc[0]
    assert (df["dC_material"] >= 0).all() and df["dC_max"].ge(df["dC_material"]).all()


def test_valor_zero_nao_tem_influencia_e_tipo_ordinal():
    X = np.array([[0.0, 3], [1.0, 4]])
    p = DecisionProblem(["A", "B"], ["c1", "c2 (ordinal 1-5)"], X, X.copy(), ["cost", "benefit"],
                        [None, None], np.array([0.5, 0.5]))
    df = influencia_celulas(p, {("A", "c1"): ("A verificar", ""), ("A", "c2 (ordinal 1-5)"): ("A verificar", "")})
    assert df.set_index("criterio").loc["c1", "dC_max"] == pytest.approx(0)
    assert df.set_index("criterio").loc["c2 (ordinal 1-5)", "tipo"] == "ordinal"
    with pytest.raises(ValueError):
        influencia_celulas(p, {}, 0)


def test_tabela_do_stent_usa_a_base():
    df = tabela_caso("Stent vascular")
    assert set(df["cenario"]) <= {"A", "B"}
    assert not df.duplicated(["material", "criterio"]).any()  # B só com células novas
    assert df["estado"].str.startswith("A verificar").all()
    assert (df[df["cenario"] == "B"]["material"].isin(
        ["Liga de Mg WE43 (bioabsorvível)", "PLLA (bioabsorvível)"])
        | df[df["cenario"] == "B"]["criterio"].str.startswith("Tempo")).all()


def test_resumo_md_tem_uma_seccao_por_caso():
    tabelas = {"Stent": tabela_caso("Stent vascular")}
    texto = lpv.resumo_md(tabelas, 0.2)
    assert "## Stent" in texto and "±20 %" in texto and "Vencedor do TOPSIS" in texto


def test_valores_atribuidos_pela_opcao_O2_nao_entram():
    df = tabela_caso("Stent vascular")
    perm = ["Aço inox 316L", "Co-Cr L605", "Co-Ni-Cr-Mo MP35N", "Pt-Cr"]
    reab = df[df["criterio"].str.startswith("Tempo de reabsorção")]
    assert not reab["material"].isin(perm).any()
    assert set(reab["material"]) == {"Liga de Mg WE43 (bioabsorvível)", "PLLA (bioabsorvível)"}
