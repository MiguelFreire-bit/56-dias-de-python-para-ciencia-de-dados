## Dia 55 - Receber um problema e escolher um caminho

**Competência principal:** Machine learning

**Reforço estatístico:** Escolha de métrica; validação; estabilidade e interpretação.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 80 min

**Problema:** Um laboratório recebe um lote de medidas químicas e quer uma prova de conceito reproduzível para distinguir cultivares. Você define a abordagem, respeitando um orçamento pequeno de comparação.

**Dados/entrada:** dia_55/wine.csv; Wine/UCI, 178 amostras, 13 atributos químicos, target 0/1/2, row_id excluído. Fonte: https://archive.ics.uci.edu/dataset/109/wine. Reserve 25% teste estratificado com seed=55. Limite: baseline + no máximo dois tipos de modelo, até três configurações por tipo; sem dados externos.

**Tarefa:**
1. Defina métrica principal e protocolo antes de medir; faça diagnóstico curto, prepare dados e compare no desenvolvimento com CV estratificada de 4 folds (shuffle=True,seed=55).
2. Congele a escolha e avalie uma única vez no teste; reporte por classe, limitações e uma melhoria ligada a falha observada.

**Entregável esperado:** Notebook/script reexecutável e relatório de até 400 palavras.

**Critérios de conclusão:**
- [ ] O procedimento justifica métrica, transformação e escolha; alvo e ID não vazam.
- [ ] Transformações são internas ao Pipeline/CV, e teste permanece fora da busca.
- [ ] Há baseline, métricas por classe e análise honesta; não precisa superar uma meta artificial para concluir.
- [ ] Tempo de treino é limitado: não amplia a busca para perseguir resultado de teste.

**Perguntas de interpretação:**
- Que decisão foi sustentada pelos dados e qual ainda depende de hipótese?
- Como você demonstraria que a execução é reproduzível em outro ambiente?

**Apoio direcionado:** F, cap. 13; roadmap E1-E3; complemento validação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
