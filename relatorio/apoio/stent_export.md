# Stent vascular: export de dados (commit 7f6f8ac, 30 set 2026)

Gerado a partir de data/ (materiais.csv, criterios.csv, cenarios.csv), src/ e results/. Só dados.

## 1. Candidatos

| Material | Norma | Classe | Estatuto | Triagem | A | B | B-bio |
|---|---|---|---|---|---|---|---|
| Aço inox 316L | ASTM F138 | Metal | Clínico (1.ª geração) | aprovado | sim | sim |  |
| Co-Cr L605 | ASTM F90 | Metal | Clínico | aprovado | sim | sim |  |
| Co-Ni-Cr-Mo MP35N | ASTM F562 | Metal | Clínico | aprovado | sim | sim |  |
| Pt-Cr | - | Metal | Clínico | aprovado | sim | sim |  |
| Nitinol (autoexpansível) | ASTM F2063 | Metal (superelástico) | Excluído (autoexpansível: só discussão) | eliminado |  |  |  |
| Liga de Mg WE43 (bioabsorvível) | - | Metal biodegradável | Clínico (Magmaris) | aprovado |  | sim | sim |
| PLLA (bioabsorvível) | - | Polímero biodegradável | Descontinuado (Absorb, 2017) | aprovado |  | sim | sim |

Cenários (cenarios.csv) aplicáveis ao stent:

- A: Só materiais em uso clínico (stent: só permanentes, 316L, L605, MP35N, Pt-Cr)
- B: Inclui investigação e bioabsorvíveis (stent: A + Mg WE43 e PLLA; permanentes com o pior valor observado no tempo de reabsorção, opção O2)
- B-bio: Só bioabsorvíveis (Mg WE43 e PLLA) com o tempo de reabsorção; comparação, não ranking (opção O3)
- R-sentinela: Sensibilidade do tempo de reabsorção atribuído aos permanentes: 60, 120, 600 e 1200 meses (opção O1)
- Q: Só critérios quantitativos (sem ordinais)
- W: Sensibilidade dos pesos
- η: Sensibilidade ao nível de confiança η de 0 a 1, passo 0,1 (resultado principal: η = 1)
- M: Concordância entre métodos
- C-custo: Peso do custo relativo baixo (0,01) vs elevado (0,25), restantes pesos redistribuídos
- MC: Incerteza das propriedades

## 2. Critérios (criterios.csv)

| Critério | Tipo | Alvo | Unidade | Peso | Justificação |
|---|---|---|---|---|---|
| Tipo de expansão | Estrito | Expansível por balão | - |  | Exclui Nitinol (autoexpansível) do ranking |
| Índice material de recuo elástico σy/E (proxy) | Custo |  | - | 0,1 | Proxy ao nível do material, não do dispositivo; menor = menos recuo |
| Espessura típica de strut | Custo |  | µm | 0,2 | Struts finos → menos reestenose/trombose |
| Alongamento na rotura | Benefício |  | % | 0,1 | Expansão sem fratura |
| Resistência à tração | Benefício |  | MPa | 0,1 | Resistência radial e fadiga pulsátil |
| Módulo de Young | Benefício |  | GPa | 0,05 | Rigidez radial com struts finos |
| Radiopacidade (ordinal 1-5) | Benefício |  | - | 0,1 | Visibilidade em fluoroscopia (substitui a densidade) |
| Compatibilidade com RM (ordinal 1-5) | Benefício |  | - | 0,05 | Seguimento por RM/angio-RM |
| Compatibilidade com esterilização (ordinal 1-5) | Benefício |  | - | 0,05 | Fármaco e polímero limitam o método |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | Custo |  | - | 0,05 |  |
| Fabricabilidade (ordinal 1-5) | Benefício |  | - | 0,05 | Corte laser, memória de forma |
| Tempo de reabsorção (só cenário B) | Alvo | 12 | meses | 0,15 | Suporte ~3-6 meses; reabsorção completa desejável em ~1 ano |

Pesos usados no cenário A (renormalizados): Índice material de recuo elástico σy/E (proxy) 0,118; Espessura típica de strut 0,235; Alongamento na rotura 0,118; Resistência à tração 0,118; Módulo de Young 0,059; Radiopacidade (ordinal 1-5) 0,118; Compatibilidade com RM (ordinal 1-5) 0,059; Compatibilidade com esterilização (ordinal 1-5) 0,059; Custo relativo de material e fabrico (1-5, 5 = mais caro) 0,059; Fabricabilidade (ordinal 1-5) 0,059

Pesos usados no cenário B (renormalizados): Índice material de recuo elástico σy/E (proxy) 0,1; Espessura típica de strut 0,2; Alongamento na rotura 0,1; Resistência à tração 0,1; Módulo de Young 0,05; Radiopacidade (ordinal 1-5) 0,1; Compatibilidade com RM (ordinal 1-5) 0,05; Compatibilidade com esterilização (ordinal 1-5) 0,05; Custo relativo de material e fabrico (1-5, 5 = mais caro) 0,05; Fabricabilidade (ordinal 1-5) 0,05; Tempo de reabsorção 0,15

## 3. Valores (todas as linhas do stent em materiais.csv e o índice derivado σy/E)

| Material | Propriedade | Unidade | Típico | Mín. | Máx. | Texto | Fonte | doi_url | Estado |
|---|---|---|---|---|---|---|---|---|---|
| Aço inox 316L | Alongamento na rotura | % | 50 | 40 | 60 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Alongamento na rotura | % | 52,5 | 50 | 55 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Alongamento na rotura | % | 45 | 45 | 45 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Alongamento na rotura | % | 13,5 | 10 | 17 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Alongamento na rotura | % | 12,5 | 10 | 15 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Alongamento na rotura | % | 4 | 2 | 6 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Alongamento na rotura | % | 45 | 45 | 45 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Compatibilidade com RM (ordinal 1-5) | - | 2 | 2 | 2 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Co-Cr L605 | Compatibilidade com RM (ordinal 1-5) | - | 3 | 3 | 3 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Compatibilidade com RM (ordinal 1-5) | - | 3 | 3 | 3 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Compatibilidade com RM (ordinal 1-5) | - | 5 | 5 | 5 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Nitinol (autoexpansível) | Compatibilidade com RM (ordinal 1-5) | - | 4 | 4 | 4 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| PLLA (bioabsorvível) | Compatibilidade com RM (ordinal 1-5) | - | 5 | 5 | 5 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Pt-Cr | Compatibilidade com RM (ordinal 1-5) | - | 3 | 3 | 3 |  | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Aço inox 316L | Compatibilidade com esterilização (ordinal 1-5) | - | 4 | 4 | 4 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Co-Cr L605 | Compatibilidade com esterilização (ordinal 1-5) | - | 4 | 4 | 4 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Compatibilidade com esterilização (ordinal 1-5) | - | 4 | 4 | 4 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Compatibilidade com esterilização (ordinal 1-5) | - | 4 | 4 | 4 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Nitinol (autoexpansível) | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| PLLA (bioabsorvível) | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Pt-Cr | Compatibilidade com esterilização (ordinal 1-5) | - | 4 | 4 | 4 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Aço inox 316L | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 1 | 1 | 1 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Co-Cr L605 | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 3 | 3 | 3 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 3 | 3 | 3 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 5 | 5 | 5 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Nitinol (autoexpansível) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 4 | 4 | 4 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| PLLA (bioabsorvível) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 5 | 5 | 5 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Pt-Cr | Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 4 | 4 | 4 |  | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Aço inox 316L | Densidade | g/cm³ | 8 | 8 | 8 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Densidade | g/cm³ | 9,1 | 9,1 | 9,1 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Densidade | g/cm³ | 8,4 | 8,4 | 8,4 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Densidade | g/cm³ | 1,84 | 1,84 | 1,84 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Densidade | g/cm³ | 6,45 | 6,45 | 6,45 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Densidade | g/cm³ | 1,27 | 1,25 | 1,29 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Densidade | g/cm³ | 9,9 | 9,9 | 9,9 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Espessura típica de strut | µm | 120 | 100 | 140 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Espessura típica de strut | µm | 75 | 60 | 90 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Espessura típica de strut | µm | 75 | 60 | 90 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Espessura típica de strut | µm | 135 | 120 | 150 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Espessura típica de strut | µm | 125 | 100 | 150 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Espessura típica de strut | µm | 155 | 150 | 160 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Espessura típica de strut | µm | 77,5 | 74 | 81 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Fabricabilidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Co-Cr L605 | Fabricabilidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Fabricabilidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Fabricabilidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Nitinol (autoexpansível) | Fabricabilidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| PLLA (bioabsorvível) | Fabricabilidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Pt-Cr | Fabricabilidade (ordinal 1-5) | - | 4 | 4 | 4 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Aço inox 316L | Módulo de Young | GPa | 193 | 193 | 193 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Módulo de Young | GPa | 243 | 243 | 243 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Módulo de Young | GPa | 233 | 233 | 233 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Módulo de Young | GPa | 44,5 | 44 | 45 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Módulo de Young | GPa | 57,5 | 40 | 75 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Módulo de Young | GPa | 3,35 | 3,1 | 3,6 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Módulo de Young | GPa | 203 | 203 | 203 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Radiopacidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| Co-Cr L605 | Radiopacidade (ordinal 1-5) | - | 4 | 4 | 4 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Radiopacidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Radiopacidade (ordinal 1-5) | - | 1 | 1 | 1 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| Nitinol (autoexpansível) | Radiopacidade (ordinal 1-5) | - | 2 | 2 | 2 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| PLLA (bioabsorvível) | Radiopacidade (ordinal 1-5) | - | 1 | 1 | 1 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| Pt-Cr | Radiopacidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Radiopacidade depende sobretudo do número atómico efetivo e da espessura: confirmar com literatura de stents |  | A verificar |
| Aço inox 316L | Resistência à tração | MPa | 592,5 | 515 | 670 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Resistência à tração | MPa | 1025 | 1000 | 1050 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Resistência à tração | MPa | 945 | 930 | 960 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Resistência à tração | MPa | 250 | 220 | 280 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Resistência à tração | MPa | 1185 | 1070 | 1300 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Resistência à tração | MPa | 65 | 60 | 70 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Resistência à tração | MPa | 834 | 834 | 834 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Tempo de reabsorção | meses | 10,5 | 9 | 12 |  | Haude M et al. Lancet 2016;387:31-39 (BIOSOLVE-II, Magmaris) |  | A verificar |
| Nitinol (autoexpansível) | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Tempo de reabsorção | meses | 42 | 36 | 48 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Tensão de cedência | MPa | 272,5 | 205 | 340 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Tensão de cedência | MPa | 480 | 460 | 500 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Tensão de cedência | MPa | 412,5 | 410 | 415 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Tensão de cedência | MPa | 172,5 | 150 | 195 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Tensão de cedência | MPa | 475 | 350 | 600 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Tensão de cedência | MPa | 60 | 50 | 70 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Tensão de cedência | MPa | 480 | 480 | 480 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Teor de níquel | % (massa) | 14 | 13 | 15 |  | Página de fornecedor (Upmet), 316L ASTM F138 | https://www.upmet.com/products/stainless-steel/316lslvm | Verificado (fornecedor) |
| Co-Cr L605 | Teor de níquel | % (massa) | 10 | 9 | 11 |  | Página de fornecedor (MGM Industries), L605 ASTM F90 | https://www.mgm-industries.com/l605-alloy | Verificado (fornecedor) |
| Co-Ni-Cr-Mo MP35N | Teor de níquel | % (massa) | 35 | 33 | 37 |  | Página de fornecedor (stainless.eu), MP35N ASTM F562 | https://www.stainless.eu/en/products/cobalt-alloys/mp35n/ | Verificado (fornecedor) |
| Liga de Mg WE43 (bioabsorvível) | Teor de níquel | % (massa) | 0,005 | 0 | 0,005 |  | MakeItFrom, WE43B (cita ASTM B80) | https://www.makeitfrom.com/material-properties/WE43B-WE43B-T6-M18432-Magnesium | A verificar |
| PLLA (bioabsorvível) | Teor de níquel | % (massa) | 0 | 0 | 0 |  | Composição química do PLLA |  | Verificado (composição química) |
| Pt-Cr | Teor de níquel | % (massa) | 9 | 9 | 9 |  | A novel platinum chromium everolimus-eluting stent for the treatment of coronary artery disease. Biologics: Targets and Therapy 2013;7:149 [confirmar autores e ano] | https://doi.org/10.2147/BTT.S34939 | Verificado |
| Aço inox 316L | Tipo de expansão | - |  |  |  | balão |  |  | A verificar |
| Co-Cr L605 | Tipo de expansão | - |  |  |  | balão |  |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Tipo de expansão | - |  |  |  | balão |  |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Tipo de expansão | - |  |  |  | balão |  |  | A verificar |
| Nitinol (autoexpansível) | Tipo de expansão | - |  |  |  | autoexpansível |  |  | A verificar |
| PLLA (bioabsorvível) | Tipo de expansão | - |  |  |  | balão |  |  | A verificar |
| Pt-Cr | Tipo de expansão | - |  |  |  | balão |  |  | A verificar |
| Aço inox 316L | Índice material de recuo elástico σy/E (proxy) | - | 0,0014 | 0,0011 | 0,0018 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Co-Cr L605 | Índice material de recuo elástico σy/E (proxy) | - | 0,002 | 0,0019 | 0,0021 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Co-Ni-Cr-Mo MP35N | Índice material de recuo elástico σy/E (proxy) | - | 0,0018 | 0,0018 | 0,0018 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Liga de Mg WE43 (bioabsorvível) | Índice material de recuo elástico σy/E (proxy) | - | 0,0039 | 0,0033 | 0,0044 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Nitinol (autoexpansível) | Índice material de recuo elástico σy/E (proxy) | - | 0,0098 | 0,0047 | 0,015 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| PLLA (bioabsorvível) | Índice material de recuo elástico σy/E (proxy) | - | 0,0182 | 0,0139 | 0,0226 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Pt-Cr | Índice material de recuo elástico σy/E (proxy) | - | 0,0024 | 0,0024 | 0,0024 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |

Linhas: 104; estados: A verificar 92; A verificar (derivado) 7; Verificado (fornecedor) 3; Verificado 1; Verificado (composição química) 1

## 4. Rankings (η = 1)

### Cenário A

Critérios: Índice material de recuo elástico σy/E (proxy); Espessura típica de strut; Alongamento na rotura; Resistência à tração; Módulo de Young; Radiopacidade (ordinal 1-5); Compatibilidade com RM (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro); Fabricabilidade (ordinal 1-5)

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Co-Cr L605 | 0,761 (1) | 0,891 (1) | 0 (1) |
| Co-Ni-Cr-Mo MP35N | 0,613 (2) | 0,848 (2) | 0,325 (2) |
| Pt-Cr | 0,572 (3) | 0,823 (3) | 0,443 (3) |
| Aço inox 316L | 0,352 (4) | 0,767 (4) | 1 (4) |

### Cenário B

Critérios: Índice material de recuo elástico σy/E (proxy); Espessura típica de strut; Alongamento na rotura; Resistência à tração; Módulo de Young; Radiopacidade (ordinal 1-5); Compatibilidade com RM (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro); Fabricabilidade (ordinal 1-5); Tempo de reabsorção

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Co-Cr L605 | 0,664 (1) | 0,646 (1) | 0 (1) |
| Pt-Cr | 0,644 (2) | 0,601 (3) | 0,062 (3) |
| Co-Ni-Cr-Mo MP35N | 0,642 (3) | 0,617 (2) | 0,047 (2) |
| Aço inox 316L | 0,507 (4) | 0,564 (4) | 0,162 (4) |
| Liga de Mg WE43 (bioabsorvível) | 0,448 (5) | 0,468 (5) | 0,459 (5) |
| PLLA (bioabsorvível) | 0,147 (6) | 0,242 (6) | 1 (6) |

### Cenário B-bio (comparação, não ranking: 2 materiais)

Critérios: Índice material de recuo elástico σy/E (proxy); Espessura típica de strut; Alongamento na rotura; Resistência à tração; Módulo de Young; Radiopacidade (ordinal 1-5); Compatibilidade com RM (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro); Fabricabilidade (ordinal 1-5); Tempo de reabsorção

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Liga de Mg WE43 (bioabsorvível) | 1 (1) | 0,993 (1) | 0 (1) |
| PLLA (bioabsorvível) | 0 (2) | 0,452 (2) | 1 (2) |

## 5. Robustez (results/resumo_robustez.md)

η = 1 no resultado principal; sensibilidades a partir do cenário A. Monte Carlo: 10000 iterações, seed 42. No MC propriedades, as propriedades quantitativas com mín. = máx. variam ±10 % à volta do típico (data/parametros.csv).

Vencedor no cenário A: TOPSIS Co-Cr L605; WASPAS Co-Cr L605; VIKOR Co-Cr L605

#### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| B | B | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,94 |
| B-bio (comparação) | B-bio | Liga de Mg WE43 (bioabsorvível) | Liga de Mg WE43 (bioabsorvível) | Liga de Mg WE43 (bioabsorvível) | n/a |
| R-sentinela | 60 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,94 |
| R-sentinela | 120 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,94 |
| R-sentinela | 600 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,94 |
| R-sentinela | 1200 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,89 |
| Q | sem ordinais | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,0 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| η | η = 0,1 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| η | η = 0,2 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| η | η = 0,3 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,40 |
| η | η = 0,4 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,40 |
| η | η = 0,5 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,80 |
| η | η = 0,6 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,80 |
| η | η = 0,7 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,8 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,9 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 1,0 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| C-custo | custo baixo (0,01) | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| C-custo | custo elevado (0,25) | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |

#### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Co-Cr L605 | 94,8 % | 87,6 % | 94,6 % |
| Co-Ni-Cr-Mo MP35N | 5,1 % | 12,3 % | 5,3 % |
| Pt-Cr | 0,1 % | 0,0 % | 0,1 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Co-Cr L605 | 100,0 % | 100,0 % | 100,0 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |
| Co-Ni-Cr-Mo MP35N | 0,0 % | 0,0 % | 0,0 % |
| Pt-Cr | 0,0 % | 0,0 % | 0,0 % |

#### Onde o vencedor muda (face ao cenário A)

- η, η = 0,0, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,1, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,2, WASPAS: Co-Cr L605 → Aço inox 316L
- C-custo, custo elevado (0,25), WASPAS: Co-Cr L605 → Aço inox 316L

## 6. Triagem (critérios estritos)

| Material | Critério | Regra | Valor | Resultado | Motivo |
|---|---|---|---|---|---|
| Nitinol (autoexpansível) | Estatuto na base | não 'Excluído' |  | eliminado | Excluído (autoexpansível: só discussão) |
| Aço inox 316L | Tipo de expansão | Expansível por balão | balão | aprovado | valor 'balão' está no alvo 'Expansível por balão' |
| Co-Cr L605 | Tipo de expansão | Expansível por balão | balão | aprovado | valor 'balão' está no alvo 'Expansível por balão' |
| Co-Ni-Cr-Mo MP35N | Tipo de expansão | Expansível por balão | balão | aprovado | valor 'balão' está no alvo 'Expansível por balão' |
| Pt-Cr | Tipo de expansão | Expansível por balão | balão | aprovado | valor 'balão' está no alvo 'Expansível por balão' |
| Nitinol (autoexpansível) | Tipo de expansão | Expansível por balão | autoexpansível | eliminado | valor 'autoexpansível' não está no alvo 'Expansível por balão' |
| Liga de Mg WE43 (bioabsorvível) | Tipo de expansão | Expansível por balão | balão | aprovado | valor 'balão' está no alvo 'Expansível por balão' |
| PLLA (bioabsorvível) | Tipo de expansão | Expansível por balão | balão | aprovado | valor 'balão' está no alvo 'Expansível por balão' |

## 7. Notas metodológicas do stent (excertos literais de docs/NOTAS_METODOLOGICAS.md)

- Cenários (data/cenarios.csv): A = só materiais em uso clínico; B = inclui investigação e bioabsorvíveis. No stent, A = só permanentes (316L, L605, MP35N, Pt-Cr); B = A + Mg WE43 e PLLA.
- Tempo de reabsorção do stent (critério só do cenário B; alvo 12 meses):
  - B (opção O2): os permanentes recebem o pior valor observado (48 meses, máximo do PLLA). Interpretação: "não reabsorver é pelo menos tão mau como o pior bioabsorvível". Limitação: subestima o caso permanente (um permanente nunca reabsorve). Coerente nos três métodos, que usam os valores em bruto.
  - B-bio (opção O3): só Mg WE43 e PLLA, com o critério; apresentar como comparação, não como ranking (2 materiais).
  - R-sentinela (opção O1): sensibilidade a 60, 120, 600 e 1200 meses para os permanentes. TOPSIS e VIKOR não dependem do valor acima de 48 meses; o WASPAS depende (a eq. 13 leva r para 0 e o produto arrasta os permanentes): com 1200 meses o 316L cai para 5.º.
- η: resultado principal com η = 1 (só pesos subjetivos, justificados pelos mecanismos de falha). Os pesos objetivos (desvio-padrão) dependem da dispersão do conjunto de candidatos e mudam com o cenário (A vs B), por isso o η entra só como análise de sensibilidade (0 a 1, passo 0,1). O η = 0,5 vinha do valor inicial sugerido no artigo (secção 2.4).
- σy/E (src/biomat_mcdm/indices.py, calculado a partir de σy e E da base; intervalo = σy mín./E máx. a σy máx./E mín.): proxy ao nível do material da deformação elástica na cedência. Em stents expansíveis por balão, maior σy/E → maior recuo elástico → critério de CUSTO. Não é o recuo do dispositivo (depende da geometria do padrão, struts, processamento).
- [ ] Tipo de expansão dos stents (data/materiais.csv, 7 linhas "A verificar", sem referência).

Excertos de data/leia_me.md:

Densidade deixa de ser proxy de radiopacidade (nova escala de radiopacidade) · σy/E renomeado "proxy material" · Nitinol fora do ranking · K_IC retirado do par articular · "Resistência" retirada da matriz dentária (tração ≠ flexão) · alvos do scaffold passam a cenários · nova folha Cenarios
Par articular e implante dentário ficam SEMIQUANTITATIVOS (ordinais > 50 % do peso): MCDM quantitativo só para haste, stent (balão) e scaffold.
- Nova propriedade "Tipo de expansão" do stent (balão ou autoexpansível), usada na triagem.
- Índices derivados calculados em src/biomat_mcdm/indices.py (σy/E do stent; E_implante/E_osso da haste).
  - "Verificado (composição química)": valor que resulta da composição química do material (ex.: 0 % de níquel num polímero sem metais).
- Teor de níquel (stent): % em massa; no WE43 é um limite máximo de impureza e tipico = máximo (pior caso).
3. Stents: o Nitinol é autoexpansível (outra classe): eliminado na triagem pela regra "Tipo de expansão"; só na discussão.
4. Cenários (cenarios.csv): A = só materiais clínicos; B = inclui investigação e bioabsorvíveis. No stent, A = só permanentes em uso clínico (316L, L605, MP35N, Pt-Cr); B = A + Mg WE43 e PLLA.

Níquel: ainda sem nota em NOTAS_METODOLOGICAS.md (prevista na tarefa 10: todas as ligas permanentes candidatas contêm níquel; relevância clínica debatida [fonte a indicar]). Valores na secção 3 (propriedade "Teor de níquel"); ainda não é critério em criterios.csv.

## 8. Apoio já existente

- relatorio/apoio/: nenhum ficheiro específico do stent.
- Linhas que referem o stent noutros ficheiros:

  - relatorio/00_resumo_executivo.md: linhas 13, 18, 24
  - docs/TP2_fisiopatologia_da_falha.md: linhas 105, 118, 122, 126, 130, 134, 136, 138, 140, 146, 148, 150, 181, 223, 236, 251, 264, 272, 282
  - docs/TP2_guia_de_fontes.md: linhas 24, 50, 58, 60, 64, 65, 66, 93, 94, 136, 137, 138, 139, 141, 175, 177, 180, 222, 231
  - docs/backlog_artigo.md: linhas 16, 21
