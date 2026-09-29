# Notas metodológicas (ir preenchendo, vira a secção de Métodos)

## Âmbito
- MCDM quantitativo: haste femoral, stent coronário expansível por balão, scaffold ósseo.
- Semiquantitativo (ordinais > 50 % do peso): par articular, implante dentário.
- Nitinol (autoexpansível, periférico) fora do ranking; só na discussão.

## Níveis de validação (não confundir)
| Nível | Pergunta | O que se pode afirmar |
|---|---|---|
| Verificação de código | O algoritmo está bem implementado? | Reproduz Petković et al. 2025 dentro de tolerância definida |
| Robustez interna | O ranking muda com pesos, método, η, incerteza, alvos? | A seleção é robusta/frágil nos cenários testados |
| Validação clínica | O ranking prevê desempenho clínico? | NÃO demonstrado: trabalho futuro |

A "% de vitórias" no Monte Carlo NÃO é probabilidade de sucesso clínico: é a frequência com que um material fica em 1.º nas hipóteses do modelo.

## Decisões e justificações
- Dados: fonte de verdade = CSV em data/ (+ data/leia_me.md); o .xlsx é gerado por scripts/exportar_xlsx.py (só valores, sem fórmulas). η = 1 por omissão (data/parametros.csv; antes 0,5, vindo da folha Criterios do .xlsx).
- Cenários (data/cenarios.csv): A = só materiais em uso clínico; B = inclui investigação e bioabsorvíveis. No stent, A = só permanentes (316L, L605, MP35N, Pt-Cr); B = A + Mg WE43 e PLLA.
- Tempo de reabsorção do stent (critério só do cenário B; alvo 12 meses):
  - B (opção O2): os permanentes recebem o pior valor observado (48 meses, máximo do PLLA). Interpretação: "não reabsorver é pelo menos tão mau como o pior bioabsorvível". Limitação: subestima o caso permanente (um permanente nunca reabsorve). Coerente nos três métodos, que usam os valores em bruto.
  - B-bio (opção O3): só Mg WE43 e PLLA, com o critério; apresentar como comparação, não como ranking (2 materiais).
  - R-sentinela (opção O1): sensibilidade a 60, 120, 600 e 1200 meses para os permanentes. TOPSIS e VIKOR não dependem do valor acima de 48 meses; o WASPAS depende (a eq. 13 leva r para 0 e o produto arrasta os permanentes): com 1200 meses o 316L cai para 5.º.
- η: resultado principal com η = 1 (só pesos subjetivos, justificados pelos mecanismos de falha). Os pesos objetivos (desvio-padrão) dependem da dispersão do conjunto de candidatos e mudam com o cenário (A vs B), por isso o η entra só como análise de sensibilidade (0 a 1, passo 0,1). O η = 0,5 vinha do valor inicial sugerido no artigo (secção 2.4).
- σy/E (src/biomat_mcdm/indices.py, calculado a partir de σy e E da base; intervalo = σy mín./E máx. a σy máx./E mín.): proxy ao nível do material da deformação elástica na cedência. Em stents expansíveis por balão, maior σy/E → maior recuo elástico → critério de CUSTO. Não é o recuo do dispositivo (depende da geometria do padrão, struts, processamento).
- E_implante/E_osso (indices.stiffness_ratio; osso cortical 15-20 GPa de data/tecido.csv): indicador exploratório de risco relativo de stress shielding, não é critério (o módulo já é critério-alvo); a transferência de carga real depende de geometria, fixação e contacto (FEA = trabalho futuro).
- Alvo E = 17 GPa na haste: todos os candidatos estão acima do alvo → na prática funciona como "menor é melhor" com escala comprimida; testar vs critério de custo com limiar de fadiga (cenário T-haste). O cenário T-haste inclui também a comparação do alvo 14 GPa (Petković et al. 2025, Tabela A3, C5) vs 17 GPa.
- Triagem estrita (src/biomat_mcdm/screening.py), antes dos métodos:
  - regras numéricas avaliadas no pior caso do intervalo (mín. para "≥", máx. para "≤"): a segurança não é compensável;
  - estatuto "Excluído" na base elimina (Nitinol: autoexpansível, outra classe de dispositivo);
  - regras qualitativas (ISO 10993 da haste, fratura da cabeça cerâmica, ISO 14801) não eliminam: ficam "não avaliado" no registo e são discutidas no texto;
  - material sem dados para uma regra numérica não é eliminado: fica "não avaliado (sem dados)";
  - regras categóricas (valor em texto na coluna valor_texto): "Tipo de expansão" = balão ou autoexpansível; passa se o valor está no alvo ("Expansível por balão");
  - resultado atual: eliminados o MoM (segurança iónica 1 < 2) e o Nitinol (tipo de expansão autoexpansível; também pelo estatuto "Excluído").
- Alvos do scaffold = cenário de referência para osso trabecular, não ótimo universal (cenário T-scaffold).
- Densidade removida como proxy de radiopacidade (depende do número atómico efetivo e da espessura).
- K_IC removido do par articular (valor metálico arbitrário); fratura cerâmica tratada como requisito estrito/discussão.
- Tração (metais) e flexão (cerâmicos) não são comparáveis → retirado da matriz dentária; requisito estrito ISO 14801.
- Desgaste: só comparar valores do mesmo tipo de evidência (in vivo radiográfico/RSA OU simulador ISO 14242).

## Reprodução de Petković et al. 2025
Caso de estudo 2 (haste da prótese da anca), TOPSIS; testes em tests/test_reproduce_petkovic.py.
- Incoerência no artigo, verificada no PDF a 27 set 2026:
  - Tabela A3 (p. 30): M1-C9 (biocompatibilidade) = 0,41.
  - Figura A6 (p. 30, captura do software MCSl, η = 1): M1-C9 = 0,59.
  - Todas as outras 149 células, os 10 alvos, os 15 C_i e as 15 posições coincidem entre a
    Figura A6 e o que está nos testes.
- Os resultados publicados (Tabela 3, Tabela 4, Figura A6) foram calculados com 0,59.
- Com a matriz da Figura A6 e os pesos com 5 casas mostrados na mesma figura, o nosso TOPSIS
  reproduz os 15 C_i (diferença máxima 5e-6) e as 15 posições.
- Com os pesos da Tabela A3 (3 casas) e M1-C9 = 0,59: posições iguais para η = 0,8; 0,9; 1;
  para η = 0,7, M10 e M11 trocam (C a 0,00005 de distância, abaixo do efeito do arredondamento
  dos pesos).
- Com a matriz da Tabela A3 (0,41): só 4 de 15 posições coincidem (η = 1); o 1.º lugar (M7)
  mantém-se.
- Os pesos da Figura A6 correspondem a frações n/180 (21, 18, 25, 13, 16, 11, 17, 24, 26, 9;
  soma 180). Observação, não usada nos testes.
- Estado: email ao autor correspondente por enviar (rascunho em docs/email_petkovic.md).
- Para a secção de Métodos: a verificação usa os dados do software (Figura A6) e declara a
  incoerência da Tabela A3.
- Pesos (eq. 1, secção 2.4): o artigo não descreve sobre que matriz se calcula o desvio-padrão.
  A normalização abaixo foi RECONSTITUÍDA a partir dos resultados publicados (pesos para
  η = 0,7; 0,8; 0,9), não descrita no artigo; pergunta ao autor no email (docs/email_petkovic.md):
  - benefício e alvo: x_ij / max x_j; custo: min x_j / x_ij; w_j^O = σ_j / Σ σ_k;
  - caso 2 com os dados do software: diferença máxima 0,0005 (arredondamento a 3 casas);
    com a Tabela A3 (M1-C9 = 0,41): 0,003. Segunda confirmação independente de M1-C9 = 0,59;
  - caso 1 (placa, Tabela A2 = Figura A4): diferença máxima 0,0005; o custo relativo (C10)
    só se reproduz com min/x (com x/max: 0,0024).
  - Implementação: src/biomat_mcdm/weights.py; testes em tests/test_reproduce_petkovic.py.
- WASPAS (eqs. 9-16) e VIKOR (eqs. 17-20), com os dados do software:
  - reproduzem os 15 Q_i e os 15 P_i publicados nos casos 1 e 2 (diferença < 1e-5);
  - o TOPSIS reproduz também os 15 C_i do caso 1;
  - com os pesos combinados calculados por weights.py (sem arredondamento), os três métodos
    reproduzem as 60 posições da Tabela 4 cada um, incluindo η = 0,7 (a troca M10/M11 vinha
    só do arredondamento dos pesos publicados a 3 casas);
  - solução de compromisso do VIKOR (passo 6): reproduz o conjunto M12, M15, M13, M7 do texto (p. 21).
- Pormenores RECONSTITUÍDOS a partir dos resultados publicados (o artigo não os escreve):
  - WASPAS: alvo igual ao máximo da coluna usa a eq. 9; igual ao mínimo usa a eq. 10
    (com a eq. 13 nesses casos a diferença chega a 0,41);
  - VIKOR: A_j = max{x_max, T} - min{x_min, T} em todas as colunas; o "A_j = 1 para valores
    normalizados" não se aplica a dados em bruto (com A_j = 1 nas colunas em [0, 1], diferença até 0,42).
- Com a Tabela A3 (M1-C9 = 0,41), o WASPAS falha só em M1 (14 de 15 Q_i), o que explica a
  afirmação antiga "14 de 15", agora com código que a demonstra.

## Robustez (src/biomat_mcdm/robustness.py, scripts/run_all.py)
- Resultado principal: cenário A, η = 1. As análises de sensibilidade partem do cenário A.
- MC propriedades: cada valor sorteado com distribuição uniforme entre mín. e máx. da base; 10 000 iterações, seed 42; a mesma seed para os três métodos (mesmos sorteios).
- W pesos: cada peso multiplicado por um fator uniforme em [0,8; 1,2] e renormalizado (±20 %).
- η: 0 a 1, passo 0,1, com os pesos objetivos do desvio-padrão calculados sobre a matriz do cenário A.
- T-haste: alvo de E = 14 (Petković et al. 2025), 15, 17, 20 GPa (osso cortical 15-20, tecido.csv) e módulo como critério de custo.
- T-scaffold: alvos no mínimo e no máximo do osso trabecular (tecido.csv) para compressão (2-12 MPa), módulo (50-500 MPa) e porosidade (50-90 %); tempo de degradação sem referência no tecido: fatores de sensibilidade x0,5 e x2 sobre o alvo (não são valores da literatura).
- C-custo: peso do custo relativo 0,01 (baixo) e 0,25 (elevado), restantes pesos redistribuídos proporcionalmente (valores de desenho da análise, não da literatura).
- M: Spearman entre os três métodos em cada cenário e variante (não calculado com 2 materiais: B-bio).
- A "% de 1.º lugar" é a frequência nas hipóteses do modelo, não a probabilidade de sucesso clínico.
- Reversão de ranking observada (scaffold, 28 set 2026): ao retirar PLLA, PLGA e quitosano/HA (cenário A com os estatutos novos), o β-TCP e o PCL/β-TCP trocam de posição (TOPSIS e VIKOR: PCL/β-TCP 1.º com 8 materiais, β-TCP 1.º com 5), porque as normalizações dependem do mínimo e do máximo de cada coluna. Exemplo concreto para o item "Testes formais de reversão de ranking" do backlog e para a secção de limitações.
- Scaffold: a fragilidade do ranking reflete em parte a incerteza dos dados (propriedades muito dependentes da porosidade, intervalos largos na base) e não só o método. Na discussão, separar as duas causas, por exemplo comparando a % de 1.º lugar do MC propriedades (incerteza dos dados) com a do W pesos (incerteza das preferências). Cenário A com os estatutos novos (5 materiais): β-TCP 53,6 % / 31,6 % / 37,4 % (T/W/V) no MC propriedades, mas 91,7 % / 100 % / 85,3 % no W pesos; ou seja, o 1.º lugar é estável face aos pesos e frágil face aos dados.

## Fontes das propriedades mecânicas da haste (29 set 2026)
- Fadiga a 10^7 ciclos e tensão de cedência das quatro ligas clínicas (316L encruado 20 %,
  Co-Cr-Mo forjado a quente, Ti-6Al-4V, Ti cp grau 4 recozido): Okazaki 2012 (Materials 5:2981,
  Tabela 2), para usar o mesmo laboratório e o mesmo ensaio (tração-tração, R = 0,1, 10 Hz).
  A fadiga é derivada (σFS/σUTS × σUTS), com o estado "Verificado (derivado)"; a cedência usa
  média ± DP como mín.-máx.
- Limitações:
  - (a) O Ti-6Al-4V foi ensaiado ao ar e o aço e o Co-Cr-Mo em meio de Eagle a 37 °C. É uma
    diferença conservadora, porque em meio fisiológico a fadiga costuma ser igual ou inferior
    [fonte a indicar]. O meio do ensaio do Ti cp grau 4 não é indicado no artigo.
  - (b) O artigo não diz se o Ti-6Al-4V é ELI (O medido 0,07 %). O módulo do Ti-6Al-4V ELI
    continua a vir de Li et al. 2014 (Tabela 4, ELI).
  - (c) As ligas β (Ti-13Nb-13Zr e TNZT) continuam com outras fontes (Geetha 2009 e Li et al.
    2014), por isso o método de ensaio mistura-se nessas duas.
- Os módulos vêm de Li et al. 2014 (ligas de Ti) e de Navarro et al. 2008 (316L e Co-Cr-Mo).
  O Niinomi 1998 só tem ligas de Ti e deixou de ser fonte do 316L e do Co-Cr-Mo.

## Valores a verificar (fora de data/materiais.csv)
Os valores de propriedades "A verificar" estão na base e serão listados por
scripts/listar_por_verificar.py (tarefa 12). Aqui ficam os que não estão nessa coluna:
- [ ] Fonte para o alvo de E do osso cortical femoral (17 GPa) ou alinhamento com os 14 GPa do artigo-base (Petković et al. 2025).
  Pista: a folha Tecido da base (data/tecido.csv) dá 15-20 GPa (nota "slide 10"; fonte sugerida Ratner et al. 2020, Navarro et al. 2008: confirmar); o ponto médio é 17,5 GPa.
- [ ] Tipo de expansão dos stents (data/materiais.csv, 7 linhas "A verificar", sem referência).
- [ ] Estatuto clínico dos 8 materiais do scaffold (Clínico (substituto ósseo) / Clínico (uso limitado) / Investigação), proposto a 28 set 2026; fonte a verificar indicada na coluna notas de data/materiais.csv (Rezwan et al. 2006, Bose et al. 2012, Hench 1991, Woodruff & Hutmacher 2010, Athanasiou et al. 1996, base 510(k) da FDA; PCL/β-TCP e quitosano/HA sem fonte).

## Por preencher
- Fontes dos dados e critério de inclusão:
- Justificação final dos pesos e do η:
- Parâmetros do Monte Carlo:
- Limitações:
