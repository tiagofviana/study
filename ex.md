https://code.visualstudio.com/docs/languages/markdown
https://www.markdownguide.org/basic-syntax/
formula
https://katex.org/docs/api


# 🚀 Voxflow

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento.

## 📋 Pré-requisitos

Primeiramente certifique-se de ter as seguintes programas corretamente instalados:

- NodeJS 22.12.0
- Python 3.12
- PostgreSQL 16.4

## 🛠️ Como configurar o projeto

Siga as intruções de cada tópico abaixo, seguindo a ordem apresentada.

### PostgreSQL

No postgres, crie um banco de dados vazio chamado `voxflow_db`. O schema do banco será criado automáticamente mais à frente.

### NodeJS

No diretório do projeto, instale as dependências do node com o seguinte comando:

```sh
$ npm install
```

Para o funcionamento adequado do projeto, o node cria alguns arquivos estáticos importantes. Rode os seguintes comandos para esses arquivos:

> **IMPORTANTE** Para encerrar a execução dos comandos abaixo, será necessário pressionar `CTRL + C` no terminal.

```sh
$ npm run styles
```

```sh
$ npm run build
```

### Python

> **IMPORTANTE** Verifique qual é a forma de invocar o python sey terminal. Estas intruções tomam como referência o nome "python".

No diretório do projeto, cria o ambiente virtual com o seguinte comando:

```sh
$ python -m venv venv
```

Ative o ambiente virtual:

```sh
$ . .\venv\Scripts\activate
```

Note que `(env)` aparecerá no prompt. Isso indica que o terminal está funcionando em um ambiente virtual. Acesse a pasta `\src` e instale as dependências necessárias:

```sh
(env)$ cd src
```

```sh
(env)$ pip install -r ./requirements/dev.txt
```

Após o `pip` terminar de baixar todas as dependências, ainda na pasta `src`, crie o arquivo `.env` e adicione as variáveis de ambiente listadas abaixo com suas respectivas chaves:

```
DJANGO_LOG_LEVEL=DEBUG
DJANGO_SECRET_KEY=<sua-chave>
DJANGO_ALLOWED_HOSTS=*
DJANGO_CSRF_TRUSTED_ORIGINS=https://*

# Database
DATABASE_NAME=<nome-do-banco>
DATABASE_USER=<nome-de-usuário>
DATABASE_PASSWORD=<senha>
DATABASE_HOST=<host>
DATABASE_PORT=<porta>



# Email
EMAIL_PORT=<porta>
EMAIL_HOST_USER=<email-do-provedor>
EMAIL_HOST_PASSWORD=<senha-do-provedor>
DJANGO_ADMINS=Admin <seu-email.com>

```

Certifique-se que o banco de dados configurado no `.env` existe no PostgreSQL. Então faça as migrações:

```sh
(env)$ python manage.py migrate
```

Rode o seguinte comando para inicializar algumas tabela de riscos do banco de dados

```sh
(env)$ python .\manage.py loaddata .\patients\migrations\risks.json
```

## 🛠️ Como rodar o projeto

Após a configuração, rode o projeto com o seguinte comando:

> **IMPORTANTE** Para encerrar a execução do comando abaixo, será necessário pressionar `CTRL + C` no terminal.

```sh
(env)$ python manage.py runserver
```

E navegue: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>
