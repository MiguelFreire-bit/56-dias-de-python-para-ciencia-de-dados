## Dia 30 - Resíduo não é só número que sobra

**Competência principal:** Machine learning

**Reforço estatístico:** Padrão residual; especificação; comparação com baseline.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** O tempo de resposta cresce com a quantidade de usuários. Um ajuste linear pode ter bom R² e ainda deixar estrutura nos erros.

**Dados/entrada:** dia_30/carga.csv; 12 níveis de usuários e tempos em ms. Treine somente usuários 1-8; avalie usuários 9-12. Compare reta com polinômio de grau 2 e baseline constante igual à média de treino. É extrapolação didática, não amostra aleatória.

**Tarefa:**
1. Ajuste os três métodos sem usar os quatro últimos alvos no treino.
2. Compare MAE de treino e avaliação; examine resíduos contra usuários e justifique qual modelo parece adequado e quais riscos permanecem.

**Entregável esperado:** Tabela de erros, gráfico residual e recomendação limitada ao experimento.

**Critérios de conclusão:**
- [ ] Mesmo recorte de treino e avaliação para todos os métodos.
- [ ] Baseline calcula sua média apenas no treino; transformação polinomial não usa alvo de avaliação.
- [ ] A recomendação usa padrão residual e extrapolação, sem escolher só o maior R² de treino.

**Perguntas de interpretação:**
- Um resíduo médio próximo de zero garante especificação adequada?
- Por que quatro casos de avaliação não sustentam conclusão definitiva?

**Apoio direcionado:** F, cap. 12; complemento validação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
