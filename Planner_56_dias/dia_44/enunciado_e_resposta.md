## Dia 44 - Uma busca lexical para servir de referência

**Competência principal:** NLP e recuperação de informação

**Reforço estatístico:** Sem conexão estatística central; similaridade e ranking.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Antes de usar embeddings e RAG, um portal precisa de uma busca simples que possa ser inspecionada. Ela pode falhar em paráfrases; isso é parte da avaliação.

**Dados/entrada:** dia_44/corpus.csv e dia_44/consultas.csv; oito documentos fictícios e quatro perguntas com documento relevante fornecido. Use TfidfVectorizer(lowercase=True,strip_accents="unicode") e similaridade de cosseno. Sem serviço externo.

**Tarefa:**
1. Ajuste TF-IDF somente nos documentos e transforme as perguntas com o mesmo vetorizador.
2. Retorne top-3 por consulta, com score e doc_id; desempate por doc_id crescente. Analise pelo menos um acerto e um limite, sem retocar o corpus para esconder falhas.

**Entregável esperado:** Função de busca, rankings e análise de erros/limites.

**Critérios de conclusão:**
- [ ] Cada ranking tem três IDs distintos do corpus e scores em ordem não crescente.
- [ ] Perguntas não entram no fit do vocabulário nem o rótulo relevante na similaridade.
- [ ] Scores são descritos como similaridade, não probabilidade de a resposta estar correta.

**Perguntas de interpretação:**
- Por que uma paráfrase pode falhar mesmo quando a resposta existe?
- O que este baseline permite testar antes de adicionar complexidade?

**Apoio direcionado:** Roadmap E4-E5; complemento TF-IDF.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
