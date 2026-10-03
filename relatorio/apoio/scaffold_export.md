# Scaffold ósseo: export de dados (commit 65551f3, 03/10/2026)

Gerado por scripts/exportar_caso.py a partir de data/, src/ e results/. Só dados.

## 1. Candidatos

| Material | Norma | Classe | Estatuto | Triagem | A | B |
|---|---|---|---|---|---|---|
| PCL | - | Polímero | Clínico (uso limitado) | aprovado | sim | sim |
| PLLA | - | Polímero | Investigação | aprovado |  | sim |
| PLGA 50:50 | - | Polímero | Investigação | aprovado |  | sim |
| Hidroxiapatite (HA) porosa | - | Cerâmico | Clínico (substituto ósseo) | aprovado | sim | sim |
| β-TCP poroso | - | Cerâmico | Clínico (substituto ósseo) | aprovado | sim | sim |
| Vidro bioativo 45S5 poroso | - | Vidro | Clínico (substituto ósseo, partículas) | aprovado | sim | sim |
| Compósito PCL/β-TCP (impressão 3D) | - | Compósito | Clínico (uso limitado) | aprovado | sim | sim |
| Quitosano/HA (liofilizado) | - | Compósito natural | Investigação | aprovado |  | sim |

Cenários aplicáveis (cenarios.csv):

- A: Só materiais em uso clínico (stent: só permanentes, 316L, L605, MP35N, Pt-Cr)
- B: Inclui investigação e bioabsorvíveis (stent: A + Mg WE43 e PLLA; permanentes com o pior valor observado no tempo de reabsorção, opção O2)
- Q: Só critérios quantitativos (sem ordinais)
- W: Sensibilidade dos pesos
- η: Sensibilidade ao nível de confiança η de 0 a 1, passo 0,1 (resultado principal: η = 1)
- M: Concordância entre métodos
- T-scaffold: Sensibilidade dos alvos
- C-custo: Peso do custo relativo baixo (0,01) vs elevado (0,25), restantes pesos redistribuídos
- MC: Incerteza das propriedades
- P-foco: Foco no problema crítico do professor (2 out 2026): peso dos critérios de ligação direta x2 (fator_foco_problema), restantes renormalizados; sensibilidade: direta + indireta (data/problemas_criticos.csv). Par articular: sensibilidade semiquantitativa à parte

## 2. Critérios (criterios.csv)

| Critério | Tipo | Alvo | Unidade | Peso | Justificação |
|---|---|---|---|---|---|
| Resistência à compressão (scaffold) | Alvo | 7 | MPa | 0,15 | Osso trabecular ~2-12 MPa: CENÁRIO de referência, ver folha Cenarios |
| Módulo de compressão (scaffold) | Alvo | 250 | MPa | 0,1 | Osso trabecular ~50-500 MPa: CENÁRIO de referência, ver folha Cenarios |
| Porosidade | Alvo | 70 | % | 0,15 | Poros interligados >100 µm; trabecular 50-90%: CENÁRIO de referência, ver folha Cenarios |
| Tempo de degradação | Alvo | 9 | meses | 0,15 | Acompanhar a regeneração óssea: CENÁRIO de referência, ver folha Cenarios |
| Bioatividade (ordinal 1-5) | Benefício |  | - | 0,15 | Osteocondução/ligação ao osso |
| Imprimibilidade 3D (ordinal 1-5) | Benefício |  | - | 0,1 | Controlo da arquitetura porosa |
| Compatibilidade com esterilização (ordinal 1-5) | Benefício |  | - | 0,1 | Polímeros de baixa Tf e hidrolisáveis |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | Custo |  | - | 0,1 |  |

Pesos no cenário A (renormalizados): Resistência à compressão (scaffold) 0,15; Módulo de compressão (scaffold) 0,1; Porosidade 0,15; Tempo de degradação 0,15; Bioatividade (ordinal 1-5) 0,15; Imprimibilidade 3D (ordinal 1-5) 0,1; Compatibilidade com esterilização (ordinal 1-5) 0,1; Custo relativo de material e fabrico (1-5, 5 = mais caro) 0,1

Pesos no cenário B (renormalizados): Resistência à compressão (scaffold) 0,15; Módulo de compressão (scaffold) 0,1; Porosidade 0,15; Tempo de degradação 0,15; Bioatividade (ordinal 1-5) 0,15; Imprimibilidade 3D (ordinal 1-5) 0,1; Compatibilidade com esterilização (ordinal 1-5) 0,1; Custo relativo de material e fabrico (1-5, 5 = mais caro) 0,1

Referência de tecido (tecido.csv, osso trabecular):

| Propriedade | Unidade | Mín. | Máx. | Fonte | Estado |
|---|---|---|---|---|---|
| Módulo de Young | MPa | 50 | 500 | Ratner et al. 2020; Navarro et al. 2008; Karageorgiou & Kaplan 2005: confirmar | A verificar |
| Resistência à compressão | MPa | 2 | 12 | Ratner et al. 2020; Navarro et al. 2008; Karageorgiou & Kaplan 2005: confirmar | A verificar |
| Porosidade | % | 50 | 90 | Ratner et al. 2020; Navarro et al. 2008; Karageorgiou & Kaplan 2005: confirmar | A verificar |

## 3. Valores (materiais.csv e índices derivados)

| Material | Propriedade | Unidade | Típico | Mín. | Máx. | Texto | Fonte | doi_url | Estado |
|---|---|---|---|---|---|---|---|---|---|
| Compósito PCL/β-TCP (impressão 3D) | Bioatividade (ordinal 1-5) | - | 3 | 3 | 3 |  | Bruyas A et al. J Mater Res 2018;33:1948-1959; rubrica segundo a classificação de Hench (LEIA-ME) | https://doi.org/10.1557/jmr.2018.112 | Verificado |
| Hidroxiapatite (HA) porosa | Bioatividade (ordinal 1-5) | - | 4 | 4 | 4 |  | Grandfield K et al. J R Soc Interface 2010;7:1497-1501; rubrica segundo a classificação de Hench (LEIA-ME) | https://doi.org/10.1098/rsif.2010.0213 | Verificado |
| PCL | Bioatividade (ordinal 1-5) | - | 1 | 1 | 1 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PLGA 50:50 | Bioatividade (ordinal 1-5) | - | 1 | 1 | 1 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PLLA | Bioatividade (ordinal 1-5) | - | 1 | 1 | 1 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Quitosano/HA (liofilizado) | Bioatividade (ordinal 1-5) | - | 3 | 3 | 3 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Vidro bioativo 45S5 poroso | Bioatividade (ordinal 1-5) | - | 5 | 5 | 5 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| β-TCP poroso | Bioatividade (ordinal 1-5) | - | 4 | 4 | 4 |  | Kotani S et al. J Biomed Mater Res 1991;25:1303-1315; rubrica segundo a classificação de Hench (LEIA-ME) | https://doi.org/10.1002/jbm.820251010 | Verificado |
| Compósito PCL/β-TCP (impressão 3D) | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | Bruyas A et al. Tissue Eng Part A 2019;25:248-256 | https://doi.org/10.1089/ten.tea.2018.0130 | Verificado |
| Hidroxiapatite (HA) porosa | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| PCL | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| PLGA 50:50 | Compatibilidade com esterilização (ordinal 1-5) | - | 2 | 2 | 2 |  | Holy CE, Cheng C, Davies JE, Shoichet MS. Biomaterials 2001;22:25-31 (Tabela 2) | https://doi.org/10.1016/S0142-9612(00)00136-8 | Verificado |
| PLLA | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Quitosano/HA (liofilizado) | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Vidro bioativo 45S5 poroso | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| β-TCP poroso | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | FDA 510(k) K032409 (Vitoss, Orthovita, 2003); FDA 510(k) K120152 (Cerasorb Plus, Riemser, 2012) | https://fda.innolitics.com/device/K032409 | Verificado (fornecedor) |
| Compósito PCL/β-TCP (impressão 3D) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 2 | 2 | 2 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Hidroxiapatite (HA) porosa | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 3 | 3 | 3 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| PCL | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 1 | 1 | 1 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| PLGA 50:50 | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 2 | 2 | 2 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| PLLA | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 1 | 1 | 1 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Quitosano/HA (liofilizado) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 2 | 2 | 2 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Vidro bioativo 45S5 poroso | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 4 | 4 | 4 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| β-TCP poroso | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 3 | 3 | 3 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Imprimibilidade 3D (ordinal 1-5) | - | 5 | 5 | 5 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Hidroxiapatite (HA) porosa | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PCL | Imprimibilidade 3D (ordinal 1-5) | - | 5 | 5 | 5 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PLGA 50:50 | Imprimibilidade 3D (ordinal 1-5) | - | 3 | 3 | 3 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PLLA | Imprimibilidade 3D (ordinal 1-5) | - | 4 | 4 | 4 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Quitosano/HA (liofilizado) | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Bergonzi C et al. Sci Rep 2019;9:362 | https://doi.org/10.1038/s41598-018-36613-8 | Verificado |
| Vidro bioativo 45S5 poroso | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| β-TCP poroso | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Módulo de compressão (scaffold) | MPa | 23,1 | 22,2 | 51,5 |  | Reichert JC et al. Int Orthop 2011;35:1229-1236; Kawai T et al. J Orthop Res 2018;36:1002-1011 | https://doi.org/10.1007/s00264-010-1146-x | Verificado |
| Hidroxiapatite (HA) porosa | Módulo de compressão (scaffold) | MPa | 1750 | 500 | 3000 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PCL | Módulo de compressão (scaffold) | MPa | 50 | 20 | 80 |  | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |  | A verificar |
| PLGA 50:50 | Módulo de compressão (scaffold) | MPa | 35 | 10 | 60 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PLLA | Módulo de compressão (scaffold) | MPa | 175 | 50 | 300 |  | Karanth D et al. Clin Exp Dent Res 2023;9:398-408; Yin HM et al. Polymers 2016;8:213 | https://doi.org/10.1002/cre2.712 | Verificado |
| Quitosano/HA (liofilizado) | Módulo de compressão (scaffold) | MPa | 0,76 | 0,08 | 0,8 |  | Gaihre B, Jayasuriya AC. Mater Sci Eng C 2018;91:330-339; Wang H et al. Heliyon 2024;10:e25832 | https://doi.org/10.1016/j.msec.2018.05.060 | Verificado |
| Vidro bioativo 45S5 poroso | Módulo de compressão (scaffold) | MPa | 275 | 50 | 500 |  | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |  | A verificar |
| β-TCP poroso | Módulo de compressão (scaffold) | MPa | 550 | 100 | 1000 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Porosidade | % | 70 | 60 | 70 |  | Sparks DS et al. Sci Adv 2023;9:eadd6071; Nam JH et al. J Periodontal Implant Sci 2023;53:218-232 | https://doi.org/10.1126/sciadv.add6071 | Verificado |
| Hidroxiapatite (HA) porosa | Porosidade | % | 65 | 55 | 80 |  | FDA 510(k) K023998 (Tabela 1: Pro Osteon 200); Hoogendoorn HA et al. Clin Orthop Relat Res 1984;187:281-288 | https://www.accessdata.fda.gov/cdrh_docs/pdf2/K023998.pdf | Verificado (fornecedor) |
| PCL | Porosidade | % | 61 | 48 | 77 |  | Zein I et al. Biomaterials 2002;23:1169-1185; Hutmacher DW et al. J Biomed Mater Res 2001;55:203-216 | https://doi.org/10.1016/s0142-9612(01)00232-0 | Verificado |
| PLGA 50:50 | Porosidade | % | 80 | 73 | 87 |  | Lu L et al. Biomaterials 2000;21:1837-1845 | https://doi.org/10.1016/s0142-9612(00)00047-8 | Verificado |
| PLLA | Porosidade | % | 75 | 60 | 90 |  | Lu L et al. Biomaterials 2000;21:1595-1605; Budyanto L, Goh YQ, Ooi CP. J Mater Sci Mater Med 2009;20:105-111; Ghosh S et al. J Mater Sci Mater Med 2007;18:185-193 | https://doi.org/10.1016/S0142-9612(00)00048-X | Verificado |
| Quitosano/HA (liofilizado) | Porosidade | % | 87,5 | 86,9 | 91,3 |  | Gaihre B, Jayasuriya AC. Mater Sci Eng C 2018;91:330-339; Wang H et al. Heliyon 2024;10:e25832 | https://doi.org/10.1016/j.msec.2018.05.060 | Verificado |
| Vidro bioativo 45S5 poroso | Porosidade | % | 80 | 70 | 90 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| β-TCP poroso | Porosidade | % | 65 | 65 | 92 |  | FDA 510(k) K120152 (Cerasorb Plus); FDA 510(k) K032409 (Vitoss); Furusawa T et al. Int J Implant Dent 2016;2:4 | https://fda.innolitics.com/device/K120152 | Verificado (fornecedor) |
| Compósito PCL/β-TCP (impressão 3D) | Resistência à compressão (scaffold) | MPa | 4,3 | 2,2 | 6,38 |  | Kawai T et al. J Orthop Res 2018;36:1002-1011; Wong WS et al. Cureus 2025;17:e86272 | https://doi.org/10.1002/jor.23673 | A verificar |
| Hidroxiapatite (HA) porosa | Resistência à compressão (scaffold) | MPa | 3,4 | 1,6 | 22,5 |  | Liang H et al. Int J Bioprint 2022;8(1):502; Zhang P, Zhou Q, He R. Materials 2024;17:6092 (Tabela 1) | https://doi.org/10.18063/ijb.v8i1.502 | Verificado |
| PCL | Resistência à compressão (scaffold) | MPa | 6 | 2 | 10 |  | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |  | A verificar |
| PLGA 50:50 | Resistência à compressão (scaffold) | MPa | 1,75 | 0,5 | 3 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PLLA | Resistência à compressão (scaffold) | MPa | 5 | 1 | 10 |  | Karanth D et al. Clin Exp Dent Res 2023;9:398-408 | https://doi.org/10.1002/cre2.712 | Verificado |
| Quitosano/HA (liofilizado) | Resistência à compressão (scaffold) | MPa | 0,05 | 0,03 | 0,06 |  | Gaihre B, Jayasuriya AC. Mater Sci Eng C 2018;91:330-339 | https://doi.org/10.1016/j.msec.2018.05.060 | Verificado |
| Vidro bioativo 45S5 poroso | Resistência à compressão (scaffold) | MPa | 0,915 | 0,58 | 1,1 |  | Baino F, Fiume E. Materials 2019;12:3244 (Tabela 1) | https://doi.org/10.3390/ma12193244 | Verificado |
| β-TCP poroso | Resistência à compressão (scaffold) | MPa | 2 | 0,35 | 7,72 |  | Montelongo SA et al. J Mater Sci Mater Med 2021;32:94; Xulin H et al. Int J Bioprint 2023;9(2):673; Hashimoto K, Oikawa H, Shibata H. Int J Mol Sci 2024;25:5363 | https://doi.org/10.1007/s10856-021-06569-9 | Verificado |
| Compósito PCL/β-TCP (impressão 3D) | Tempo de degradação | meses | 18 | 12 | 24 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Hidroxiapatite (HA) porosa | Tempo de degradação | meses | 60 | 42 | 60 |  | Hoogendoorn HA et al. Clin Orthop Relat Res 1984;187:281-288; Oonishi H et al. J Biomed Mater Res 2000;51:37-46 | https://doi.org/10.1097/00003086-198407000-00043 | Verificado |
| PCL | Tempo de degradação | meses | 30 | 24 | 36 |  | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |  | A verificar |
| PLGA 50:50 | Tempo de degradação | meses | 2 | 1 | 3 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PLLA | Tempo de degradação | meses | 42 | 24 | 60 |  | Bos RRM et al. Biomaterials 1991;12:32-36; Bergsma JE et al. Biomaterials 1995;16:25-31 | https://doi.org/10.1016/0142-9612(91)90128-w | Verificado |
| Quitosano/HA (liofilizado) | Tempo de degradação | meses | 7,5 | 3 | 12 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Vidro bioativo 45S5 poroso | Tempo de degradação | meses | 16 | 6 | 24 |  | Tadjoedin ES et al. Clin Oral Implants Res 2002;13:428-436; Tadjoedin ES et al. Clin Oral Implants Res 2000;11:334-344 | https://doi.org/10.1034/j.1600-0501.2002.130412.x | Verificado |
| β-TCP poroso | Tempo de degradação | meses | 12 | 6 | 18 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |

Linhas: 64; estados: A verificar 39; Verificado 22; Verificado (fornecedor) 3

## 4. Rankings (η = 1)

### Cenário A

Critérios: Resistência à compressão (scaffold); Módulo de compressão (scaffold); Porosidade; Tempo de degradação; Bioatividade (ordinal 1-5); Imprimibilidade 3D (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro)

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Compósito PCL/β-TCP (impressão 3D) | 0,628 (1) | 0,745 (1) | 0 (1) |
| β-TCP poroso | 0,577 (2) | 0,641 (3) | 0,479 (2) |
| Vidro bioativo 45S5 poroso | 0,537 (3) | 0,575 (4) | 0,697 (4) |
| PCL | 0,525 (4) | 0,648 (2) | 0,683 (3) |
| Hidroxiapatite (HA) porosa | 0,436 (5) | 0,464 (5) | 1 (5) |

ΔC 1.º-2.º (TOPSIS) = 0,051 (regra: < 0,01 = empate)

### Cenário B

Critérios: Resistência à compressão (scaffold); Módulo de compressão (scaffold); Porosidade; Tempo de degradação; Bioatividade (ordinal 1-5); Imprimibilidade 3D (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro)

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Compósito PCL/β-TCP (impressão 3D) | 0,676 (1) | 0,745 (1) | 0 (1) |
| β-TCP poroso | 0,59 (2) | 0,651 (3) | 0,404 (2) |
| PCL | 0,558 (3) | 0,667 (2) | 0,631 (4) |
| Vidro bioativo 45S5 poroso | 0,554 (4) | 0,596 (5) | 0,576 (3) |
| PLLA | 0,516 (5) | 0,625 (4) | 0,751 (5) |
| Hidroxiapatite (HA) porosa | 0,47 (6) | 0,466 (7) | 0,862 (6) |
| Quitosano/HA (liofilizado) | 0,453 (7) | 0,411 (8) | 0,981 (7) |
| PLGA 50:50 | 0,424 (8) | 0,498 (6) | 1 (8) |

ΔC 1.º-2.º (TOPSIS) = 0,085 (regra: < 0,01 = empate)

## 5. Robustez (results/resumo_robustez.md)

η = 1 no resultado principal; sensibilidades a partir do cenário A. Monte Carlo: 10000 iterações, seed 42. No MC propriedades, as propriedades quantitativas com mín. = máx. variam ±10 % à volta do típico (data/parametros.csv).

Vencedor no cenário A: TOPSIS Compósito PCL/β-TCP (impressão 3D); WASPAS Compósito PCL/β-TCP (impressão 3D); VIKOR Compósito PCL/β-TCP (impressão 3D)

#### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| B | B | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,81 |
| Q | sem ordinais | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,0 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,1 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,2 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,3 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,4 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,5 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,6 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,7 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,8 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,9 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| η | η = 1,0 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| T-scaffold | Resistência à compressão: 2 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 0,80 |
| T-scaffold | Resistência à compressão: 12 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| T-scaffold | Módulo de compressão: 50 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| T-scaffold | Módulo de compressão: 500 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| T-scaffold | Porosidade: 50 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| T-scaffold | Porosidade: 90 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,60 |
| T-scaffold | Tempo de degradação: x0,5 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| T-scaffold | Tempo de degradação: x2,0 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| C-custo | custo baixo (0,01) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| C-custo | custo elevado (0,25) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| P-foco | direta | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | 0,80 |
| P-foco | direta + indireta | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,90 |

#### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| β-TCP poroso | 52,2 % | 24,6 % | 38,6 % |
| Compósito PCL/β-TCP (impressão 3D) | 38,9 % | 67,5 % | 46,3 % |
| Vidro bioativo 45S5 poroso | 8,8 % | 5,5 % | 15,0 % |
| PCL | 0,1 % | 2,4 % | 0,0 % |
| Hidroxiapatite (HA) porosa | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Compósito PCL/β-TCP (impressão 3D) | 95,7 % | 100,0 % | 99,6 % |
| β-TCP poroso | 4,3 % | 0,0 % | 0,4 % |
| Hidroxiapatite (HA) porosa | 0,0 % | 0,0 % | 0,0 % |
| PCL | 0,0 % | 0,0 % | 0,0 % |
| Vidro bioativo 45S5 poroso | 0,0 % | 0,0 % | 0,0 % |

#### Onde o vencedor muda (face ao cenário A)

- T-scaffold, Resistência à compressão: 2, TOPSIS: Compósito PCL/β-TCP (impressão 3D) → β-TCP poroso
- T-scaffold, Resistência à compressão: 2, WASPAS: Compósito PCL/β-TCP (impressão 3D) → β-TCP poroso
- T-scaffold, Resistência à compressão: 2, VIKOR: Compósito PCL/β-TCP (impressão 3D) → β-TCP poroso
- P-foco, direta, TOPSIS: Compósito PCL/β-TCP (impressão 3D) → β-TCP poroso
- P-foco, direta, VIKOR: Compósito PCL/β-TCP (impressão 3D) → β-TCP poroso

## 6. Triagem (critérios estritos)

| Material | Critério | Regra | Valor | Resultado | Motivo |
|---|---|---|---|---|---|

## 7. Valores "A verificar" por influência (results/por_verificar.md)

Vencedor do TOPSIS: cenário A: Compósito PCL/β-TCP (impressão 3D); cenário B: Compósito PCL/β-TCP (impressão 3D).
Células a verificar: 39 (0 mudam o vencedor com ±20 %).

| # | Cenário | Material | Critério | Tipo | Típico | ΔC material | ΔC máx. | Muda vencedor | Fonte atual |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A | Hidroxiapatite (HA) porosa | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 5,0000 | 0,042 | 0,042 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 2 | A | Vidro bioativo 45S5 poroso | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 5,0000 | 0,025 | 0,029 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 3 | B | Quitosano/HA (liofilizado) | Bioatividade (ordinal 1-5) | ordinal | 3,0000 | 0,022 | 0,022 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 4 | A | Compósito PCL/β-TCP (impressão 3D) | Resistência à compressão (scaffold) | quantitativo | 4,3000 | 0,020 | 0,020 | não | Kawai T et al. J Orthop Res 2018;36:1002-1011; Wong WS et al. Cureus 2025;17:e86272 |
| 5 | A | Compósito PCL/β-TCP (impressão 3D) | Imprimibilidade 3D (ordinal 1-5) | ordinal | 5,0000 | 0,019 | 0,019 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 6 | A | PCL | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,019 | 0,029 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 7 | A | PCL | Imprimibilidade 3D (ordinal 1-5) | ordinal | 5,0000 | 0,018 | 0,018 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 8 | A | PCL | Resistência à compressão (scaffold) | quantitativo | 6,0000 | 0,018 | 0,024 | não | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |
| 9 | B | PLLA | Imprimibilidade 3D (ordinal 1-5) | ordinal | 4,0000 | 0,017 | 0,017 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 10 | A | Vidro bioativo 45S5 poroso | Porosidade | quantitativo | 80,0000 | 0,017 | 0,045 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 11 | A | β-TCP poroso | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 3,0000 | 0,015 | 0,015 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 12 | A | PCL | Tempo de degradação | quantitativo | 30,0000 | 0,014 | 0,014 | não | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |
| 13 | B | PLLA | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,013 | 0,013 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 14 | B | PLGA 50:50 | Imprimibilidade 3D (ordinal 1-5) | ordinal | 3,0000 | 0,013 | 0,013 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 15 | A | Hidroxiapatite (HA) porosa | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 3,0000 | 0,013 | 0,013 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 16 | B | Quitosano/HA (liofilizado) | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,012 | 0,012 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 17 | A | β-TCP poroso | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,012 | 0,012 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 18 | B | PLGA 50:50 | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 2,0000 | 0,010 | 0,010 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 19 | A | Compósito PCL/β-TCP (impressão 3D) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 2,0000 | 0,010 | 0,010 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 20 | B | Quitosano/HA (liofilizado) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 2,0000 | 0,009 | 0,009 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 21 | A | Compósito PCL/β-TCP (impressão 3D) | Tempo de degradação | quantitativo | 18,0000 | 0,009 | 0,009 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 22 | B | PLLA | Bioatividade (ordinal 1-5) | ordinal | 1,0000 | 0,008 | 0,008 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 23 | A | Vidro bioativo 45S5 poroso | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,008 | 0,011 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 24 | A | Hidroxiapatite (HA) porosa | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,007 | 0,011 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 25 | B | PLGA 50:50 | Resistência à compressão (scaffold) | quantitativo | 1,7500 | 0,006 | 0,006 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 26 | B | PLGA 50:50 | Bioatividade (ordinal 1-5) | ordinal | 1,0000 | 0,006 | 0,008 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 27 | A | β-TCP poroso | Tempo de degradação | quantitativo | 12,0000 | 0,005 | 0,005 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 28 | B | PLLA | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 1,0000 | 0,004 | 0,004 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 29 | B | Quitosano/HA (liofilizado) | Tempo de degradação | quantitativo | 7,5000 | 0,004 | 0,004 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 30 | A | β-TCP poroso | Módulo de compressão (scaffold) | quantitativo | 550,0000 | 0,003 | 0,003 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 31 | B | PLGA 50:50 | Tempo de degradação | quantitativo | 2,0000 | 0,002 | 0,002 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 32 | A | Hidroxiapatite (HA) porosa | Módulo de compressão (scaffold) | quantitativo | 1750,0000 | 0,002 | 0,003 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 33 | A | Vidro bioativo 45S5 poroso | Módulo de compressão (scaffold) | quantitativo | 275,0000 | 0,001 | 0,001 | não | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |
| 34 | B | PLGA 50:50 | Módulo de compressão (scaffold) | quantitativo | 35,0000 | 0,000 | 0,000 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 35 | A | PCL | Módulo de compressão (scaffold) | quantitativo | 50,0000 | 0,000 | 0,000 | não | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |
| 36 | A | Vidro bioativo 45S5 poroso | Bioatividade (ordinal 1-5) | ordinal | 5,0000 | 0,000 | 0,040 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 37 | A | Vidro bioativo 45S5 poroso | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 4,0000 | 0,000 | 0,019 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 38 | A | PCL | Bioatividade (ordinal 1-5) | ordinal | 1,0000 | 0,000 | 0,005 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 39 | A | PCL | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 1,0000 | 0,000 | 0,003 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |

## 8. Notas (linhas literais de docs/NOTAS_METODOLOGICAS.md e data/leia_me.md)

- MCDM quantitativo: haste femoral, stent coronário expansível por balão, scaffold ósseo.
- Alvos do scaffold = cenário de referência para osso trabecular, não ótimo universal (cenário T-scaffold).
- Regra da porosidade (scaffold, 1 out 2026): as propriedades mecânicas de um scaffold usam-se à porosidade típica desse material (±10 pontos percentuais); valores medidos a porosidades muito diferentes ficam de fora ou só alargam o intervalo, com nota. Exemplo: na HA porosa (típico 65 %) entram os valores de resistência a 60 % e a ~70 %, e ficam de fora os de 40 % e de 80 %.
- Regra do típico (scaffold, 1 out 2026): típico = mediana das fontes dentro da janela de porosidade (porosidade típica do material ±10 pontos percentuais); o intervalo vai do mínimo ao máximo dessas fontes. Com uma só fonte na janela, o típico é o valor dessa fonte e a nota diz "uma só fonte".
- HA não reabsorvível (scaffold, 1 out 2026): o tempo de degradação da HA segue a lógica da opção O2 do stent: mínimo 42 meses (sem reabsorção em 3,5 anos) e máximo e típico iguais ao pior valor observado nos outros materiais do scaffold (60 meses, PLLA). É um valor de modelação e subestima a permanência real da HA.
- PLLA do scaffold = scaffold impresso ou extrudido; as espumas têm módulo 1 a 2 ordens de grandeza abaixo.
- Bioatividade (scaffold, 1 out 2026): a rubrica segue a classificação de Hench (classe A, osteoprodutivo, nota 5; classe B, osteocondutor, nota 4); a HA e o β-TCP ficam com 4 e o vidro 45S5 com 5.
- T-scaffold: alvos no mínimo e no máximo do osso trabecular (tecido.csv) para compressão (2-12 MPa), módulo (50-500 MPa) e porosidade (50-90 %); tempo de degradação sem referência no tecido: fatores de sensibilidade x0,5 e x2 sobre o alvo (não são valores da literatura).
- P-foco (3 out 2026): problema crítico de cada dispositivo indicado pelo professor (2 out 2026). O peso dos critérios ligados ao problema (data/problemas_criticos.csv) é multiplicado por fator_foco_problema = 2 (valor de desenho) e os pesos são renormalizados. Resultado principal: só critérios de ligação direta; sensibilidade: direta + indireta. Scaffold: leitura literal do professor no resultado principal (porosidade, bioatividade, tempo de degradação); a resistência, o módulo e a imprimibilidade entram só na sensibilidade (decisão do André, 3 out). Par articular: sensibilidade semiquantitativa à parte (results/semiquantitativos.csv). Mapa e resultados em relatorio/apoio/problemas_criterios.md.
- Reversão de ranking observada (scaffold, 28 set 2026): ao retirar PLLA, PLGA e quitosano/HA (cenário A com os estatutos novos), o β-TCP e o PCL/β-TCP trocam de posição (TOPSIS e VIKOR: PCL/β-TCP 1.º com 8 materiais, β-TCP 1.º com 5), porque as normalizações dependem do mínimo e do máximo de cada coluna. Exemplo concreto para o item "Testes formais de reversão de ranking" do backlog e para a secção de limitações.
- Scaffold: a fragilidade do ranking reflete em parte a incerteza dos dados (propriedades muito dependentes da porosidade, intervalos largos na base) e não só o método. Na discussão, separar as duas causas, por exemplo comparando a % de 1.º lugar do MC propriedades (incerteza dos dados) com a do W pesos (incerteza das preferências). Cenário A com os estatutos novos (5 materiais): β-TCP 53,6 % / 31,6 % / 37,4 % (T/W/V) no MC propriedades, mas 91,7 % / 100 % / 85,3 % no W pesos; ou seja, o 1.º lugar é estável face aos pesos e frágil face aos dados.
  scaffold) o vencedor do Monte Carlo não muda; no stent, o 1.º lugar do Co-Cr L605 desce
  mín. e o máx. Um típico fora de [mín., máx.] dá erro. Haste, scaffold e reprodução de Petković
  Everolimus-Eluting Bioresorbable Coronary Scaffolds: The ABSORB III Trial. J Am Coll Cardiol 2017;70:2852-2862,
  Three-year outcomes of bioresorbable vascular scaffolds versus second-generation drug-eluting stents. Medicine
  bioresorbable scaffold. J Thorac Dis 2017;9(Suppl 9):S903-S913, doi:10.21037/jtd.2017.06.34 (revisão, texto
- Não encontrada: a referência "Chua 2025" do rascunho do chat (sem registo na Crossref com esse autor e tema); substituída a 3 out 2026 por Lodewijks et al. Cureus 2024;16(8):e66256, doi:10.7759/cureus.66256 (defeitos tibiais muito grandes tratados com PCL/TCP impresso; confirmado na Crossref), na discussão (8.5) e no caso do scaffold.
- Heliyon 2025, "Editor Note" sobre Wang Y et al. Heliyon 2024;10:e26071 (doi:10.1016/j.heliyon.2025.e44205), usado no módulo do PCL/β-TCP: conteúdo não lido (página com acesso bloqueado); verificar se é correção ou manifestação de preocupação.
- [ ] Estatuto clínico dos 8 materiais do scaffold (Clínico (substituto ósseo) / Clínico (uso limitado) / Investigação), proposto a 28 set 2026; fonte a verificar indicada na coluna notas de data/materiais.csv (Rezwan et al. 2006, Bose et al. 2012, Hench 1991, Woodruff & Hutmacher 2010, Athanasiou et al. 1996, base 510(k) da FDA; PCL/β-TCP e quitosano/HA sem fonte).

leia_me.md:

Densidade deixa de ser proxy de radiopacidade (nova escala de radiopacidade) · σy/E renomeado "proxy material" · Nitinol fora do ranking · K_IC retirado do par articular · "Resistência" retirada da matriz dentária (tração ≠ flexão) · alvos do scaffold passam a cenários · nova folha Cenarios
Par articular e implante dentário ficam SEMIQUANTITATIVOS (ordinais > 50 % do peso): MCDM quantitativo só para haste, stent (balão) e scaffold.
## Alterações v0.6 (1 out 2026): 1.ª ronda do scaffold
- Regra da porosidade para as propriedades mecânicas dos scaffolds (ver "Cuidados").
- 11 linhas do scaffold com fonte primária: porosidade do quitosano/HA, do PLLA e do β-TCP; resistência à compressão da HA; e sete notas ordinais (imprimibilidade, esterilização e bioatividade).
## Alterações v0.7 (1 out 2026): 2.ª ronda do scaffold
- Regra do típico: típico = mediana das fontes dentro da janela de porosidade (porosidade típica do material ±10 pontos percentuais); o intervalo vai do mínimo ao máximo dessas fontes.
- β-TCP: resistência 0,35-7,72 MPa, típico 2. PCL/β-TCP: porosidade típica 70 % (especificação dos scaffolds por FDM).
- PLLA definido como scaffold impresso; degradação 24-60 meses, com dados de PLLA maciço.
- Bioatividade (classificação de Hench): 5 = classe A, osteoprodutivo (ex.: vidro 45S5); 4 = classe B, osteocondutor com ligação química ao osso (HA, β-TCP); 3 = osteocondutor sem ligação química, ou compósito com fase bioativa minoritária; 2 = pouca interação; 1 = bioinerte ou sem osteocondução. Fonte: Hench LL. Bioactive ceramics: theory and clinical applications. Bioceramics 1994;7:3-14 (original não lido); classes A e B lidas em Bramhill J, Ross S, Ross G. Int J Environ Res Public Health 2017;14:66, doi:10.3390/ijerph14010066 (revisão, texto completo).
1. Propriedades de scaffolds dependem da porosidade. Regra da porosidade: as propriedades mecânicas de um scaffold usam-se à porosidade típica desse material (±10 pontos percentuais); valores medidos a porosidades muito diferentes ficam de fora ou só alargam o intervalo, com nota. Dentro da janela, típico = mediana das fontes dentro da janela de porosidade (porosidade típica do material ±10 pontos percentuais); o intervalo vai do mínimo ao máximo dessas fontes. Regista sempre a porosidade e o método de fabrico do estudo.

## 9. Apoio já existente

Linhas que referem o caso noutros ficheiros:

- relatorio/00_resumo_executivo.md: linhas 14, 18, 24, 25
- docs/TP2_fisiopatologia_da_falha.md: linhas 146, 173, 177, 185, 189, 195, 197, 208, 223, 252, 280, 283, 287
- docs/TP2_guia_de_fontes.md: linhas 24, 140, 141, 142, 144, 145, 146, 149, 178, 179, 182, 184, 185, 186, 187, 231
- docs/backlog_artigo.md: linhas 14, 24
