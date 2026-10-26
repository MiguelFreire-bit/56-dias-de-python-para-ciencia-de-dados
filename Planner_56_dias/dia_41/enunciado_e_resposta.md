## Dia 41 - Uma API pode falhar sem estragar os dados

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Sem conexão estatística central; foco em ingestão HTTP.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Uma rotina consulta dados oficiais, mas precisa se comportar corretamente quando há timeout, erro HTTP ou corpo inválido. A atividade deve funcionar sem rede.

**Dados/entrada:** dia_41/ipca_2023_2024.csv e dia_41/ipca_original.json: SGS433/BCB, produtor IBGE; Brasil 2023-2024, campos originais data/valor. Endpoint: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. dia_41/respostas_http.csv descreve quatro cenários simuláveis; injete um cliente falso no lugar do HTTP real.

**Tarefa:**
1. Implemente leitura/validação de resposta e conversão de data/valor para o esquema do CSV.
2. Teste sucesso, 404, timeout e JSON inválido com doubles/mocks. Chamada real é opcional; nunca necessária para concluir.

**Entregável esperado:** Função com dependência HTTP injetável e quatro testes de comportamento.

**Critérios de conclusão:**
- [ ] Sucesso gera 24 meses únicos e numéricos; falha não retorna tabela vazia indistinguível de sucesso.
- [ ] Há timeout explícito no cliente real e erro classificado nos testes.
- [ ] Resposta bruta/origem são preservadas; não há loop ilimitado de tentativas.

**Perguntas de interpretação:**
- Por que um mock de sucesso não prova disponibilidade atual do serviço?
- Como distinguir ausência de dados de falha de acesso?

**Apoio direcionado:** Roadmap E1 C07 e E3; complemento de testes.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**
