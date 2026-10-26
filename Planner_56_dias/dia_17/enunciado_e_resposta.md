## Dia 17 - Custo esperado não é custo garantido

**Competência principal:** Probabilidade e amostragem

**Reforço estatístico:** Esperança, variância e risco de cauda.

**Nível de dificuldade:** intermediário | Tempo-alvo: 50 min

**Problema:** Uma operação quer uma reserva média de custo por pedido e também saber se essa média descreve o risco de um pedido isolado.

**Dados/entrada:** dia_17/custos.csv. Eventos mutuamente exclusivos e exaustivos: sem falha p=0,70/custo 0; leve p=0,25/custo 20; grave p=0,05/custo 300. Considere pedidos independentes somente para a simulação.

**Tarefa:**
1. Calcule E(C), E(C²), Var(C) e desvio padrão pelas probabilidades.
2. Simule 5.000 pedidos (seed=170) e compare média e proporção de custos maiores que R$100 com os valores teóricos.

**Entregável esperado:** Memória de cálculo, tabela teórica/simulada e decisão sobre como comunicar o risco.

**Critérios de conclusão:**
- [ ] Probabilidades somam 1; variância usa E(C²)-E(C)².
- [ ] Custo esperado e desvio estão em reais; variância em reais².
- [ ] Comunicação separa média no longo prazo de custo individual e de eventos raros.

**Perguntas de interpretação:**
- Um pedido precisa ter custo igual ao esperado?
- Por que somente a média é insuficiente para uma reserva de segurança?

**Apoio direcionado:** F, cap. 5; G, cap. 5.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
