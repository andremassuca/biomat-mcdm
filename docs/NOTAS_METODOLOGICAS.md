# Notas metodológicas (ir preenchendo, vira a secção de Métodos)

## Âmbito
- MCDM quantitativo: haste femoral, stent coronário expansível por balão, scaffold ósseo.
- Semiquantitativo (ordinais > 50 % do peso): par articular, implante dentário.
- Nitinol (autoexpansível, periférico) fora do ranking; só na discussão.

## Níveis de validação (não confundir)
| Nível | Pergunta | O que se pode afirmar |
|---|---|---|
| Verificação de código | O algoritmo está bem implementado? | Reproduz Petković et al. 2025 dentro de tolerância definida |
| Robustez interna | O ranking muda com pesos, método, η, incerteza, alvos? | A seleção é robusta/frágil nos cenários testados |
| Validação clínica | O ranking prevê desempenho clínico? | NÃO demonstrado: trabalho futuro |

A "% de vitórias" no Monte Carlo NÃO é probabilidade de sucesso clínico: é a frequência com que um material fica em 1.º nas hipóteses do modelo.

## Decisões e justificações
- σy/E: proxy ao nível do material da deformação elástica na cedência. Em stents expansíveis por balão, maior σy/E → maior recuo elástico → critério de CUSTO. Não é o recuo do dispositivo (depende da geometria do padrão, struts, processamento).
- E_implante/E_osso: indicador exploratório de risco relativo de stress shielding; a transferência de carga real depende de geometria, fixação e contacto (FEA = trabalho futuro).
- Alvo E = 17 GPa na haste: todos os candidatos estão acima do alvo → na prática funciona como "menor é melhor" com escala comprimida; testar vs critério de custo com limiar de fadiga (cenário T-haste). O cenário T-haste inclui também a comparação do alvo 14 GPa (Petković et al. 2025, Tabela A3, C5) vs 17 GPa.
- Alvos do scaffold = cenário de referência para osso trabecular, não ótimo universal (cenário T-scaffold).
- Densidade removida como proxy de radiopacidade (depende do número atómico efetivo e da espessura).
- K_IC removido do par articular (valor metálico arbitrário); fratura cerâmica tratada como requisito estrito/discussão.
- Tração (metais) e flexão (cerâmicos) não são comparáveis → retirado da matriz dentária; requisito estrito ISO 14801.
- Desgaste: só comparar valores do mesmo tipo de evidência (in vivo radiográfico/RSA OU simulador ISO 14242).

## Reprodução de Petković et al. 2025
Caso de estudo 2 (haste da prótese da anca), TOPSIS; testes em tests/test_reproduce_petkovic.py.
- Incoerência no artigo, verificada no PDF a 27 set 2026:
  - Tabela A3 (p. 30): M1-C9 (biocompatibilidade) = 0,41.
  - Figura A6 (p. 30, captura do software MCSl, η = 1): M1-C9 = 0,59.
  - Todas as outras 149 células, os 10 alvos, os 15 C_i e as 15 posições coincidem entre a
    Figura A6 e o que está nos testes.
- Os resultados publicados (Tabela 3, Tabela 4, Figura A6) foram calculados com 0,59.
- Com a matriz da Figura A6 e os pesos com 5 casas mostrados na mesma figura, o nosso TOPSIS
  reproduz os 15 C_i (diferença máxima 5e-6) e as 15 posições.
- Com os pesos da Tabela A3 (3 casas) e M1-C9 = 0,59: posições iguais para η = 0,8; 0,9; 1;
  para η = 0,7, M10 e M11 trocam (C a 0,00005 de distância, abaixo do efeito do arredondamento
  dos pesos).
- Com a matriz da Tabela A3 (0,41): só 4 de 15 posições coincidem (η = 1); o 1.º lugar (M7)
  mantém-se.
- Os pesos da Figura A6 correspondem a frações n/180 (21, 18, 25, 13, 16, 11, 17, 24, 26, 9;
  soma 180). Observação, não usada nos testes.
- Estado: email ao autor correspondente por enviar (rascunho em docs/email_petkovic_M1C9.md).
- Para a secção de Métodos: a verificação usa os dados do software (Figura A6) e declara a
  incoerência da Tabela A3.
- WASPAS e VIKOR: por verificar quando forem implementados (secções 2.7 e 2.8).

## Valores a verificar (fora de data/materiais.csv)
Os valores de propriedades "A verificar" estão na base e serão listados por
scripts/listar_por_verificar.py (tarefa 12). Aqui ficam os que não estão nessa coluna:
- [ ] Fonte para o alvo de E do osso cortical femoral (17 GPa) ou alinhamento com os 14 GPa do artigo-base (Petković et al. 2025).

## Por preencher
- Fontes dos dados e critério de inclusão:
- Justificação final dos pesos e do η:
- Parâmetros do Monte Carlo:
- Limitações:
