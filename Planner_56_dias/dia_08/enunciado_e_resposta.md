## Dia 8 - Primeira análise de uma série oficial

**Competência principal:** pandas e análise exploratória

**Reforço estatístico:** Distribuição, tendência central e dispersão.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 45 min

**Problema:** Um relatório quer comparar o comportamento da inflação mensal em dois anos, sem confundir variação mensal com inflação acumulada.

**Dados/entrada:** dia_08/ipca_2023_2024.csv: SGS 433, IPCA, produzido pelo IBGE e distribuído pelo BCB. Brasil; jan/2023-dez/2024; 24 meses; data e ipca_pct (variação percentual mensal). Use a cópia fornecida. Consulta alternativa: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024

**Tarefa:**
1. Converta datas e valores, valide a grade mensal e separe os dois anos.
2. Calcule média, mediana, mínimo, máximo e desvio padrão descritivo (ddof=0) por ano. Escreva uma comparação sem inferência populacional.

**Entregável esperado:** Tabela anual, verificações e interpretação de até oito linhas.

**Critérios de conclusão:**
- [ ] Há 12 observações por ano, meses únicos e valores numéricos.
- [ ] Percentuais mensais são identificados como taxas, sem soma ou média chamada de acumulado anual.
- [ ] A interpretação considera centro e dispersão e não atribui causa a mudanças.

**Perguntas de interpretação:**
- O que significa uma taxa mensal negativa?
- A média mensal responde à mesma pergunta que o acumulado anual?

**Apoio direcionado:** F, cap. 2; T, pp. 13-16.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
