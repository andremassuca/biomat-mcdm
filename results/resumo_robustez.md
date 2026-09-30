# Resumo da robustez (PRELIMINAR: dados por verificar)

η = 1 no resultado principal; sensibilidades a partir do cenário A. Monte Carlo: 10000 iterações, seed 42. No MC propriedades, as propriedades quantitativas com mín. = máx. variam ±10 % à volta do típico (data/parametros.csv).

## Haste

Vencedor no cenário A: TOPSIS Ti-6Al-4V ELI; WASPAS Ti-6Al-4V ELI; VIKOR Ti-6Al-4V ELI

### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| B | B | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,77 |
| Q | sem ordinais | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,10 |
| η | η = 0,0 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti cp grau 4 | 0,90 |
| η | η = 0,1 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 1,00 |
| η | η = 0,2 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 1,00 |
| η | η = 0,3 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 1,00 |
| η | η = 0,4 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,80 |
| η | η = 0,5 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,80 |
| η | η = 0,6 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,80 |
| η | η = 0,7 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,70 |
| η | η = 0,8 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,40 |
| η | η = 0,9 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,40 |
| η | η = 1,0 | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| T-haste | alvo 14 GPa | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| T-haste | alvo 15 GPa | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| T-haste | alvo 17 GPa | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| T-haste | alvo 20 GPa | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| T-haste | módulo como custo | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,70 |
| C-custo | custo baixo (0,01) | Ti-6Al-4V ELI | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,30 |
| C-custo | custo elevado (0,25) | Aço inox 316L | Ti-6Al-4V ELI | Ti-6Al-4V ELI | 0,60 |

### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Ti-6Al-4V ELI | 100,0 % | 100,0 % | 100,0 % |
| Co-Cr-Mo forjado | 0,0 % | 0,0 % | 0,0 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |
| Ti cp grau 4 | 0,0 % | 0,0 % | 0,0 % |
| Ti-13Nb-13Zr | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Ti-6Al-4V ELI | 100,0 % | 100,0 % | 100,0 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |
| Co-Cr-Mo forjado | 0,0 % | 0,0 % | 0,0 % |
| Ti cp grau 4 | 0,0 % | 0,0 % | 0,0 % |
| Ti-13Nb-13Zr | 0,0 % | 0,0 % | 0,0 % |

### Onde o vencedor muda (face ao cenário A)

- η, η = 0,0, VIKOR: Ti-6Al-4V ELI → Ti cp grau 4
- C-custo, custo elevado (0,25), TOPSIS: Ti-6Al-4V ELI → Aço inox 316L

## Stent

Vencedor no cenário A: TOPSIS Co-Cr L605; WASPAS Co-Cr L605; VIKOR Co-Cr L605

### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| B | B | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| B-bio (comparação) | B-bio | Liga de Mg WE43 (bioabsorvível) | Liga de Mg WE43 (bioabsorvível) | Liga de Mg WE43 (bioabsorvível) | n/a |
| R-sentinela | 60 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| R-sentinela | 120 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| R-sentinela | 600 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| R-sentinela | 1200 meses | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| Q | sem ordinais | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,80 |
| η | η = 0,0 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,80 |
| η | η = 0,1 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,80 |
| η | η = 0,2 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | 0,40 |
| η | η = 0,3 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | -0,20 |
| η | η = 0,4 | Co-Cr L605 | Aço inox 316L | Co-Cr L605 | -0,20 |
| η | η = 0,5 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,20 |
| η | η = 0,6 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,20 |
| η | η = 0,7 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 0,80 |
| η | η = 0,8 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 0,9 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| η | η = 1,0 | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| C-custo | custo baixo (0,01) | Co-Cr L605 | Co-Cr L605 | Co-Cr L605 | 1,00 |
| C-custo | custo elevado (0,25) | Aço inox 316L | Aço inox 316L | Co-Cr L605 | 0,80 |

### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Co-Cr L605 | 79,0 % | 90,8 % | 82,9 % |
| Co-Ni-Cr-Mo MP35N | 11,9 % | 7,3 % | 14,3 % |
| Pt-Cr | 9,2 % | 1,9 % | 2,8 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| Co-Cr L605 | 89,1 % | 100,0 % | 98,3 % |
| Pt-Cr | 10,9 % | 0,0 % | 1,7 % |
| Aço inox 316L | 0,0 % | 0,0 % | 0,0 % |
| Co-Ni-Cr-Mo MP35N | 0,0 % | 0,0 % | 0,0 % |

### Onde o vencedor muda (face ao cenário A)

- η, η = 0,0, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,1, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,2, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,3, WASPAS: Co-Cr L605 → Aço inox 316L
- η, η = 0,4, WASPAS: Co-Cr L605 → Aço inox 316L
- C-custo, custo elevado (0,25), TOPSIS: Co-Cr L605 → Aço inox 316L
- C-custo, custo elevado (0,25), WASPAS: Co-Cr L605 → Aço inox 316L

## Scaffold

Vencedor no cenário A: TOPSIS β-TCP poroso; WASPAS β-TCP poroso; VIKOR β-TCP poroso

### Vencedor por cenário e método

| Cenário | Variante | TOPSIS | WASPAS | VIKOR | ρ mín. entre métodos |
|---|---|---|---|---|---|
| A | A | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| B | B | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,88 |
| Q | sem ordinais | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| η | η = 0,0 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| η | η = 0,1 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,70 |
| η | η = 0,2 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,3 | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 1,00 |
| η | η = 0,4 | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,5 | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,6 | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,7 | β-TCP poroso | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,8 | β-TCP poroso | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| η | η = 0,9 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| η | η = 1,0 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| T-scaffold | Resistência à compressão: 2 | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | 1,00 |
| T-scaffold | Resistência à compressão: 12 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 0,90 |
| T-scaffold | Módulo de compressão: 50 | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | β-TCP poroso | 0,50 |
| T-scaffold | Módulo de compressão: 500 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 0,90 |
| T-scaffold | Porosidade: 50 | β-TCP poroso | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | 0,90 |
| T-scaffold | Porosidade: 90 | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | Vidro bioativo 45S5 poroso | 1,00 |
| T-scaffold | Tempo de degradação: x0,5 | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| T-scaffold | Tempo de degradação: x2,0 | β-TCP poroso | Compósito PCL/β-TCP (impressão 3D) | Compósito PCL/β-TCP (impressão 3D) | 0,80 |
| C-custo | custo baixo (0,01) | β-TCP poroso | β-TCP poroso | β-TCP poroso | 1,00 |
| C-custo | custo elevado (0,25) | Compósito PCL/β-TCP (impressão 3D) | PCL | PCL | 0,70 |

### Monte Carlo: % de 1.º lugar

**MC propriedades**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| β-TCP poroso | 53,6 % | 31,6 % | 37,4 % |
| Vidro bioativo 45S5 poroso | 28,2 % | 23,7 % | 38,8 % |
| Compósito PCL/β-TCP (impressão 3D) | 18,2 % | 43,0 % | 23,8 % |
| PCL | 0,0 % | 1,7 % | 0,0 % |
| Hidroxiapatite (HA) porosa | 0,0 % | 0,0 % | 0,0 % |

**W pesos ±20 %**

| Material | TOPSIS | WASPAS | VIKOR |
|---|---|---|---|
| β-TCP poroso | 91,7 % | 100,0 % | 85,3 % |
| Compósito PCL/β-TCP (impressão 3D) | 8,3 % | 0,0 % | 14,7 % |
| Hidroxiapatite (HA) porosa | 0,0 % | 0,0 % | 0,0 % |
| PCL | 0,0 % | 0,0 % | 0,0 % |
| Vidro bioativo 45S5 poroso | 0,0 % | 0,0 % | 0,0 % |

### Onde o vencedor muda (face ao cenário A)

- B, B, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- B, B, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,0, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,0, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,0, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,1, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,1, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,1, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,2, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,2, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,2, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,3, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,3, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,3, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,4, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,4, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,5, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,5, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,6, TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,6, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,7, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- η, η = 0,8, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Resistência à compressão: 2, TOPSIS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Resistência à compressão: 2, WASPAS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Resistência à compressão: 2, VIKOR: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Módulo de compressão: 50, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Porosidade: 50, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Porosidade: 90, TOPSIS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Porosidade: 90, WASPAS: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Porosidade: 90, VIKOR: β-TCP poroso → Vidro bioativo 45S5 poroso
- T-scaffold, Tempo de degradação: x2,0, WASPAS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- T-scaffold, Tempo de degradação: x2,0, VIKOR: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- C-custo, custo elevado (0,25), TOPSIS: β-TCP poroso → Compósito PCL/β-TCP (impressão 3D)
- C-custo, custo elevado (0,25), WASPAS: β-TCP poroso → PCL
- C-custo, custo elevado (0,25), VIKOR: β-TCP poroso → PCL

## Cenários

- **A**: Só materiais em uso clínico (stent: só permanentes, 316L, L605, MP35N, Pt-Cr)
- **B**: Inclui investigação e bioabsorvíveis (stent: A + Mg WE43 e PLLA; permanentes com o pior valor observado no tempo de reabsorção, opção O2)
- **B-bio**: Só bioabsorvíveis (Mg WE43 e PLLA) com o tempo de reabsorção; comparação, não ranking (opção O3)
- **R-sentinela**: Sensibilidade do tempo de reabsorção atribuído aos permanentes: 60, 120, 600 e 1200 meses (opção O1)
- **Q**: Só critérios quantitativos (sem ordinais)
- **W**: Sensibilidade dos pesos
- **η**: Sensibilidade ao nível de confiança η de 0 a 1, passo 0,1 (resultado principal: η = 1)
- **M**: Concordância entre métodos
- **T-scaffold**: Sensibilidade dos alvos
- **T-haste**: Sensibilidade do alvo de E (inclui 14 GPa, Petković et al. 2025, vs 17 GPa)
- **C-custo**: Peso do custo relativo baixo (0,01) vs elevado (0,25), restantes pesos redistribuídos
- **MC**: Incerteza das propriedades
