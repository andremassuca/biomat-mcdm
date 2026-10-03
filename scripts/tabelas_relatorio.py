"""Gera as tabelas do relatório a partir de data/ e de results/, para baterem sempre com os resultados.

Para cada caso (haste, par articular, stent, scaffold, implante dentário):
  relatorio/tabelas/<chave>_criterios.md    critério, tipo, alvo, peso e justificação (criterios.csv)
  relatorio/tabelas/<chave>_resultados.md   pontuação e posição nos três métodos, cenários A e B, com o ΔC
  relatorio/tabelas/<chave>_robustez.md     Monte Carlo, η e P-foco em frases curtas geradas dos resultados
Os casos quantitativos leem results/pontuacoes.csv, results/monte_carlo.csv e results/rankings_cenarios.csv
(correr antes scripts/run_all.py); os semiquantitativos calculam as pontuações com as mesmas funções e
leem results/semiquantitativos.csv.
Uso: python scripts/tabelas_relatorio.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from biomat_mcdm.io import DATA, build_problem
from biomat_mcdm.pipeline import METODOS, fmt_pt, rank_all_methods

RAIZ = Path(__file__).resolve().parents[1]
RESULTS = RAIZ / "results"
DESTINO = RAIZ / "relatorio" / "tabelas"
LIMIAR_EMPATE = 0.01  # ΔC (TOPSIS) abaixo do qual dois materiais contam como empatados

# chave: (nome em criterios.csv, nome em results/, quantitativo?)
CASOS = {
    "haste": ("Prótese da anca | Haste femoral", "Haste", True),
    "par": ("Prótese da anca | Par articular", "Par articular", False),
    "stent": ("Stent vascular", "Stent", True),
    "scaffold": ("Scaffold (regeneração óssea)", "Scaffold", True),
    "dentario": ("Implante dentário", "Implante dentário", False),
}
TIPOS = {"Benefício": "benefício", "Custo": "custo", "Alvo": "alvo", "Estrito": "eliminatório"}
SCORE = {"TOPSIS": ("C_TOPSIS", False), "WASPAS": ("Q_WASPAS", False), "VIKOR": ("P_VIKOR", True)}


def num(x: float | str, casas: int = 3) -> str:
    """Número em português (vírgula decimal); texto e vazios passam como estão."""
    if isinstance(x, str) or pd.isna(x):
        return "" if pd.isna(x) else x
    return fmt_pt(float(x), casas)


def pct(v: float) -> str:
    """Percentagem com uma casa, ou duas quando a uma casa arredondaria para 0 ou 100 sem o ser."""
    casas = 2 if (99.95 <= v < 100) or (0 < v < 0.05) else 1
    return f"{fmt_pt(v, casas)} %"


def md(df: pd.DataFrame) -> str:
    """Tabela em Markdown (cabeçalho, separador e linhas), sem dependências externas."""
    linhas = ["| " + " | ".join(df.columns) + " |", "|" + "---|" * len(df.columns)]
    linhas += ["| " + " | ".join(str(v) for v in r) + " |" for r in df.itertuples(index=False)]
    return "\n".join(linhas)


def tabela_criterios(caso: str, data_dir: Path = DATA) -> pd.DataFrame:
    """Critérios de um caso como estão em criterios.csv, com o tipo por extenso.

    Em linguagem simples: a tabela "Candidatos e critérios" do relatório; os critérios
    eliminatórios aparecem sem peso, porque só servem para a triagem.
    """
    c = pd.read_csv(data_dir / "criterios.csv")
    c = c[c["caso_componente"] == caso]
    peso = c["peso"].map(lambda p: "" if pd.isna(p) else fmt_pt(float(p), 2))
    alvo = [("" if pd.isna(a) else f"{a} {u}".replace(" -", "").strip()) for a, u in zip(c["alvo"], c["unidade"])]
    return pd.DataFrame({"Critério": c["criterio"].to_numpy(), "Tipo": c["tipo"].map(TIPOS).to_numpy(),
                         "Alvo": alvo, "Peso": peso.to_numpy(),
                         "Justificação": c["justificacao"].fillna("").to_numpy()})


def nota_pesos(caso: str, data_dir: Path = DATA) -> str:
    """Nota sob a tabela quando os pesos do cenário A não somam 1 (critérios só do cenário B)."""
    c = pd.read_csv(data_dir / "criterios.csv")
    c = c[(c["caso_componente"] == caso) & (c["tipo"] != "Estrito")]
    so_b = c["criterio"].str.contains("só cenário B")
    soma_a = c.loc[~so_b, "peso"].sum()
    if abs(soma_a - 1) < 1e-9:
        return ""
    return (f"\n\nPesos da base de dados. No cenário A, sem os critérios só do cenário B, somam "
            f"{fmt_pt(soma_a, 2)} e são renormalizados para somar 1.")


def pontuacoes(chave: str, data_dir: Path = DATA, results: Path = RESULTS) -> pd.DataFrame:
    """Pontuações e posições nos cenários A e B (quantitativos: de results/pontuacoes.csv)."""
    caso, rotulo, quant = CASOS[chave]
    if quant:
        pt = pd.read_csv(results / "pontuacoes.csv")
        return pt[pt["caso"] == rotulo].reset_index(drop=True)
    partes = [rank_all_methods(build_problem(caso, cen, data_dir)).assign(caso=rotulo, cenario=cen)
              for cen in ("A", "B")]
    return pd.concat(partes, ignore_index=True)


def delta_c(pt: pd.DataFrame, cenario: str) -> float:
    """Diferença de C (TOPSIS) entre o 1.º e o 2.º lugar num cenário."""
    c = pt[pt["cenario"] == cenario]["C_TOPSIS"].sort_values(ascending=False).to_numpy()
    return float(c[0] - c[1])


def tabela_resultados(pt: pd.DataFrame) -> pd.DataFrame:
    """Uma linha por cenário e material, ordenada pela posição no TOPSIS."""
    linhas = []
    for cen, g in pt.groupby("cenario", sort=True):
        for r in g.sort_values("pos_TOPSIS").itertuples():
            linhas.append({"Cenário": cen, "Material": r.material,
                           "C (TOPSIS)": num(r.C_TOPSIS), "Pos. T": r.pos_TOPSIS,
                           "Q (WASPAS)": num(r.Q_WASPAS), "Pos. W": r.pos_WASPAS,
                           "P (VIKOR)": num(r.P_VIKOR), "Pos. V": r.pos_VIKOR})
    return pd.DataFrame(linhas)


def frase_delta(pt: pd.DataFrame) -> str:
    """Frase com o ΔC de cada cenário e a indicação de empate."""
    partes = []
    for cen in sorted(pt["cenario"].unique()):
        d = delta_c(pt, cen)
        partes.append(f"cenário {cen}: ΔC = {fmt_pt(d, 3)}" + (" (empate, abaixo de 0,01)" if d < LIMIAR_EMPATE else ""))
    return "Diferença de C entre o 1.º e o 2.º no TOPSIS: " + "; ".join(partes) + "."


def vencedor(g: pd.DataFrame) -> str:
    return " = ".join(sorted(g[g["posicao"] == 1]["material"]))


def gama_eta(eta: pd.DataFrame, vencedor_base: str) -> str:
    """Valores de η em que o vencedor de um método difere do vencedor com η = 1, em forma compacta."""
    vals = sorted(float(v.replace("η = ", "").replace(",", ".")) for v, g in eta.groupby("variante")
                  if vencedor(g) != vencedor_base)
    if not vals:
        return "nunca"
    passo = [round(0.1 * k, 1) for k in range(len(vals))]
    if vals == passo:
        return "η = 0" if len(vals) == 1 else f"η de 0 a {fmt_pt(vals[-1], 1)}"
    return ", ".join(f"η = {fmt_pt(v, 1)}" for v in vals)


def robustez_linhas(chave: str, results: Path = RESULTS) -> list[str]:
    """Frases curtas, geradas dos resultados, para a secção "Robustez" de cada caso."""
    caso, rotulo, quant = CASOS[chave]
    L = []
    if quant:
        mc = pd.read_csv(results / "monte_carlo.csv")
        mc = mc[(mc["caso"] == rotulo) & (mc["analise"] == "MC propriedades")]
        piv = mc.pivot(index="material", columns="metodo", values="pct_primeiro")[METODOS]
        piv = piv[piv.max(axis=1) >= 1].sort_values("TOPSIS", ascending=False)
        n = f"{int(mc['n_iter'].iloc[0]):,}".replace(",", " ")
        L.append(f"- Monte Carlo das propriedades ({n} iterações, cenário A), % de 1.º lugar (TOPSIS / WASPAS / VIKOR): "
                 + "; ".join(f"{a} {' / '.join(pct(v) for v in row)}" for a, row in piv.iterrows()) + ".")
        rk = pd.read_csv(results / "rankings_cenarios.csv")
        rk = rk[rk["caso"] == rotulo]
        base = {m: vencedor(rk[(rk["cenario"] == "A") & (rk["metodo"] == m)]) for m in METODOS}
        eta = rk[rk["cenario"] == "η"]
        partes = [f"{m}: {gama_eta(eta[eta['metodo'] == m], base[m])}" for m in METODOS]
        L.append("- Combinação com pesos objetivos (η de 0 a 1; η = 1 é o resultado principal), η em que o "
                 "vencedor muda: " + "; ".join(partes) + ".")
        foco = rk[rk["cenario"] == "P-foco"]
    else:
        foco = pd.read_csv(results / "semiquantitativos.csv")
        foco = foco[(foco["caso"] == rotulo) & (foco["cenario"] != "A")]
        L.append("- Caso SEMIQUANTITATIVO (escalas ordinais com mais de 50 % do peso): o ranking é uma indicação.")
    for (cen, var), g in foco.groupby(["cenario", "variante"], sort=False):
        rot = f"P-foco ({var})" if cen == "P-foco" else f"Sensibilidade ({var})"
        L.append(f"- {rot}: " + "; ".join(f"{m} {vencedor(g[g['metodo'] == m])}" for m in METODOS) + ".")
    return L


def gerar(destino: Path = DESTINO, data_dir: Path = DATA, results: Path = RESULTS) -> list[Path]:
    """Escreve as três tabelas de cada caso; devolve os caminhos."""
    destino.mkdir(parents=True, exist_ok=True)
    feitos = []
    for chave, (caso, _, quant) in CASOS.items():
        pt = pontuacoes(chave, data_dir, results)
        aviso = "" if quant else "\n\nSEMIQUANTITATIVO: escalas ordinais com mais de 50 % do peso; o ranking é uma indicação."
        textos = {"criterios": md(tabela_criterios(caso, data_dir)) + nota_pesos(caso, data_dir),
                  "resultados": md(tabela_resultados(pt)) + "\n\n" + frase_delta(pt) + aviso,
                  "robustez": "\n".join(robustez_linhas(chave, results))}
        for nome, texto in textos.items():
            p = destino / f"{chave}_{nome}.md"
            p.write_text(f"<!-- gerado por scripts/tabelas_relatorio.py; não editar à mão -->\n{texto}\n", encoding="utf-8")
            feitos.append(p)
    return feitos


if __name__ == "__main__":
    for p in gerar():
        print(p)
