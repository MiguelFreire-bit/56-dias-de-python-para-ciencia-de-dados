## Dia 35 - Validação cruzada também tem limites

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Variação entre folds; seleção e teste reservado.

**Nível de dificuldade:** intermediário | Tempo-alvo: 65 min

**Problema:** Uma equipe anuncia a melhor média de validação como se fosse uma avaliação final independente. Você deve distinguir seleção de hiperparâmetro e teste.

**Dados/entrada:** dia_35/wine.csv; Wine/UCI; 178 casos, 13 atributos, target 0/1/2, sem row_id em X. Fonte: https://archive.ics.uci.edu/dataset/109/wine. Reserve 25% teste estratificado, seed=35; no desenvolvimento use StratifiedKFold(5,shuffle=True,random_state=35).

**Tarefa:**
1. Compare Pipeline de padronização + KNN com k=3,5,9 nos mesmos folds, por macro-F1.
2. Escolha maior média; empate até 1e-12 favorece maior k. Ajuste no desenvolvimento e avalie uma vez no teste. Reporte os cinco valores e o desvio, sem tratá-los como observações independentes.

**Entregável esperado:** Tabela por fold, regra registrada e resultado final.

**Critérios de conclusão:**
- [ ] Scaler é reajustado dentro de cada fold, via Pipeline.
- [ ] Teste permanece separado da busca.
- [ ] Desvio entre folds é descrição de estabilidade, não IC95% automático da generalização.

**Perguntas de interpretação:**
- Por que escolher o melhor k e reportar apenas sua CV pode ser otimista?
- Repetir splits até melhorar o teste mantém o teste reservado?

**Apoio direcionado:** Roadmap E2; complemento validação cruzada.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
