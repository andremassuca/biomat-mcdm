# Ponto de situação

Atualizado no fim de cada tarefa da fila. Última atualização: 3 out 2026 (tarde).

## Prazos
- Relatório: 8 out 2026.
- Poster (BioJornadas): 16 out 2026. Participação confirmada com a coordenadora (3 out); Prof. Pedro Sampaio convidado para orientador.

## Problemas críticos por dispositivo (professor, 2 out 2026)
Referir explicitamente no relatório (texto em docs/aulas/problemas_criticos_2026-10-02.md, fora do Git):
- Prótese da anca: desgaste e libertação de partículas.
- Implante dentário: integração com o osso e corrosão.
- Stent vascular: resistência mecânica e biocompatibilidade.
- Scaffold: suporte celular e degradação controlada.
Formato do relatório: liberdade total (sem limite de páginas nem modelo obrigatório; professor, 3 out).

## Fila de trabalho (tudo no ramo main, uma tarefa de cada vez)
Para o relatório, até 8 out:
1. Scaffold, 2.ª ronda. Feito.
2. Stent: frases com fonte e espessura de strut do 316L. Feito.
3. Figuras com os ajustes pedidos e os dados atuais; export do scaffold. Feito.
4. Textos: rascunhos de métodos, validação, discussão e caso do scaffold; verificação de cada número; números do stent; cálculo de Gibson-Ashby. Feito.
P1. Mapa problema crítico → critérios. Feito (relatorio/apoio/problemas_criterios.md).
P2. Cenário P-foco. Feito: só o scaffold muda (β-TCP 1.º no TOPSIS e no VIKOR com a leitura literal; PCL/β-TCP mantém-se com a leitura ampla e no WASPAS).
P3. Implante dentário centrado na osteointegração e na corrosão. Feito: critério de corrosão (0,15), osteointegração com fontes (Ti-6Al-4V 4 → 2); Ti cp grau 4 em 1.º em todas as versões (relatorio/apoio/dentario_apoio.md).
P4. Textos dos problemas críticos nos quatro casos, Q3/Q6/Q8 do dentário e conclusões. Feito.
P5. Montagem do relatório. Feito (3 out): RELATORIO.md (scripts/montar_relatorio.py) e RELATORIO_v0.pdf (pandoc + Tectonic). Para regenerar: run_all.py, figuras.py, tabelas_relatorio.py, montar_relatorio.py e depois pandoc relatorio/RELATORIO.md -o relatorio/RELATORIO_v0.pdf --pdf-engine=D:/LAB/.tools/tectonic/tectonic.exe --resource-path=relatorio. Versão 1 (3 out): RELATORIO_v1.pdf com 54 páginas, anexo B só com a contagem por estado (tabela completa no .xlsx e em relatorio/tabelas/anexo_b_dados.md) e nenhuma marca por confirmar no texto. Falta: revisão do André.
4b. Textos: introdução, conclusões, resumo, caso do implante dentário, declaração e glossário. Gravados; falta verificar cada número e alinhar o implante dentário com a base.
5. Estrutura do relatório (proposta do Claude Code, a aprovar antes de montar): relatorio/RELATORIO.md, lista única de referências e scripts/verificar_referencias.py.
6. Implante dentário: passou para P3.
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
- Stent: o texto do caso (Monte Carlo, "43 a 62 %" e "8 a 12 %") e a discussão ("o L605 ganha em cerca de metade das iterações", "L605 mais robusto") e as conclusões ("o L605 é a escolha de referência, por ser mais robusto à incerteza dos dados") têm os números anteriores à regra da forma revista; pedir ao chat a frase nova com os valores de 2 out.
- Métodos e glossário: a frase da regra da forma ("as outras formas só alargam o intervalo") ficou desatualizada.
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

## Stent (2 out 2026, regra da forma revista)
- Cenário A: Pt-Cr em 1.º no TOPSIS e no VIKOR, L605 em 1.º no WASPAS; ΔC = 0,024.
- Cenário B: L605 em 1.º nos três métodos, empatado com o Pt-Cr (ΔC = 0,002).
- Regra da forma revista (2 out): mín. e máx. só com a forma do dispositivo (tubo ou fita); outras formas só na nota; valor único com ±10 %. Os típicos e os rankings não mudaram; mudou o Monte Carlo.
- Monte Carlo das propriedades (cenário A): Pt-Cr em 1.º em 57-70 % das iterações (TOPSIS 69,9 %; WASPAS 56,6 %; VIKOR 59,1 %), L605 em 27-42 %, MP35N em 2-9 %. Antes da revisão: L605 43-62 %, MP35N 26-46 %, Pt-Cr 8-12 %.
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
