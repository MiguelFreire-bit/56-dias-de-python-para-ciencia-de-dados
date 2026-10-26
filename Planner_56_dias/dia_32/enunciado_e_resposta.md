## Dia 32 - Aprender a separar antes de transformar

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Vazamento de dados; separação treino/teste.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Uma equipe padroniza todos os dados antes de separar treino e teste. Você vai comparar esse fluxo com uma separação correta e explicar o problema mesmo se as métricas ficarem parecidas.

**Dados/entrada:** dia_32/iris.csv; Iris/UCI, 150 plantas, quatro medidas em cm e target 0=setosa, 1=versicolor, 2=virginica; row_id é identificador, excluído dos atributos. Fonte: https://archive.ics.uci.edu/dataset/53/iris. Cópia do load_iris do scikit-learn incluída.

**Tarefa:**
1. Separe 70/30 com stratify=target e random_state=32. Compare StandardScaler ajustado em tudo versus somente no treino, seguido de KNN k=5.
2. Inspecione médias de ajuste do scaler e acurácia; marque o fluxo global como demonstração de erro, sem recomendá-lo.

**Entregável esperado:** Dois fluxos identificados, métricas e diagnóstico.

**Critérios de conclusão:**
- [ ] Não inclui row_id nem target em X.
- [ ] No fluxo correto, fit do scaler e do modelo acessa apenas treino; teste só usa transform/predict.
- [ ] Você reconhece vazamento como falha de procedimento mesmo sem aumento de acurácia.

**Perguntas de interpretação:**
- Por que resultado semelhante não valida o fluxo errado?
- Como Pipeline ajudaria quando a separação é por folds?

**Apoio direcionado:** Roadmap E2; complemento de avaliação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
