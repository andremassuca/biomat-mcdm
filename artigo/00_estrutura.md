# Estrutura do artigo (IMRaD): só pontos a cobrir

Regra: este ficheiro tem estrutura e listas, sem prosa. O texto é escrito pelo André, em
inglês, depois de 16 out 2026.

**Pergunta de investigação:** "Are target-based MCDM rankings of biomaterials robust to changes
in method, criteria weights and property uncertainty across different medical device classes?"

**Contribuição face a Petković et al. 2025 (Appl. Sci. 15(16), 9198):**
1. Extensão a cerâmicos, polímeros e biodegradáveis (o artigo-base só tem metais).
2. Critério-alvo de degradação (tempo de degradação do scaffold; tempo de reabsorção do stent no cenário B).
3. Análise de robustez: Monte Carlo, sensibilidade a η, concordância entre métodos.
4. Validação da implementação por reprodução exata do caso publicado, com identificação de uma incoerência na Tabela A3.
5. Casos históricos de falha como validação qualitativa.

Legenda das origens: `docs/` notas e fontes; `data/` dados; `results/` resultados;
`tests/` verificação do código.

---

## Title
- [ ] Incluir: target-based MCDM, biomaterial selection, robustness, device classes
- [ ] 2 ou 3 versões para escolher com o Prof. Pedro Sampaio
- Origem: pergunta de investigação (acima)

## Abstract
- [ ] Contexto: seleção de biomateriais depende do dispositivo e do mecanismo de falha
- [ ] Lacuna: MCDM com critérios-alvo aplicado sobretudo a metais e sem análise de robustez sistemática
- [ ] Métodos: TOPSIS, WASPAS e VIKOR com critérios-alvo; 3 casos quantitativos; cenários de robustez
- [ ] Resultados principais: materiais mais bem posicionados por caso; % de 1.º lugar no Monte Carlo; concordância entre métodos
- [ ] Verificação: reprodução exata de Petković et al. 2025
- [ ] Conclusão: onde o ranking é robusto e onde é frágil
- [ ] Limite de palavras da revista: ver `02_revistas_alvo.md`
- Origem: `results/` (a produzir nas tarefas 9 e 11), `tests/test_reproduce_petkovic.py`

## Keywords
- [ ] 5 a 6 palavras-chave (ex.: biomaterial selection; MCDM; target-based criteria; TOPSIS; robustness analysis; Monte Carlo)
- [ ] Confirmar se a revista usa vocabulário controlado

## Introduction
- [ ] Classes de dispositivos e mecanismos de falha: haste femoral, stent, scaffold ósseo
  - Origem: `docs/TP2_fisiopatologia_da_falha.md` (casos 1, 3 e 4)
- [ ] Porque a seleção de biomateriais é um problema multicritério (propriedades em conflito)
  - Origem: `docs/TP2_guia_de_fontes.md` (6.1 Metodologia)
- [ ] Critérios-alvo: quando "mais" não é melhor (ex.: módulo de Young e stress shielding)
  - Origem: `docs/NOTAS_METODOLOGICAS.md` (Decisões e justificações)
- [ ] Estado da arte: Petković et al. 2025; Jahan et al. (normalização alvo) [confirmar referências]
  - Origem: `docs/TP2_guia_de_fontes.md` (6.1)
- [ ] Lacuna: poucos trabalhos testam robustez a método, pesos e incerteza; poucos cobrem cerâmicos, polímeros e biodegradáveis
- [ ] Pergunta de investigação e as 5 contribuições (acima)

## Materials and Methods
- [ ] Fluxograma do método (Figura 1)
- [ ] Mapa mecanismo de falha → propriedade → critério (Figura 2)
  - Origem: `docs/TP2_fisiopatologia_da_falha.md` (secções "Implicações para a seleção")
- [ ] Casos e âmbito: 3 quantitativos (haste, stent expansível por balão, scaffold); par articular e implante dentário semiquantitativos; Nitinol fora do ranking
  - Origem: `docs/NOTAS_METODOLOGICAS.md` (Âmbito), `CLAUDE.md` (Âmbito congelado)
- [ ] Materiais candidatos, estatuto clínico e fontes das propriedades (Tabela 1)
  - Origem: `data/materiais.csv`, `data/base_dados_biomateriais.xlsx` (folha Materiais)
- [ ] Critério de inclusão dos dados e tratamento de intervalos (mín./máx.; valor típico = ponto médio)
  - Origem: `src/biomat_mcdm/io.py`, `docs/NOTAS_METODOLOGICAS.md` (Por preencher)
- [ ] Triagem por critérios estritos (o que foi eliminado e porquê)
  - Origem: `src/biomat_mcdm/screening.py` (tarefa 7), `data/criterios.csv` (tipo Estrito)
- [ ] Critérios, tipos, alvos e pesos por caso (Tabela 2)
  - Origem: `data/criterios.csv`, `data/base_dados_biomateriais.xlsx` (folha Criterios)
- [ ] Índices derivados: σy/E do stent (custo, recuo elástico); E_implante/E_osso da haste
  - Origem: `docs/NOTAS_METODOLOGICAS.md`, folha Indices (tarefa 8)
- [ ] Pesos: desvio-padrão e combinação com η (eq. 1 de Petković et al.)
  - Origem: `src/biomat_mcdm/weights.py` (tarefa 5)
- [ ] Métodos: normalização alvo (eq. 2), TOPSIS (2.6), WASPAS (2.7, eqs. 9-16), VIKOR (2.8)
  - Origem: `src/biomat_mcdm/normalization.py`, `src/biomat_mcdm/methods/`
- [ ] Verificação do código: reprodução do caso 2 de Petković et al. 2025
  - Dados do software (Figura A6) em vez da Tabela A3; incoerência M1-C9 (0,41 vs 0,59)
  - Tolerância: 1e-5 (C_i e pesos publicados com 5 casas)
  - Origem: `tests/test_reproduce_petkovic.py`, `docs/NOTAS_METODOLOGICAS.md` (Reprodução de Petković et al. 2025)
- [ ] Cenários de robustez: A, B, Q, W, η, M, T-scaffold, T-haste, MC (10 000 iterações, seed 42), custo com peso baixo vs elevado
  - Origem: `data/base_dados_biomateriais.xlsx` (folha Cenarios), `src/biomat_mcdm/robustness.py` (tarefa 9)
- [ ] Perfis de doente: jovem ativo vs idoso com osteoporose (haste); alergia ao níquel (stent)
  - Origem: `data/perfis.yaml` (tarefa 10)
- [ ] Níveis de validação: verificação de código, robustez interna, validação clínica (não demonstrada)
  - Origem: `docs/NOTAS_METODOLOGICAS.md` (Níveis de validação), folha Cenarios
- [ ] Software e disponibilidade: Python, versões das bibliotecas, repositório e DOI Zenodo
  - Origem: `pyproject.toml`, `CITATION.cff`

## Results
- [ ] Reprodução do caso publicado (Tabela 3 ou suplementar): C_i publicados vs calculados; posições
  - Origem: `tests/test_reproduce_petkovic.py`
- [ ] Triagem: materiais eliminados por caso e motivo
  - Origem: `results/` (tarefa 7)
- [ ] Rankings por caso e método (Figura 3, heatmap)
  - Origem: `results/*.csv` (tarefa 9)
- [ ] Robustez Monte Carlo: % de 1.º lugar por material e caso (Figura 4)
  - Origem: `results/*.csv` (tarefa 9)
- [ ] Sensibilidade a η (Figura 5)
- [ ] Concordância entre métodos (cenário M): correlação de Spearman ou equivalente
- [ ] Sensibilidade dos alvos (T-haste, T-scaffold) e do peso do custo
- [ ] Efeito dos perfis de doente (Figura 6)
  - Origem: `results/` (tarefa 10)
- [ ] Casos semiquantitativos (par articular, implante dentário): resumo em tabela
  - Origem: `relatorio/00_resumo_executivo.md`, `docs/TP2_fisiopatologia_da_falha.md`

## Discussion
- [ ] Resposta direta à pergunta de investigação, caso a caso (robusto vs frágil)
- [ ] Comparação com Petković et al. 2025 e com a prática clínica
- [ ] Reprodutibilidade em MCDM: a reprodução exata só foi possível com os dados da captura do software; incoerência na Tabela A3; importância de publicar dados e código
  - Origem: `docs/NOTAS_METODOLOGICAS.md`, `docs/backlog_artigo.md` (Validação)
- [ ] Casos históricos como validação qualitativa: o modelo teria penalizado estes materiais? (Tabela 4)
  - Origem: `docs/TP2_fisiopatologia_da_falha.md` (Casos históricos de falha e lições de seleção)
  - Absorb: seguir a formulação dos factos verificados em `CLAUDE.md`
- [ ] O que o modelo não captura: processamento, geometria, esterilização, cirurgia
- [ ] % de 1.º lugar no Monte Carlo não é probabilidade de sucesso clínico
  - Origem: `docs/NOTAS_METODOLOGICAS.md`
- [ ] Implicações para quem seleciona materiais (sem recomendações clínicas)

## Limitations
- [ ] Valores de propriedades da literatura, com intervalos largos; estado "A verificar" até verificação
  - Origem: `scripts/listar_por_verificar.py` (tarefa 12)
- [ ] Pesos subjetivos definidos pelo autor, sem painel de especialistas
- [ ] Critérios ordinais (1-5) com julgamento do autor
- [ ] σy/E e E_implante/E_osso são proxies ao nível do material, não do dispositivo
- [ ] Sem FEA nem dados clínicos: validação clínica não demonstrada
- [ ] Perfis de doente simplificados (2), regras com evidência por verificar
- [ ] Reprodução só do caso 2 de Petković et al. e só do TOPSIS até WASPAS e VIKOR estarem implementados

## Conclusions
- [ ] Resposta curta à pergunta de investigação
- [ ] 3 a 4 conclusões numeradas, uma por contribuição
- [ ] Trabalho futuro: itens de `docs/backlog_artigo.md` que ficam para depois
