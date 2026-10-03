# Caso 4: Scaffold para regeneração óssea

## Problema crítico e resposta

**Problema indicado pelo docente: suporte celular e degradação controlada.**

Os critérios que respondem diretamente ao problema são a porosidade e a bioatividade (suporte celular) e o tempo de degradação (degradação controlada), com 45 % do peso no total. A imprimibilidade e as propriedades mecânicas contribuem de forma indireta.

O resultado depende da leitura do problema. Com a leitura literal (só porosidade, bioatividade e degradação, com o peso duplicado), o β-TCP poroso passa a 1.º com o TOPSIS e o VIKOR: é mais bioativo (nota 4, contra 3 do compósito) e degrada-se em cerca de 12 meses, mais perto do alvo de 9 meses do que o compósito (cerca de 18). Com a leitura ampla, que inclui o suporte mecânico enquanto o osso se forma, o compósito PCL/β-TCP impresso mantém o 1.º lugar. A resposta proposta é, por isso, o compósito para defeitos que suportam carga, e o β-TCP poroso quando a prioridade é só o suporte celular e a reabsorção.

## Candidatos e critérios

<!-- incluir: tabelas/scaffold_criterios.md -->

## Resultados

<!-- incluir: tabelas/scaffold_resultados.md -->

## Robustez

<!-- incluir: tabelas/scaffold_robustez.md -->

<!-- figura: fig_b_posicoes -->
<!-- figura: fig_c_monte_carlo -->
<!-- figura: fig_d_vencedor_eta -->

## Resposta às questões do enunciado

### 1. Função do dispositivo

Um scaffold ósseo preenche um defeito ósseo demasiado grande para cicatrizar sozinho (defeito de tamanho crítico), por exemplo depois de um trauma, da remoção de um tumor ou de uma infeção. Funciona como uma estrutura temporária: dá suporte às células, permite a entrada de vasos sanguíneos e guia a formação de osso novo. Idealmente, degrada-se à medida que o osso novo o substitui, sem deixar material permanente.

### 2. Propriedades mecânicas necessárias

O scaffold deve aproximar-se do osso trabecular que vai substituir:
- resistência à compressão de cerca de 2 a 12 MPa;
- módulo de compressão de cerca de 50 a 500 MPa.

No trabalho, estes intervalos foram usados como critérios-alvo (7 MPa e 250 MPa), testados em cenários de sensibilidade com os extremos do intervalo.

Há um compromisso central: a porosidade é necessária para a regeneração, mas quanto mais poroso, mais fraco. Por isso as propriedades mecânicas só se comparam à porosidade típica de cada material (regra da porosidade). Em defeitos que suportam carga, o scaffold não trabalha sozinho e é protegido por fixação metálica.

### 3. Propriedades químicas e físicas relevantes

- **Porosidade e tamanho de poro:** poros interligados, com porosidade elevada e poros de algumas centenas de micrómetros, permitem a entrada de células e vasos [confirmar: Karageorgiou e Kaplan 2005]. O alvo usado foi 70 %.
- **Velocidade de degradação:** deve acompanhar a formação de osso novo; o alvo usado foi cerca de 9 meses. Um scaffold que se degrada depressa demais perde o suporte antes do tempo; um que dura demasiado ocupa o espaço do osso novo.
- **Produtos de degradação:** os poliésteres (PLLA, PLGA) libertam produtos ácidos; os fosfatos de cálcio libertam iões de cálcio e fosfato, que o organismo usa; o vidro 45S5 liberta iões de silício, cálcio e sódio e eleva o pH local.
- **Molhabilidade da superfície**, que condiciona a adesão das células.
- **Compatibilidade com a esterilização:** os polímeros de baixo ponto de fusão (PCL, cerca de 60 °C) não suportam autoclave, e a radiação degrada parte das cadeias poliméricas.

### 4. Biocompatibilidade

Além dos ensaios gerais da série ISO 10993, interessa a biocompatibilidade dos produtos de degradação, porque o scaffold vai sendo libertado no tecido ao longo de meses. A acidificação local pelos produtos do PLGA, em particular quando se degrada depressa, pode causar reação inflamatória [confirmar fonte]. Os fosfatos de cálcio e os vidros bioativos têm composição próxima da fase mineral do osso.

### 5. Bioinerte, bioativo ou biodegradável

O scaffold ideal é **bioativo e biodegradável**. Segundo a classificação de Hench, há dois níveis de bioatividade:
- **Classe A, osteoprodutiva:** estimula a formação de osso novo (vidro 45S5).
- **Classe B, osteocondutora com ligação ao osso:** serve de guia ao crescimento do osso (hidroxiapatite, β-TCP).

Os polímeros sintéticos (PCL, PLLA, PLGA) são biodegradáveis mas pouco bioativos. Os compósitos polímero-cerâmico combinam as duas características.

### 6. Riscos de corrosão, desgaste ou degradação

- **Fratura frágil** dos scaffolds cerâmicos porosos, que têm resistência baixa e pouca tenacidade.
- **Perda prematura de suporte**, se a degradação for rápida (PLGA, cerca de 1 a 3 meses).
- **Persistência a longo prazo**, se a degradação for lenta: a hidroxiapatite não foi reabsorvida de forma mensurável em 3,5 anos (Hoogendoorn et al. 1984), e o PLLA maciço persiste vários anos.
- **Inflamação** pelos produtos ácidos de degradação dos poliésteres.
- **Má vascularização no centro** de scaffolds grandes ou pouco interligados.
- **Alteração das propriedades pela esterilização:** no PCL/β-TCP, a radiação por feixe de eletrões tornou a degradação mais rápida (Bruyas et al. 2019).

### 7. Resposta do organismo

Depois da implantação forma-se um hematoma e uma resposta inflamatória inicial, que recruta células mesenquimais. Estas migram para o interior dos poros e diferenciam-se em osteoblastos, que depositam osso novo ao longo das superfícies do scaffold (osteocondução). Os materiais osteoprodutivos, como o vidro 45S5, estimulam ainda essa diferenciação. Com o tempo, o osso novo é remodelado; o scaffold é reabsorvido por osteoclastos (fosfatos de cálcio) ou por hidrólise (polímeros), até ser substituído por osso.

### 8. Vantagem face aos materiais atuais

Propõe-se um **scaffold compósito de PCL com β-TCP, fabricado por impressão 3D**. Na análise multicritério ficou em 1.º lugar com os três métodos, nos cenários A e B (ΔC = 0,052 em A e 0,085 em B), e manteve o 1.º lugar em quase todos os cenários de sensibilidade: só perde para o β-TCP quando o alvo da resistência à compressão desce para 2 MPa. O resultado é estável face aos pesos (1.º lugar em 96 a 100 % das iterações com pesos ±20 %), mas sensível à incerteza dos dados: no Monte Carlo das propriedades, o β-TCP fica em 1.º em mais iterações do que o compósito com o TOPSIS (52 % contra 39 %), embora não com o WASPAS (25 % contra 68 %) nem com o VIKOR (39 % contra 46 %). O β-TCP é, por isso, uma alternativa competitiva quando a prioridade é a bioatividade e o defeito não exige resistência.

O resultado mudou com a verificação dos dados, e a mudança é instrutiva. Com os valores de partida, tirados de revisões, ganhava o β-TCP poroso. À porosidade relevante (cerca de 65 %), porém, a resistência à compressão do β-TCP é de apenas cerca de 2 MPa (mediana de três estudos), e não os 8 MPa de partida. O β-TCP puro tem bioatividade e degradação adequadas, mas é frágil. O PCL é tenaz e fácil de imprimir, mas pouco bioativo e de degradação lenta. O compósito junta as vantagens dos dois: a fase polimérica dá tenacidade e permite controlar a arquitetura dos poros por impressão, e a fase cerâmica dá bioatividade. Já tem uso clínico limitado (Lodewijks et al. 2025; Lodewijks et al. 2024).

Os outros candidatos ficaram atrás por razões claras:
- o vidro 45S5 tem a melhor bioatividade, mas resistência muito baixa como scaffold poroso (cerca de 1 MPa);
- a hidroxiapatite praticamente não se reabsorve;
- o PLGA degrada-se depressa demais;
- o quitosano/HA tem resistência e módulo cerca de duas ordens de grandeza abaixo do osso trabecular.

Uma limitação: o tempo de degradação do compósito continua "A verificar", porque as fontes divergem e nenhuma mede a reabsorção completa.

### 9. Fabrico

- **Compósito PCL/β-TCP:** mistura de PCL fundido com partículas de β-TCP (tipicamente 20 % em massa; Lodewijks et al. 2025), extrudida camada a camada por impressão 3D (deposição de material fundido), com uma arquitetura de filamentos cruzados que define poros interligados (por exemplo, filamentos de 300 µm separados por 1200 µm, com 70 % de porosidade; Sparks et al. 2023). Pode seguir-se um tratamento de superfície para aumentar a molhabilidade, por exemplo com hidróxido de sódio (Kawai et al. 2018).
- **Esterilização:** óxido de etileno ou radiação, sabendo que a radiação por feixe de eletrões acelera a degradação em cerca de 25 % (Bruyas et al. 2019).
- **Outros processos usados nos candidatos:** sinterização de espumas cerâmicas (β-TCP, HA); lixiviação de sal, separação de fases ou liofilização (polímeros e quitosano/HA).

### 10. Testes antes da utilização clínica

- **Biocompatibilidade:** série ISO 10993, incluindo a identificação dos produtos de degradação de polímeros e de cerâmicos [confirmar partes e edições].
- **Caracterização do scaffold:** guias ASTM para scaffolds de engenharia de tecidos e para medição da porosidade [confirmar normas: ASTM F2150, ASTM F2450].
- **Degradação in vitro:** ensaio de degradação de polímeros absorvíveis [confirmar norma: ISO 13781].
- **Ensaios mecânicos:** compressão à porosidade de projeto.
- **Ensaios in vivo:** modelos animais de defeito ósseo de tamanho crítico [confirmar exemplo].
- **Clínica:** ensaios clínicos com seguimento radiológico da formação de osso.

### 11. Propriedades que caracterizam cada material face à aplicação

- **Microtomografia (micro-CT):** porosidade, tamanho e interligação dos poros.
- **Microscopia eletrónica (SEM):** morfologia dos poros e distribuição das partículas cerâmicas.
- **Ensaio de compressão:** resistência e módulo à porosidade de projeto.
- **GPC e DSC:** peso molecular e cristalinidade da fase polimérica.
- **Difração de raios X e FTIR:** fases cristalinas do β-TCP e composição.
- **Termogravimetria (TGA):** teor real de cerâmica no compósito.
- **Ângulo de contacto:** molhabilidade.
- **Degradação in vitro:** perda de massa, peso molecular e pH ao longo do tempo.
- **Ensaio em fluido corporal simulado:** formação de apatite (bioatividade).
- **Cultura de células:** adesão, proliferação e atividade da fosfatase alcalina.
