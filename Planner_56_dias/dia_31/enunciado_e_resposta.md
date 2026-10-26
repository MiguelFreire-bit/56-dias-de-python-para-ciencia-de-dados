## Dia 31 - A métrica muda a preferência

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** MAE, RMSE, erro quadrático e influência de extremos.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Dois modelos têm previsões prontas para os mesmos seis pedidos. Não há treino neste exercício; o foco é escolher o critério que corresponde ao custo do erro.

**Dados/entrada:** dia_31/previsoes.csv; real, modelo_A, modelo_B em unidades vendidas. Cenário 1: cada unidade de erro absoluto custa igual. Cenário 2: grandes erros recebem custo proporcional ao quadrado do erro.

**Tarefa:**
1. Calcule erro assinado, absoluto e quadrático por caso; depois MAE e RMSE.
2. Faça análise de sensibilidade removendo o último caso somente da comparação adicional, preservando o resultado principal.

**Entregável esperado:** Tabela por caso, resumo por modelo e escolha nos dois cenários.

**Critérios de conclusão:**
- [ ] Ambos usam os mesmos seis casos na comparação principal.
- [ ] RMSE aplica raiz à média dos quadrados, não à soma.
- [ ] A decisão conecta métrica e custo; a sensibilidade não é usada para apagar resultado inconveniente.

**Perguntas de interpretação:**
- Por que não existe uma métrica universalmente melhor?
- Qual risco há em excluir o caso mais difícil após ver quem perde?

**Apoio direcionado:** F, cap. 12; roadmap E2; complemento métricas.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
