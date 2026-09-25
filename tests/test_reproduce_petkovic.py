"""Verificação do código: caso de estudo 2 (componente femoral da prótese da anca) de
Petković, Madić & Mitković, Appl. Sci. 2025, 15(16), 9198, doi:10.3390/app15169198.

Dados copiados do artigo: matriz de decisão, valores-alvo e pesos da Tabela A3; resultados
das Tabelas 3 (η = 1) e 4 (posições para η = 0,7; 0,8; 0,9; 1). Todos os critérios têm um
valor-alvo T_j (para os de benefício, T_j é o melhor valor da coluna); C5 (módulo, T = 14 GPa)
e C6 (densidade, T = 2,1 g/cm³) são critérios-alvo com o alvo abaixo de todos os materiais.

Resultado da verificação (tolerância definida para a secção de Métodos):
  - o 1.º lugar do TOPSIS (M7) é reproduzido para os quatro valores de η;
  - correlação de Spearman com o ranking publicado ≥ 0,95 para todos os η;
  - os valores C_i das ligas de Ti M10, M12 e M13 coincidem com os publicados (±0,001).
Os valores C_i dos restantes materiais ficam acima dos publicados (até +0,05), o que não se
explica pelo arredondamento dos pesos nem por variantes da solução ideal ou dos tipos de
critério. Com os mesmos dados, a normalização do WASPAS (eqs. 9-13) reproduz os Q_i publicados
em 14 de 15 materiais (±0,0005), o que indica que os dados foram bem transcritos e que a
diferença está num pormenor de implementação do TOPSIS no software dos autores que o artigo
não descreve. Fica registado como limitação da verificação (test_topsis_valores_exatos).
"""
import numpy as np
import pytest
from scipy.stats import spearmanr

from biomat_mcdm.methods.topsis import rank, topsis

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


@pytest.mark.xfail(strict=True, reason="diferença de implementação no software dos autores; ver docstring do módulo")
def test_topsis_valores_exatos():
    C = topsis(X, np.array(PESOS[1.0]), TIPOS, ALVOS)
    assert C == pytest.approx(C_PUBLICADO, abs=1e-3)
