## Dia 37 - Acurácia alta pode esconder falhas

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Matriz de confusão, precisão, recall e prevalência.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 55 min

**Problema:** Um sistema detecta fraude fictícia rara. Dois classificadores já produziram previsões; não é necessário treiná-los. A equipe anuncia somente acurácia.

**Dados/entrada:** dia_37/alertas.csv; contagens de grupos de eventos disjuntos. Classe positiva=fraude (1); negativos=0. A é constante zero; B varia conforme a coluna. Trate quantidade como peso de frequência, total de 100 eventos.

**Tarefa:**
1. Construa matrizes ponderadas de cada modelo e calcule acurácia, precisão, recall e F1.
2. Adote convenção precision=0 quando não há predição positiva, declarando a divisão sem denominador e a convenção. Compare com o objetivo de encontrar fraudes.

**Entregável esperado:** Tabela de métricas e crítica do anúncio.

**Critérios de conclusão:**
- [ ] Contagens ponderam quantidade, não só as quatro linhas agregadas.
- [ ] Classe positiva e convenção de divisão indefinida são explícitas.
- [ ] A conclusão informa prevalência e não interpreta precisão como recall.

**Perguntas de interpretação:**
- Por que prever sempre negativo pode ter boa acurácia?
- Qual métrica responde à fração dos alertas que é fraude?

**Apoio direcionado:** F, cap. 13; roadmap E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
