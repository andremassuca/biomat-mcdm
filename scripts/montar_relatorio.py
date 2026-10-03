"""Monta relatorio/RELATORIO.md a partir dos rascunhos, das tabelas geradas e das figuras.

Ordem: capa (metadados YAML), resumo, índice (gerado pelo pandoc), 1 Introdução (com a Tabela 1, resumo
dos casos), 2 Métodos, 3 Validação, 4-7 Casos (anca, stent, scaffold, implante dentário), 8 Discussão,
9 Conclusões, Referências, Normas citadas, Anexos A e B, Glossário e Declaração.
- Os marcadores <!-- incluir: tabelas/x.md --> e <!-- figura: fig_x --> são substituídos pelas tabelas
  de relatorio/tabelas/ e pelas figuras de results/figures/, numeradas pela ordem em que aparecem.
- As citações "Apelido (et al.) ano" passam a "Apelido (et al.) [n]", pela ordem da primeira citação, e a
  lista de referências sai numerada (estilo Vancouver), a partir de relatorio/referencias.md.
- As normas ISO e ASTM citadas saem numa lista própria, por ordem alfabética.
Correr antes scripts/run_all.py, scripts/figuras.py e scripts/tabelas_relatorio.py.
Uso: python scripts/montar_relatorio.py
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REL = RAIZ / "relatorio"
FIGURAS = "../results/figures"  # caminho relativo a relatorio/

_spec = importlib.util.spec_from_file_location("verificar_referencias", RAIZ / "scripts" / "verificar_referencias.py")
vr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vr)

CASOS = [("caso_anca_rascunho.md", 4), ("caso_stent_rascunho.md", 5), ("caso_scaffold_rascunho.md", 6),
         ("caso_dentario_rascunho.md", 7)]
NOMES_TABELA = {"haste": "haste femoral", "par": "par articular (semiquantitativo)", "stent": "stent vascular",
                "scaffold": "scaffold ósseo", "dentario": "implante dentário (semiquantitativo)"}
LEGENDAS = {
    "fig_a_rigidez_haste": "Razão entre o módulo de Young de cada liga candidata à haste e o do osso cortical "
                           "(barra: valor típico; traço: mínimo a máximo).",
    "fig_b_posicoes": "Posição de cada material por método (TOPSIS, WASPAS e VIKOR) nos três casos quantitativos, "
                      "cenários A e B (η = 1).",
    "fig_c_monte_carlo": "Monte Carlo das propriedades (10 000 iterações, cenário A): percentagem das iterações em "
                         "que cada material fica em 1.º lugar, por método.",
    "fig_d_vencedor_eta": "Material em 1.º lugar no cenário A, por método, quando η vai de 0 (só pesos objetivos) "
                          "a 1 (só pesos subjetivos).",
    "fig_e_resumo": "Resumo dos três casos quantitativos: vencedor por método, robustez no Monte Carlo das "
                    "propriedades e cenários em que o vencedor muda.",
    "fig_f_semiquantitativos": "Valores por critério nos casos semiquantitativos (par articular e implante "
                               "dentário), cenário A; cor do pior (claro) ao melhor (escuro) em cada critério.",
}
INCLUIR = re.compile(r"<!-- incluir: tabelas/(?P<nome>[\w]+)\.md -->")
FIGURA = re.compile(r"<!-- figura: ([\w]+) -->")
BLOCO_FIGURAS = re.compile(r"(?:<!-- figura: [\w]+ -->\s*)+")
NORMA = re.compile(r"\b(?:ISO|ASTM)\s(?:F?\d[\w.\-]*(?::\d{4})?(?:\(\d{4}\))?(?:e\d)?)"
                   r"(?:,\s(?:F\d[\w.\-]*))*")


def ler(nome: str) -> str:
    return (REL / nome).read_text(encoding="utf-8").strip()


def sem_titulo(texto: str) -> str:
    """Tira a primeira linha de título (# ...)."""
    linhas = texto.splitlines()
    return "\n".join(linhas[1:]).strip() if linhas and linhas[0].startswith("# ") else texto


def renumerar_caso(texto: str, n: int) -> str:
    """Título "# Caso k: X" passa a "# n. X"; secções ## numeradas n.1, n.2, ...; questões "### k." passam a "### Qk.".

    Em linguagem simples: põe o caso no número de secção do relatório e deixa as questões do
    enunciado identificadas como Q1 a Q11.
    """
    texto = re.sub(r"^# Caso \d+: (.+)$", lambda m: f"# {n}. {m.group(1)}", texto, count=1, flags=re.M)
    contador = iter(range(1, 100))
    texto = re.sub(r"^## (?!\d)(.+)$", lambda m: f"## {n}.{next(contador)} {m.group(1)}", texto, flags=re.M)
    return re.sub(r"^### (\d+)\. ", r"### Q\1. ", texto, flags=re.M)


class Numerador:
    """Numera figuras e tabelas pela ordem em que aparecem e guarda o número de cada figura."""

    def __init__(self) -> None:
        self.tabela = 0
        self.figuras: dict[str, int] = {}

    def nova_tabela(self) -> int:
        self.tabela += 1
        return self.tabela

    def figura(self, nome: str) -> tuple[int, bool]:
        """Número da figura e se é a primeira vez que aparece."""
        if nome in self.figuras:
            return self.figuras[nome], False
        self.figuras[nome] = len(self.figuras) + 1
        return self.figuras[nome], True


def tabela_gerada(nome: str, num: Numerador) -> str:
    """Conteúdo de relatorio/tabelas/<nome>.md, com legenda e frase de chamada quando é tabela."""
    corpo = "\n".join(l for l in ler(f"tabelas/{nome}.md").splitlines() if not l.startswith("<!--")).strip()
    chave, tipo = nome.rsplit("_", 1)
    if tipo == "robustez":
        return corpo
    n = num.nova_tabela()
    if tipo == "criterios":
        legenda = f"Critérios, tipo, alvo, peso e justificação: {NOMES_TABELA[chave]}."
        chamada = f"Os critérios e os pesos estão na Tabela {n}."
    else:
        legenda = f"Pontuação e posição nos três métodos e consenso de Borda, cenários A e B: {NOMES_TABELA[chave]}."
        chamada = f"Os resultados estão na Tabela {n}."
    return f"{chamada}\n\n**Tabela {n}.** {legenda}\n\n{corpo}"


def lista_pt(nums: list[int]) -> str:
    """[1] -> "Figura 1"; [2, 3, 4] -> "Figuras 2, 3 e 4"."""
    if len(nums) == 1:
        return f"Figura {nums[0]}"
    return "Figuras " + ", ".join(map(str, nums[:-1])) + f" e {nums[-1]}"


def bloco_figuras(nomes: list[str], num: Numerador) -> str:
    """Um bloco de marcadores de figura seguidos: uma frase de chamada e as figuras novas, com legenda."""
    novas, vistas = [], []
    for nome in nomes:
        n, primeira = num.figura(nome)
        (novas if primeira else vistas).append((n, nome))
    frases = []
    if novas:
        verbo = "mostra" if len(novas) == 1 else "mostram"
        frases.append(f"A{'s' if len(novas) > 1 else ''} {lista_pt([n for n, _ in novas])} {verbo} estes resultados.")
    if vistas:
        frases.append(f"Ver também a{'s' if len(vistas) > 1 else ''} {lista_pt([n for n, _ in vistas])}.")
    out = [" ".join(frases)]
    for n, nome in novas:
        out.append(f"![]({FIGURAS}/{nome}.png){{width=100%}}\n\n**Figura {n}.** {LEGENDAS[nome]}")
    return "\n\n".join(out)


def substituir_marcadores(texto: str, num: Numerador) -> str:
    texto = INCLUIR.sub(lambda m: tabela_gerada(m["nome"], num), texto)
    # Figuras seguidas no mesmo bloco: uma só frase de chamada no início.
    return BLOCO_FIGURAS.sub(lambda m: bloco_figuras(FIGURA.findall(m.group(0)), num) + "\n\n", texto)


def tabela_resumo(num: Numerador) -> str:
    """Tabela 1: a tabela de 00_resumo_executivo.md (caso, problema, biomateriais e proposta)."""
    linhas = [l for l in ler("00_resumo_executivo.md").splitlines() if l.startswith("|")]
    n = num.nova_tabela()
    return (f"A Tabela {n} resume, para cada caso, o problema do material atual, os biomateriais comparados e a "
            f"proposta.\n\n**Tabela {n}.** Resumo dos casos.\n\n" + "\n".join(linhas))


def base_norma(n: str) -> str:
    """Código da norma sem a edição (ASTM F2182-19e2 -> ASTM F2182; ISO 7206-4:2010 -> ISO 7206-4)."""
    if n.startswith("ASTM"):
        return re.sub(r"-\d{2}(?:e\d)?(?:\(\d{4}\))?$", "", n)
    return re.sub(r":\d{4}$", "", n)


def normas(texto: str) -> list[str]:
    """Normas ISO e ASTM citadas, por ordem alfabética, sem repetições (listas "ASTM F1, F2" separadas).

    Quando a mesma norma aparece com e sem edição, fica só a forma com edição.
    """
    out = set()
    for m in NORMA.finditer(texto):
        partes = [p.strip().rstrip(".") for p in m.group(0).split(",")]
        org = partes[0].split()[0]
        out.add(partes[0])
        out.update(f"{org} {p}" for p in partes[1:])
    com_edicao = {base_norma(n) for n in out if base_norma(n) != n}
    final = [n for n in out if base_norma(n) != n or n not in com_edicao]
    return sorted(final, key=lambda s: (s.split()[0], [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]))


YAML = """---
title: "Qual é o biomaterial ideal?"
subtitle: "Seleção multicritério de biomateriais com critérios-alvo e análise de robustez"
author:
  - "André Oliveira Massuça"
  - "Licenciatura em Engenharia Biomédica, Universidade Lusófona"
  - "UC Próteses e Órgãos Artificiais (docente: Prof. Pedro Sampaio), TP2"
date: "Outubro de 2026 (versão 0, para revisão)"
lang: pt-PT
toc: true
toc-depth: 2
toc-title: "Índice"
documentclass: article
fontsize: 11pt
geometry: margin=2.3cm
mainfont: "Libertinus Serif"
mathfont: "Libertinus Math"
linestretch: 1.15
colorlinks: true
abstract: |
{abstract}
---
"""


def montar() -> str:
    num = Numerador()
    resumo = sem_titulo(ler("resumo_rascunho.md"))
    corpo = [ler("introducao_rascunho.md") + "\n\n" + tabela_resumo(num),
             ler("metodos_rascunho.md"), ler("validacao_rascunho.md")]
    corpo += [renumerar_caso(ler(f), n) for f, n in CASOS]
    disc = ler("discussao_rascunho.md")
    disc = disc.replace("\n## 8.2", "\n\n<!-- figura: fig_e_resumo -->\n\n## 8.2", 1)
    corpo += [disc, ler("conclusao_rascunho.md")]
    texto = "\n\n".join(substituir_marcadores(c, num) for c in corpo)
    anexo_a = ler("anexo_a_equacoes.md")
    fim = "\n\n".join([anexo_a, ler("glossario.md"), ler("declaracao_ia_rascunho.md")])
    refs = vr.ler_referencias()
    numerado, ordem = vr.numerar(texto + "\n\n" + fim, refs)
    texto, fim = numerado.split("\n\n# Anexo A", 1)
    fim = "# Anexo A" + fim
    lista = "\n".join(f"{i}. {refs[k]}" for i, k in enumerate(ordem, 1))
    lista_normas = "\n".join(f"- {n}" for n in normas(texto + fim))
    anexo_b = "\n".join(l for l in ler("tabelas/anexo_b_dados.md").splitlines() if not l.startswith("<!--"))
    anexo_b = re.sub(r"^## (.+)$", lambda m, c=iter(range(1, 20)): f"## B.{next(c)} {m.group(1)}", anexo_b,
                     flags=re.M)
    anexo_a, resto = fim.split("\n\n# Glossário", 1)
    partes = [YAML.format(abstract="\n".join("  " + l for l in resumo.splitlines())), texto,
              "# Referências\n\n" + lista, "# Normas citadas\n\n" + lista_normas,
              anexo_a, anexo_b, "# Glossário" + resto]
    return "\n\n".join(partes) + "\n"


def main() -> None:
    destino = REL / "RELATORIO.md"
    destino.write_text(montar(), encoding="utf-8")
    print(destino)


if __name__ == "__main__":
    main()
