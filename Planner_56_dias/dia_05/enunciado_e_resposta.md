## Dia 5 - Percentis sem regra escondida

**Competência principal:** Estatística descritiva

**Reforço estatístico:** Quartis, percentis, IQR e regra exploratória de outliers.

**Nível de dificuldade:** básico | Tempo-alvo: 45 min

**Problema:** Uma central quer conhecer a cauda de espera e usa um boxplot. É preciso separar alerta estatístico de confirmação de erro.

**Dados/entrada:** dia_05/esperas.csv; 12 esperas em minutos. Use quantis por interpolação linear, equivalente a pandas quantile(interpolation="linear"). Regra exploratória: abaixo de Q1-1,5 IQR ou acima de Q3+1,5 IQR.

**Tarefa:**
1. Calcule Q1, mediana, Q3 e P90; registre a convenção.
2. Construa boxplot, identifique os valores sinalizados e descreva uma política de investigação sem excluí-los.

**Entregável esperado:** Tabela de quantis, boxplot e nota sobre a cauda.

**Critérios de conclusão:**
- [ ] Quantis estão entre mínimo e máximo e na ordem esperada.
- [ ] Valores sinalizados seguem exatamente os limites calculados.
- [ ] O texto distingue sinalização exploratória, erro e caso raro válido.

**Perguntas de interpretação:**
- P90 é garantia de prazo para o próximo atendimento?
- Por que duas bibliotecas podem produzir quartis diferentes?

**Apoio direcionado:** F, cap. 2; B, cap. 9.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
