# Apoio ao relatório: caso da prótese da anca (haste femoral e par articular)

Regra: só listas, tabelas e fontes. O texto é escrito pelo André.
Estado dos dados: todos os valores da base de dados estão "A verificar" (54 da haste, 35 do
par articular). Fonte: data/materiais.csv, data/criterios.csv; gerado a 27 set 2026.

---

## 1. Pontos a cobrir nas 11 questões

Enunciado: docs/enunciado_TP2.md (local, não versionado). Legenda: "Fisiopat." =
docs/TP2_fisiopatologia_da_falha.md; "Guia" = docs/TP2_guia_de_fontes.md; "2.1"/"2.2"/"3" =
secções deste ficheiro. [fonte a indicar] = ponto sem fonte nos docs: não usar sem referência.

Proposta atual (relatorio/00_resumo_executivo.md): haste em Ti-6Al-4V ELI; cabeça em ZTA;
acetábulo em HXLPE estabilizado com vitamina E (vitamina E: [fonte a indicar], não está na base).

### Q1. Qual é a função do dispositivo?
- Haste:
  - [ ] Transmitir a carga da articulação ao fémur (carga cíclica: ~1-2 milhões de ciclos de marcha/ano, justificação da fadiga em data/criterios.csv; Silva et al. 2002 [confirmar], Guia 6.3)
  - [ ] Fixação ao osso a longo prazo (cimentada ou não cimentada) [fonte a indicar]
  - [ ] Suportar a cabeça femoral através do cone (junção modular) (Fisiopat. 1.4.7)
- Par articular:
  - [ ] Permitir o movimento com baixo atrito e baixo desgaste (Fisiopat. 1.4.1)
  - [ ] Componentes: cabeça femoral + componente acetabular (2.2)
- Ambos:
  - [ ] Contexto: artroplastia total da anca como intervenção de sucesso; descolamento asséptico como causa importante de revisão a longo prazo (Fisiopat. 1.1)
  - [ ] Números de causas de revisão: só NJR ou AOANJRR, com edição e ano (Guia 5; Fisiopat. 1.5)
  - [ ] Horizonte temporal: vida do material vs vida funcional vs vida clínica vs vida do doente (Fisiopat. "Cinco horizontes temporais")

### Q2. Que propriedades mecânicas são necessárias?
- Haste:
  - [ ] Módulo de Young próximo do osso (alvo 17 GPa na base; 14 GPa em Petković et al. 2025: ver P3) → stress shielding (Fisiopat. 1.4.8; Huiskes et al. 1992 🟡)
  - [ ] Limite de fadiga a 10^7 ciclos: critério com maior peso (0,25); valores em 2.1 (280 a 750 MPa)
  - [ ] Tensão de cedência: evitar deformação plástica (2.1: 440 a 872 MPa)
  - [ ] Compromisso rigidez vs fadiga: as ligas β de Ti (TNZT, 60,5 GPa) têm menor módulo mas menor fadiga (357,5 MPa) (2.1; resumo executivo, notas)
  - [ ] Ensaio normalizado de resistência e fadiga de componentes femorais: ISO 7206 (Guia 3)
- Par articular:
  - [ ] Dureza da cabeça: resistência a riscos por terceiro corpo (2.2: 375 HV CoCrMo vs 1862,5 HV ZTA; Chevalier 2006 🟡)
  - [ ] Resistência à fratura da cabeça cerâmica: critério estrito, avaliação qualitativa; K_IC fora da matriz (data/criterios.csv; LEIA-ME v0.3)
  - [ ] Caso Prozyr: fraturas por alteração do processo de fabrico (Fisiopat. Casos históricos; Masonis et al. 2004 🟡)

### Q3. Que propriedades químicas e físicas são relevantes?
- Haste:
  - [ ] Resistência à corrosão, camada passiva (2.1: ordinal 3 a 5; rubrica em LEIA-ME)
  - [ ] Densidade (2.1: 4,43 a 8,4 g/cm³; peso 0,05; já não é proxy de radiopacidade, LEIA-ME v0.3)
  - [ ] Compatibilidade com RM: artefacto e aquecimento (2.1: 316L = 2, Co-Cr = 3, Ti = 4; ASTM F2182/F2119 [confirmar])
  - [ ] Superfície para fixação não cimentada: rugosidade, molhabilidade [fonte a indicar] (ver Caracterização)
- Par articular:
  - [ ] Taxa de desgaste linear (2.2: 0,003 a 0,15 mm/ano; indicar tipo de evidência, in vivo radiográfico)
  - [ ] Oxidação do polietileno, reticulação (Fisiopat. 1.4.1; 1.6: FTIR)
  - [ ] Compatibilidade com esterilização (2.2; ISO 11137 / ISO 11135; Kurtz 2016 [confirmar]); caso Hylamer (Fisiopat. Casos históricos)
  - [ ] Compatibilidade galvânica cabeça-cone (2.2; Fisiopat. 1.4.7)
  - [ ] Envelhecimento hidrotérmico da zircónia (Chevalier 2006 🟡; base: nota na dureza)

### Q4. Como será a biocompatibilidade?
- Ambos:
  - [ ] Critério estrito de triagem: ISO 10993 (data/criterios.csv); avaliação biológica no quadro da gestão de risco: ISO 10993-1 (Guia 3)
  - [ ] Biocompatibilidade como resposta adequada do hospedeiro numa aplicação específica (Williams 2008 🟡, Guia 6.2)
  - [ ] Reação a corpo estranho comum a todos os implantes (Fisiopat. "Resposta comum"; Anderson et al. 2008 🟡)
- Haste:
  - [ ] Libertação iónica e corrosão (rubrica de corrosão, 2.1); elementos de liga do Ti-6Al-4V (Al, V) vs ligas β sem V (Geetha et al. 2009 🟡) [confirmar no artigo]
- Par articular:
  - [ ] Partículas de desgaste como principal ameaça biológica (Fisiopat. 1.4.1-1.4.5)
  - [ ] Iões Co/Cr e hipersensibilidade tipo IV no metal-metal (Fisiopat. 1.4.6; Hallab & Jacobs 2009 [confirmar]) → MoM eliminado (estrito: segurança iónica ≥ 2)

### Q5. O material será bioinerte, bioativo ou biodegradável?
- Classificação de biocerâmicos (slides 32-33, Aula 2): Tipo 1 quase inertes; Tipo 2 microporosos; Tipo 3 bioativos; Tipo 4 reabsorvíveis
  - [ ] ZTA e alumina da cabeça femoral: Tipo 1 (quase inertes): alumina e zircónia nos cerâmicos cristalinos quase inertes (slides 32-33, Aula 2; Hench 1991 🟡, Guia 6.6)
  - [ ] Tipo 2/3 na anca: revestimento de hidroxiapatite em hastes não cimentadas; fosfatos de cálcio como revestimento e reforço de implantes metálicos (slides 34-35, Aula 2) [fonte clínica a indicar; não está na base]
  - [ ] Tipo 4: não se aplica à anca (é o caso do scaffold)
- Metais e polímeros (fora da classificação Tipo 1-4, que é só para cerâmicos):
  - [ ] Ligas de Ti, Co-Cr, 316L: bioinertes no sentido de não se ligarem quimicamente ao osso; camada passiva de óxido (rubrica de corrosão, 2.1)
  - [ ] UHMWPE/HXLPE: bioinerte; o problema são as partículas, não o material em bloco (Fisiopat. 1.4.1)
- [ ] Nenhum componente da anca deve ser biodegradável (função permanente)

### Q6. Existe risco de corrosão, desgaste ou degradação?
- Haste:
  - [ ] Corrosão em fenda e fretting na junção cabeça-cone (Fisiopat. 1.4.7; Cooper et al. 2012 🟡; ASTM F1875, Guia 3)
  - [ ] Corrosão generalizada: 316L mais suscetível (2.1: ordinal 3)
  - [ ] Fratura por fadiga da haste (ligar a Q2)
- Par articular:
  - [ ] Desgaste por par tribológico (2.2): MoP 0,15 > MoXLPE 0,03 > CoXLPE 0,025 > MoM 0,0065 > CoC 0,003 mm/ano
  - [ ] Oxidação do polietileno ao longo do tempo (Fisiopat. "Cinco horizontes": vida do material)
  - [ ] Envelhecimento da zircónia (Chevalier 2006 🟡)
  - [ ] Iões metálicos no MoM (Fisiopat. 1.4.6); caso ASR 2010 (Fisiopat. Casos históricos [confirmar])
- [ ] Ranking dia 0 vs ano 10: as propriedades evoluem no corpo (Fisiopat. "Cinco horizontes"; backlog: trabalho futuro)

### Q7. Como o organismo poderá responder ao material?
- Par articular (via principal):
  - [ ] Cascata: partículas → fagocitose (TLR, NLRP3) → NF-κB, TNF-α, IL-1β, IL-6, PGE2 → RANKL/OPG → osteoclastos → osteólise → micromovimento → mais partículas (Fisiopat. 1.4.1-1.4.5; Goodman & Gallo 2019 🟡)
  - [ ] Tamanho submicrométrico das partículas de UHMWPE (Green et al. 1998 [confirmar])
  - [ ] Hipersensibilidade tipo IV, ALVAL, pseudotumores no MoM (Fisiopat. 1.4.6)
- Haste:
  - [ ] Stress shielding e remodelação (mecanostato; Frost 1987 [confirmar]; Huiskes et al. 1992 🟡)
  - [ ] Corrosão cabeça-cone com reação local mesmo sem par metal-metal (Fisiopat. 1.4.7)
- Ambos:
  - [ ] Sinais de falha e exames: radiografia, TC, iões séricos, RM MARS, diagnóstico diferencial com infeção (Fisiopat. 1.2, 1.3)
  - [ ] Nem todas as revisões se devem ao material: luxação, infeção, fratura periprotésica, erro técnico (Fisiopat. 1.5)

### Q8. Qual é a vantagem relativamente aos materiais atualmente utilizados?
- Haste (Ti-6Al-4V ELI vs 316L e Co-Cr):
  - [ ] Módulo 112 GPa vs 195 (316L) e 225 (Co-Cr) GPa: menos stress shielding (2.1)
  - [ ] Melhor corrosão e RM do que o 316L (2.1: 5 vs 3; 4 vs 2)
  - [ ] Fadiga inferior ao Co-Cr (575 vs 750 MPa): desvantagem a declarar
  - [ ] Resultado PRELIMINAR com os três métodos (results/haste_preliminar.md): 1.º em TOPSIS, WASPAS e VIKOR nos cenários A e B; ver secção 4
- Par articular (ZTA/HXLPE vs MoP convencional e MoM):
  - [ ] Desgaste 0,025 vs 0,15 mm/ano (MoP) (2.2)
  - [ ] Sem par metálico na junção cabeça-cone (galvânica 5 vs 3) (2.2; Fisiopat. 1.4.7)
  - [ ] Sem iões Co/Cr do par articular (vs MoM) (Fisiopat. 1.4.6)
  - [ ] Revisão por par tribológico em registos: Whitehouse et al. 2024 ✅ (financiado pela CeramTec: declarar); NJR/AOANJRR com edição e ano
- [ ] Limites: o modelo não substitui controlo de fabrico, validação do dispositivo e vigilância (Fisiopat. Casos históricos, parágrafo final)

### Q9. Como poderia ser fabricado?
- Haste:
  - [ ] Ligas normalizadas: Ti-6Al-4V ELI ASTM F136 / ISO 5832-3; Co-Cr-Mo forjado ASTM F799 / F1537; 316L ASTM F138 / ISO 5832-1 (Guia 3; dizer que as designações F dos slides da Aula 2 são normas ASTM)
  - [ ] Forjamento e maquinagem; fabrico aditivo de hastes porosas (fabricabilidade 2.1; Geetha 2009, Navarro 2008 [confirmar])
  - [ ] Revestimento de hidroxiapatite em hastes não cimentadas (fosfatos de cálcio como revestimento de implantes metálicos, slides 34-35, Aula 2) [fonte clínica a indicar]
- Par articular:
  - [ ] Cabeça ZTA: ISO 6474-2 (Guia 3); processo cerâmico [fonte a indicar]; lição Prozyr: controlo de qualidade por lote (Fisiopat. Casos históricos)
  - [ ] HXLPE: reticulação e esterilização; lição Hylamer (esterilização gama ao ar) (Kurtz 2016 🟡; Fisiopat. Casos históricos)
- [ ] Custo relativo de material e fabrico (rubrica LEIA-ME; não é preço hospitalar) (2.1, 2.2)

### Q10. Que testes serão necessários antes da utilização clínica?
- Biológicos:
  - [ ] ISO 10993-1 (avaliação no quadro da gestão de risco); ISO 10993-6 (efeitos locais após implantação); ISO 10993-18 (caracterização química, para o polietileno) (Guia 3)
- Mecânicos e tribológicos:
  - [ ] Haste: ISO 7206 (resistência e fadiga de componentes femorais)
  - [ ] Par articular: ISO 14242 (simulador de desgaste)
  - [ ] Junção cabeça-cone: ASTM F1875 (fretting-corrosão)
- Materiais:
  - [ ] Conformidade com as normas de material (Q9) e ISO 14630 (requisitos gerais de implantes não ativos)
- Regulação:
  - [ ] ISO 14971 (gestão de risco); MDR (UE) 2017/745, Anexo VIII (classe de risco: usar a formulação segura do Guia 4); avaliação clínica; vigilância pós-comercialização (FDA MAUDE, EUDAMED, INFARMED) (Guia 4)
- [ ] Seguimento após implantação: clínico e radiográfico (Fisiopat. "Seguimento e manutenção")

### Q11. Identifique as propriedades que caracterizam cada material tendo em conta a sua aplicação
- [ ] Tabela por material com as propriedades da secção 2 (haste: 2.1; par: 2.2), com intervalo, fonte e estado
- [ ] Ligação propriedade → mecanismo de falha → critério (Fisiopat. 1.6)
- [ ] Técnicas de caracterização por propriedade: ver a subsecção "Caracterização" abaixo
- [ ] Declarar: todos os valores "A verificar" até confirmação na fonte primária (LEIA-ME)

### Caracterização (lista do enunciado + técnicas dos slides da Aula 2)

Técnicas de uso geral não citadas nos docs estão marcadas [fonte a indicar]; as da tabela
1.6 da Fisiopat. estão marcadas como tal.

| Técnica ou propriedade | Propriedade medida | Material da anca | Porque importa | Fonte |
|---|---|---|---|---|
| Densidade | Massa volúmica (picnometria, método de Arquimedes) | Todos (2.1) | Critério de custo (peso 0,05) | [fonte a indicar] |
| Dureza | Dureza Vickers (HV) | Cabeça CoCrMo vs ZTA (2.2) | Riscos por terceiro corpo | Chevalier 2006 🟡 (valores); técnica [fonte a indicar] |
| Flexibilidade | Módulo de Young (ensaio de tração; flexão em cerâmicos) | Haste (2.1) | Stress shielding | Fisiopat. 1.6 (ensaio de tração) |
| Absorção de água | Ganho de massa por imersão (gravimetria) | Polietileno (baixa) | Pouco relevante na anca; relevante em polímeros degradáveis (scaffold) | [fonte a indicar] |
| Resistência mecânica | Tração, cedência, fadiga | Haste (2.1) | Fadiga é o critério com maior peso | ISO 7206 (Guia 3) |
| Comportamento térmico | DSC (cristalinidade), TGA | UHMWPE/HXLPE | Efeito da reticulação e do tratamento térmico | [fonte a indicar] |
| Condutividade elétrica / eletroquímica | Ensaios eletroquímicos de corrosão (polarização) [fonte a indicar] | Haste, cabeça metálica, cone | Corrosão galvânica cabeça-cone | Fisiopat. 1.6 (imersão + ICP-MS) |
| Microscopia: SEM/EDS | Morfologia e composição | Partículas de desgaste; superfícies de fretting | Osteólise; corrosão cabeça-cone | Fisiopat. 1.6 |
| Microscopia: AFM | Rugosidade à nanoescala | Superfície da cabeça femoral; superfície da haste | Desgaste; fixação | [fonte a indicar] |
| FTIR / ATR-FTIR | Índice de oxidação; grupos químicos da superfície | UHMWPE/HXLPE | Oxidação → desgaste | Fisiopat. 1.6 (FTIR) |
| Raman | Fases cristalinas | Zircónia na ZTA (fase tetragonal vs monoclínica) | Envelhecimento hidrotérmico | [fonte a indicar]; Chevalier 2006 🟡 (envelhecimento) |
| XRD | Fases cristalinas | Ligas de Ti (α, β); zircónia na ZTA | Microestrutura; envelhecimento | [fonte a indicar] |
| Ângulo de contacto | Molhabilidade da superfície | Haste não cimentada; cabeça | Adsorção de proteínas; lubrificação | [fonte a indicar] |
| XPS / ESCA | Química da camada passiva (primeiros nm) | Ligas de Ti, Co-Cr | Libertação iónica | Fisiopat. 1.6 |
| SIMS | Composição de superfície e perfil em profundidade | Camada de óxido das ligas | Contaminação, espessura do óxido | [fonte a indicar] |

---

## 2. Valores da base de dados

### 2.1 Haste femoral (ponto médio de mín.-máx.; todos "A verificar")

| Propriedade | 316L | Co-Cr-Mo forjado | Ti-6Al-4V ELI | Ti cp grau 4 | Ti-13Nb-13Zr | TNZT (só cen. B) | Fonte na base |
|---|---|---|---|---|---|---|---|
| Módulo de Young (GPa) | 195 (190-200) | 225 (210-240) | 112 (110-114) | 106,5 (103-110) | 81,5 (79-84) | 60,5 (55-66) | Niinomi 1998; Geetha 2009 (Ti-13Nb-13Zr, TNZT) |
| Limite de fadiga 10^7 ciclos (MPa) | 280 (180-380) | 750 (600-900) | 575 (500-650) | 385 (340-430) | 550 (500-600) | 357,5 (265-450) | Idem |
| Tensão de cedência (MPa) | 440 (190-690) | 850 (700-1000) | 835 (795-875) | 515 (480-550) | 872 (836-908) | 540 (530-550) | Idem |
| Densidade (g/cm³) | 7,95 | 8,4 | 4,43 | 4,51 | 5,0 | 5,7 | Idem |
| Corrosão (1-5) | 3 | 4 | 5 | 5 | 5 | 5 | Rubrica (LEIA-ME); justificar com literatura |
| Compatibilidade com RM (1-5) | 2 | 3 | 4 | 4 | 4 | 4 | Shellock / MRIsafety.com; ASTM F2182 e F2119 [confirmar] |
| Custo relativo (1-5, custo) | 1 | 3 | 3 | 2 | 4 | 5 | Rubrica (LEIA-ME); não é preço hospitalar |
| Fabricabilidade (1-5) | 5 | 4 | 5 | 4 | 3 | 2 | Geetha 2009; Navarro 2008 [confirmar] |

Critérios e pesos da haste (data/criterios.csv): E alvo 17 GPa (0,20); fadiga (0,25);
cedência (0,10); corrosão (0,15); densidade custo (0,05); RM (0,10); custo (0,05);
fabricabilidade (0,10). Ordinais somam 0,40 (regra: ≤ 0,50). Estrito: ISO 10993.

### 2.2 Par articular (semiquantitativo; todos "A verificar")

| Propriedade | MoP (CoCrMo/UHMWPE) | MoXLPE (CoCrMo/HXLPE) | CoXLPE (ZTA/HXLPE) | CoC (ZTA/ZTA) | MoM (abandonado) | Fonte na base |
|---|---|---|---|---|---|---|
| Desgaste linear (mm/ano) | 0,15 (0,1-0,2) | 0,03 (0,01-0,05) | 0,025 (0,01-0,04) | 0,003 (0,001-0,005) | 0,0065 (0,003-0,01) | Kurtz 2016, UHMWPE Biomaterials Handbook; notas: indicar tipo de evidência (in vivo radiográfico) |
| Segurança iónica / ALTR (1-5) | 4 | 4 | 5 | 5 | 1 (eliminado na triagem, estrito ≥ 2) | Rubrica (LEIA-ME) |
| Dureza da cabeça (HV) | 375 | 375 | 1862,5 | 1862,5 | 375 | Chevalier 2006 (zircónia/envelhecimento) |
| Galvânica cabeça-cone (1-5) | 3 | 3 | 5 | 5 | 2 | Literatura sobre trunnionosis [confirmar] |
| Esterilização (1-5) | 2 | 4 | 4 | 5 | 5 | ISO 11137 / ISO 11135; Kurtz 2016 [confirmar] |
| RM (1-5) | 3 | 3 | 5 | 5 | 2 | Shellock / MRIsafety.com; ASTM F2182 e F2119 [confirmar] |
| Custo relativo (1-5, custo) | 1 | 2 | 3 | 4 | 3 | Rubrica (LEIA-ME) |

Pesos: desgaste 0,35; segurança iónica 0,25; galvânica 0,15; custo 0,10; dureza, esterilização
e RM 0,05 cada. Estritos: segurança iónica ≥ 2; risco de fratura da cabeça cerâmica
(avaliação qualitativa, K_IC fora da matriz).

---

## 3. Fontes por tema (de docs/)

| Tema | Onde está | Referências [estado no guia] |
|---|---|---|
| Descolamento asséptico, osteólise (partículas → macrófagos → NF-κB → RANKL/OPG) | docs/TP2_fisiopatologia_da_falha.md, 1.4.1-1.4.5 | Green et al. 1998 [confirmar]; Goodman & Gallo 2019 [🟡] |
| Iões metálicos, ALTR, pseudotumores | 1.4.6 | Hallab & Jacobs 2009 [confirmar] |
| Corrosão cabeça-cone (trunnionosis) | 1.4.7 | Cooper et al. 2012 [🟡] |
| Stress shielding, mecanostato | 1.4.8 | Frost 1987 [confirmar]; Huiskes et al. 1992 [🟡] |
| Sinais, exames, diagnóstico diferencial | 1.2, 1.3 | (tabela na secção 1.3) |
| Causas de revisão (números) | 1.5 | Só relatório anual do NJR ou do AOANJRR, com edição e ano (guia, secção 5) |
| Mecanismo → propriedade → critério → técnica | 1.6 | (tabela na secção 1.6) |
| Casos históricos (PTFE, Hylamer, Prozyr, ASR) | Secção "Casos históricos de falha" | Masonis et al. 2004 [🟡]; restantes [confirmar] |
| Materiais para THA (revisão geral) | docs/TP2_guia_de_fontes.md, 6.3 | Hu & Yoon 2018 [✅] |
| Par articular e risco de revisão | 6.3 | Whitehouse et al. 2024 [✅] (financiado pela CeramTec: declarar) |
| Desgaste | 6.3 | Merola & Affatato 2019 [🟡]; Kurtz 2016 [🟡] |
| Zircónia | 6.3 | Chevalier 2006 [🟡] |
| Propriedades das ligas de Ti | 6.2 | Niinomi 1998 [🟡]; Geetha et al. 2009 [🟡] |
| Método (critérios-alvo) | 6.1 | Petković et al. 2025 [✅]; Jahan et al. 2012 [🟡] |

---

## 4. Perguntas prováveis na reunião (resultado preliminar da haste)

Resultado em results/haste_preliminar.md e results/figures/haste_preliminar.png (η = 1).
PRELIMINAR: dados por verificar.
- Cenário A, TOPSIS: Ti-6Al-4V ELI 0,744; Ti-13Nb-13Zr 0,652; Co-Cr-Mo 0,611; Ti cp grau 4 0,517; 316L 0,251.
- Posições A (TOPSIS / WASPAS / VIKOR): Ti-6Al-4V 1/1/1; Ti-13Nb-13Zr 2/2/2; Co-Cr 3/4/3; Ti cp 4/3/4; 316L 5/5/5.
- Spearman entre métodos: cenário A 0,90 a 1,00; cenário B 0,83 a 1,00 (o WASPAS é o que discorda).

### P1. Porque é que o Co-Cr fica em 3.º apesar de ser muito mais rígido do que o osso?
Dados de apoio:
- E do Co-Cr: 225 GPa, cerca de 13 vezes o alvo (17 GPa); é o pior no critério de módulo (r = 0).
- Todos os candidatos estão acima do alvo: a normalização (eq. 2) usa o intervalo 17 a 225 GPa, por isso a escala fica comprimida. O Ti-6Al-4V (112 GPa, cerca de 6,6 vezes o alvo) recebe só r = 0,54.
- O Co-Cr é o melhor em fadiga (750 MPa; r = 1), que tem o maior peso (0,25), e quase o melhor em cedência (r = 0,95).
- Contribuição do módulo para a distância à solução ideal (D+²) do Co-Cr: 0,019; a do 316L na fadiga: 0,063.
- Sensibilidade (EXPLORATÓRIO: cálculo de 27 set, não versionado; os números definitivos geram-se num script na tarefa 9):
  - peso do módulo 0,40 em vez de 0,20: Co-Cr desce para 4.º (0,488; Ti cp grau 4 sobe para 0,579);
  - sem o critério de módulo: Co-Cr sobe para 2.º (0,706);
  - módulo como custo em vez de alvo: Co-Cr mantém-se em 3.º (0,552), quase empatado com Ti cp grau 4 (0,544).
- Leitura para a resposta: a posição do Co-Cr depende do peso dado ao stress shielding face à fadiga; é isso que o cenário W (pesos) e o T-haste (alvo) vão testar.
- Fonte clínica para o stress shielding: docs/TP2_fisiopatologia_da_falha.md 1.4.8; Huiskes et al. 1992 [🟡].

### P2. Porque ganha o Ti-6Al-4V ELI e não o Ti-13Nb-13Zr, que é mais próximo do osso?
Dados de apoio:
- Ti-13Nb-13Zr é melhor no módulo (81,5 vs 112 GPa; r = 0,69 vs 0,54) e na cedência (872 vs 835 MPa).
- Perde nos ordinais: custo relativo 4 vs 3 (r = 0 vs 0,33) e fabricabilidade 3 vs 5 (r = 0 vs 1); estes dois critérios pesam 0,15 no total.
- Fadiga semelhante (550 vs 575 MPa).
- No cenário B a diferença encurta (0,734 vs 0,687).
- Estatuto na base: Ti-13Nb-13Zr "Clínico (uso limitado)".

### P3. De onde vêm os pesos e o alvo de 17 GPa?
Dados de apoio:
- Pesos subjetivos definidos pelo André, com justificação por critério em data/criterios.csv (coluna "justificacao"); ainda sem o η (weights.py, tarefa 5).
- Ordinais pesam 0,40 do total (regra da base: ≤ 0,50).
- Alvo de 17 GPa: justificação "aproximar do osso cortical" (data/criterios.csv); a base não tem fonte para os 17 GPa: fica "A verificar".
- Petković et al. 2025 usam 14 GPa como alvo do módulo na haste (Tabela A3, C5; confirmado no PDF).
- Registado em docs/NOTAS_METODOLOGICAS.md (valores a verificar; cenário T-haste passa a comparar 14 vs 17 GPa).

### P4. Estes números são fiáveis?
Dados de apoio:
- 54 de 54 valores da haste estão "A verificar"; fontes de partida: Niinomi 1998 e Geetha et al. 2009 (guia 6.2, ambos 🟡).
- Alguns intervalos são largos: cedência do 316L 190-690 MPa; fadiga do Co-Cr 600-900 MPa. O ranking usa o ponto médio.
- O Monte Carlo (tarefa 9, 10 000 iterações entre mín. e máx.) mostra se o 1.º lugar se mantém dentro destes intervalos.

### P5. Como sabes que o código está certo?
Dados de apoio:
- Reprodução do caso 2 de Petković et al. 2025: 15 de 15 C_i (diferença máxima 5e-6) e 15 de 15 posições (tests/test_reproduce_petkovic.py).
- Encontrada uma incoerência no artigo: Tabela A3 M1-C9 = 0,41; Figura A6 (software) = 0,59; os resultados publicados usam 0,59 (docs/NOTAS_METODOLOGICAS.md). Email ao autor por enviar.

### P6. Porque é que o WASPAS põe o Co-Cr abaixo do Ti cp grau 4 (4.º no cenário A, 5.º no B)?
Dados de apoio (cálculo de 28 set com waspas.normalize_waspas, cenário A; EXPLORATÓRIO):
- Normalização diferente (eqs. 9-13 vs eq. 2 do TOPSIS): nos critérios de benefício o WASPAS usa x/máx, o TOPSIS usa o intervalo. Fadiga do Ti cp grau 4: r = 0,51 no WASPAS (385/750) vs 0,22 no TOPSIS; a vantagem do Co-Cr na fadiga pesa menos.
- Módulo (alvo abaixo de todos, eq. 11): r_E do Co-Cr = 0,076 (Ti cp: 0,602).
- A parte de produto (WPM, eq. 15) castiga valores baixos: r_E^0,20 = 0,60 no Co-Cr vs 0,90 no Ti cp; WPM Co-Cr 0,501 vs Ti cp 0,685 (soma pesada, WSM: 0,681 vs 0,712).
- Leitura para a resposta: a concordância entre métodos (cenário M) é parte da análise de robustez; o 1.º e o 2.º lugar não mudam com o método.
