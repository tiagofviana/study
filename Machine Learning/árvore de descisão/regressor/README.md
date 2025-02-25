# Árvore de decisão de regressão

- [1. Critérios de divisão](#1-critérios-de-divisão)
- [2. Melhorias e variações](#2-melhorias-e-variações)
- [3. Algoritmos](#3-algoritmos)

## 1. Critérios de divisão

### 1.2 Impureza

> **DEFINIÇÃO:** É uma medida de impureza ou desigualdade de um nó. Ela varia entre 0 e 1, onde 0 indica que todos os elementos em um nó pertencem ao mesmo grupo (homogêneo), e 1 indica uma divisão uniforme entre as classes. A impureza é medida com base na variabilidade dos valores contínuos na variável dependente.


#### 1.2.1 Soma dos Quadrados dos Erros (SSE)

> **DEFINIÇÃO:** métrica utilizada para medir a diferença entre os valores reais e os valores preditos em um modelo de regressão


Formula:
```math
    SSE = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
```
- _yi_ é o valor real da amostra (observado).
- _y^i_ é o valor predito pelo modelo para a amostra _i_.
- _n_ é o número total de amostras ou dados no conjunto.

> **Detalhe**: O **resíduo** é a diferença entre o valor real observado (ou valor verdadeiro) e o valor predito pela árvore para uma dada observação, ou seja:

```math
    \text{Resíduo}_i = y_i - \hat{y}_i
```

#### 1.2.1.1 Interpretação:
- **SSE menor**: Quanto menor o valor do SSE, melhor o modelo, pois significa que as previsões do modelo estão mais próximas dos valores reais.

- **SSE maior**: Um valor maior indica que o modelo tem um erro maior nas previsões e não está ajustando bem os dados.


#### 1.2.3 R-quadrado

> **DEFINIÇÃO:** métrica que avalia o desempenho de modelos de regressão.

Formula:
```math
   R^2 = 1 - \frac{SSE}{SST}
```

- _SSE_ é a soma dos quadrados dos erros, ou seja, a diferença entre os valores reais e as previsões do modelo. 
- _SST_ é a soma total dos quadrados, ou seja, a diferença entre os valores reais e a média dos valores reais.

##### 1.2.5.1 Interpretação

- **𝑅2 < 0**: Em alguns casos (quando o modelo é muito ruim), o R quadrado pode ser negativo, indicando que o modelo está ajustando os dados pior do que uma simples média. Isso pode ocorrer em modelos mal ajustados ou se você for forçar o modelo a se ajustar a dados que claramente não são lineares.
- **R2 = 0**: o modelo não consegue explicar nenhuma variabilidade dos dados. O modelo está basicamente fazendo previsões aleatórias.
- **𝑅2 = 1**: o modelo consegue explicar toda a variabilidade dos dados. As previsões do modelo são perfeitas, ou seja, os valores preditos coincidem com os reais.
- **0 < 𝑅2 < 1**: o modelo explica uma certa porcentagem da variabilidade dos dados. Quanto mais próximo de 1, melhor o modelo se ajusta aos dados.

### 2. Melhorias e variações

- **Random Forests**: Conjunto de árvores de decisão que reduz a variabilidade, treinando várias árvores com amostras e subconjuntos de características aleatórias.
- **Boosting**: Técnica que combina várias árvores fracas, treinadas de forma sequencial, onde cada árvore corrige os erros da anterior.

#### 2.1 Tratar um overfiting
Alguns dos principais hiperparâmetros que podem ser ajustados para controlar a complexidade da árvore e reduzir o overfitting:

1. Profundidade Máxima da Árvore (max_depth)
2. Número Mínimo de Amostras por Nó (min_samples_split)
3. Número Mínimo de Amostras por Folha (min_samples_leaf)
4. Valor Máximo de Características (max_features)
5. Poda (Pruning)


## 3. Algoritmos

Será utilziado o python. Segue abaixo o comando das para instalar as ferramentas utilizadas:

```sh
    pip install pandas seaborn matplotlib scikit-learn
```

Código: [./main.py](./main.py)