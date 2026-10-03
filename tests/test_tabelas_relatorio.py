"""Testes de scripts/tabelas_relatorio.py (o script carrega-se pelo caminho)."""
import importlib.util
from pathlib import Path

import pandas as pd
import pytest

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "tabelas_relatorio.py"
spec = importlib.util.spec_from_file_location("tabelas_relatorio", CAMINHO)
tr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tr)


def test_tabela_criterios_tem_todos_os_criterios_do_caso():
    crit = pd.read_csv(tr.DATA / "criterios.csv")
    for caso, _, _ in tr.CASOS.values():
        t = tr.tabela_criterios(caso)
        assert len(t) == (crit["caso_componente"] == caso).sum()
        assert set(t["Tipo"]) <= set(tr.TIPOS.values())
    t = tr.tabela_criterios("Prótese da anca | Haste femoral")
    assert t.loc[t["Critério"] == "Módulo de Young", "Alvo"].item() == "17 GPa"
    assert t.loc[t["Critério"] == "Módulo de Young", "Peso"].item() == "0,20"


def test_resultados_quantitativos_batem_com_results(tmp_path):
    pt = tr.pontuacoes("stent")
    assert set(pt["cenario"]) == {"A", "B"}
    assert tr.delta_c(pt, "A") == pytest.approx(0.024, abs=5e-4)
    assert "empate" in tr.frase_delta(pt)  # cenário B: ΔC = 0,002
    t = tr.tabela_resultados(pt)
    assert len(t) == len(pt) and t.iloc[0]["Pos. T"] == 1


def test_semiquantitativo_calcula_pontuacoes():
    pt = tr.pontuacoes("dentario")
    a = pt[pt["cenario"] == "A"].sort_values("pos_TOPSIS")
    assert a.iloc[0]["material"] == "Ti cp grau 4"


def test_pct_nao_arredonda_para_100_nem_para_0():
    assert tr.pct(99.99) == "99,99 %"
    assert tr.pct(100.0) == "100,0 %"
    assert tr.pct(0.01) == "0,01 %"
    assert tr.pct(56.64) == "56,6 %"


def test_gama_eta_compacta():
    eta = pd.DataFrame({"variante": ["η = 0,0", "η = 0,1", "η = 0,2", "η = 0,3"],
                        "material": ["X", "X", "Y", "Y"], "posicao": [1, 1, 1, 1]})
    assert tr.gama_eta(eta, "Y") == "η de 0 a 0,1"
    assert tr.gama_eta(eta, "X") == "η = 0,2, η = 0,3"
    assert tr.gama_eta(eta[eta["material"] == "Y"], "Y") == "nunca"


def test_nota_pesos_so_quando_nao_somam_1():
    assert "0,85" in tr.nota_pesos("Stent vascular")
    assert tr.nota_pesos("Prótese da anca | Haste femoral") == ""


def test_gerar_escreve_tres_ficheiros_por_caso(tmp_path):
    feitos = tr.gerar(tmp_path)
    assert len(feitos) == 3 * len(tr.CASOS) + 2  # mais o anexo B completo e o resumido
    texto = (tmp_path / "par_resultados.md").read_text(encoding="utf-8")
    assert "SEMIQUANTITATIVO" in texto and texto.startswith("<!-- gerado")


def test_anexo_b_tem_todas_as_linhas_da_base():
    m = pd.read_csv(tr.DATA / "materiais.csv")
    total = sum(len(tr.tabela_dados(c)) for c in m["caso"].drop_duplicates())
    assert total == len(m)
    t = tr.tabela_dados("Stent vascular")
    l605 = t[(t["Material"] == "Co-Cr L605") & (t["Propriedade"] == "Módulo de Young")].iloc[0]
    assert l605["Valor"] == "225" and l605["Estado"] == "Verificado (fornecedor)"
    assert "Contagem por estado" in tr.anexo_b()


def test_anexo_b_resumo_conta_por_caso_e_no_total():
    m = pd.read_csv(tr.DATA / "materiais.csv")
    t = tr.contagem_estados()
    assert t.loc["Total", "Total"] == len(m)
    assert t.loc["Stent vascular", "Total"] == (m["caso"] == "Stent vascular").sum()
    texto = tr.anexo_b_resumo()
    assert "anexo digital (data/base_dados_biomateriais.xlsx)" in texto and f"{len(m)} linhas" in texto
