## Dia 54 - Complexidade precisa provar utilidade

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Repetições agrupadas, comparação pareada e trade-offs.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 75 min

**Problema:** Duas arquiteturas foram testadas nas mesmas 20 tarefas, três vezes por tarefa. Uma é simples e a outra multiagente. Você recebe logs simulados e precisa recomendar uma escolha sem tratar 60 execuções como 60 tarefas independentes.

**Dados/entrada:** dia_54/comparacao.csv; 60 linhas, chave tarefa+rodada. Assuma tarefas sorteadas independentemente da população-alvo; rodadas da mesma tarefa podem ser dependentes. Correto em 0/1; latência ms; custo reais. Regra pedagógica prévia: adotar multi somente se ganho de acerto>=0,05 (5 pp), custo médio<=2 vezes o simples e latência média<=2 vezes o simples.

**Tarefa:**
1. Compare acerto, custo e latência por arquitetura, por rodada e por tarefa.
2. Faça bootstrap pareado de 20 IDs de tarefa (3.000 reamostras, seed=540), levando suas três rodadas juntas; IC percentil95% do ganho de acerto. Aplique a regra e discuta a incerteza além dela.

**Entregável esperado:** Tabelas, intervalo do ganho e recomendação de até 250 palavras.

**Critérios de conclusão:**
- [ ] Cada reamostra conserva pares de arquiteturas e três rodadas de cada tarefa sorteada.
- [ ] Regras de orçamento e ganho são avaliadas sem mudar limites após olhar resultados.
- [ ] A recomendação aceita manter a versão simples e distingue dados simulados de evidência de produção.

**Perguntas de interpretação:**
- Por que escolher só a melhor rodada favorece uma arquitetura?
- Um ganho pontual que passa o limiar elimina a incerteza sobre tarefas novas?

**Apoio direcionado:** Roadmap E6-E7; complemento bootstrap por grupos.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
