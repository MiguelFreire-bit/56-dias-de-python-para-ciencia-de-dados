## Dia 14 - Um gráfico para cada pergunta

**Competência principal:** pandas e análise exploratória

**Reforço estatístico:** Distribuição versus evolução temporal; percentuais compostos.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 55 min

**Problema:** Um relatório usa somente um histograma para explicar quando a inflação variou. Você precisa escolher representações adequadas e separar média de acumulação.

**Dados/entrada:** dia_14/ipca_2023_2024.csv, SGS 433/BCB, produtor IBGE; Brasil, jan/2023-dez/2024; data e ipca_pct. Cópia incluída e consulta alternativa: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024

**Tarefa:**
1. Produza linha temporal e histograma com limites de classes declarados.
2. Calcule acumulado por ano por composição de fatores (1+taxa/100), sem usar soma como resultado final; compare com a soma em uma análise separada.

**Entregável esperado:** Dois gráficos, tabela anual e texto distinguindo as perguntas.

**Critérios de conclusão:**
- [ ] Linha usa datas ordenadas e histograma usa os mesmos 24 meses.
- [ ] Acumulado resulta do produto dos fatores, convertido novamente para %.
- [ ] Unidades e limites estão rotulados; não apresenta o histograma como sequência temporal.

**Perguntas de interpretação:**
- Que informação cada gráfico perde?
- Por que uma taxa negativa não torna o fator de composição negativo neste recorte?

**Apoio direcionado:** F, cap. 2; T, pp. 17-21; complemento de composição de taxas.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
