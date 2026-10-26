## Dia 21 - Reamostrar para enxergar incerteza

**Competência principal:** Inferência estatística

**Reforço estatístico:** Bootstrap percentil e interpretação de intervalo.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Doze usuários foram sorteados independentemente de uma população ampla de atendimentos. Você precisa estimar a média e tornar visível sua incerteza, com poucos dados e assimetria.

**Dados/entrada:** dia_21/duracoes.csv; tempos em minutos. Reamostragem bootstrap: 5.000 amostras de tamanho 12 com reposição, seed=210. Intervalo percentil de 95%: quantis 2,5% e 97,5% das médias bootstrap, interpolação linear.

**Tarefa:**
1. Construa a distribuição bootstrap da média e o intervalo percentil.
2. Compare desvio dos dados com desvio das médias bootstrap e escreva a interpretação e duas limitações.

**Entregável esperado:** Gráfico das médias, estimativa, intervalo e nota de cautela.

**Critérios de conclusão:**
- [ ] Cada reamostra mantém n=12 e usa reposição; total de médias é 5.000.
- [ ] Intervalo usa médias reamostradas, não percentis dos tempos individuais.
- [ ] A interpretação não atribui 95% de chance ao parâmetro fixo e reconhece a aproximação em amostra pequena.

**Perguntas de interpretação:**
- Bootstrap inventa representatividade que a amostra não tem?
- Por que o intervalo da média não é intervalo para um novo atendimento?

**Apoio direcionado:** F, cap. 6; complemento bootstrap.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
