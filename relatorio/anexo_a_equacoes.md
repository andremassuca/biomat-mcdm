# Anexo A. Equações dos métodos

As equações seguem Petković et al. 2025, com a numeração do artigo entre parênteses retos. São as que
estão implementadas em src/biomat_mcdm/ e foram validadas contra os resultados publicados nos casos de
estudo 1 e 2 do artigo (secção 3). Notação: $x_{ij}$ é o valor do material $i$ ($i = 1, \dots, m$) no
critério $j$ ($j = 1, \dots, n$); $w_j$ é o peso do critério $j$, com $\sum_j w_j = 1$.

## A.1 Valor de referência de cada critério

Para cada critério define-se um valor de referência $T_j$:

$$
T_j = \begin{cases}
\max_i x_{ij} & \text{critério de benefício} \\
\min_i x_{ij} & \text{critério de custo} \\
\text{valor-alvo} & \text{critério-alvo}
\end{cases}
$$

## A.2 Pesos

Pesos combinados [eq. 1], com o nível de confiança $\eta \in [0, 1]$ nos pesos subjetivos $w_j^S$:

$$ w_j = \eta \, w_j^S + (1 - \eta) \, w_j^O $$

Pesos objetivos pelo método do desvio-padrão: cada coluna é posta na mesma escala
($x_{ij}/\max_i x_{ij}$ nos critérios de benefício e alvo; $\min_i x_{ij}/x_{ij}$ nos de custo), calcula-se
o desvio-padrão $\sigma_j$ de cada coluna e

$$ w_j^O = \frac{\sigma_j}{\sum_{k=1}^{n} \sigma_k} $$

O resultado principal usa $\eta = 1$ (só pesos subjetivos); $\eta$ de 0 a 1 é uma análise de sensibilidade.

## A.3 TOPSIS com critérios-alvo

Normalização linear com critérios-alvo [eq. 2] (Jahan et al. 2012):

$$ r_{ij} = 1 - \frac{|x_{ij} - T_j|}{\max\{x_j^{\max}, T_j\} - \min\{x_j^{\min}, T_j\}} $$

com $r_{ij} \in [0, 1]$ e 1 no melhor desempenho. Matriz pesada: $v_{ij} = w_j \, r_{ij}$. Soluções ideal e
anti-ideal: $v_j^{+} = \max_i v_{ij}$ e $v_j^{-} = \min_i v_{ij}$. Distâncias euclidianas e proximidade
relativa:

$$ D_i^{+} = \sqrt{\sum_j (v_{ij} - v_j^{+})^2}, \qquad D_i^{-} = \sqrt{\sum_j (v_{ij} - v_j^{-})^2}, \qquad
C_i = \frac{D_i^{-}}{D_i^{+} + D_i^{-}} $$

O maior $C_i$ é o melhor. Neste trabalho, duas posições consecutivas com $\Delta C < 0{,}01$ contam como
empate.

## A.4 WASPAS com critérios-alvo

Normalização própria [eqs. 9 a 13], com $x_j^{\min}$ e $x_j^{\max}$ o mínimo e o máximo da coluna:

$$
r_{ij} = \begin{cases}
x_{ij} / x_j^{\max} & \text{benefício [9]} \\
x_j^{\min} / x_{ij} & \text{custo [10]} \\
1 - (x_{ij} - T_j) / x_j^{\max} & \text{alvo abaixo de todos os valores, } T_j < x_j^{\min} \text{ [11]} \\
1 - (T_j - x_{ij}) / T_j & \text{alvo acima de todos os valores, } T_j > x_j^{\max} \text{ [12]} \\
1 - |x_{ij} - T_j| / (x_j^{\max} - x_j^{\min}) & \text{alvo entre o mínimo e o máximo [13]}
\end{cases}
$$

Quando o alvo coincide com o máximo da coluna usa-se a eq. 9, e quando coincide com o mínimo a eq. 10
(caso que o artigo não escreve; esta regra reproduz os resultados publicados). Soma pesada [eq. 14],
produto pesado [eq. 15] e pontuação final [eq. 16], com $\lambda = 0{,}5$:

$$ Q_i^{(1)} = \sum_j w_j \, r_{ij}, \qquad Q_i^{(2)} = \prod_j r_{ij}^{\,w_j}, \qquad
Q_i = \lambda \, Q_i^{(1)} + (1 - \lambda) \, Q_i^{(2)} $$

O maior $Q_i$ é o melhor.

## A.5 VIKOR com critérios-alvo

Com $A_j = \max\{x_j^{\max}, T_j\} - \min\{x_j^{\min}, T_j\}$ (o artigo indica $A_j = 1$ para dados já
normalizados; aqui os dados entram em bruto, por isso usa-se o intervalo), a utilidade do grupo [eq. 17] e
o arrependimento individual [eq. 18] são:

$$ S_i = \sum_j w_j \left(1 - e^{-|x_{ij} - T_j| / A_j}\right), \qquad
R_i = \max_j \, w_j \left(1 - e^{-|x_{ij} - T_j| / A_j}\right) $$

e o índice de compromisso [eq. 19], com $v = 0{,}5$:

$$ P_i = v \, \frac{S_i - S^{\min}}{S^{\max} - S^{\min}} + (1 - v) \, \frac{R_i - R^{\min}}{R^{\max} - R^{\min}} $$

O menor $P_i$ é o melhor. A solução de compromisso [eq. 20] exige que o 1.º tenha vantagem suficiente
sobre o 2.º ($P_{(2)} - P_{(1)} \ge 1/(m-1)$) e seja também o melhor em $S$ ou em $R$.

## A.6 Análises de robustez

- **Monte Carlo das propriedades:** em cada uma de 10 000 iterações (semente 42), cada $x_{ij}$ é sorteado
  com distribuição uniforme entre o mínimo e o máximo da base; os valores de fonte única variam ±10 % à
  volta do típico; os critérios ordinais não variam.
- **Monte Carlo dos pesos:** cada $w_j$ é multiplicado por um fator uniforme em $[0{,}8; 1{,}2]$ e os pesos
  são renormalizados.
- **P-foco:** os pesos dos critérios ligados ao problema crítico de cada dispositivo são multiplicados por
  2 e todos os pesos são renormalizados.
- **Concordância entre métodos:** coeficiente de correlação de Spearman entre as ordenações.

## A.7 Consenso de Borda

Com $p_i^{(k)}$ a posição do material $i$ no método $k \in \{\text{TOPSIS}, \text{WASPAS}, \text{VIKOR}\}$ e $m$ o
número de materiais, os pontos de Borda são

$$ B_i = \sum_{k} \left( m - p_i^{(k)} \right) $$

Os materiais ordenam-se por $B_i$ decrescente; em caso de empate, prevalece a posição no TOPSIS.
