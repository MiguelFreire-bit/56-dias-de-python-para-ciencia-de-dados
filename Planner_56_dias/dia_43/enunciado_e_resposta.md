## Dia 43 - Representar texto exige escolhas

**Competência principal:** NLP e recuperação de informação

**Reforço estatístico:** Frequências; efeito da unidade de contagem.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 55 min

**Problema:** Um portal fictício quer entender seu pequeno acervo antes de fazer busca. Você vai mostrar como decisões de tokenização alteram contagens, sem afirmar compreensão semântica.

**Dados/entrada:** dia_43/corpus.csv; oito documentos inteiramente fictícios, sem dados pessoais. Uma linha por documento; colunas doc_id, tema e texto. Não é necessário baixar modelo de linguagem.

**Tarefa:**
1. Implemente tokenização simples: minúsculas e sequências de letras Unicode, preservando acentos. Compare com uma versão sem acentos.
2. Calcule frequência total de tokens e frequência de documentos para cinco termos escolhidos, incluindo "cartão" e "Python". Mantenha o corpus original.

**Entregável esperado:** Duas versões tokenizadas, tabela de frequências e justificativa.

**Critérios de conclusão:**
- [ ] IDs e associação texto-documento são preservados.
- [ ] Frequência de documentos conta presença uma vez por documento; não confunde com número total de ocorrências.
- [ ] Você registra a regra e demonstra um efeito concreto da normalização.

**Perguntas de interpretação:**
- Remover acentos pode ajudar busca e ao mesmo tempo perder informação?
- Tokenização simples equivale à tokenização de um LLM?

**Apoio direcionado:** Roadmap E4; complemento NLP.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
