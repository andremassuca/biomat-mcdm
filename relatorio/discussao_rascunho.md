# 8. Discussão

## 8.1 Robustez diferente em cada caso

Os três casos quantitativos dão conclusões com graus de confiança muito diferentes, e essa diferença é, em si, um resultado:
- **Haste femoral:** o Ti-6Al-4V ELI ficou em 1.º lugar com os três métodos, nos dois cenários e em pelo menos 99,99 % das iterações do Monte Carlo. A conclusão é robusta à incerteza dos dados e dos pesos.
- **Stent:** o platina-crómio e o cobalto-crómio L605 ficaram praticamente empatados nos rankings determinísticos, mas o Pt-Cr é claramente mais robusto à incerteza dos dados (1.º em 57 a 70 % das iterações do Monte Carlo). A ressalva é que esse resultado assenta em propriedades do Pt-Cr ainda só confirmadas em fontes secundárias.
- **Scaffold:** o compósito PCL/β-TCP impresso passou para 1.º lugar depois da verificação dos dados, com os três métodos e nos dois cenários (ΔC = 0,052 em A e 0,085 em B), sobretudo porque a resistência à compressão do β-TCP poroso, à porosidade relevante, é muito inferior ao valor de partida. O resultado é estável nos pesos (1.º lugar em cerca de 96 a 100 % das iterações com pesos ±20 %) mas sensível aos dados: no Monte Carlo das propriedades, o β-TCP fica em 1.º em mais iterações do que o compósito com o TOPSIS (52 % contra 39 %), embora não com o WASPAS (25 % contra 68 %) nem com o VIKOR (39 % contra 46 %).

## 8.2 A verificação dos dados mudou as conclusões

Os valores de partida vinham sobretudo de revisões. A verificação em fontes primárias alterou valores com impacto direto nos resultados:
- o módulo do Ti-6Al-4V ELI (o valor de partida era o da liga normal, não o da ELI);
- o estado do aço 316L (encruado, como nas hastes, e não recozido);
- a ordem entre o L605 e o Pt-Cr no stent;
- o vencedor do scaffold.

A lição metodológica é que um método multicritério não é mais fiável do que os dados que recebe. Duas regras foram essenciais para comparar valores de fontes diferentes: usar a forma do produto que o dispositivo realmente usa (tubo, fita, fio) e, nos scaffolds, comparar as propriedades mecânicas à mesma porosidade.

No stent, uma primeira versão dos dados incluía, nos intervalos, valores de formas de produto que o stent não usa (fio e barra). Isso fazia parecer o L605 e o MP35N mais robustos do que são; com os intervalos restritos à forma do dispositivo (tubo ou fita), o mais robusto passou a ser o Pt-Cr. É um exemplo de como a definição da incerteza, e não só o valor típico, pode mudar a conclusão.

## 8.3 Porque é que os métodos discordam

Quando os métodos discordam, a causa é quase sempre um material com um ponto muito forte e um muito fraco. O exemplo mais claro é o Co-Cr-Mo na haste: 2.º lugar no TOPSIS, porque a fadiga excelente compensa a rigidez excessiva, e 5.º no WASPAS, cuja parte multiplicativa penaliza fortemente o módulo muito afastado do osso. Usar três métodos tornou visível esta dependência, em vez de a esconder atrás de um único ranking.

## 8.4 O papel do custo

Quando o custo recebe peso elevado, o aço 316L volta a ser competitivo, na haste com o TOPSIS e no stent com o WASPAS. Isto reflete a realidade clínica: o aço continua a ser usado em contextos de custo restrito. A escolha final depende, por isso, das prioridades do hospital, e a análise torna essa dependência explícita. Com um teto de orçamento que exclui os materiais de custo relativo acima de 3, o vencedor só muda no stent: sem o Pt-Cr, o L605 passa a 1.º com os três métodos. Na haste (sai o Ti-13Nb-13Zr) e no scaffold (sai o vidro 45S5), o vencedor mantém-se.

## 8.5 Comparação com a prática clínica

As escolhas do modelo coincidem, em geral, com a prática clínica atual, o que reforça a sua credibilidade. Onde divergem, a divergência tem uma explicação.
- **Haste:** nos registos, a fixação não cimentada e a híbrida dominam (NJR 2026: 42,5 % e 41,8 % das primárias de 2025; AOANJRR 2025: 62,9 % e 35,7 % em 2024); as hastes não cimentadas são sobretudo de Ti-6Al-4V (Hu e Yoon 2018). O aço continua a ser usado em hastes cimentadas polidas (Lamb et al. 2025), o que é coerente com o resultado de que o aço volta a ser competitivo quando o custo pesa muito.
- **Par articular:** na prática, os pares mais usados são uma cabeça contra polietileno (cerâmica em cerca de 59 % e metálica em cerca de 33 % das primárias de 2025 no NJR; na Austrália, 97 % usaram polietileno reticulado ou cerâmica mista); o cerâmica-cerâmica caiu para cerca de 2 % e é usado em doentes mais novos (idade mediana de 59 a 60 anos, contra 70 no total; NJR 2026). O modelo coloca o cerâmica-cerâmica em 1.º lugar porque o desgaste domina os critérios, enquanto o risco de fratura e o ruído foram tratados de forma qualitativa e não entram no cálculo. É a principal divergência face à prática, e explica a preferência frequente pelo par cerâmica contra polietileno reticulado.
- **Stent:** os stents com eluição de fármaco atuais usam plataformas de cobalto-crómio ou de platina-crómio, com struts de cerca de 55 a 90 µm, e o aço inoxidável das plataformas de 1.ª geração (Cypher, Taxus) foi abandonado (Brami et al. 2023; Macaya-Ten et al. 2024). O modelo chega à mesma conclusão.
- **Scaffold:** os substitutos ósseos sintéticos mais usados na clínica são fosfatos de cálcio, como o β-TCP e a hidroxiapatite, e os compósitos impressos começam a ter uso clínico (Lodewijks et al. 2025; Lodewijks et al. 2024). O modelo coloca o compósito à frente quando o suporte mecânico conta, e o β-TCP quando só contam o suporte celular e a degradação.
- **Implante dentário:** o titânio comercialmente puro continua a ser a referência, e a zircónia é uma alternativa sobretudo estética, como no modelo.

## 8.6 Enquadramento regulamentar e disponibilidade

Em Portugal e na União Europeia, os dispositivos estudados estão sujeitos ao Regulamento (UE) 2017/745 relativo aos dispositivos médicos, aplicado em Portugal pelo INFARMED como autoridade competente. Pelas regras de classificação do anexo VIII, as próteses totais da anca e os stents coronários são dispositivos de classe III, os implantes dentários de classe IIb e os substitutos ósseos total ou maioritariamente absorvidos de classe III (regra 8 do anexo VIII). Os dispositivos de classe III exigem avaliação por um organismo notificado, investigação clínica na maioria dos casos e acompanhamento clínico depois da comercialização. O fabricante tem ainda de manter um sistema de gestão da qualidade segundo a ISO 13485 e um processo de gestão do risco segundo a ISO 14971.

Isto tem uma consequência direta para a seleção: um material sem historial clínico no dispositivo em causa, mesmo com melhores propriedades, implica anos de ensaios e de investigação clínica antes de poder ser usado. Foi por isso que os resultados se separaram num cenário A, só com materiais em uso clínico, e num cenário B, que inclui materiais em investigação. Nos Estados Unidos, o percurso equivalente passa pela FDA: os implantes dentários endósseos são de classe II e entram em regra por notificação prévia (510(k); 21 CFR 872.3640), e os dispositivos de classe III, como os stents com eluição de fármaco, por aprovação pré-comercialização (PMA; por exemplo, o XIENCE V, P070015). Quanto à disponibilidade, os materiais propostos para a haste, o par articular, o stent e o implante dentário são usados em dispositivos comercializados na União Europeia, enquanto os compósitos PCL/β-TCP impressos têm, por agora, uso clínico limitado (Lodewijks et al. 2024; Lodewijks et al. 2025).

## 8.7 Material ou dispositivo?

Várias propriedades decisivas são do dispositivo e não do material. A espessura dos struts depende do desenho do stent, e a rigidez de uma haste depende também da sua arquitetura. Um cálculo simples ilustra o alcance desta ideia: pela relação de Gibson e Ashby para materiais celulares, uma estrutura porosa de Ti-6Al-4V com cerca de 60 % de porosidade teria um módulo próximo do osso cortical: com E = E_s (1 − p)², constante C = 1 e E_s = 105,5 GPa (valor típico do Ti-6Al-4V ELI na base), o alvo de 17 GPa obtém-se com p = 59,9 %, e a 60 % de porosidade o módulo é 16,9 GPa (Gibson e Ashby 1997, cap. 5). A solução para o stress shielding pode não ser outra liga, mas a mesma liga estruturada, por exemplo por fabrico aditivo.

## 8.8 Limitações

- Os valores vêm de estudos diferentes, com métodos de ensaio e formas de produto diferentes; as regras da forma e da porosidade reduzem, mas não eliminam, essa heterogeneidade.
- Alguns critérios são ordinais, com rubricas definidas neste trabalho; foram mantidos minoritários no peso e testados num cenário sem ordinais.
- Os pesos subjetivos são valores de desenho, justificados mas não medidos.
- Os métodos de normalização dependem do mínimo e do máximo de cada critério, o que pode causar reversão de ranking ao acrescentar ou retirar materiais; observou-se um caso no scaffold.
- Parte dos valores continua "A verificar", embora, na haste e no scaffold, nenhum dos restantes mude o vencedor com uma variação de ±20 %; no stent, três ainda mudam (alongamento e tração do Pt-Cr e σy/E do L605).

## 8.9 Trabalho futuro

- Perfis de doente (idade, atividade, osteoporose, alergias, obesidade) que alterem pesos, alvos e exclusões.
- Custo ao longo da vida, com as taxas de revisão dos registos de artroplastia.
- A porosidade como variável de desenho.
- Uma ferramenta interativa que permita a médicos e engenheiros explorar as prioridades e ver o efeito no resultado.
