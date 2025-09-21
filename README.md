# 🔗 Encurtador de URLs com UTM e gerador de QR Code

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

Um serviço de backend para encurtamento de URLs, construído com Python e FastAPI. O projeto permite não apenas a criação de links curtos, mas também a adição dinâmica de parâmetros UTM para rastreamento de campanhas e a geração instantânea de QR Codes para cada link.

![Demo do Projeto](https://exemplo.com/link_para_sua_imagem_demo.png)

## Funcionalidades principais

* **Encurtamento de URL:** Converte URLs longas em links curtos e únicos usando um algoritmo Base62.
* **Adição de parâmetros UTM:** Anexa dinamicamente parâmetros `utm_source`, `utm_medium`, `utm_campaign`, etc., à URL original, ideal para marketing digital.
* **Geração de QR Code:** Gera um QR Code para cada link encurtado através de um endpoint dedicado (`/{short_code}/qrcode`).
* **Redirecionamento rápido:** Utiliza redirecionamentos HTTP 307 para garantir performance.
* **Documentação automática:** A API é 100% documentada e testável via interface Swagger UI (`/docs`).

## Tecnologias utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e conceitos:

* **Backend:** Python 3.11, FastAPI
* **Banco de dados:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validação de dados:** Pydantic
* **Conteinerização:** Docker & Docker Compose
* **Servidor:** Uvicorn
* **Deploy:** Servidor VPS (Ubuntu)

## Endpoints da API

A API possui 3 endpoints principais:

| Método | Rota                     | Descrição                                         |
| :----- | :----------------------- | :-------------------------------------------------- |
| `POST` | `/urls`                  | Cria uma nova URL encurtada, com ou sem UTMs.       |
| `GET`  | `/{short_code}`          | Redireciona para a URL original correspondente.     |
| `GET`  | `/{short_code}/qrcode`   | Retorna a imagem de um QR Code para a URL encurtada.|

## Como executar o projeto localmente

Para executar este projeto no seu ambiente, você precisará ter o [Git](https://git-scm.com/) e o [Docker](https://www.docker.com/) (com Docker Compose) instalados.

```bash
# 1. Clone o repositório
$ git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

# 2. Navegue até a pasta do projeto
$ cd seu-repositorio

# 3. Crie o arquivo de variáveis de ambiente
# (No Windows, use 'copy .env.example .env')
$ cp .env.example .env

# 4. Suba os contêineres com Docker Compose
# O comando --build é necessário apenas na primeira vez
$ docker compose up --build

# 5. (Em um novo terminal) Crie as tabelas no banco de dados
$ docker compose exec api python create_tables.py