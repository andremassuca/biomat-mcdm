"""Verificação do código: caso de estudo 2 (componente femoral da prótese da anca) de
Petković, Madić & Mitković, Appl. Sci. 2025, 15(16), 9198, doi:10.3390/app15169198.

Dados copiados do artigo: matriz de decisão, valores-alvo e pesos da Tabela A3; resultados
das Tabelas 3 (η = 1) e 4 (posições para η = 0,7; 0,8; 0,9; 1). Todos os critérios têm um
valor-alvo T_j (para os de benefício, T_j é o melhor valor da coluna); C5 (módulo, T = 14 GPa)
e C6 (densidade, T = 2,1 g/cm³) são critérios-alvo com o alvo abaixo de todos os materiais.

Incoerência no artigo (verificada no PDF a 27 set 2026): a Tabela A3 dá M1-C9
(biocompatibilidade) = 0,41, mas a Figura A6 (captura do software MCSl, η = 1) mostra
M1-C9 = 0,59; todas as outras células, os alvos, os C_i e as posições coincidem. Os C_i
publicados (Tabela 3, Figura A6) foram calculados com 0,59. A Figura A6 mostra também os pesos
com 5 casas decimais (arredondados a 3 casas dão os da Tabela A3 para η = 1).

Por isso há dois conjuntos de dados:
  - X (fiel à Tabela A3, M1-C9 = 0,41): verifica que os resultados publicados NÃO se obtêm
    a partir da tabela; os testes exatos com X ficam como xfail (strict).
  - X_SOFTWARE (M1-C9 = 0,59, como na Figura A6) com PESOS_SOFTWARE: reproduz os 15 C_i
    publicados com diferença máxima de 5e-6 e as 15 posições.

Resultado da verificação com X (tolerância definida para a secção de Métodos):
  - o 1.º lugar do TOPSIS (M7) é reproduzido para os quatro valores de η;
  - correlação de Spearman com o ranking publicado ≥ 0,95 para todos os η;
  - os valores C_i das ligas de Ti M10, M12 e M13 coincidem com os publicados (±0,001).

Pesos (eq. 1, secção 2.4): com os pesos subjetivos da Figura A6 (η = 1), os pesos objetivos
do desvio-padrão (weights.py) reproduzem os pesos publicados para η = 0,7; 0,8; 0,9 com os
dados do software (diferença máxima 0,0005, arredondamento a 3 casas), mas não com a
Tabela A3 (0,003): segunda confirmação independente de M1-C9 = 0,59. O caso de estudo 1
(placa; Tabela A2 e Figura A4, matrizes iguais) confirma a normalização do custo (C10).

WASPAS (eqs. 9-16) e VIKOR (eqs. 17-20), com os dados do software: reproduzem os 15 Q_i e os
15 P_i publicados nos casos 1 (Tabela 1, Figura A4) e 2 (Tabela 3) com diferença < 1e-5.
Com os pesos combinados calculados (weights.py, sem arredondamento), os três métodos
reproduzem as 60 posições da Tabela 4 cada um (4 valores de η x 15 materiais), incluindo
η = 0,7. Com a Tabela A3, o WASPAS só falha em M1 (14 de 15 Q_i).
"""
import numpy as np
import pytest
from scipy.stats import spearmanr

from biomat_mcdm.methods.topsis import rank, topsis
from biomat_mcdm.methods.vikor import compromise_set, vikor
from biomat_mcdm.methods.waspas import waspas
from biomat_mcdm.weights import combine_weights, std_dev_weights

# M1-M4 aços inoxidáveis; M5-M9 ligas de Co; M10-M15 titânio e ligas de Ti (Tabela A1)
MATERIAIS = ["M%d" % i for i in range(1, 16)]
# C1 cedência (MPa), C2 tração (MPa), C3 fadiga (MPa), C4 alongamento (%), C5 módulo (GPa),
# C6 densidade (g/cm³), C7 tenacidade relativa, C8 corrosão, C9 biocompatibilidade, C10 maquinabilidade
X = np.array([
    [250, 585, 330, 57, 193, 7.95, 0.865, 0.41, 0.41, 0.865],
    [450, 825, 320, 45, 193, 7.86, 0.865, 0.5, 0.59, 0.865],
    [580, 930, 380, 52, 200, 7.64, 0.865, 0.5, 0.745, 0.865],
    [450, 840, 370, 39, 195, 7.75, 0.745, 0.5, 0.59, 0.865],
    [585, 1035, 300, 25, 241, 8.28, 0.59, 0.745, 0.745, 0.335],
    [880, 1350, 700, 22, 241, 8.28, 0.59, 0.745, 0.745, 0.41],
    [1115, 1420, 760, 28, 241, 8.29, 0.59, 0.745, 0.745, 0.335],
    [1340, 1400, 700, 21, 235, 8.43, 0.59, 0.665, 0.59, 0.255],
    [415, 1035, 440, 60, 243, 9.22, 0.59, 0.665, 0.665, 0.335],
    [550, 670, 430, 22, 103, 4.51, 0.335, 0.955, 0.955, 0.5],
    [710, 880, 550, 12, 105, 4.43, 0.335, 0.865, 0.865, 0.41],
    [850, 950, 540, 12, 105, 4.52, 0.335, 0.955, 0.955, 0.41],
    [820, 900, 580, 6, 112, 4.45, 0.335, 0.865, 0.955, 0.41],
    [570, 690, 320, 15, 103, 4.48, 0.335, 0.865, 0.865, 0.5],
    [920, 960, 600, 25, 78, 5.06, 0.335, 0.865, 0.865, 0.41],
], float)
ALVOS = [1340, 1420, 760, 60, 14, 2.1, 0.865, 0.955, 0.955, 0.865]
TIPOS = ["target"] * 10
PESOS = {
    0.7: [0.111, 0.095, 0.125, 0.090, 0.098, 0.071, 0.100, 0.119, 0.121, 0.071],
    0.8: [0.113, 0.096, 0.130, 0.084, 0.095, 0.067, 0.098, 0.124, 0.129, 0.064],
    0.9: [0.115, 0.098, 0.134, 0.078, 0.092, 0.064, 0.096, 0.129, 0.137, 0.057],
    1.0: [0.117, 0.100, 0.139, 0.072, 0.089, 0.061, 0.094, 0.133, 0.144, 0.050],
}

# Dados usados pelo software dos autores (Figura A6, η = 1): igual a X exceto M1-C9 = 0,59
X_SOFTWARE = X.copy()
X_SOFTWARE[0, 8] = 0.59
PESOS_SOFTWARE = [0.11667, 0.10000, 0.13889, 0.07222, 0.08889, 0.06111, 0.09444, 0.13333,
                  0.14444, 0.05000]

# Tabela 3 (η = 1)
C_PUBLICADO = [0.31059, 0.32923, 0.41753, 0.30558, 0.37383, 0.56664, 0.60806, 0.51629,
               0.37006, 0.52711, 0.53481, 0.59714, 0.58041, 0.44623, 0.59240]
Q_WASPAS_PUBLICADO = [0.49658, 0.53911, 0.59748, 0.53317, 0.49616, 0.6056, 0.63975, 0.60614,
                      0.50988, 0.62369, 0.63011, 0.66704, 0.63605, 0.57241, 0.69360]
P_VIKOR_PUBLICADO = [0.99262, 0.94838, 0.5774, 1, 0.9333, 0.20032, 0.07027, 0.64589,
                     0.7612, 0.30244, 0.18257, 0, 0.06465, 0.72884, 0.06339]

# Tabela 4: posições TOPSIS por η
RANK_TOPSIS_PUBLICADO = {
    0.7: [13, 12, 9, 15, 14, 4, 1, 6, 11, 8, 7, 3, 5, 10, 2],
    0.8: [14, 13, 9, 15, 12, 5, 1, 8, 11, 7, 6, 3, 4, 10, 2],
    0.9: [14, 13, 10, 15, 12, 5, 1, 8, 11, 7, 6, 2, 4, 9, 3],
    1.0: [14, 13, 10, 15, 11, 5, 1, 8, 12, 7, 6, 2, 4, 9, 3],
}


@pytest.mark.parametrize("eta", PESOS)
def test_topsis_mesmo_primeiro_lugar(eta):
    r = rank(topsis(X, np.array(PESOS[eta]), TIPOS, ALVOS))
    assert MATERIAIS[int(np.argmin(r))] == "M7"


@pytest.mark.parametrize("eta", PESOS)
def test_topsis_concordancia_com_ranking_publicado(eta):
    r = rank(topsis(X, np.array(PESOS[eta]), TIPOS, ALVOS))
    rho = spearmanr(r, RANK_TOPSIS_PUBLICADO[eta])[0]
    assert rho >= 0.95


def test_topsis_valores_exatos_ligas_ti():
    C = topsis(X, np.array(PESOS[1.0]), TIPOS, ALVOS)
    for i in (9, 11, 12):  # M10, M12, M13
        assert C[i] == pytest.approx(C_PUBLICADO[i], abs=1e-3)


@pytest.mark.xfail(strict=True, reason="Tabela A3 tem M1-C9 = 0,41; o software usou 0,59 (Figura A6)")
def test_topsis_valores_exatos():
    C = topsis(X, np.array(PESOS[1.0]), TIPOS, ALVOS)
    assert C == pytest.approx(C_PUBLICADO, abs=1e-3)


@pytest.mark.xfail(strict=True, reason="Tabela A3 tem M1-C9 = 0,41; o software usou 0,59 (Figura A6)")
@pytest.mark.parametrize("eta", PESOS)
def test_topsis_posicoes_exatas(eta):
    r = rank(topsis(X, np.array(PESOS[eta]), TIPOS, ALVOS))
    assert list(r) == RANK_TOPSIS_PUBLICADO[eta]


def test_software_valores_exatos():
    # Tolerância 1e-5: os C_i estão publicados com 5 casas (erro de arredondamento até 5e-6)
    # e os pesos da Figura A6 também estão arredondados a 5 casas.
    C = topsis(X_SOFTWARE, np.array(PESOS_SOFTWARE), TIPOS, ALVOS)
    assert C == pytest.approx(C_PUBLICADO, abs=1e-5)


def test_software_posicoes_eta_1():
    r = rank(topsis(X_SOFTWARE, np.array(PESOS_SOFTWARE), TIPOS, ALVOS))
    assert list(r) == RANK_TOPSIS_PUBLICADO[1.0]


@pytest.mark.parametrize("eta", [
    pytest.param(0.7, marks=pytest.mark.xfail(strict=True, reason=(
        "M10 e M11 trocam (C a 0,00005 de distância); os pesos só estão publicados com 3 casas"))),
    0.8, 0.9, 1.0,
])
def test_software_posicoes_pesos_publicados(eta):
    # Pesos da Tabela A3 (3 casas); para η ≠ 1 o artigo não mostra os pesos com mais casas.
    r = rank(topsis(X_SOFTWARE, np.array(PESOS[eta]), TIPOS, ALVOS))
    assert list(r) == RANK_TOPSIS_PUBLICADO[eta]


# Pesos (eq. 1). Tolerância 6e-4: os pesos da Tabela A3 estão publicados com 3 casas
# (erro de arredondamento até 5e-4) e os subjetivos da Figura A6 com 5 casas.
@pytest.mark.parametrize("eta", [0.7, 0.8, 0.9])
def test_pesos_combinados_caso2_software(eta):
    w_obj = std_dev_weights(X_SOFTWARE, TIPOS)
    w = combine_weights(np.array(PESOS_SOFTWARE), w_obj, eta)
    assert w == pytest.approx(PESOS[eta], abs=6e-4)


@pytest.mark.xfail(strict=True, reason="Tabela A3 tem M1-C9 = 0,41; o software usou 0,59 (Figura A6)")
def test_pesos_combinados_caso2_tabela_A3():
    w = combine_weights(np.array(PESOS_SOFTWARE), std_dev_weights(X, TIPOS), 0.7)
    assert w == pytest.approx(PESOS[0.7], abs=6e-4)


# Caso de estudo 1 (placa): Tabela A2 (p. 28), igual à matriz da Figura A4 (p. 27).
# C1-C9 alvo (C1-C3, C6-C9 com o alvo no melhor valor da coluna; C4 módulo 18 GPa, C5
# densidade 2,1 g/cm³); C10 custo relativo (alvo 1 = mínimo da coluna, tratado como custo).
X_CASO1 = np.array([
    [250, 585, 57, 193, 7.95, 0.865, 0.41, 0.41, 0.865, 2.4],
    [450, 825, 45, 193, 7.86, 0.865, 0.5, 0.59, 0.865, 3.1],
    [580, 930, 52, 200, 7.64, 0.865, 0.5, 0.745, 0.865, 1],
    [450, 840, 39, 195, 7.75, 0.745, 0.5, 0.59, 0.865, 2.6],
    [585, 1035, 25, 241, 8.28, 0.59, 0.745, 0.745, 0.335, 21.9],
    [880, 1350, 22, 241, 8.28, 0.59, 0.745, 0.745, 0.41, 23.1],
    [1115, 1420, 28, 241, 8.29, 0.59, 0.745, 0.745, 0.335, 87],
    [1340, 1400, 21, 235, 8.43, 0.59, 0.665, 0.59, 0.255, 37.5],
    [415, 1035, 60, 243, 9.22, 0.59, 0.665, 0.665, 0.335, 36.2],
    [550, 670, 22, 103, 4.51, 0.335, 0.955, 0.955, 0.5, 13.1],
    [710, 880, 12, 105, 4.43, 0.335, 0.865, 0.865, 0.41, 18],
    [850, 950, 12, 105, 4.52, 0.335, 0.955, 0.955, 0.41, 15.5],
    [820, 900, 6, 112, 4.45, 0.335, 0.865, 0.955, 0.41, 16],
    [570, 690, 15, 103, 4.48, 0.335, 0.865, 0.865, 0.5, 16.5],
    [920, 960, 25, 78, 5.06, 0.335, 0.865, 0.865, 0.41, 19.4],
], float)
ALVOS_CASO1 = [1340, 1420, 60, 18, 2.1, 0.865, 0.955, 0.955, 0.865, None]
TIPOS_CASO1 = ["target"] * 9 + ["cost"]
PESOS_SOFTWARE_CASO1 = [0.12778, 0.13889, 0.07222, 0.10000, 0.06111, 0.09444, 0.12778,
                        0.13889, 0.07778, 0.06111]  # Figura A4, η = 1
PESOS_CASO1 = {
    0.7: [0.118, 0.121, 0.088, 0.105, 0.070, 0.098, 0.114, 0.120, 0.089, 0.078],
    0.8: [0.121, 0.127, 0.083, 0.103, 0.067, 0.097, 0.119, 0.126, 0.085, 0.072],
    0.9: [0.125, 0.133, 0.078, 0.102, 0.064, 0.096, 0.123, 0.132, 0.081, 0.067],
    1.0: [0.128, 0.139, 0.072, 0.100, 0.061, 0.094, 0.128, 0.139, 0.078, 0.061],
}


def test_pesos_software_caso1_arredondados_dao_tabela_A2():
    assert list(np.round(PESOS_SOFTWARE_CASO1, 3)) == PESOS_CASO1[1.0]


@pytest.mark.parametrize("eta", [0.7, 0.8, 0.9])
def test_pesos_combinados_caso1(eta):
    w_obj = std_dev_weights(X_CASO1, TIPOS_CASO1)
    w = combine_weights(np.array(PESOS_SOFTWARE_CASO1), w_obj, eta)
    assert w == pytest.approx(PESOS_CASO1[eta], abs=6e-4)


# Resultados publicados do caso 1 (Tabela 1, η = 1; P também na Figura A4)
C_CASO1 = [0.36091, 0.43561, 0.51072, 0.41394, 0.46863, 0.56775, 0.57665, 0.54337, 0.42652,
           0.52587, 0.52614, 0.58704, 0.55505, 0.48953, 0.57799]
Q_WASPAS_CASO1 = [0.47867, 0.54989, 0.6405, 0.5391, 0.46466, 0.51537, 0.51996, 0.5081,
                  0.44765, 0.56698, 0.55239, 0.59301, 0.55713, 0.53661, 0.60526]
P_VIKOR_CASO1 = [0.96259, 0.53136, 0.34875, 0.61966, 0.53465, 0.28385, 0.25942, 0.36803,
                 0.73832, 0.50918, 0.33352, 0.00151, 0.20215, 0.65273, 0.08705]

# Tabela 4 (p. 21): posições WASPAS e VIKOR do caso 2 por η
RANK_WASPAS_PUBLICADO = {
    0.7: [13, 11, 7, 12, 15, 8, 3, 9, 14, 4, 5, 2, 6, 10, 1],
    0.8: [13, 11, 7, 12, 15, 8, 3, 9, 14, 6, 5, 2, 4, 10, 1],
    0.9: [14, 11, 7, 12, 15, 9, 3, 8, 13, 6, 5, 2, 4, 10, 1],
    1.0: [14, 11, 9, 12, 15, 8, 3, 7, 13, 6, 5, 2, 4, 10, 1],
}
RANK_VIKOR_PUBLICADO = {
    0.7: [13, 12, 8, 14, 15, 5, 1, 10, 9, 6, 7, 2, 4, 11, 3],
    0.8: [13, 12, 8, 14, 15, 5, 1, 9, 10, 7, 6, 2, 4, 11, 3],
    0.9: [13, 12, 8, 15, 14, 5, 1, 9, 10, 7, 6, 2, 4, 11, 3],
    1.0: [14, 13, 8, 15, 12, 6, 4, 9, 11, 7, 5, 1, 3, 10, 2],
}

# Tolerância 1e-5 nos valores: publicados com 5 casas (arredondamento até 5e-6).
CASOS = {
    "caso1": (X_CASO1, PESOS_SOFTWARE_CASO1, TIPOS_CASO1, ALVOS_CASO1, C_CASO1, Q_WASPAS_CASO1, P_VIKOR_CASO1),
    "caso2": (X_SOFTWARE, PESOS_SOFTWARE, TIPOS, ALVOS, C_PUBLICADO, Q_WASPAS_PUBLICADO, P_VIKOR_PUBLICADO),
}


@pytest.mark.parametrize("caso", CASOS)
def test_topsis_valores_publicados(caso):
    Xc, w, tipos, alvos, C, _, _ = CASOS[caso]
    assert topsis(Xc, np.array(w), tipos, alvos) == pytest.approx(C, abs=1e-5)


@pytest.mark.parametrize("caso", CASOS)
def test_waspas_valores_publicados(caso):
    Xc, w, tipos, alvos, _, Q, _ = CASOS[caso]
    assert waspas(Xc, np.array(w), tipos, alvos) == pytest.approx(Q, abs=1e-5)


@pytest.mark.parametrize("caso", CASOS)
def test_vikor_valores_publicados(caso):
    Xc, w, tipos, alvos, _, _, P = CASOS[caso]
    assert vikor(Xc, np.array(w), tipos, alvos)["P"] == pytest.approx(P, abs=1e-5)


@pytest.mark.xfail(strict=True, reason="Tabela A3 tem M1-C9 = 0,41; o software usou 0,59 (Figura A6)")
def test_waspas_tabela_A3():
    assert waspas(X, np.array(PESOS_SOFTWARE), TIPOS, ALVOS) == pytest.approx(Q_WASPAS_PUBLICADO, abs=1e-5)


@pytest.mark.parametrize("eta", [0.7, 0.8, 0.9, 1.0])
def test_tabela_4_tres_metodos_com_pesos_calculados(eta):
    w = combine_weights(np.array(PESOS_SOFTWARE), std_dev_weights(X_SOFTWARE, TIPOS), eta)
    assert list(rank(topsis(X_SOFTWARE, w, TIPOS, ALVOS))) == RANK_TOPSIS_PUBLICADO[eta]
    assert list(rank(waspas(X_SOFTWARE, w, TIPOS, ALVOS))) == RANK_WASPAS_PUBLICADO[eta]
    P = vikor(X_SOFTWARE, w, TIPOS, ALVOS)["P"]
    assert list(rank(P, higher_is_better=False)) == RANK_VIKOR_PUBLICADO[eta]


def test_vikor_compromisso_caso2():
    # Texto da p. 21: P(7) - P(12) = 0,07027 < 1/(m - 1) = 0,071, logo M12, M15, M13 e M7
    # são considerados as alternativas de 1.º lugar.
    out = vikor(X_SOFTWARE, np.array(PESOS_SOFTWARE), TIPOS, ALVOS)
    idx = compromise_set(out["S"], out["R"], out["P"])
    assert sorted(MATERIAIS[i] for i in idx) == sorted(["M12", "M15", "M13", "M7"])
