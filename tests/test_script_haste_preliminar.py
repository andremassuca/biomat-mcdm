"""Testes das funções de scripts/haste_preliminar.py (o script não é um pacote: carrega-se pelo caminho)."""
import importlib.util
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "haste_preliminar.py"
spec = importlib.util.spec_from_file_location("haste_preliminar", CAMINHO)
hp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hp)


@pytest.fixture(scope="module")
def cenario_a():
    return hp.calcular("A")


def test_ordenado_por_topsis(cenario_a):
    df, _, _ = cenario_a
    assert df["pos_TOPSIS"].tolist() == sorted(df["pos_TOPSIS"])


def test_pesos_com_virgula_decimal(cenario_a):
    _, _, p = cenario_a
    texto = hp.criterios_md(p)
    assert "peso 0,20" in texto
    assert "peso 0." not in texto
    assert "alvo 17" in texto


def test_tabela_md_tem_os_tres_metodos_e_spearman(cenario_a):
    df, rho, p = cenario_a
    linhas = hp.tabela_md("A", df, rho, p)
    texto = "\n".join(linhas)
    assert "| Material | TOPSIS (C) | WASPAS (Q) | VIKOR (P, menor = melhor) |" in texto
    assert "Correlação de Spearman" in texto
    assert len([l for l in linhas if l.startswith("| ") and ".º (" in l]) == len(df)
    assert "0." not in texto.split("Critérios e pesos")[1].split("\n")[0]


def test_cor_texto_contrasta_com_o_fundo():
    assert hp.cor_texto((0.1, 0.2, 0.5, 1)) == "white"
    assert hp.cor_texto((0.9, 0.93, 0.97, 1)) == hp.TEXTO


def test_figura_tem_dois_paineis_e_aviso():
    res = {c: hp.calcular(c)[:2] for c in ("A", "B")}
    fig = hp.figura(res)
    assert len(fig.axes) == 2
    assert "PRELIMINAR: dados por verificar" in fig._suptitle.get_text()
    plt.close(fig)
