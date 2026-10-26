## Dia 29 - Uma regressão que você consegue explicar

**Competência principal:** Machine learning

**Reforço estatístico:** Mínimos quadrados; coeficiente, intercepto e resíduo.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Uma imobiliária quer uma referência descritiva de aluguel em função da área. Os oito imóveis são um recorte observacional fictício; a relação não identifica efeito causal da área.

**Dados/entrada:** dia_29/imoveis.csv; area_m2 e aluguel_reais. Use todos os oito casos para ajuste didático; ainda não declare capacidade de generalização. Consulte a fórmula beta1=sum((x-xbarra)(y-ybarra))/sum((x-xbarra)^2).

**Tarefa:**
1. Calcule beta1 e beta0 a partir das somas e confira com LinearRegression.
2. Produza valores ajustados, resíduos y-y_hat e gráfico; estime para 65 m² e discuta separadamente 250 m².

**Entregável esperado:** Modelo escrito em unidades, tabela de resíduos e gráfico.

**Critérios de conclusão:**
- [ ] Coeficientes manual e da biblioteca coincidem até 1e-6.
- [ ] Soma dos resíduos do ajuste com intercepto é aproximadamente zero.
- [ ] Você distingue interpolação de extrapolação e não chama erro de treino de validação.

**Perguntas de interpretação:**
- Qual unidade e significado do coeficiente angular?
- O intercepto representa aluguel confiável de um imóvel de área zero?

**Apoio direcionado:** F, cap. 12; T, pp. 27-29; roadmap E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
