## Dia 39 - Comparar modelos preservando os pares

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Bootstrap pareado; intervalo da diferença de erros.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Dois modelos foram avaliados nos mesmos 12 casos independentes, sorteados da população de interesse. A diferença entre as médias de erro precisa ser acompanhada de incerteza.

**Dados/entrada:** dia_39/erros.csv; erros absolutos já calculados, mesma unidade para A e B. Delta=MAE_A-MAE_B. Bootstrap pareado: 5.000 reamostras de índices dos 12 casos, seed=390, IC percentil95%.

**Tarefa:**
1. Calcule delta e intervalo reamostrando casos inteiros, preservando A/B.
2. Compare a conclusão com a simples ordenação das médias e indique o que mudaria se os casos fossem dias consecutivos dependentes.

**Entregável esperado:** Estimativa, intervalo e parecer sobre força da comparação.

**Critérios de conclusão:**
- [ ] Uma mesma seleção de índices é aplicada às duas colunas em cada reamostra.
- [ ] Unidade de análise é o caso e o sinal de delta é explicado.
- [ ] Você discute incerteza, dependência e amostra pequena; não força superioridade quando o resultado não sustenta.

**Perguntas de interpretação:**
- Por que reamostrar A e B separadamente perde informação?
- Um intervalo que inclui zero prova equivalência?

**Apoio direcionado:** F, caps. 6-7; complemento bootstrap pareado.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
