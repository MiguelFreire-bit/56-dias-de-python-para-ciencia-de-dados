## Dia 48 - Um prompt melhor sob qual critério?

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Comparação pareada; discordâncias; custo.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Duas versões de prompt foram avaliadas nas mesmas 12 perguntas independentes por uma rubrica fixa. O prompt B usa mais tokens. O teste pequeno não deve virar uma promessa ampla.

**Dados/entrada:** dia_48/prompts.csv; correto=1, incorreto=0; tokens são totais por chamada. Preço didático único=R$0,01 por 1.000 tokens. Para teste exato de discordâncias: b=A acerta/B erra; c=A erra/B acerta; sob H0, b em b+c segue Binomial(b+c,0,5).

**Tarefa:**
1. Monte a tabela pareada 2x2, taxas de acerto, diferença e custos totais.
2. Execute teste binomial bilateral nas discordâncias, alpha=0,05; se b+c=0, reporte ausência de discordâncias sem inventar um teste. Recomende próximo passo considerando evidência e custo.

**Entregável esperado:** Tabela pareada, métricas, teste e recomendação.

**Critérios de conclusão:**
- [ ] Perguntas iguais são comparadas como pares; não trata 24 julgamentos como amostras independentes.
- [ ] Custos usam divisão por 1.000 e a mesma tarifa.
- [ ] O texto distingue melhoria observada, evidência estatística e relevância prática.

**Perguntas de interpretação:**
- Por que concordâncias não entram na contagem binomial das discordâncias?
- O que precisaria mudar se as 12 perguntas fossem todas variações de duas dúvidas?

**Apoio direcionado:** F, caps. 5 e 7; roadmap E4-E5; complemento comparação pareada.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
