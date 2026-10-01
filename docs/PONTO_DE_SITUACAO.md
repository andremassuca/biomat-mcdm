# Ponto de situação

Atualizado no fim de cada sessão de trabalho. Última atualização: 1 out 2026.

## Prazos
- Relatório: 8 out 2026.
- Poster (BioJornadas): 16 out 2026.

## Estado por caso
- Haste femoral (quantitativo): resultados preliminares gerados; 31 células por verificar, nenhuma muda o vencedor.
- Stent (quantitativo): 1.ª e 2.ª rondas de verificação aplicadas; 44 células por verificar, 3 mudam o vencedor.
- Scaffold ósseo (quantitativo): resultados preliminares gerados; 64 células por verificar, 3 mudam o vencedor.
- Par articular e implante dentário (semiquantitativos): tabela do par articular em relatorio/apoio/.
- Relatório: rascunho do caso da anca em relatorio/ (caso_anca_rascunho.md; o 05_1_anca.md é um rascunho antigo, preservado).
- Export de dados do stent (relatorio/apoio/stent_export.md) gerado de novo com a 2.ª ronda.

## Stent depois da 2.ª ronda (1 out 2026)
- Cenário A: Pt-Cr em 1.º no TOPSIS e no VIKOR, L605 em 1.º no WASPAS. ΔC entre o 1.º e o 2.º no TOPSIS: 0,026.
- Cenário B: L605 em 1.º nos três métodos, com o Pt-Cr praticamente empatado (ΔC = 0,002).
- Cenário B-bio: Mg WE43 à frente do PLLA.
- Monte Carlo das propriedades (cenário A): L605 em 1.º em 51-62 % das iterações, conforme o método. O resultado do cenário A não é robusto.
- Células por verificar que mudam o vencedor: alongamento e tração do Pt-Cr (fontes secundárias) e σy/E do L605 (derivado).
- Leitura: L605 e Pt-Cr estão empatados. O vencedor depende do alongamento e da tração do Pt-Cr, que ainda vêm de fontes secundárias, por isso o O'Brien 2010 (texto completo, Tabelas 4 e 6) é decisivo para fechar o caso.

## Por fazer
- Pt-Cr: confirmar módulo, tração e alongamento numa fonte primária (O'Brien 2010, Tabelas 4 e 6, tubo recozido). A cedência está confirmada só pelo resumo.
- Registar o URL da ficha da Alleima (316L).
- Texto do caso do stent e do scaffold no relatório.

## Testes
`pytest -q`: 171 passam, 8 falhas esperadas (xfail).
