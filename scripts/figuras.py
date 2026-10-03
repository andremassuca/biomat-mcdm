"""Figuras dos três casos quantitativos, para o relatório e o poster A0.

Lê só ficheiros já gerados: data/materiais.csv e data/tecido.csv (figura a) e
results/rankings_cenarios.csv, results/pontuacoes.csv e results/monte_carlo.csv (as outras).
Não recalcula nenhum método: correr primeiro scripts/run_all.py.

Gera em results/figures/ (PNG a 300 dpi e SVG):
  fig_a_rigidez_haste          barras E_implante/E_osso com a faixa do osso cortical
  fig_b_posicoes               posição por método, três casos, cenários A e B
  fig_c_monte_carlo            % de 1.º lugar no Monte Carlo de propriedades, por método
  fig_c2_monte_carlo_completo  % de 1.º, 2.º e 3.º lugar (anexo)
  fig_d_vencedor_eta           vencedor em função de η, por método
  fig_e_resumo                 uma linha por caso: vencedor, Monte Carlo e o que o muda
Uso: python scripts/figuras.py
"""
from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "biomat-mcdm"  # identificadores fixos: SVG igual a cada execução
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgba
from matplotlib.patches import Patch, Rectangle
import pandas as pd

from biomat_mcdm.indices import stiffness_ratio
from biomat_mcdm.io import DATA
from biomat_mcdm.pipeline import METODOS, fmt_pt

RESULTS = Path(__file__).resolve().parents[1] / "results"
NOTA = "Preliminar: dados em verificação"
CASOS = {"Haste": "Haste femoral", "Stent": "Stent", "Scaffold": "Scaffold ósseo"}
TEXTO, TEXTO_2, GRELHA = "#0b0b0b", "#52514e", "#d9d8d4"
F_TITULO, F_SUB, F_EIXO, F_NOTA = 18, 14, 14, 11
LIMIAR_EMPATE = 0.01  # diferença de C no TOPSIS abaixo da qual duas posições contam como empate
RAMPA = LinearSegmentedColormap.from_list("azul", ["#1f5fb0", "#dbe8f7"])
TONS_LUGAR = {"pct_primeiro": "#1f5fb0", "pct_segundo": "#7fa8d9", "pct_terceiro": "#dbe8f7"}
NOME_LUGAR = {"pct_primeiro": "1.º lugar", "pct_segundo": "2.º lugar", "pct_terceiro": "3.º lugar"}
COR_METODO = {"TOPSIS": "#222222", "WASPAS": "#7d7d7d", "VIKOR": "#c4c4c4"}

# Paleta fixa por material (Okabe e Ito, segura para daltónicos), igual em todas as figuras.
# Dentro de cada caso não há duas cores iguais; o 316L tem a mesma cor na haste e no stent.
AZUL, LARANJA, VERDE, CINZA = "#0072B2", "#E69F00", "#009E73", "#999999"
CEU, VERMELHAO, ROSA, AMARELO = "#56B4E9", "#D55E00", "#CC79A7", "#F0E442"
COR_MATERIAL = {
    "Haste": {"Ti-6Al-4V ELI": AZUL, "Co-Cr-Mo forjado": LARANJA, "Ti-13Nb-13Zr": VERDE,
              "Aço inox 316L": CINZA, "Ti cp grau 4": AMARELO, "Ti-35Nb-7Zr-5Ta (TNZT)": ROSA},
    "Stent": {"Pt-Cr": AZUL, "Co-Cr L605": LARANJA, "Co-Ni-Cr-Mo MP35N": VERDE,
              "Aço inox 316L": CINZA, "Liga de Mg WE43 (bioabsorvível)": VERMELHAO,
              "PLLA (bioabsorvível)": ROSA, "Nitinol (autoexpansível)": AMARELO},
    "Scaffold": {"β-TCP poroso": AZUL, "Compósito PCL/β-TCP (impressão 3D)": LARANJA,
                 "Vidro bioativo 45S5 poroso": VERDE, "Quitosano/HA (liofilizado)": CINZA,
                 "PCL": CEU, "Hidroxiapatite (HA) porosa": VERMELHAO, "PLLA": ROSA,
                 "PLGA 50:50": AMARELO},
}
# Nomes curtos para os eixos e, mais curtos ainda, para caber dentro de uma célula
ABREVIA = {" (bioabsorvível)": "", " (liofilizado)": "", "Liga de ": "", " (impressão 3D)": "",
           "Compósito ": "", " (autoexpansível)": "", "Hidroxiapatite (HA)": "HA"}
ABREVIA_CELULA = {"Ti-6Al-4V ELI": "Ti-6Al-4V", "Ti cp grau 4": "Ti cp", "Aço inox 316L": "316L",
                  "Co-Cr L605": "L605", "Co-Cr-Mo forjado": "Co-Cr-Mo", "Co-Ni-Cr-Mo MP35N": "MP35N",
                  "β-TCP poroso": "β-TCP", "Compósito PCL/β-TCP (impressão 3D)": "PCL/β-TCP",
                  "Vidro bioativo 45S5 poroso": "45S5"}
MUDA = {"B": "juntar os materiais em investigação", "Q": "tirar os critérios ordinais",
        "T-haste": "mudar o alvo do módulo", "T-scaffold": "mudar os alvos",
        "P-foco": "reforçar os critérios do problema crítico"}


def curto(material: str) -> str:
    """Nome do material sem os parênteses longos, para caber nos eixos."""
    for a, b in ABREVIA.items():
        material = material.replace(a, b)
    return material


def curto_celula(material: str) -> str:
    """Nome ainda mais curto, para escrever dentro de uma célula (empates: nomes com " = ")."""
    return " = ".join(ABREVIA_CELULA.get(m, curto(m)) for m in material.split(" = "))


def cor(caso: str, material: str) -> str:
    """Cor fixa do material; num empate usa a do primeiro nome."""
    return COR_MATERIAL[caso][material.split(" = ")[0]]


def cor_texto(rgba: tuple[float, ...]) -> str:
    """Texto branco sobre fundo escuro e preto sobre fundo claro (luminância relativa WCAG)."""
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgba[:3]]
    lum = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    return "white" if 1.05 / (lum + 0.05) > (lum + 0.05) / 0.05 else TEXTO


def limpar(ax: plt.Axes) -> None:
    """Estilo comum: sem moldura, marcas discretas."""
    for lado in ax.spines.values():
        lado.set_visible(False)
    ax.tick_params(colors=TEXTO_2, labelsize=F_EIXO, length=0)


def cabecalho(fig: plt.Figure, titulo: str, subtitulo: str, topo: float = 0.88) -> None:
    """Título com a conclusão, subtítulo técnico e nota de preliminar no canto inferior direito.

    `topo` é a fração da altura da figura onde acabam os gráficos (o resto fica para o cabeçalho).
    O título pode ter várias linhas (separadas por "\n"); o subtítulo desce em conformidade.
    """
    linhas_extra = titulo.count("\n")
    fig.tight_layout(rect=(0, 0.035, 1, topo))
    fig.text(0.012, 0.985, titulo, fontsize=F_TITULO, fontweight="bold", color=TEXTO, va="top")
    fig.text(0.012, 0.985 - (F_TITULO + 10 + 1.25 * F_TITULO * linhas_extra) / 72 / fig.get_figheight(), subtitulo,
             fontsize=F_SUB, color=TEXTO_2, va="top")
    fig.text(0.99, 0.008, NOTA, fontsize=F_NOTA, color=TEXTO_2, ha="right", va="bottom", style="italic")


def dados_rigidez(data_dir: Path = DATA) -> tuple[pd.DataFrame, tuple[float, float], tuple[float, float]]:
    """Razão E_implante/E_osso de cada material da haste, a faixa do osso e o seu módulo (GPa).

    Em linguagem simples: a razão diz quantas vezes o implante é mais rígido do que o osso
    (1 = igual). A faixa é o intervalo do osso dividido pelo seu ponto médio, por isso fica
    à volta de 1. A coluna `investigacao` marca os materiais que ainda não têm uso clínico.
    """
    mat = pd.read_csv(data_dir / "materiais.csv")
    tec = pd.read_csv(data_dir / "tecido.csv")
    df = stiffness_ratio(mat, tec).sort_values("razao_tipica").reset_index(drop=True)
    estatuto = mat[mat["caso"] == "Prótese da anca"].drop_duplicates("material").set_index("material")["estatuto"]
    df["investigacao"] = df["material"].map(estatuto).str.contains("Investigação").to_numpy()
    osso = tec[(tec["tecido"] == "Osso cortical") & (tec["propriedade"] == "Módulo de Young")].iloc[0]
    meio = (osso["min"] + osso["max"]) / 2
    return df, (osso["min"] / meio, osso["max"] / meio), (float(osso["min"]), float(osso["max"]))


def dados_posicoes(rk: pd.DataFrame, caso: str, cenario: str) -> pd.DataFrame:
    """Tabela material x método com as posições de um caso e cenário, ordenada pelo TOPSIS."""
    g = rk[(rk["caso"] == caso) & (rk["cenario"] == cenario) & (rk["variante"] == cenario)]
    return g.pivot(index="material", columns="metodo", values="posicao")[METODOS].sort_values(METODOS)


def empates_topsis(pt: pd.DataFrame, caso: str, cenario: str, limiar: float = LIMIAR_EMPATE) -> set[str]:
    """Materiais cujo C do TOPSIS difere menos de `limiar` do material seguinte (e esse seguinte).

    Em linguagem simples: quando duas pontuações estão quase iguais, a ordem entre os dois
    materiais não é de confiar, e as duas células levam o sinal "=".
    """
    g = pt[(pt["caso"] == caso) & (pt["cenario"] == cenario)].sort_values("C_TOPSIS", ascending=False)
    nomes, c = g["material"].tolist(), g["C_TOPSIS"].to_numpy()
    fora = set()
    for i in range(len(c) - 1):
        if c[i] - c[i + 1] < limiar:
            fora |= {nomes[i], nomes[i + 1]}
    return fora


def frase_concordancia(t: pd.DataFrame) -> str:
    """Frase simples sobre a concordância dos três métodos (em vez do coeficiente de Spearman)."""
    if all(t[m].tolist() == t[METODOS[0]].tolist() for m in METODOS):
        return "Os três métodos dão a mesma ordem."
    if len({t[m].idxmin() for m in METODOS}) == 1:
        return "Mesmo vencedor nos três métodos; a ordem dos outros varia."
    return "Os métodos não concordam no 1.º lugar."


def dados_monte_carlo(mc: pd.DataFrame, caso: str, metodo: str) -> pd.DataFrame:
    """% de 1.º, 2.º e 3.º lugar de cada material no Monte Carlo de propriedades."""
    g = mc[(mc["caso"] == caso) & (mc["analise"] == "MC propriedades") & (mc["metodo"] == metodo)]
    return g.set_index("material")[list(TONS_LUGAR)].sort_values(list(TONS_LUGAR), ascending=False)


def dados_primeiro(mc: pd.DataFrame, caso: str) -> pd.DataFrame:
    """% de 1.º lugar por material (linhas) e método (colunas), ordenada pelo TOPSIS."""
    g = mc[(mc["caso"] == caso) & (mc["analise"] == "MC propriedades")]
    t = g.pivot(index="material", columns="metodo", values="pct_primeiro")[METODOS]
    return t.sort_values(METODOS, ascending=False)


def separar_zeros(t: pd.DataFrame, minimo: float = 0.5) -> tuple[pd.DataFrame, list[str]]:
    """Separa os materiais que nunca chegam ao 1.º lugar dos que chegam em pelo menos um método.

    Em linguagem simples: um material conta como "0 %" quando a percentagem arredonda a zero
    (menos de `minimo`) nos três métodos. Devolve a tabela dos outros e a lista dos nomes a zero.
    """
    fica = (t >= minimo).any(axis=1)
    return t[fica], t.index[~fica].tolist()


def dados_vencedor_eta(rk: pd.DataFrame, caso: str) -> pd.DataFrame:
    """Vencedor por método (linhas) e por valor de η (colunas, 0 a 1).

    Em linguagem simples: para cada η e cada método, o material que ficou em 1.º lugar.
    Se houver empate, os nomes aparecem juntos com " = ".
    """
    g = rk[(rk["caso"] == caso) & (rk["cenario"] == "η") & (rk["posicao"] == 1)].copy()
    g["eta"] = g["variante"].str.replace("η = ", "").str.replace(",", ".").astype(float)
    venc = g.groupby(["metodo", "eta"])["material"].apply(lambda s: " = ".join(sorted(s)))
    return venc.unstack("eta").loc[METODOS]


def vencedores(rk: pd.DataFrame, caso: str) -> pd.DataFrame:
    """Vencedor de cada (cenário, variante, método) de um caso."""
    g = rk[(rk["caso"] == caso) & (rk["posicao"] == 1)]
    return (g.groupby(["cenario", "variante", "metodo"], sort=False)["material"]
            .apply(lambda s: " = ".join(sorted(s))).reset_index())


def o_que_muda(rk: pd.DataFrame, caso: str) -> str:
    """Frase curta com os cenários de sensibilidade em que o vencedor do cenário A muda.

    Em linguagem simples: compara o 1.º lugar de cada método em cada cenário com o 1.º lugar
    desse método no cenário A e junta numa frase os cenários em que não coincidem. Entre
    parênteses ficam os métodos em que muda, quando não são os três.
    """
    v = vencedores(rk, caso)
    base = v[v["cenario"] == "A"].set_index("metodo")["material"]
    v = v[~v["cenario"].isin(["A", "B-bio", "R-sentinela"])]
    v = v[v["material"] != v["metodo"].map(base)]

    def metodos(g: pd.DataFrame) -> str:
        m = [x for x in METODOS if x in set(g["metodo"])]
        return "" if len(m) == len(METODOS) else f" ({', '.join(m)})"

    partes = []
    for cen, g in v.groupby("cenario", sort=False):
        if cen == "η":
            etas = g["variante"].str.replace("η = ", "").str.replace(",", ".").astype(float)
            partes.append(("η = 0" if etas.max() == 0 else f"η até {fmt_pt(etas.max(), 1)}") + metodos(g))
        elif cen == "C-custo":
            for var, h in g.groupby("variante", sort=False):
                partes.append(f"peso do {var.split(' (')[0]}" + metodos(h))
        else:
            partes.append(MUDA.get(cen, cen) + metodos(g))
    return "; ".join(partes) if partes else "nenhum cenário de sensibilidade"


def dados_resumo(rk: pd.DataFrame, mc: pd.DataFrame) -> pd.DataFrame:
    """Uma linha por caso: vencedores do cenário A, % de 1.º lugar no Monte Carlo e o que muda.

    `vencedores` é um dicionário material -> métodos em que ganha; `monte_carlo` é um
    dicionário material -> lista das três percentagens (TOPSIS, WASPAS, VIKOR).
    """
    linhas = []
    for caso in CASOS:
        v = vencedores(rk, caso)
        a = v[v["cenario"] == "A"]
        venc = {m: a[a["material"] == m]["metodo"].tolist() for m in dict.fromkeys(a["material"])}
        p = dados_primeiro(mc, caso)
        linhas.append({"caso": caso, "vencedores": venc,
                       "monte_carlo": {m: p.loc[m].tolist() for m in venc},
                       "muda": o_que_muda(rk, caso)})
    return pd.DataFrame(linhas)


def fig_rigidez(df: pd.DataFrame, faixa: tuple[float, float], osso: tuple[float, float]) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(13, 0.8 * len(df) + 3.6))
    ax.axvspan(*faixa, color="#f0d9a8", zorder=0)
    ax.text(faixa[1] + 0.12, -0.72, "osso", fontsize=F_EIXO, color="#8a5a00", va="center")
    for i, r in enumerate(df.itertuples()):
        c = cor("Haste", r.material)
        ax.barh(i, r.razao_tipica, height=0.62, zorder=2, color=to_rgba(c, 0.35 if r.investigacao else 1),
                edgecolor=c, linewidth=1.5, linestyle="--" if r.investigacao else "-",
                hatch="//" if r.investigacao else None)
        ax.text(r.razao_max + 0.2, i, f"×{fmt_pt(r.razao_tipica, 0)}", va="center", fontsize=F_EIXO + 2,
                color=TEXTO, fontweight="bold")
    ax.errorbar(df["razao_tipica"], range(len(df)), fmt="none", ecolor=TEXTO, elinewidth=1.4, capsize=5,
                xerr=[df["razao_tipica"] - df["razao_min"], df["razao_max"] - df["razao_tipica"]], zorder=3)
    ax.set_yticks(range(len(df)), [curto(m) for m in df["material"]])
    ax.set_ylim(len(df) - 0.5, -1.05)
    ax.set_xlim(0, df["razao_max"].max() * 1.1)
    ax.set_xlabel("E do implante / E do osso cortical (1 = igual ao osso)", fontsize=F_EIXO, color=TEXTO_2)
    ax.xaxis.grid(True, color=GRELHA, linewidth=0.8)
    ax.set_axisbelow(True)
    limpar(ax)
    if df["investigacao"].any():
        c = cor("Haste", df[df["investigacao"]]["material"].iloc[0])
        ax.legend(handles=[Patch(facecolor="none", edgecolor=c, hatch="//", linestyle="--", linewidth=1.5,
                                 label="em investigação")],
                  loc="upper right", frameon=False, fontsize=F_EIXO)
    lo, hi = fmt_pt(df["razao_tipica"].min(), 0), fmt_pt(df["razao_tipica"].max(), 0)
    cabecalho(fig, f"Todas as ligas são {lo} a {hi} vezes mais rígidas do que o osso cortical",
              f"Haste femoral: módulo de Young do implante a dividir pelo do osso cortical "
              f"({fmt_pt(osso[0], 0)}-{fmt_pt(osso[1], 0)} GPa).\n"
              "Barra: valor típico; traço: mínimo a máximo.",
              topo=0.87)
    return fig


def fig_posicoes(rk: pd.DataFrame, pt: pd.DataFrame) -> plt.Figure:
    tab = {(c, cen): dados_posicoes(rk, c, cen) for c in CASOS for cen in ("A", "B")}
    alt = [max(len(tab[c, cen]) for c in CASOS) for cen in ("A", "B")]
    fig, eixos = plt.subplots(2, 3, figsize=(21, 0.62 * sum(alt) + 5.5), height_ratios=alt)
    for i, cen in enumerate(("A", "B")):
        for j, caso in enumerate(CASOS):
            ax, t = eixos[i, j], tab[caso, cen]
            n, pos = len(t), t.to_numpy()
            iguais = empates_topsis(pt, caso, cen)
            ax.imshow(pos, cmap=RAMPA, vmin=1, vmax=max(n, 2), aspect="auto")
            for a in range(n):
                for b in range(3):
                    marca = " =" if b == 0 and t.index[a] in iguais else ""
                    ax.text(b, a, f"{pos[a, b]}.º{marca}", ha="center", va="center", fontsize=F_EIXO,
                            color=cor_texto(RAMPA((pos[a, b] - 1) / max(n - 1, 1))))
            for k in range(1, 3):
                ax.axvline(k - 0.5, color="white", linewidth=2)
            for k in range(1, n):
                ax.axhline(k - 0.5, color="white", linewidth=2)
            ax.set_xticks(range(3), METODOS)
            ax.set_yticks(range(n), [curto(m) for m in t.index])
            ax.xaxis.tick_top()
            limpar(ax)
            ax.set_title(f"{CASOS[caso]}, cenário {cen}", fontsize=F_EIXO + 1, color=TEXTO, loc="left",
                         pad=30, fontweight="bold")
            ax.set_xlabel(frase_concordancia(t), fontsize=F_EIXO - 1, color=TEXTO_2, labelpad=8, loc="left")
    cabecalho(fig, "Os três métodos concordam no vencedor da haste e do scaffold; no stent "
                   "o 1.º lugar depende do método e empata no cenário B",
              "Posição de cada material por método (η = 1). Cenário A: só materiais em uso clínico; "
              "cenário B: inclui investigação.\n"
              f"O sinal = marca as posições do TOPSIS com diferença de C inferior a {fmt_pt(LIMIAR_EMPATE, 2)} "
              "para o material seguinte.", topo=0.87)
    return fig


def fig_monte_carlo(mc: pd.DataFrame) -> plt.Figure:
    tab = {c: separar_zeros(dados_primeiro(mc, c)) for c in CASOS}
    n = [len(t) + 0.6 for t, _ in tab.values()]
    fig, eixos = plt.subplots(3, 1, figsize=(13, 0.8 * sum(n) + 5.5), height_ratios=n, sharex=True)
    h = 0.26
    for ax, caso in zip(eixos, CASOS):
        t, zeros = tab[caso]
        if zeros:
            ax.text(0, len(t) - 0.42, "Restantes materiais: 0 % nos três métodos ("
                    + ", ".join(curto(z) for z in zeros) + ")", fontsize=F_EIXO - 2, color=TEXTO_2,
                    va="top", style="italic")
        for k, m in enumerate(METODOS):
            y = [i + (k - 1) * h for i in range(len(t))]
            ax.barh(y, t[m], height=h * 0.92, color=COR_METODO[m], label=m)
            for yi, v in zip(y, t[m]):
                ax.text(v + 1.2, yi, f"{fmt_pt(v, 0)} %", va="center", fontsize=F_EIXO - 2, color=TEXTO)
        ax.set_yticks(range(len(t)), [curto(x) for x in t.index])
        ax.set_ylim(len(t) + 0.1, -0.5)
        ax.set_xlim(0, 112)
        ax.set_xticks(range(0, 101, 20))
        ax.xaxis.grid(True, color=GRELHA, linewidth=0.8)
        ax.set_axisbelow(True)
        limpar(ax)
        ax.set_title(CASOS[caso], fontsize=F_EIXO + 1, color=TEXTO, loc="left", fontweight="bold")
    eixos[-1].set_xlabel("% das iterações em 1.º lugar", fontsize=F_EIXO, color=TEXTO_2)
    eixos[1].legend(loc="lower right", frameon=False, fontsize=F_EIXO, ncols=3)
    it = int(mc["n_iter"].iloc[0])
    cabecalho(fig, "Só na haste o 1.º lugar resiste à incerteza dos dados",
              f"Monte Carlo das propriedades, cenário A, {it} iterações: percentagem das iterações\n"
              "em que cada material fica em 1.º lugar, por método.", topo=0.90)
    return fig


def fig_monte_carlo_completo(mc: pd.DataFrame) -> plt.Figure:
    n = [len(dados_monte_carlo(mc, c, METODOS[0])) for c in CASOS]
    fig, eixos = plt.subplots(3, 3, figsize=(19, 0.62 * sum(n) + 5), height_ratios=n, sharex=True)
    for i, caso in enumerate(CASOS):
        ordem = dados_monte_carlo(mc, caso, METODOS[0]).index  # mesma ordem nos três métodos
        for j, m in enumerate(METODOS):
            ax, t = eixos[i, j], dados_monte_carlo(mc, caso, m).loc[ordem]
            esq = pd.Series(0.0, index=t.index)
            for col, tom in TONS_LUGAR.items():
                ax.barh(range(len(t)), t[col], left=esq, color=tom, height=0.66,
                        edgecolor="white", linewidth=1)
                for k, (v, e) in enumerate(zip(t[col], esq)):
                    if v >= 12:
                        ax.text(e + v / 2, k, fmt_pt(v, 0), ha="center", va="center",
                                fontsize=F_EIXO - 2, color=cor_texto(to_rgba(tom)))
                esq = esq + t[col]
            ax.set_yticks(range(len(t)), [curto(x) for x in t.index] if j == 0 else [])
            ax.set_ylim(len(t) - 0.5, -0.5)
            ax.set_xlim(0, 100)
            limpar(ax)
            ax.set_title(f"{CASOS[caso]}: {m}", fontsize=F_EIXO + 1, color=TEXTO, loc="left", fontweight="bold")
            if i == 2:
                ax.set_xlabel("% das iterações", fontsize=F_EIXO, color=TEXTO_2)
    fig.legend(handles=[Patch(color=c, label=NOME_LUGAR[k]) for k, c in TONS_LUGAR.items()],
               loc="lower left", bbox_to_anchor=(0.01, 0.0), ncols=3, frameon=False, fontsize=F_EIXO)
    it = int(mc["n_iter"].iloc[0])
    cabecalho(fig, "No stent e no scaffold os três primeiros lugares trocam entre si",
              f"Monte Carlo das propriedades, cenário A, {it} iterações: percentagem das iterações "
              "em 1.º, 2.º e 3.º lugar, por método (anexo).", topo=0.90)
    return fig


def fig_vencedor_eta(rk: pd.DataFrame) -> plt.Figure:
    fig, eixos = plt.subplots(3, 1, figsize=(16, 12.5))
    for ax, caso in zip(eixos, CASOS):
        t = dados_vencedor_eta(rk, caso)
        nc = len(t.columns)
        for a, m in enumerate(t.index):
            for b, eta in enumerate(t.columns):
                c = cor(caso, t.loc[m, eta])
                ax.add_patch(Rectangle((b - 0.5, a - 0.5), 1, 1, color=c, ec="white", lw=2))
                ax.text(b, a, curto_celula(t.loc[m, eta]), ha="center", va="center", fontsize=F_EIXO - 3,
                        color=cor_texto(to_rgba(c)))
        ax.add_patch(Rectangle((nc - 1.5, -0.5), 1, len(t.index), fill=False, ec=TEXTO, lw=3,
                               zorder=5, clip_on=False))
        ax.set_xlim(-0.5, nc - 0.5)
        ax.set_ylim(len(t.index) - 0.5, -0.5)
        ax.set_xticks(range(nc), [f"η = {fmt_pt(e, 1)}" for e in t.columns])
        ax.set_yticks(range(len(t.index)), t.index)
        limpar(ax)
        ax.tick_params(axis="x", labelsize=F_EIXO - 2)
        ax.set_title(CASOS[caso], fontsize=F_EIXO + 1, color=TEXTO, loc="left", fontweight="bold")
        if ax is eixos[0]:
            ax.text(nc - 1, -0.62, "resultado principal", ha="center", va="bottom",
                    fontsize=F_EIXO - 2, color=TEXTO, fontweight="bold")
    eixos[-1].set_xlabel("← pesos dos dados  |  pesos definidos por nós →", fontsize=F_EIXO + 1,
                         color=TEXTO, labelpad=12)
    cabecalho(fig, "Na haste e no scaffold o vencedor quase não depende de η; no stent muda",
              "Material em 1.º lugar no cenário A, por método, quando η vai de 0 (só pesos objetivos, "
              "tirados dos dados)\na 1 (só pesos subjetivos, definidos no trabalho).", topo=0.89)
    return fig


def fig_resumo(resumo: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(19, 1.9 * len(resumo) + 3.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(len(resumo), -0.42)
    ax.axis("off")
    colunas = {0.0: "Caso", 0.13: "Vencedor no cenário A", 0.47: "% de 1.º lugar no Monte Carlo",
               0.74: "O que muda o vencedor"}
    for x, nome in colunas.items():
        ax.text(x, -0.3, nome, fontsize=F_EIXO, color=TEXTO_2, fontweight="bold", va="center")
    ax.text(0.47, -0.08, " / ".join(METODOS), fontsize=F_EIXO - 2, color=TEXTO_2, va="center")
    for i, r in enumerate(resumo.itertuples()):
        ax.axhline(i + 0.02, color=GRELHA, linewidth=1.2)
        ax.text(0.0, i + 0.5, CASOS[r.caso], fontsize=F_TITULO, color=TEXTO, fontweight="bold", va="center")
        k = len(r.vencedores)
        for j, (mat, met) in enumerate(r.vencedores.items()):
            y = i + (j + 1) / (k + 1)
            ax.add_patch(Rectangle((0.13, y - 0.11), 0.016, 0.22, color=cor(r.caso, mat)))
            nome = ax.text(0.155, y, curto(mat), fontsize=F_TITULO - 1, color=TEXTO, va="center",
                           fontweight="bold")
            if len(met) < len(METODOS):
                ax.annotate(f"({', '.join(met)})", xy=(1, 0.5), xycoords=nome, xytext=(10, 0),
                            textcoords="offset points", fontsize=F_EIXO - 1, color=TEXTO_2, va="center")
            ax.text(0.47, y, " / ".join(f"{fmt_pt(v, 0)} %" for v in r.monte_carlo[mat]),
                    fontsize=F_TITULO - 1, color=TEXTO, va="center")
        frase = r.muda if r.muda.startswith("η") else r.muda[0].upper() + r.muda[1:]
        ax.text(0.74, i + 0.5, "\n".join(textwrap.wrap(frase, 34)), fontsize=F_EIXO, color=TEXTO,
                va="center", linespacing=1.35)
    cabecalho(fig, "Haste: vencedor estável. Stent: sensível aos dados e aos pesos.\n"
                   "Scaffold: estável a pequenas variações dos pesos, sensível aos dados e ao foco no problema",
              "Resumo dos três casos quantitativos: vencedor por método no cenário A (η = 1), robustez no "
              "Monte Carlo das propriedades\ne cenários de sensibilidade em que o vencedor muda.", topo=0.79)
    return fig


def gravar(fig: plt.Figure, nome: str, pasta: Path) -> list[Path]:
    pasta.mkdir(parents=True, exist_ok=True)
    caminhos = []
    for ext in ("png", "svg"):
        caminhos.append(pasta / f"{nome}.{ext}")
        fig.savefig(caminhos[-1], dpi=300, metadata={"Date": None} if ext == "svg" else None)
    plt.close(fig)
    return caminhos


def todas(rk: pd.DataFrame, pt: pd.DataFrame, mc: pd.DataFrame, data_dir: Path = DATA) -> dict[str, plt.Figure]:
    """As seis figuras, por nome de ficheiro."""
    return {"fig_a_rigidez_haste": fig_rigidez(*dados_rigidez(data_dir)),
            "fig_b_posicoes": fig_posicoes(rk, pt),
            "fig_c_monte_carlo": fig_monte_carlo(mc),
            "fig_c2_monte_carlo_completo": fig_monte_carlo_completo(mc),
            "fig_d_vencedor_eta": fig_vencedor_eta(rk),
            "fig_e_resumo": fig_resumo(dados_resumo(rk, mc))}


def main() -> None:
    rk = pd.read_csv(RESULTS / "rankings_cenarios.csv")
    pt = pd.read_csv(RESULTS / "pontuacoes.csv")
    mc = pd.read_csv(RESULTS / "monte_carlo.csv")
    for nome, fig in todas(rk, pt, mc).items():
        for c in gravar(fig, nome, RESULTS / "figures"):
            print(c)


if __name__ == "__main__":
    main()
