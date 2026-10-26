## Dia 36 - O futuro não pode treinar o passado

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Validação temporal; baseline; erro fora da amostra.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Uma previsão de inflação mensal usa embaralhamento aleatório e parece boa. A tarefa é montar uma avaliação histórica pequena coerente com a informação disponível.

**Dados/entrada:** dia_36/ipca_2023_2024.csv; SGS433/BCB, produtor IBGE, Brasil, 2023-2024; data e ipca_pct. Endpoint: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. Defina X_t=taxa do mês anterior e alvo=taxa do mês t. Janeiro/2023 fica sem lag; o alvo só é previsto após publicação do mês anterior.

**Tarefa:**
1. Treine regressão linear com alvos de fev-dez/2023 e congele coeficientes.
2. Avalie alvos jan-dez/2024 usando o lag real disponível em cada origem e compare com persistência y_hat_t=y_(t-1), por MAE e gráfico. Não ajuste no teste.

**Entregável esperado:** Tabela de 12 previsões, cortes e métricas, com limitações.

**Critérios de conclusão:**
- [ ] Nenhuma feature consulta o próprio alvo ou o mês seguinte.
- [ ] Regressão e persistência usam os mesmos 12 meses de avaliação.
- [ ] A tarefa é reconhecida como previsão um passo adiante com origens sucessivas, não previsão simultânea dos 12 meses.

**Perguntas de interpretação:**
- Por que um split aleatório altera o significado da avaliação?
- Com 11 alvos de treino, o que você pode afirmar com segurança?

**Apoio direcionado:** Roadmap E2; F, cap. 12; complemento temporal.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
