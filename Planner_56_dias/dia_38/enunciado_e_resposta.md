## Dia 38 - Escolher o limiar pelo custo

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Decisão probabilística; custo esperado empírico.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Uma análise atribui custo 1 a falso positivo e custo 5 a falso negativo. Você recebe scores de validação e deve escolher um limiar sem acessar um teste.

**Dados/entrada:** dia_38/validacao.csv; 12 casos independentes fictícios de validação, real em 0/1 e score em [0,1]. Candidatos: 0,2;0,4;0,6;0,8. Prediga positivo se score>=limiar. Custo total=FP+5*FN. Não há conjunto de teste nesta atividade.

**Tarefa:**
1. Calcule matriz, custo total, precisão e recall para os quatro limiares.
2. Escolha menor custo; empate favorece limiar maior. Explique que a estimativa de desempenho final ainda falta.

**Entregável esperado:** Tabela de trade-offs e regra de decisão documentada.

**Critérios de conclusão:**
- [ ] Convenção >= é aplicada também nos valores de fronteira.
- [ ] A regra usa somente validação; custos são aplicados às contagens corretas.
- [ ] Você não chama scores de probabilidades calibradas sem evidência e não chama o custo escolhido de resultado final de teste.

**Perguntas de interpretação:**
- Mudar o custo dos falsos negativos pode mudar o limiar?
- Como uma prevalência diferente em produção afetaria essa decisão?

**Apoio direcionado:** F, cap. 13; complemento seleção de limiar.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
