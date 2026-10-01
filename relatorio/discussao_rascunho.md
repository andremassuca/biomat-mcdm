# 8. Discussão

## 8.1 Robustez diferente em cada caso

Os três casos quantitativos dão conclusões com graus de confiança muito diferentes, e essa diferença é, em si, um resultado:
- **Haste femoral:** o Ti-6Al-4V ELI ficou em 1.º lugar com os três métodos, nos dois cenários e em pelo menos 99,99 % das iterações do Monte Carlo. A conclusão é robusta à incerteza dos dados e dos pesos.
- **Stent:** o cobalto-crómio L605 e o platina-crómio ficaram praticamente empatados. O vencedor depende do método e do cenário, e no Monte Carlo o L605 ganha em cerca de metade das iterações. Os dois são equivalentes, com o L605 mais robusto e o Pt-Cr preferível quando a visibilidade radiológica com struts finos é prioritária.
- **Scaffold:** o compósito PCL/β-TCP impresso passou para 1.º lugar depois da verificação dos dados, com os três métodos e nos dois cenários (ΔC = 0,052 em A e 0,085 em B), sobretudo porque a resistência à compressão do β-TCP poroso, à porosidade relevante, é muito inferior ao valor de partida. O resultado é estável nos pesos (1.º lugar em cerca de 96 a 100 % das iterações com pesos ±20 %) mas sensível aos dados: no Monte Carlo das propriedades, o β-TCP fica em 1.º em mais iterações do que o compósito com o TOPSIS (52 % contra 39 %), embora não com o WASPAS (25 % contra 68 %) nem com o VIKOR (39 % contra 46 %).

## 8.2 A verificação dos dados mudou as conclusões

Os valores de partida vinham sobretudo de revisões. A verificação em fontes primárias alterou valores com impacto direto nos resultados:
- o módulo do Ti-6Al-4V ELI (o valor de partida era o da liga normal, não o da ELI);
- o estado do aço 316L (encruado, como nas hastes, e não recozido);
- a ordem entre o L605 e o Pt-Cr no stent;
- o vencedor do scaffold.

A lição metodológica é que um método multicritério não é mais fiável do que os dados que recebe. Duas regras foram essenciais para comparar valores de fontes diferentes: usar a forma do produto que o dispositivo realmente usa (tubo, fita, fio) e, nos scaffolds, comparar as propriedades mecânicas à mesma porosidade.

## 8.3 Porque é que os métodos discordam

Quando os métodos discordam, a causa é quase sempre um material com um ponto muito forte e um muito fraco. O exemplo mais claro é o Co-Cr-Mo na haste: 2.º lugar no TOPSIS, porque a fadiga excelente compensa a rigidez excessiva, e 5.º no WASPAS, cuja parte multiplicativa penaliza fortemente o módulo muito afastado do osso. Usar três métodos tornou visível esta dependência, em vez de a esconder atrás de um único ranking.

## 8.4 O papel do custo

Quando o custo recebe peso elevado, o aço 316L volta a ser competitivo, na haste com o TOPSIS e no stent com o WASPAS. Isto reflete a realidade clínica: o aço continua a ser usado em contextos de custo restrito. A escolha final depende, por isso, das prioridades do hospital, e a análise torna essa dependência explícita.

## 8.5 Material ou dispositivo?

Várias propriedades decisivas são do dispositivo e não do material. A espessura dos struts depende do desenho do stent, e a rigidez de uma haste depende também da sua arquitetura. Um cálculo simples ilustra o alcance desta ideia: pela relação de Gibson e Ashby para materiais celulares, uma estrutura porosa de Ti-6Al-4V com cerca de 60 % de porosidade teria um módulo próximo do osso cortical: com E = E_s (1 − p)², constante C = 1 e E_s = 105,5 GPa (valor típico do Ti-6Al-4V ELI na base), o alvo de 17 GPa obtém-se com p = 59,9 %, e a 60 % de porosidade o módulo é 16,9 GPa (Gibson e Ashby, Cellular Solids [confirmar edição e página]). A solução para o stress shielding pode não ser outra liga, mas a mesma liga estruturada, por exemplo por fabrico aditivo.

## 8.6 Limitações

- Os valores vêm de estudos diferentes, com métodos de ensaio e formas de produto diferentes; as regras da forma e da porosidade reduzem, mas não eliminam, essa heterogeneidade.
- Alguns critérios são ordinais, com rubricas definidas neste trabalho; foram mantidos minoritários no peso e testados num cenário sem ordinais.
- Os pesos subjetivos e os multiplicadores dos perfis são valores de desenho, justificados mas não medidos.
- Os métodos de normalização dependem do mínimo e do máximo de cada critério, o que pode causar reversão de ranking ao acrescentar ou retirar materiais; observou-se um caso no scaffold.
- Parte dos valores continua "A verificar", embora, na haste e no scaffold, nenhum dos restantes mude o vencedor com uma variação de ±20 %; no stent, três ainda mudam (alongamento e tração do Pt-Cr e σy/E do L605).

## 8.7 Trabalho futuro

- Perfis de doente (idade, atividade, osteoporose, alergias, obesidade) que alterem pesos, alvos e exclusões.
- Custo ao longo da vida, com as taxas de revisão dos registos de artroplastia.
- A porosidade como variável de desenho.
- Uma ferramenta interativa que permita a médicos e engenheiros explorar as prioridades e ver o efeito no resultado.
