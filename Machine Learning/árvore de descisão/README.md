# Árvore de decisão

- [1. Introdução](#1-introdução)
- [2. Estrutura](#2-estrutura)
- [3. Critérios de divisão](#3-critérios-de-divisão)
- [4. Vantagens e desvantagens](#4-vantagens-e-desvantagens)
- [5. Melhorias e variações](#5-melhorias-e-variações)
- [6. Algoritmos](#6-malgoritmos)

## 1. Introdução

> **DEFINIÇÃO:** Árvores de decisão tem como ojetivo caracterizar uma variável alvo (target). É uma técnica de aprendizado de máquina usada tanto para **classificação** (variáveis do tipo qualitativa) quanto para **regressão** (variáveis do tipo quantitativa).

Elas funcionam de maneira semelhante a uma **árvore de decisão lógica**, onde cada nó interno representa uma "decisão" baseada em uma característica dos dados, e cada ramo representa a resposta dessa decisão.

O objetivo é dividir os dados em grupos (ou classes) mais homogêneos, tomando decisões em cada etapa até chegar a um resultado final.

## 2. Estrutura

- A árvore começa com um nó raiz, que contém todos os dados disponíveis. 
- Em cada nó interno, a árvore faz uma "decisão" baseada em um critério específico de divisão dos dados. Isso é feito utilizando uma característica do dado, como "idade", "renda", "temperatura", etc.
- Cada divisão divide os dados em dois ou mais grupos. Esses grupos são chamados de "ramos" e são definidos com base na característica escolhida.
- Esse processo de divisão continua de forma recursiva até que os dados fiquem em grupos suficientemente pequenos, chamados de "nós folha". Nos nós folha, o valor final da previsão é atribuído. Para problemas de classificação, o nó folha será o rótulo da classe predominante; para problemas de regressão, o valor médio da variável de interesse.

## 3. Critérios de divisão

- [3.1 Entropia de Shannon](#31-entropia-de-shannon)
- [3.2 Índice de Gini](#32-índice-de-gini)
- [3.3 Redução da variância](#33-redução-da-variância)

### 3.1 Entropia de Shannon

>  **DEFINIÇÃO:** medida da incerteza ou imprevisibilidade de uma variável aleatória.

```math
    H(X) = - \sum_{i=1}^{n} p_i \log_2(p_i)
```

- Quanto menor a entropia, mais homogêneo é o conjunto de dados, ou seja, as observações são idênticas em um grupo, esse grupo tem "pureza" total. 

- Quanto maior a entropia, mais heterogêneo é o conjunto de dados, ou serja, as observações são divergentes em um grupo, esse grupo tem "impureza".

#### 3.1.2 Interpretação

- **Entropia alta**: significa que o sistema (ou variável aleatória) tem muita incerteza. Os resultados são mais imprevisíveis. Por exemplo, em um dado com 6 faces justas, a entropia é máxima porque qualquer face pode sair com igual probabilidade, e não sabemos qual será o resultado de antemão.

- **Entropia baixa**: significa que o sistema tem pouca incerteza. Por exemplo, se você tem uma variável que sempre assume o valor "1", a entropia é zero, porque não há surpresa nem incerteza sobre o valor.

### 3.2 Índice de Gini

É uma medida de impureza ou desigualdade de um nó. Ela varia entre 0 e 1, onde 0 indica que todos os elementos em um nó pertencem ao mesmo grupo (homogêneo), e 1 indica uma divisão uniforme entre as classes.

Quando você está construindo uma árvore de decisão, o objetivo é minimizar o índice de Gini ao dividir os dados nos nós. Isso significa que, para cada divisão, você escolhe o atributo que resulta na menor impureza (ou Gini) nos nós filhos. Isso ajuda a criar grupos mais homogêneos em termos de classe.

Formula:
```math
    Gini(D) = 1 - \sum_{i=1}^{c} p_i^2
```

- _D_ é o conjunto de dados no nó.
- _c_ é o número de classes.
- _pi_ é a proporção de elementos da classe _i_ no nó _D_.

#### 3.2.1 Passos para calcular o Gini:

1. Para cada classe _i_ no nó, calcule a proporção _pi_ da classe no conjunto de dados _D_.

2. Eleve _pi_ ao quadrado.

3. Some os quuadrados de todas as proporções das classes.

4. Subtraia essa soma de 1 para obter o índice de Gini.

Exemplo:

Suponha que temos um nó com 10 amostras, e as classes são "A" e "B". Das 10 amostras, 4 pertencem à classe "A" e 6 à classe "B". Então, temos:

- _pa_ = 4/10 = 0.4
- _pb_ = 6/10 = 0.6

```math
    Gini(D) = 1 - (p_A^2 + p_B^2) = 0.48
```

### 3.3 Redução da variância
Usando na regressão, avalia como a variância dos dados é reduzida após a divisão. Quanto menor a variância, mais homogêneo é o grupo.

### 3.4 Hiperparâmetros
> **DEFINIÇÃO:** é um parâmetro que é definido antes do processo de treinamento. Esses parâmetros controlam o comportamento do modelo e influenciam o desempenho e a capacidade de generalização.

> **Importante**: A escolha correta dos hiperparâmetros pode ter um grande impacto no sucesso do modelo.

Exemplos:

- Número de folhas.
- Profundidade máxima
- Custo de complexidade (CCP)

### 4. Vantagens e desvantagens

#### 4.1 Vantagens

- **Interpretabilidade**: Como o modelo é representado visualmente por uma árvore, é fácil de entender e interpretar.
- **Não requer pré-processamento complexo**: Árvores de decisão podem lidar bem com dados categóricos e numéricos sem a necessidade de normalização ou escalonamento dos dados.
- **Capacidade de lidar com relações não lineares**: Diferente de modelos lineares, as árvores podem capturar relações complexas entre as variáveis.


#### 4.1 Desvantagens

- **Overfitting**: Árvores de decisão podem se ajustar excessivamente aos dados de treinamento, capturando até mesmo o ruído. Isso pode ser controlado por técnicas como poda e limitação da profundidade da árvore.
- **Instabilidade**: Árvores de decisão podem ser sensíveis a pequenas variações nos dados, o que pode levar a resultados diferentes se o modelo for treinado com dados ligeiramente diferentes.


### 5 Melhorias e variações

- **Random Forests**: Conjunto de árvores de decisão que reduz a variabilidade, treinando várias árvores com amostras e subconjuntos de características aleatórias.
- **Boosting**: Técnica que combina várias árvores fracas, treinadas de forma sequencial, onde cada árvore corrige os erros da anterior.

#### 5.1 Tratar um overfiting
Alguns dos principais hiperparâmetros que podem ser ajustados para controlar a complexidade da árvore e reduzir o overfitting:
1. Profundidade Máxima da Árvore (max_depth)
2. Número Mínimo de Amostras por Nó (min_samples_split)
3. Número Mínimo de Amostras por Folha (min_samples_leaf)
4. Valor Máximo de Características (max_features)
5. Poda (Pruning)

## 6. Algoritmos

### Classificação
Será utilziado o python. Segue abaixo o comando das para instalar as ferramentas utilizadas:

```sh
    pip install pandas seaborn matplotlib scikit-learn
```

Código:
[classification/main.py](./classification/main.py)


## 7. Análise do algoritmo resultante

### 7.1 Tabela Cruzada

> **DEFINIÇÃO:** conhecida como tabela de contingência ou tabela de contingência cruzada, é uma ferramenta estatística utilizada para resumir e analisar a relação entre duas ou mais variáveis categóricas. Ela mostra como os dados se distribuem entre diferentes categorias e pode ser usada para identificar padrões, tendências ou relações entre essas variáveis.

#### 7.1.1 Estrutura

A tabela cruzada organiza os dados em uma matriz onde:

- **Linhas** representam os valores de uma variável.
- **Colunas** representam os valores de outra variável.
- **As células** da tabela mostram a contagem (ou a frequência) de ocorrências para cada combinação de valores dessas variáveis.

#### 7.1.2 Exemplo

Imagine um estudo sobre gênero (masculino e feminino) e preferência de bebida (café, chá, suco). A tabela cruzada pode se parecer com isso:


<table>
    <tr>
        <th>Gênero</th>
        <th>Café</th>
        <th>Chá</th>
        <th>Suco</th>
    </tr>
    <tr>
        <td>Masculino</td>
        <td>20</td>
        <td>10</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Feminino</td>
        <td>25</td>
        <td>12</td>
        <td>20</td>
    </tr>
</table>

### 7.2 Acurácia

> **DEFINIÇÃO:** mede a proporção de previsões corretas feitas por um modelo de classificação.

> **Importante:** A acurácia é útil, mas pode não ser a melhor métrica em todos os casos, especialmente quando as classes estão desbalanceadas (quando uma classificação é muito mais frequente que as outras). Nesses casos, outras métricas como precisão, recall ou F1-score podem ser mais indicada.

### 7.3 Acurácia balanceada

> **DEFINIÇÃO:** métrica de avaliação utilizada quando o conjunto de dados tem um desbalanceamento entre as classes (ou seja, uma classe é muito mais frequente do que as outras).


- A acurácia balanceada leva em consideração a precisão em cada classe de forma igual, independentemente do número de instâncias em cada classe. Ela calcula a média das taxas de acerto (ou sensibilidade) para cada classe, o que ajuda a medir o desempenho do modelo de maneira mais justa quando as classes estão desbalanceadas.

### 7.4 Matriz de confusão

> **DEFINIÇÃO:** tabela que ajuda a visualizar a quantidade de acertos e erros do modelo em relação a diferentes classes.

- Ela é especialmente útil em problemas de classificação. Para uma classificação binária (por exemplo, sim ou não), a matriz de confusão tem a seguinte forma:


<table>
    <tr>
        <th></th>
        <th>Previsto Positivo</th>
        <th>Previsto Negativo</th>
    </tr>
    <tr>
        <td>Real Positivo</td>
        <td>Verdadeiro Positivo (TP)</td>
        <td>Falso Negativo (FN)</td>
    </tr>
    <tr>
        <td>Real Negativo</td>
        <td>Falso Positivo (FP)</td>
        <td>Verdadeiro Negativo (TN)</td>
    </tr>
</table>


### 7.5 Curva ROC

> **DEFINIÇÃO:**  (Receiver Operating Characteristic) é uma representação gráfica utilizada para avaliar o desempenho de modelos de classificação, especialmente quando há desequilíbrio nas classes

- Quanto maior a área embaixo curva, melhor o modelo

#### 7.5.1 Components

- **Eixo X**: Representa a taxa de falsos positivos (FPR - False Positive Rate), que é a proporção de casos negativos que foram incorretamente classificados como positivos. A fórmula para o FPR é:

```math
\text{FPR} = \frac{\text{Falsos Positivos}}{\text{Falsos Positivos} + \text{Verdadeiros Negativos}}
```

- **Eixo Y**: Representa a taxa de verdadeiros positivos (TPR - True Positive Rate), também conhecida como sensibilidade ou recall. Ela é a proporção de casos positivos que foram corretamente classificados como positivos. A fórmula para o TPR é:

```math
\text{TPR} = \frac{\text{Verdadeiros Positivos}}{\text{Verdadeiros Positivos} + \text{Falsos Negativos}}
```

### 7.6 Validação Cruzada (Cross-Validation)

> **DEFINIÇÃO:** técnica  para avaliar a performance de um modelo, ajudando a verificar a sua capacidade de generalização (ou seja, como ele se comportará em dados não vistos). A ideia central da validação cruzada é dividir os dados em subconjuntos (amostra de treino, amostra de validação e amostra de teste), treinar o modelo em diferentes combinações de treinamento e validação, e então avaliar a performance do modelo em cada combinação.

> **IMPORTANTE**: amostra de teste não é utilizada nem para treinar e nem para escolher o modelo.