# Ensemble
- [1. Introdução](#1-introdução)
- [2. Tipos](#2-tipos)

## 1. Introdução

> **DEFINIÇÃO:** técnica onde múltiplos modelos são combinados para melhorar o desempenho preditivo, é possível obter resultados mais robustos e precisos do que confiar em um único modelo

## 2. Tipos

Os principais tipos são:

1. Bagging  (Bootstrap Aggregating)
2. Boosting
3. Stacking (Empilhamento)

### 2.1 Bagging  (Bootstrap Aggregating)

> **DEFINIÇÃO:** esse consiste em uma coleção de árvores de decisão treinadas em subconjuntos diferentes de dados e, no final, a previsão de todas as árvores é combinada por votação (para classificação) ou média (para regressão). Um exemplo é o **Random Forest**.

Código: [./bootstrapping.py](./bootstrapping.py)

### 2.2 Boosting
> **DEFINIÇÃO:** treina modelos de forma sequencial, onde cada novo modelo tenta corrigir os erros cometidos pelos modelos anteriores.

A ideia é que modelos mais fracos podem ser combinados para formar um modelo mais forte, corrigindo as falhas de predições anteriores. Um exemplo é o **Gradient Boosting**.


### 2.3 Stacking (Empilhamento)

> **DEFINIÇÃO:** combina diferentes tipos de modelos, por exemplo, árvore de decisão, redes neurais, máquinas de vetores de suporte, etc. Cada modelo é treinado separadamente e suas previsões são então usadas como entrada para um novo modelo chamado de meta-modelo ou modelo de segundo nível. Esse meta-modelo aprende a melhor forma de combinar as previsões dos modelos anteriores.