## Dia 53 - Ferramentas limitadas antes de agentes

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Sem conexão estatística central; roteamento e controle de execução.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 70 min

**Problema:** Um futuro copiloto precisa combinar consulta numérica e documental. O exercício é um roteador determinístico pequeno, preparando os contratos de ferramentas antes de envolver um LLM.

**Dados/entrada:** dia_53/pedidos.csv e os dois CSVs ferramenta_*. Dados: A=120,B=80; documento chave prazo informa 2 dias úteis/fonte D1. Tipo dados chama consulta numérica; documento chama prazo; hibrida chama ambas e usa argumento como grupo. Escrita e outro são proibidos. Falha indica o mock que deve lançar timeout.

**Tarefa:**
1. Implemente funções de leitura e roteador com tipos explícitos, trace de chamadas e máximo de duas ferramentas por pedido.
2. Trate grupo inexistente, timeout e tipo proibido sem executar comandos livres. Em híbrida com falha de dados, devolva resultado parcial identificado, sem inventar total.

**Entregável esperado:** Código, oito resultados e testes de limite/comportamento.

**Critérios de conclusão:**
- [ ] Todos os oito pedidos terminam e respeitam no máximo duas chamadas.
- [ ] Proibidos não acionam ferramenta; fonte documental e número são preservados.
- [ ] Resultado parcial é distinto de sucesso completo; você não apresenta o roteador como sistema multiagente pronto.

**Perguntas de interpretação:**
- Que contrato já pode ser testado antes de conectar um LLM?
- Por que permitir SQL ou código livre muda o risco e o escopo?

**Apoio direcionado:** Roadmap E3 e preparação conceitual para E6.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
