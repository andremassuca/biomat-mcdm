"""Verifica as citações do relatório contra a lista única de referências (relatorio/referencias.md).

Uma citação no texto tem a forma "Apelido [et al.|e Apelido|& Apelido] AAAA" (ex.: "Higuchi et al. 2019",
"Hu e Yoon 2018", "NJR 2026"); a chave correspondente é "Apelido AAAA" (apelido do primeiro autor ou
entidade). Mostra as citações sem referência e as referências que nenhum texto cita.
Também numera as citações pela ordem da primeira ocorrência (estilo Vancouver), para a montagem do
relatório (scripts/montar_relatorio.py).
Uso: python scripts/verificar_referencias.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REFERENCIAS = RAIZ / "relatorio" / "referencias.md"
# Textos do relatório, pela ordem em que entram no RELATORIO.md.
TEXTOS = ["resumo_rascunho.md", "introducao_rascunho.md", "metodos_rascunho.md", "validacao_rascunho.md",
          "caso_anca_rascunho.md", "caso_stent_rascunho.md", "caso_scaffold_rascunho.md",
          "caso_dentario_rascunho.md", "discussao_rascunho.md", "conclusao_rascunho.md",
          "anexo_a_equacoes.md", "glossario.md", "declaracao_ia_rascunho.md"]

_NOME = r"[A-ZÁÉÍÓÚÂÊÔÃÕÇÅÖÜ][\w'’\-]+"
CITACAO = re.compile(rf"\b(?P<nome>{_NOME})(?P<meio> et al\.,?| e {_NOME}| & {_NOME})?,? (?P<ano>(?:19|20)\d\d)\b")
ENTRADA = re.compile(r"^- \[(?P<chave>[^\]]+)\] (?P<texto>.+)$")


def ler_referencias(caminho: Path = REFERENCIAS) -> dict[str, str]:
    """Entradas da lista única: {chave: texto da referência}."""
    out = {}
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        m = ENTRADA.match(linha)
        if m:
            out[m["chave"]] = m["texto"]
    return out


def citacoes(texto: str, chaves: set[str] | None = None) -> list[str]:
    """Chaves citadas num texto, pela ordem da primeira ocorrência e sem repetições.

    Em linguagem simples: procura "Apelido (et al.) ano" e devolve "Apelido ano". Com `chaves`,
    só conta as que estão na lista ou que têm "et al." ou um segundo autor (para não confundir
    nomes próprios seguidos de um ano, como "Absorb 2017", com citações).
    """
    vistas = []
    for m in CITACAO.finditer(texto):
        k = f"{m['nome']} {m['ano']}"
        if chaves is not None and k not in chaves and not m["meio"]:
            continue
        if k not in vistas:
            vistas.append(k)
    return vistas


def verificar(pasta: Path = RAIZ / "relatorio", referencias: Path = REFERENCIAS) -> tuple[list[str], list[str]]:
    """Devolve (citações sem referência, referências não citadas)."""
    refs = ler_referencias(referencias)
    citadas = []
    for nome in TEXTOS:
        p = pasta / nome
        if p.exists():
            for k in citacoes(p.read_text(encoding="utf-8"), set(refs)):
                if k not in citadas:
                    citadas.append(k)
    sem_ref = [k for k in citadas if k not in refs]
    nao_citadas = sorted(k for k in refs if k not in citadas)
    return sem_ref, nao_citadas


def numerar(texto: str, refs: dict[str, str]) -> tuple[str, list[str]]:
    """Substitui o ano de cada citação pelo número [n] da referência, por ordem de primeira citação.

    Ex.: "Higuchi et al. 2019" passa a "Higuchi et al. [3]". Devolve o texto e a ordem das chaves.
    Citações sem entrada na lista ficam como estão.
    """
    ordem: list[str] = []

    def troca(m: re.Match) -> str:
        k = f"{m['nome']} {m['ano']}"
        if k not in refs:
            return m.group(0)
        if k not in ordem:
            ordem.append(k)
        return f"{m['nome']}{m['meio'] or ''} [{ordem.index(k) + 1}]"

    return CITACAO.sub(troca, texto), ordem


def main() -> int:
    sem_ref, nao_citadas = verificar()
    print(f"Citações sem referência ({len(sem_ref)}):")
    print("\n".join(f"  - {k}" for k in sem_ref) or "  nenhuma")
    print(f"Referências não citadas ({len(nao_citadas)}):")
    print("\n".join(f"  - {k}" for k in nao_citadas) or "  nenhuma")
    return 1 if sem_ref else 0


if __name__ == "__main__":
    sys.exit(main())
