## Dia 47 - JSON válido ainda pode estar errado

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Taxas de validade sintática, de esquema e de fundamentação.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Um extrator fictício recebe um documento por vez e devolve prazo e custo. As respostas já foram coletadas; você deve auditar camadas de qualidade distintas.

**Dados/entrada:** dia_47/corpus.csv e dia_47/saidas.csv; oito textos e seis saídas fictícias. Contrato estrito: prazo_dias inteiro>=0 ou null; custo_reais número>=0 ou null; fonte igual ao documento recebido; sem campos extras. Prazo só representa devolução/emissão, nunca viagens por dia; não inventar valor quando ausente. Registrar dias úteis quando o texto o disser, em observação da auditoria.

**Tarefa:**
1. Valide parsing e esquema sem converter strings numéricas automaticamente.
2. Revise semanticamente as seis saídas contra os textos, incluindo unidade, ausência e fonte; calcule três taxas separadas, todas sobre seis saídas.

**Entregável esperado:** Validador, matriz de auditoria por camada e explicação de duas falhas.

**Critérios de conclusão:**
- [ ] Saída que não parseia conta como falha de parsing, esquema e fundamentação no resumo sobre seis.
- [ ] Um JSON com tipos corretos não é automaticamente aprovado semanticamente.
- [ ] Cada rejeição cita trecho ou regra; nenhuma chamada paga é necessária.

**Perguntas de interpretação:**
- Por que validar com Pydantic não prova que a resposta é verdadeira?
- Quando null é mais fiel do que zero?

**Apoio direcionado:** Roadmap E3-E5; complemento de avaliação estruturada.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
