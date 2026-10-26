## Dia 18 - Amostra grande não cura seleção ruim

**Competência principal:** Probabilidade e amostragem

**Reforço estatístico:** População finita, amostragem aleatória e estratificada; viés.

**Nível de dificuldade:** intermediário | Tempo-alvo: 50 min

**Problema:** Um serviço funciona de manhã e à noite. O gestor entrevista apenas quem chega primeiro de manhã para estimar o tempo médio de todo o cadastro.

**Dados/entrada:** dia_18/cadastro.csv; população finita de 16 atendimentos. IDs 1-8/manhã e 9-16/noite. Amostra por conveniência: IDs 1-6. Alternativas: sorteie seis IDs sem reposição (seed=180) e três por turno (seed=181).

**Tarefa:**
1. Calcule média da população e das três amostras.
2. Compare composição e erro de cada estimativa; explique por que a estratificação proposta admite pesos iguais neste cadastro.

**Entregável esperado:** Tabela de seleção, composição e erros, com uma recomendação.

**Critérios de conclusão:**
- [ ] Cada amostra tem seis IDs distintos; a estratificada tem três por turno.
- [ ] Você usa população conhecida apenas como referência didática, não como dado normalmente disponível.
- [ ] A conclusão não afirma que um único sorteio bom garante método superior em toda repetição.

**Perguntas de interpretação:**
- Qual diferença entre erro amostral e viés de seleção?
- Se os turnos tivessem tamanhos diferentes, três por turno exigiria que cuidado?

**Apoio direcionado:** F, cap. 6; T, p. 46.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
