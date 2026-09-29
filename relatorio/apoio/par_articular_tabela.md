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
| Taxa de desgaste linear | mm/ano | 0,15 (0,1-0,2) | 0,03 (0,01-0,05) | 0,025 (0,01-0,04) | 0,003 (0,001-0,005) | 0,0065 (0,003-0,01) |
| Segurança iónica / risco ALTR (ordinal 1-5) | - | 4 | 4 | 5 | 5 | 1 |
| Dureza da cabeça | HV | 375 (300-450) | 375 (300-450) | 1862,5 (1750-1975) | 1862,5 (1750-1975) | 375 (300-450) |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | - | 3 | 3 | 5 | 5 | 2 |
| Compatibilidade com esterilização (ordinal 1-5) | - | 2 | 4 | 4 | 5 | 5 |
| Compatibilidade com RM (ordinal 1-5) | - | 3 | 3 | 5 | 5 | 2 |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | - | 1 | 2 | 3 | 4 | 3 |

## 4. Fontes e estado

| Critério | Par | Fonte (referencia) | doi_url | Estado |
|---|---|---|---|---|
| Taxa de desgaste linear | CoCrMo / UHMWPE convencional | Kurtz SM. UHMWPE Biomaterials Handbook, 3rd ed., 2016 |  | A verificar |
| Taxa de desgaste linear | CoCrMo / HXLPE | Kurtz SM. UHMWPE Biomaterials Handbook, 3rd ed., 2016 |  | A verificar |
| Taxa de desgaste linear | ZTA / HXLPE | Kurtz SM. UHMWPE Biomaterials Handbook, 3rd ed., 2016 |  | A verificar |
| Taxa de desgaste linear | ZTA / ZTA | Kurtz SM. UHMWPE Biomaterials Handbook, 3rd ed., 2016 |  | A verificar |
| Taxa de desgaste linear | CoCrMo / CoCrMo | Kurtz SM. UHMWPE Biomaterials Handbook, 3rd ed., 2016 |  | A verificar |
| Segurança iónica / risco ALTR (ordinal 1-5) | CoCrMo / UHMWPE convencional | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Segurança iónica / risco ALTR (ordinal 1-5) | CoCrMo / HXLPE | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Segurança iónica / risco ALTR (ordinal 1-5) | ZTA / HXLPE | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Segurança iónica / risco ALTR (ordinal 1-5) | ZTA / ZTA | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Segurança iónica / risco ALTR (ordinal 1-5) | CoCrMo / CoCrMo | Escala ordinal definida no trabalho (rubrica em LEIA-ME): justificar com literatura |  | A verificar |
| Dureza da cabeça | CoCrMo / UHMWPE convencional | Chevalier J. Biomaterials 2006;27:535-543 (zircónia/envelhecimento) |  | A verificar |
| Dureza da cabeça | CoCrMo / HXLPE | Chevalier J. Biomaterials 2006;27:535-543 (zircónia/envelhecimento) |  | A verificar |
| Dureza da cabeça | ZTA / HXLPE | Chevalier J. Biomaterials 2006;27:535-543 (zircónia/envelhecimento) |  | A verificar |
| Dureza da cabeça | ZTA / ZTA | Chevalier J. Biomaterials 2006;27:535-543 (zircónia/envelhecimento) |  | A verificar |
| Dureza da cabeça | CoCrMo / CoCrMo | Chevalier J. Biomaterials 2006;27:535-543 (zircónia/envelhecimento) |  | A verificar |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | CoCrMo / UHMWPE convencional | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | CoCrMo / HXLPE | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | ZTA / HXLPE | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | ZTA / ZTA | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar |
| Compatibilidade galvânica cabeça-cone (ordinal 1-5) | CoCrMo / CoCrMo | Literatura sobre corrosão na junção cabeça-cone (trunnionosis): confirmar |  | A verificar |
| Compatibilidade com esterilização (ordinal 1-5) | CoCrMo / UHMWPE convencional | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Compatibilidade com esterilização (ordinal 1-5) | CoCrMo / HXLPE | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Compatibilidade com esterilização (ordinal 1-5) | ZTA / HXLPE | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Compatibilidade com esterilização (ordinal 1-5) | ZTA / ZTA | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Compatibilidade com esterilização (ordinal 1-5) | CoCrMo / CoCrMo | ISO 11137 (radiação) / ISO 11135 (EtO); Kurtz 2016 para UHMWPE: confirmar |  | A verificar |
| Compatibilidade com RM (ordinal 1-5) | CoCrMo / UHMWPE convencional | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Compatibilidade com RM (ordinal 1-5) | CoCrMo / HXLPE | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Compatibilidade com RM (ordinal 1-5) | ZTA / HXLPE | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Compatibilidade com RM (ordinal 1-5) | ZTA / ZTA | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Compatibilidade com RM (ordinal 1-5) | CoCrMo / CoCrMo | Shellock FG / MRIsafety.com; ASTM F2182 (aquecimento) e F2119 (artefactos): confirmar |  | A verificar |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | CoCrMo / UHMWPE convencional | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | CoCrMo / HXLPE | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | ZTA / HXLPE | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | ZTA / ZTA | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |
| Custo relativo de material e fabrico (1-5, 5 = mais caro) | CoCrMo / CoCrMo | Índice relativo de material e fabrico (rubrica no LEIA-ME); não representa preço hospitalar |  | A verificar |

## 5. Estatuto e notas por par

| Par | Estatuto | Notas (materiais.csv) |
|---|---|---|
| CoCrMo / UHMWPE convencional (MoP) | Clínico | OBRIGATÓRIO indicar tipo de evidência: in vivo (radiográfico/RSA) vs simulador ISO 14242: não misturar ; Osteólise por partículas de PE; corrosão na junção cabeça-cone / Cabeça CoCr em cone de Ti: corrosão por fretting documentada / PE convencional esterilizado por gama ao ar → oxidação (histórico) / Cabeça CoCr (a haste também conta: ver nota metodológica) |
| CoCrMo / HXLPE (MoXLPE) | Clínico | OBRIGATÓRIO indicar tipo de evidência: in vivo (radiográfico/RSA) vs simulador ISO 14242: não misturar ; PE altamente reticulado; oxidação se radiação gama sem estabilização / Idem / HXLPE refundido/recozido ou com vitamina E |
| ZTA / HXLPE (CoXLPE) | Clínico | OBRIGATÓRIO indicar tipo de evidência: in vivo (radiográfico/RSA) vs simulador ISO 14242: não misturar ; Cerâmica na cabeça elimina corrosão na junção / Cabeça cerâmica elimina o par galvânico / Idem |
| ZTA / ZTA (CoC) | Clínico | OBRIGATÓRIO indicar tipo de evidência: in vivo (radiográfico/RSA) vs simulador ISO 14242: não misturar ; Risco de fratura baixo mas não nulo; ruído (squeaking) / Idem / Cerâmicos e metais: sem limitações |
| CoCrMo / CoCrMo (MoM) | Clínico (abandonado) | OBRIGATÓRIO indicar tipo de evidência: in vivo (radiográfico/RSA) vs simulador ISO 14242: não misturar ; Iões Co/Cr, ALTR; recolha ASR 2010: candidato a eliminar na triagem / Fretting no cone + desgaste metálico na articulação / Idem / Duas superfícies CoCr |

## 6. Pontos em aberto para a Q8

- Vitamina E: não está na base (nenhum par com HXLPE estabilizado com vitamina E).
- Todos os valores do par articular estão "A verificar" (ver secção 4).
- Taxa de desgaste: a nota do CSV exige indicar o tipo de evidência (in vivo vs simulador ISO 14242) e não misturar os dois.
