## Dia 20 - Dispersão de taxas perto de zero

**Competência principal:** pandas e análise exploratória

**Reforço estatístico:** Desvio padrão, unidade e limites do coeficiente de variação.

**Nível de dificuldade:** intermediário | Tempo-alvo: 50 min

**Problema:** Um relatório usa coeficiente de variação para qualquer coluna numérica. Sua tarefa é avaliar se ele comunica bem taxas mensais que podem estar próximas de zero ou negativas.

**Dados/entrada:** dia_20/ipca_2023_2024.csv; IPCA, SGS 433/BCB, produtor IBGE; Brasil, 2023-2024; data e ipca_pct. Acesso alternativo: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. Use os 24 meses; trate a série como sequência temporal descritiva.

**Tarefa:**
1. Compare, por ano, desvio padrão (ddof=0), IQR e coeficiente de variação calculado como s/média.
2. Repita o CV após subtrair 0,40 ponto percentual de cada taxa, apenas como experimento de referência, sem chamar a série transformada de IPCA observado.

**Entregável esperado:** Tabela original/transformada e escolha justificada de medida.

**Critérios de conclusão:**
- [ ] Você diferencia porcentagem de ponto percentual.
- [ ] A série artificial é identificada e a sensibilidade do CV à origem é discutida.
- [ ] Não usa o CV como regra universal nem aplica inferência i.i.d. aos meses.

**Perguntas de interpretação:**
- Qual medida preserva interpretação quando a média se aproxima de zero?
- Mudar a origem da escala deveria alterar uma medida de dispersão absoluta?

**Apoio direcionado:** F, cap. 2; complemento sobre escalas e CV.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
