"""Testes de scripts/montar_relatorio.py (o script carrega-se pelo caminho)."""
import importlib.util
import re
from pathlib import Path

CAMINHO = Path(__file__).resolve().parents[1] / "scripts" / "montar_relatorio.py"
spec = importlib.util.spec_from_file_location("montar_relatorio", CAMINHO)
mr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mr)


def test_renumerar_caso():
    t = "# Caso 3: Stent\n\n## Problema\n\ntexto\n\n## Resultados\n\n### 1. Função do dispositivo\n"
    r = mr.renumerar_caso(t, 5)
    assert r.startswith("# 5. Stent")
    assert "## 5.1 Problema" in r and "## 5.2 Resultados" in r and "### Q1. Função do dispositivo" in r


def test_normas_alfabeticas_e_sem_duplicados():
    t = "ASTM F2182 e ASTM F2182-19e2; ISO 7206-4:2010; ASTM F2052-21, F2213-25; ISO 14801."
    assert mr.normas(t) == ["ASTM F2052-21", "ASTM F2182-19e2", "ASTM F2213-25", "ISO 7206-4:2010", "ISO 14801"]


def test_bloco_de_figuras_numera_uma_vez_e_remete_depois():
    num = mr.Numerador()
    a = mr.bloco_figuras(["fig_b_posicoes", "fig_c_monte_carlo"], num)
    assert a.startswith("As Figuras 1 e 2 mostram") and "**Figura 2.**" in a
    b = mr.bloco_figuras(["fig_c_monte_carlo"], num)
    assert b == "Ver também a Figura 2."


def test_relatorio_montado_sem_marcadores_e_com_referencias_numeradas():
    texto = mr.montar()
    assert "<!--" not in texto
    corpo, resto = texto.split("\n# Referências\n", 1)
    refs = re.findall(r"^(\d+)\. ", resto.split("\n# Normas citadas")[0], flags=re.M)
    citados = {int(n) for n in re.findall(r"\[(\d+)\]", corpo)}
    assert citados == set(range(1, len(refs) + 1))
    for sec in ("# 1. Introdução", "# 4. Prótese total da anca", "# 7. Implante dentário", "# 9. Conclusões",
                "# Anexo A.", "# Anexo B.", "# Glossário"):
        assert sec in texto
    figs = re.findall(r"\*\*Figura (\d+)\.\*\*", texto)
    assert figs == [str(i) for i in range(1, len(figs) + 1)]
