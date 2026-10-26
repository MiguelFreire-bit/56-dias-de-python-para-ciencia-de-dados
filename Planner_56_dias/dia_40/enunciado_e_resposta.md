## Dia 40 - Um contrato de dados que detecta falhas

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Sem conexão estatística central; foco em qualidade e testes.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Um pipeline deve impedir dados inválidos de chegar a uma análise. Você precisa distinguir erro de regra, ausência permitida e conflito de chave.

**Dados/entrada:** dia_40/lote.csv. Contrato: id único e não vazio; idade inteira 0-120; renda >=0 ou ausente; segmento em A/B. Rendas ausentes são permitidas com aviso. IDs duplicados com conteúdo diferente vão todos à quarentena; não escolher versão arbitrariamente.

**Tarefa:**
1. Implemente validação que retorna linhas válidas e relatório de problemas.
2. Escreva testes para lote válido, idade inválida, renda ausente, segmento inválido e duplicação conflitante.

**Entregável esperado:** Função, testes e auditoria reproduzível.

**Critérios de conclusão:**
- [ ] Ausência de renda é aviso, não exclusão automática; zero permanece válido.
- [ ] Ambas as versões conflitantes são rastreadas e não aparecem como dados limpos.
- [ ] Testes verificam comportamento de contrato e mensagens, não apenas repetem a implementação.

**Perguntas de interpretação:**
- Por que escolher a primeira duplicata pode esconder uma decisão de negócio?
- Que regra precisaria ser negociada antes de imputar renda?

**Apoio direcionado:** Roadmap E1 e E3; T, pp. 10-12.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
