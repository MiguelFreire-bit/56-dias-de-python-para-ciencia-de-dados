## Dia 42 - Diagnosticar uma média no serviço

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Média por unidade de análise; zeros e ausência.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Uma API promete gasto médio por cliente cadastrado, incluindo clientes sem compra. A consulta existente calcula AVG(p.valor) após INNER JOIN. Você precisa corrigir o resultado e proteger o contrato.

**Dados/entrada:** dia_42/pedidos.csv, dia_42/clientes.csv e dia_42/consulta_com_erro.sql. Cadastros A/Norte, B/Sul, C/Sul; pedidos A/10,A/20,B/30. Todos os pedidos do período estão presentes; sem pedido significa gasto zero neste período.

**Tarefa:**
1. Identifique os dois problemas de granularidade/cobertura e escreva consulta correta.
2. Implemente uma função de serviço local que recebe a região e devolve clientes e média; região inexistente deve produzir erro explícito, não média zero. Teste ambos os grupos e o caso inexistente.

**Entregável esperado:** SQL corrigido, função, testes e explicação.

**Critérios de conclusão:**
- [ ] Agrega primeiro por cliente e inclui cadastrados sem pedido.
- [ ] Contagem de clientes usa cadastro, sem inflação por pedidos.
- [ ] Região inexistente é diferente de clientes existentes com gasto zero; testes capturam a diferença.

**Perguntas de interpretação:**
- Qual diferença entre média por pedido e por cliente?
- Por que aqui zero é adequado para ausência de pedido, mas nem toda ausência deve virar zero?

**Apoio direcionado:** Roadmap E1 e E3; F, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
