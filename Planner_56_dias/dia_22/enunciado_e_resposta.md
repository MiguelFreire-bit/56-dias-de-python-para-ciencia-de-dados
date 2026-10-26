## Dia 22 - Um intervalo para a média

**Competência principal:** Inferência estatística

**Reforço estatístico:** Intervalo t; estimativa pontual, erro padrão e confiança.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Uma fábrica sorteou 12 embalagens independentes de um processo estável aproximadamente normal. O desvio padrão populacional é desconhecido.

**Dados/entrada:** dia_22/pesos.csv; pesos em gramas. Construa intervalo bilateral de 95% para a média com t de Student, n-1 graus de liberdade. Não confunda especificação de 500 g com observação adicional.

**Tarefa:**
1. Calcule média, desvio amostral, erro padrão, valor crítico e intervalo t.
2. Confira com SciPy e compare a largura com um intervalo de 90% para os mesmos dados.

**Entregável esperado:** Memória das componentes e tabela de dois intervalos.

**Critérios de conclusão:**
- [ ] Usa ddof=1 e erro padrão s/sqrt(n).
- [ ] Limites calculados manualmente e pela biblioteca coincidem até 1e-6.
- [ ] Confiança é interpretada como propriedade do procedimento em repetições, com hipóteses indicadas.

**Perguntas de interpretação:**
- Maior confiança altera a média observada?
- O intervalo descreve 95% dos pesos individuais?

**Apoio direcionado:** F, cap. 6; G, cap. 6.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
