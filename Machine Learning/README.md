# Machine learning (aprendizando de máquina)
- [1. Introdução](#1-introdução)
- [2. Paradigmas](#2-paradigmas)
- [3. Tabela](#3-tabela)

## 1. Introdução
> **DEFINIÇÃO:** É um ramo da Inteligência Artificial (IA) que envolve a construção de modelos matemáticos (modelos preditivos, ou seja, um previsão) para entender dados. IA é definido como o estudo dos agentes que recebem percepçõs do ambiente e perfomam uma ação. 


## 2. Paradigmas
- [1.1 Aprendizado supervisionado](#11-aprendizado-supervisionado)
- [1.2 Aprendizado não supervisionado](#12-aprendizado-não-supervisionado)
- [1.3 Aprendizado por reforço](#12-aprendizado-por-reforço)
- [1.4 Aprendizado semi-supervisionado](#12-aprendizado-semi-supervisionado)
- [1.5 Aprendizado auto-supervisionado](#12-aprendizado-auto-supervisionado)


### 2.1 Aprendizado supervisionado

> **DEFINIÇÃO:** Quando modelo é treinado com dados rotulados, ou seja, para cada entrada, existe uma saída conhecida (rótulo). O objetivo é aprender uma função que, dada uma nova entrada, consiga prever a saída correta.

#### 2.1.1 Tipos

- [1.1.1.1 Classificação](#1111-classificação)
- [1.1.1.2 Regressão](#1112-regressão)


##### 2.1.1.1 Classificação
> **DEFINIÇÃO:** Quando se trabalha com váriaveis do tipo qualitativa.

Exemplo: 
- quando se trabalha com  identificar se uma imagem é de um gato ou cachorro.

##### 2.1.1.1 Regressão

> **DEFINIÇÃO:** Quando se trabalha com váriaveis do tipo quantitativas.

Exemplo:
- prever o preço de uma casa com base em suas características.


### 2.1.2 Algoritmos:

- Árvore de decisão
- Regressão linear
- Máquinas de vetor de suporte (SVM)

## 3. Tabela

- Cada paradigma é adequado para tipos específicos de problemas e tipos de dados. 
- O [aprendizado supervisionado](#11-aprendizado-supervisionado) é frequentemente usado quando você tem rótulos disponíveis
- O [aprendizado não supervisionado](#12-aprendizado-não-supervisionado) é útil quando você está tentando explorar dados sem um alvo explícito.
- O [aprendizado por reforço](#12-aprendizado-por-reforço) é ideal para problemas de decisão sequencial.
- O [aprendizado semi-supervisionado](#12-aprendizado-semi-supervisionado) e [aprendizado auto-supervisionado](#12-aprendizado-auto-supervisionado) se tornam úteis quando há poucos dados rotulados disponíveis.

<table>
    <tr>
        <th>Paradigma</th>
        <th>Dados Rotulados</th>
        <th>Tipos</th>
        <th>Algoritmo</th>
    </tr>
    <tr>
        <td>Supervisionado</td>
        <td>Sim</td>
        <td>Classificação, Regressão</td>
        <td>Regressão Linear, SVM, Árvores de Decisão</td>
    </tr>
    <tr>
        <td>Não Supervisionado</td>
        <td>Não</td>
        <td>Agrupamento, Redução de Dimensionalidade</td>
        <td>K-means, PCA</td>
    </tr>
    <tr>
        <td>Por Reforço</td>
        <td>Não</td>
        <td>Jogos, Robótica, Decisão Sequencial</td>
        <td>Q-learning, Deep Q-Network (DQN)</td>
    </tr>
    <tr>
        <td>Semi-Supervisionado</td>
        <td>Parcial</td>
        <td>Classificação com dados limitados</td>
        <td>Redes Neurais, KNN</td>
    </tr>
    <tr>
        <td>Auto-Supervisionado</td>
        <td>Não</td>
        <td>Previsão de palavras, Imagens</td>
        <td>BERT, GPT</td>
    </tr>
</table>