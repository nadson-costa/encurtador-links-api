# Encurtador de URLs com UTM, gerador de QR Code e validação de segurança

[![Documentação](https://img.shields.io/badge/Ver_Documenta%C3%A7%C3%A3o-49CC90?style=for-the-badge&logo=docs&logoColor=white))](https://encurtador.teste-app.com.br/docs)
[![Front-end para teste da API](https://img.shields.io/badge/Ver_Demonstração-007BFF?style=for-the-badge&logo=rocket&logoColor=white)](https://encurtador.teste-app.com.br)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-1.25-009639?style=for-the-badge&logo=nginx&logoColor=white)

---

### Descrição

Um serviço de backend para encurtamento de URLs, construído com Python e FastAPI. O projeto permite não apenas a criação de links curtos, mas também a adição dinâmica de parâmetros UTM para rastreamento de campanhas, a geração instantânea de QR Codes e a validação de segurança de URLs contra a API do Google Safe Browsing para prevenir o uso malicioso do serviço.

A aplicação é totalmente conteinerizada com Docker, servida através de um proxy reverso Nginx com certificado SSL e possui um frontend simples e interativo para demonstrar as funcionalidades.

### Demonstraçao(GIF)

![demo-encurtador](https://github.com/user-attachments/assets/a360d5dc-82d3-4fe8-8b2d-9d5caccb9b8a)


### Funcionalidades principais

* **Encurtamento de URL:** Converte URLs longas em links curtos e únicos usando um algoritmo Base62.
* **Adição de parâmetros UTM:** Anexa dinamicamente parâmetros `utm_source`, `utm_medium`, `utm_campaign`, etc., à URL original, ideal para marketing digital.
* **Geração de QR Code:** Gera um QR Code para cada link encurtado através de um endpoint dedicado (`/{short_code}/qrcode`).
* **Validação de segurança:** Integração com a API **Google Safe Browsing** para bloquear a criação de links para domínios maliciosos conhecidos.
* **Frontend interativo:** Uma interface simples e bem construída para consumir a API, feita com HTML, CSS e JavaScript puros.
* **Documentação automática:** A API é 100% documentada e testável via interface Swagger UI em [`/docs`](https://encurtador.teste-app.com.br/docs).

### Stacks do projeto

* **Backend:** Python 3.11, FastAPI
* **Banco de Dados:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validação de dados:** Pydantic
* **Comunicação com APIs Externas:** HTTPX
* **Conteinerização:** Docker & Docker Compose
* **Proxy reverso e servidor web:** Nginx
* **Certificado SSL:** Let's Encrypt (via Certbot)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Hospedagem:** Servidor VPS (Ubuntu)
* **DNS & CDN:** Cloudflare

### Como executar localmente

Para executar este projeto no seu ambiente, você precisará ter o [Git](https://git-scm.com/) e o [Docker](https://www.docker.com/) (com Docker Compose) instalados.

```bash
# 1. Clone o repositório
$ git clone [https://github.com/nadson-costa/encurtador-links-api.git](https://github.com/nadson-costa/encurtador-links-api.git)

# 2. Navegue até a pasta do projeto
$ cd encurtador-links-api

# 3. Crie e preencha o arquivo de variáveis de ambiente
# (No Windows, use 'copy .env.example .env')
$ cp .env.example .env

# 4. Adicione suas chaves secretas ao arquivo .env
#    (DATABASE_URL e SAFE_BROWSING_API_KEY)

# 5. Suba os contêineres com Docker Compose
# O comando --build é necessário apenas na primeira vez
$ docker compose up --build -d

# 6. (Em um novo terminal) Crie as tabelas no banco de dados
$ docker compose exec api python create_tables.py
