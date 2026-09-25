# biomat-mcdm

Seleção multicritério de biomateriais com **critérios-alvo** e **análise de robustez**, aplicada a quatro classes de dispositivos médicos: prótese da anca (haste e par articular), implante dentário, stent vascular e scaffold para regeneração óssea.

Base metodológica: Petković, Madić & Mitković, *Appl. Sci.* 2025, 15(16), 9198 (doi:10.3390/app15169198). Este projeto estende a abordagem a materiais não metálicos e biodegradáveis e quantifica a robustez dos rankings.

## Pergunta de investigação

A escolha do biomaterial mantém-se quando mudam (i) o método de decisão, (ii) os pesos e (iii) a incerteza nas propriedades?

## Pipeline

```
dados (CSV) → triagem (critérios estritos) → matriz de decisão
           → normalização (benefício / custo / alvo)
           → TOPSIS · WASPAS · VIKOR
           → Monte Carlo sobre [mín, máx] + variação de pesos/η
           → concordância entre rankings (Spearman) → figuras
```

## Estrutura

```
data/                   materiais.csv, criterios.csv (+ .xlsx editável)
src/biomat_mcdm/
  io.py                 leitura dos dados e construção da matriz  [implementado]
  screening.py          triagem por critérios estritos            [TODO]
  normalization.py      normalização benefício/custo/alvo         [TODO]
  weights.py            pesos objetivos e combinação com η         [TODO]
  methods/topsis.py     TOPSIS estendido                           [TODO]
  methods/waspas.py     WASPAS estendido                           [TODO]
  methods/vikor.py      VIKOR abrangente                           [TODO]
  robustness.py         Monte Carlo + Spearman                     [TODO]
  plots.py              figuras para relatório e poster            [TODO]
tests/                  testes = especificação das funções
docs/                   notas metodológicas (viram a secção de Métodos)
results/                rankings e figuras gerados
```

## Como trabalhar

```bash
pip install -e ".[dev]"
pytest -q            # começa a vermelho; implementa até ficar verde
```

Ordem sugerida:
1. `normalization.py` → `pytest tests/test_normalization.py`
2. `methods/topsis.py` → `pytest tests/test_topsis.py`
3. Reproduzir o caso da anca do artigo → `tests/test_reproduce_petkovic.py`
4. `weights.py`, `waspas.py`, `vikor.py`
5. `robustness.py` e `plots.py`

## Estado dos dados

Todos os valores estão marcados **"A verificar"** em `data/materiais.csv`. Nenhum valor entra no relatório/poster sem fonte confirmada (DOI/URL preenchido).

## Autor

André Oliveira Massuça, ORCID [0009-0005-1527-843X](https://orcid.org/0009-0005-1527-843X)
