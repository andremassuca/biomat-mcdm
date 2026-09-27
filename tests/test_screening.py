"""Testes da triagem por critérios estritos."""
import pandas as pd
import pytest

from biomat_mcdm.io import build_problem
from biomat_mcdm.screening import StrictRule, apply_strict, parse_rule, screen_case


def longo(linhas):
    return pd.DataFrame(linhas, columns=["material", "estatuto", "propriedade", "min", "max"])


@pytest.mark.parametrize("alvo, op, limite", [("≥ 2", ">=", 2.0), (">= 2", ">=", 2.0),
                                              ("≤ 0,5", "<=", 0.5), ("= 3", "==", 3.0)])
def test_parse_regra_numerica(alvo, op, limite):
    r = parse_rule("c", alvo)
    assert (r.op, r.limite) == (op, limite)
    assert r.numerica


@pytest.mark.parametrize("alvo", ["Aprovado", "Avaliação qualitativa", "Expansível por balão"])
def test_parse_regra_qualitativa(alvo):
    r = parse_rule("c", alvo)
    assert not r.numerica
    assert r.alvo == alvo


def test_elimina_quem_falha_no_pior_caso_do_intervalo():
    m = longo([["A", "Clínico", "p", 3, 4], ["B", "Clínico", "p", 1, 3], ["C", "Clínico", "p", 2, 2]])
    aprovados, reg = apply_strict(m, [parse_rule("p", "≥ 2")])
    assert aprovados == ["A", "C"]  # B tem mínimo 1 < 2
    linha_b = reg[reg["material"] == "B"].iloc[0]
    assert linha_b["resultado"] == "eliminado"
    assert linha_b["valor"] == 1
    assert "mínimo" in linha_b["motivo"]


def test_regra_menor_ou_igual_usa_o_maximo():
    m = longo([["A", "Clínico", "p", 1, 6], ["B", "Clínico", "p", 1, 4]])
    aprovados, _ = apply_strict(m, [parse_rule("p", "≤ 5")])
    assert aprovados == ["B"]


def test_estatuto_excluido_elimina_com_motivo():
    m = longo([["A", "Clínico", "p", 1, 1], ["N", "Excluído (autoexpansível: só discussão)", "p", 1, 1]])
    aprovados, reg = apply_strict(m, [])
    assert aprovados == ["A"]
    assert reg.iloc[0]["motivo"] == "Excluído (autoexpansível: só discussão)"


def test_sem_dados_nao_elimina_e_fica_registado():
    m = longo([["A", "Clínico", "p", 3, 3], ["B", "Clínico", "outra", 1, 1]])
    aprovados, reg = apply_strict(m, [parse_rule("p", "≥ 2")])
    assert aprovados == ["A", "B"]
    assert reg[reg["material"] == "B"].iloc[0]["motivo"] == "sem dados na base"


def test_regra_qualitativa_nao_elimina():
    m = longo([["A", "Clínico", "p", 1, 1]])
    aprovados, reg = apply_strict(m, [StrictRule("Biocompatibilidade", "Aprovado")])
    assert aprovados == ["A"]
    assert reg.iloc[0]["resultado"] == "não avaliado"


def test_par_articular_elimina_so_o_mom():
    aprovados, reg = screen_case("Prótese da anca | Par articular")
    assert "CoCrMo / CoCrMo (MoM)" not in aprovados
    assert len(aprovados) == 4
    elim = reg[reg["resultado"] == "eliminado"]
    assert elim["material"].tolist() == ["CoCrMo / CoCrMo (MoM)"]


def test_stent_elimina_nitinol():
    aprovados, _ = screen_case("Stent vascular")
    assert not any("Nitinol" in a for a in aprovados)


def test_haste_nao_elimina_ninguem():
    aprovados, _ = screen_case("Prótese da anca | Haste femoral")
    assert len(aprovados) == 6


def test_build_problem_aplica_a_triagem():
    p = build_problem("Prótese da anca | Par articular", "B")
    assert "CoCrMo / CoCrMo (MoM)" not in p.alternatives


def test_caso_inexistente_da_erro():
    with pytest.raises(ValueError):
        screen_case("Caso que não existe")
