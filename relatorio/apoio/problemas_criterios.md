# Problemas críticos do professor e critérios da análise

Apoio do Claude Code (3 out 2026). Fonte do mapa: data/problemas_criticos.csv. Resultados:
results/resumo_robustez.md (cenário P-foco) e results/semiquantitativos.csv (par articular).

Problemas críticos indicados pelo professor (2 out 2026):
- Prótese da anca: desgaste e libertação de partículas.
- Implante dentário: integração com o osso e corrosão.
- Stent vascular: resistência mecânica e biocompatibilidade.
- Scaffold: suporte celular e degradação controlada.

## Mapa problema → critérios

Pesos no cenário A, como entram no cálculo (renormalizados; no stent, os pesos da base a dividir
por 0,85, porque o tempo de reabsorção só entra no cenário B).

| Caso | Problema | Critério | Peso (A) | Ligação |
|---|---|---|---|---|
| Anca, par articular | Desgaste e partículas | Taxa de desgaste linear | 0,35 | direta |
| | | Segurança iónica / risco ALTR (ordinal) | 0,25 (e triagem ≥ 2, que exclui o MoM) | direta |
| | | Compatibilidade galvânica cabeça-cone (ordinal) | 0,15 | direta |
| | | Dureza da cabeça | 0,05 | indireta |
| | | Compatibilidade com esterilização (ordinal) | 0,05 | indireta |
| Anca, haste | Desgaste e partículas | Resistência à corrosão (ordinal) | 0,15 | direta |
| Implante dentário | Integração com o osso | Evidência clínica de osteointegração (ordinal) | 0,25 | direta |
| | | Módulo de Young (alvo 15 GPa) | 0,20 | indireta |
| | Corrosão | (sem critério; a acrescentar) | 0 | |
| Stent | Resistência mecânica | Índice σy/E (recuo elástico) | 0,118 | direta |
| | | Alongamento na rotura | 0,118 | direta |
| | | Resistência à tração | 0,118 | direta |
| | | Módulo de Young | 0,059 | direta |
| | Biocompatibilidade | Espessura típica de strut | 0,235 | direta (propriedade do dispositivo) |
| | | Tempo de reabsorção (só cenário B) | 0,15 em B | indireta |
| Scaffold | Suporte celular | Porosidade | 0,15 | direta |
| | | Bioatividade (ordinal) | 0,15 | direta |
| | | Imprimibilidade 3D (ordinal) | 0,10 | indireta |
| | | Resistência à compressão | 0,15 | indireta (leitura ampla: suporte mecânico) |
| | | Módulo de compressão | 0,10 | indireta (leitura ampla: suporte mecânico) |
| | Degradação controlada | Tempo de degradação | 0,15 | direta |

Peso total dos critérios do problema (cenário A): par articular 0,75 (0,85 com indiretos);
haste 0,15; implante dentário 0,25 (0,45 com o módulo); stent 0,65 (0,55 em B); scaffold 0,45
(0,80 com indiretos).

Lacunas: no implante dentário não há critério de corrosão; no stent, o teor de níquel não é
critério (entra no perfil de alergia); no scaffold, a acidez dos produtos de degradação não é
critério.

## Cenário P-foco

Regra: o peso dos critérios ligados ao problema é multiplicado por 2 (fator_foco_problema, valor de
desenho) e todos os pesos são renormalizados. Resultado principal: só critérios de ligação direta
(no scaffold, a leitura literal do professor: porosidade, bioatividade e tempo de degradação);
sensibilidade: direta + indireta. Parte do cenário A, η = 1.

Entre parênteses, a diferença entre o 1.º e o 2.º (C no TOPSIS, Q no WASPAS, P no VIKOR).

| Caso | Versão | Peso do problema | TOPSIS | WASPAS | VIKOR | Muda face a A? |
|---|---|---|---|---|---|---|
| Haste | A | 0,15 | Ti-6Al-4V ELI (0,175) | Ti-6Al-4V ELI (0,069) | Ti-6Al-4V ELI (0,606) | |
| | P-foco, direta | 0,26 | Ti-6Al-4V ELI (0,182) | Ti-6Al-4V ELI (0,061) | Ti-6Al-4V ELI (0,435) | não |
| Stent | A | 0,65 | Pt-Cr (0,024) | Co-Cr L605 (0,014) | Pt-Cr (0,024) | |
| | P-foco, direta | 0,79 | Pt-Cr (0,028) | Co-Cr L605 (0,018) | Pt-Cr (0,026) | não |
| Scaffold | A | 0,45 | PCL/β-TCP (0,052) | PCL/β-TCP (0,098) | PCL/β-TCP (0,480) | |
| | P-foco, direta | 0,62 | **β-TCP poroso** (0,015) | PCL/β-TCP (0,070) | **β-TCP poroso** (0,075) | sim, TOPSIS e VIKOR |
| | P-foco, direta + indireta | 0,89 | PCL/β-TCP (0,116) | PCL/β-TCP (0,127) | PCL/β-TCP (0,542) | não |
| Par articular (semiquantitativo) | A | 0,75 | ZTA/ZTA (0,154) | ZTA/ZTA (0,389) | ZTA/ZTA (0,340) | |
| | P-foco, direta | 0,86 | ZTA/ZTA (0,224) | ZTA/ZTA (0,449) | ZTA/ZTA (0,392) | não |
| | P-foco, direta + indireta | 0,92 | ZTA/ZTA (0,223) | ZTA/ZTA (0,435) | ZTA/ZTA (0,391) | não |

Na haste e no stent, a versão direta + indireta dá o mesmo que a direta (a haste não tem critérios
indiretos; o único indireto do stent só entra no cenário B).

Leitura:
- Haste, stent e par articular: o vencedor não muda quando se reforça o problema crítico. No stent,
  os critérios do problema já pesam 65 % no cenário A, por isso o reforço muda pouco.
- Scaffold: com a leitura literal do professor, o β-TCP poroso passa a 1.º no TOPSIS e no VIKOR
  (melhor bioatividade e degradação mais próxima do alvo); o compósito PCL/β-TCP mantém-se 1.º no
  WASPAS. Se o suporte mecânico também contar, o compósito ganha nos três. A escolha do scaffold
  depende, por isso, de quanto se valoriza a resistência mecânica face ao suporte biológico. No
  TOPSIS a diferença é pequena (0,015), mas acima do limiar de empate (0,01).
