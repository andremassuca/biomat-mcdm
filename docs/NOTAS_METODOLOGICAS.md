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
- Regra da porosidade (scaffold, 1 out 2026): as propriedades mecânicas de um scaffold usam-se à porosidade típica desse material (±10 pontos percentuais); valores medidos a porosidades muito diferentes ficam de fora ou só alargam o intervalo, com nota. Exemplo: na HA porosa (típico 65 %) entram os valores de resistência a 60 % e a ~70 %, e ficam de fora os de 40 % e de 80 %.
- Regra do típico (scaffold, 1 out 2026): típico = mediana das fontes dentro da janela de porosidade (porosidade típica do material ±10 pontos percentuais); o intervalo vai do mínimo ao máximo dessas fontes. Com uma só fonte na janela, o típico é o valor dessa fonte e a nota diz "uma só fonte".
- HA não reabsorvível (scaffold, 1 out 2026): o tempo de degradação da HA segue a lógica da opção O2 do stent: mínimo 42 meses (sem reabsorção em 3,5 anos) e máximo e típico iguais ao pior valor observado nos outros materiais do scaffold (60 meses, PLLA). É um valor de modelação e subestima a permanência real da HA.
- PLLA do scaffold = scaffold impresso ou extrudido; as espumas têm módulo 1 a 2 ordens de grandeza abaixo.
- Bioatividade (scaffold, 1 out 2026): a rubrica segue a classificação de Hench (classe A, osteoprodutivo, nota 5; classe B, osteocondutor, nota 4); a HA e o β-TCP ficam com 4 e o vidro 45S5 com 5.
- Densidade removida como proxy de radiopacidade (depende do número atómico efetivo e da espessura). Com a rubrica de radiopacidade (data/leia_me.md, 1 out 2026), a densidade continua a não ser critério do stent, mas serve de evidência de apoio para a ordem da radiopacidade (Allocco 2010, doi:10.1186/1745-6215-11-1).
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
- P-foco (3 out 2026): problema crítico de cada dispositivo indicado pelo professor (2 out 2026). O peso dos critérios ligados ao problema (data/problemas_criticos.csv) é multiplicado por fator_foco_problema = 2 (valor de desenho) e os pesos são renormalizados. Resultado principal: só critérios de ligação direta; sensibilidade: direta + indireta. Scaffold: leitura literal do professor no resultado principal (porosidade, bioatividade, tempo de degradação); a resistência, o módulo e a imprimibilidade entram só na sensibilidade (decisão do André, 3 out). Par articular: sensibilidade semiquantitativa à parte (results/semiquantitativos.csv). Mapa e resultados em relatorio/apoio/problemas_criterios.md.
- O-orçamento (3 out 2026): exclui na triagem os materiais com custo relativo acima de teto_custo_relativo = 3 (valor de desenho), sem mudar os pesos; cenário A dos três casos quantitativos. Sai o Ti-13Nb-13Zr (haste), o Pt-Cr (stent) e o vidro 45S5 (scaffold); o vencedor só muda no stent (L605 nos três métodos).
- Consenso de Borda (3 out 2026): cada método dá (m - posição) pontos; ranking pela soma; empate desempatado pela posição no TOPSIS (pipeline.consenso_borda). Cenário A: Ti-6Al-4V ELI, Pt-Cr (8 contra 7 do L605) e PCL/β-TCP; cenário B: Ti-6Al-4V ELI, L605 e PCL/β-TCP.
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

## Posições próximas no TOPSIS (regra de desempate, 30 set 2026)
- Se a diferença de C (coeficiente de proximidade do TOPSIS) entre duas posições consecutivas for
  < 0,01, essas posições consideram-se indistinguíveis e reportam-se como empate.
- Haste, cenário A (depois do commit 80ef2a3): 2.º Co-Cr-Mo forjado C = 0,577; 3.º Ti-13Nb-13Zr
  C = 0,532; diferença 0,045 (> 0,01), por isso os dois lugares distinguem-se. No WASPAS e no VIKOR
  o 2.º lugar é o Ti-13Nb-13Zr: o 2.º lugar depende do método.
- η = 0 na eq. 1 (w_j = η · w_j^S + (1 - η) · w_j^O) corresponde a pesos só objetivos (método do
  desvio-padrão); η = 1 a pesos só subjetivos (src/biomat_mcdm/weights.py, combine_weights).
- O Monte Carlo (propriedades e W pesos ±20 %) corre só no cenário A; o TNZT (só no cenário B)
  não entra no Monte Carlo.

## Incerteza dos valores únicos no Monte Carlo (30 set 2026)
- Valores de um único estudo não têm incerteza zero. No MC propriedades, as células
  quantitativas com mín. = máx. passam a variar ±10 % à volta do típico
  (data/parametros.csv, incerteza_valor_unico = 0,10; robustness.alargar_valores_unicos).
  Os ordinais não variam. ±10 % é um valor de desenho.
- Com e sem esta variação, o 1.º lugar da haste é 100 % nos três métodos (teste de 30 set 2026),
  arredondado a uma casa decimal; o valor exato com a variação é 99,99 % no TOPSIS (1 iteração
  em 10 000 com o Co-Cr-Mo forjado) e 100 % no WASPAS e no VIKOR. Nos três casos (haste, stent,
  scaffold) o vencedor do Monte Carlo não muda; no stent, o 1.º lugar do Co-Cr L605 desce
  ligeiramente (TOPSIS 96,8 → 94,8 %; WASPAS 87,8 → 87,7 %; VIKOR 95,7 → 94,6 %).

## Fratura cerâmica e squeaking: fontes (30 set 2026)
- Texto completo confirmado:
  - Hallan G, Fenstad AM, Furnes O. Clin Orthop Relat Res 2020;478(6):1254-1261,
    doi:10.1097/CORR.0000000000001272 (registo norueguês, 1997-2017, mediana 6,3 anos):
    fratura com revisão em 0,15 % das cabeças de alumina (IC 95 % 0,11 a 0,20) e 0,01 % das
    de AMC/BIOLOX delta (IC 95 % 0,002 a 0,09); HR ajustado 14,1. Só conta fraturas com revisão.
    Liners (confirmado no texto completo a 3 out 2026, secção de resultados): fratura do liner em
    8 doentes com CoC (seis de alumina, um de AMC, um de zircónia), incidência global de 0,14 %
    (CeramTec 0,08 %; Morgan 0,24 %); poucos casos para análise estatística. PDF em
    helse-bergen.no (Nasjonal kompetansetjeneste for leddproteser og hoftebrudd).
  - Zhao CC, Qu GX, Yan SG, Cai XZ. J Orthop Surg Res 2018;13:133, doi:10.1186/s13018-018-0841-y
    (meta-análise, CoC de 4.ª geração, 14 estudos): squeaking em cerca de 3 % (I² = 87 %).
- Apoio, só resumo:
  - Howard DP et al. Bone Joint J 2017;99-B(8):1012-1019 (NJR, só CoC): cabeças Delta 0,009 %,
    Forte 0,119 %; liners Delta 0,126 %, Forte 0,112 %.
  - Owen DH et al. Bone Joint J 2014;96-B(2):181-187 (meta-análise e AOANJRR): squeaking 4,2 %;
    revisão por squeaking 0,2 %.
  - Stanat SJ, Capozzi JD. J Arthroplasty 2012;27(3):445-453 (meta-análise, 3.ª e 4.ª geração):
    squeaking 2,4 %.
- Não usar sem ir à fonte primária: Massin P et al. Orthop Traumatol Surg Res 2014;100(6 Suppl):
  S317-S321 (cabeças Delta 0,003 % e alumina 0,021 %): valores do fabricante (CeramTec),
  conflito de interesses.
- O risco de fratura é um critério estrito sem regra numérica: estas fontes ficam na tabela de
  apoio do par articular e no texto, não em data/materiais.csv.

## Fontes do texto da anca (30 set 2026)
- Q2, ciclos de marcha: Silva M, Shepherd EF, Jackson WO, Dorey FJ, Schmalzried TP. Average patient
  walking activity approaches 2 million cycles per year: pedometers under-record walking activity.
  J Arthroplasty 2002;17(6):693-697, doi:10.1054/arth.2002.32699. "The SAM recorded an average of
  1.9 million cycles/y" (33 doentes, acelerómetro no tornozelo). Só resumo.
- Q2, forças na marcha: Bergmann G, Deuretzbacher G, Heller M, Graichen F,
  Rohlmann A, Strauss J, Duda GN. Hip contact forces and gait patterns from routine activities.
  J Biomech 2001;34(7):859-871, doi:10.1016/S0021-9290(01)00040-9. O resumo dá 238 % do peso
  corporal na marcha a cerca de 4 km/h (4 doentes), 251 % a subir e 260 % a descer escadas, e só
  menciona o tropeção ("except during stumbling") sem valor. Só resumo.
- Q2, tropeção: Bergmann G, Graichen F, Rohlmann A. Hip joint contact forces during stumbling.
  Langenbecks Arch Surg 2004;389(1):53-59, doi:10.1007/s00423-003-0434-y (PMID 14625775): "Peak forces
  are approximately twice as high during real stumbling as during any other activity and may range
  higher than eight-times the body weight". Só resumo.
- Q3, artefactos de RM: Månsson S, Müller GM, Wellman F, Nittka M, Lundin B. Phantom based
  qualitative and quantitative evaluation of artifacts in MR images of metallic hip prostheses.
  Phys Med 2015;31(2):173-178, doi:10.1016/j.ejmp.2014.12.001: haste de Ti com pontuações de
  artefacto 3 a 4 vezes mais baixas do que as de CoCr e aço (1,5 T, fantoma). Só resumo. Apoio:
  Radzi S et al. Quant Imaging Med Surg 2014;4(3):163-172 (PMC4032923): parafusos, 3,7 mm (Ti) vs
  10,9 mm (aço) a 1,5 T. Só resumo.
- Q6, corrosão no cone:
  - Goldberg JR, Gilbert JL, Jacobs JJ, Bauer TW, Paprosky W, Leurgans S. A multicenter retrieval
    study of the taper interfaces of modular hip prostheses. Clin Orthop Relat Res 2002;(401):149-161,
    doi:10.1097/00003086-200208000-00018: 231 explantes; corrosão moderada a grave em 42 % das
    cabeças de ligas mistas vs 28 % de ligas iguais. Lido só no resumo; o resultado (mais corrosão
    com ligas mistas) está no resumo; "mixed alloy" na literatura de explantes = cabeça CoCr sobre
    colo de Ti (definição não escrita no resumo do Goldberg nem no texto do Cooper 2012 [fonte a indicar]).
  - Cooper HJ, Della Valle CJ, Berger RA, Tetreault M, Paprosky WG, Sporer SM, Jacobs JJ. Corrosion
    at the head-neck taper as a cause for adverse local tissue reactions after total hip arthroplasty.
    J Bone Joint Surg Am 2012;94(18):1655-1661, doi:10.2106/JBJS.K.01352 (PMC3444948): ALTR em pares
    metal-polietileno por corrosão no cone; 3 dos 10 casos com haste de Ti e cabeça de Co. Texto completo.
- Q6, MoM:
  - MHRA. Medical Device Alert MDA/2010/069: DePuy ASR hip replacement implants, 7 set 2010
    ("Recall of ASR hip replacement implants due to increased rates of revision"; substitui a
    MDA/2010/044). Lido na cópia em PDF alojada pela Medsafe (Nova Zelândia):
    https://www.medsafe.govt.nz/hot/RecallActionNoticesNew/MetalOnMetalHipImplants/MHRA%20MDA-2010-069.pdf
    O URL original no gov.uk ou no UK Government Web Archive não foi encontrado.
  - FDA, Class 2 Device Recall, evento 57177 (ex.: Z-1749-2011), iniciada a 23 ago 2010:
    https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm?id=95530
  - Chalmers BP, Perry KI, Taunton MJ, Mabry TM, Abdel MP. Diagnosis of adverse local tissue reactions
    following metal-on-metal hip arthroplasty. Curr Rev Musculoskelet Med 2016;9(1):67-74,
    doi:10.1007/s12178-016-9321-3 (PMC4762796). Texto completo.
- Q9, fadiga do Ti-6Al-4V por EBM: Hrabe N, Gnäupel-Herold T, Quinn T. Fatigue properties of a
  titanium alloy (Ti-6Al-4V) fabricated via electron beam melting (EBM): effects of internal defects
  and residual stress. Int J Fatigue 2017;94(Part 2):202-210, doi:10.1016/j.ijfatigue.2016.04.022
  (NIST, https://www.nist.gov/node/1186311): 200-250 MPa no estado de fabrico, 550-600 MPa após HIP;
  20 Hz, R = 0,1. Resumo na página do NIST; texto completo na versão de conferência do NIST
  (https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=921698).
- Q10 e Q11, normas (iso.org e store.astm.org, consultadas a 30 set 2026): ISO 7206-4:2010 + Amd 1:2016;
  ISO 7206-6:2013; ISO 7206-10:2018 + Amd 1:2021; ISO 14242-1:2014 + Amd 1:2018; ISO 14242-2:2016;
  ASTM F2129-25, F1875-26, F2052-21, F2213-25, F2182-19e2, F2119-24; ASTM F2102-17(2026) (guia).
  - ISO 7206-6:2013 em revisão (DIS em votação desde jul 2026): voltar a verificar a 7 out.
  - ISO 14242-1 e 14242-2 também na etapa "to be revised"; voltar a verificar a 7 out.

## Stent: fontes e regras (30 set 2026)
- Regra da forma (revista a 2 out 2026): nas propriedades dependentes da forma, o mínimo, o máximo
  e o típico cobrem só a forma usada no dispositivo. No stent (cortado a laser de tubo), essa forma
  é o tubo ou a fita; os valores de outras formas (fio, barra, chapa) ficam só na nota da linha,
  para registo, e não entram no intervalo do Monte Carlo. Se a forma do dispositivo tiver um único
  valor, mín. = máx. e aplica-se a regra dos valores únicos (±10 % à volta do típico,
  incerteza_valor_unico em parametros.csv).
  Quando a ficha não diz se o valor é típico ou mínimo de especificação, a nota di-lo.
  - Versão anterior (30 set): as outras formas alargavam o intervalo (ex.: alongamento do MP35N
    40-70 % por causa do fio). Foi abandonada porque o Monte Carlo sorteava valores que o tubo
    não atinge.
  - Linhas revistas a 2 out: L605 módulo 225-243 → 225 (único); L605 tração 900-1138 → 900-1000;
    L605 alongamento 40-50 → 40 (único); MP35N tração 931-965 → 965 (único); MP35N alongamento
    40-70 → 40 (único). Sem alteração: 316L alongamento 40-50 (as duas fontes são de tubo) e L605
    cedência 380-700 (intervalo da fita). Os típicos não mudaram.
  - Exceção mantida (decisão de 30 set): no L605, o típico da cedência (476 MPa) e da tração
    (996 MPa) é o da chapa (Haynes), por não haver ficha de tubo com valores; os dois ficam dentro
    do intervalo da fita (Matthey).
- A espessura de strut é uma propriedade do dispositivo, não do material; a diferença entre o MP35N
  (Resolute, 90 µm) e o L605 (XIENCE, 81 µm) reflete o desenho do stent, não uma limitação da liga.
  Discutir no texto.
- Tempos de reabsorção do PLLA (Absorb) e do Mg (Magmaris): as fontes encontradas são de modelos
  animais (porco); o Seguchi 2023 é pré-clínico (mini-porcos), não humano. Magmaris: 12-24 meses,
  típico 18 (ponto médio, por coerência com o PLLA).
- Desde 30 set 2026, os métodos usam a coluna "tipico" de materiais.csv (ponto médio quando está
  vazia; src/biomat_mcdm/io.py, DecisionProblem.X_tipico); o Monte Carlo continua a sortear entre o
  mín. e o máx. Um típico fora de [mín., máx.] dá erro. Haste, scaffold e reprodução de Petković
  et al. 2025 ficaram iguais (o típico era o ponto médio). O σy/E derivado usa agora σy típico / E típico.

## Fontes do texto do stent (1 out 2026)
Referências das frases de relatorio/caso_stent_rascunho.md. "Só resumo" quando o texto completo não foi lido.
As normas ASTM foram lidas na loja oficial (store.astm.org) e as ISO em catálogos de organismos nacionais, porque
astm.org e iso.org não abriram.
- Ciclos e durabilidade (Q2, Q10): ASTM F2477-24, Standard Test Methods for in vitro Pulsatile Durability Testing of
  Vascular Stents and Endovascular Prostheses (o âmbito da edição F2477-19 indicava 10 anos a 72 batimentos por
  minuto, pelo menos 380 milhões de ciclos; o da F2477-24 já não traz o número). FDA. Non-Clinical Engineering
  Tests and Recommended Labeling for Intravascular Stents and Associated Delivery Systems. 18 abr 2010,
  https://www.fda.gov/media/71639/download (recomenda o equivalente a dez anos; não indica número de ciclos).
- Espessura de strut e reestenose (Q2): Kastrati A, Mehilli J, Dirschinger J, et al. Intracoronary stenting and
  angiographic results: strut thickness effect on restenosis outcome (ISAR-STEREO) trial. Circulation
  2001;103:2816-2821, doi:10.1161/01.CIR.103.23.2816 (texto completo; reestenose 15,0 % com 50 µm e 25,8 % com
  140 µm). Pache J, Kastrati A, Mehilli J, et al. (ISAR-STEREO-2). J Am Coll Cardiol 2003;41:1283-1288,
  doi:10.1016/S0735-1097(03)00119-0 (só resumo; 17,9 % e 31,4 %). O ensaio mede reestenose, não lesão da parede.
- Alergia ao níquel (Q3): Köster R, Vieluf D, Kiehn M, et al. Nickel and molybdenum contact allergies in patients
  with coronary in-stent restenosis. Lancet 2000;356:1895-1897, doi:10.1016/S0140-6736(00)03262-1 (só resumo).
  Gong Z, Li M, Guo X, et al. Stent implantation in patients with metal allergy: a systemic review and
  meta-analysis. Coron Artery Dis 2013;24:684-689, doi:10.1097/MCA.0b013e3283647ad1 (só resumo; apoia a
  associação). Norgaz T, Hobikoglu G, Serdar ZA, et al. Is there a link between nickel allergy and coronary stent
  restenosis? Tohoku J Exp Med 2005;206:243-246, doi:10.1620/tjem.206.243 (só resumo; 43 doentes, sem relação).
- Absorb (Q5): FDA, carta aos profissionais de saúde de 18 mar 2017 e atualização de 31 out 2017 (vendas paradas a
  14 set 2017; a FDA não indica o motivo). Kereiakes DJ, Ellis SG, Metzger C, et al. 3-Year Clinical Outcomes With
  Everolimus-Eluting Bioresorbable Coronary Scaffolds: The ABSORB III Trial. J Am Coll Cardiol 2017;70:2852-2862,
  doi:10.1016/j.jacc.2017.10.010 (só resumo; trombose do dispositivo 2,3 % e 0,7 %). Ke J, Zhang H, Huang J, et al.
  Three-year outcomes of bioresorbable vascular scaffolds versus second-generation drug-eluting stents. Medicine
  (Baltimore) 2020;99:e21554, doi:10.1097/MD.0000000000021554 (meta-análise, texto completo; struts de 157 µm).
- Struts do 316L (Q8): Nikam N, Steinberg TB, Steinberg DH. Advances in stent technologies and their effect on
  clinical efficacy and safety. Med Devices (Auckl) 2014;7:165-178, doi:10.2147/MDER.S31869 (revisão, texto
  completo, Tabela 1: Express 132 µm, Cypher 140 µm). O limite de 100 µm não tem fonte e saiu.
- Fabrico do stent de magnésio (Q9): Moravej M, Mantovani D. Biodegradable metals for cardiovascular stent
  application: interests and new opportunities. Int J Mol Sci 2011;12:4250-4270, doi:10.3390/ijms12074250
  (revisão, texto completo). Rapetto C, Leoncini M. Magmaris: a new generation metallic sirolimus-eluting fully
  bioresorbable scaffold. J Thorac Dis 2017;9(Suppl 9):S903-S913, doi:10.21037/jtd.2017.06.34 (revisão, texto
  completo). "Tubo extrudido" e o papel do revestimento na corrosão inicial não têm fonte e saíram.
- Normas (Q10): ISO 25539-2:2020, Cardiovascular implants, Endovascular devices, Part 2: Vascular stents. ASTM
  F2079-09(2022), Standard Test Method for Measuring Intrinsic Elastic Recoil of Balloon-Expandable Stents. ASTM
  F3067-26, Standard Guide for Radial Loading of Balloon-Expandable and Self-Expanding Vascular Stents. Edições em
  vigor das outras normas do mesmo parágrafo: ASTM F2129-25, F2052-21, F2213-25, F2182-19e2 e F2119-24; ISO
  10993-4:2017; ISO 11135:2014.

## Implante dentário: fontes da osteointegração e da corrosão (3 out 2026)
- Pesquisa com dois subagentes; 37 DOIs confirmados na Crossref ou no Europe PMC. Quase tudo lido só no resumo (estado "Verificado" com a nota "só resumo", decisão do André); texto completo só em Müller 2015 e Roehling 2026 (financiamento), Kurtz e Devine 2007 e Grandin 2012.
- Osteointegração (sobrevivência clínica): Adell 1990 (Ti cp, 15 anos); Howe 2019 (meta-análise, 10 anos); Müller 2024 (RCT TiZr vs Ti grau IV, 10 anos, patrocínio Straumann); Altuna 2016 (TiZr); Pieralli 2017 e Roehling 2018 (zircónia, 1-5 anos); Roehling 2026 (zircónia de uma peça, 10 anos, financiado pela Straumann); Herber 2025 e Steyer 2021 (outros sistemas de zircónia, 62-80 %); Morton 2018 (consenso ITI); Shah 2016 e Johansson 1998 (Ti-6Al-4V); Najeeb 2016 e Mishra 2019 (PEEK, só pré-clínico). BIC em animal sem diferença clara entre Ti, TiZr e zircónia (Gottlow 2012; Gahlert 2012; Manzano 2014).
- Corrosão: Nakagawa 1999 e 2001, Matono 2006, Huang 2003 (fluoretos); Apaza-Bedoya 2017, Stimmelmayr 2012, Corne 2019, Taher 2003 (ligação implante-pilar, galvânica); Safioti 2017, Olmedo 2013, Mombelli 2018 (partículas de Ti e peri-implantite: associação, sem causalidade provada); Chevalier 2006 e 2009, Lughi 2010, Kocjan 2021, Kohal 2025 (envelhecimento da Y-TZP); Kurtz e Devine 2007, Liebermann 2016 (PEEK); Akimoto 2018, Santos 2023, Grandin 2012 (Ti-Zr).
- Por confirmar: limiar de pH e fluoreto no texto completo de Nakagawa 1999; Ti-6Al-4V vs Ti cp com fluoreto (só resumo de Nakagawa 2001); Roxolid sem dados com fluoreto nem ensaio eletroquímico com a composição comercial; unidades de Safioti 2017; grau do Ti cp em Adell 1990; conflitos de interesse de Roehling 2018, Altuna 2016, Gottlow 2012, Kohal 2025, Corne 2019 e Kocjan 2021; séries clínicas com Ti-6Al-4V identificada no corpo do implante.
- Peso ordinal do dentário passa a 0,70: o caso continua semiquantitativo (indicação, não resultado).
- Tabela de apoio: relatorio/apoio/dentario_apoio.md.

## Fontes da introdução e da comparação com a prática clínica (3 out 2026)
- Confirmadas na Crossref: Jahan A, Ismail MY, Sapuan SM, Mustapha F. Material screening and choosing methods: a review. Mater Des 2010;31(2):696-705, doi:10.1016/j.matdes.2009.08.013; Jahan A, Bahraminasab M, Edwards KL. A target-based normalization technique for materials selection. Mater Des 2012;35:647-654, doi:10.1016/j.matdes.2011.09.005; Lodewijks et al. Eur J Trauma Emerg Surg 2025, doi:10.1007/s00068-025-02982-9 (seguimento a longo prazo de PCL/TCP impresso em defeitos segmentares).
- Ashby MF. Materials Selection in Mechanical Design, 5.ª ed. Elsevier (Butterworth-Heinemann), 2017, ISBN 978-0-08-100599-6 (edição confirmada na página da Elsevier; a 4.ª ed., 2011, tem doi:10.1016/C2009-0-25539-5).
- Não encontrada: a referência "Chua 2025" do rascunho do chat (sem registo na Crossref com esse autor e tema); substituída a 3 out 2026 por Lodewijks et al. Cureus 2024;16(8):e66256, doi:10.7759/cureus.66256 (defeitos tibiais muito grandes tratados com PCL/TCP impresso; confirmado na Crossref), na discussão (8.5) e no caso do scaffold.
- Heliyon 2025, "Editor Note" sobre Wang Y et al. Heliyon 2024;10:e26071 (doi:10.1016/j.heliyon.2025.e44205): conteúdo não confirmado (página da revista com acesso bloqueado; sem correção, manifestação de preocupação ou retratação associada no PubMed (PMID 38468962), no PMC (PMC10925999) nem na Crossref, incluindo os dados do Retraction Watch, consultados a 3 out 2026). A Tabela 3 do artigo dá uma resistência à compressão (27,9 MPa) quase igual ao módulo (48,2 MPa), pouco plausível num scaffold poroso. Decisão do André: retirado da base; módulo do PCL/β-TCP com a mediana das três fontes restantes (típico 35,7 → 23,1 MPa; mín. e máx. iguais). Efeito: rankings e ΔC iguais; pontuações do WASPAS e do VIKOR mudam na 3.ª casa; MC das propriedades igual; W pesos ±20 %: compósito 95,9 → 95,7 % no TOPSIS. Se a revista esclarecer que é só uma correção, pode voltar.
- Registos (PDFs em fontes/): NJR 23rd Annual Report 2026, Hips (ISSN 2054-183X, dados até 31 dez 2025): Tabela 3.H2 (pp. 37-38), fixação em 2025: não cimentada 42,5 %, híbrida 41,8 %, cimentada 12,3 %; superfícies de apoio em 2025 (somas de valores arredondados): cerâmica/PE cerca de 59 %, metal/PE cerca de 33 %, CoC cerca de 2 %, dupla mobilidade cerca de 5 %; Tabela 3.H3 e p. 46: CoC em doentes mais novos (mediana 59-60 anos contra 70 no total). O NJR não distingue o PE reticulado nestas tabelas. AOANJRR 2025 Annual Report (Lewis PL et al., doi:10.25310/MXFR3061): fixação em 2024 na prótese total convencional: não cimentada 62,9 %, híbrida 35,7 %, cimentada 1,4 % (Figura HT3, p. 255-256); 97 % com par "moderno" (XLPE ou cerâmica mista) (p. 303). Nenhum registo reporta o material da haste.
- Material das hastes não cimentadas: Hu e Yoon 2018 (Biomater Res, doi:10.1186/s40824-018-0144-8); hastes cimentadas polidas de aço inoxidável em uso: Lamb JN et al. PLOS Med 2025;22(11):e1004538, doi:10.1371/journal.pmed.1004538 (só resumo). Khanuja et al. JBJS Am 2011;93:500-509 (doi:10.2106/JBJS.J.00774): DOI certo, conteúdo não lido.
- Stents: Brami P et al. J Clin Med 2023;12:6711 (secção 2: "stainless steel was abandoned for cobalt-chromium and platinum-chromium alloys"; Tabela 1: 9 plataformas atuais de CoCr ou PtCr, struts de 55 a 89 µm); Macaya-Ten F et al. REC Interv Cardiol 2024 (Tabela 3: Cypher e Taxus em aço inoxidável; retirada faseada). Nenhuma escreve "316L".

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
