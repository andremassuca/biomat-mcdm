# LEIA-ME da base de dados

Fonte de verdade: os ficheiros CSV em data/ (materiais, criterios, tecido, cenarios, parametros)
e este ficheiro (texto da folha LEIA-ME). O base_dados_biomateriais.xlsx é gerado por
scripts/exportar_xlsx.py e não se edita à mão.

## Estado dos valores
- Todos os valores são pontos de partida de manuais e revisões e estão marcados "A verificar".
- Antes de usar um valor no relatório ou no poster: abre a fonte, confirma o número, preenche a coluna doi_url e muda o estado para "Verificado".
- Se a fonte der outro valor, usa o da fonte e regista a página ou tabela na coluna notas.

## Alterações v0.3 (após revisão crítica)
Densidade deixa de ser proxy de radiopacidade (nova escala de radiopacidade) · σy/E renomeado "proxy material" · Nitinol fora do ranking · K_IC retirado do par articular · "Resistência" retirada da matriz dentária (tração ≠ flexão) · alvos do scaffold passam a cenários · nova folha Cenarios

Par articular e implante dentário ficam SEMIQUANTITATIVOS (ordinais > 50 % do peso): MCDM quantitativo só para haste, stent (balão) e scaffold.

## Alterações v0.4 (28 set 2026)
- Os CSV passam a ser a fonte de verdade; o .xlsx é gerado só com valores (sem fórmulas).
- Novas colunas em materiais.csv: doi_url (a preencher) e valor_texto (propriedades categóricas).
- Nova propriedade "Tipo de expansão" do stent (balão ou autoexpansível), usada na triagem.
- Índices derivados calculados em src/biomat_mcdm/indices.py (σy/E do stent; E_implante/E_osso da haste).
- Cenários em cenarios.csv; η em parametros.csv.

## Alterações v0.5 (1 out 2026): 2.ª ronda do stent
- Valores de fichas de fornecedor no 316L (alongamento), no L605 (cedência, módulo, tração) e no MP35N (tração), com o valor anterior na nota.
- L605: o típico é o da chapa (Haynes), por não haver ficha de tubo com valores; a fita (Matthey) dá o intervalo.
- Pt-Cr: cedência com fonte primária (O'Brien 2010, só resumo); módulo, tração e alongamento continuam "A verificar", com fontes secundárias na nota.
- Radiopacidade: rubrica escrita (ver "Rubricas ordinais"), fontes nas 7 linhas e estado "Verificado"; as notas não mudam.
- Densidades do 316L, L605, MP35N e Pt-Cr com fonte. A densidade não é critério do stent.

## Alterações v0.6 (1 out 2026): 1.ª ronda do scaffold
- Rubrica da bioatividade reescrita segundo a classificação de Hench (classes A e B); as notas dos materiais não mudam.
- Regra da porosidade para as propriedades mecânicas dos scaffolds (ver "Cuidados").
- 11 linhas do scaffold com fonte primária: porosidade do quitosano/HA, do PLLA e do β-TCP; resistência à compressão da HA; e sete notas ordinais (imprimibilidade, esterilização e bioatividade).
- A esterilização da HA continua "A verificar".

## Alterações v0.7 (1 out 2026): 2.ª ronda do scaffold
- Regra do típico: típico = mediana das fontes dentro da janela de porosidade (porosidade típica do material ±10 pontos percentuais); o intervalo vai do mínimo ao máximo dessas fontes.
- β-TCP: resistência 0,35-7,72 MPa, típico 2. PCL/β-TCP: porosidade típica 70 % (especificação dos scaffolds por FDM).
- HA: tempo de degradação tratado como não reabsorvível (mínimo 42 meses; máximo e típico = pior valor observado nos outros materiais, como a opção O2 do stent).
- PLLA definido como scaffold impresso; degradação 24-60 meses, com dados de PLLA maciço.
- Vidro 45S5: resistência 0,2-1,1 MPa e degradação 6-24 meses (dados de partículas). O módulo fica sem fonte primária.
- Quitosano/HA: módulo e resistência cerca de dez vezes abaixo dos valores anteriores.
- Porosidades do PCL, do PLGA e da HA com fonte.

## Legenda
- min e max alimentam o Monte Carlo (distribuição entre mín. e máx.).
- tipico = valor usado nos métodos; por omissão o ponto médio; pode diferir quando a regra da forma ou outra regra o justifica, com nota.
- Estados da coluna estado:
  - "A verificar": valor de partida (manual, revisão ou fonte secundária) ainda não confirmado na fonte original.
  - "Verificado": valor confirmado na fonte indicada em doi_url (artigo ou norma).
  - "Verificado (fornecedor)": valor confirmado numa página de fornecedor que declara cumprir a norma, não no texto da norma.
  - "Verificado (composição química)": valor que resulta da composição química do material (ex.: 0 % de níquel num polímero sem metais).
  - "Verificado (derivado)": valor calculado a partir de dados da fonte (ex.: razão σFS/σUTS × σUTS), com o cálculo na nota.
- Teor de níquel (stent): % em massa; no WE43 é um limite máximo de impureza e tipico = máximo (pior caso).

## Tipos de critério (Petković et al., Appl Sci 2025;15:9198)
Estrito = triagem passa/falha · Benefício = maior é melhor · Custo = menor é melhor · Alvo = mais próximo do valor-alvo é melhor

## Rubricas ordinais (1-5): justificar cada nota no relatório com uma referência
- Corrosão: 5 = camada passiva estável sem libertação relevante; 3 = suscetível a picadas/fendas in vivo; 1 = corrosão clinicamente problemática
- Segurança iónica/ALTR: 5 = sem contacto metal-metal; 4 = risco na junção cabeça-cone; 1 = libertação de iões Co/Cr com ALTR documentada
- Osteointegração: 5 = padrão-ouro com décadas de dados; 3 = dados clínicos a médio prazo; 1 = bioinerte com fraca aposição óssea
- Estética: 5 = cor de dente; 3 = neutro; 2 = sombra cinzenta possível
- Bioatividade (classificação de Hench): 5 = classe A, osteoprodutivo (ex.: vidro 45S5); 4 = classe B, osteocondutor com ligação química ao osso (HA, β-TCP); 3 = osteocondutor sem ligação química, ou compósito com fase bioativa minoritária; 2 = pouca interação; 1 = bioinerte ou sem osteocondução. Fonte: Hench LL. Bioactive ceramics: theory and clinical applications. Bioceramics 1994;7:3-14 (original não lido); classes A e B lidas em Bramhill J, Ross S, Ross G. Int J Environ Res Public Health 2017;14:66, doi:10.3390/ijerph14010066 (revisão, texto completo).
- Imprimibilidade 3D: 5 = extrusão direta fácil; 3 = possível com limitações; 2 = requer técnicas especiais (robocasting, liofilização)
- Compatibilidade com RM: 5 = sem artefacto/aquecimento relevante; 4 = MR-condicional, artefacto pequeno (Ti); 3 = artefacto moderado (CoCr, Pt); 2 = artefacto marcado (aço inox)
- Esterilização: 5 = aceita métodos padrão sem degradação; 4 = requer método específico sem perda de propriedades; 3 = método restrito com risco de degradação; 2 = degradação documentada
- Custo relativo de material e fabrico (NÃO é preço clínico; critério de CUSTO): 1 = matéria-prima e processo maduros, menor complexidade; 2 = processo estabelecido com maior exigência de controlo; 3 = liga/material especializado ou cadeia de fabrico exigente; 4 = material caro, processo complexo, revestimento ou controlo rigoroso; 5 = material crítico, arquitetura complexa ou processo pouco escalável
- Fabricabilidade: 5 = processos industriais maduros (incl. fabrico aditivo); 3 = possível com limitações; 2 = escala laboratorial
- Galvânica cabeça-cone: 5 = sem par metálico; 3 = CoCr em cone de Ti (fretting documentado); 2 = múltiplas interfaces metal-metal
- Radiopacidade (stent): 5 = liga com fração elevada de elemento de Z alto (Pt-Cr); 4 = melhoria clara face ao 316L (L605, com W); 3 = referência dos metais de stent (316L, MP35N); 2 = pouco radiopaco (Nitinol); 1 = radiotransparente, precisa de marcadores (Mg WE43, PLLA). Critério: teor de elementos de Z alto (Pt, Z = 78; W, Z = 74). A densidade não é critério (desde a v0.3), serve só de evidência de apoio. Fontes: Allocco DJ et al. Trials 2010;11:1, doi:10.1186/1745-6215-11-1 (PMC2826324); PMC3692344 ("modest improvement" do CoCr face ao aço).

NOTA: índices ordinais só devem pesar ≤ 50 % do total de cada caso: o resto deve vir de propriedades medidas.

## Cuidados
1. Propriedades de scaffolds dependem da porosidade. Regra da porosidade: as propriedades mecânicas de um scaffold usam-se à porosidade típica desse material (±10 pontos percentuais); valores medidos a porosidades muito diferentes ficam de fora ou só alargam o intervalo, com nota. Dentro da janela, típico = mediana das fontes dentro da janela de porosidade (porosidade típica do material ±10 pontos percentuais); o intervalo vai do mínimo ao máximo dessas fontes. Regista sempre a porosidade e o método de fabrico do estudo.
2. Cerâmicos: resistência à flexão ≠ resistência à tração. Assinala sempre qual é.
3. Stents: o Nitinol é autoexpansível (outra classe): eliminado na triagem pela regra "Tipo de expansão"; só na discussão.
4. Cenários (cenarios.csv): A = só materiais clínicos; B = inclui investigação e bioabsorvíveis. No stent, A = só permanentes em uso clínico (316L, L605, MP35N, Pt-Cr); B = A + Mg WE43 e PLLA.

## Níveis de validação
(1) verificação de código = reproduzir Petković et al. 2025; (2) robustez interna = cenários; (3) validação clínica = NÃO demonstrada (trabalho futuro).
