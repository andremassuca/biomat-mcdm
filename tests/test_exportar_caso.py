"""Testes de scripts/exportar_caso.py (o script carrega-se pelo caminho)."""
import importlib.util
from pathlib import Path

import pytest

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "exportar_caso.py"
spec = importlib.util.spec_from_file_location("exportar_caso", CAMINHO)
ec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ec)


def test_auxiliares():
    assert ec.fmt(0.2) == "0,2" and ec.fmt(float("nan")) == ""
    assert ec.txt("a|b") == "a;b"
    assert ec.aplica("Todos", "Stent") and ec.aplica("Haste, stent, scaffold", "Scaffold")
    assert not ec.aplica("Haste", "Stent")
    assert ec.seccao_md("x\n## A\nlinha\n### sub\n## B\nz", "A") == "linha\n#### sub"


@pytest.mark.parametrize("caso", ["stent", "scaffold"])
def test_gerar_tem_as_seccoes(caso):
    texto = ec.gerar(caso)
    for s in ("## 1. Candidatos", "## 2. Critérios", "## 3. Valores", "## 4. Rankings", "## 5. Robustez",
              "## 6. Triagem", "## 8. Notas", "## 9. Apoio"):
        assert s in texto
    assert chr(0x2014) not in texto  # travessão


def test_dividir_respeita_o_limite_e_repete_cabecalho():
    linhas = ["# T", "", "| a | b |", "|---|---|"] + [f"| {k} | {'x' * 50} |" for k in range(200)]
    partes = ec.dividir("\n".join(linhas), limite=2000)
    assert len(partes) > 1
    assert all(len(p.encode("utf-8")) < 2600 for p in partes)
    assert "| a | b |" in partes[1] and partes[1].startswith("[Parte 2 de")
