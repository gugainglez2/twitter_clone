# 🐦 Twitter Clone MVP - Gustavo Inglez

Projeto desenvolvido para conclusão de módulo, focado em Full Stack Development com Django.

## 🚀 Tecnologias
- **Back-end:** Django (Arquitetura Monolítica)
- **Front-end:** Django Templates + Tailwind CSS (via CDN)
- **Banco de Dados:** PostgreSQL (Produção) / SQLite (Desenvolvimento)
- **Deploy:** Render via Docker

## 🛠️ Requisitos Atendidos (7/10+)
- [x] **Autenticação:** Sistema completo de cadastro e login.
- [x] **Tweets:** CRUD de postagens com limite de caracteres.
- [x] **Social:** Sistema de Seguir (Follow) e Feed personalizado.
- [x] **Interações:** Curtidas e Comentários funcionais.
- [x] **Perfil:** Edição de dados do usuário e foto de perfil.

## 📦 Como rodar este projeto
1. Clone o repositório: `git clone https://github.com/gugainglez2/twitter_clone.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py migrate`
4. Inicie o servidor: `python manage.py runserver`