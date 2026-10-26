# Planner de prática técnica - 56 dias

Miguel Silva Freire | Rumo ao CD | 23/10/2026

## 1. Lógica do planner

Este planner pratica o roadmap oficial versão 1.1, de 21/10/2026 (31 páginas). Não substitui cursos, projetos P1-P3 nem critérios de avanço da trilha. Os problemas aqui têm contextos próprios e não usam projetos profissionais, energia solar ou dados privados.

Os 56 dias são sessões numeradas, sem datas fixas. Cada dia termina em uma entrega própria e contém todos os dados necessários no enunciado ou no pacote de dados. Conceitos se acumulam, arquivos de soluções anteriores não são pré-requisitos. Reutilizar uma fonte é prática de transferência, não continuação de projeto.

A sequência começa com execução orientada e avança para interpretação, escolha, comparação, diagnóstico e justificativa. Os dias finais continuam pequenos: recebem logs, saídas ou datasets já preparados para que o desafio seja decidir, não montar infraestrutura.

Estatística é transversal: centro e dispersão reaparecem em taxas, amostragem, intervalos, testes, resíduos, métricas de modelos e avaliação de IA. Nos dias sem conexão estatística central isso é dito explicitamente. Todas as atividades cobram explicação, inclusive as de código.

Dados reais entram quando ajudam a habilidade: IPCA/IBGE via BCB em um recorte fixo e Iris/Wine da UCI via cópias locais do scikit-learn. Os demais casos são sintéticos, pequenos e identificados como tais. Não há dados de empresa. Todas as bases usadas estão fornecidas; rede e contas pagas não são necessárias.

Os exercícios de texto e ferramentas preparam E4-E7 sem exigir um RAG, LLM ou multiagente completo nesta janela. Fine-tuning, Spark e infraestrutura distribuída não entram: não resolvem a prioridade atual de fundamentos e raciocínio estatístico.

### Como usar

Organização: reserve de 35 a 80 minutos conforme o dia; a estimativa inclui leitura do problema, código, interpretação e conferência. É tempo-alvo, não prazo de aprovação. Se faltar teoria, estude-a no roadmap e retome a mesma sessão; não sacrifique entendimento para cumprir calendário.

Rotina sugerida: 5-10 min para entender e prever o comportamento; maior parte para resolver; 10-15 min finais para conferir critérios e responder às perguntas. Nos dias avançados, escreva método e métrica antes de olhar a comparação.

Primeira tentativa: pode consultar documentação e os materiais indicados. Tente formular a estratégia antes de pedir código à IA. Para correção, envie o número do dia, código/consulta, tabelas ou gráficos e respostas de interpretação.

Marque concluído quando todos os critérios do dia tiverem evidência. Não é necessário obter melhora de um modelo, um p significativo ou uma arquitetura complexa vencedora. Uma conclusão negativa bem demonstrada vale; vazamento e justificativas ausentes precisam ser corrigidos.

Formato editável: cada pasta dia_XX inclui seu enunciado em Markdown, dados e espaço para resposta. O arquivo Planner_56_dias.md reúne tudo. CSVs usam UTF-8, vírgula como separador e ponto decimal, salvo exemplos de sujeira deliberada documentados. Célula vazia é ausência, não zero.

Ambiente: Python 3 com numpy, pandas, scipy, matplotlib, scikit-learn e pytest. JSON, CSV e SQLite usam a biblioteca padrão. Pydantic/requests são alternativas opcionais; não são necessários se usar validação própria e cliente falso. Registre versões. Sem instalação ou configuração de cloud como tarefa escondida.

## 2. Blocos de progressão

| Dias | Objetivo | Competências | Nível esperado ao final | Roadmap |
|---|---|---|---|---|
| 1-7 | Entender antes de resumir | Python, tipos, centro, dispersão, limpeza e pesos. | Calcular, conferir e explicar medidas com orientação. | E1; fundamentos de E2 |
| 8-14 | Explorar sem distorcer | pandas, dados oficiais, associação, ausências, SQL e gráficos. | Conectar pergunta, unidade de análise e denominador. | E1-E2 |
| 15-21 | Pensar em variabilidade | Probabilidade, distribuições, seleção, simulação e bootstrap. | Distinguir dados, estatística e incerteza. | E2 |
| 22-28 | Inferir com limites | Intervalos, testes, pareamento, contagens, multiplicidade e poder. | Formular hipóteses e interpretar evidência sem certezas indevidas. | E2 |
| 29-35 | Modelar com avaliação válida | Regressão, resíduos, classificação, Pipelines e validação. | Comparar modelos com baseline e teste preservado. | E2; preparação para E3 |
| 36-42 | Validar e entregar código confiável | Tempo, métricas, limiar, incerteza pareada, contratos, HTTP e testes. | Diagnosticar erros de avaliação e proteger funções de dados. | E1-E3 |
| 43-49 | Avaliar texto e recuperação | Tokenização, TF-IDF, recuperação, proporções, JSON e respostas. | Separar falhas de recuperação, estrutura, resposta e citação. | Preparação para E4-E5 |
| 50-56 | Escolher e defender decisões | Segmentos, drift, logs, ferramentas, arquitetura e auditorias. | Receber um problema delimitado, escolher abordagem e justificar limites. | Consolidação E1-E3; preparação E5-E7 |

## 3. Planner completo - 56 dias

## Dia 1 - Antes de calcular, entender as colunas

**Competência principal:** Python e estruturas de dados

**Reforço estatístico:** Tipos de variáveis; unidade de observação; população e amostra.

**Nível de dificuldade:** básico | Tempo-alvo: 35 min

**Problema:** Uma loja entregou seis registros e quer começar uma análise. Os códigos de clientes parecem números, mas cada coluna tem um significado diferente.

**Dados/entrada:** dia_01/clientes.csv. Seis clientes observados em uma semana; não são um censo de toda a clientela. Satisfação: ruim < regular < boa < ótima. Valores monetários em reais.

**Tarefa:**
1. Leia o CSV com Python ou pandas e descreva cada coluna: significado, tipo técnico e tipo estatístico.
2. Mantenha o ID como texto e represente um registro como dicionário. Conte clientes por bairro.

**Entregável esperado:** Dicionário das cinco colunas, código curto e tabela por bairro.

**Critérios de conclusão:**
- [ ] As seis linhas são preservadas e os IDs mantêm os zeros iniciais.
- [ ] Cada variável recebe classificação justificada; as contagens por bairro somam seis.
- [ ] Você distingue a amostra observada da população à qual a loja gostaria de generalizar.

**Perguntas de interpretação:**
- Que operações fazem sentido com compras, mas não com id?
- Uma média dos códigos de bairro seria interpretável? Por quê?

**Apoio direcionado:** F, cap. 1; B, caps. 3-4; G, cap. 1.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 2 - Contar com o denominador certo

**Competência principal:** Estatística descritiva

**Reforço estatístico:** Frequências absoluta, relativa e acumulada.

**Nível de dificuldade:** básico | Tempo-alvo: 35 min

**Problema:** Um atendimento quer comunicar a distribuição de satisfação de 12 respostas, sem transformar uma escala ordinal em medida contínua.

**Dados/entrada:** dia_02/respostas.csv: uma linha por resposta; ordem ruim < regular < boa < ótima. Todas as respostas são válidas.

**Tarefa:**
1. Construa frequências absolutas, relativas e relativas acumuladas nessa ordem.
2. Faça um gráfico de barras com rótulos e calcule a proporção de respostas pelo menos boas.

**Entregável esperado:** Tabela, gráfico e interpretação de quatro linhas.

**Critérios de conclusão:**
- [ ] Contagens somam 12 e proporções somam 1 antes do arredondamento.
- [ ] Frequência acumulada respeita a ordem declarada e termina em 1.
- [ ] O gráfico identifica número de respostas e não sugere intervalos numéricos iguais entre categorias.

**Perguntas de interpretação:**
- O que muda se o denominador incluir pessoas que não responderam?
- Por que ordenar alfabeticamente prejudica a frequência acumulada?

**Apoio direcionado:** F, cap. 2; G, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 3 - Uma entrega muito demorada

**Competência principal:** Estatística descritiva

**Reforço estatístico:** Média, mediana, moda e sensibilidade a valor extremo.

**Nível de dificuldade:** básico | Tempo-alvo: 40 min

**Problema:** Uma empresa quer resumir o tempo típico de entrega. Uma das nove entregas demorou muito mais que as outras; ainda não se sabe se houve erro.

**Dados/entrada:** dia_03/entregas.csv; minutos por entrega: 18, 20, 21, 22, 22, 23, 24, 25, 90. Todos os nove registros são observações válidas para esta atividade.

**Tarefa:**
1. Calcule média, mediana e moda; confira uma medida por cálculo explícito.
2. Recalcule as medidas em uma análise de sensibilidade sem 90, preservando a versão completa. Escolha uma medida para representar tempo típico.

**Entregável esperado:** Tabela das duas análises e justificativa da medida escolhida.

**Critérios de conclusão:**
- [ ] Versão completa tem nove casos e a análise de sensibilidade tem oito.
- [ ] Cálculo explícito concorda com a biblioteca até 1e-8.
- [ ] A escolha considera assimetria; o valor extremo não é tratado automaticamente como erro.

**Perguntas de interpretação:**
- Qual pergunta a média responde e qual a mediana responde?
- Que informação adicional você pediria antes de excluir a entrega?

**Apoio direcionado:** F, cap. 2; G, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 4 - Médias iguais, experiências diferentes

**Competência principal:** Estatística descritiva

**Reforço estatístico:** Variância populacional e amostral; desvio padrão.

**Nível de dificuldade:** básico | Tempo-alvo: 45 min

**Problema:** Dois postos apresentam tempos médios semelhantes, mas o usuário percebe regularidades diferentes. Os cinco atendimentos de cada posto formam a população finita observada de uma manhã.

**Dados/entrada:** dia_04/filas.csv; A=[8,9,10,11,12], B=[2,6,10,14,18], em minutos. Depois considere separadamente o cenário em que esses mesmos dados são amostras de muitas manhãs.

**Tarefa:**
1. Calcule média, variância com divisor n e desvio padrão de cada posto.
2. Para A, mostre desvios e quadrados; depois compare o resultado com divisor n-1 e explique em qual cenário cada convenção foi usada.

**Entregável esperado:** Tabela de dispersão e memória de cálculo de A.

**Critérios de conclusão:**
- [ ] Soma dos desvios de cada grupo é aproximadamente zero.
- [ ] Variância é reportada em min² e desvio padrão em minutos.
- [ ] Convenção ddof está explícita; não mistura estimativa amostral com descrição da população finita.

**Perguntas de interpretação:**
- Que diferença de experiência não aparece na média?
- Por que trocar n por n-1 não é apenas um detalhe de software?

**Apoio direcionado:** F, cap. 2; G, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 6 - Limpar preservando o que aconteceu

**Competência principal:** Limpeza e qualidade de dados

**Reforço estatístico:** Ausência e efeito do tratamento em estatísticas.

**Nível de dificuldade:** básico | Tempo-alvo: 45 min

**Problema:** Uma exportação de pedidos mistura vírgula decimal, duplicação exata, ausência e quantidade impossível. Zero é quantidade válida; quantidade negativa é inválida neste cadastro de vendas.

**Dados/entrada:** dia_06/pedidos_sujos.csv. Chave: pedido. Quantidade deve ser inteiro >=0; preço deve ser número >=0. Duplicação exata pode ser removida; outros problemas devem ser separados para revisão, sem inventar valores.

**Tarefa:**
1. Leia as colunas inicialmente como texto e faça conversões explícitas.
2. Produza tabela válida e tabela de auditoria por motivo; calcule o total de itens somente nos registros válidos.

**Entregável esperado:** Código, saída limpa, auditoria e balanço de linhas.

**Critérios de conclusão:**
- [ ] Cada linha original tem destino rastreável, incluindo a duplicata.
- [ ] Ausência não vira zero e preço inválido não desaparece silenciosamente.
- [ ] Executar o tratamento novamente sobre a saída válida não muda seu conteúdo.

**Perguntas de interpretação:**
- Por que preencher quantidade ausente com zero muda a interpretação?
- O total dos registros válidos representa o total de todas as vendas?

**Apoio direcionado:** T, pp. 10-11; roadmap E1.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 7 - A média das médias pode enganar

**Competência principal:** Estatística descritiva

**Reforço estatístico:** Média ponderada e unidade de análise.

**Nível de dificuldade:** básico | Tempo-alvo: 40 min

**Problema:** Uma coordenação informa a média geral das notas tirando a média simples das médias das turmas. As turmas têm tamanhos diferentes.

**Dados/entrada:** dia_07/turmas.csv; A:10 alunos/média 9; B:30/média 6; C:60/média 7. Cada aluno fez uma prova e pertence a uma única turma. As médias fornecidas são exatas.

**Tarefa:**
1. Calcule a média das médias e a média ponderada pelo número de alunos.
2. Defina qual medida responde à nota média por aluno e qual responde à média de uma turma escolhida uniformemente.

**Entregável esperado:** Duas medidas com fórmulas e nota de cinco linhas.

**Critérios de conclusão:**
- [ ] Os pesos somam o total de alunos e não usam os valores das notas.
- [ ] Cada medida está associada à unidade sorteada ou resumida.
- [ ] A conclusão se limita à média: não inventa variância individual a partir das médias das turmas.

**Perguntas de interpretação:**
- Que dados faltam para calcular o desvio padrão das notas individuais?
- Em qual situação as duas médias coincidiriam?

**Apoio direcionado:** F, cap. 2; roadmap E1-E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 8 - Primeira análise de uma série oficial

**Competência principal:** pandas e análise exploratória

**Reforço estatístico:** Distribuição, tendência central e dispersão.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 45 min

**Problema:** Um relatório quer comparar o comportamento da inflação mensal em dois anos, sem confundir variação mensal com inflação acumulada.

**Dados/entrada:** dia_08/ipca_2023_2024.csv: SGS 433, IPCA, produzido pelo IBGE e distribuído pelo BCB. Brasil; jan/2023-dez/2024; 24 meses; data e ipca_pct (variação percentual mensal). Use a cópia fornecida. Consulta alternativa: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024

**Tarefa:**
1. Converta datas e valores, valide a grade mensal e separe os dois anos.
2. Calcule média, mediana, mínimo, máximo e desvio padrão descritivo (ddof=0) por ano. Escreva uma comparação sem inferência populacional.

**Entregável esperado:** Tabela anual, verificações e interpretação de até oito linhas.

**Critérios de conclusão:**
- [ ] Há 12 observações por ano, meses únicos e valores numéricos.
- [ ] Percentuais mensais são identificados como taxas, sem soma ou média chamada de acumulado anual.
- [ ] A interpretação considera centro e dispersão e não atribui causa a mudanças.

**Perguntas de interpretação:**
- O que significa uma taxa mensal negativa?
- A média mensal responde à mesma pergunta que o acumulado anual?

**Apoio direcionado:** F, cap. 2; T, pp. 13-16.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 9 - Associação não é explicação causal

**Competência principal:** Análise bivariada e visualização

**Reforço estatístico:** Covariância amostral e correlação de Pearson.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 50 min

**Problema:** Uma escola observa horas de estudo declaradas e notas de oito estudantes. Quer saber se existe associação, sem afirmar que uma hora adicional necessariamente produz uma nota maior.

**Dados/entrada:** dia_09/estudo.csv; horas=[1,2,3,4,5,6,7,8]; notas=[4,5,5,6,7,7,8,6]. Estudo observacional; nenhum aluno foi sorteado para estudar um tempo específico.

**Tarefa:**
1. Faça dispersão e calcule covariância amostral e Pearson.
2. Transforme horas em minutos e recalcule as duas medidas. Compare as unidades e o efeito da transformação.

**Entregável esperado:** Gráfico, tabela das medidas nas duas escalas e interpretação.

**Critérios de conclusão:**
- [ ] Correlação está em [-1,1] e a transformação usa fator 60.
- [ ] Você explica por que uma medida depende da escala, com evidência numérica.
- [ ] A conclusão indica pelo menos um possível confundidor e não faz afirmação causal.

**Perguntas de interpretação:**
- Qual papel o último ponto tem na associação?
- Uma correlação alta garantiria boa previsão para um aluno novo?

**Apoio direcionado:** F, cap. 3; G, cap. 3; T, p. 46.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 10 - Quando o agregado muda a história

**Competência principal:** Análise bivariada e visualização

**Reforço estatístico:** Taxas condicionais, ponderação e confundimento.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 50 min

**Problema:** Dois procedimentos fictícios são comparados apenas pela taxa geral de sucesso. A distribuição da gravidade dos casos difere entre eles; não houve sorteio de procedimento.

**Dados/entrada:** dia_10/tratamentos.csv. Cada linha contém número de sucessos e total de pessoas; falhas=total-sucessos. Todos os totais se referem a grupos disjuntos.

**Tarefa:**
1. Calcule taxas por procedimento e gravidade, e depois taxas agregadas.
2. Compare a composição dos procedimentos e monte uma visualização que preserve os estratos.

**Entregável esperado:** Tabelas estratificada e agregada, gráfico e avaliação da recomendação.

**Critérios de conclusão:**
- [ ] Taxas usam sucessos/total, sem média simples de percentuais de linhas.
- [ ] Diferença de composição é quantificada e relacionada à comparação agregada.
- [ ] A análise não declara superioridade causal de um procedimento observacional.

**Perguntas de interpretação:**
- Por que o agregado e os estratos podem sugerir ordens diferentes?
- O que um experimento aleatorizado acrescentaria?

**Apoio direcionado:** F, caps. 3-4; T, p. 46. Contexto inteiramente fictício.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 11 - Ausência também conta uma história

**Competência principal:** Limpeza e qualidade de dados

**Reforço estatístico:** Viés de não resposta e análise de sensibilidade.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 50 min

**Problema:** Uma pesquisa de renda tem três respostas ausentes. A chefia pede uma renda média de todos os oito convidados, embora só cinco tenham informado o valor.

**Dados/entrada:** dia_11/rendas.csv. Ausência significa não resposta; renda zero seria válida, mas não está observada. Para uma análise de sensibilidade hipotética, suponha cada renda ausente entre R$1.000 e R$6.000; isso não é informação verificada.

**Tarefa:**
1. Calcule taxa de não resposta e média dos respondentes.
2. Calcule os limites da média dos oito sob as duas extremidades hipotéticas. Compare com preencher pela média observada.

**Entregável esperado:** Tabela com cenários separados e explicação dos limites da estimativa.

**Critérios de conclusão:**
- [ ] Média observada usa cinco rendas e taxa de ausência usa oito convidados.
- [ ] Cenários não são apresentados como dados recuperados.
- [ ] A conclusão discute representatividade; não pressupõe ausência completamente aleatória.

**Perguntas de interpretação:**
- Preencher pela média resolve o viés de seleção?
- Qual hipótese seria necessária para generalizar os respondentes?

**Apoio direcionado:** F, cap. 6; T, pp. 10, 46.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 12 - Um JOIN que não inventa clientes

**Competência principal:** SQL

**Reforço estatístico:** Granularidade e denominadores após junções.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 55 min

**Problema:** Um gestor quer o número de clientes e o valor de pedidos por cidade. Uma junção ingênua conta várias vezes o mesmo cliente e oculta pedidos sem cadastro.

**Dados/entrada:** dia_12/clientes.csv e dia_12/pedidos.csv. Clientes: C1/Recife, C2/Natal, C3/Recife, C4/Olinda. Pedidos: P1/C1/100, P2/C1/50, P3/C2/80, P4/C9/20. Use SQLite; C9 não existe no cadastro.

**Tarefa:**
1. Crie as duas tabelas; use LEFT JOIN para preservar clientes sem pedido.
2. Entregue valor e clientes distintos por cidade e uma consulta separada de pedidos órfãos. Confira o total de pedidos antes e depois de cada relação.

**Entregável esperado:** Duas consultas SQL, tabelas de saída e explicação da granularidade.

**Critérios de conclusão:**
- [ ] O cliente sem pedido aparece com valor zero somente na agregação de pedidos, sem criar pedido fictício.
- [ ] Clientes distintos são contados pela chave; o pedido órfão é explicitamente auditado.
- [ ] A soma dos valores associados mais os órfãos reconcilia com todos os pedidos.

**Perguntas de interpretação:**
- Por que COUNT(*) depois de JOIN não é necessariamente número de clientes?
- Quando um INNER JOIN esconderia um problema de qualidade?

**Apoio direcionado:** Roadmap E1, C08-C09; complemento SQL.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 13 - Taxa de conversão em SQL

**Competência principal:** SQL

**Reforço estatístico:** Média de razões versus razão de somas.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 50 min

**Problema:** Um painel compara canais pela média simples das taxas diárias. Os volumes de visitas diferem e há um dia sem visita.

**Dados/entrada:** dia_13/campanhas.csv; uma linha por dia/canal. Visitas e compras são contagens; compras<=visitas; o dia de zero visitas não tem taxa definida. SQLite disponível localmente.

**Tarefa:**
1. Use SQL para calcular taxa diária com proteção de divisão por zero e taxa global por canal.
2. Mostre também a média simples das taxas diárias válidas e compare as perguntas respondidas.

**Entregável esperado:** Consulta com CTE ou subconsulta e tabela de duas taxas por canal.

**Critérios de conclusão:**
- [ ] Divisão usa ponto flutuante e zero visitas produz NULL, não taxa zero.
- [ ] Taxa global usa SUM(compras)/SUM(visitas).
- [ ] A interpretação identifica qual medida pondera o volume e trata o dia sem visitas explicitamente.

**Perguntas de interpretação:**
- Qual medida responde à chance de compra de uma visita selecionada no período?
- Por que a média de taxas pode inverter uma decisão?

**Apoio direcionado:** Roadmap E1; F, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 14 - Um gráfico para cada pergunta

**Competência principal:** pandas e análise exploratória

**Reforço estatístico:** Distribuição versus evolução temporal; percentuais compostos.

**Nível de dificuldade:** básico/intermediário | Tempo-alvo: 55 min

**Problema:** Um relatório usa somente um histograma para explicar quando a inflação variou. Você precisa escolher representações adequadas e separar média de acumulação.

**Dados/entrada:** dia_14/ipca_2023_2024.csv, SGS 433/BCB, produtor IBGE; Brasil, jan/2023-dez/2024; data e ipca_pct. Cópia incluída e consulta alternativa: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024

**Tarefa:**
1. Produza linha temporal e histograma com limites de classes declarados.
2. Calcule acumulado por ano por composição de fatores (1+taxa/100), sem usar soma como resultado final; compare com a soma em uma análise separada.

**Entregável esperado:** Dois gráficos, tabela anual e texto distinguindo as perguntas.

**Critérios de conclusão:**
- [ ] Linha usa datas ordenadas e histograma usa os mesmos 24 meses.
- [ ] Acumulado resulta do produto dos fatores, convertido novamente para %.
- [ ] Unidades e limites estão rotulados; não apresenta o histograma como sequência temporal.

**Perguntas de interpretação:**
- Que informação cada gráfico perde?
- Por que uma taxa negativa não torna o fator de composição negativo neste recorte?

**Apoio direcionado:** F, cap. 2; T, pp. 17-21; complemento de composição de taxas.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 15 - A condição muda a probabilidade

**Competência principal:** Probabilidade e amostragem

**Reforço estatístico:** Probabilidade conjunta, condicional e independência.

**Nível de dificuldade:** intermediário | Tempo-alvo: 45 min

**Problema:** Uma pesquisa de 200 pessoas registra o canal de origem e a realização de compra. Um analista confunde a chance de compra dado o canal com a chance do canal dado a compra.

**Dados/entrada:** dia_15/pesquisa.csv; quatro contagens agregadas: email/comprou=30, email/não=70, busca/comprou=60, busca/não=40. Os 200 participantes são distintos; seleção uniforme dentro dessa tabela.

**Tarefa:**
1. Calcule P(compra), P(email e compra), P(compra|email) e P(email|compra).
2. Verifique independência pela definição usando a tabela, sem executar teste de hipótese ainda.

**Entregável esperado:** Tabela de probabilidades com numeradores e denominadores explícitos.

**Critérios de conclusão:**
- [ ] Probabilidades permanecem em [0,1] e probabilidades conjuntas somam 1.
- [ ] Cada condicional usa o universo da condição, não sempre 200.
- [ ] A verificação de independência compara quantidades compatíveis e se limita à tabela observada.

**Perguntas de interpretação:**
- Por que inverter a condição muda o denominador?
- Independência observada em uma tabela garantiria independência na população?

**Apoio direcionado:** F, cap. 4; G, cap. 4.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 16 - Do evento à distribuição

**Competência principal:** Probabilidade e amostragem

**Reforço estatístico:** Distribuição binomial, frequência e probabilidade.

**Nível de dificuldade:** intermediário | Tempo-alvo: 50 min

**Problema:** Um sistema recebe dez solicitações independentes por lote. Cada uma tem probabilidade fixa de falha de 0,20. Quer-se entender a chance de ocorrerem pelo menos três falhas.

**Dados/entrada:** dia_16/parametros.csv: n=10, p=0,20, 10.000 lotes, seed=160. Gere cada lote como contagem binomial com numpy.random.default_rng; os parâmetros são hipóteses didáticas, não estimativas de produção.

**Tarefa:**
1. Calcule a probabilidade teórica de X>=3 por soma da função de massa ou função de sobrevivência.
2. Simule os lotes, compare a frequência empírica e apresente um gráfico de distribuição.

**Entregável esperado:** Código, probabilidade teórica, estimativa simulada e gráfico.

**Critérios de conclusão:**
- [ ] O evento inclui três falhas e não apenas valores acima de três.
- [ ] Simulação é reproduzível e todas as contagens estão entre 0 e 10.
- [ ] A diferença entre teoria e simulação é quantificada e discutida; não exige igualdade exata.

**Perguntas de interpretação:**
- O que deixa de valer se as falhas ocorrerem em cascata?
- Mais simulações corrigiriam uma hipótese de independência falsa?

**Apoio direcionado:** F, caps. 4-5; G, caps. 4-5.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 19 - Por que médias variam menos

**Competência principal:** Probabilidade e amostragem

**Reforço estatístico:** Distribuição amostral da média; desvio padrão e erro padrão.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Tempos individuais são assimétricos. Uma colega afirma que a média de 50 atendimentos tem a mesma dispersão que um atendimento.

**Dados/entrada:** dia_19/parametros.csv. População teórica: exponencial com escala 10 minutos. Simule 2.000 amostras independentes de n=5 e de n=50, com reposição conceitual, seed=190.

**Tarefa:**
1. Compare histogramas dos tempos individuais e das médias dos dois tamanhos.
2. Calcule dispersão das médias e compare com sigma/sqrt(n), usando sigma=10.

**Entregável esperado:** Três distribuições visualizadas e tabela de dispersão.

**Critérios de conclusão:**
- [ ] As médias são calculadas dentro de cada amostra, produzindo 2.000 médias por n.
- [ ] A comparação usa unidades e eixos identificados; seed e ddof da estimativa empírica são registrados.
- [ ] A explicação distingue distribuição dos dados de distribuição de uma estatística.

**Perguntas de interpretação:**
- Aumentar n faz os dados individuais ficarem normais?
- O erro padrão estima que tipo de incerteza?

**Apoio direcionado:** F, cap. 6; G, cap. 6.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 20 - Dispersão de taxas perto de zero

**Competência principal:** pandas e análise exploratória

**Reforço estatístico:** Desvio padrão, unidade e limites do coeficiente de variação.

**Nível de dificuldade:** intermediário | Tempo-alvo: 50 min

**Problema:** Um relatório usa coeficiente de variação para qualquer coluna numérica. Sua tarefa é avaliar se ele comunica bem taxas mensais que podem estar próximas de zero ou negativas.

**Dados/entrada:** dia_20/ipca_2023_2024.csv; IPCA, SGS 433/BCB, produtor IBGE; Brasil, 2023-2024; data e ipca_pct. Acesso alternativo: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. Use os 24 meses; trate a série como sequência temporal descritiva.

**Tarefa:**
1. Compare, por ano, desvio padrão (ddof=0), IQR e coeficiente de variação calculado como s/média.
2. Repita o CV após subtrair 0,40 ponto percentual de cada taxa, apenas como experimento de referência, sem chamar a série transformada de IPCA observado.

**Entregável esperado:** Tabela original/transformada e escolha justificada de medida.

**Critérios de conclusão:**
- [ ] Você diferencia porcentagem de ponto percentual.
- [ ] A série artificial é identificada e a sensibilidade do CV à origem é discutida.
- [ ] Não usa o CV como regra universal nem aplica inferência i.i.d. aos meses.

**Perguntas de interpretação:**
- Qual medida preserva interpretação quando a média se aproxima de zero?
- Mudar a origem da escala deveria alterar uma medida de dispersão absoluta?

**Apoio direcionado:** F, cap. 2; complemento sobre escalas e CV.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 22 - Um intervalo para a média

**Competência principal:** Inferência estatística

**Reforço estatístico:** Intervalo t; estimativa pontual, erro padrão e confiança.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Uma fábrica sorteou 12 embalagens independentes de um processo estável aproximadamente normal. O desvio padrão populacional é desconhecido.

**Dados/entrada:** dia_22/pesos.csv; pesos em gramas. Construa intervalo bilateral de 95% para a média com t de Student, n-1 graus de liberdade. Não confunda especificação de 500 g com observação adicional.

**Tarefa:**
1. Calcule média, desvio amostral, erro padrão, valor crítico e intervalo t.
2. Confira com SciPy e compare a largura com um intervalo de 90% para os mesmos dados.

**Entregável esperado:** Memória das componentes e tabela de dois intervalos.

**Critérios de conclusão:**
- [ ] Usa ddof=1 e erro padrão s/sqrt(n).
- [ ] Limites calculados manualmente e pela biblioteca coincidem até 1e-6.
- [ ] Confiança é interpretada como propriedade do procedimento em repetições, com hipóteses indicadas.

**Perguntas de interpretação:**
- Maior confiança altera a média observada?
- O intervalo descreve 95% dos pesos individuais?

**Apoio direcionado:** F, cap. 6; G, cap. 6.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 23 - Testar sem transformar p em certeza

**Competência principal:** Inferência estatística

**Reforço estatístico:** Teste t de uma média; hipótese, p-valor e efeito.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Um serviço alega média de 10 minutos. Foram sorteados 12 atendimentos independentes de processo aproximadamente normal. A pergunta foi definida antes de ver os dados: a média difere de 10?

**Dados/entrada:** dia_23/atendimento.csv; minutos. Teste bilateral, H0:mu=10, alpha=0,05, desvio populacional desconhecido. Reporte também diferença de médias em minutos e IC95% t.

**Tarefa:**
1. Formule H0/H1, execute o teste e calcule efeito e intervalo.
2. Reescreva a frase de um colega: “p é a probabilidade de a hipótese nula ser verdadeira”, explicando o erro sem trocar por outra certeza.

**Entregável esperado:** Relatório curto: hipóteses, estatística, graus de liberdade, p, efeito, IC e decisão.

**Critérios de conclusão:**
- [ ] Teste é bilateral, com alpha fixado previamente.
- [ ] Decisão e relação entre IC bilateral e valor nulo são consistentes.
- [ ] Conclusão não usa “aceitar H0” como prova nem interpreta p como probabilidade da hipótese.

**Perguntas de interpretação:**
- Um p alto provaria que o serviço cumpre exatamente 10 minutos?
- Que diferença existe entre significância e diferença relevante para o usuário?

**Apoio direcionado:** F, cap. 7; B, cap. 5; G, cap. 7.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 24 - Comparar duas médias com hipóteses claras

**Competência principal:** Inferência estatística

**Reforço estatístico:** Teste de Welch; diferença de médias e incerteza.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Pessoas foram alocadas aleatoriamente a duas interfaces e medidas uma vez. Deseja-se comparar tempo médio de tarefa, sem presumir variâncias iguais. Os tempos são aproximadamente normais em cada população.

**Dados/entrada:** dia_24/grupos.csv; A tem 8 pessoas e B tem 10, sem pareamento. H0:mu_A-mu_B=0, bilateral, alpha=0,05. Efeito relevante foi definido como redução de pelo menos 2 minutos.

**Tarefa:**
1. Calcule resumos, teste t de Welch e diferença A-B.
2. Construa IC95% de Welch usando erro padrão sqrt(sA²/nA+sB²/nB) e graus de liberdade de Welch-Satterthwaite; consulte documentação para a fórmula.

**Entregável esperado:** Tabela, teste, intervalo e decisão separando evidência e relevância.

**Critérios de conclusão:**
- [ ] Observações independentes não são tratadas como pares.
- [ ] Variâncias são amostrais e não são forçadas a ser iguais.
- [ ] O sinal da diferença é consistente e a conclusão considera a margem prática de 2 minutos e a incerteza.

**Perguntas de interpretação:**
- Precisamos de um teste de normalidade para autorizar automaticamente o método?
- Que resultado adicional ajudaria se a amostra fosse muito assimétrica?

**Apoio direcionado:** F, cap. 7; B, caps. 6 e 12. Leitura crítica de pressupostos.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 25 - Antes e depois da mesma pessoa

**Competência principal:** Inferência estatística

**Reforço estatístico:** Pareamento, distribuição das diferenças e causalidade.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Oito pessoas executaram a tarefa antes e depois de um treinamento. Não houve grupo de controle. A análise deve preservar quem é quem.

**Dados/entrada:** dia_25/pares.csv; tempo em minutos; mesmas oito pessoas nos dois momentos. Considere diferenças aproximadamente normais e independentes entre pessoas. Defina d=depois-antes; teste bilateral, alpha=0,05.

**Tarefa:**
1. Analise a distribuição das diferenças, faça teste t pareado e IC95% para a diferença média.
2. Compare o desenho com amostras independentes e discuta o que impede uma conclusão causal forte sobre o treinamento.

**Entregável esperado:** Gráfico de pares ou diferenças, teste e interpretação.

**Critérios de conclusão:**
- [ ] Pares são ligados por pessoa e diferenças mantêm sinal consistente.
- [ ] O teste usa oito diferenças, sem tratar 16 registros como unidades independentes.
- [ ] Conclusão distingue mudança observada de efeito causal identificado.

**Perguntas de interpretação:**
- O que se perde ao embaralhar a coluna depois?
- Como prática, tempo e seleção podem explicar parte da mudança?

**Apoio direcionado:** F, caps. 7-8; B, cap. 12.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 26 - Poucas contagens exigem cuidado

**Competência principal:** Inferência estatística

**Reforço estatístico:** Tabela 2x2; Fisher exato; diferença de proporções.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Um piloto aleatorizado com 20 visitantes compara duas páginas. Algumas células têm poucas pessoas. A equipe quer escolher um teste sem confiar apenas em uma regra automática.

**Dados/entrada:** dia_26/experimento.csv; grupos independentes A:1/10 converteu; B:5/10. Teste bilateral de associação, alpha=0,05. Cada visitante aparece uma única vez.

**Tarefa:**
1. Monte a tabela 2x2 e calcule as proporções e a diferença B-A.
2. Calcule frequências esperadas sob independência e execute Fisher exato bilateral; justifique a escolha diante do tamanho das células.

**Entregável esperado:** Tabela observada/esperada, teste e interpretação de seis linhas.

**Critérios de conclusão:**
- [ ] A orientação da tabela e a definição do efeito estão declaradas.
- [ ] O teste não usa percentuais como se fossem contagens.
- [ ] O relatório distingue ausência de evidência de equivalência e não promete generalização ampla a partir de 20 visitantes.

**Perguntas de interpretação:**
- Por que a aproximação qui-quadrado pode ser frágil aqui?
- A diferença observada basta para decidir que uma página é superior?

**Apoio direcionado:** F, caps. 3 e 8; B, cap. 11.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 27 - Dez chances de anunciar uma descoberta

**Competência principal:** Inferência estatística

**Reforço estatístico:** Erro tipo I, família de testes e Bonferroni.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Dez métricas primárias foram testadas no mesmo experimento. Todos os p-valores fornecidos são de testes válidos individualmente. O relatório quer destacar qualquer p<0,05 sem discutir multiplicidade.

**Dados/entrada:** dia_27/testes.csv; dez p-valores. Família definida: todos os dez testes; alpha familiar=0,05. Para calcular a probabilidade teórica de ao menos um falso positivo, suponha separadamente dez testes independentes sob H0 verdadeira.

**Tarefa:**
1. Compare decisões sem correção com Bonferroni (alpha/10) e calcule p ajustado limitado a 1.
2. Calcule 1-(1-alpha)^10 no cenário teórico e explique onde a independência foi usada.

**Entregável esperado:** Tabela de decisões e crítica do relatório.

**Critérios de conclusão:**
- [ ] Número de testes da família permanece dez, incluindo resultados não significativos.
- [ ] Ajustes não produzem p>1 e o limiar foi definido para a família inteira.
- [ ] O texto distingue controle familiar, alpha por teste e probabilidade posterior de erro de uma descoberta.

**Perguntas de interpretação:**
- Selecionar só os testes significativos antes de corrigir seria válido?
- Qual custo de poder pode acompanhar uma correção conservadora?

**Apoio direcionado:** F, cap. 7; complemento sobre multiplicidade.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 28 - Não detectar não é provar ausência

**Competência principal:** Inferência estatística

**Reforço estatístico:** Erro tipo II, poder, tamanho amostral e simulação.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Um estudo pode não detectar uma diferença de um minuto. Você vai medir o comportamento de um teste quando sabe, na simulação, se há efeito.

**Dados/entrada:** dia_28/parametros.csv. Gere amostras normais independentes com sigma=3, mu=10 sob H0 e mu=11 sob H1. Teste t bilateral contra 10, alpha=0,05; n=15 e 60; 1.000 repetições por cenário; seed=280.

**Tarefa:**
1. Estime taxa de rejeição sob H0 e sob H1 para cada n.
2. Interprete as taxas como erro tipo I aproximado e poder; estime beta=1-poder e discuta variação de Monte Carlo.

**Entregável esperado:** Tabela 2x2 de cenários e parecer sobre desenho de estudo.

**Critérios de conclusão:**
- [ ] O teste estima o desvio em cada amostra, sem usar sigma conhecido para trocá-lo por z.
- [ ] Taxas estão baseadas em 1.000 decisões e sementes são registradas.
- [ ] Você explica erro tipo II e não exige que alpha empírico seja exatamente 0,05.

**Perguntas de interpretação:**
- Aumentar n muda o efeito verdadeiro de um minuto?
- Por que um resultado não significativo de amostra pequena é pouco informativo sobre equivalência?

**Apoio direcionado:** F, caps. 6-7; G, caps. 6-7; complemento simulação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 29 - Uma regressão que você consegue explicar

**Competência principal:** Machine learning

**Reforço estatístico:** Mínimos quadrados; coeficiente, intercepto e resíduo.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Uma imobiliária quer uma referência descritiva de aluguel em função da área. Os oito imóveis são um recorte observacional fictício; a relação não identifica efeito causal da área.

**Dados/entrada:** dia_29/imoveis.csv; area_m2 e aluguel_reais. Use todos os oito casos para ajuste didático; ainda não declare capacidade de generalização. Consulte a fórmula beta1=sum((x-xbarra)(y-ybarra))/sum((x-xbarra)^2).

**Tarefa:**
1. Calcule beta1 e beta0 a partir das somas e confira com LinearRegression.
2. Produza valores ajustados, resíduos y-y_hat e gráfico; estime para 65 m² e discuta separadamente 250 m².

**Entregável esperado:** Modelo escrito em unidades, tabela de resíduos e gráfico.

**Critérios de conclusão:**
- [ ] Coeficientes manual e da biblioteca coincidem até 1e-6.
- [ ] Soma dos resíduos do ajuste com intercepto é aproximadamente zero.
- [ ] Você distingue interpolação de extrapolação e não chama erro de treino de validação.

**Perguntas de interpretação:**
- Qual unidade e significado do coeficiente angular?
- O intercepto representa aluguel confiável de um imóvel de área zero?

**Apoio direcionado:** F, cap. 12; T, pp. 27-29; roadmap E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 30 - Resíduo não é só número que sobra

**Competência principal:** Machine learning

**Reforço estatístico:** Padrão residual; especificação; comparação com baseline.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** O tempo de resposta cresce com a quantidade de usuários. Um ajuste linear pode ter bom R² e ainda deixar estrutura nos erros.

**Dados/entrada:** dia_30/carga.csv; 12 níveis de usuários e tempos em ms. Treine somente usuários 1-8; avalie usuários 9-12. Compare reta com polinômio de grau 2 e baseline constante igual à média de treino. É extrapolação didática, não amostra aleatória.

**Tarefa:**
1. Ajuste os três métodos sem usar os quatro últimos alvos no treino.
2. Compare MAE de treino e avaliação; examine resíduos contra usuários e justifique qual modelo parece adequado e quais riscos permanecem.

**Entregável esperado:** Tabela de erros, gráfico residual e recomendação limitada ao experimento.

**Critérios de conclusão:**
- [ ] Mesmo recorte de treino e avaliação para todos os métodos.
- [ ] Baseline calcula sua média apenas no treino; transformação polinomial não usa alvo de avaliação.
- [ ] A recomendação usa padrão residual e extrapolação, sem escolher só o maior R² de treino.

**Perguntas de interpretação:**
- Um resíduo médio próximo de zero garante especificação adequada?
- Por que quatro casos de avaliação não sustentam conclusão definitiva?

**Apoio direcionado:** F, cap. 12; complemento validação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 31 - A métrica muda a preferência

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** MAE, RMSE, erro quadrático e influência de extremos.

**Nível de dificuldade:** intermediário | Tempo-alvo: 55 min

**Problema:** Dois modelos têm previsões prontas para os mesmos seis pedidos. Não há treino neste exercício; o foco é escolher o critério que corresponde ao custo do erro.

**Dados/entrada:** dia_31/previsoes.csv; real, modelo_A, modelo_B em unidades vendidas. Cenário 1: cada unidade de erro absoluto custa igual. Cenário 2: grandes erros recebem custo proporcional ao quadrado do erro.

**Tarefa:**
1. Calcule erro assinado, absoluto e quadrático por caso; depois MAE e RMSE.
2. Faça análise de sensibilidade removendo o último caso somente da comparação adicional, preservando o resultado principal.

**Entregável esperado:** Tabela por caso, resumo por modelo e escolha nos dois cenários.

**Critérios de conclusão:**
- [ ] Ambos usam os mesmos seis casos na comparação principal.
- [ ] RMSE aplica raiz à média dos quadrados, não à soma.
- [ ] A decisão conecta métrica e custo; a sensibilidade não é usada para apagar resultado inconveniente.

**Perguntas de interpretação:**
- Por que não existe uma métrica universalmente melhor?
- Qual risco há em excluir o caso mais difícil após ver quem perde?

**Apoio direcionado:** F, cap. 12; roadmap E2; complemento métricas.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 32 - Aprender a separar antes de transformar

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Vazamento de dados; separação treino/teste.

**Nível de dificuldade:** intermediário | Tempo-alvo: 60 min

**Problema:** Uma equipe padroniza todos os dados antes de separar treino e teste. Você vai comparar esse fluxo com uma separação correta e explicar o problema mesmo se as métricas ficarem parecidas.

**Dados/entrada:** dia_32/iris.csv; Iris/UCI, 150 plantas, quatro medidas em cm e target 0=setosa, 1=versicolor, 2=virginica; row_id é identificador, excluído dos atributos. Fonte: https://archive.ics.uci.edu/dataset/53/iris. Cópia do load_iris do scikit-learn incluída.

**Tarefa:**
1. Separe 70/30 com stratify=target e random_state=32. Compare StandardScaler ajustado em tudo versus somente no treino, seguido de KNN k=5.
2. Inspecione médias de ajuste do scaler e acurácia; marque o fluxo global como demonstração de erro, sem recomendá-lo.

**Entregável esperado:** Dois fluxos identificados, métricas e diagnóstico.

**Critérios de conclusão:**
- [ ] Não inclui row_id nem target em X.
- [ ] No fluxo correto, fit do scaler e do modelo acessa apenas treino; teste só usa transform/predict.
- [ ] Você reconhece vazamento como falha de procedimento mesmo sem aumento de acurácia.

**Perguntas de interpretação:**
- Por que resultado semelhante não valida o fluxo errado?
- Como Pipeline ajudaria quando a separação é por folds?

**Apoio direcionado:** Roadmap E2; complemento de avaliação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 33 - Um pipeline mínimo de classificação

**Competência principal:** Machine learning

**Reforço estatístico:** Padronização, probabilidades e avaliação multiclasse.

**Nível de dificuldade:** intermediário | Tempo-alvo: 65 min

**Problema:** Um laboratório quer classificar amostras de vinho em três cultivares usando medidas químicas. Não se trata de prever qualidade ou gosto.

**Dados/entrada:** dia_33/wine.csv; Wine/UCI, 178 amostras, 13 atributos, target 0/1/2 para cultivar, row_id excluído. Fonte: https://archive.ics.uci.edu/dataset/109/wine. Treino/teste 75/25, estratificado, random_state=33. Campos são os nomes de load_wine; unidades variam, não as invente.

**Tarefa:**
1. Ajuste Pipeline(StandardScaler, LogisticRegression(max_iter=2000)) e baseline DummyClassifier(strategy="most_frequent").
2. Avalie acurácia, macro-F1 e matriz de confusão no mesmo teste. Inspecione dois erros, se houver; caso contrário, discuta a limitação do teste pequeno.

**Entregável esperado:** Código, tabela comparativa e interpretação por classe.

**Critérios de conclusão:**
- [ ] Transformações são ajustadas no treino; mesmo split para baseline e modelo.
- [ ] Macro-F1 não é confundido com média ponderada por suporte.
- [ ] Alvo e identificador ficam fora das features e probabilidades por linha somam aproximadamente 1.

**Perguntas de interpretação:**
- Por que padronizar medidas químicas de escalas distintas?
- Uma acurácia alta prova desempenho em qualquer região e safra?

**Apoio direcionado:** F, cap. 13; roadmap E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 34 - Complexidade e overfitting

**Competência principal:** Machine learning

**Reforço estatístico:** Viés, variância e desempenho de treino/validação.

**Nível de dificuldade:** intermediário | Tempo-alvo: 65 min

**Problema:** Uma árvore profunda consegue memorizar amostras pequenas. Você deve escolher complexidade antes de observar o teste final.

**Dados/entrada:** dia_34/iris.csv; Iris/UCI, 150 plantas, quatro atributos em cm e target 0/1/2; row_id excluído. Fonte: https://archive.ics.uci.edu/dataset/53/iris. Primeiro reserve 20% de teste estratificado (seed=34); no restante reserve 25% para validação (seed=35).

**Tarefa:**
1. Compare DecisionTreeClassifier com max_depth=1,2,4,None (random_state=34), usando somente treino e validação.
2. Escolha por macro-F1 de validação; empate até 1e-12 favorece menor profundidade. Reajuste no desenvolvimento completo e avalie uma vez no teste.

**Entregável esperado:** Curva/tabela de complexidade e registro da escolha antes do teste.

**Critérios de conclusão:**
- [ ] Teste não participa da escolha; índices dos três subconjuntos não se sobrepõem.
- [ ] Há métricas de treino e validação para quatro profundidades e somente um resultado final de teste.
- [ ] Você discute overfitting sem exigir que uma árvore específica necessariamente perca.

**Perguntas de interpretação:**
- Maior pontuação de treino equivale a melhor modelo?
- Como o tamanho pequeno da validação afeta a escolha?

**Apoio direcionado:** Roadmap E2; complemento viés/variância.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 35 - Validação cruzada também tem limites

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Variação entre folds; seleção e teste reservado.

**Nível de dificuldade:** intermediário | Tempo-alvo: 65 min

**Problema:** Uma equipe anuncia a melhor média de validação como se fosse uma avaliação final independente. Você deve distinguir seleção de hiperparâmetro e teste.

**Dados/entrada:** dia_35/wine.csv; Wine/UCI; 178 casos, 13 atributos, target 0/1/2, sem row_id em X. Fonte: https://archive.ics.uci.edu/dataset/109/wine. Reserve 25% teste estratificado, seed=35; no desenvolvimento use StratifiedKFold(5,shuffle=True,random_state=35).

**Tarefa:**
1. Compare Pipeline de padronização + KNN com k=3,5,9 nos mesmos folds, por macro-F1.
2. Escolha maior média; empate até 1e-12 favorece maior k. Ajuste no desenvolvimento e avalie uma vez no teste. Reporte os cinco valores e o desvio, sem tratá-los como observações independentes.

**Entregável esperado:** Tabela por fold, regra registrada e resultado final.

**Critérios de conclusão:**
- [ ] Scaler é reajustado dentro de cada fold, via Pipeline.
- [ ] Teste permanece separado da busca.
- [ ] Desvio entre folds é descrição de estabilidade, não IC95% automático da generalização.

**Perguntas de interpretação:**
- Por que escolher o melhor k e reportar apenas sua CV pode ser otimista?
- Repetir splits até melhorar o teste mantém o teste reservado?

**Apoio direcionado:** Roadmap E2; complemento validação cruzada.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 36 - O futuro não pode treinar o passado

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Validação temporal; baseline; erro fora da amostra.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Uma previsão de inflação mensal usa embaralhamento aleatório e parece boa. A tarefa é montar uma avaliação histórica pequena coerente com a informação disponível.

**Dados/entrada:** dia_36/ipca_2023_2024.csv; SGS433/BCB, produtor IBGE, Brasil, 2023-2024; data e ipca_pct. Endpoint: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. Defina X_t=taxa do mês anterior e alvo=taxa do mês t. Janeiro/2023 fica sem lag; o alvo só é previsto após publicação do mês anterior.

**Tarefa:**
1. Treine regressão linear com alvos de fev-dez/2023 e congele coeficientes.
2. Avalie alvos jan-dez/2024 usando o lag real disponível em cada origem e compare com persistência y_hat_t=y_(t-1), por MAE e gráfico. Não ajuste no teste.

**Entregável esperado:** Tabela de 12 previsões, cortes e métricas, com limitações.

**Critérios de conclusão:**
- [ ] Nenhuma feature consulta o próprio alvo ou o mês seguinte.
- [ ] Regressão e persistência usam os mesmos 12 meses de avaliação.
- [ ] A tarefa é reconhecida como previsão um passo adiante com origens sucessivas, não previsão simultânea dos 12 meses.

**Perguntas de interpretação:**
- Por que um split aleatório altera o significado da avaliação?
- Com 11 alvos de treino, o que você pode afirmar com segurança?

**Apoio direcionado:** Roadmap E2; F, cap. 12; complemento temporal.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 37 - Acurácia alta pode esconder falhas

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Matriz de confusão, precisão, recall e prevalência.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 55 min

**Problema:** Um sistema detecta fraude fictícia rara. Dois classificadores já produziram previsões; não é necessário treiná-los. A equipe anuncia somente acurácia.

**Dados/entrada:** dia_37/alertas.csv; contagens de grupos de eventos disjuntos. Classe positiva=fraude (1); negativos=0. A é constante zero; B varia conforme a coluna. Trate quantidade como peso de frequência, total de 100 eventos.

**Tarefa:**
1. Construa matrizes ponderadas de cada modelo e calcule acurácia, precisão, recall e F1.
2. Adote convenção precision=0 quando não há predição positiva, declarando a divisão sem denominador e a convenção. Compare com o objetivo de encontrar fraudes.

**Entregável esperado:** Tabela de métricas e crítica do anúncio.

**Critérios de conclusão:**
- [ ] Contagens ponderam quantidade, não só as quatro linhas agregadas.
- [ ] Classe positiva e convenção de divisão indefinida são explícitas.
- [ ] A conclusão informa prevalência e não interpreta precisão como recall.

**Perguntas de interpretação:**
- Por que prever sempre negativo pode ter boa acurácia?
- Qual métrica responde à fração dos alertas que é fraude?

**Apoio direcionado:** F, cap. 13; roadmap E2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 38 - Escolher o limiar pelo custo

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Decisão probabilística; custo esperado empírico.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Uma análise atribui custo 1 a falso positivo e custo 5 a falso negativo. Você recebe scores de validação e deve escolher um limiar sem acessar um teste.

**Dados/entrada:** dia_38/validacao.csv; 12 casos independentes fictícios de validação, real em 0/1 e score em [0,1]. Candidatos: 0,2;0,4;0,6;0,8. Prediga positivo se score>=limiar. Custo total=FP+5*FN. Não há conjunto de teste nesta atividade.

**Tarefa:**
1. Calcule matriz, custo total, precisão e recall para os quatro limiares.
2. Escolha menor custo; empate favorece limiar maior. Explique que a estimativa de desempenho final ainda falta.

**Entregável esperado:** Tabela de trade-offs e regra de decisão documentada.

**Critérios de conclusão:**
- [ ] Convenção >= é aplicada também nos valores de fronteira.
- [ ] A regra usa somente validação; custos são aplicados às contagens corretas.
- [ ] Você não chama scores de probabilidades calibradas sem evidência e não chama o custo escolhido de resultado final de teste.

**Perguntas de interpretação:**
- Mudar o custo dos falsos negativos pode mudar o limiar?
- Como uma prevalência diferente em produção afetaria essa decisão?

**Apoio direcionado:** F, cap. 13; complemento seleção de limiar.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 39 - Comparar modelos preservando os pares

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Bootstrap pareado; intervalo da diferença de erros.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Dois modelos foram avaliados nos mesmos 12 casos independentes, sorteados da população de interesse. A diferença entre as médias de erro precisa ser acompanhada de incerteza.

**Dados/entrada:** dia_39/erros.csv; erros absolutos já calculados, mesma unidade para A e B. Delta=MAE_A-MAE_B. Bootstrap pareado: 5.000 reamostras de índices dos 12 casos, seed=390, IC percentil95%.

**Tarefa:**
1. Calcule delta e intervalo reamostrando casos inteiros, preservando A/B.
2. Compare a conclusão com a simples ordenação das médias e indique o que mudaria se os casos fossem dias consecutivos dependentes.

**Entregável esperado:** Estimativa, intervalo e parecer sobre força da comparação.

**Critérios de conclusão:**
- [ ] Uma mesma seleção de índices é aplicada às duas colunas em cada reamostra.
- [ ] Unidade de análise é o caso e o sinal de delta é explicado.
- [ ] Você discute incerteza, dependência e amostra pequena; não força superioridade quando o resultado não sustenta.

**Perguntas de interpretação:**
- Por que reamostrar A e B separadamente perde informação?
- Um intervalo que inclui zero prova equivalência?

**Apoio direcionado:** F, caps. 6-7; complemento bootstrap pareado.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 40 - Um contrato de dados que detecta falhas

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Sem conexão estatística central; foco em qualidade e testes.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Um pipeline deve impedir dados inválidos de chegar a uma análise. Você precisa distinguir erro de regra, ausência permitida e conflito de chave.

**Dados/entrada:** dia_40/lote.csv. Contrato: id único e não vazio; idade inteira 0-120; renda >=0 ou ausente; segmento em A/B. Rendas ausentes são permitidas com aviso. IDs duplicados com conteúdo diferente vão todos à quarentena; não escolher versão arbitrariamente.

**Tarefa:**
1. Implemente validação que retorna linhas válidas e relatório de problemas.
2. Escreva testes para lote válido, idade inválida, renda ausente, segmento inválido e duplicação conflitante.

**Entregável esperado:** Função, testes e auditoria reproduzível.

**Critérios de conclusão:**
- [ ] Ausência de renda é aviso, não exclusão automática; zero permanece válido.
- [ ] Ambas as versões conflitantes são rastreadas e não aparecem como dados limpos.
- [ ] Testes verificam comportamento de contrato e mensagens, não apenas repetem a implementação.

**Perguntas de interpretação:**
- Por que escolher a primeira duplicata pode esconder uma decisão de negócio?
- Que regra precisaria ser negociada antes de imputar renda?

**Apoio direcionado:** Roadmap E1 e E3; T, pp. 10-12.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 42 - Diagnosticar uma média no serviço

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Média por unidade de análise; zeros e ausência.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Uma API promete gasto médio por cliente cadastrado, incluindo clientes sem compra. A consulta existente calcula AVG(p.valor) após INNER JOIN. Você precisa corrigir o resultado e proteger o contrato.

**Dados/entrada:** dia_42/pedidos.csv, dia_42/clientes.csv e dia_42/consulta_com_erro.sql. Cadastros A/Norte, B/Sul, C/Sul; pedidos A/10,A/20,B/30. Todos os pedidos do período estão presentes; sem pedido significa gasto zero neste período.

**Tarefa:**
1. Identifique os dois problemas de granularidade/cobertura e escreva consulta correta.
2. Implemente uma função de serviço local que recebe a região e devolve clientes e média; região inexistente deve produzir erro explícito, não média zero. Teste ambos os grupos e o caso inexistente.

**Entregável esperado:** SQL corrigido, função, testes e explicação.

**Critérios de conclusão:**
- [ ] Agrega primeiro por cliente e inclui cadastrados sem pedido.
- [ ] Contagem de clientes usa cadastro, sem inflação por pedidos.
- [ ] Região inexistente é diferente de clientes existentes com gasto zero; testes capturam a diferença.

**Perguntas de interpretação:**
- Qual diferença entre média por pedido e por cliente?
- Por que aqui zero é adequado para ausência de pedido, mas nem toda ausência deve virar zero?

**Apoio direcionado:** Roadmap E1 e E3; F, cap. 2.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 45 - Acertar um trecho não é recuperar todos

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Hit@k, Recall@k, Precision@k e denominadores.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 60 min

**Problema:** Duas buscas têm rankings prontos. A equipe chama todas as métricas de “acurácia do RAG”, incluindo uma pergunta sem resposta no acervo.

**Dados/entrada:** dia_45/ranking.csv; IDs separados por ponto e vírgula. Relevantes são conjunto de referência; Q4 não tem nenhum documento relevante. k=3. Hit@3=1 se algum relevante foi recuperado. Recall=recuperados relevantes/total relevante; Precision=recuperados relevantes/3.

**Tarefa:**
1. Calcule as três métricas por pergunta respondível e média macro nas Q1-Q3.
2. Para Q4 registre que recall é indefinido e não a inclua no macro de respondíveis; discuta separadamente por que a busca ainda retorna candidatos.

**Entregável esperado:** Tabela por pergunta, resumo por sistema e explicação dos denominadores.

**Critérios de conclusão:**
- [ ] Interseções tratam IDs como conjuntos, sem duplicar evidência.
- [ ] Hit e recall não são confundidos quando há mais de um relevante.
- [ ] Q4 não recebe recall zero silenciosamente nem vira prova de que o sistema sabe recusar resposta.

**Perguntas de interpretação:**
- Bom Hit@3 garante que a resposta gerada seja correta?
- Que métrica ajuda quando a resposta exige dois documentos?

**Apoio direcionado:** Roadmap E5; complemento métricas de recuperação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 47 - JSON válido ainda pode estar errado

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Taxas de validade sintática, de esquema e de fundamentação.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Um extrator fictício recebe um documento por vez e devolve prazo e custo. As respostas já foram coletadas; você deve auditar camadas de qualidade distintas.

**Dados/entrada:** dia_47/corpus.csv e dia_47/saidas.csv; oito textos e seis saídas fictícias. Contrato estrito: prazo_dias inteiro>=0 ou null; custo_reais número>=0 ou null; fonte igual ao documento recebido; sem campos extras. Prazo só representa devolução/emissão, nunca viagens por dia; não inventar valor quando ausente. Registrar dias úteis quando o texto o disser, em observação da auditoria.

**Tarefa:**
1. Valide parsing e esquema sem converter strings numéricas automaticamente.
2. Revise semanticamente as seis saídas contra os textos, incluindo unidade, ausência e fonte; calcule três taxas separadas, todas sobre seis saídas.

**Entregável esperado:** Validador, matriz de auditoria por camada e explicação de duas falhas.

**Critérios de conclusão:**
- [ ] Saída que não parseia conta como falha de parsing, esquema e fundamentação no resumo sobre seis.
- [ ] Um JSON com tipos corretos não é automaticamente aprovado semanticamente.
- [ ] Cada rejeição cita trecho ou regra; nenhuma chamada paga é necessária.

**Perguntas de interpretação:**
- Por que validar com Pydantic não prova que a resposta é verdadeira?
- Quando null é mais fiel do que zero?

**Apoio direcionado:** Roadmap E3-E5; complemento de avaliação estruturada.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 48 - Um prompt melhor sob qual critério?

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Comparação pareada; discordâncias; custo.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Duas versões de prompt foram avaliadas nas mesmas 12 perguntas independentes por uma rubrica fixa. O prompt B usa mais tokens. O teste pequeno não deve virar uma promessa ampla.

**Dados/entrada:** dia_48/prompts.csv; correto=1, incorreto=0; tokens são totais por chamada. Preço didático único=R$0,01 por 1.000 tokens. Para teste exato de discordâncias: b=A acerta/B erra; c=A erra/B acerta; sob H0, b em b+c segue Binomial(b+c,0,5).

**Tarefa:**
1. Monte a tabela pareada 2x2, taxas de acerto, diferença e custos totais.
2. Execute teste binomial bilateral nas discordâncias, alpha=0,05; se b+c=0, reporte ausência de discordâncias sem inventar um teste. Recomende próximo passo considerando evidência e custo.

**Entregável esperado:** Tabela pareada, métricas, teste e recomendação.

**Critérios de conclusão:**
- [ ] Perguntas iguais são comparadas como pares; não trata 24 julgamentos como amostras independentes.
- [ ] Custos usam divisão por 1.000 e a mesma tarifa.
- [ ] O texto distingue melhoria observada, evidência estatística e relevância prática.

**Perguntas de interpretação:**
- Por que concordâncias não entram na contagem binomial das discordâncias?
- O que precisaria mudar se as 12 perguntas fossem todas variações de duas dúvidas?

**Apoio direcionado:** F, caps. 5 e 7; roadmap E4-E5; complemento comparação pareada.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 49 - Falha de busca, de resposta ou de fonte?

**Competência principal:** Avaliação de aplicações de IA

**Reforço estatístico:** Rubrica de qualidade e análise de erros por categoria.

**Nível de dificuldade:** intermediário/avançado | Tempo-alvo: 65 min

**Problema:** Um assistente de portal produziu seis respostas simuladas. Você precisa avaliar fidelidade e classificar falhas sem considerar qualquer recusa como sucesso.

**Dados/entrada:** dia_49/casos.csv. Fontes permitidas por caso: C1/D1, C2/D2, C3/D7, C4/D4, C5/D6, C6/D8; cada contexto do CSV é a evidência completa da respectiva pergunta. Dados são fictícios e nenhum endereço deve ser acessado.

**Tarefa:**
1. Defina rubrica: correção, suporte no contexto, fonte válida e recusa adequada; avalie cada resposta.
2. Classifique falhas observadas e escreva três novos casos de teste (não execute LLM). Separe instruções do sistema de conteúdo documental em um template de prompt.

**Entregável esperado:** Auditoria de seis casos, rubrica e três testes adicionais.

**Critérios de conclusão:**
- [ ] Responder sem evidência e recusar quando há evidência são ambos avaliados como problemas.
- [ ] Citação existente não prova suporte; fonte incorreta é registrada separadamente.
- [ ] O template é descrito como medida parcial: não alega resolver ataques apenas por palavras proibidas ou delimitação.

**Perguntas de interpretação:**
- Qual diferença entre citar uma fonte e ser sustentado por ela?
- Por que um conjunto simulado não comprova robustez de um LLM real?

**Apoio direcionado:** Roadmap E4-E5; complemento testes adversariais.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 50 - O agregado esconde quem recebe o erro

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Métricas condicionais, prevalência e tamanho de grupo.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 65 min

**Problema:** Um classificador de necessidade de suporte atende usuários de app e web. O relatório usa só uma métrica global. Os canais têm tamanhos e prevalências diferentes.

**Dados/entrada:** dia_50/segmentos.csv; cada linha é célula de confusão com frequência n. Classe positiva=precisa de suporte; sem pessoa duplicada. Nenhum canal é amostra representativa de todos os usuários futuros por garantia.

**Tarefa:**
1. Escolha e calcule métricas globais e por canal, incluindo obrigatoriamente recall, taxa de falsos positivos e suporte de classe.
2. Recomende uma investigação antes de mudar limiares ou prometer equidade; justifique os denominadores e a influência do grupo menor.

**Entregável esperado:** Tabela estratificada, visualização escolhida e parecer de até 250 palavras.

**Critérios de conclusão:**
- [ ] Células usam n como peso e totais conciliam com o agregado.
- [ ] Recall e FPR usam denominadores diferentes corretamente.
- [ ] O parecer distingue diferença observada, incerteza por grupo e causas não demonstradas; não resolve o problema apenas igualando taxas.

**Perguntas de interpretação:**
- Uma boa taxa global assegura bom atendimento em cada canal?
- Qual informação faltaria para explicar por que os erros diferem?

**Apoio direcionado:** F, caps. 3 e 13; roadmap E2/E7; complemento avaliação por segmento.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 52 - Monitorar sem esconder as falhas

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Mediana, P95, denominadores e viés por sobrevivência.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 65 min

**Problema:** Um serviço anuncia latência média apenas nas respostas bem-sucedidas. Você deve construir um resumo operacional que também represente erros e cauda de latência.

**Dados/entrada:** dia_52/logs.csv; 20 requisições; latência observada de cada tentativa em ms, inclusive timeout de 1.000 ms; tokens faturados somente conforme a coluna. Meta didática: falhas<=5% e P95 das respostas ok<=500 ms. Quantis lineares; custo R$0,01/1.000 tokens.

**Tarefa:**
1. Calcule sucesso/falha sobre todas as tentativas; compare média, mediana e P95 para sucessos e para todas as tentativas.
2. Avalie as duas metas, calcule custo total e por resposta bem-sucedida, e recomende uma investigação prioritária.

**Entregável esperado:** Painel tabular, uma visualização e parecer operacional.

**Critérios de conclusão:**
- [ ] Falhas incluem timeout e erro; denominador é 20.
- [ ] P95 declara subconjunto e convenção; custo não descarta tokens de falhas caso existissem.
- [ ] Relatório não transforma observação de timeout em latência real de processamento após o corte.

**Perguntas de interpretação:**
- Por que excluir timeout pode melhorar artificialmente a aparência do serviço?
- Uma média baixa assegura boa experiência para quem está na cauda?

**Apoio direcionado:** F, cap. 2; roadmap E7.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 53 - Ferramentas limitadas antes de agentes

**Competência principal:** Engenharia de software e APIs

**Reforço estatístico:** Sem conexão estatística central; roteamento e controle de execução.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 70 min

**Problema:** Um futuro copiloto precisa combinar consulta numérica e documental. O exercício é um roteador determinístico pequeno, preparando os contratos de ferramentas antes de envolver um LLM.

**Dados/entrada:** dia_53/pedidos.csv e os dois CSVs ferramenta_*. Dados: A=120,B=80; documento chave prazo informa 2 dias úteis/fonte D1. Tipo dados chama consulta numérica; documento chama prazo; hibrida chama ambas e usa argumento como grupo. Escrita e outro são proibidos. Falha indica o mock que deve lançar timeout.

**Tarefa:**
1. Implemente funções de leitura e roteador com tipos explícitos, trace de chamadas e máximo de duas ferramentas por pedido.
2. Trate grupo inexistente, timeout e tipo proibido sem executar comandos livres. Em híbrida com falha de dados, devolva resultado parcial identificado, sem inventar total.

**Entregável esperado:** Código, oito resultados e testes de limite/comportamento.

**Critérios de conclusão:**
- [ ] Todos os oito pedidos terminam e respeitam no máximo duas chamadas.
- [ ] Proibidos não acionam ferramenta; fonte documental e número são preservados.
- [ ] Resultado parcial é distinto de sucesso completo; você não apresenta o roteador como sistema multiagente pronto.

**Perguntas de interpretação:**
- Que contrato já pode ser testado antes de conectar um LLM?
- Por que permitir SQL ou código livre muda o risco e o escopo?

**Apoio direcionado:** Roadmap E3 e preparação conceitual para E6.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


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


## Dia 55 - Receber um problema e escolher um caminho

**Competência principal:** Machine learning

**Reforço estatístico:** Escolha de métrica; validação; estabilidade e interpretação.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 80 min

**Problema:** Um laboratório recebe um lote de medidas químicas e quer uma prova de conceito reproduzível para distinguir cultivares. Você define a abordagem, respeitando um orçamento pequeno de comparação.

**Dados/entrada:** dia_55/wine.csv; Wine/UCI, 178 amostras, 13 atributos químicos, target 0/1/2, row_id excluído. Fonte: https://archive.ics.uci.edu/dataset/109/wine. Reserve 25% teste estratificado com seed=55. Limite: baseline + no máximo dois tipos de modelo, até três configurações por tipo; sem dados externos.

**Tarefa:**
1. Defina métrica principal e protocolo antes de medir; faça diagnóstico curto, prepare dados e compare no desenvolvimento com CV estratificada de 4 folds (shuffle=True,seed=55).
2. Congele a escolha e avalie uma única vez no teste; reporte por classe, limitações e uma melhoria ligada a falha observada.

**Entregável esperado:** Notebook/script reexecutável e relatório de até 400 palavras.

**Critérios de conclusão:**
- [ ] O procedimento justifica métrica, transformação e escolha; alvo e ID não vazam.
- [ ] Transformações são internas ao Pipeline/CV, e teste permanece fora da busca.
- [ ] Há baseline, métricas por classe e análise honesta; não precisa superar uma meta artificial para concluir.
- [ ] Tempo de treino é limitado: não amplia a busca para perseguir resultado de teste.

**Perguntas de interpretação:**
- Que decisão foi sustentada pelos dados e qual ainda depende de hipótese?
- Como você demonstraria que a execução é reproduzível em outro ambiente?

**Apoio direcionado:** F, cap. 13; roadmap E1-E3; complemento validação.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## Dia 56 - Auditoria final: defender uma decisão

**Competência principal:** Avaliação e validação de modelos

**Reforço estatístico:** Vazamento temporal; erro, heterogeneidade e limites de evidência.

**Nível de dificuldade:** avançado dentro do escopo atual | Tempo-alvo: 80 min

**Problema:** Você recebeu dados oficiais, previsões prontas e metadados. A equipe recomenda o modelo de menor erro. Seu papel é auditar a validade da comparação antes de recomendar qualquer uso.

**Dados/entrada:** dia_56/ipca_2023_2024.csv, dia_56/previsoes_recebidas.csv e metadados.json. IPCA SGS433/BCB, produtor IBGE; Brasil 2023-2024. Fonte alternativa: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024. Alvos jan-dez/2024; previsão feita após publicação do mês anterior. Há persistência, regressão linear e modelo_C; leia integralmente os metadados.

**Tarefa:**
1. Audite datas, unidades, chaves, cobertura e informação disponível de cada candidato. Defina elegibilidade antes da ordenação.
2. Escolha uma métrica principal justificada, compare candidatos elegíveis nos mesmos meses e examine erros por semestre. Produza um gráfico e recomendação com limites; não treine nem ajuste no teste.

**Entregável esperado:** Relatório independente de até 500 palavras, código de auditoria, tabela de erros e gráfico.

**Critérios de conclusão:**
- [ ] As 12 datas de previsão conciliam por chave com o observado; nenhuma junção posicional silenciosa.
- [ ] A decisão distingue erro baixo de protocolo válido; cada exclusão possui evidência dos metadados.
- [ ] A avaliação não usa os 12 meses como se fossem amostra i.i.d. para um IC ingênuo e não declara causalidade.
- [ ] O relatório registra recomendação, incerteza e próximo teste; um resultado desfavorável ao modelo complexo é aceitável.

**Perguntas de interpretação:**
- Qual resultado aparente você rejeitaria por invalidade do procedimento?
- O que você consegue defender agora e o que precisaria observar em um período novo?

**Apoio direcionado:** Roadmap E1-E3/E7; F, cap. 12; complemento auditoria temporal.

**Registro:** data: ____ | tempo: ____ | concluído: [ ]

**Minha resposta / evidências:**


**Dúvida que restou:**


## 4. Mapa de competências

Uma competência principal por dia; total=56. As retomadas estatísticas abaixo são transversais e podem se sobrepor.

| Competência principal | Dias | Quantidade |
|---|---|---|
| Python e estruturas de dados | 1 | 1 |
| Estatística descritiva | 2, 3, 4, 5, 7 | 5 |
| Limpeza e qualidade de dados | 6, 11 | 2 |
| pandas e análise exploratória | 8, 14, 20 | 3 |
| Análise bivariada e visualização | 9, 10 | 2 |
| SQL | 12, 13 | 2 |
| Probabilidade e amostragem | 15, 16, 17, 18, 19 | 5 |
| Inferência estatística | 21, 22, 23, 24, 25, 26, 27, 28 | 8 |
| Machine learning | 29, 30, 33, 34, 55 | 5 |
| Avaliação e validação de modelos | 31, 32, 35, 36, 37, 38, 39, 50, 51, 56 | 10 |
| Engenharia de software e APIs | 40, 41, 42, 52, 53 | 5 |
| NLP e recuperação de informação | 43, 44 | 2 |
| Avaliação de aplicações de IA | 45, 46, 47, 48, 49, 54 | 6 |

### Conteúdos estatísticos recorrentes

| Conteúdo | Dias | Quantidade |
|---|---|---|
| Tipos de variáveis | 1 | 1 |
| Tendência central | 3, 7, 8, 11, 14, 18, 20, 42 | 8 |
| Dispersão e quantis | 4, 5, 8, 17, 19, 20, 21, 22, 35, 52 | 10 |
| Frequências e denominadores | 2, 13, 15, 43, 45, 52 | 6 |
| Ponderação e granularidade | 7, 10, 12, 13, 42, 50 | 6 |
| Valores extremos | 3, 5, 31 | 3 |
| Ausência e seu impacto | 6, 11 | 2 |
| Amostragem e representatividade | 1, 4, 11, 18, 19, 21, 22, 39, 46, 50, 54 | 11 |
| Associação e confundimento | 9, 10, 25, 29 | 4 |
| Probabilidade e condicionamento | 10, 15, 16, 17, 26, 27, 37, 46, 48 | 9 |
| Distribuições | 14, 16, 19, 51 | 4 |
| Simulação de variabilidade | 16, 17, 19, 21, 28 | 5 |
| Intervalos e incerteza | 21, 22, 23, 24, 25, 39, 46, 54 | 8 |
| Testes e interpretação de hipóteses | 23, 24, 25, 26, 27, 28, 48 | 7 |
| Erros tipo I/II e poder | 27, 28 | 2 |
| Efeito e relevância prática | 23, 24, 26, 28, 48, 54 | 6 |
| Regressão | 29, 30, 36 | 3 |
| Resíduos e diagnóstico | 29, 30, 56 | 3 |
| Métricas e comparação | 30, 31, 32, 33, 34, 36, 37, 38, 39, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56 | 20 |
| Validação e desenho de avaliação | 30, 31, 32, 33, 34, 35, 36, 38, 39, 44, 51, 55, 56 | 13 |
| Vazamento de dados | 32, 35, 36, 55, 56 | 5 |
| Viés e variância em modelos | 34 | 1 |
| Classificação | 33, 37, 38, 50, 55 | 5 |

## 5. Mapa de bases públicas utilizadas

As cópias locais são o fallback principal. Os enunciados indicam recorte, colunas e URL alternativa; nenhum exercício depende de baixar novos dados.

| Dia | Base | Órgão/repositório | Link | Finalidade |
|---|---|---|---|---|
| 8 | IPCA, SGS 433 | IBGE (produção); BCB (distribuição) | https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433 | Primeira análise de uma série oficial |
| 14 | IPCA, SGS 433 | IBGE (produção); BCB (distribuição) | https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433 | Um gráfico para cada pergunta |
| 20 | IPCA, SGS 433 | IBGE (produção); BCB (distribuição) | https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433 | Dispersão de taxas perto de zero |
| 32 | Iris | UCI; cópia de load_iris/scikit-learn | https://archive.ics.uci.edu/dataset/53/iris | Aprender a separar antes de transformar |
| 33 | Wine | UCI; cópia de load_wine/scikit-learn | https://archive.ics.uci.edu/dataset/109/wine | Um pipeline mínimo de classificação |
| 34 | Iris | UCI; cópia de load_iris/scikit-learn | https://archive.ics.uci.edu/dataset/53/iris | Complexidade e overfitting |
| 35 | Wine | UCI; cópia de load_wine/scikit-learn | https://archive.ics.uci.edu/dataset/109/wine | Validação cruzada também tem limites |
| 36 | IPCA, SGS 433 | IBGE (produção); BCB (distribuição) | https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433 | O futuro não pode treinar o passado |
| 41 | IPCA, SGS 433 | IBGE (produção); BCB (distribuição) | https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433 | Uma API pode falhar sem estragar os dados |
| 55 | Wine | UCI; cópia de load_wine/scikit-learn | https://archive.ics.uci.edu/dataset/109/wine | Receber um problema e escolher um caminho |
| 56 | IPCA, SGS 433 | IBGE (produção); BCB (distribuição) | https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433 | Auditoria final: defender uma decisão |

### Recortes e acesso

**IPCA, SGS 433:** 24 taxas mensais, Brasil, jan/2023-dez/2024. data; ipca_pct, % mensal. Endpoint exato no enunciado; original JSON incluído no Dia 41. Fonte: https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433

**Iris:** 150 plantas; 4 medidas em cm, target 0/1/2 e row_id. Recorte completo; variante fornecida é a cópia do scikit-learn. Fonte: https://archive.ics.uci.edu/dataset/53/iris

**Wine:** 178 amostras; 13 atributos químicos, target 0/1/2 e row_id. Recorte completo. Cultivar, não nota de qualidade. Fonte: https://archive.ics.uci.edu/dataset/109/wine

## 6. Marco esperado ao final

- Ler dados pequenos, classificar variáveis, auditar tipos/chaves/ausências e produzir agregações em Python/pandas e SQL com unidade de análise correta.

- Escolher e interpretar centro, dispersão, distribuição, probabilidade, intervalo e teste dentro das hipóteses do problema; separar associação de causalidade e significância de relevância.

- Comparar modelos com baseline e protocolo explícito; evitar vazamento, preservar teste, interpretar erros e reconhecer resultados instáveis ou insuficientes.

- Construir funções de dados com contratos e testes e tratar falhas de integração sem esconder erro como ausência de dados.

- Inspecionar uma busca lexical e avaliar recuperação, resposta, citação, estrutura, custo e latência separadamente; justificar uma escolha entre alternativas simples e complexas.

- Defender uma análise pequena com pergunta, evidência, método, resultado e limites. Isso prepara os projetos do roadmap, mas ainda não comprova domínio de LLMs, deploy, cloud ou operação real em equipe.

### Referências e limites de uso

**[R] Roadmap oficial mais recente.** Roadmap_CESAR_Miguel_Freire.pdf, versão 1.1, 21/10/2026, 31 páginas. Fonte principal para prioridade e maturidade: E1 dados; E2 estatística/ML; E3 software/APIs; E4 NLP/LLMs; E5 RAG; E6 ferramentas/agentes; E7 operação. O plano antigo de IA generativa foi apenas contexto histórico.

**[F] Fávero e Belfiore.** Manual de Análise de Dados - Estatística e Machine Learning, 2ª edição, conforme o conteúdo do EPUB fornecido. Seleção: caps. 1-3 (variáveis e descrição), 4-5 (probabilidade/distribuições), 6 (amostragem e estimação), 7-8 (testes), 12-13 (regressão e classificação). Os demais métodos multivariados não foram incluídos só por constarem no livro.

**[B] Steven Dutt-Ross.** bookdown.pdf: Manual de Análise de Dados, atualização indicada no arquivo em 21/07/2020. Seleção: caps. 3-6 (tipos, banco e hipóteses), 7-10 (pressupostos e outliers), 11-13 (associação e comparação). Os exemplos em R fundamentam raciocínio; as entregas usam Python. Não adotar exclusão de outliers para forçar normalidade, nem testes de pressupostos como semáforo automático.

**[T] Análise de Dados: Da Teoria à Prática.** PDF de apresentação fornecido: limpeza, pp. 10-11; estatística e gráficos, pp. 13-21; modelagem e comunicação nas seções correspondentes; interpretação crítica, p. 46. Apoio de visão geral. Afirmações de mercado e percentuais sem fonte verificável não fundamentam este planner.

**[G] Repositório complementar.** https://github.com/jvataidee/ManualdeAnalisedeDadosPython. Conferidos README e notebooks dos capítulos 2 e 7, além da organização dos capítulos 1-7. Apoio a frequências, operações com NumPy/pandas e visualização de testes; não é um gabarito nem fonte de cobertura completa de ML. Não executei seus notebooks integralmente. Fórmulas e versões de terceiros devem ser verificadas.

**[C] Complementos técnicos e decisões pedagógicas.** Bootstrap, Wilson, validação temporal/cruzada, métricas de recuperação, testes de software e avaliação de IA são complementos ao material e ao roadmap. As divisões em dias, tempos, rubricas e limites de comparação são decisões pedagógicas deste planner, não exigências oficiais do CESAR ou dos autores. Enunciados originais, sem transcrição dos exercícios dos livros.

- [BCB - série oficial SGS 433](https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433)

- [BCB - endpoint exato do recorte](https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024)

- [UCI - Iris](https://archive.ics.uci.edu/dataset/53/iris)

- [UCI - Wine](https://archive.ics.uci.edu/dataset/109/wine)

- [scikit-learn - Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)

- [scikit-learn - prevenção de vazamento](https://scikit-learn.org/stable/common_pitfalls.html)

- [SciPy - testes estatísticos](https://docs.scipy.org/doc/scipy/reference/stats.html)

- [scikit-learn - TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

Consulta de fontes públicas e preparação das cópias: 23/10/2026. A cópia do IPCA foi obtida pelo endpoint oficial; Iris e Wine foram exportados das cópias locais do scikit-learn. Nenhum resultado de exercício é oferecido como gabarito.