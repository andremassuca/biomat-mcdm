"""Export só de dados de um caso quantitativo (stent ou scaffold), para levar ao chat.

Lê data/, src/ e results/ (sem os alterar) e grava relatorio/apoio/<caso>_export.md com:
candidatos, critérios, valores, rankings, robustez, triagem, valores a verificar (results/por_verificar.md),
notas metodológicas e apoio existente. Com --partes, divide também em partes numeradas até ~12 KB.

Uso: python scripts/exportar_caso.py stent|scaffold [--partes]
"""
from __future__ import annotations

import argparse
import re
import subprocess
from datetime import date
from pathlib import Path

import pandas as pd

from biomat_mcdm.io import DATA, build_problem, load_data
from biomat_mcdm.pipeline import rank_all_methods
from biomat_mcdm.screening import screen_case

ROOT = Path(__file__).resolve().parents[1]
APOIO = ROOT / "relatorio" / "apoio"
CASOS = {
    "stent": {"nome": "Stent vascular", "titulo": "Stent vascular", "chave": "Stent",
              "cenarios": ("A", "B", "B-bio"), "tecido": None,
              "notas": r"[Ss]tent|reabsor|σy/E|níquel|Nitinol|Tipo de expansão"},
    "scaffold": {"nome": "Scaffold (regeneração óssea)", "titulo": "Scaffold ósseo", "chave": "Scaffold",
                 "cenarios": ("A", "B"), "tecido": "Osso trabecular",
                 "notas": r"[Ss]caffold|porosidade|T-scaffold|β-TCP|trabecular"},
}
LIMITE_PARTE = 11500  # bytes


def fmt(x, casas: int = 4) -> str:
    """Número com vírgula decimal e sem zeros inúteis; vazio para NaN."""
    return "" if pd.isna(x) else f"{round(float(x), casas):g}".replace(".", ",")


def txt(x) -> str:
    """Texto seguro para uma célula de tabela Markdown."""
    return "" if pd.isna(x) else str(x).replace("|", ";").replace("\n", " ")


def aplica(casos: str, chave: str) -> bool:
    """True se a coluna 'casos' de cenarios.csv abrange o caso."""
    return casos in ("Todos", "Todos os quantitativos") or chave.lower() in str(casos).lower()


def seccao_md(texto: str, titulo: str) -> str:
    """Conteúdo da secção '## titulo' de um Markdown (até à secção seguinte), com subtítulos rebaixados."""
    m = re.search(rf"\n## {re.escape(titulo)}\n(.*?)(?=\n## |\Z)", texto, re.S)
    return "" if m is None else m.group(1).strip().replace("\n### ", "\n#### ")


def gerar(caso: str, data_dir: Path = DATA, root: Path = ROOT) -> str:
    """Texto Markdown do export de um caso ("stent" ou "scaffold")."""
    cfg = CASOS[caso]
    nome = cfg["nome"]
    mat, crit = load_data(data_dir)
    m = mat[mat["caso_componente"] == nome]
    c = crit[crit["caso_componente"] == nome]
    probs = {cen: build_problem(nome, cen, data_dir) for cen in cfg["cenarios"]}
    aprov, reg = screen_case(nome, data_dir)
    materiais = list(dict.fromkeys(m["material"]))
    commit = subprocess.run(["git", "log", "-1", "--format=%h"], cwd=root, capture_output=True,
                            text=True).stdout.strip()

    L = [f"# {cfg['titulo']}: export de dados (commit {commit}, {date.today():%d/%m/%Y})", "",
         "Gerado por scripts/exportar_caso.py a partir de data/, src/ e results/. Só dados.", ""]
    cab_cen = " | ".join(cfg["cenarios"])
    L += ["## 1. Candidatos", "", f"| Material | Norma | Classe | Estatuto | Triagem | {cab_cen} |",
          "|---|---|---|---|---|" + "---|" * len(cfg["cenarios"])]
    for a in materiais:
        r = m[m["material"] == a].iloc[0]
        cols = " | ".join("sim" if a in p.alternatives else "" for p in probs.values())
        L.append(f"| {a} | {txt(r['norma'])} | {txt(r['classe'])} | {txt(r['estatuto'])} | "
                 f"{'aprovado' if a in aprov else 'eliminado'} | {cols} |")
    cen = pd.read_csv(data_dir / "cenarios.csv")
    L += ["", "Cenários aplicáveis (cenarios.csv):", ""]
    L += [f"- {r.cenario}: {txt(r.descricao)}" for r in cen.itertuples() if aplica(r.casos, cfg["chave"])]
    L.append("")

    L += ["## 2. Critérios (criterios.csv)", "", "| Critério | Tipo | Alvo | Unidade | Peso | Justificação |",
          "|---|---|---|---|---|---|"]
    L += [f"| {r.criterio} | {r.tipo} | {txt(r.alvo)} | {txt(r.unidade)} | {fmt(r.peso)} | {txt(r.justificacao)} |"
          for r in c.itertuples()]
    for cn in ("A", "B"):
        p = probs[cn]
        L.append(f"\nPesos no cenário {cn} (renormalizados): " +
                 "; ".join(f"{k} {fmt(w, 3)}" for k, w in zip(p.criteria, p.weights)))
    if cfg["tecido"]:
        tec = pd.read_csv(data_dir / "tecido.csv")
        tec = tec[tec["tecido"] == cfg["tecido"]]
        L += ["", f"Referência de tecido (tecido.csv, {cfg['tecido'].lower()}):", "",
              "| Propriedade | Unidade | Mín. | Máx. | Fonte | Estado |", "|---|---|---|---|---|---|"]
        L += [f"| {r.propriedade} | {r.unidade} | {fmt(r.min)} | {fmt(r.max)} | {txt(r.fonte)} | {txt(r.estado)} |"
              for r in tec.itertuples()]
    L.append("")

    L += ["## 3. Valores (materiais.csv e índices derivados)", "",
          "| Material | Propriedade | Unidade | Típico | Mín. | Máx. | Texto | Fonte | doi_url | Estado |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in m.sort_values(["propriedade", "material"]).itertuples():
        L.append(f"| {r.material} | {r.propriedade} | {txt(r.unidade)} | {fmt(r.tipico)} | {fmt(r.min)} | "
                 f"{fmt(r.max)} | {txt(r.valor_texto)} | {txt(r.referencia)} | {txt(r.doi_url)} | {txt(r.estado)} |")
    L += ["", f"Linhas: {len(m)}; estados: " + "; ".join(f"{k} {v}" for k, v in m["estado"].value_counts().items()), ""]

    L += ["## 4. Rankings (η = 1)", ""]
    for cn, p in probs.items():
        df = rank_all_methods(p).sort_values("pos_TOPSIS")
        cs = df["C_TOPSIS"].sort_values(ascending=False).to_numpy()
        L += [f"### Cenário {cn}", "", "Critérios: " + "; ".join(p.criteria), "",
              "| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |", "|---|---|---|---|"]
        L += [f"| {r.material} | {fmt(r.C_TOPSIS, 3)} ({r.pos_TOPSIS}) | {fmt(r.Q_WASPAS, 3)} ({r.pos_WASPAS}) | "
              f"{fmt(r.P_VIKOR, 3)} ({r.pos_VIKOR}) |" for r in df.itertuples()]
        L += ["", f"ΔC 1.º-2.º (TOPSIS) = {fmt(cs[0] - cs[1], 3)} (regra: < 0,01 = empate)", ""]

    res = (root / "results" / "resumo_robustez.md").read_text(encoding="utf-8")
    cab = res.split("\n## ")[0].strip().splitlines()[-1]
    L += ["## 5. Robustez (results/resumo_robustez.md)", "", cab, "", seccao_md(res, cfg["chave"]), ""]

    L += ["## 6. Triagem (critérios estritos)", "", "| Material | Critério | Regra | Valor | Resultado | Motivo |",
          "|---|---|---|---|---|---|"]
    L += [f"| {r.material} | {r.criterio} | {txt(r.regra)} | {txt(r.valor)} | {r.resultado} | {txt(r.motivo)} |"
          for r in reg.itertuples()]
    L.append("")

    pv = root / "results" / "por_verificar.md"
    if pv.exists():
        L += ["## 7. Valores \"A verificar\" por influência (results/por_verificar.md)", "",
              seccao_md(pv.read_text(encoding="utf-8"), cfg["chave"]), ""]

    notas = (root / "docs" / "NOTAS_METODOLOGICAS.md").read_text(encoding="utf-8").splitlines()
    leia = (data_dir / "leia_me.md").read_text(encoding="utf-8").splitlines()
    L += ["## 8. Notas (linhas literais de docs/NOTAS_METODOLOGICAS.md e data/leia_me.md)", ""]
    L += [l for l in notas if re.search(cfg["notas"], l)]
    L += ["", "leia_me.md:", ""] + [l for l in leia if re.search(cfg["notas"], l)]
    L.append("")

    L += ["## 9. Apoio já existente", "", "Linhas que referem o caso noutros ficheiros:", ""]
    for rel in ["relatorio/00_resumo_executivo.md", "docs/TP2_fisiopatologia_da_falha.md",
                "docs/TP2_guia_de_fontes.md", "docs/backlog_artigo.md"]:
        f = root / rel
        if f.exists():
            n = [str(k + 1) for k, l in enumerate(f.read_text(encoding="utf-8").splitlines())
                 if re.search(cfg["chave"], l, re.IGNORECASE)]
            if n:
                L.append(f"- {rel}: linhas {', '.join(n)}")
    L.append("")
    return "\n".join(L)


def dividir(texto: str, limite: int = LIMITE_PARTE) -> list[str]:
    """Divide o Markdown em partes até ~limite bytes, sem separar o cabeçalho de uma tabela da sua
    primeira linha (se cortar a meio de uma tabela, repete o cabeçalho na parte seguinte)."""
    linhas = texto.split("\n")
    partes, atual, tam, cab = [], [], 0, None
    for i, l in enumerate(linhas):
        if l.startswith("| ") and i + 1 < len(linhas) and linhas[i + 1].startswith("|---"):
            cab = [l, linhas[i + 1]]
        nb = len(l.encode("utf-8")) + 1
        pode = not l.startswith("|---") and not (atual and atual[-1].startswith("|---"))
        if tam + nb > limite and pode and atual:
            partes.append(atual)
            atual, tam = [], 0
            if l.startswith("| ") and cab and l != cab[0]:
                atual = ["(continuação da tabela)", ""] + cab
                tam = sum(len(x.encode("utf-8")) + 1 for x in atual)
        atual.append(l)
        tam += nb
    partes.append(atual)
    n = len(partes)
    return [f"[Parte {k} de {n}]\n\n" + "\n".join(p) + "\n" for k, p in enumerate(partes, 1)]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("caso", choices=sorted(CASOS))
    ap.add_argument("--partes", action="store_true", help="grava também as partes numeradas")
    a = ap.parse_args()
    texto = gerar(a.caso)
    APOIO.mkdir(parents=True, exist_ok=True)
    out = APOIO / f"{a.caso}_export.md"
    out.write_text(texto, encoding="utf-8")
    print(out, out.stat().st_size, "bytes")
    if a.partes:
        for k, p in enumerate(dividir(texto), 1):
            f = APOIO / f"{a.caso}_export_parte{k}.md"
            f.write_text(p, encoding="utf-8")
            print(f, f.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
