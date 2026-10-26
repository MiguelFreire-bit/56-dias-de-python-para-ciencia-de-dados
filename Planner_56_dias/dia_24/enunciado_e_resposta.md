## Dia 24 - Comparar duas médias com hipóteses claras

**Competência principal:** Inferência estatística

**Reforço estatístico:** Teste de Welch; diferença de médias e incerteza.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Pessoas foram alocadas aleatoriamente a duas interfaces e medidas uma vez. Deseja-se comparar tempo médio de tarefa, sem presumir variâncias iguais. Os tempos são aproximadamente normais em cada população.

**Dados/entrada:** dia_24/grupos.csv; A tem 8 pessoas e B tem 10, sem pareamento. H0:mu_A-mu_B=0, bilateral, alpha=0,05. Efeito relevante foi definido como redução de pelo menos 2 minutos.

**Tarefa:**
1. Calcule resumos, teste t de Welch e diferença A-B.
2. Construa IC95% de Welch usando erro padrão sqrt(sA²/nA+sB²/nB) e graus de liberdade de Welch-Satterthwaite; consulte documentação para a fórmula.

**Entregável esperado:** Tabela, teste, intervalo e decisão separando evidência e relevância.

**Critérios de conclusão:**
- [ ] Observações independentes não são tratadas como pares.
- [ ] Variâncias são amostrais e não são forçadas a ser iguais.
- [ ] O sinal da diferença é consistente e a conclusão considera a margem prática de 2 minutos e a incerteza.

**Perguntas de interpretação:**
- Precisamos de um teste de normalidade para autorizar automaticamente o método?
- Que resultado adicional ajudaria se a amostra fosse muito assimétrica?

**Apoio direcionado:** F, cap. 7; B, caps. 6 e 12. Leitura crítica de pressupostos.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
