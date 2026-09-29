# Par articular: tabela de apoio (semiquantitativo, sem ranking)

Gerado a partir de data/materiais.csv, data/criterios.csv e da triagem (src/biomat_mcdm/screening.py) a 29 set 2026. Valores: típico (mín.-máx.). Não se calcula ranking: o caso é semiquantitativo (ordinais > 50 % do peso).

## 1. Critérios

| Critério | Tipo | Regra ou peso | Unidade | Justificação |
|---|---|---|---|---|
| Segurança iónica / risco ALTR (ordinal 1-5) | Estrito | ≥ 2 | - | Triagem: elimina o MoM (segurança não é compensável) |
| Risco de fratura da cabeça cerâmica | Estrito | Avaliação qualitativa | - | K_IC retirado da matriz; discutido no texto |
| Taxa de desgaste linear | Custo | 0,35 | mm/ano | SEMIQUANTITATIVO (ordinais > 50 %). Partículas → osteólise |
| Segurança iónica / risco ALTR (ordinal 1-5) | Benefício | 0,25 | - | Lição do MoM |
| Dureza da cabeça | Benefício | 0,05 | HV | Riscos por terceiro corpo |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | Benefício | 0,15 | - | Corrosão na junção (trunnionosis) |
| Compatibilidade com esterilização (ordinal 1-5) | Benefício | 0,05 | - | Oxidação do PE irradiado |
| Compatibilidade com RM (ordinal 1-5) | Benefício | 0,05 | - |  |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | Custo | 0,1 | - |  |

Peso dos critérios ordinais (inclui o custo relativo 1-5): 0,6; medidos (desgaste, dureza): 0,4.

## 2. Critérios estritos (triagem)

| Par | Segurança iónica ≥ 2 | Risco de fratura da cabeça cerâmica | Passa a triagem? |
|---|---|---|---|
| CoCrMo / UHMWPE convencional (MoP) | aprovado (4) | não avaliado (avaliação qualitativa no texto) | Sim (fratura: não avaliada, só no texto) |
| CoCrMo / HXLPE (MoXLPE) | aprovado (4) | não avaliado (avaliação qualitativa no texto) | Sim (fratura: não avaliada, só no texto) |
| ZTA / HXLPE (CoXLPE) | aprovado (5) | não avaliado (avaliação qualitativa no texto) | Sim (fratura: não avaliada, só no texto) |
| ZTA / ZTA (CoC) | aprovado (5) | não avaliado (avaliação qualitativa no texto) | Sim (fratura: não avaliada, só no texto) |
| CoCrMo / CoCrMo (MoM) | eliminado (1) | não avaliado (avaliação qualitativa no texto) | Não (eliminado) |

O risco de fratura cerâmica não tem regra numérica (K_IC retirado da matriz): o código regista-o como "não avaliado" e não elimina nenhum par. Só se aplica aos pares com cabeça ou acetábulo em ZTA (CoXLPE e CoC).

## 3. Valores por par (típico, mín.-máx.)

| Critério | Unidade | CoCrMo / UHMWPE convencional (MoP) | CoCrMo / HXLPE (MoXLPE) | ZTA / HXLPE (CoXLPE) | ZTA / ZTA (CoC) | CoCrMo / CoCrMo (MoM) |
|---|---|---|---|---|---|---|
| Taxa de desgaste linear | mm/ano | 0,077 (0,04-0,106) | 0,0161 (0,011-0,0212) | 0,038 (0,032-0,044) | 0,0041 (0,0019-0,0063) | 0,0054 (0,0035-0,0073) |
| Segurança iónica / risco ALTR (ordinal 1-5) | - | 4 | 4 | 5 | 5 | 1 |
| Dureza da cabeça | HV | 340 (312-368) | 340 (312-368) | 1937 | 1937 | 340 (312-368) |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | - | 3 | 3 | 5 | 5 | 2 |
| Compatibilidade com esterilização (ordinal 1-5) | - | 2 | 4 | 4 | 5 | 5 |
| Compatibilidade com RM (ordinal 1-5) | - | 3 | 3 | 5 | 5 | 2 |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 1 | 2 | 3 | 4 | 3 |

## 4. Fontes e estado

| Critério | Par | Fonte (referencia) | doi_url | Estado | Nota |
|---|---|---|---|---|---|
| Taxa de desgaste linear | CoCrMo / UHMWPE convencional | Teeter MG, Yuan X, Somerville LE, MacDonald SJ, McCalden RW, Naudie DD. Thirteen-year wear rate comparison of highly crosslinked and conventional polyethylene in total hip arthroplasty. Can J Surg 2017;60(3):212-216 | https://doi.org/10.1503/cjs.005216 | Verificado | in vivo, RSA; CoCr 28 mm contra PE convencional (Trilogy, Zimmer); ensaio aleatorizado, n = 8 por braço aos 13,6 anos; rodagem incluída; mín.-máx. = intervalo; sem rodagem (primeiros 5 anos): 0,051 ± 0,022 mm/ano; Glyn-Jones 2015 (RSA): 0,030 mm/ano em regime estacionário, cabeça não indicada; mistura de métodos: RSA neste par, radiografia simples nos restantes |
| Taxa de desgaste linear | CoCrMo / HXLPE | Higuchi Y, Seki T, Morita D, Komatsu D, Takegami Y, Ishiguro N. Comparison of wear rate between ceramic-on-ceramic, metal on highly cross-linked polyethylene, and metal-on-metal bearings. Rev Bras Ortop 2019;54(3):295-302, Tabela 4 | https://doi.org/10.1055/s-0039-1691762 | Verificado | in vivo, radiografia simples (AP); CoCr contra HXLPE Crossfire (Stryker); n = 77; 7,6 anos; média ± DP; rodagem incluída; sem rodagem (true wear): 0,0096 mm/ano |
| Taxa de desgaste linear | ZTA / HXLPE | Kim YH, Park JW. Eighteen-Year Results of Cementless THA with Alumina-on-HXLPE Bearings in Patients <30 Years Old. J Bone Joint Surg Am 2020;102(14):1255-1259 | https://doi.org/10.2106/JBJS.19.01157 | Verificado | alumina BIOLOX forte, não ZTA; doentes < 30 anos (muito ativos): pior caso; não comparável com o MoXLPE, porque os estudos, os polietilenos e os métodos são diferentes; in vivo, radiografia simples (AP, AutoCAD); 28 mm contra HXLPE Marathon (DePuy); cerca de 54 ancas; 17,8 anos; média ± DP; tratamento da rodagem não explicado; Weishorn 2023: 0,059 ± 0,031 mm/ano sem rodagem (Biolox sem geração indicada, contra Durasul); Dahl 2013 (RSA, PE convencional): a cabeça de alumina desgastou o PE menos de metade da CoCr (0,62 vs 1,40 mm aos 10 anos), única comparação cerâmica vs CoCr no mesmo estudo |
| Taxa de desgaste linear | ZTA / ZTA | Higuchi Y, Seki T, Morita D, Komatsu D, Takegami Y, Ishiguro N. Comparison of wear rate between ceramic-on-ceramic, metal on highly cross-linked polyethylene, and metal-on-metal bearings. Rev Bras Ortop 2019;54(3):295-302, Tabela 4 | https://doi.org/10.1055/s-0039-1691762 | Verificado | alumina, não ZTA; a ZTA desgasta igual ou menos, logo é o pior caso; in vivo, radiografia simples (AP); BIOLOX forte; n = 105; 7,6 anos; média ± DP; rodagem incluída (sem rodagem: 0,0037 mm/ano); van Loon 2021 (BIOLOX delta, 32 mm, n = 25 aos 10 anos): mediana 0,000 mm/ano (0,000 a 0,005); valores abaixo da resolução da radiografia simples: a diferença entre CoC e MoM não é significativa |
| Taxa de desgaste linear | CoCrMo / CoCrMo | Higuchi Y, Seki T, Morita D, Komatsu D, Takegami Y, Ishiguro N. Comparison of wear rate between ceramic-on-ceramic, metal on highly cross-linked polyethylene, and metal-on-metal bearings. Rev Bras Ortop 2019;54(3):295-302, Tabela 4 | https://doi.org/10.1055/s-0039-1691762 | Verificado | in vivo, radiografia simples (AP); Pinnacle 28 e 36 mm; n = 55; 7,6 anos; média ± DP; rodagem incluída (sem rodagem: 0,0051 mm/ano); Sieber 1999 (explantes Metasul, n = 118): cerca de 25 µm/ano no 1.º ano e 5 µm/ano depois do 3.º [confirmar: só o resumo]; valores abaixo da resolução da radiografia simples: a diferença entre CoC e MoM não é significativa |
| Segurança iónica / risco ALTR (ordinal 1-5) | CoCrMo / UHMWPE convencional | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |  |
| Segurança iónica / risco ALTR (ordinal 1-5) | CoCrMo / HXLPE | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |  |
| Segurança iónica / risco ALTR (ordinal 1-5) | ZTA / HXLPE | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |  |
| Segurança iónica / risco ALTR (ordinal 1-5) | ZTA / ZTA | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |  |
| Segurança iónica / risco ALTR (ordinal 1-5) | CoCrMo / CoCrMo | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |  |
| Dureza da cabeça | CoCrMo / UHMWPE convencional | Fischer A, Weiß S, Wimmer MA. The tribological difference between biomedical steels and CoCrMo-alloys. J Mech Behav Biomed Mater 2012;9:50-62, Tabela 1 | https://doi.org/10.1016/j.jmbbm.2012.01.007 | Verificado | varão forjado, não cabeça femoral; HV10 = 340 ± 28 (mín.-máx. = média ± DP); CoCr29Mo6 de baixo carbono, ISO 5832-6 / ASTM F1537, solubilizado |
| Dureza da cabeça | CoCrMo / HXLPE | Fischer A, Weiß S, Wimmer MA. The tribological difference between biomedical steels and CoCrMo-alloys. J Mech Behav Biomed Mater 2012;9:50-62, Tabela 1 | https://doi.org/10.1016/j.jmbbm.2012.01.007 | Verificado | varão forjado, não cabeça femoral; HV10 = 340 ± 28 (mín.-máx. = média ± DP); CoCr29Mo6 de baixo carbono, ISO 5832-6 / ASTM F1537, solubilizado |
| Dureza da cabeça | ZTA / HXLPE | KYOCERA Medical Technologies. BIOLOX delta Ceramic (página de produto), Tabela 1; consultada a 29 set 2026 | https://medical.kyocera.com/joint/prdct/biolox-delta-ceramic.html | Verificado (fornecedor) | BIOLOX delta; fonte: página de distribuidor (Kyocera), não o fabricante: 19 GPa (HV1); conversão: 19 / 0,009807 = 1937 HV; apoio: Merkert 2008 (resumo de congresso): 1975 HV; DePuy (folheto): cerca de 2000 HV |
| Dureza da cabeça | ZTA / ZTA | KYOCERA Medical Technologies. BIOLOX delta Ceramic (página de produto), Tabela 1; consultada a 29 set 2026 | https://medical.kyocera.com/joint/prdct/biolox-delta-ceramic.html | Verificado (fornecedor) | BIOLOX delta; fonte: página de distribuidor (Kyocera), não o fabricante: 19 GPa (HV1); conversão: 19 / 0,009807 = 1937 HV; apoio: Merkert 2008 (resumo de congresso): 1975 HV; DePuy (folheto): cerca de 2000 HV |
| Dureza da cabeça | CoCrMo / CoCrMo | Fischer A, Weiß S, Wimmer MA. The tribological difference between biomedical steels and CoCrMo-alloys. J Mech Behav Biomed Mater 2012;9:50-62, Tabela 1 | https://doi.org/10.1016/j.jmbbm.2012.01.007 | Verificado | varão forjado, não cabeça femoral; HV10 = 340 ± 28 (mín.-máx. = média ± DP); CoCr29Mo6 de baixo carbono, ISO 5832-6 / ASTM F1537, solubilizado |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | CoCrMo / UHMWPE convencional | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar | Cabeça CoCr em cone de Ti: corrosão por fretting documentada |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | CoCrMo / HXLPE | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar | Idem |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | ZTA / HXLPE | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar | Cabeça cerâmica elimina o par galvânico |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | ZTA / ZTA | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar | Idem |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | CoCrMo / CoCrMo | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar | Fretting no cone + desgaste metálico na articulação |
| Compatibilidade com esterilização (ordinal 1-5) | CoCrMo / UHMWPE convencional | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar | PE convencional esterilizado por gama ao ar → oxidação (histórico) |
| Compatibilidade com esterilização (ordinal 1-5) | CoCrMo / HXLPE | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar | HXLPE refundido/recozido ou com vitamina E |
| Compatibilidade com esterilização (ordinal 1-5) | ZTA / HXLPE | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar | Idem |
| Compatibilidade com esterilização (ordinal 1-5) | ZTA / ZTA | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar | Cerâmicos e metais: sem limitações |
| Compatibilidade com esterilização (ordinal 1-5) | CoCrMo / CoCrMo | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar | Idem |
| Compatibilidade com RM (ordinal 1-5) | CoCrMo / UHMWPE convencional | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar | Cabeça CoCr (a haste também conta: ver nota metodológica) |
| Compatibilidade com RM (ordinal 1-5) | CoCrMo / HXLPE | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |  |
| Compatibilidade com RM (ordinal 1-5) | ZTA / HXLPE | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |  |
| Compatibilidade com RM (ordinal 1-5) | ZTA / ZTA | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |  |
| Compatibilidade com RM (ordinal 1-5) | CoCrMo / CoCrMo | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar | Duas superfícies CoCr |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | CoCrMo / UHMWPE convencional | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |  |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | CoCrMo / HXLPE | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |  |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | ZTA / HXLPE | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |  |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | ZTA / ZTA | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |  |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | CoCrMo / CoCrMo | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |  |

## 5. Estatuto e nota geral por par

| Par | Estatuto | Nota geral (materiais.csv) |
|---|---|---|
| CoCrMo / UHMWPE convencional (MoP) | Clínico | Osteólise por partículas de PE; corrosão na junção cabeça-cone |
| CoCrMo / HXLPE (MoXLPE) | Clínico | PE altamente reticulado; oxidação se radiação gama sem estabilização |
| ZTA / HXLPE (CoXLPE) | Clínico | Cerâmica na cabeça elimina corrosão na junção |
| ZTA / ZTA (CoC) | Clínico | Risco de fratura baixo mas não nulo; ruído (squeaking) |
| CoCrMo / CoCrMo (MoM) | Clínico (abandonado) | Iões Co/Cr, ALTR; recolha ASR 2010: candidato a eliminar na triagem |

## 6. Desgaste em simulador (só apoio; não entra em materiais.csv)

Unidade original: mm³ por milhão de ciclos (volume). Não é convertível para mm/ano nem comparável com os valores in vivo lineares da secção 3.

| Par | Rodagem | Estacionário | Global ou outra condição | Fonte | Condições |
|---|---|---|---|---|---|
| CoC (BIOLOX delta, 36 mm) | 0,163 ± 0,026 | 0,038 ± 0,012 | global 0,118 ± 0,036 | Reinders J et al. PLoS One 2013;8(8):e73252, Tabela 3, https://doi.org/10.1371/journal.pone.0073252 | ISO 14242-1; n = 4; 2,4 milhões de ciclos |
| MoM (CoCrMo de alto carbono, 28 mm) | média 0,99 (0 a 3 milhões de ciclos, 45°) | 0,44 | 2,65 a 65°; 4,14 a 5,47 em microsseparação | Al-Hajjar M et al. J Biomed Mater Res B 2013;101B(2):213-222, https://doi.org/10.1002/jbm.b.32824 | simulador Leeds II, não é estritamente ISO 14242; n = 3 por ângulo |
| MoM (36 mm) | não indicado | 0,17 | 0,35 a 45°; 0,37 a 65° | Al-Hajjar 2013 | idem |

## 7. Notas para a Q8

- Métodos misturados no desgaste in vivo: RSA no MoP (Teeter 2017); radiografia simples nos restantes pares.
- CoC vs MoM: os valores (cerca de 0,004 e 0,005 mm/ano) estão abaixo da resolução da radiografia simples; a diferença entre eles não é significativa.
- CoXLPE vs MoXLPE: não comparáveis (estudos, polietilenos, doentes e métodos diferentes); o CoXLPE é alumina BIOLOX forte em doentes < 30 anos (pior caso).
- Dahl et al. 2013 (Acta Orthop 84:360, https://doi.org/10.3109/17453674.2013.810516; RSA, 10 anos): única comparação cerâmica (alumina) vs CoCr no mesmo estudo, com polietileno convencional (GUR 1050 moldado por compressão, esterilizado por radiação gama em azoto): 0,62 vs 1,40 mm de desgaste proximal. Os autores dizem que a diferença pode ser menor com polietileno reticulado.
- Vitamina E: não está na base (nenhum par com HXLPE estabilizado com vitamina E).

## 8. Fratura de componentes cerâmicos e squeaking (critério estrito sem regra numérica; não entra em materiais.csv)

| Tema | Valor | Condições | Fonte | Texto completo? |
|---|---|---|---|---|
| Fratura da cabeça (com revisão) | alumina 0,15 % (IC 95 % 0,11-0,20); AMC/BIOLOX delta 0,01 % (IC 95 % 0,002-0,09); HR ajustado 14,1 | registo norueguês, 1997-2017, mediana 6,3 anos; 31 479 CoP e 5790 CoC; liners 0,14 % | Hallan G, Fenstad AM, Furnes O. Clin Orthop Relat Res 2020;478(6):1254-1261, https://doi.org/10.1097/CORR.0000000000001272 | sim |
| Fratura (componentes revistos) | cabeças Delta 0,009 %, Forte 0,119 %; liners Delta 0,126 %, Forte 0,112 % | NJR, só CoC, 111 681 PTA | Howard DP et al. Bone Joint J 2017;99-B(8):1012-1019, https://doi.org/10.1302/0301-620X.99B8.BJJ-2017-0019.R1 | só resumo |
| Fratura (dados do fabricante) | cabeças Delta 0,003 %, alumina 0,021 % | valores da CeramTec: conflito de interesses; não usar sem a fonte primária | Massin P et al. Orthop Traumatol Surg Res 2014;100(6 Suppl):S317-S321, https://doi.org/10.1016/j.otsr.2014.05.010 | só resumo |
| Squeaking | cerca de 3 % (I² = 87 %) | meta-análise, CoC de 4.ª geração, 14 estudos | Zhao CC et al. J Orthop Surg Res 2018;13:133, https://doi.org/10.1186/s13018-018-0841-y | sim |
| Squeaking | 4,2 %; revisão por squeaking 0,2 % | meta-análise (43 estudos, 16 828 CoC) e AOANJRR | Owen DH et al. Bone Joint J 2014;96-B(2):181-187, https://doi.org/10.1302/0301-620X.96B2.32784 | só resumo |
| Squeaking | 2,4 % (150/6137) | meta-análise, 3.ª e 4.ª geração, 12 estudos | Stanat SJ, Capozzi JD. J Arthroplasty 2012;27(3):445-453, https://doi.org/10.1016/j.arth.2011.04.031 | só resumo |
