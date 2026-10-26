## Dia 52 - Monitorar sem esconder as falhas

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Mediana, P95, denominadores e viés por sobrevivência.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 65 min

**Problema:** Um serviço anuncia latência média apenas nas respostas bem-sucedidas. Você deve construir um resumo operacional que também represente erros e cauda de latência.

**Dados/entrada:** dia_52/logs.csv; 20 requisições; latência observada de cada tentativa em ms, inclusive timeout de 1.000 ms; tokens faturados somente conforme a coluna. Meta didática: falhas<=5% e P95 das respostas ok<=500 ms. Quantis lineares; custo R$0,01/1.000 tokens.

**Tarefa:**
1. Calcule sucesso/falha sobre todas as tentativas; compare média, mediana e P95 para sucessos e para todas as tentativas.
2. Avalie as duas metas, calcule custo total e por resposta bem-sucedida, e recomende uma investigação prioritária.

**Entregável esperado:** Painel tabular, uma visualização e parecer operacional.

**Critérios de conclusão:**
- [ ] Falhas incluem timeout e erro; denominador é 20.
- [ ] P95 declara subconjunto e convenção; custo não descarta tokens de falhas caso existissem.
- [ ] Relatório não transforma observação de timeout em latência real de processamento após o corte.

**Perguntas de interpretação:**
- Por que excluir timeout pode melhorar artificialmente a aparência do serviço?
- Uma média baixa assegura boa experiência para quem está na cauda?

**Apoio direcionado:** F, cap. 2; roadmap E7.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
