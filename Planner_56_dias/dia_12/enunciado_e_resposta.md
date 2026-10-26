## Dia 12 - Um JOIN que não inventa clientes

**Competência principal:** SQL

**Reforço estatístico:** Granularidade e denominadores após junções.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 55 min

**Problema:** Um gestor quer o número de clientes e o valor de pedidos por cidade. Uma junção ingênua conta várias vezes o mesmo cliente e oculta pedidos sem cadastro.

**Dados/entrada:** dia_12/clientes.csv e dia_12/pedidos.csv. Clientes: C1/Recife, C2/Natal, C3/Recife, C4/Olinda. Pedidos: P1/C1/100, P2/C1/50, P3/C2/80, P4/C9/20. Use SQLite; C9 não existe no cadastro.

**Tarefa:**
1. Crie as duas tabelas; use LEFT JOIN para preservar clientes sem pedido.
2. Entregue valor e clientes distintos por cidade e uma consulta separada de pedidos órfãos. Confira o total de pedidos antes e depois de cada relação.

**Entregável esperado:** Duas consultas SQL, tabelas de saída e explicação da granularidade.

**Critérios de conclusão:**
- [ ] O cliente sem pedido aparece com valor zero somente na agregação de pedidos, sem criar pedido fictício.
- [ ] Clientes distintos são contados pela chave; o pedido órfão é explicitamente auditado.
- [ ] A soma dos valores associados mais os órfãos reconcilia com todos os pedidos.

**Perguntas de interpretação:**
- Por que COUNT(*) depois de JOIN não é necessariamente número de clientes?
- Quando um INNER JOIN esconderia um problema de qualidade?

**Apoio direcionado:** Roadmap E1, C08-C09; complemento SQL.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
