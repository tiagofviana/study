# Fundamentos da estatística
Sumário:
- [1. Tipos de variáveis](#1-tipos-de-variáveis)
- [2. Estatística descritiva ou análise exploratória](#2-estatística-descritiva-ou-análise-exploratória)


## 1. Tipos de variáveis
- [1.1 Qualitativa](#11-qualitativa)
- [1.2 Quantitativa](#12-quantitativa)

### 1.1 Qualitativa

> **DEFINIÇÃO:** Variáveis que atributem categorias ou classificações

Exemplos:
- Escala Likert
- Estado civil
- Cor do verículo
- Faixa de renda*
    
### 1.2 Quantitativa

> **DEFINIÇÃO:** Variáveis que atributem contagem ou mensuração
    
Exemplos:
- Idade (anos)
- Peso (kg)
- Temperatura
- Renda (R$)
    
## 2. Estatística descritiva ou análise exploratória

- [2.1 Tabela de frequência](#21-tabela-de-frequência)
- [2.2 Medidas de posição](#22-medidas-de-posição)
- [2.3 Medidas de dispersão](#23-medidas-de-dispersão)

### 2.1 Tabela de frequência
- [2.1.1 Frequência absolute](#211-frequência-absolute)
- [2.1.2 Frequência relativa](#212-frequência-relativa)
- [2.1.3 Frequência absolute acumulada](#213-frequência-absolute-acumulada)
- [2.1.4 Frequência relativa acumulada](#214-frequência-relativa-acumulada)


#### 2.1.1 Frequência absolute
> **DEFINIÇÃO:** contagem da ocorrência de cada categoria.

#### 2.1.2 Frequência relativa

> **DEFINIÇÃO:** percentual de cada categoria em relação ao total de observaões.

#### 2.1.3 Frequência absolute acumulada

> **DEFINIÇÃO:** soma da frequência absoluta a cada nova categoria.


#### 2.1.4 Frequência relativa acumulada

> **DEFINIÇÃO:** soma da frequência relativa a cada nova categoria.


### 2.2 Medidas de posição

- [2.2.1 Média](#221-média)
- [2.2.2 Mediana](#222-mediana)
- [2.2.3 Moda](#223-moda)
- [2.2.4 Percentis](#224-percentis)
- [2.2.4 Quartis](#225-quartis)
- [2.2.4 Decis](#226-decis)


#### 2.2.1 Média

> **DEFINIÇÃO:** média da variável

Fórmula:

```math
    Média = \frac{1}{n} \sum_{i=1}^{n} x_i
```

- _n_ é o número de elementos.
- _xi_ são os valores individuais.


#### 2.2.2 Mediana

> **DEFINIÇÃO:** é o valor central da sequência em ordem crescente.

Fórmula para número ímpar de elementos:

```math
    Mediana = \frac{n+1}{2}
```
- _n_ é o número total de elementos.

Fórmula para número par de elementos:

```math
    Mediana= \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}
```

- É a média dos dois valores centrais.


#### 2.2.3 Moda

> **DEFINIÇÃO:** é o valor com a maior frequência absoluta.

> **Importante:** A moda só pode ser calculada para dados qualitativos. Caso nenhum valor se repita, existirá a moda.

#### 2.2.4 Percentis

> **DEFINIÇÃO:** Percentis são valores que dividem um conjunto de dados ordenados em 100 partes iguais. O k-ésimo percentil é o valor abaixo do qual k% dos dados estão localizados. 

> **Importante:** O 50º percentil é a mediana.

Fórmula:

```math
\text{Pos}(k) = \left[ (n-1) \cdot \left( \frac{k}{100} \right) \right] + 1

```

- _Posk_ é a posição do percentil _k_.
- _k_ é o percentil desejado (por exemplo, 25 para o 25º percentil).
- _n_ é o número total de dados.

#### 2.2.5 Quartis

> **DEFINIÇÃO:** Os quartis são uma divisão específica dos dados ordenados, dividindo-os em 4 partes iguais:

- 1º Quartil = 25º Percentil
- 2º Quartil = 50º Percentil
- 3º Quartil = 75º Percentil

#### 2.2.6 Decis

> **DEFINIÇÃO:** São os elementos da distribuição da variável que dividem as observações em dez partes iguais,
considerando que a variável esteja com seus valores organizados de forma crescente


### 2.3 Medidas de dispersão

- [2.3.1 Amplitude](#231-amplitude)
- [2.3.2 Variância](#232-variância)
- [2.3.3 Desvio padrão](#233-desvio-padrão)
- [2.3.4 Erro padrão](#234-erro-padrão)
- [2.3.5 Coeficiente de variação](#235-coeficiente-de-variação)

#### 2.3.1 Amplitude

> **DEFINIÇÃO:** é a diferença entre o valor máximo e o valor mínimo de uma variável.

#### 2.3.2 Variância

> **DEFINIÇÃO:** mostra a dispersão das observações de uma variável em torno de sua média.

Fórmula:
```math
    S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
```

#### 2.3.3 Desvio padrão

> **DEFINIÇÃO:**  é uma medida derivada da variância, tornando mais simples a interpretação da dispersão em torno da
média.

Fórmula:
```math
    S = \sqrt{S^2}
```

#### 2.3.4 Erro padrão

> **DEFINIÇÃO:** o desvio padrão da média da variável.

Fórmula:
```math
    S\bar{x} = \frac{S}{\sqrt{n}}
```

#### 2.3.5 Coeficiente de variação

> **DEFINIÇÃO:** é uma medida de dispersão relativa, pois relaciona o desvio padrão e a média de uma variável.

> **Nota:** pode ser utilizada para realizar comparações entre amostras, por exemplo.

> **Importante:** quanto menor o CV, mais homogêneos são os valores da variável e mais concentrados estão os valores
em torno da média

Fórmula:
```math
    CV = \frac{S}{\bar{x}} \times 100
```