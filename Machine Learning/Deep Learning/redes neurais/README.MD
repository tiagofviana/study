# Redes neurais

- [1. Introdução](#1-introdução)
- [2. Estrutura](#2-estrutura)
- [3. Como as redes neurais aprendem](#3-como-as-redes-neurais-aprendem)
- [4. Tipos](#4-tipos)
- [5. Vantagens e desvantagens](#3-vantagens-e-desvantagens)
- [6. Ganho de performance](#6-ganho-de-performance)

## 1. Introdução

> **DEFINIÇÃO:** é um modelo inspirado no funcionamento do cérebro humano.

Elas são compostas por unidades chamadas neurônios ou nós, que estão organizados em camadas. Cada neurônio recebe um conjunto de entradas, realiza um cálculo e gera uma saída.

Podem ser aplicadas em problemas complexos, como reconhecimento de imagem, processamento de linguagem natural, e jogos.

## 2. Estrutura

- Cada neurônimo é chamado de preceptron
- As **camadas de entrada (input layers)** recebem os dados brutos (entradas) que a rede irá processar. Cada neurônio nesta camada corresponde a uma característica ou atributo do dado.
- As **camadas ocultas (hidden layers)** são as camadas entre a entrada e a saída. Aqui, os neurônios processam as entradas e transmitem informações para a próxima camada. O número de camadas e neurônios em cada camada pode variar, o que influencia a complexidade da rede.
- A **camada de saída (output layer)** gera a previsão ou o resultado da rede. Dependendo do tipo de problema, o número de neurônios nesta camada varia. Por exemplo, para um problema de classificação binária, haverá um único neurônio de saída, enquanto para uma classificação multiclasse, pode haver um neurônio para cada classe.

### 2.1 Normalização dos dados iniciais

Antes de utilzarmos os dados é  recomendado realizar a normalização ou padronização para melhorar a performance do modelo.
Assim existem diferentes tipos de normalização.

#### 2.1.1 Tipos

1. Mix max normalization
    - normalziar os dados entre 0 e 1 (mix max normalization). Assim, garente uma descida do gradiente descendente mais suave, diminuindo a o erro da busca e, consequentemente, o processamento.

2. StandardScaler
    - do"sklearn.preprocessing import StandardScaler" do python.
    - utilizada quando você está lidando com dados numéricos, pode haver diferentes escalas entre as variáveis. Por exemplo, uma variável pode estar na faixa de 0 a 1, enquanto outra pode variar entre 0 e 1000.
    - padroniza os dados para que cada característica tenha média 0 e desvio padrão 1

### 2.2 Função de ativação

> **DEFINIÇÃO:** componente que determina se um neurônio deve ser ativado ou não, ou seja, se a informação recebida por esse neurônio será transmitida para a próxima camada.

Ela introduz não linearidade no modelo, permitindo que redes neurais aprendam e representem padrões complexos, como os encontrados em imagens, texto ou séries temporais.

Sem funções de ativação, as redes neurais seriam apenas combinações lineares de entradas, incapazes de resolver problemas complexos. Por isso, a função de ativação é crucial para que as redes neurais possam aprender tarefas como reconhecimento de imagem, tradução de linguagem ou análise de sentimentos.

#### 2.2.1 Tipos

1. **Sigmoid** (função logística)
    - Fórmula: 
    ```math
        \sigma(z) = \frac{e^{-z}}{1 + e^{-z}}
    ```
    - Saída: Entre 0 e 1.
    - Características:
        - A função comprime a saída para um intervalo de 0 a 1, o que pode ser interpretado como uma probabilidade.
    - **Desvantagem**: O problema do desvanecimento do gradiente (vanishing gradient), onde a derivada se aproxima de 0 para valores muito altos ou muito baixos de entrada, o que pode dificultar o treinamento de redes mais profundas.
    - **Aplicação**: É utlizadoe m tarefas onde a saída precisa ser uma probabilidade ou em problemas de classificação binária.

2. **Tanh** (tangente hiperbólica)
    - Fórmula: 
    ```math
        \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
    ```
    - Saída: Entre -1 e 1.
    - Características:
        - A tangente hiperbólica é semelhante à sigmoid, mas a saída é centrada em torno de zero, o que pode ajudar a melhorar o desempenho durante o treinamento.
        - Pode ser útil em redes neurais com entradas que podem assumir valores positivos e negativos.
    - **Desvantagem**: Assim como a sigmoid, a tanh também sofre de desvanecimento do gradiente, o que pode dificultar o treinamento de redes muito profundas.

3. **ReLU** (rectified linear unit)
    - Fórmula: 
    ```math
        \text{ReLU}(z) = \max(0, z)
    ```
    - Saída: Pode ser qualquer valor real, dependendo do parâmetro 𝛼
    - Características:
        - Tenta resolver o problema do neurônio morto permitindo que, para entradas negativas, a função tenha uma pequena inclinação.
    - **Desvantagem**: O valor de 𝛼 precisa ser ajustado corretamente, o que pode tornar o treinamento um pouco mais complexo.
    - **Aplicação**: problemas de classificação como, por exemplo se o cara vai pagar a dívida ou não.
    
4. **Linear**
    - Fórmula:
     ```math
        f(z) = z
    ```
    - Saída: multiplica o valor _Z_ por 1, ou seja, ele mesmo
    - Características:
        - Todas as funções de ativação entre as camadas são lineares, ou seja, cada neurônio realiza uma simples multiplicação e soma dos inputs.

    - **Desvantagem**: Não consegue aprender padrões complexos, pois, apesar de ter várias camadas, as saídas de cada camada ainda podem ser representadas como uma combinação linear das entradas. O que significa que, independentemente de quantas camadas você tenha, a rede será equivalente a uma única camada linear. Portanto, ela tem a mesma capacidade que uma regressão linear.
    - **Aplicação**: utilizadas principalmente em problemas de regressão, onde o objetivo é prever uma saída contínua com base em entradas lineares.
    
### 2.3 Função do erro / função de custo / função de perda
> **DEFINIÇÃO:** permite veficiar o quão assertivo é determinada previsão. 

São diferentes para variáveis contínuas, discreta (é tipos a contínua, mas possui valores finitos) e categóricas.

#### 2.3.1 Contínua e discreta

Métricas utilizadas para avaliar a performance de modelos de regressão e redes neurais.

- Erro quadrático médio

```math
    MSE = \frac{1}{n} \sum_{i=1}^{n} (actual - predicted)^2
```
-  Erro absoluto médio
```math
    MAE = \frac{1}{n} \sum_{i=1}^{n} \left| actual - predicted \right|
```

#### 2.3.1 Categorica

- Binary cross-entropy
- Categorical cross-entropy


### 2.4 Regularização

> **DEFINIÇÃO:** técnica usada para evitar o overfitting. Em resumo, a regularização adiciona uma penalidade à função de perda do modelo para evitar que os pesos da rede neural se tornem muito grandes, o que pode levar ao overfitting.

#### 2.4.1 Tipos

1. **Dropout**
    - técnica que desativa aleatoriamente uma porcentagem das unidades (neurônios) durante o treinamento de cada iteração **de forma aleatória**. Isso força a rede a não depender excessivamente de nenhuma unidade específica, promovendo uma maior generalização.
    - introduz "ruído"

2. **L1**
    - adiciona uma penalização ao **valor absoluto dos pesos**. O efeito da regularização L1 é agressivo na redução dos pesos para zero, o que pode levar à sparsidade do modelo (ou seja, muitos pesos se tornam exatamente zero, o que pode ajudar na seleção de características).

3. **L2**
    - adiciona uma penalização ao **quadrado dos pesos**. Ela á parecida com a L1, a diferença é que ela pode levar para **próximo** de zero.

4. **Early Stopping**
    - técnica onde o treinamento da rede é interrompido quando a performance no conjunto de validação começa a piorar, mesmo que o erro no conjunto de treinamento continue diminuindo. Isso indica que a rede começou a se ajustar excessivamente aos dados de treinamento (overfitting), e interromper o treinamento mais cedo ajuda a evitar isso.

## 3. Como as redes neurais aprendem

O aprendizado em uma rede neural é realizado por meio de um processo chamado retropropagação (backpropagation). Esse processo envolve os seguintes passos:

1. **Forward pass (passagem direta)**: é o processo no qual os dados de entrada são passados através da rede, camada por camada, até que a saída final seja gerada.

2. **Cálculo do erro**: O erro é calculado comparando a previsão gerada pela rede com o valor real (rótulo). O erro pode ser medido usando uma função de perda (por exemplo, erro quadrático médio ou entropia cruzada).

3. **Backward pass (retropropagação)**: A rede ajusta seus pesos e vieses para reduzir o erro. Isso é feito usando o algoritmo de **gradiente descendente**, que calcula as derivadas da função de perda em relação aos pesos e faz ajustes nos pesos para minimizar o erro.

4. **Iteração**: Esse processo é repetido muitas vezes (em várias épocas), com a rede aprendendo aos poucos como fazer previsões mais precisas.

## 4. Tipos

### 4.1 Rede Neural Rasa (SNN - Shallow Neural Network)

Possui uma estrutura simples, com uma camada de entrada, uma única camada oculta (ou nenhuma) e uma camada de saída. 
O termo "shallow" (rasa) é usado para contrastar com redes neurais "deep" (profundas), que possuem várias camadas ocultas, ou seja, **deep learning**.

### 4.2 Redes Neurais feedforward (FNN - Feedforward Neural Network)

É um tipo em que os neurônios da mesma camada não se conectam, mas cada um deles se coenctam com cada neurônio da próxima camada. O termo "feedforward" se refere ao fato de que as informações são passadas de um neurônio para outro, de forma direta e unidirecional, sem retroalimentação.

Também conhecida como perceptron multicamadas (MLP - Multi-Layer Perceptron)

A ordem das features não é relevante.

### 4.3 Redes Neurais Recorrentes (RNN - Recurrent Neural Networks)

Projetadas para lidar com dados sequenciais, como séries temporais ou texto. Elas têm conexões "recorrentes" que permitem que informações anteriores influenciem o processamento atual.

A ordem das features é relevante. Exemplo:
- O rato correu do gato.
- O gato correu do rato.
Se cada palavra é um token, a ordem de processamento tem interferencia no resultado, a rede memoriza.
 
### 4.4 Redes Neurais Convolucionais (CNN - Convolutional Neural Networks)

Usadas principalmente em processamento de imagens e vídeo. Elas aplicam convoluções para extrair características locais de uma imagem (como bordas, texturas) e são muito boas para reconhecimento visual.

### 4.5 Redes Generativas (GANs - Generative Adversarial Networks):

Compostas por duas redes neurais que competem entre si: uma geradora, que cria amostras de dados, e uma discriminadora, que tenta distinguir entre dados reais e gerados. GANs são usadas em tarefas como geração de imagens realistas e deepfakes.

## 5. Vantagens e desvantagens

Vantagens das redes neurais:
Capacidade de aprender representações complexas: Elas são ótimas em aprender padrões em grandes volumes de dados, principalmente quando esses dados são altamente não lineares ou complexos.
Versatilidade: Podem ser aplicadas a uma grande variedade de problemas, desde imagem até texto, áudio, e muito mais.
Adaptabilidade: Elas podem melhorar com o tempo à medida que recebem mais dados e podem aprender características que não são explicitamente programadas.
Desvantagens:
Necessidade de grandes quantidades de dados: Para obter bons resultados, redes neurais geralmente precisam de grandes volumes de dados para treinamento.
Consumo computacional: O treinamento de redes neurais, especialmente redes profundas, pode ser muito intensivo em termos de tempo e recursos computacionais.
Dificuldade de interpretação: As redes neurais são frequentemente chamadas de "caixas-pretas", já que seus processos internos podem ser difíceis de interpretar e entender.


## 6. Ganho de performance

### 6.1 Bath

> **DEFINIÇÃO:** usando quando se tem restrição de memória, no qual os dados são agrupados em "lotes". Assim, a cada interação, a rede processa cada um do lotes.

