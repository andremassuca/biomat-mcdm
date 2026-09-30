# Scaffold ósseo: export de dados (commit f10facb, 30/09/2026)

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
| Compósito PCL/β-TCP (impressão 3D) | Bioatividade (ordinal 1-5) | - | 3 | 3 | 3 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Hidroxiapatite (HA) porosa | Bioatividade (ordinal 1-5) | - | 4 | 4 | 4 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PCL | Bioatividade (ordinal 1-5) | - | 1 | 1 | 1 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PLGA 50:50 | Bioatividade (ordinal 1-5) | - | 1 | 1 | 1 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| PLLA | Bioatividade (ordinal 1-5) | - | 1 | 1 | 1 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Quitosano/HA (liofilizado) | Bioatividade (ordinal 1-5) | - | 3 | 3 | 3 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Vidro bioativo 45S5 poroso | Bioatividade (ordinal 1-5) | - | 5 | 5 | 5 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| β-TCP poroso | Bioatividade (ordinal 1-5) | - | 4 | 4 | 4 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Hidroxiapatite (HA) porosa | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| PCL | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| PLGA 50:50 | Compatibilidade com esterilização (ordinal 1-5) | - | 2 | 2 | 2 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| PLLA | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Quitosano/HA (liofilizado) | Compatibilidade com esterilização (ordinal 1-5) | - | 3 | 3 | 3 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Vidro bioativo 45S5 poroso | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| β-TCP poroso | Compatibilidade com esterilização (ordinal 1-5) | - | 5 | 5 | 5 |  | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
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
| Quitosano/HA (liofilizado) | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Vidro bioativo 45S5 poroso | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| β-TCP poroso | Imprimibilidade 3D (ordinal 1-5) | - | 2 | 2 | 2 |  | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Módulo de compressão (scaffold) | MPa | 90 | 30 | 150 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Hidroxiapatite (HA) porosa | Módulo de compressão (scaffold) | MPa | 1750 | 500 | 3000 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PCL | Módulo de compressão (scaffold) | MPa | 50 | 20 | 80 |  | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |  | A verificar |
| PLGA 50:50 | Módulo de compressão (scaffold) | MPa | 35 | 10 | 60 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PLLA | Módulo de compressão (scaffold) | MPa | 175 | 50 | 300 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Quitosano/HA (liofilizado) | Módulo de compressão (scaffold) | MPa | 5,5 | 1 | 10 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Vidro bioativo 45S5 poroso | Módulo de compressão (scaffold) | MPa | 275 | 50 | 500 |  | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |  | A verificar |
| β-TCP poroso | Módulo de compressão (scaffold) | MPa | 550 | 100 | 1000 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Porosidade | % | 60 | 50 | 70 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| Hidroxiapatite (HA) porosa | Porosidade | % | 65 | 50 | 80 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| PCL | Porosidade | % | 65 | 50 | 80 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| PLGA 50:50 | Porosidade | % | 80 | 70 | 90 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| PLLA | Porosidade | % | 75 | 60 | 90 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| Quitosano/HA (liofilizado) | Porosidade | % | 87,5 | 80 | 95 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| Vidro bioativo 45S5 poroso | Porosidade | % | 80 | 70 | 90 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| β-TCP poroso | Porosidade | % | 65 | 50 | 80 |  | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Resistência à compressão (scaffold) | MPa | 7,5 | 3 | 12 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Hidroxiapatite (HA) porosa | Resistência à compressão (scaffold) | MPa | 11 | 2 | 20 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PCL | Resistência à compressão (scaffold) | MPa | 6 | 2 | 10 |  | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |  | A verificar |
| PLGA 50:50 | Resistência à compressão (scaffold) | MPa | 1,75 | 0,5 | 3 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PLLA | Resistência à compressão (scaffold) | MPa | 5,5 | 1 | 10 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Quitosano/HA (liofilizado) | Resistência à compressão (scaffold) | MPa | 0,55 | 0,1 | 1 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Vidro bioativo 45S5 poroso | Resistência à compressão (scaffold) | MPa | 1,15 | 0,3 | 2 |  | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |  | A verificar |
| β-TCP poroso | Resistência à compressão (scaffold) | MPa | 8 | 1 | 15 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Compósito PCL/β-TCP (impressão 3D) | Tempo de degradação | meses | 18 | 12 | 24 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Hidroxiapatite (HA) porosa | Tempo de degradação | meses | 42 | 24 | 60 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PCL | Tempo de degradação | meses | 30 | 24 | 36 |  | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |  | A verificar |
| PLGA 50:50 | Tempo de degradação | meses | 2 | 1 | 3 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| PLLA | Tempo de degradação | meses | 27 | 18 | 36 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Quitosano/HA (liofilizado) | Tempo de degradação | meses | 7,5 | 3 | 12 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |
| Vidro bioativo 45S5 poroso | Tempo de degradação | meses | 9 | 6 | 12 |  | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |  | A verificar |
| β-TCP poroso | Tempo de degradação | meses | 12 | 6 | 18 |  | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |  | A verificar |

Linhas: 64; estados: A verificar 64

## 4. Rankings (η = 1)

### Cenário A

Critérios: Resistência à compressão (scaffold); Módulo de compressão (scaffold); Porosidade; Tempo de degradação; Bioatividade (ordinal 1-5); Imprimibilidade 3D (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro)

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| β-TCP poroso | 0,645 (1) | 0,718 (1) | 0 (1) |
| Compósito PCL/β-TCP (impressão 3D) | 0,6 (2) | 0,669 (2) | 0,125 (2) |
| Vidro bioativo 45S5 poroso | 0,599 (3) | 0,662 (3) | 0,163 (3) |
| PCL | 0,48 (4) | 0,625 (4) | 0,705 (4) |
| Hidroxiapatite (HA) porosa | 0,422 (5) | 0,494 (5) | 1 (5) |

ΔC 1.º-2.º (TOPSIS) = 0,045 (regra: < 0,01 = empate)

### Cenário B

Critérios: Resistência à compressão (scaffold); Módulo de compressão (scaffold); Porosidade; Tempo de degradação; Bioatividade (ordinal 1-5); Imprimibilidade 3D (ordinal 1-5); Compatibilidade com esterilização (ordinal 1-5); Custo relativo de material e fabrico (1-5, 5 = mais caro)

| Material | TOPSIS C (pos.) | WASPAS Q (pos.) | VIKOR P, menor = melhor (pos.) |
|---|---|---|---|
| Compósito PCL/β-TCP (impressão 3D) | 0,647 (1) | 0,736 (2) | 0,053 (1) |
| β-TCP poroso | 0,641 (2) | 0,753 (1) | 0,059 (2) |
| Vidro bioativo 45S5 poroso | 0,593 (3) | 0,69 (3) | 0,157 (3) |
| PCL | 0,521 (4) | 0,669 (4) | 0,633 (5) |
| PLLA | 0,508 (5) | 0,665 (5) | 0,697 (6) |
| Quitosano/HA (liofilizado) | 0,488 (6) | 0,564 (6) | 0,607 (4) |
| Hidroxiapatite (HA) porosa | 0,46 (7) | 0,5 (8) | 0,804 (7) |
| PLGA 50:50 | 0,416 (8) | 0,537 (7) | 1 (8) |

ΔC 1.º-2.º (TOPSIS) = 0,006 (regra: < 0,01 = empate)

## 5. Robustez (results/resumo_robustez.md)

η = 1 no resultado principal; sensibilidades a partir do cenário A. Monte Carlo: 10000 iterações, seed 42. No MC propriedades, as propriedades quantitativas com mín. = máx. variam ±10 % à volta do típico (data/parametros.csv).

Vencedor no cenário A: TOPSIS β-TCP poroso; WASPAS β-TCP poroso; VIKOR β-TCP poroso

#### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| B | B | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,88 |
| Q | sem ordinais | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| η | η = 0,0 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| η | η = 0,1 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| η | η = 0,2 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,3 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,4 | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,5 | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,6 | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,7 | β-TCP poroso | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,8 | β-TCP poroso | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,9 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| η | η = 1,0 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| T-scaffold | Resistência à compressão: 2 | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | 1,00 |
| T-scaffold | Resistência à compressão: 12 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 0,90 |
| T-scaffold | Módulo de compressão: 50 | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | 0,50 |
| T-scaffold | Módulo de compressão: 500 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 0,90 |
| T-scaffold | Porosidade: 50 | β-TCP poroso | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| T-scaffold | Porosidade: 90 | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | 1,00 |
| T-scaffold | Tempo de degradação: x0,5 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| T-scaffold | Tempo de degradação: x2,0 | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,80 |
| C-custo | custo baixo (0,01) | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| C-custo | custo elevado (0,25) | Compósito PCL/β-TCP (impressão 3D) | PCL | PCL | 0,70 |

#### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| β-TCP poroso | 53,6 % | 31,6 % | 37,4 % |
| Vidro bioativo 45S5 poroso | 28,2 % | 23,7 % | 38,8 % |
| Compósito PCL/β-TCP (impressão 3D) | 18,2 % | 43,0 % | 23,8 % |
| PCL | 0,0 % | 1,7 % | 0,0 % |
| Hidroxiapatite (HA) porosa | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| β-TCP poroso | 91,7 % | 100,0 % | 85,3 % |
| Compósito PCL/β-TCP (impressão 3D) | 8,3 % | 0,0 % | 14,7 % |
| Hidroxiapatite (HA) porosa | 0,0 % | 0,0 % | 0,0 % |
| PCL | 0,0 % | 0,0 % | 0,0 % |
| Vidro bioativo 45S5 poroso | 0,0 % | 0,0 % | 0,0 % |

#### Onde o vencedor muda (face ao cenário A)

- B, B, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- B, B, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,0, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,0, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,0, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,1, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,1, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,1, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,2, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,2, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,2, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,3, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,3, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,3, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,4, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,4, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,5, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,5, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,6, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,6, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,7, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,8, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Resistência à compressão: 2, TOPSIS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Resistência à compressão: 2, WASPAS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Resistência à compressão: 2, VIKOR: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Módulo de compressão: 50, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Porosidade: 50, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Porosidade: 90, TOPSIS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Porosidade: 90, WASPAS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Porosidade: 90, VIKOR: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Tempo de degradação: x2,0, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Tempo de degradação: x2,0, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- C-custo, custo elevado (0,25), TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- C-custo, custo elevado (0,25), WASPAS: β-TCP poroso → PCL
- C-custo, custo elevado (0,25), VIKOR: β-TCP poroso → PCL

## 6. Triagem (critérios estritos)

| Material | Critério | Regra | Valor | Resultado | Motivo |
|---|---|---|---|---|---|

## 7. Valores "A verificar" por influência (results/por_verificar.md)

Vencedor do TOPSIS: cenário B: Compósito PCL/β-TCP (impressão 3D); cenário A: β-TCP poroso.
Células a verificar: 64 (3 mudam o vencedor com ±20 %).

| # | Cenário | Material | Critério | Tipo | Típico | ΔC material | ΔC máx. | Muda vencedor | Fonte atual |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | Quitosano/HA (liofilizado) | Porosidade | quantitativo | 87,5000 | 0,040 | 0,041 | sim → β-TCP poroso | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 2 | B | Quitosano/HA (liofilizado) | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,010 | 0,017 | sim → β-TCP poroso | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 3 | B | PLGA 50:50 | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 2,0000 | 0,000 | 0,014 | sim → β-TCP poroso | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 4 | A | Hidroxiapatite (HA) porosa | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 5,0000 | 0,047 | 0,047 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 5 | A | Hidroxiapatite (HA) porosa | Bioatividade (ordinal 1-5) | ordinal | 4,0000 | 0,038 | 0,038 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 6 | B | PLLA | Porosidade | quantitativo | 75,0000 | 0,038 | 0,038 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 7 | A | Compósito PCL/β-TCP (impressão 3D) | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,037 | 0,037 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 8 | A | β-TCP poroso | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 5,0000 | 0,034 | 0,034 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 9 | A | β-TCP poroso | Bioatividade (ordinal 1-5) | ordinal | 4,0000 | 0,034 | 0,034 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 10 | A | β-TCP poroso | Porosidade | quantitativo | 65,0000 | 0,033 | 0,033 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 11 | A | Compósito PCL/β-TCP (impressão 3D) | Bioatividade (ordinal 1-5) | ordinal | 3,0000 | 0,030 | 0,030 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 12 | A | Hidroxiapatite (HA) porosa | Resistência à compressão (scaffold) | quantitativo | 11,0000 | 0,029 | 0,029 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 13 | A | Compósito PCL/β-TCP (impressão 3D) | Porosidade | quantitativo | 60,0000 | 0,027 | 0,027 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 14 | B | PLGA 50:50 | Porosidade | quantitativo | 80,0000 | 0,027 | 0,027 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 15 | A | PCL | Tempo de degradação | quantitativo | 30,0000 | 0,027 | 0,027 | não | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |
| 16 | B | Quitosano/HA (liofilizado) | Bioatividade (ordinal 1-5) | ordinal | 3,0000 | 0,026 | 0,026 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 17 | A | Vidro bioativo 45S5 poroso | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 5,0000 | 0,026 | 0,032 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 18 | A | Vidro bioativo 45S5 poroso | Porosidade | quantitativo | 80,0000 | 0,024 | 0,026 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 19 | A | PCL | Imprimibilidade 3D (ordinal 1-5) | ordinal | 5,0000 | 0,024 | 0,024 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 20 | A | Compósito PCL/β-TCP (impressão 3D) | Imprimibilidade 3D (ordinal 1-5) | ordinal | 5,0000 | 0,023 | 0,023 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 21 | A | β-TCP poroso | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 3,0000 | 0,022 | 0,022 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 22 | B | PLLA | Imprimibilidade 3D (ordinal 1-5) | ordinal | 4,0000 | 0,020 | 0,020 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 23 | A | PCL | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,019 | 0,029 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 24 | A | β-TCP poroso | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,019 | 0,019 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 25 | A | PCL | Porosidade | quantitativo | 65,0000 | 0,019 | 0,019 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 26 | A | Compósito PCL/β-TCP (impressão 3D) | Tempo de degradação | quantitativo | 18,0000 | 0,019 | 0,019 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 27 | B | PLLA | Tempo de degradação | quantitativo | 27,0000 | 0,018 | 0,018 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 28 | A | Hidroxiapatite (HA) porosa | Porosidade | quantitativo | 65,0000 | 0,018 | 0,018 | não | Karageorgiou V, Kaplan D. Biomaterials 2005;26:5474-5491 (porosidade) |
| 29 | B | Quitosano/HA (liofilizado) | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,016 | 0,016 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 30 | B | PLGA 50:50 | Imprimibilidade 3D (ordinal 1-5) | ordinal | 3,0000 | 0,015 | 0,015 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 31 | B | PLLA | Compatibilidade com esterilização (ordinal 1-5) | ordinal | 3,0000 | 0,015 | 0,015 | não | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |
| 32 | A | Hidroxiapatite (HA) porosa | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 3,0000 | 0,014 | 0,014 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 33 | A | β-TCP poroso | Resistência à compressão (scaffold) | quantitativo | 8,0000 | 0,013 | 0,013 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 34 | B | PLGA 50:50 | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 2,0000 | 0,012 | 0,012 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 35 | A | Vidro bioativo 45S5 poroso | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,011 | 0,017 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 36 | B | Quitosano/HA (liofilizado) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 2,0000 | 0,011 | 0,011 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 37 | A | Compósito PCL/β-TCP (impressão 3D) | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 2,0000 | 0,011 | 0,011 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 38 | A | PCL | Resistência à compressão (scaffold) | quantitativo | 6,0000 | 0,010 | 0,010 | não | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |
| 39 | A | Compósito PCL/β-TCP (impressão 3D) | Resistência à compressão (scaffold) | quantitativo | 7,5000 | 0,010 | 0,010 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 40 | B | PLLA | Resistência à compressão (scaffold) | quantitativo | 5,5000 | 0,010 | 0,010 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 41 | A | β-TCP poroso | Tempo de degradação | quantitativo | 12,0000 | 0,009 | 0,009 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 42 | B | PLLA | Bioatividade (ordinal 1-5) | ordinal | 1,0000 | 0,009 | 0,009 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 43 | A | Vidro bioativo 45S5 poroso | Tempo de degradação | quantitativo | 9,0000 | 0,009 | 0,012 | não | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |
| 44 | A | Hidroxiapatite (HA) porosa | Imprimibilidade 3D (ordinal 1-5) | ordinal | 2,0000 | 0,007 | 0,017 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 45 | B | PLGA 50:50 | Bioatividade (ordinal 1-5) | ordinal | 1,0000 | 0,006 | 0,008 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 46 | B | Quitosano/HA (liofilizado) | Tempo de degradação | quantitativo | 7,5000 | 0,006 | 0,006 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 47 | B | PLLA | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 1,0000 | 0,005 | 0,005 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 48 | A | β-TCP poroso | Módulo de compressão (scaffold) | quantitativo | 550,0000 | 0,004 | 0,004 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 49 | B | PLGA 50:50 | Resistência à compressão (scaffold) | quantitativo | 1,7500 | 0,003 | 0,003 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 50 | B | PLGA 50:50 | Tempo de degradação | quantitativo | 2,0000 | 0,003 | 0,003 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 51 | A | Hidroxiapatite (HA) porosa | Módulo de compressão (scaffold) | quantitativo | 1750,0000 | 0,001 | 0,003 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 52 | B | PLLA | Módulo de compressão (scaffold) | quantitativo | 175,0000 | 0,001 | 0,001 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 53 | A | Vidro bioativo 45S5 poroso | Resistência à compressão (scaffold) | quantitativo | 1,1500 | 0,001 | 0,001 | não | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |
| 54 | A | Vidro bioativo 45S5 poroso | Módulo de compressão (scaffold) | quantitativo | 275,0000 | 0,001 | 0,001 | não | Hench LL. J Am Ceram Soc 1991;74:1487-1510 (vidros bioativos) |
| 55 | A | PCL | Módulo de compressão (scaffold) | quantitativo | 50,0000 | 0,001 | 0,001 | não | Woodruff MA, Hutmacher DW. Prog Polym Sci 2010;35:1217-1256 (PCL) |
| 56 | A | Compósito PCL/β-TCP (impressão 3D) | Módulo de compressão (scaffold) | quantitativo | 90,0000 | 0,001 | 0,001 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 57 | B | Quitosano/HA (liofilizado) | Resistência à compressão (scaffold) | quantitativo | 0,5500 | 0,000 | 0,001 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 58 | B | PLGA 50:50 | Módulo de compressão (scaffold) | quantitativo | 35,0000 | 0,000 | 0,000 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 59 | B | Quitosano/HA (liofilizado) | Módulo de compressão (scaffold) | quantitativo | 5,5000 | 0,000 | 0,000 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 60 | A | Vidro bioativo 45S5 poroso | Bioatividade (ordinal 1-5) | ordinal | 5,0000 | 0,000 | 0,043 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 61 | A | Hidroxiapatite (HA) porosa | Tempo de degradação | quantitativo | 42,0000 | 0,000 | 0,029 | não | Rezwan K et al. Biomaterials 2006;27:3413-3431 (scaffolds ósseos) |
| 62 | A | Vidro bioativo 45S5 poroso | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 4,0000 | 0,000 | 0,027 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |
| 63 | A | PCL | Bioatividade (ordinal 1-5) | ordinal | 1,0000 | 0,000 | 0,005 | não | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |
| 64 | A | PCL | Custo relativo de material e fabrico (1-5, 5 = mais caro) | ordinal | 1,0000 | 0,000 | 0,004 | não | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |

## 8. Notas (linhas literais de docs/NOTAS_METODOLOGICAS.md e data/leia_me.md)

- MCDM quantitativo: haste femoral, stent coronário expansível por balão, scaffold ósseo.
- Alvos do scaffold = cenário de referência para osso trabecular, não ótimo universal (cenário T-scaffold).
- T-scaffold: alvos no mínimo e no máximo do osso trabecular (tecido.csv) para compressão (2-12 MPa), módulo (50-500 MPa) e porosidade (50-90 %); tempo de degradação sem referência no tecido: fatores de sensibilidade x0,5 e x2 sobre o alvo (não são valores da literatura).
- Reversão de ranking observada (scaffold, 28 set 2026): ao retirar PLLA, PLGA e quitosano/HA (cenário A com os estatutos novos), o β-TCP e o PCL/β-TCP trocam de posição (TOPSIS e VIKOR: PCL/β-TCP 1.º com 8 materiais, β-TCP 1.º com 5), porque as normalizações dependem do mínimo e do máximo de cada coluna. Exemplo concreto para o item "Testes formais de reversão de ranking" do backlog e para a secção de limitações.
- Scaffold: a fragilidade do ranking reflete em parte a incerteza dos dados (propriedades muito dependentes da porosidade, intervalos largos na base) e não só o método. Na discussão, separar as duas causas, por exemplo comparando a % de 1.º lugar do MC propriedades (incerteza dos dados) com a do W pesos (incerteza das preferências). Cenário A com os estatutos novos (5 materiais): β-TCP 53,6 % / 31,6 % / 37,4 % (T/W/V) no MC propriedades, mas 91,7 % / 100 % / 85,3 % no W pesos; ou seja, o 1.º lugar é estável face aos pesos e frágil face aos dados.
  scaffold) o vencedor do Monte Carlo não muda; no stent, o 1.º lugar do Co-Cr L605 desce
  mín. e o máx. Um típico fora de [mín., máx.] dá erro. Haste, scaffold e reprodução de Petković
- [ ] Estatuto clínico dos 8 materiais do scaffold (Clínico (substituto ósseo) / Clínico (uso limitado) / Investigação), proposto a 28 set 2026; fonte a verificar indicada na coluna notas de data/materiais.csv (Rezwan et al. 2006, Bose et al. 2012, Hench 1991, Woodruff & Hutmacher 2010, Athanasiou et al. 1996, base 510(k) da FDA; PCL/β-TCP e quitosano/HA sem fonte).

leia_me.md:

Densidade deixa de ser proxy de radiopacidade (nova escala de radiopacidade) · σy/E renomeado "proxy material" · Nitinol fora do ranking · K_IC retirado do par articular · "Resistência" retirada da matriz dentária (tração ≠ flexão) · alvos do scaffold passam a cenários · nova folha Cenarios
Par articular e implante dentário ficam SEMIQUANTITATIVOS (ordinais > 50 % do peso): MCDM quantitativo só para haste, stent (balão) e scaffold.
1. Propriedades de scaffolds dependem da porosidade: compara só valores com porosidades semelhantes, ou regista a porosidade.

## 9. Apoio já existente

Linhas que referem o caso noutros ficheiros:

- relatorio/00_resumo_executivo.md: linhas 14, 18, 24, 25
- docs/TP2_fisiopatologia_da_falha.md: linhas 146, 173, 177, 185, 189, 195, 197, 208, 223, 252, 280, 283, 287
- docs/TP2_guia_de_fontes.md: linhas 24, 140, 141, 142, 144, 145, 146, 149, 178, 179, 182, 184, 185, 186, 187, 231
- docs/backlog_artigo.md: linhas 14, 24
