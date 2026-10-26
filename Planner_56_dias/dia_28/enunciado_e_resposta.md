## Dia 28 - Não detectar não é provar ausência

**Competência principal:** Inferência estatística

**Reforço estatístico:** Erro tipo II, poder, tamanho amostral e simulação.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Um estudo pode não detectar uma diferença de um minuto. Você vai medir o comportamento de um teste quando sabe, na simulação, se há efeito.

**Dados/entrada:** dia_28/parametros.csv. Gere amostras normais independentes com sigma=3, mu=10 sob H0 e mu=11 sob H1. Teste t bilateral contra 10, alpha=0,05; n=15 e 60; 1.000 repetições por cenário; seed=280.

**Tarefa:**
1. Estime taxa de rejeição sob H0 e sob H1 para cada n.
2. Interprete as taxas como erro tipo I aproximado e poder; estime beta=1-poder e discuta variação de Monte Carlo.

**Entregável esperado:** Tabela 2x2 de cenários e parecer sobre desenho de estudo.

**Critérios de conclusão:**
- [ ] O teste estima o desvio em cada amostra, sem usar sigma conhecido para trocá-lo por z.
- [ ] Taxas estão baseadas em 1.000 decisões e sementes são registradas.
- [ ] Você explica erro tipo II e não exige que alpha empírico seja exatamente 0,05.

**Perguntas de interpretação:**
- Aumentar n muda o efeito verdadeiro de um minuto?
- Por que um resultado não significativo de amostra pequena é pouco informativo sobre equivalência?

**Apoio direcionado:** F, caps. 6-7; G, caps. 6-7; complemento simulação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
