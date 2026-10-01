# 5.1 Prótese da anca

*Rascunho de trabalho. Os valores numéricos vêm da base de dados do projeto (data/materiais.csv) e estão todos "a verificar"; as referências marcadas [confirmar] ainda não foram lidas na fonte.*

A prótese total da anca tem dois componentes com requisitos muito diferentes: a **haste femoral**, que transmite a carga ao fémur e tem de resistir à fadiga durante décadas, e o **par articular** (cabeça femoral e componente acetabular), que tem de deslizar com o mínimo de desgaste. Por isso as questões são respondidas separadamente para cada um sempre que faz sentido. A haste é comparada de forma quantitativa; o par articular, de forma semiquantitativa, porque a decisão depende sobretudo de critérios de segurança e porque os dados de desgaste publicados vêm de tipos de evidência diferentes (in vivo e simulador) que não se devem misturar.

## Fisiopatologia da falha (resumo)

A principal causa de falha tardia ligada ao material é o **descolamento asséptico por osteólise**. O deslizamento da cabeça contra o acetábulo liberta partículas de desgaste; no polietileno convencional, uma fração importante é submicrométrica, a gama mais facilmente fagocitada (Green et al., 1998 [confirmar]). Os macrófagos fagocitam as partículas e ativam o NF-κB, com libertação de TNF-α, IL-1β, IL-6 e PGE2. Estas citocinas aumentam o RANKL e diminuem a osteoprotegerina, o que ativa os osteoclastos e reabsorve o osso à volta do implante. A fixação perde-se, surge micromovimento e gera-se ainda mais desgaste (Goodman & Gallo, 2019 [confirmar]).

Há três vias paralelas. Nos pares **metal-metal**, os iões de Co e Cr podem desencadear uma hipersensibilidade tardia com necrose e pseudotumores (reação adversa local, ALTR) (Hallab & Jacobs, 2009 [confirmar]). Na **junção cabeça-cone** de próteses modulares, o micromovimento rompe a camada passiva e instala-se corrosão em fenda, mesmo sem par metal-metal (Cooper et al., 2012 [confirmar]). Por último, uma haste muito mais rígida do que o osso provoca **stress shielding**: o fémur proximal fica subcarregado e perde massa óssea (Huiskes et al., 1992 [confirmar]).

Nem todas as revisões se devem ao material: luxação, infeção, fratura periprotésica e erro técnico também pesam, em proporções que variam entre registos [confirmar: relatório anual do NJR ou do AOANJRR, com edição e ano]. A fisiopatologia completa está no Anexo A.

| Mecanismo | Propriedade que o desencadeia | Critério no modelo | Técnica de caracterização |
|---|---|---|---|
| Osteólise por partículas | Taxa de desgaste, oxidação do PE | Taxa de desgaste (peso mais alto no par articular) | Simulador ISO 14242; FTIR; SEM das partículas |
| Hipersensibilidade a iões | Libertação de Co/Cr | Segurança iónica (critério estrito) | Imersão + ICP-MS; XPS da camada passiva |
| Corrosão cabeça-cone | Par metálico na junção | Compatibilidade galvânica | Fretting-corrosão (ASTM F1875); SEM/EDS |
| Stress shielding | Módulo de elasticidade | Módulo com alvo no osso; razão E_implante/E_osso | Ensaio de tração (módulo) |

## 1. Função do dispositivo

A prótese substitui a articulação coxofemoral quando a cartilagem está destruída, sobretudo por coxartrose, e tem de devolver ao doente uma marcha sem dor. A **haste** é introduzida no canal medular do fémur e transfere para o osso as cargas do peso do corpo e da marcha, fixada com cimento ósseo ou por crescimento ósseo na superfície (não cimentada). A **cabeça femoral**, montada no cone da haste, articula com o **componente acetabular**, fixado na bacia, e o par tem de permitir o movimento com baixo atrito e desgaste mínimo durante 15 a 20 anos ou mais.

## 2. Propriedades mecânicas necessárias

**Haste.** A propriedade decisiva é a **resistência à fadiga**: a haste é solicitada em cada passo, na ordem de 1 a 2 milhões de ciclos por ano, e por isso o critério usado é o limite de fadiga a 10⁷ ciclos [confirmar fonte do número de ciclos]. Precisa também de **tensão de cedência** elevada, para não deformar plasticamente, e de um **módulo de elasticidade** tão próximo do osso quanto possível, para reduzir o stress shielding. Estes dois últimos requisitos estão em conflito: os metais mais resistentes (Co-Cr-Mo, 210 a 240 GPa) são também os mais rígidos, e mesmo o Ti-6Al-4V (110 a 114 GPa) está muito acima do osso cortical, cerca de 17 GPa (valores a verificar). Por isso o módulo é tratado no modelo como critério-alvo e não como "menor é melhor".

**Par articular.** Importam a **resistência ao desgaste**, a **dureza** da cabeça (resistência a riscos por partículas de terceiro corpo) e, nos cerâmicos, a **tenacidade à fratura**, porque a falha de uma cabeça cerâmica é súbita. No polietileno interessam também a resistência à fluência e à fadiga.

## 3. Propriedades químicas e físicas relevantes

- **Camada passiva de óxido** (TiO₂ no titânio, Cr₂O₃ no Co-Cr e no aço): é ela que garante a resistência à corrosão e a baixa libertação de iões, e a sua estabilidade sob fretting decide o comportamento na junção cabeça-cone.
- **Composição química**: presença de Ni (aço 316L), Co e Cr, Al e V (Ti-6Al-4V), porque são os elementos que podem ser libertados.
- **Estado de oxidação e grau de reticulação do polietileno**: a reticulação reduz o desgaste, mas a irradiação cria radicais livres que, se não forem estabilizados, levam à oxidação e à perda de propriedades ao longo do tempo (Kurtz, 2016 [confirmar]).
- **Densidade**: critério secundário (o titânio tem cerca de metade da densidade do Co-Cr).
- **Rugosidade e molhabilidade da superfície**: rugosidade alta na superfície da haste não cimentada (favorece a fixação óssea) e o mais baixa possível na cabeça (reduz o desgaste).
- **Compatibilidade com ressonância magnética**: os doentes com prótese da anca são frequentemente idosos e fazem RM; o titânio causa menos artefacto do que o Co-Cr e o aço.

## 4. Biocompatibilidade

Todos os candidatos têm de cumprir a avaliação biológica no quadro da gestão de risco (ISO 10993-1 [confirmar versão]). As ligas de titânio têm a melhor tolerância tecidual entre os metais usados em hastes, graças ao óxido estável. No Ti-6Al-4V há alguma preocupação com a libertação de Al e V a longo prazo, o que motivou ligas sem estes elementos, como o Ti-13Nb-13Zr (Geetha et al., 2009 [confirmar]). O aço 316L contém níquel, um alergénio frequente, e o Co-Cr liberta iões de Co e Cr. No par articular, a biocompatibilidade depende sobretudo dos **produtos de desgaste**: partículas de polietileno (osteólise), iões e nanopartículas metálicas (ALTR) ou partículas cerâmicas, que são biologicamente pouco ativas mas podem surgir em caso de fratura. A cerâmica ZTA é quase inerte, correspondendo ao Tipo 1 da classificação de biocerâmicos do slide 32 da Aula 2.

## 5. Bioinerte, bioativo ou biodegradável

Ambos os componentes são **bioinertes** (ou, mais rigorosamente, biotolerados): têm de permanecer estáveis durante décadas, e nenhum material biodegradável tem resistência à fadiga suficiente para uma haste. A fixação não cimentada pode, no entanto, usar uma **superfície bioativa**: revestimentos de hidroxiapatite ou superfícies porosas de titânio promovem o crescimento ósseo na interface [confirmar referência]. A bioatividade é assim uma propriedade da superfície, não do material do corpo da haste.

## 6. Risco de corrosão, desgaste ou degradação

- **Haste**: risco de corrosão baixo nas ligas de titânio, mas não nulo na **junção cabeça-cone**, onde o fretting rompe a camada passiva; o risco é maior quando se combina uma cabeça de Co-Cr com um cone de titânio (dois metais diferentes). Fratura por fadiga é rara, mas possível em hastes de pequeno diâmetro ou com mau apoio proximal.
- **Par articular**: o **desgaste do polietileno** é o risco principal; o polietileno convencional esterilizado por radiação gama ao ar oxida e desgasta mais depressa (caso histórico do Hylamer [confirmar]). O polietileno altamente reticulado reduz muito o desgaste, e a estabilização com vitamina E limita a oxidação [confirmar]. Nas cabeças cerâmicas, o risco é a **fratura**, baixo com as cerâmicas atuais mas não nulo (caso Prozyr, Masonis et al., 2004 [confirmar]), e nos pares cerâmica-cerâmica pode surgir ruído (squeaking). O par metal-metal tem desgaste volumétrico baixo, mas liberta iões, o que o elimina na triagem.

## 7. Resposta do organismo

A resposta inicial é a reação a corpo estranho comum a qualquer implante (adsorção de proteínas, inflamação aguda e crónica, células gigantes e cápsula fibrosa) (Anderson et al., 2008 [confirmar]). A longo prazo, o que decide o desfecho é a resposta às **partículas de desgaste** (cascata macrófago, citocinas, RANKL/OPG, osteólise), aos **iões metálicos** (hipersensibilidade tipo IV com ALVAL e pseudotumores) e à **distribuição de carga** (remodelação óssea adaptativa e stress shielding), descritas na fisiopatologia acima. Uma boa escolha de material atua sobre as três: menos partículas, sem par metal-metal e rigidez mais próxima do osso.

## 8. Vantagem face aos materiais atuais

Admitindo que o dispositivo atual do hospital usa uma haste de aço ou Co-Cr com cabeça metálica sobre polietileno convencional, ou um par metal-metal, a proposta traz três vantagens:

1. **Haste de Ti-6Al-4V ELI**: módulo cerca de metade do Co-Cr (menos stress shielding), boa resistência à fadiga, sem níquel nem cobalto e melhor compatibilidade com RM. No resultado preliminar do TOPSIS fica em 1.º lugar nos cenários A e B, à frente do Ti-13Nb-13Zr e do Co-Cr-Mo (secção 6; dados a verificar).
2. **Cabeça em ZTA**: elimina o par metálico na junção cabeça-cone e a libertação de iões pela cabeça, é mais dura e resistente a riscos e, sendo um compósito de alumina com zircónia, tem maior tenacidade do que a alumina simples [confirmar].
3. **Acetábulo em HXLPE com vitamina E**: desgaste muito inferior ao polietileno convencional e melhor resistência à oxidação, o que atua diretamente sobre a causa da osteólise.

Um estudo de registo com mais de um milhão de próteses do NJR comparou o risco de revisão entre superfícies de apoio (Whitehouse et al., 2024). O estudo foi financiado pela CeramTec, fabricante de componentes cerâmicos, o que deve ser tido em conta ao interpretar os resultados a favor dos pares cerâmicos [confirmar o resultado principal antes de o citar].

## 9. Fabrico

- **Haste**: as ligas de titânio e de Co-Cr são forjadas e maquinadas; a superfície de fixação não cimentada pode ser jateada, receber revestimento poroso ou de hidroxiapatite, ou ser produzida por fabrico aditivo com estrutura porosa integrada. As designações F136, F67, F799 e F75 dos slides da Aula 2 são normas ASTM (Ti-6Al-4V ELI, Ti cp, Co-Cr-Mo forjado e Co-Cr-Mo fundido, respetivamente) [confirmar títulos].
- **Cabeça ZTA**: processamento de pós (mistura de alumina e zircónia), conformação, sinterização e prensagem isostática a quente, seguidos de retificação e polimento de precisão; cada cabeça é normalmente submetida a ensaio de prova [confirmar] (ISO 6474-2 [confirmar versão]).
- **Acetábulo HXLPE**: o UHMWPE é reticulado por irradiação (gama ou feixe de eletrões); os radicais livres são depois tratados por refusão ou recozimento, ou estabilizados com vitamina E; a esterilização final deve evitar a presença de ar [confirmar] (Kurtz, 2016 [confirmar]).

## 10. Testes antes da utilização clínica

- **Avaliação biológica**: ISO 10993-1, com os ensaios aplicáveis (citotoxicidade, sensibilização, efeitos locais após implantação, ISO 10993-6) [confirmar versões].
- **Haste**: resistência e fadiga do componente femoral segundo a ISO 7206 (várias partes) [confirmar partes e versões].
- **Par articular**: desgaste em simulador de anca segundo a ISO 14242 [confirmar versão]; ensaios de resistência da cabeça cerâmica (rotura estática e fadiga) [confirmar norma].
- **Junção cabeça-cone**: fretting-corrosão segundo a ASTM F1875 [confirmar versão].
- **Materiais**: conformidade com as normas de material (ASTM F136, F67, F799/F1537; ISO 6474-2) [confirmar versões].
- Depois dos ensaios pré-clínicos, avaliação clínica e **vigilância pós-comercialização**, incluindo registos nacionais; o caso da prótese ASR mostra que alguns problemas só são detetados nesta fase [confirmar].

## 11. Propriedades que caracterizam cada material face à aplicação

| Material | Propriedades que o caracterizam para esta aplicação |
|---|---|
| Aço inox 316L | Barato e fácil de fabricar; módulo cerca de 190 a 200 GPa; fadiga inferior às outras ligas; contém níquel; artefacto marcado em RM. Fica em último lugar no resultado preliminar. |
| Co-Cr-Mo forjado | Resistência à fadiga e à cedência mais altas; o mais rígido (210 a 240 GPa); liberta Co e Cr; muito resistente ao desgaste, por isso usado em cabeças. |
| Ti-6Al-4V ELI | Boa fadiga e cedência com metade da rigidez do Co-Cr; óxido passivo estável; baixa densidade; boa compatibilidade com RM; resistência ao desgaste fraca, por isso não é usado como superfície articular. |
| Ti cp grau 4 | Excelente biocompatibilidade, mas resistência limitada para hastes muito solicitadas. |
| Ti-13Nb-13Zr | Módulo mais baixo (cerca de 80 GPa), sem Al nem V; uso clínico limitado e custo mais alto. |
| Ti-35Nb-7Zr-5Ta (TNZT) | Módulo mais próximo do osso (cerca de 55 a 66 GPa), mas ainda em investigação; só entra no cenário B. |
| ZTA (cabeça) | Muito dura e resistente ao desgaste e a riscos; quase inerte; sem iões metálicos; risco de fratura baixo mas não nulo. |
| HXLPE com vitamina E (acetábulo) | Desgaste muito menor do que o UHMWPE convencional; resistência à oxidação melhorada pela vitamina E. |

*Valores de módulo a verificar nas fontes primárias (Niinomi, 1998; Geetha et al., 2009; normas ASTM) [confirmar].*

## Caracterização dos materiais propostos

| Técnica | Propriedade | Porquê nesta aplicação | Norma |
|---|---|---|---|
| Ensaio de tração | Módulo, cedência, resistência à tração, alongamento | Stress shielding e deformação plástica da haste | ISO 6892-1 [confirmar] |
| Ensaio de fadiga do componente | Resistência à fadiga da haste | Carga cíclica durante décadas | ISO 7206 [confirmar partes] |
| Dureza Vickers | Dureza da cabeça e da haste | Resistência a riscos por terceiro corpo | ISO 6507-1 [confirmar] |
| Densidade (Arquimedes) | Densidade; porosidade residual da cerâmica | Qualidade da sinterização da ZTA | [confirmar] |
| Simulador de anca | Taxa de desgaste do par | Causa principal da osteólise | ISO 14242 [confirmar versão] |
| FTIR | Índice de oxidação do polietileno | Oxidação aumenta o desgaste | ASTM F2102 [confirmar] |
| DSC | Cristalinidade e comportamento térmico do PE | Efeito da reticulação e do tratamento térmico | [confirmar] |
| XRD | Fases cristalinas da ZTA (fração monoclínica) | Envelhecimento hidrotérmico da zircónia | ISO 6474-2 [confirmar] |
| SEM/EDS | Morfologia e composição de partículas e superfícies | Tamanho das partículas de desgaste; corrosão na junção | [confirmar] |
| XPS | Química da camada passiva | Estabilidade do óxido e libertação de iões | [confirmar] |
| Ângulo de contacto | Molhabilidade da superfície | Adsorção de proteínas e fixação óssea da haste | [confirmar] |
| ICP-MS após imersão | Iões libertados (Co, Cr, Ti, Al, V) | Risco de hipersensibilidade e toxicidade | ISO 10993-15 [confirmar] |
| Ensaio de fretting-corrosão | Corrosão na junção cabeça-cone | Trunnionosis | ASTM F1875 [confirmar versão] |

A lógica da tabela segue o slide 11 da Aula 2: o **volume** do material determina a função mecânica (tração, fadiga, dureza), e a **superfície** controla a interação com as proteínas e as células (XPS, ângulo de contacto, rugosidade).
