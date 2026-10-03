# 2. Métodos

## 2.1 Visão geral

Para cada caso clínico seguiu-se o mesmo processo, em sete passos:
1. definição da função do dispositivo e do problema do material atual;
2. escolha dos materiais candidatos;
3. triagem por critérios eliminatórios;
4. definição dos critérios de comparação e dos respetivos pesos;
5. normalização dos valores e ordenação dos materiais por três métodos de decisão multicritério;
6. análise da robustez do resultado;
7. validação da implementação contra um estudo publicado.

Três casos (haste femoral, stent coronário expansível por balão e scaffold para regeneração óssea) foram tratados quantitativamente. Os outros dois componentes (par articular da anca e implante dentário) foram tratados de forma semiquantitativa, porque a maior parte do peso dos seus critérios cabia a escalas ordinais (60 % do peso nos dois; a regra do trabalho é não passar de 50 % nos casos quantitativos, que têm 30 a 45 %). Nestes, apresenta-se a matriz de dados e a triagem, sem ranking.

## 2.2 Materiais candidatos e cenários

Para cada caso, os candidatos incluem os materiais em uso clínico e alternativas em investigação. Para não misturar materiais com graus de evidência muito diferentes, os resultados foram obtidos em dois cenários:
- **Cenário A:** só materiais em uso clínico.
- **Cenário B:** inclui também materiais em investigação (e, no stent, os bioabsorvíveis).

## 2.3 Critérios

Cada critério pertence a um de quatro tipos:
- **Estrito (eliminatório):** o material passa ou não passa (por exemplo, a biocompatibilidade segundo a ISO 10993, ou o tipo de expansão do stent). Os materiais eliminados ficam registados, com o motivo.
- **Benefício:** quanto maior, melhor (por exemplo, o limite de fadiga).
- **Custo:** quanto menor, melhor (por exemplo, a densidade ou o custo relativo).
- **Alvo:** o melhor valor é um valor intermédio. É o caso do módulo de Young da haste, que deve aproximar-se do osso cortical para reduzir o stress shielding. Seguiu-se a abordagem de critérios-alvo de Petković et al. (2025).

Usaram-se também dois índices derivados:
- σy/E, como indicador do recuo elástico do stent;
- E_implante/E_osso, como medida do desajuste de rigidez da haste.

Alguns critérios não têm uma grandeza física simples (resistência à corrosão, compatibilidade com ressonância magnética, fabricabilidade, custo relativo). Para estes usaram-se escalas ordinais de 1 a 5, com uma rubrica escrita para cada nível, apoiada em literatura.

## 2.4 Base de dados e verificação dos valores

Todos os valores estão numa base de dados única (ficheiros CSV). Cada valor tem um mínimo, um máximo, um valor típico, a fonte e um estado de verificação: "Verificado", "Verificado (fornecedor)", "Verificado (derivado)", "Verificado (composição química)" ou "A verificar".

Os valores de partida vieram de revisões. Os valores com mais influência no resultado foram verificados em fontes primárias (normas, artigos com ensaio, fichas técnicas de fabricantes e de fornecedores); os restantes ficam marcados "A verificar" (83 das 295 linhas da base estão verificadas). A ordem de verificação seguiu a influência de cada valor no resultado: cada valor foi variado ±20 % com os restantes fixos, e verificaram-se primeiro os que mudavam o vencedor.

Usaram-se três regras para manter os valores comparáveis:
- **Regra da forma:** quando uma propriedade depende da forma do produto (tubo, fita, fio, chapa), o mínimo e o máximo cobrem só a forma usada no dispositivo; os valores de outras formas ficam registados nas notas, mas não entram no cálculo. Quando a forma do dispositivo tem um único valor, aplica-se uma incerteza de ±10 %.
- **Regra da porosidade:** nos scaffolds, as propriedades mecânicas usam-se à porosidade típica do material (±10 pontos percentuais); o típico é a mediana das fontes dentro dessa janela.
- **Materiais permanentes num critério de reabsorção:** recebem o pior valor observado entre os reabsorvíveis do mesmo caso, como valor de modelação.

## 2.5 Normalização

Os critérios têm unidades diferentes (MPa, GPa, µm, escalas 1-5). Antes de os combinar, cada valor foi convertido numa nota adimensional entre 0 e 1. Nos critérios de benefício e de custo, a nota cresce com a proximidade ao melhor valor observado. Nos critérios-alvo, cresce com a proximidade ao valor-alvo, segundo a normalização de Petković et al. (2025) (eq. 2 no TOPSIS; o WASPAS usa as eqs. 9 a 13 e o VIKOR uma distância ao valor de referência, eqs. 17 e 18).

## 2.6 Pesos

Os pesos combinam duas fontes de informação:
- **Pesos subjetivos (w^S):** definidos neste trabalho com base na função clínica de cada dispositivo, com a justificação de cada peso indicada na tabela de critérios.
- **Pesos objetivos (w^O):** obtidos dos próprios dados pelo método do desvio-padrão. Um critério em que os materiais diferem mais recebe mais peso, porque distingue melhor as alternativas.

Os dois combinam-se por w = η · w^S + (1 − η) · w^O. O resultado principal usa η = 1 (só pesos subjetivos, justificados clinicamente). A sensibilidade a η foi analisada de 0 a 1, em passos de 0,1.

## 2.7 Métodos de decisão multicritério

Usaram-se três métodos que combinam os critérios de formas diferentes. Quando concordam, o resultado é mais sólido:
- **TOPSIS:** ordena os materiais pela proximidade relativa a uma solução ideal (o melhor valor em todos os critérios) e pelo afastamento a uma solução anti-ideal. O resultado é o coeficiente C, entre 0 e 1. Um ponto forte pode compensar um ponto fraco.
- **WASPAS:** combina a soma ponderada e o produto ponderado das notas normalizadas (λ = 0,5). A parte multiplicativa penaliza fortemente um critério com nota muito baixa, por isso o método favorece materiais equilibrados.
- **VIKOR:** procura a solução de compromisso. Combina o afastamento total à solução ideal (S) com o maior afastamento num único critério (R), através de um parâmetro v = 0,5. O índice final (P, na notação de Petković et al.) é tanto melhor quanto menor.

As equações de cada método seguem Petković et al. (2025) e são apresentadas em anexo.

## 2.8 Análise de robustez

O resultado foi testado em várias frentes:
- **Cenários de sensibilidade:** retirar os critérios ordinais (Q); variar η de 0 a 1; alterar os valores-alvo (T); dar peso baixo ou elevado ao custo (C-custo); impor um teto de orçamento [cenário ainda por implementar]; no stent, variar o valor atribuído aos permanentes no tempo de reabsorção (R-sentinela).
- **Monte Carlo das propriedades:** 10 000 repetições (semente 42), com cada valor sorteado uniformemente entre o mínimo e o máximo da base. Os valores de uma única fonte, sem intervalo, variaram ±10 % à volta do típico.
- **Monte Carlo dos pesos:** pesos perturbados ±20 %.
- **Concordância entre métodos:** coeficiente de correlação de Spearman entre as ordenações.
- **Regra de empate:** duas posições consecutivas cujo C do TOPSIS difere menos de 0,01 consideram-se empatadas.

## 2.9 Validação da implementação

A implementação foi validada reproduzindo o caso de estudo da prótese da anca de Petković et al. (2025). Foram reproduzidos os 15 coeficientes C publicados e as posições correspondentes, com uma diferença máxima de cerca de 5 × 10⁻⁶.

Nesta reprodução detetou-se uma incoerência no artigo: o valor de M1-C9 na Tabela A3 é 0,41, mas os resultados publicados só se reproduzem com 0,59. Os dados foram mantidos fiéis à tabela e a diferença ficou documentada (secção de validação).

## 2.10 Implementação e reprodutibilidade

Todo o processo foi implementado em Python, com testes automáticos para cada função (192 testes, dos quais 8 são falhas esperadas que documentam a incoerência do artigo reproduzido). Os dados, o código e os resultados estão num repositório com histórico de versões, e os resultados podem ser regenerados por quatro scripts (cálculo dos cenários, lista dos valores por verificar, figuras e folha de cálculo).
