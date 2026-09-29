from biomat_mcdm.io import build_problem, load_parametros


def test_haste_cenario_A_exclui_investigacao():
    p = build_problem("Prótese da anca | Haste femoral", "A")
    assert "Ti-35Nb-7Zr-5Ta (TNZT)" not in p.alternatives
    assert p.X.shape == (len(p.alternatives), len(p.criteria))
    assert abs(p.weights.sum() - 1) < 1e-9


def test_par_articular_cenario_A_exclui_mom():
    p = build_problem("Prótese da anca | Par articular", "A")
    assert not any("MoM" in a for a in p.alternatives)


def test_stent_cenario_B_inclui_bioabsorviveis():
    p = build_problem("Stent vascular", "B")
    assert "Liga de Mg WE43 (bioabsorvível)" in p.alternatives
    # opção O2: os permanentes recebem o pior valor observado (48 meses, máximo do PLLA)
    j = p.criteria.index("Tempo de reabsorção")
    perm = [i for i, a in enumerate(p.alternatives) if "bioabsorvível" not in a]
    assert set(p.X[perm, j]) == {48.0}


def test_reabsorcao_so_entra_em_B():
    assert "Tempo de reabsorção" not in build_problem("Stent vascular", "A").criteria


def test_cenario_B_bio_so_bioabsorviveis_com_o_criterio():
    p = build_problem("Stent vascular", "B-bio")
    assert p.alternatives == ["Liga de Mg WE43 (bioabsorvível)", "PLLA (bioabsorvível)"]
    assert "Tempo de reabsorção" in p.criteria


def test_valor_em_falta_explicito_para_sensibilidade():
    p = build_problem("Stent vascular", "B", valor_em_falta={"Tempo de reabsorção": 600})
    j = p.criteria.index("Tempo de reabsorção")
    assert p.X[0, j] == 600


def test_cenario_desconhecido_da_erro():
    import pytest
    with pytest.raises(ValueError):
        build_problem("Stent vascular", "Z")


def test_nitinol_nunca_entra_no_ranking():
    for sc in ("A", "B"):
        p = build_problem("Stent vascular", sc)
        assert not any("Nitinol" in a for a in p.alternatives)


def test_par_articular_sem_kic():
    p = build_problem("Prótese da anca | Par articular", "B")
    assert not any("K_IC" in c for c in p.criteria)


def test_stent_usa_radiopacidade_e_nao_densidade():
    p = build_problem("Stent vascular", "A")
    assert "Radiopacidade (ordinal 1-5)" in p.criteria
    assert "Densidade" not in p.criteria


def test_stent_cenario_A_so_permanentes_e_B_com_bioabsorviveis():
    from biomat_mcdm.io import build_problem
    a = build_problem("Stent vascular", "A").alternatives
    b = build_problem("Stent vascular", "B").alternatives
    assert a == ["Aço inox 316L", "Co-Cr L605", "Co-Ni-Cr-Mo MP35N", "Pt-Cr"]
    assert b == a + ["Liga de Mg WE43 (bioabsorvível)", "PLLA (bioabsorvível)"]


def test_scaffold_cenario_A_so_uso_clinico_mas_mantem_biodegradaveis():
    from biomat_mcdm.io import build_problem
    a = build_problem("Scaffold (regeneração óssea)", "A").alternatives
    assert sorted(a) == sorted(["Hidroxiapatite (HA) porosa", "β-TCP poroso", "Vidro bioativo 45S5 poroso",
                                "PCL", "Compósito PCL/β-TCP (impressão 3D)"])  # PCL é biodegradável e fica
    assert len(build_problem("Scaffold (regeneração óssea)", "B").alternatives) == 8


def test_load_parametros_le_eta_e_incerteza():
    par = load_parametros()
    assert par["eta"] == 1.0
    assert par["incerteza_valor_unico"] == 0.1
