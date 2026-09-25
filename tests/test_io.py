from biomat_mcdm.io import build_problem


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
    assert "Tempo de reabsorção" not in p.criteria  # permanentes sem valor → tratar à parte


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
