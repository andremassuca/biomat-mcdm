# 3. Validação da implementação

Antes de aplicar os métodos aos casos deste trabalho, foi necessário garantir que a implementação estava correta. Para isso reproduziu-se um estudo publicado que usa os mesmos métodos com critérios-alvo: Petković et al. (2025), Applied Sciences 15(16):9198.

## 3.1 Reprodução do caso da prótese da anca

Reproduziu-se o caso de estudo 2 do artigo (seleção de material para prótese da anca), com a matriz de decisão, os tipos de critério, os valores-alvo e os pesos publicados. A implementação reproduziu:
- os 15 coeficientes C do TOPSIS publicados (um por material, com η = 1, Tabela 3), com uma diferença máxima de cerca de 5 × 10⁻⁶;
- as posições correspondentes;
- os 15 valores Q do WASPAS e os 15 valores P do VIKOR dos casos 1 e 2 do artigo (Tabelas 1 e 3), com uma diferença inferior a 10⁻⁵, e as 60 posições da Tabela 4 em cada método.

Um único resultado, para η = 0,7, difere por efeito de arredondamento dos valores publicados, e está registado como diferença esperada.

## 3.2 Incoerência encontrada no artigo

Na reprodução detetou-se uma incoerência nos dados publicados. Na Tabela A3, o material M1 tem o valor 0,41 no critério C9. Com esse valor, os resultados calculados não coincidem com os publicados; com 0,59, coincidem todos.

A tabela foi verificada célula a célula sobre a imagem das páginas do artigo, e o valor impresso é de facto 0,41. A Figura A6 do próprio artigo, uma captura do software dos autores, mostra 0,59 nessa célula. Conclui-se que o software usou 0,59, e que a incoerência está na tabela publicada e não na implementação.

Os dados foram mantidos fiéis à tabela publicada, e a diferença ficou documentada com um teste separado que usa 0,59. Este resultado mostra o valor de reproduzir estudos publicados antes de reutilizar os seus métodos, e é uma contribuição deste trabalho para a reprodutibilidade em decisão multicritério.
