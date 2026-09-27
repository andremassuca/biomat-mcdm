"""Testes de scripts/exportar_xlsx.py (o script não é um pacote: carrega-se pelo caminho)."""
import importlib.util
from pathlib import Path

import pandas as pd
import pytest

from biomat_mcdm.io import DATA

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "exportar_xlsx.py"
spec = importlib.util.spec_from_file_location("exportar_xlsx", CAMINHO)
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)


@pytest.fixture(scope="module")
def livro():
    return ex.construir()


def test_folhas(livro):
    assert livro.sheetnames == ["LEIA-ME", "Materiais", "Criterios", "Soma_pesos", "Indices_stent",
                                "Indices_haste", "Cenarios", "Tecido", "Parametros"]


def test_nota_de_geracao_automatica(livro):
    assert livro["LEIA-ME"]["A1"].value == "Gerado automaticamente a partir de data/*.csv; não editar à mão."


def test_sem_formulas(livro):
    for ws in livro.worksheets:
        for linha in ws.iter_rows(values_only=True):
            assert not any(isinstance(v, str) and v.startswith("=") for v in linha)


def test_materiais_e_criterios_iguais_aos_csv(livro):
    for folha, ficheiro in (("Materiais", "materiais.csv"), ("Criterios", "criterios.csv")):
        csv = pd.read_csv(DATA / ficheiro)
        ws = livro[folha]
        assert ws.max_row == len(csv) + 1
        assert [c.value for c in ws[1]] == list(csv.columns)
        assert ws.auto_filter.ref is not None
        assert ws.freeze_panes == "A2"


def test_soma_dos_pesos_por_caso():
    crit = pd.read_csv(DATA / "criterios.csv")
    s = ex.soma_pesos(crit).set_index("caso_componente")["soma_dos_pesos"]
    assert s["Prótese da anca | Haste femoral"] == pytest.approx(1)
    assert s["Stent vascular"] == pytest.approx(1)  # 0,85 + 0,15 do tempo de reabsorção (só B)


def test_indices_e_parametros(livro):
    assert livro["Indices_stent"].max_row == 8   # cabeçalho + 7 materiais
    assert livro["Indices_haste"].max_row == 7   # cabeçalho + 6 materiais
    assert livro["Parametros"]["A2"].value == "eta"
    assert livro["Parametros"]["B2"].value == 1.0
