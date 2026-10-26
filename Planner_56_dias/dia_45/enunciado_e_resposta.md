## Dia 45 - Acertar um trecho não é recuperar todos

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Hit@k, Recall@k, Precision@k e denominadores.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Duas buscas têm rankings prontos. A equipe chama todas as métricas de “acurácia do RAG”, incluindo uma pergunta sem resposta no acervo.

**Dados/entrada:** dia_45/ranking.csv; IDs separados por ponto e vírgula. Relevantes são conjunto de referência; Q4 não tem nenhum documento relevante. k=3. Hit@3=1 se algum relevante foi recuperado. Recall=recuperados relevantes/total relevante; Precision=recuperados relevantes/3.

**Tarefa:**
1. Calcule as três métricas por pergunta respondível e média macro nas Q1-Q3.
2. Para Q4 registre que recall é indefinido e não a inclua no macro de respondíveis; discuta separadamente por que a busca ainda retorna candidatos.

**Entregável esperado:** Tabela por pergunta, resumo por sistema e explicação dos denominadores.

**Critérios de conclusão:**
- [ ] Interseções tratam IDs como conjuntos, sem duplicar evidência.
- [ ] Hit e recall não são confundidos quando há mais de um relevante.
- [ ] Q4 não recebe recall zero silenciosamente nem vira prova de que o sistema sabe recusar resposta.

**Perguntas de interpretação:**
- Bom Hit@3 garante que a resposta gerada seja correta?
- Que métrica ajuda quando a resposta exige dois documentos?

**Apoio direcionado:** Roadmap E5; complemento métricas de recuperação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
