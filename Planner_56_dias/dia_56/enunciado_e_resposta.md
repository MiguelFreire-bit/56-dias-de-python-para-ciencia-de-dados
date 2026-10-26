## Dia 56 - Auditoria final: defender uma decisão

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Vazamento temporal; erro, heterogeneidade e limites de evidência.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 80 min

**Problema:** Você recebeu dados oficiais, previsões prontas e metadados. A equipe recomenda o modelo de menor erro. Seu papel é auditar a validade da comparação antes de recomendar qualquer uso.

**Dados/entrada:** dia_56/ipca_2023_2024.csv, dia_56/previsoes_recebidas.csv e metadados.json. IPCA SGS433/BCB, produtor IBGE; Brasil 2023-2024. Fonte alternativa: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. Alvos jan-dez/2024; previsão feita após publicação do mês anterior. Há persistência, regressão linear e modelo_C; leia integralmente os metadados.

**Tarefa:**
1. Audite datas, unidades, chaves, cobertura e informação disponível de cada candidato. Defina elegibilidade antes da ordenação.
2. Escolha uma métrica principal justificada, compare candidatos elegíveis nos mesmos meses e examine erros por semestre. Produza um gráfico e recomendação com limites; não treine nem ajuste no teste.

**Entregável esperado:** Relatório independente de até 500 palavras, código de auditoria, tabela de erros e gráfico.

**Critérios de conclusão:**
- [ ] As 12 datas de previsão conciliam por chave com o observado; nenhuma junção posicional silenciosa.
- [ ] A decisão distingue erro baixo de protocolo válido; cada exclusão possui evidência dos metadados.
- [ ] A avaliação não usa os 12 meses como se fossem amostra i.i.d. para um IC ingênuo e não declara causalidade.
- [ ] O relatório registra recomendação, incerteza e próximo teste; um resultado desfavorável ao modelo complexo é aceitável.

**Perguntas de interpretação:**
- Qual resultado aparente você rejeitaria por invalidade do procedimento?
- O que você consegue defender agora e o que precisaria observar em um período novo?

**Apoio direcionado:** Roadmap E1-E3/E7; F, cap. 12; complemento auditoria temporal.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
