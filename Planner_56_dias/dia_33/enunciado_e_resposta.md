## Dia 33 - Um pipeline mínimo de classificação

**Competência principal:** Machine learning

**Reforço estatístico:** Padronização, probabilidades e avaliação multiclasse.

**Nível de dificuldade:** intermediário | Tempo-alvo: 65 min

**Problema:** Um laboratório quer classificar amostras de vinho em três cultivares usando medidas químicas. Não se trata de prever qualidade ou gosto.

**Dados/entrada:** dia_33/wine.csv; Wine/UCI, 178 amostras, 13 atributos, target 0/1/2 para cultivar, row_id excluído. Fonte: https://archive.ics.uci.edu/dataset/109/wine. Treino/teste 75/25, estratificado, random_state=33. Campos são os nomes de load_wine; unidades variam, não as invente.

**Tarefa:**
1. Ajuste Pipeline(StandardScaler, LogisticRegression(max_iter=2000)) e baseline DummyClassifier(strategy="most_frequent").
2. Avalie acurácia, macro-F1 e matriz de confusão no mesmo teste. Inspecione dois erros, se houver; caso contrário, discuta a limitação do teste pequeno.

**Entregável esperado:** Código, tabela comparativa e interpretação por classe.

**Critérios de conclusão:**
- [ ] Transformações são ajustadas no treino; mesmo split para baseline e modelo.
- [ ] Macro-F1 não é confundido com média ponderada por suporte.
- [ ] Alvo e identificador ficam fora das features e probabilidades por linha somam aproximadamente 1.

**Perguntas de interpretação:**
- Por que padronizar medidas químicas de escalas distintas?
- Uma acurácia alta prova desempenho em qualquer região e safra?

**Apoio direcionado:** F, cap. 13; roadmap E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
