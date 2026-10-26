## Dia 50 - O agregado esconde quem recebe o erro

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Métricas condicionais, prevalência e tamanho de grupo.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 65 min

**Problema:** Um classificador de necessidade de suporte atende usuários de app e web. O relatório usa só uma métrica global. Os canais têm tamanhos e prevalências diferentes.

**Dados/entrada:** dia_50/segmentos.csv; cada linha é célula de confusão com frequência n. Classe positiva=precisa de suporte; sem pessoa duplicada. Nenhum canal é amostra representativa de todos os usuários futuros por garantia.

**Tarefa:**
1. Escolha e calcule métricas globais e por canal, incluindo obrigatoriamente recall, taxa de falsos positivos e suporte de classe.
2. Recomende uma investigação antes de mudar limiares ou prometer equidade; justifique os denominadores e a influência do grupo menor.

**Entregável esperado:** Tabela estratificada, visualização escolhida e parecer de até 250 palavras.

**Critérios de conclusão:**
- [ ] Células usam n como peso e totais conciliam com o agregado.
- [ ] Recall e FPR usam denominadores diferentes corretamente.
- [ ] O parecer distingue diferença observada, incerteza por grupo e causas não demonstradas; não resolve o problema apenas igualando taxas.

**Perguntas de interpretação:**
- Uma boa taxa global assegura bom atendimento em cada canal?
- Qual informação faltaria para explicar por que os erros diferem?

**Apoio direcionado:** F, caps. 3 e 13; roadmap E2/E7; complemento avaliação por segmento.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
