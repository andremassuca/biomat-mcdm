# Caso 3: Stent vascular coronário

## Problema crítico e resposta

**Problema indicado pelo docente: resistência mecânica e biocompatibilidade.**

A resistência mecânica corresponde, na análise, ao índice de recuo elástico (σy/E), ao alongamento na rotura, à resistência à tração e ao módulo de Young. A biocompatibilidade corresponde sobretudo à espessura dos struts, o critério de maior peso, porque struts mais finos estão associados a menos reestenose e trombose. Em conjunto, estes critérios somam cerca de 65 % do peso.

O platina-crómio ficou em 1.º lugar com o TOPSIS e o VIKOR, e o cobalto-crómio L605 com o WASPAS, e este resultado mantém-se quando o peso dos critérios ligados ao problema é duplicado. O Pt-Cr é o mais robusto à incerteza dos dados (1.º em 57 a 70 % das iterações do Monte Carlo). O teor de níquel, relevante para a biocompatibilidade em doentes alérgicos, é discutido na questão 3.

## Candidatos e critérios

<!-- incluir: tabelas/stent_criterios.md -->

## Resultados

<!-- incluir: tabelas/stent_resultados.md -->

## Robustez

<!-- incluir: tabelas/stent_robustez.md -->

<!-- figura: fig_b_posicoes -->
<!-- figura: fig_c_monte_carlo -->
<!-- figura: fig_d_vencedor_eta -->

## Resposta às questões do enunciado

### 1. Função do dispositivo

O stent coronário é uma malha metálica tubular implantada por cateter numa artéria coronária estreitada por aterosclerose. Depois da angioplastia com balão, o stent é expandido contra a parede da artéria e funciona como andaime: mantém o lúmen aberto, impede o recuo elástico da parede e fixa as dissecções provocadas pela dilatação. Nos stents atuais, a malha serve também de suporte a um revestimento que liberta um fármaco antiproliferativo (stents com eluição de fármaco), para reduzir a reestenose.

Este trabalho considera apenas stents expansíveis por balão. Os stents autoexpansíveis (Nitinol) pertencem a outra classe de dispositivo, com outra mecânica de implantação, e ficaram fora da comparação.

### 2. Propriedades mecânicas necessárias

O stent passa por dois regimes mecânicos muito diferentes:
- **Na implantação**, o metal tem de se deformar plasticamente sem fissurar: o stent é dilatado várias vezes o seu diâmetro inicial. Isto exige ductilidade elevada (alongamento na rotura).
- **Depois de expandido**, tem de manter o diâmetro contra a pressão da parede arterial (resistência radial) e recuar o mínimo possível. O recuo elástico é tanto menor quanto menor for a razão entre a tensão de cedência e o módulo de Young (σy/E): o metal deve "ceder" com facilidade durante a expansão e ser rígido depois. No trabalho, σy/E foi usado como indicador ao nível do material; o recuo real depende também do desenho do stent.

Ao longo da vida do doente, o stent sofre uma carga pulsátil a cada batimento cardíaco, cerca de 38 milhões de ciclos por ano a 72 batimentos por minuto; os ensaios de durabilidade simulam 10 anos (ASTM F2477; FDA 2010), pelo que a resistência à fadiga é essencial.

Um módulo de Young e uma resistência à tração elevados permitem struts (as hastes da malha) mais finos sem perder resistência radial. Isto é importante clinicamente: struts mais finos estão associados a menos reestenose: no ISAR-STEREO, 15,0 % com 50 µm contra 25,8 % com 140 µm (Kastrati et al. 2001). Por isso, a espessura de strut foi o critério com maior peso. A espessura é uma propriedade do dispositivo, não só do material: a diferença entre o MP35N (Resolute, cerca de 90 µm) e o L605 (XIENCE, 81 µm) reflete também o desenho de cada stent.

### 3. Propriedades químicas e físicas relevantes

- **Resistência à corrosão no sangue.** Tal como nas próteses ortopédicas, depende do filme passivo de óxido (Cr2O3 nas ligas de aço, cobalto-crómio e platina-crómio).
- **Teor de níquel.** Todas as ligas permanentes candidatas contêm níquel: cerca de 13-15 % no 316L, 9-11 % no L605, 33-37 % no MP35N e 9 % no Pt-Cr. É relevante em doentes com alergia ao níquel, embora a importância clínica desta alergia em stents seja debatida: há estudos que a associam a reestenose (Köster et al. 2000; Gong et al. 2013) e outros que não encontram relação (Norgaz et al. 2005).
- **Radiopacidade.** O cardiologista tem de ver o stent em fluoroscopia para o posicionar. A radiopacidade depende do teor de elementos de número atómico elevado e da espessura: a platina (Z = 78) e o tungsténio do L605 (Z = 74) tornam estas ligas mais visíveis do que o 316L, mesmo com struts finos (Allocco et al. 2010).
- **Compatibilidade com ressonância magnética**, para o seguimento por angio-RM.
- **Compatibilidade com o revestimento e com a esterilização.** O polímero e o fármaco não suportam calor; os stents com eluição de fármaco são esterilizados por óxido de etileno.

### 4. Biocompatibilidade

O stent está em contacto direto e permanente com o sangue, por isso além dos ensaios gerais da série ISO 10993 interessa sobretudo a interação com o sangue (ISO 10993-4): trombogenicidade, adesão de plaquetas e ativação da coagulação. A superfície deve ser rapidamente coberta por endotélio, que é a defesa natural contra a trombose.

Nas ligas candidatas, a biocompatibilidade está bem estabelecida pelo uso clínico (316L, L605, MP35N e Pt-Cr). Nos bioabsorvíveis, interessa também a biocompatibilidade dos produtos de degradação: iões de magnésio no WE43 e ácido láctico no PLLA, ambos metabolizados pelo organismo.

### 5. Bioinerte, bioativo ou biodegradável

Há duas filosofias:
- **Stent permanente bioinerte** (316L, L605, MP35N, Pt-Cr): fica para sempre na artéria. O revestimento com fármaco é farmacologicamente ativo, mas o metal é inerte.
- **Stent bioabsorvível** (liga de magnésio WE43, PLLA): suporta a artéria durante a cicatrização (cerca de 3 a 6 meses) e depois desaparece, devolvendo à artéria a capacidade de se dilatar e evitando um corpo estranho permanente.

A ideia dos bioabsorvíveis é atraente, mas o primeiro dispositivo de grande difusão, o Absorb (PLLA), com struts de cerca de 157 µm, deixou de ser comercializado em setembro de 2017, depois de dados de maior trombose do scaffold do que com o stent metálico (2,3 % contra 0,7 % aos 3 anos no ABSORB III; Kereiakes et al. 2017), que vários autores associam em parte à espessura dos struts (Ke et al. 2020). O Magmaris (magnésio) continua em uso clínico.

### 6. Riscos de corrosão, desgaste ou degradação

- **Reestenose intra-stent:** novo estreitamento por proliferação de tecido dentro do stent (questão 7). Foi o principal problema dos stents metálicos sem fármaco.
- **Trombose do stent:** formação de coágulo sobre o stent, rara mas grave (enfarte). O risco é maior enquanto a superfície não está coberta por endotélio, e com struts espessos.
- **Corrosão e libertação de iões:** o 316L é suscetível a corrosão localizada (picadas), com libertação de níquel.
- **Fratura de struts por fadiga:** pode levar a perda de suporte e reestenose localizada.
- **Recuo elástico:** perda de diâmetro logo após a expansão.
- **Nos bioabsorvíveis:** uma degradação demasiado rápida perde o suporte antes de a artéria cicatrizar; demasiado lenta anula a vantagem. No magnésio, a corrosão liberta hidrogénio.

### 7. Resposta do organismo

A expansão do stent lesa o endotélio e a parede da artéria. Seguem-se a adesão e ativação de plaquetas na superfície exposta e uma resposta inflamatória. Os fatores de crescimento libertados estimulam a migração e a proliferação de células musculares lisas da parede, que produzem matriz extracelular: é a hiperplasia neointimal. Em quantidade moderada, cobre o stent e estabiliza-o; em excesso, estreita de novo a artéria (reestenose).

Os stents com eluição de fármaco libertam um antiproliferativo (por exemplo, everolimus) que trava esta proliferação. O custo é um atraso na reendotelização, que obriga a terapêutica antiplaquetária dupla durante meses para prevenir a trombose. Struts mais finos e polímeros mais biocompatíveis aceleram a cobertura endotelial.

### 8. Vantagem face aos materiais atuais

O dispositivo a substituir é o stent de aço 316L, de primeira geração. Os seus problemas são os struts espessos (cerca de 130-140 µm nas plataformas de primeira geração; Nikam et al. 2014), a menor radiopacidade e o teor de níquel. Na análise multicritério (TOPSIS, WASPAS e VIKOR), o 316L ficou em último lugar entre os metais permanentes nos dois cenários.

As duas ligas de nova geração, **cobalto-crómio L605** e **platina-crómio**, ficaram praticamente empatadas:
- No cenário A (só materiais em uso clínico), o Pt-Cr fica em 1.º lugar com o TOPSIS e o VIKOR, e o L605 com o WASPAS; a diferença é pequena (ΔC = 0,024).
- No cenário B (inclui bioabsorvíveis), o L605 fica em 1.º com os três métodos, empatado com o Pt-Cr (ΔC = 0,002, abaixo do limiar de empate).
- Na análise de Monte Carlo, o Pt-Cr fica em 1.º lugar em 57 a 70 % das iterações, contra 27 a 42 % do L605 e menos de 10 % do MP35N.

Propõe-se assim o **Pt-Cr** como escolha de referência: é o mais robusto à incerteza dos dados e o mais radiopaco, o que permite struts finos bem visíveis em fluoroscopia. O **L605** é uma alternativa praticamente equivalente. Uma ressalva: o módulo, a resistência à tração e o alongamento do Pt-Cr ainda só foram confirmados em fontes secundárias, por isso o 1.º lugar deve ser confirmado com a fonte primária (O'Brien et al. 2010).

Face ao 316L, ambas permitem struts de cerca de 74-81 µm com resistência radial suficiente, são mais radiopacas e têm menos níquel. O MP35N fica em 3.º: tem o maior teor de níquel (33-37 %) e, nos dispositivos atuais, struts ligeiramente mais espessos.

No WASPAS, o 316L volta a ganhar quando o custo tem peso elevado ou quando os pesos são tirados sobretudo dos dados (η até 0,2); o TOPSIS e o VIKOR mantêm o L605 nesses casos. Na haste observou-se algo semelhante, mas no TOPSIS: quando o custo domina, o aço torna-se competitivo com alguns métodos.

Os bioabsorvíveis ficaram atrás dos metais permanentes no cenário B (Mg WE43 em 5.º, PLLA em 6.º). Entre os dois, o magnésio é claramente superior: struts mais finos, maior resistência e reabsorção mais rápida.

### 9. Fabrico

- **Ligas permanentes:** tubo sem costura de pequeno diâmetro, obtido por trefilagem; corte a laser do padrão da malha; remoção da escória e decapagem; recozimento para recuperar a ductilidade; eletropolimento para alisar a superfície e melhorar a passivação.
- **Revestimento com fármaco:** polímero com o fármaco aplicado por pulverização sobre os struts.
- **Montagem e esterilização:** compressão do stent sobre o balão (crimping); esterilização por óxido de etileno.
- **Magnésio:** minitubo sem costura cortado a laser e eletropolido (Moravej e Mantovani 2011); no Magmaris, a liga é revestida com 7 µm de PLLA que liberta sirolimus (Rapetto e Leoncini 2017).

### 10. Testes antes da utilização clínica

- **Biocompatibilidade:** série ISO 10993, em particular a ISO 10993-4 (interação com o sangue).
- **Ensaios específicos de stents:** ISO 25539-2:2020 (implantes cardiovasculares, dispositivos endovasculares, parte 2: stents vasculares).
- **Durabilidade à fadiga pulsátil:** ASTM F2477-24; a duração equivalente a 10 anos é recomendação do guia da FDA (2010), e as edições até à F2477-19 indicavam pelo menos 380 milhões de ciclos.
- **Recuo elástico e resistência radial:** ASTM F2079-09(2022) (recuo elástico) e ASTM F3067-26 (guia de ensaio da resistência radial).
- **Corrosão:** polarização potenciodinâmica (ASTM F2129).
- **Ressonância magnética:** ASTM F2052, F2213, F2182 e F2119.
- **Esterilização:** validação por óxido de etileno (ISO 11135).
- **Clínica:** ensaios em animal e ensaios clínicos aleatorizados com seguimento de reestenose e trombose.

### 11. Propriedades que caracterizam cada material face à aplicação

**Ligas permanentes (L605, Pt-Cr):**
- Ensaio de tração em tubo recozido: tensão de cedência, módulo de Young, resistência à tração e alongamento (e daí σy/E).
- Microscopia eletrónica (SEM) dos struts antes e depois da expansão, para detetar fissuras.
- Espessura e rugosidade dos struts (perfilometria).
- XPS, para a composição do filme passivo.
- Polarização e espectrometria (ICP-MS) para medir a libertação de níquel e outros iões.
- Radiopacidade em fluoroscopia.
- Ângulo de contacto, para a superfície que recebe o revestimento.

**Bioabsorvíveis:**
- Magnésio: taxa de corrosão in vitro (perda de massa e libertação de hidrogénio).
- PLLA: peso molecular por cromatografia (GPC), cristalinidade por DSC e degradação in vitro ao longo do tempo.
