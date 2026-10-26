## Dia 27 - Dez chances de anunciar uma descoberta

**Competência principal:** Inferência estatística

**Reforço estatístico:** Erro tipo I, família de testes e Bonferroni.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Dez métricas primárias foram testadas no mesmo experimento. Todos os p-valores fornecidos são de testes válidos individualmente. O relatório quer destacar qualquer p<0,05 sem discutir multiplicidade.

**Dados/entrada:** dia_27/testes.csv; dez p-valores. Família definida: todos os dez testes; alpha familiar=0,05. Para calcular a probabilidade teórica de ao menos um falso positivo, suponha separadamente dez testes independentes sob H0 verdadeira.

**Tarefa:**
1. Compare decisões sem correção com Bonferroni (alpha/10) e calcule p ajustado limitado a 1.
2. Calcule 1-(1-alpha)^10 no cenário teórico e explique onde a independência foi usada.

**Entregável esperado:** Tabela de decisões e crítica do relatório.

**Critérios de conclusão:**
- [ ] Número de testes da família permanece dez, incluindo resultados não significativos.
- [ ] Ajustes não produzem p>1 e o limiar foi definido para a família inteira.
- [ ] O texto distingue controle familiar, alpha por teste e probabilidade posterior de erro de uma descoberta.

**Perguntas de interpretação:**
- Selecionar só os testes significativos antes de corrigir seria válido?
- Qual custo de poder pode acompanhar uma correção conservadora?

**Apoio direcionado:** F, cap. 7; complemento sobre multiplicidade.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
