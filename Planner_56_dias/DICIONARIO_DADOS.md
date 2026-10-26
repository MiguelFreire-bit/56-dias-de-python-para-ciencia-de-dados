# Dicionário e procedência

Cada enunciado descreve suas colunas e unidades. Todos os dados são sintéticos, exceto os dias listados no mapa de bases públicas. IDs não são atributos preditivos.

## IPCA
SGS 433: produção IBGE, distribuição Banco Central do Brasil. Brasil, jan/2023-dez/2024. `data`: primeiro dia do mês de referência em ISO, não data de publicação. `ipca_pct`: variação percentual mensal. Valores negativos são admissíveis. O JSON original do recorte consta no Dia 41 (`data` dd/mm/aaaa e `valor` texto decimal com ponto). Obtenção: 23/10/2026.
Endpoint: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2024

Nos exercícios temporais a origem é após a publicação da taxa anterior; os arquivos não têm datas de publicação e não devem ser usados para simular informação disponível no primeiro dia do mês.

## Iris
Fonte acadêmica UCI: https://archive.ics.uci.edu/dataset/53/iris
Cópia fornecida: sklearn.datasets.load_iris, scikit-learn 1.8.0. 150 linhas; `row_id` é índice 0-149; `sepal_length_cm`, `sepal_width_cm`, `petal_length_cm`, `petal_width_cm`: medidas em cm; `target`: 0=setosa, 1=versicolor, 2=virginica. A cópia do scikit-learn contém correções históricas e não deve ser silenciosamente substituída por outra variante da UCI.

## Wine
Fonte acadêmica UCI: https://archive.ics.uci.edu/dataset/109/wine
Cópia fornecida: sklearn.datasets.load_wine, scikit-learn 1.8.0. 178 linhas. `row_id`: 0-177; `target`: 0,1,2 são os três cultivares codificados; não usar como escala de qualidade. Atributos: alcohol (álcool), malic_acid (ácido málico), ash (cinzas), alcalinity_of_ash (alcalinidade das cinzas), magnesium (magnésio), total_phenols (fenóis totais), flavanoids (flavonoides), nonflavanoid_phenols (fenóis não flavonoides), proanthocyanins (proantocianidinas), color_intensity (intensidade de cor), hue (tonalidade), od280/od315_of_diluted_wines (razão óptica) e proline (prolina). Nem toda unidade é detalhada no pacote original; não atribua uma unidade inventada. Para modelagem, preserve escala original e ajuste transformações só no treino.

## Dados simulados
Tabelas pequenas, documentos, metadados, logs e saídas simuladas foram criados para o problema de cada dia. Não representam estudo real nem afirmações sobre políticas públicas. As taxas, custos e critérios são pedagógicos.
