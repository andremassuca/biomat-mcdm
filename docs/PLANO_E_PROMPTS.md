# Plano e prompts

> Nota: a versão completa deste ficheiro ficou no portátil. Esta cópia contém só a
> secção da app interativa, atualizada a 27 set 2026. Integrar com o original quando
> o André o trouxer.

## App interativa (poster)

**Tipo:** aplicação de computador para Windows, que abre numa janela e corre localmente,
sem internet. Não é um site.

### Tecnologia
- Python + PySide6 (Qt), com gráficos matplotlib embebidos.
- Empacotamento com PyInstaller num `.exe` em `D:\LAB\biomat-mcdm\dist`
  (`dist/` e `build/` no `.gitignore`).
- Distribuição pelo GitHub Releases. Não precisa de alojamento nem de repositório público.

### Ecrãs
1. Escolher o caso (haste, stent, scaffold) e ver a tabela de materiais.
2. Pesos e η em barras deslizantes; ranking e gráfico atualizados em tempo real
   para TOPSIS, WASPAS e VIKOR.
3. Botão para correr o Monte Carlo e mostrar a % de 1.º lugar.
4. Escolher o perfil de doente e ver o efeito.
5. Exportar o gráfico em PNG.

### Regras
- Só começa depois de 8 out 2026.
- O poster tem prioridade: se a 12 out o poster não estiver desenhado, a app fica para depois.
- Usa exatamente as funções de `src/`, sem lógica duplicada.
- Uso nas BioJornadas com o portátil na banca; o QR code do poster aponta para o
  repositório ou para a release.

### Preparação desde já (sem código da app)
- Manter as funções de `src/` puras e rápidas.
- Um ponto de entrada por caso, que sirva tanto o `scripts/run_all.py` como a app.
- Monte Carlo com número de iterações configurável (10 000 para os resultados;
  uma versão rápida para a app).
