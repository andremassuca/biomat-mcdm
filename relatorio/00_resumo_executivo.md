# 4. Resumo executivo

*Rascunho de trabalho. As propostas são preliminares: a escolha final de cada caso depende dos resultados da secção 6 e da verificação dos dados na base de dados.*

O enunciado descreve um hospital que quer substituir um dispositivo cujo material falha por rejeição, desgaste, corrosão ou perda de propriedades mecânicas. A Tabela 4.1 resume, para cada um dos quatro casos, o problema do material atual, os biomateriais que foram comparados e a solução proposta. Em todos os casos a proposta resulta de duas fases: primeiro eliminam-se os materiais que falham um requisito que não pode ser compensado (por exemplo, a segurança iónica no par articular), e só depois se ordenam os restantes.

**Tabela 4.1.** Casos, problemas, biomateriais investigados e proposta.

| Caso | Problema | Biomateriais a investigar | Proposta |
|---|---|---|---|
| **Prótese da anca** | **Desgaste:** partículas do par articular que levam a osteólise e descolamento asséptico. **Corrosão/rejeição:** iões Co/Cr nos pares metal-metal e corrosão na junção cabeça-cone. **Mecânico:** stress shielding por rigidez excessiva da haste. | *Haste:* aço inox 316L, Co-Cr-Mo forjado, Ti-6Al-4V ELI, Ti cp grau 4, Ti-13Nb-13Zr; Ti-35Nb-7Zr-5Ta (TNZT, em investigação, só no cenário B). *Par articular:* CoCrMo/UHMWPE, CoCrMo/HXLPE, ZTA/HXLPE, ZTA/ZTA, CoCrMo/CoCrMo (metal-metal, eliminado na triagem). | Haste em Ti-6Al-4V ELI; cabeça femoral cerâmica em ZTA; componente acetabular em polietileno altamente reticulado (HXLPE) estabilizado com vitamina E. |
| **Implante dentário** | **Rejeição/integração:** falha de osteointegração e peri-implantite. **Mecânico:** fratura do implante ou do pilar. Estética em gengiva fina. | Ti cp grau 4, Ti-6Al-4V ELI, Ti-Zr (cerca de 15 % Zr), zircónia Y-TZP, PEEK. | Ti cp grau 4 com superfície rugosa; zircónia Y-TZP como alternativa estética, sem eliminar o risco de peri-implantite, que depende também do controlo de placa e de fatores do doente. |
| **Stent vascular** | **Rejeição/resposta do organismo:** reestenose por hiperplasia da neoíntima e trombose tardia. **Corrosão:** libertação de níquel em doentes com alergia. **Mecânico:** recuo elástico e struts espessos. | Aço inox 316L, Co-Cr L605, Co-Ni-Cr-Mo MP35N, Pt-Cr; bioabsorvíveis (liga de Mg WE43, PLLA) só no cenário B. Nitinol fica fora da comparação por ser autoexpansível. | Stent de liga de Co-Cr (L605) com struts finos e eluição de fármaco. Os bioabsorvíveis são discutidos de forma crítica a partir do caso Absorb. |
| **Scaffold ósseo** | **Mecânico:** compromisso entre porosidade e resistência. **Degradação:** reabsorção dessincronizada da formação de osso novo e acidez dos produtos de degradação dos poliésteres. | PCL, PLLA, PLGA 50:50, hidroxiapatite (HA) porosa, β-TCP poroso, vidro bioativo 45S5, compósito PCL/β-TCP, quitosano/HA. | Compósito PCL/β-TCP impresso em 3D, com porosidade interligada: o polímero dá tenacidade e permite controlar a arquitetura, e a fase cerâmica dá bioatividade e atenua a acidez local. |

## Tipo de análise por caso

A comparação quantitativa (TOPSIS, WASPAS e VIKOR com critérios-alvo, segundo Petković et al., 2025) só foi aplicada onde há propriedades medidas e comparáveis entre materiais: haste femoral, stent expansível por balão e scaffold ósseo. No par articular e no implante dentário, mais de metade do peso da decisão recai sobre critérios qualitativos (segurança iónica, evidência de osteointegração, estética), e os dados de desgaste ou de resistência não são diretamente comparáveis. Nesses dois casos a comparação é semiquantitativa.

## Notas sobre as propostas

- **Anca.** O par metal-metal é eliminado antes da ordenação, porque a segurança iónica não pode ser compensada por um bom desempenho noutros critérios. A escolha da haste depende sobretudo do compromisso entre a rigidez (mais próxima do osso) e a resistência à fadiga; as ligas beta de titânio, como o TNZT, são mais próximas do osso mas ainda não têm uso clínico corrente.
- **Implante dentário.** A zircónia resolve o problema estético, mas não tem o mesmo volume de evidência clínica de osteointegração que o titânio, e a peri-implantite não depende só do material.
- **Stent.** O Absorb (PLLA) foi descontinuado pela Abbott a 14 de setembro de 2017, invocando oficialmente baixas vendas, num contexto de mais trombose do scaffold e eventos cardíacos face ao stent metálico Xience no ensaio ABSORB III e de alertas da FDA em 2017. Por isso os bioabsorvíveis entram apenas num cenário alternativo e não na proposta principal.
- **Scaffold.** Os valores-alvo (porosidade, módulo, resistência à compressão e tempo de degradação) representam osso trabecular de referência e não um ótimo universal; a proposta é testada com vários alvos na análise de robustez.

Em nenhum caso a proposta é uma recomendação clínica. É a escolha mais defensável com os critérios, pesos e dados usados, e a secção 6 mostra até que ponto se mantém quando essas hipóteses mudam.
