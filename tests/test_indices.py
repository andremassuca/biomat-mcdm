"""Testes dos índices derivados (σy/E do stent e E_implante/E_osso da haste)."""
import pandas as pd
import pytest

from biomat_mcdm.indices import SIGMA_E, sigma_y_over_e, stiffness_ratio
from biomat_mcdm.io import build_problem, load_data, load_tissue

COLS = ["caso", "componente", "material", "norma", "classe", "estatuto", "propriedade",
        "unidade", "min", "max", "referencia", "notas", "tipico", "estado"]


def linha(material, prop, lo, hi, caso="Stent vascular", comp="Estrutura do stent"):
    return dict(zip(COLS, [caso, comp, material, "-", "Metal", "Clínico", prop, "-", lo, hi, "", "", (lo + hi) / 2, ""]))


def test_sigma_y_sobre_e_com_intervalo_conservador():
    m = pd.DataFrame([linha("A", "Tensão de cedência", 200, 300), linha("A", "Módulo de Young", 100, 200)])
    d = sigma_y_over_e(m).iloc[0]
    assert d["propriedade"] == SIGMA_E
    assert d["min"] == pytest.approx(200 / 200_000)   # σy mínimo / E máximo
    assert d["max"] == pytest.approx(300 / 100_000)   # σy máximo / E mínimo
    assert d["min"] <= d["tipico"] <= d["max"]


def test_sem_um_dos_valores_nao_ha_indice():
    m = pd.DataFrame([linha("A", "Tensão de cedência", 200, 300)])
    assert sigma_y_over_e(m).empty


def test_so_calcula_para_o_stent():
    m = pd.DataFrame([linha("A", "Tensão de cedência", 200, 300, caso="Prótese da anca", comp="Haste femoral"),
                      linha("A", "Módulo de Young", 100, 200, caso="Prótese da anca", comp="Haste femoral")])
    assert sigma_y_over_e(m).empty


def test_indice_entra_na_base_e_no_problema_do_stent_como_custo():
    mat, crit = load_data()
    assert (mat["propriedade"] == SIGMA_E).sum() == 7
    assert SIGMA_E in set(crit["criterio"])
    p = build_problem("Stent vascular", "A")
    j = p.criteria.index(SIGMA_E)
    assert p.types[j] == "cost"
    assert not any("Nitinol" in a for a in p.alternatives)


def test_razao_de_rigidez_da_haste():
    mat, _ = load_data()
    r = stiffness_ratio(mat, load_tissue()).set_index("material")
    assert len(r) == 6
    # Ti-6Al-4V ELI: E 110-114 GPa; osso cortical 15-20 GPa
    assert r.loc["Ti-6Al-4V ELI", "razao_tipica"] == pytest.approx(112 / 17.5)
    assert r.loc["Ti-6Al-4V ELI", "razao_min"] == pytest.approx(110 / 20)
    assert r.loc["Ti-6Al-4V ELI", "razao_max"] == pytest.approx(114 / 15)
    assert (r["razao_min"] > 1).all()   # todos mais rígidos do que o osso


def test_razao_sem_tecido_da_erro():
    mat, _ = load_data()
    with pytest.raises(ValueError):
        stiffness_ratio(mat, load_tissue(), tecido="Tecido inexistente")
