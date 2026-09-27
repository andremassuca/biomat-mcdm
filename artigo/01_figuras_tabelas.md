# Plano de figuras e tabelas

Colunas R e P: serve também o relatório (R) e o poster (P). Figuras em `results/figures/`
(PNG 300 dpi e SVG, tarefa 11). Nada aqui está feito, exceto onde indicado.

## Figuras

| N.º | Figura | O que mostra | Dados de origem | R | P |
|---|---|---|---|---|---|
| F1 | Fluxograma do método | Dados → triagem estrita → índices derivados → pesos (η) → TOPSIS/WASPAS/VIKOR → robustez → perfis | `docs/NOTAS_METODOLOGICAS.md`, `src/` | sim | sim |
| F2 | Mapa mecanismo de falha → propriedade → critério | Para cada caso, ligação entre falha clínica, propriedade do material e critério do modelo | `docs/TP2_fisiopatologia_da_falha.md`, `data/criterios.csv` | sim | sim |
| F3 | Rankings por caso e método (heatmap) | Posição de cada material × método (TOPSIS, WASPAS, VIKOR), um painel por caso | `results/*.csv` (tarefa 9), `src/biomat_mcdm/plots.py` | sim | sim |
| F4 | Robustez Monte Carlo | % de 1.º lugar por material, por caso (10 000 iterações, seed 42) | `results/*.csv` (tarefa 9) | sim | sim |
| F5 | Sensibilidade a η | Posição ou C de cada material para η = 0,7; 0,8; 0,9; 1 | `results/*.csv` (tarefa 9) | sim | talvez |
| F6 | Efeito dos perfis de doente | Ranking de referência vs perfil (haste: jovem ativo vs idoso com osteoporose; stent: alergia ao níquel) | `data/perfis.yaml`, `results/` (tarefa 10) | sim | sim |
| F7 (suplementar) | TOPSIS preliminar da haste, cenários A e B | C por material | `results/figures/topsis_haste_preliminar.png` (feito, PRELIMINAR) | reunião | não |

## Tabelas

| N.º | Tabela | O que mostra | Dados de origem | R | P |
|---|---|---|---|---|---|
| T1 | Materiais e propriedades com fontes | Material, classe, estatuto clínico, propriedades (mín./máx.), referência, estado de verificação | `data/materiais.csv`, `data/base_dados_biomateriais.xlsx` (Materiais) | sim | resumida |
| T2 | Critérios, tipos, alvos e pesos | Por caso: critério, tipo (benefício/custo/alvo/estrito), alvo, peso, justificação | `data/criterios.csv`, `docs/NOTAS_METODOLOGICAS.md` | sim | resumida |
| T3 | Reprodução do caso publicado | Petković et al. 2025, caso 2: C_i publicados vs calculados, posições, nota sobre M1-C9 | `tests/test_reproduce_petkovic.py`, `docs/NOTAS_METODOLOGICAS.md` | sim | 1 linha (validação) |
| T4 | Casos históricos | Período, material, o que falhou, critério que teria alertado, o que o modelo não captura | `docs/TP2_fisiopatologia_da_falha.md` (Casos históricos) | sim | talvez |
| T5 | Cenários de robustez | Código, descrição, casos a que se aplica | `data/base_dados_biomateriais.xlsx` (Cenarios) | sim | não |
| T6 | Triagem | Materiais eliminados por critério estrito e motivo | `results/` (tarefa 7) | sim | não |
| T7 | Casos semiquantitativos | Par articular e implante dentário: critérios qualitativos e resultado | `relatorio/00_resumo_executivo.md` | sim | não |

## Notas
- Sem valores "A verificar" em figuras finais sem o aviso "PRELIMINAR: dados por verificar".
- Decimais com vírgula no relatório e poster; ponto no artigo em inglês.
- Poster em A0: rever tamanho mínimo de letra das figuras F3, F4 e F6.
