## Dia 46 - Oito em dez não encerra a avaliação

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Intervalo de Wilson para proporção; tamanho de amostra.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Dois testes de um assistente têm a mesma proporção de acertos, mas tamanhos diferentes. A equipe quer comparar a força da evidência, sem declarar equivalência entre sistemas.

**Dados/entrada:** dia_46/avaliacao.csv. Piloto=8/10; ampliada=80/100; amostras separadas de perguntas sorteadas independentemente da mesma população-alvo e julgadas por rubrica fixa. Use Wilson95%, z=1,96: centro=(p+z²/(2n))/(1+z²/n); margem=z*sqrt(p(1-p)/n+z²/(4n²))/(1+z²/n).

**Tarefa:**
1. Calcule estimativas pontuais, limites e larguras dos dois intervalos.
2. Faça gráfico com barras de incerteza e avalie o que a hipótese de perguntas independentes deixa de representar se várias forem paráfrases da mesma pergunta.

**Entregável esperado:** Tabela de intervalos e nota sobre qualidade do teste.

**Critérios de conclusão:**
- [ ] p=acertos/n usa proporção, sem substituir 80 em lugar de 0,80.
- [ ] Limites permanecem em [0,1] e fórmulas são reproduzíveis.
- [ ] Você distingue incerteza amostral de viés da rubrica/conjunto e não usa sobreposição como teste formal de igualdade.

**Perguntas de interpretação:**
- Mesma taxa pontual implica mesma precisão da estimativa?
- Que efeito a dependência entre paráfrases pode ter no tamanho efetivo da avaliação?

**Apoio direcionado:** F, cap. 6; roadmap E5; complemento Wilson.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
