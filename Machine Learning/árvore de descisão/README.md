# Árvore de decisão

- [1. Introdução](#1-introdução)
- [2. Estrutura](#2-estrutura)
- [3. Vantagens e desvantagens](#3-vantagens-e-desvantagens)
- [4. Acurácia X acertividade](#4-acurácia-X-acertividade)

## 1. Introdução

> **DEFINIÇÃO:** Árvores de decisão tem como ojetivo caracterizar uma variável alvo (target). É uma técnica de aprendizado de máquina usada tanto para [classificação](./classificação/README.md) (variáveis do tipo qualitativa) quanto para [regressão](./regressão/README.md) (variáveis do tipo quantitativa).

Elas funcionam de maneira semelhante a uma **árvore de decisão lógica**, onde cada nó interno representa uma "decisão" baseada em uma característica dos dados, e cada ramo representa a resposta dessa decisão.

O objetivo é dividir os dados em grupos (ou classes) mais homogêneos, tomando decisões em cada etapa até chegar a um resultado final.

## 2. Estrutura

- A árvore começa com um nó raiz, que contém todos os dados disponíveis. 
- Em cada nó interno, a árvore faz uma "decisão" baseada em um critério específico de divisão dos dados. Isso é feito utilizando uma característica do dado, como "idade", "renda", "temperatura", etc.
- Cada divisão divide os dados em dois ou mais grupos. Esses grupos são chamados de "ramos" e são definidos com base na característica escolhida.
- Esse processo de divisão continua de forma recursiva até que os dados fiquem em grupos suficientemente pequenos, chamados de "nós folha". Nos nós folha, o valor final da previsão é atribuído. Para problemas de classificação, o nó folha será o rótulo da classe predominante; para problemas de regressão, o valor médio da variável de interesse.

## 3. Vantagens e desvantagens

### 3.1 Vantagens

- **Interpretabilidade**: Como o modelo é representado visualmente por uma árvore, é fácil de entender e interpretar.
- **Não requer pré-processamento complexo**: Árvores de decisão podem lidar bem com dados categóricos e numéricos sem a necessidade de normalização ou escalonamento dos dados.
- **Capacidade de lidar com relações não lineares**: Diferente de modelos lineares, as árvores podem capturar relações complexas entre as variáveis.

### 3.2 Desvantagens

- **Overfitting**: Árvores de decisão podem se ajustar excessivamente aos dados de treinamento, capturando até mesmo o ruído. Isso pode ser controlado por técnicas como poda e limitação da profundidade da árvore.
- **Instabilidade**: Árvores de decisão podem ser sensíveis a pequenas variações nos dados, o que pode levar a resultados diferentes se o modelo for treinado com dados ligeiramente diferentes.

## 4. Acurácia X acertividade

As duas métricas são úteis, mas em diferentes cenários. Por exemplo, se tivermos um problema muito desbalanceado (muitos negativos e poucos positivos), um modelo com alta acurácia pode ter baixa acertividade (precisão) se ele errar muitos positivos, mesmo acertando a maioria dos negativos.

### 4.1 Acurácia

> **DEFINIÇÃO:** métrica mais comum para avaliar o desempenho de um modelo de classificação, ou seja, a acurácia mede a taxa de acertos gerais de um modelo. Quanto maior a acurácia, mais preciso é o modelo como um todo.

```math
    \text{Acurácia} = \frac{\text{Número de previsões corretas}}{\text{Número total de previsões}}
```

### 4.1 Acertividade

> **DEFINIÇÃO:** termo que pode ser mais relacionado à taxa de verdadeiros positivos, ou seja, a capacidade de um modelo de identificar corretamente os casos positivos. Em alguns contextos, a acertividade é usada como sinônimo de precisão.

```math
    \text{Precisão (Acertividade)} = \frac{\text{Verdadeiros Positivos}}{\text{Verdadeiros Positivos} + \text{Falsos Positivos}}
```