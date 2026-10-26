## Dia 16 - Do evento à distribuição

**Competência principal:** Probabilidade e amostragem

**Reforço estatístico:** Distribuição binomial, frequência e probabilidade.

**Nível de dificuldade:** intermediário | Tempo-alvo: 50 min

**Problema:** Um sistema recebe dez solicitações independentes por lote. Cada uma tem probabilidade fixa de falha de 0,20. Quer-se entender a chance de ocorrerem pelo menos três falhas.

**Dados/entrada:** dia_16/parametros.csv: n=10, p=0,20, 10.000 lotes, seed=160. Gere cada lote como contagem binomial com numpy.random.default_rng; os parâmetros são hipóteses didáticas, não estimativas de produção.

**Tarefa:**
1. Calcule a probabilidade teórica de X>=3 por soma da função de massa ou função de sobrevivência.
2. Simule os lotes, compare a frequência empírica e apresente um gráfico de distribuição.

**Entregável esperado:** Código, probabilidade teórica, estimativa simulada e gráfico.

**Critérios de conclusão:**
- [ ] O evento inclui três falhas e não apenas valores acima de três.
- [ ] Simulação é reproduzível e todas as contagens estão entre 0 e 10.
- [ ] A diferença entre teoria e simulação é quantificada e discutida; não exige igualdade exata.

**Perguntas de interpretação:**
- O que deixa de valer se as falhas ocorrerem em cascata?
- Mais simulações corrigiriam uma hipótese de independência falsa?

**Apoio direcionado:** F, caps. 4-5; G, caps. 4-5.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
