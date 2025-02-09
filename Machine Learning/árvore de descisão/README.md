# Árvore de decisão
Sumário:

## Introdução
Árvores de decisão tem como ojetivo caracterizar uma variável alvo (target). É uma técnica de aprendizado de máquina usada tanto para **classificação** (variáveis do tipo qualitativa) quanto para **regressão** (variáveis do tipo quantitativa).

Elas funcionam de maneira semelhante a uma **árvore de decisão lógica**, onde cada nó interno representa uma "decisão" baseada em uma característica dos dados, e cada ramo representa a resposta dessa decisão.

O objetivo é dividir os dados em grupos (ou classes) mais homogêneos, tomando decisões em cada etapa até chegar a um resultado final.

## Estrutura
A árvore começa com um nó raiz, que contém todos os dados disponíveis. 

Em cada nó interno, a árvore faz uma "decisão" baseada em um critério específico de divisão dos dados. Isso é feito utilizando uma característica do dado, como "idade", "renda", "temperatura", etc.

Cada divisão divide os dados em dois ou mais grupos. Esses grupos são chamados de "ramos" e são definidos com base na característica escolhida.

Esse processo de divisão continua de forma recursiva até que os dados fiquem em grupos suficientemente pequenos, chamados de "nós folha". Nos nós folha, o valor final da previsão é atribuído. Para problemas de classificação, o nó folha será o rótulo da classe predominante; para problemas de regressão, o valor médio da variável de interesse.



## Critérios de divisão
- Entropia
- Índice de Gini
- Redução da variância (usado em regressão)


### Entropia
Métrica para ajudar a deciddir qual variável agrega mais informação. 

Quanto menor a entropia, mais homogêneo é o conjunto de dados, ou seja, as observações são idênticas em um grupo, esse grupo tem "pureza" total. 

Quanto maior a entropia, mais heterogêneo é o conjunto de dados, ou serja, as observações são divergentes em um grupo, esse grupo tem "impureza".

### Índice de Gini

É uma medida de impureza ou desigualdade de um nó. Ela varia entre 0 e 1, onde 0 indica que todos os elementos em um nó pertencem ao mesmo grupo (homogêneo), e 1 indica uma divisão uniforme entre as classes.

Quando você está construindo uma árvore de decisão, o objetivo é minimizar o índice de Gini ao dividir os dados nos nós. Isso significa que, para cada divisão, você escolhe o atributo que resulta na menor impureza (ou Gini) nos nós filhos. Isso ajuda a criar grupos mais homogêneos em termos de classe.

Formula:
$$
    Gini(D) = 1 - \sum_{i=1}^{c} p_i^2
$$

- _D_ é o conjunto de dados no nó.
- _c_ é o número de classes.
- _pi_ é a proporção de elementos da classe _i_ no nó _D_.

#### Passos para calcular o Gini:
1. Para cada classe _i_ no nó, calcule a proporção _pi_ da classe no conjunto de dados _D_.

2. Eleve _pi_ ao quadrado.

3. Some os quuadrados de todas as proporções das classes.

4. Subtraia essa soma de 1 para obter o índice de Gini.

Exemplo:

Suponha que temos um nó com 10 amostras, e as classes são "A" e "B". Das 10 amostras, 4 pertencem à classe "A" e 6 à classe "B". Então, temos:

- _pa_ = 4/10 = 0.4
- _pb_ = 6/10 = 0.6

Math block:

$$
    Gini(D) = 1 - (p_A^2 + p_B^2) = 0.48
$$

### Redução da variância
Usando na regressão, avalia como a variância dos dados é reduzida após a divisão. Quanto menor a variância, mais homogêneo é o grupo.











Vantagens das árvores de decisão:

Interpretabilidade: Como o modelo é representado visualmente por uma árvore, é fácil de entender e interpretar.
Não requer pré-processamento complexo: Árvores de decisão podem lidar bem com dados categóricos e numéricos sem a necessidade de normalização ou escalonamento dos dados.
Capacidade de lidar com relações não lineares: Diferente de modelos lineares, as árvores podem capturar relações complexas entre as variáveis.


Desvantagens:

Sobreajuste (overfitting): Árvores de decisão podem se ajustar excessivamente aos dados de treinamento, capturando até mesmo o ruído. Isso pode ser controlado por técnicas como poda e limitação da profundidade da árvore.
Instabilidade: Árvores de decisão podem ser sensíveis a pequenas variações nos dados, o que pode levar a resultados diferentes se o modelo for treinado com dados ligeiramente diferentes.
Melhorias e variações:

Random Forests: Conjunto de árvores de decisão que reduz a variabilidade, treinando várias árvores com amostras e subconjuntos de características aleatórias.
Boosting: Técnica que combina várias árvores fracas, treinadas de forma sequencial, onde cada árvore corrige os erros da anterior.


## Algoritmos

###