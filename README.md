# Twitter Clone MVP 🐦

Projeto Final de Web Development focado em arquitetura monolítica com Django.

## 🚀 Funcionalidades
- **Autenticação:** Cadastro e Login de usuários.
- **Microblogging:** Criação de Tweets (280 caracteres).
- **Social:** Sistema de Follow (Seguir/Deixar de seguir).
- **Interações:** Curtidas e Comentários em tempo real.
- **Perfil:** Edição de foto, bio e dados pessoais.

## 🛠️ Tech Stack
- **Back-end:** Python / Django (Monolítico)
- **Banco de Dados:** PostgreSQL
- **Estilização:** Tailwind CSS (via CDN)
- **Deploy:** Render + Docker

## 📦 Como rodar localmente (Docker)
1. Clone o repositório.
2. Crie um arquivo `.env` baseado no modelo.
3. Rode `docker-compose up --build`.
4. Acesse `localhost:8000`.

## Deploy no Render

Este projeto usa PostgreSQL no Render. Como o plano FREE permite apenas um banco, criei um schema separado chamado `twitter_clone`.

### Variáveis de ambiente
- SECRET_KEY
- DEBUG
- DJANGO_ALLOWED_HOSTS
- SQL_ENGINE=django.db.backends.postgresql
- SQL_DATABASE=<nome_do_banco_existente>
- SQL_USER=<usuário>
- SQL_PASSWORD=<senha>
- SQL_HOST=<host>
- SQL_PORT=5432

### Dockerfile
O comando final roda migrações e inicia o servidor:
CMD ["sh", "-c", "python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:8000"]