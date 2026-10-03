# Stent vascular: export de dados (commit 3ec4143, 03/10/2026)

Gerado por scripts/exportar_caso.py a partir de data/, src/ e results/. Só dados.

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

Cenários aplicáveis (cenarios.csv):

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
- P-foco: Foco no problema crítico do professor (2 out 2026): peso dos critérios de ligação direta x2 (fator_foco_problema), restantes renormalizados; sensibilidade: direta + indireta (data/problemas_criticos.csv). Par articular: sensibilidade semiquantitativa à parte

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

Pesos no cenário A (renormalizados): Índice material de recuo elástico σy/E (proxy) 0,118; Espessura típica de strut 0,235; Alongamento na rotura 0,118; Resistência à tração 0,118; Módulo de Young 0,059; Radiopacidade (ordinal 1-5) 0,118; Compatibilidade com RM (ordinal 1-5) 0,059; Compatibilidade com esterilização (ordinal 1-5) 0,059; Custo relativo de material e fabrico (1-5, 5 = mais caro) 0,059; Fabricabilidade (ordinal 1-5) 0,059

Pesos no cenário B (renormalizados): Índice material de recuo elástico σy/E (proxy) 0,1; Espessura típica de strut 0,2; Alongamento na rotura 0,1; Resistência à tração 0,1; Módulo de Young 0,05; Radiopacidade (ordinal 1-5) 0,1; Compatibilidade com RM (ordinal 1-5) 0,05; Compatibilidade com esterilização (ordinal 1-5) 0,05; Custo relativo de material e fabrico (1-5, 5 = mais caro) 0,05; Fabricabilidade (ordinal 1-5) 0,05; Tempo de reabsorção 0,15

## 3. Valores (materiais.csv e índices derivados)

| Material | Propriedade | Unidade | Típico | Mín. | Máx. | Texto | Fonte | doi_url | Estado |
|---|---|---|---|---|---|---|---|---|---|
| Aço inox 316L | Alongamento na rotura | % | 40 | 40 | 50 |  | Alleima, ficha 316LVM (tubo de parede fina recozido); patente US 6780261 B2 (Scimed), tubo de stent totalmente recozido | https://patents.google.com/patent/US6780261B2/en | Verificado (fornecedor) |
| Co-Cr L605 | Alongamento na rotura | % | 40 | 40 | 40 |  | Lamineries Matthey, ficha Alloy L-605 v26E (fita recozida, declara ASTM F90); Fort Wayne Metals, L-605 alloy (fio) | https://www.matthey.ch/fileadmin/user_upload/downloads/fichetechnique/EN/Alloy_L-605_v26E.pdf | Verificado (fornecedor) |
| Co-Ni-Cr-Mo MP35N | Alongamento na rotura | % | 40 | 40 | 40 |  | K-Tube, MP35N Technical Data Sheet (tubo miniatura para stents); Ulbrich, MP35N Wire UNS R30035 (fio, declara ASTM F562) | https://www.k-tube.com/wp-content/uploads/2025/12/MP35N-K-Tube-Technical-Data-Sheet.pdf | Verificado (fornecedor) |
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
| Aço inox 316L | Densidade | g/cm³ | 8 | 8 | 8 |  | Alleima, ficha 316LVM |  | Verificado (fornecedor) |
| Co-Cr L605 | Densidade | g/cm³ | 9,27 | 9,07 | 9,27 |  | Lamineries Matthey, ficha Alloy L-605 v26E (fita); Haynes International, HAYNES 25 | https://www.matthey.ch/fileadmin/user_upload/downloads/fichetechnique/EN/Alloy_L-605_v26E.pdf | Verificado (fornecedor) |
| Co-Ni-Cr-Mo MP35N | Densidade | g/cm³ | 8,43 | 8,43 | 8,43 |  | Ulbrich, MP35N Wire UNS R30035 (declara ASTM F562) | https://www.ulbrich.com/uploads/data-sheets/MP35N-Wire-UNS-R30035.pdf | Verificado (fornecedor) |
| Liga de Mg WE43 (bioabsorvível) | Densidade | g/cm³ | 1,84 | 1,84 | 1,84 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Densidade | g/cm³ | 6,45 | 6,45 | 6,45 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Densidade | g/cm³ | 1,27 | 1,25 | 1,29 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Densidade | g/cm³ | 9,9 | 9,9 | 9,9 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Aço inox 316L | Espessura típica de strut | µm | 135 | 130 | 140 |  | Nikam N, Steinberg TB, Steinberg DH. Med Devices (Auckl) 2014;7:165-178 (Tabela 1) | https://doi.org/10.2147/MDER.S31869 | Verificado |
| Co-Cr L605 | Espessura típica de strut | µm | 81 | 81 | 81 |  | Macaya-Ten F et al. REC Interv Cardiol 2024 (Tabela 3); Brami P et al. J Clin Med 2023 | https://doi.org/10.24875/RECICE.M24000463 | Verificado |
| Co-Ni-Cr-Mo MP35N | Espessura típica de strut | µm | 90 | 90 | 91 |  | Brami P et al. J Clin Med 2023; Macaya-Ten F et al. REC Interv Cardiol 2024 (Tabela 3) | https://doi.org/10.3390/jcm12216711 | Verificado |
| Liga de Mg WE43 (bioabsorvível) | Espessura típica de strut | µm | 135 | 120 | 150 |  | Rapetto C, Leoncini M. J Thorac Dis 2017 (Tabela 1); Seguchi M et al. EuroIntervention 2023;19:e167 | https://doi.org/10.21037/jtd.2017.06.34 | Verificado |
| Nitinol (autoexpansível) | Espessura típica de strut | µm | 125 | 100 | 150 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Espessura típica de strut | µm | 155 | 150 | 160 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Espessura típica de strut | µm | 79 | 74 | 81 |  | Boston Scientific, SYNERGY Product Spec Sheet | https://www.bostonscientific.com/content/dam/bostonscientific/Interventional%20Cardiology/portfolio-group/Stents/Synergy/legacy-resource-center/SYNERGY-Product-Spec-Sheet.pdf | Verificado (fornecedor) |
| Aço inox 316L | Fabricabilidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Co-Cr L605 | Fabricabilidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Fabricabilidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Fabricabilidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Nitinol (autoexpansível) | Fabricabilidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| PLLA (bioabsorvível) | Fabricabilidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Pt-Cr | Fabricabilidade (ordinal 1-5) | - | 4 | 4 | 4 |  | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |  | A verificar |
| Aço inox 316L | Módulo de Young | GPa | 193 | 193 | 193 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Módulo de Young | GPa | 225 | 225 | 225 |  | Lamineries Matthey, ficha Alloy L-605 v26E (fita recozida, declara ASTM F90); Haynes International, HAYNES 25 (chapa solubilizada); Fort Wayne Metals, L-605 alloy (barra e fio) | https://www.matthey.ch/fileadmin/user_upload/downloads/fichetechnique/EN/Alloy_L-605_v26E.pdf | Verificado (fornecedor) |
| Co-Ni-Cr-Mo MP35N | Módulo de Young | GPa | 233 | 233 | 233 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Módulo de Young | GPa | 44,5 | 44 | 45 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Módulo de Young | GPa | 57,5 | 40 | 75 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Módulo de Young | GPa | 3,35 | 3,1 | 3,6 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Módulo de Young | GPa | 203 | 203 | 203 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Radiopacidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Co-Cr L605 | Radiopacidade (ordinal 1-5) | - | 4 | 4 | 4 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Co-Ni-Cr-Mo MP35N | Radiopacidade (ordinal 1-5) | - | 3 | 3 | 3 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Liga de Mg WE43 (bioabsorvível) | Radiopacidade (ordinal 1-5) | - | 1 | 1 | 1 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Nitinol (autoexpansível) | Radiopacidade (ordinal 1-5) | - | 2 | 2 | 2 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| PLLA (bioabsorvível) | Radiopacidade (ordinal 1-5) | - | 1 | 1 | 1 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Pt-Cr | Radiopacidade (ordinal 1-5) | - | 5 | 5 | 5 |  | Allocco DJ et al. Trials 2010;11:1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr); rubrica no LEIA-ME (teor de elementos de Z alto) | https://doi.org/10.1186/1745-6215-11-1 | Verificado |
| Aço inox 316L | Resistência à tração | MPa | 592,5 | 515 | 670 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Resistência à tração | MPa | 996 | 900 | 1000 |  | Lamineries Matthey, ficha Alloy L-605 v26E (fita recozida, declara ASTM F90); Haynes International, HAYNES 25 (chapa solubilizada); Fort Wayne Metals, L-605 alloy (barra e fio) | https://www.matthey.ch/fileadmin/user_upload/downloads/fichetechnique/EN/Alloy_L-605_v26E.pdf | Verificado (fornecedor) |
| Co-Ni-Cr-Mo MP35N | Resistência à tração | MPa | 965 | 965 | 965 |  | K-Tube, MP35N Technical Data Sheet (tubo miniatura para stents); Ulbrich, MP35N Wire UNS R30035 (fio, declara ASTM F562) | https://www.k-tube.com/wp-content/uploads/2025/12/MP35N-K-Tube-Technical-Data-Sheet.pdf | Verificado (fornecedor) |
| Liga de Mg WE43 (bioabsorvível) | Resistência à tração | MPa | 250 | 220 | 280 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Resistência à tração | MPa | 1185 | 1070 | 1300 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Resistência à tração | MPa | 65 | 60 | 70 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Resistência à tração | MPa | 834 | 834 | 834 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Ni-Cr-Mo MP35N | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Tempo de reabsorção | meses | 18 | 12 | 24 |  | Joner M et al. EuroIntervention 2018 (DREAMS 2G/Magmaris, porco); Seguchi M et al. EuroIntervention 2023;19:e167 (pré-clínico, mini-porcos) | https://doi.org/10.4244/EIJ-D-17-00708 | Verificado |
| Nitinol (autoexpansível) | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Tempo de reabsorção | meses | 42 | 36 | 48 |  | FDA SSED PMA P150023 (Absorb GT1); Gogas BD et al. Int J Cardiovasc Imaging 2012 | https://www.accessdata.fda.gov/cdrh_docs/pdf15/P150023B.pdf | Verificado |
| Pt-Cr | Tempo de reabsorção | meses |  |  |  |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Aço inox 316L | Tensão de cedência | MPa | 272,5 | 205 | 340 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Co-Cr L605 | Tensão de cedência | MPa | 476 | 380 | 700 |  | Lamineries Matthey, ficha Alloy L-605 v26E (fita recozida, declara ASTM F90); Haynes International, HAYNES 25 (chapa solubilizada); Fort Wayne Metals, L-605 alloy (barra e fio) | https://www.matthey.ch/fileadmin/user_upload/downloads/fichetechnique/EN/Alloy_L-605_v26E.pdf | Verificado (fornecedor) |
| Co-Ni-Cr-Mo MP35N | Tensão de cedência | MPa | 412,5 | 410 | 415 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| Liga de Mg WE43 (bioabsorvível) | Tensão de cedência | MPa | 172,5 | 150 | 195 |  | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |  | A verificar |
| Nitinol (autoexpansível) | Tensão de cedência | MPa | 475 | 350 | 600 |  | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |  | A verificar |
| PLLA (bioabsorvível) | Tensão de cedência | MPa | 60 | 50 | 70 |  | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |  | A verificar |
| Pt-Cr | Tensão de cedência | MPa | 480 | 480 | 480 |  | O'Brien BJ, Stinson JS, Larsen SR, Eppihimer MJ, Carroll WM. A platinum-chromium steel for cardiovascular stents. Biomaterials 2010;31:3755-3761 | https://doi.org/10.1016/j.biomaterials.2010.01.146 | Verificado |
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
| Co-Cr L605 | Índice material de recuo elástico σy/E (proxy) | - | 0,0021 | 0,0017 | 0,0031 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Co-Ni-Cr-Mo MP35N | Índice material de recuo elástico σy/E (proxy) | - | 0,0018 | 0,0018 | 0,0018 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Liga de Mg WE43 (bioabsorvível) | Índice material de recuo elástico σy/E (proxy) | - | 0,0039 | 0,0033 | 0,0044 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Nitinol (autoexpansível) | Índice material de recuo elástico σy/E (proxy) | - | 0,0083 | 0,0047 | 0,015 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| PLLA (bioabsorvível) | Índice material de recuo elástico σy/E (proxy) | - | 0,0179 | 0,0139 | 0,0226 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |
| Pt-Cr | Índice material de recuo elástico σy/E (proxy) | - | 0,0024 | 0,0024 | 0,0024 |  | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |  | A verificar (derivado) |

Linhas: 104; estados: A verificar 66; Verificado 16; Verificado (fornecedor) 14; A verificar (derivado) 7; Verificado (composição química) 1

## 4. Rankings (η = 1)

### Cenário A

Critérios: Índice material de recuo elástico σy/E (proxy); Espessura típica de strut; Alongamento na rotura; Resistência à tração; Módulo de Young; Radiopacidade (ordinal 1-5); Compatibilidade com RM (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro); Fabricabilidade (ordinal 1-5)

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Pt-Cr | 0,657 (1) | 0,851 (2) | 0 (1) |
| Co-Cr L605 | 0,633 (2) | 0,865 (1) | 0,024 (2) |
| Co-Ni-Cr-Mo MP35N | 0,58 (3) | 0,832 (3) | 0,102 (3) |
| Aço inox 316L | 0,309 (4) | 0,754 (4) | 1 (4) |

ΔC 1.º-2.º (TOPSIS) = 0,024 (regra: < 0,01 = empate)

### Cenário B

Critérios: Índice material de recuo elástico σy/E (proxy); Espessura típica de strut; Alongamento na rotura; Resistência à tração; Módulo de Young; Radiopacidade (ordinal 1-5); Compatibilidade com RM (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro); Fabricabilidade (ordinal 1-5); Tempo de reabsorção

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Co-Cr L605 | 0,675 (1) | 0,727 (1) | 0 (1) |
| Pt-Cr | 0,673 (2) | 0,717 (2) | 0,012 (2) |
| Co-Ni-Cr-Mo MP35N | 0,641 (3) | 0,702 (3) | 0,047 (3) |
| Aço inox 316L | 0,472 (4) | 0,645 (4) | 0,323 (4) |
| Liga de Mg WE43 (bioabsorvível) | 0,441 (5) | 0,471 (5) | 0,421 (5) |
| PLLA (bioabsorvível) | 0,15 (6) | 0,272 (6) | 1 (6) |

ΔC 1.º-2.º (TOPSIS) = 0,002 (regra: < 0,01 = empate)

### Cenário B-bio

Critérios: Índice material de recuo elástico σy/E (proxy); Espessura típica de strut; Alongamento na rotura; Resistência à tração; Módulo de Young; Radiopacidade (ordinal 1-5); Compatibilidade com RM (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro); Fabricabilidade (ordinal 1-5); Tempo de reabsorção

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Liga de Mg WE43 (bioabsorvível) | 1 (1) | 0,978 (1) | 0 (1) |
| PLLA (bioabsorvível) | 0 (2) | 0,525 (2) | 1 (2) |

ΔC 1.º-2.º (TOPSIS) = 1 (regra: < 0,01 = empate)

## 5. Robustez (results/resumo_robustez.md)

η = 1 no resultado principal; sensibilidades a partir do cenário A. Monte Carlo: 10000 iterações, seed 42. No MC propriedades, as propriedades quantitativas com mín. = máx. variam ±10 % à volta do típico (data/parametros.csv).

Vencedor no cenário A: TOPSIS Pt-Cr; WASPAS Co-Cr L605; VIKOR Pt-Cr

#### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | Pt-Cr | Co-Cr L605 | Pt-Cr | 0,80 |
| B | B | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| B-bio (comparação) | B-bio | Liga de Mg WE43 (bioabsorvível) | Liga de Mg WE43 (bioabsorvível) | Liga de Mg WE43 (bioabsorvível) | n/a |
| R-sentinela | 60 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| R-sentinela | 120 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| R-sentinela | 600 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,94 |
| R-sentinela | 1200 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,94 |
| Q | sem ordinais | Pt-Cr | Co-Cr L605 | Pt-Cr | 0,40 |
| η | η = 0,0 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| η | η = 0,1 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| η | η = 0,2 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | -0,20 |
| η | η = 0,3 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,40 |
| η | η = 0,4 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,40 |
| η | η = 0,5 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,6 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,80 |
| η | η = 0,7 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,8 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,9 | Pt-Cr | Co-Cr L605 | Co-Cr L605 | 0,80 |
| η | η = 1,0 | Pt-Cr | Co-Cr L605 | Pt-Cr | 0,80 |
| C-custo | custo baixo (0,01) | Pt-Cr | Co-Cr L605 | Pt-Cr | 0,80 |
| C-custo | custo elevado (0,25) | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| P-foco | direta | Pt-Cr | Co-Cr L605 | Pt-Cr | 0,80 |
| P-foco | direta + indireta | Pt-Cr | Co-Cr L605 | Pt-Cr | 0,80 |

#### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Pt-Cr | 69,9 % | 56,6 % | 59,1 % |
| Co-Cr L605 | 27,1 % | 41,8 % | 31,7 % |
| Co-Ni-Cr-Mo MP35N | 3,0 % | 1,6 % | 9,1 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Pt-Cr | 85,5 % | 0,0 % | 58,9 % |
| Co-Cr L605 | 14,5 % | 100,0 % | 40,9 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |
| Co-Ni-Cr-Mo MP35N | 0,0 % | 0,0 % | 0,2 % |

#### Onde o vencedor muda (face ao cenário A)

- B, B, TOPSIS: Pt-Cr → Co-Cr L605
- B, B, VIKOR: Pt-Cr → Co-Cr L605
- R-sentinela, 60 meses, TOPSIS: Pt-Cr → Co-Cr L605
- R-sentinela, 60 meses, VIKOR: Pt-Cr → Co-Cr L605
- R-sentinela, 120 meses, TOPSIS: Pt-Cr → Co-Cr L605
- R-sentinela, 120 meses, VIKOR: Pt-Cr → Co-Cr L605
- R-sentinela, 600 meses, TOPSIS: Pt-Cr → Co-Cr L605
- R-sentinela, 600 meses, VIKOR: Pt-Cr → Co-Cr L605
- R-sentinela, 1200 meses, TOPSIS: Pt-Cr → Co-Cr L605
- R-sentinela, 1200 meses, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,0, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,0, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,0, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,1, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,1, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,1, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,2, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,2, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,2, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,3, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,3, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,4, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,4, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,5, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,5, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,6, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,6, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,7, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,7, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,8, TOPSIS: Pt-Cr → Co-Cr L605
- η, η = 0,8, VIKOR: Pt-Cr → Co-Cr L605
- η, η = 0,9, VIKOR: Pt-Cr → Co-Cr L605
- C-custo, custo elevado (0,25), TOPSIS: Pt-Cr → Co-Cr L605
- C-custo, custo elevado (0,25), WASPAS: Co-Cr L605 → Aço inox 316L
- C-custo, custo elevado (0,25), VIKOR: Pt-Cr → Co-Cr L605

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

## 7. Valores "A verificar" por influência (results/por_verificar.md)

Vencedor do TOPSIS: cenário A: Pt-Cr; cenário B: Co-Cr L605.
Células a verificar: 43 (3 mudam o vencedor com ±20 %).

| # | Cenário | Material | Critério | Tipo | Típico | ΔC material | ΔC máx. | Muda vencedor | Fonte atual |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A | Pt-Cr | Alongamento na rotura | quantitativo | 45,0000 | 0,071 | 0,097 | sim → Co-Cr L605 | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |
| 2 | A | Co-Cr L605 | Índice material de recuo elástico σy/E (proxy) | derivado | 0,0021 | 0,039 | 0,039 | sim → Co-Cr L605 | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |
| 3 | A | Pt-Cr | Resistência à tração | quantitativo | 834,0000 | 0,034 | 0,034 | sim → Co-Cr L605 | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |
| 4 | A | Pt-Cr | Índice material de recuo elástico σy/E (proxy) | derivado | 0,0024 | 0,040 | 0,040 | não | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |
| 5 | B | PLLA (bioabsorvível) | Espessura típica de strut | quantitativo | 155,0000 | 0,039 | 0,055 | não | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |
| 6 | B | PLLA (bioabsorvível) | Compatibilidade com RM (ordinal 1-5) | ordinal | 5,0000 | 0,034 | 0,034 | não | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |
| 7 | A | Co-Ni-Cr-Mo MP35N | Índice material de recuo elástico σy/E (proxy) | derivado | 0,0018 | 0,029 | 0,029 | não | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |
| 8 | A | Aço inox 316L | Fabricabilidade (ordinal 1-5) | ordinal | 5,0000 | 0,022 | 0,022 | não | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |
| 9 | A | Co-Cr L605 | Fabricabilidade (ordinal 1-5) | ordinal | 5,0000 | 0,020 | 0,020 | não | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |
| 10 | A | Aço inox 316L | Módulo de Young | quantitativo | 193,0000 | 0,019 | 0,019 | não | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |
| 11 | A | Co-Ni-Cr-Mo MP35N | Módulo de Young | quantitativo | 233,0000 | 0,019 | 0,019 | não | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |
| 12 | A | Co-Ni-Cr-Mo MP35N | Fabricabilidade (ordinal 1-5) | ordinal | 5,0000 | 0,019 | 0,019 | não | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |
| 13 | A | Aço inox 316L | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 4,0000 | 0,017 | 0,017 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 14 | A | Pt-Cr | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 4,0000 | 0,015 | 0,017 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 15 | A | Co-Cr L605 | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 4,0000 | 0,014 | 0,017 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 16 | B | Liga de Mg WE43 (bioabsorvível) | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 4,0000 | 0,013 | 0,013 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 17 | A | Pt-Cr | Módulo de Young | quantitativo | 203,0000 | 0,013 | 0,013 | não | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |
| 18 | A | Co-Ni-Cr-Mo MP35N | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 4,0000 | 0,012 | 0,017 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 19 | A | Co-Ni-Cr-Mo MP35N | Compatibilidade com RM (ordinal 1-5) | ordinal | 3,0000 | 0,010 | 0,010 | não | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |
| 20 | A | Co-Cr L605 | Compatibilidade com RM (ordinal 1-5) | ordinal | 3,0000 | 0,010 | 0,010 | não | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |
| 21 | A | Pt-Cr | Compatibilidade com RM (ordinal 1-5) | ordinal | 3,0000 | 0,009 | 0,009 | não | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |
| 22 | B | Liga de Mg WE43 (bioabsorvível) | Compatibilidade com RM (ordinal 1-5) | ordinal | 5,0000 | 0,006 | 0,026 | não | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |
| 23 | B | PLLA (bioabsorvível) | Fabricabilidade (ordinal 1-5) | ordinal | 3,0000 | 0,005 | 0,005 | não | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |
| 24 | A | Co-Cr L605 | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 3,0000 | 0,005 | 0,005 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 25 | A | Co-Ni-Cr-Mo MP35N | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 3,0000 | 0,004 | 0,004 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 26 | B | Liga de Mg WE43 (bioabsorvível) | Fabricabilidade (ordinal 1-5) | ordinal | 3,0000 | 0,004 | 0,004 | não | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |
| 27 | B | PLLA (bioabsorvível) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 5,0000 | 0,004 | 0,004 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 28 | B | Liga de Mg WE43 (bioabsorvível) | Alongamento na rotura | quantitativo | 13,5000 | 0,004 | 0,004 | não | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |
| 29 | B | Liga de Mg WE43 (bioabsorvível) | Índice material de recuo elástico σy/E (proxy) | derivado | 0,0039 | 0,003 | 0,003 | não | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |
| 30 | B | Liga de Mg WE43 (bioabsorvível) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 5,0000 | 0,003 | 0,003 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 31 | B | Liga de Mg WE43 (bioabsorvível) | Resistência à tração | quantitativo | 250,0000 | 0,003 | 0,003 | não | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |
| 32 | B | Liga de Mg WE43 (bioabsorvível) | Módulo de Young | quantitativo | 44,5000 | 0,001 | 0,001 | não | Witte F. Acta Biomater 2010;6:1680-1692 (Mg) |
| 33 | A | Aço inox 316L | Índice material de recuo elástico σy/E (proxy) | derivado | 0,0014 | 0,000 | 0,017 | não | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |
| 34 | A | Aço inox 316L | Resistência à tração | quantitativo | 592,5000 | 0,000 | 0,013 | não | Hanawa T. J Artif Organs 2009;12:73-79 (metais para stents) |
| 35 | A | Pt-Cr | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 4,0000 | 0,000 | 0,006 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 36 | B | PLLA (bioabsorvível) | Índice material de recuo elástico σy/E (proxy) | derivado | 0,0179 | 0,000 | 0,003 | não | Calculado: tensão de cedência / módulo de Young (src/biomat_mcdm/indices.py) |
| 37 | B | PLLA (bioabsorvível) | Alongamento na rotura | quantitativo | 4,0000 | 0,000 | 0,001 | não | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |
| 38 | B | PLLA (bioabsorvível) | Resistência à tração | quantitativo | 65,0000 | 0,000 | 0,001 | não | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |
| 39 | A | Aço inox 316L | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 1,0000 | 0,000 | 0,001 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 40 | B | PLLA (bioabsorvível) | Módulo de Young | quantitativo | 3,3500 | 0,000 | 0,000 | não | Ensaios ABSORB / comunicação FDA 2017 (Absorb BVS) |
| 41 | A | Aço inox 316L | Compatibilidade com RM (ordinal 1-5) | ordinal | 2,0000 | 0,000 | 0,000 | não | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |
| 42 | A | Pt-Cr | Fabricabilidade (ordinal 1-5) | ordinal | 4,0000 | 0,000 | 0,000 | não | Geetha 2009; Navarro 2008; literatura de fabrico aditivo: confirmar |
| 43 | B | PLLA (bioabsorvível) | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,000 | 0,000 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |

## 8. Notas (linhas literais de docs/NOTAS_METODOLOGICAS.md e data/leia_me.md)

- MCDM quantitativo: haste femoral, stent coronário expansível por balão, scaffold ósseo.
- Nitinol (autoexpansível, periférico) fora do ranking; só na discussão.
- Cenários (data/cenarios.csv): A = só materiais em uso clínico; B = inclui investigação e bioabsorvíveis. No stent, A = só permanentes (316L, L605, MP35N, Pt-Cr); B = A + Mg WE43 e PLLA.
- Tempo de reabsorção do stent (critério só do cenário B; alvo 12 meses):
  - B (opção O2): os permanentes recebem o pior valor observado (48 meses, máximo do PLLA). Interpretação: "não reabsorver é pelo menos tão mau como o pior bioabsorvível". Limitação: subestima o caso permanente (um permanente nunca reabsorve). Coerente nos três métodos, que usam os valores em bruto.
- σy/E (src/biomat_mcdm/indices.py, calculado a partir de σy e E da base; intervalo = σy mín./E máx. a σy máx./E mín.): proxy ao nível do material da deformação elástica na cedência. Em stents expansíveis por balão, maior σy/E → maior recuo elástico → critério de CUSTO. Não é o recuo do dispositivo (depende da geometria do padrão, struts, processamento).
  - estatuto "Excluído" na base elimina (Nitinol: autoexpansível, outra classe de dispositivo);
  - regras categóricas (valor em texto na coluna valor_texto): "Tipo de expansão" = balão ou autoexpansível; passa se o valor está no alvo ("Expansível por balão");
  - resultado atual: eliminados o MoM (segurança iónica 1 < 2) e o Nitinol (tipo de expansão autoexpansível; também pelo estatuto "Excluído").
- HA não reabsorvível (scaffold, 1 out 2026): o tempo de degradação da HA segue a lógica da opção O2 do stent: mínimo 42 meses (sem reabsorção em 3,5 anos) e máximo e típico iguais ao pior valor observado nos outros materiais do scaffold (60 meses, PLLA). É um valor de modelação e subestima a permanência real da HA.
- Densidade removida como proxy de radiopacidade (depende do número atómico efetivo e da espessura). Com a rubrica de radiopacidade (data/leia_me.md, 1 out 2026), a densidade continua a não ser critério do stent, mas serve de evidência de apoio para a ordem da radiopacidade (Allocco 2010, doi:10.1186/1745-6215-11-1).
  em 10 000 com o Co-Cr-Mo forjado) e 100 % no WASPAS e no VIKOR. Nos três casos (haste, stent,
  scaffold) o vencedor do Monte Carlo não muda; no stent, o 1.º lugar do Co-Cr L605 desce
## Stent: fontes e regras (30 set 2026)
  e o típico cobrem só a forma usada no dispositivo. No stent (cortado a laser de tubo), essa forma
  (Resolute, 90 µm) e o L605 (XIENCE, 81 µm) reflete o desenho do stent, não uma limitação da liga.
- Tempos de reabsorção do PLLA (Absorb) e do Mg (Magmaris): as fontes encontradas são de modelos
  et al. 2025 ficaram iguais (o típico era o ponto médio). O σy/E derivado usa agora σy típico / E típico.
## Fontes do texto do stent (1 out 2026)
Referências das frases de relatorio/caso_stent_rascunho.md. "Só resumo" quando o texto completo não foi lido.
  Vascular Stents and Endovascular Prostheses (o âmbito da edição F2477-19 indicava 10 anos a 72 batimentos por
  Tests and Recommended Labeling for Intravascular Stents and Associated Delivery Systems. 18 abr 2010,
- Espessura de strut e reestenose (Q2): Kastrati A, Mehilli J, Dirschinger J, et al. Intracoronary stenting and
- Alergia ao níquel (Q3): Köster R, Vieluf D, Kiehn M, et al. Nickel and molybdenum contact allergies in patients
  with coronary in-stent restenosis. Lancet 2000;356:1895-1897, doi:10.1016/S0140-6736(00)03262-1 (só resumo).
  Gong Z, Li M, Guo X, et al. Stent implantation in patients with metal allergy: a systemic review and
  associação). Norgaz T, Hobikoglu G, Serdar ZA, et al. Is there a link between nickel allergy and coronary stent
  Three-year outcomes of bioresorbable vascular scaffolds versus second-generation drug-eluting stents. Medicine
- Struts do 316L (Q8): Nikam N, Steinberg TB, Steinberg DH. Advances in stent technologies and their effect on
- Fabrico do stent de magnésio (Q9): Moravej M, Mantovani D. Biodegradable metals for cardiovascular stent
- Normas (Q10): ISO 25539-2:2020, Cardiovascular implants, Endovascular devices, Part 2: Vascular stents. ASTM
  F2079-09(2022), Standard Test Method for Measuring Intrinsic Elastic Recoil of Balloon-Expandable Stents. ASTM
  F3067-26, Standard Guide for Radial Loading of Balloon-Expandable and Self-Expanding Vascular Stents. Edições em
- [ ] Tipo de expansão dos stents (data/materiais.csv, 7 linhas "A verificar", sem referência).

leia_me.md:

Densidade deixa de ser proxy de radiopacidade (nova escala de radiopacidade) · σy/E renomeado "proxy material" · Nitinol fora do ranking · K_IC retirado do par articular · "Resistência" retirada da matriz dentária (tração ≠ flexão) · alvos do scaffold passam a cenários · nova folha Cenarios
Par articular e implante dentário ficam SEMIQUANTITATIVOS (ordinais > 50 % do peso): MCDM quantitativo só para haste, stent (balão) e scaffold.
- Nova propriedade "Tipo de expansão" do stent (balão ou autoexpansível), usada na triagem.
- Índices derivados calculados em src/biomat_mcdm/indices.py (σy/E do stent; E_implante/E_osso da haste).
## Alterações v0.5 (1 out 2026): 2.ª ronda do stent
- Densidades do 316L, L605, MP35N e Pt-Cr com fonte. A densidade não é critério do stent.
- HA: tempo de degradação tratado como não reabsorvível (mínimo 42 meses; máximo e típico = pior valor observado nos outros materiais, como a opção O2 do stent).
## Alterações v0.8 (2 out 2026): regra da forma revista (stent)
- Regra da forma: nas propriedades dependentes da forma do produto, min, max e tipico cobrem só a forma usada no dispositivo (no stent: tubo ou fita); os valores de outras formas (fio, barra, chapa) ficam só na coluna notas. Se a forma do dispositivo tiver um único valor, min = max e o Monte Carlo aplica ±10 % (incerteza_valor_unico em parametros.csv).
  - "Verificado (composição química)": valor que resulta da composição química do material (ex.: 0 % de níquel num polímero sem metais).
- Teor de níquel (stent): % em massa; no WE43 é um limite máximo de impureza e tipico = máximo (pior caso).
- Radiopacidade (stent): 5 = liga com fração elevada de elemento de Z alto (Pt-Cr); 4 = melhoria clara face ao 316L (L605, com W); 3 = referência dos metais de stent (316L, MP35N); 2 = pouco radiopaco (Nitinol); 1 = radiotransparente, precisa de marcadores (Mg WE43, PLLA). Critério: teor de elementos de Z alto (Pt, Z = 78; W, Z = 74). A densidade não é critério (desde a v0.3), serve só de evidência de apoio. Fontes: Allocco DJ et al. Trials 2010;11:1, doi:10.1186/1745-6215-11-1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr face ao aço).
3. Stents: o Nitinol é autoexpansível (outra classe): eliminado na triagem pela regra "Tipo de expansão"; só na discussão.
4. Cenários (cenarios.csv): A = só materiais clínicos; B = inclui investigação e bioabsorvíveis. No stent, A = só permanentes em uso clínico (316L, L605, MP35N, Pt-Cr); B = A + Mg WE43 e PLLA.

## 9. Apoio já existente

Linhas que referem o caso noutros ficheiros:

- relatorio/00_resumo_executivo.md: linhas 13, 18, 24
- docs/TP2_fisiopatologia_da_falha.md: linhas 105, 118, 122, 126, 130, 134, 136, 138, 140, 146, 148, 150, 181, 223, 236, 251, 264, 272, 282
- docs/TP2_guia_de_fontes.md: linhas 24, 50, 58, 60, 64, 65, 66, 93, 94, 136, 137, 138, 139, 141, 175, 177, 180, 222, 231
- docs/backlog_artigo.md: linhas 16, 21
