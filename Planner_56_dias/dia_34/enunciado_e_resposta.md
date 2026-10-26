## Dia 34 - Complexidade e overfitting

**Competência principal:** Machine learning

**Reforço estatístico:** Viés, variância e desempenho de treino/validação.

**Nível de dificuldade:** intermediário | Tempo-alvo: 65 min

**Problema:** Uma árvore profunda consegue memorizar amostras pequenas. Você deve escolher complexidade antes de observar o teste final.

**Dados/entrada:** dia_34/iris.csv; Iris/UCI, 150 plantas, quatro atributos em cm e target 0/1/2; row_id excluído. Fonte: https://archive.ics.uci.edu/dataset/53/iris. Primeiro reserve 20% de teste estratificado (seed=34); no restante reserve 25% para validação (seed=35).

**Tarefa:**
1. Compare DecisionTreeClassifier com max_depth=1,2,4,None (random_state=34), usando somente treino e validação.
2. Escolha por macro-F1 de validação; empate até 1e-12 favorece menor profundidade. Reajuste no desenvolvimento completo e avalie uma vez no teste.

**Entregável esperado:** Curva/tabela de complexidade e registro da escolha antes do teste.

**Critérios de conclusão:**
- [ ] Teste não participa da escolha; índices dos três subconjuntos não se sobrepõem.
- [ ] Há métricas de treino e validação para quatro profundidades e somente um resultado final de teste.
- [ ] Você discute overfitting sem exigir que uma árvore específica necessariamente perca.

**Perguntas de interpretação:**
- Maior pontuação de treino equivale a melhor modelo?
- Como o tamanho pequeno da validação afeta a escolha?

**Apoio direcionado:** Roadmap E2; complemento viés/variância.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
