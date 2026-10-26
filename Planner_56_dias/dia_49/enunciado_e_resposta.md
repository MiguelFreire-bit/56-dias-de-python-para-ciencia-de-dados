## Dia 49 - Falha de busca, de resposta ou de fonte?

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Rubrica de qualidade e análise de erros por categoria.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Um assistente de portal produziu seis respostas simuladas. Você precisa avaliar fidelidade e classificar falhas sem considerar qualquer recusa como sucesso.

**Dados/entrada:** dia_49/casos.csv. Fontes permitidas por caso: C1/D1, C2/D2, C3/D7, C4/D4, C5/D6, C6/D8; cada contexto do CSV é a evidência completa da respectiva pergunta. Dados são fictícios e nenhum endereço deve ser acessado.

**Tarefa:**
1. Defina rubrica: correção, suporte no contexto, fonte válida e recusa adequada; avalie cada resposta.
2. Classifique falhas observadas e escreva três novos casos de teste (não execute LLM). Separe instruções do sistema de conteúdo documental em um template de prompt.

**Entregável esperado:** Auditoria de seis casos, rubrica e três testes adicionais.

**Critérios de conclusão:**
- [ ] Responder sem evidência e recusar quando há evidência são ambos avaliados como problemas.
- [ ] Citação existente não prova suporte; fonte incorreta é registrada separadamente.
- [ ] O template é descrito como medida parcial: não alega resolver ataques apenas por palavras proibidas ou delimitação.

**Perguntas de interpretação:**
- Qual diferença entre citar uma fonte e ser sustentado por ela?
- Por que um conjunto simulado não comprova robustez de um LLM real?

**Apoio direcionado:** Roadmap E4-E5; complemento testes adversariais.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
