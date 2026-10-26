## Dia 13 - Taxa de conversão em SQL

**Competência principal:** SQL

**Reforço estatístico:** Média de razões versus razão de somas.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 50 min

**Problema:** Um painel compara canais pela média simples das taxas diárias. Os volumes de visitas diferem e há um dia sem visita.

**Dados/entrada:** dia_13/campanhas.csv; uma linha por dia/canal. Visitas e compras são contagens; compras<=visitas; o dia de zero visitas não tem taxa definida. SQLite disponível localmente.

**Tarefa:**
1. Use SQL para calcular taxa diária com proteção de divisão por zero e taxa global por canal.
2. Mostre também a média simples das taxas diárias válidas e compare as perguntas respondidas.

**Entregável esperado:** Consulta com CTE ou subconsulta e tabela de duas taxas por canal.

**Critérios de conclusão:**
- [ ] Divisão usa ponto flutuante e zero visitas produz NULL, não taxa zero.
- [ ] Taxa global usa SUM(compras)/SUM(visitas).
- [ ] A interpretação identifica qual medida pondera o volume e trata o dia sem visitas explicitamente.

**Perguntas de interpretação:**
- Qual medida responde à chance de compra de uma visita selecionada no período?
- Por que a média de taxas pode inverter uma decisão?

**Apoio direcionado:** Roadmap E1; F, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
