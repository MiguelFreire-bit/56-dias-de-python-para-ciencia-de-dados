## Dia 6 - Limpar preservando o que aconteceu

**Competência principal:** Limpeza e qualidade de dados

**Reforço estatístico:** Ausência e efeito do tratamento em estatísticas.

**Nível de dificuldade:** básico | Tempo-alvo: 45 min

**Problema:** Uma exportação de pedidos mistura vírgula decimal, duplicação exata, ausência e quantidade impossível. Zero é quantidade válida; quantidade negativa é inválida neste cadastro de vendas.

**Dados/entrada:** dia_06/pedidos_sujos.csv. Chave: pedido. Quantidade deve ser inteiro >=0; preço deve ser número >=0. Duplicação exata pode ser removida; outros problemas devem ser separados para revisão, sem inventar valores.

**Tarefa:**
1. Leia as colunas inicialmente como texto e faça conversões explícitas.
2. Produza tabela válida e tabela de auditoria por motivo; calcule o total de itens somente nos registros válidos.

**Entregável esperado:** Código, saída limpa, auditoria e balanço de linhas.

**Critérios de conclusão:**
- [ ] Cada linha original tem destino rastreável, incluindo a duplicata.
- [ ] Ausência não vira zero e preço inválido não desaparece silenciosamente.
- [ ] Executar o tratamento novamente sobre a saída válida não muda seu conteúdo.

**Perguntas de interpretação:**
- Por que preencher quantidade ausente com zero muda a interpretação?
- O total dos registros válidos representa o total de todas as vendas?

**Apoio direcionado:** T, pp. 10-11; roadmap E1.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
