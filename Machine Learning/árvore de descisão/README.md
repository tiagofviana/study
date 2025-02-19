# Árvore de decisão

- [1. Introdução](#1-introdução)
- [2. Estrutura](#2-estrutura)

## 1. Introdução

> **DEFINIÇÃO:** Árvores de decisão tem como ojetivo caracterizar uma variável alvo (target). É uma técnica de aprendizado de máquina usada tanto para [classificação](./classificação/README.md) (variáveis do tipo qualitativa) quanto para [regressão](./regressão/README.md) (variáveis do tipo quantitativa).

Elas funcionam de maneira semelhante a uma **árvore de decisão lógica**, onde cada nó interno representa uma "decisão" baseada em uma característica dos dados, e cada ramo representa a resposta dessa decisão.

O objetivo é dividir os dados em grupos (ou classes) mais homogêneos, tomando decisões em cada etapa até chegar a um resultado final.

## 2. Estrutura

- A árvore começa com um nó raiz, que contém todos os dados disponíveis. 
- Em cada nó interno, a árvore faz uma "decisão" baseada em um critério específico de divisão dos dados. Isso é feito utilizando uma característica do dado, como "idade", "renda", "temperatura", etc.
- Cada divisão divide os dados em dois ou mais grupos. Esses grupos são chamados de "ramos" e são definidos com base na característica escolhida.
- Esse processo de divisão continua de forma recursiva até que os dados fiquem em grupos suficientemente pequenos, chamados de "nós folha". Nos nós folha, o valor final da previsão é atribuído. Para problemas de classificação, o nó folha será o rótulo da classe predominante; para problemas de regressão, o valor médio da variável de interesse.


