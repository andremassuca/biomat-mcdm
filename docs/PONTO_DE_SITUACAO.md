# Ponto de situação

Atualizado no fim de cada tarefa da fila. Última atualização: 1 out 2026.

## Prazos
- Relatório: 8 out 2026.
- Poster (BioJornadas): 16 out 2026.

## Fila de trabalho (tudo no ramo main, uma tarefa de cada vez)
Para o relatório, até 8 out:
1. Scaffold, 2.ª ronda. Feito.
2. Stent: frases com fonte e espessura de strut do 316L. Feito.
3. Figuras com os ajustes pedidos e os dados atuais; export do scaffold. Feito.
4. Textos: rascunhos de métodos, validação, discussão e caso do scaffold; verificação de cada número; números do stent; cálculo de Gibson-Ashby. Feito.
4b. Textos: introdução, conclusões, resumo, caso do implante dentário, declaração e glossário. Gravados; falta verificar cada número e alinhar o implante dentário com a base. É a próxima tarefa.
5. Enunciado e estrutura: relatorio/RELATORIO.md e scripts/verificar_referencias.py.
6. Implante dentário: tabela de apoio e proposta de fontes.
7. Cenário de orçamento, ranking de consenso e perfis de doente.
8. Apoio aos métodos: tabelas de critérios, figura dos pesos e figura do exemplo dos três métodos.
9. Análises extra: estabilidade dos pesos, frente de Pareto, confiança do ranking.
Depois da tarefa 9: tag v1-relatorio; a base de dados fica congelada para o relatório.

Depois de 8 out: custo ao longo da vida e margem de segurança à fadiga; aplicação interativa; base de dados v2.

## Feito a 1 out 2026
- Stent: 2.ª ronda de verificação, fontes das nove frases por confirmar do rascunho, espessura de strut do 316L (130-140 µm) e normas com edição.
- Scaffold: 1.ª e 2.ª rondas de verificação, rubrica da bioatividade segundo Hench, regra da porosidade e regra da mediana na janela.
- Figuras dos três casos quantitativos (seis figuras, PNG e SVG) e exports de dados do stent e do scaffold.
- Rascunhos do relatório: stent, scaffold, métodos, validação e discussão verificados contra o código e os resultados; textos gerais gravados sem verificação.

## Gravado sem commit
Nada: está tudo no repositório.

## Decisões pendentes
- Stent, MP35N no Monte Carlo: o intervalo do alongamento inclui o valor do fio (70 %); proposta: valores de outras formas só nas notas, intervalo do Monte Carlo só com a forma do dispositivo.
- Stent: o texto do caso e a discussão ainda tratam só o L605 e o Pt-Cr como candidatos ao 1.º lugar; rever depois da decisão sobre o MP35N.
- Métodos: o cenário de teto de orçamento e o anexo das equações estão no texto mas ainda não existem (tarefas 5 e 7); os perfis de doente da discussão também não (tarefa 7).
- Gibson e Ashby: edição e página da referência.
- Scaffold: seis marcas por confirmar no rascunho (fontes da porosidade e da inflamação pelo PLGA, normas e exemplo de modelo animal).
- Textos gerais (introdução, conclusões, resumo, implante dentário, declaração e glossário): gravados sem verificação.

## Estado por caso
- Haste femoral: Ti-6Al-4V ELI em 1.º nos três métodos, cenários A e B; 31 células por verificar, nenhuma muda o vencedor.
- Stent: 1.ª e 2.ª rondas aplicadas; 43 células por verificar, 3 mudam o vencedor.
- Scaffold: 1.ª e 2.ª rondas aplicadas; 39 células por verificar, nenhuma muda o vencedor.
- Par articular e implante dentário (semiquantitativos): tabela do par articular em relatorio/apoio/.
- Relatório: rascunhos dos casos da anca e do stent em relatorio/.

## Stent (1 out 2026)
- Cenário A: Pt-Cr em 1.º no TOPSIS e no VIKOR, L605 em 1.º no WASPAS; ΔC = 0,024.
- Cenário B: L605 em 1.º nos três métodos, empatado com o Pt-Cr (ΔC = 0,002).
- Monte Carlo das propriedades (cenário A): L605 em 1.º em 43-62 % das iterações, MP35N em 26-46 %, Pt-Cr em 8-12 %.
- O vencedor depende do alongamento e da tração do Pt-Cr, que ainda vêm de fontes secundárias: o O'Brien 2010 (texto completo, Tabelas 4 e 6) é decisivo.

## Scaffold depois da 2.ª ronda (1 out 2026)
- PCL/β-TCP impresso em 1.º nos três métodos, cenário A (ΔC = 0,052) e cenário B (ΔC = 0,085).
- Monte Carlo das propriedades (cenário A): PCL/β-TCP em 1.º em 39 % (TOPSIS), 68 % (WASPAS) e 46 % (VIKOR) das iterações; β-TCP em 52 %, 25 % e 39 %.
- O vencedor só muda num cenário de sensibilidade: alvo da resistência à compressão a 2 MPa (ganha o β-TCP).
- O resultado mudou com a verificação: com os valores de partida ganhava o β-TCP.
- Ficam por verificar a resistência e o tempo de degradação do PCL/β-TCP, o tempo de degradação do quitosano/HA, o módulo do β-TCP e do vidro 45S5 e a esterilização da HA e do 45S5.

## Por fazer nos dados
- Pt-Cr: confirmar módulo, tração e alongamento numa fonte primária (O'Brien 2010).
- Registar o URL da ficha da Alleima (316L).

## Testes
`pytest -q`: 184 passam, 8 falhas esperadas (xfail).
