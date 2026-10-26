## Dia 51 - Mudança nos dados e no desempenho

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Drift descritivo; distribuições; erros por janela.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 65 min

**Problema:** Um serviço mudou sua população de entrada. Há rótulos disponíveis para as duas janelas e é possível separar mudança de dados de mudança de desempenho.

**Dados/entrada:** dia_51/janelas.csv; dez casos independentes por janela, com x, real e predito em unidades de demanda. Janelas são amostras didáticas pequenas e distintas. Não existe informação de causa da mudança.

**Tarefa:**
1. Escolha resumos e uma visualização para comparar x entre janelas e calcule MAE em cada uma.
2. Avalie a frase “detectei drift, logo o modelo piorou por causa do drift”. Proponha um monitoramento com baseline, janela e regra de investigação, sem tratar um limiar arbitrário como universal.

**Entregável esperado:** Gráfico, tabela de dados/desempenho e plano breve.

**Critérios de conclusão:**
- [ ] Comparação de distribuição e de erro aparece separada.
- [ ] A afirmação causal é avaliada à luz do desenho e do tamanho de amostra.
- [ ] Plano especifica denominador, frequência e evidência a coletar; evita alertar apenas por variação de média sem contexto.

**Perguntas de interpretação:**
- Pode haver drift sem piora de erro?
- O que você conseguiria avaliar se os rótulos recentes ainda não estivessem disponíveis?

**Apoio direcionado:** Roadmap E7; T, pp. 13-21; complemento drift.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
