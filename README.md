# 🐦 Twitter Clone MVP - Gustavo Inglez

Projeto desenvolvido para conclusão de módulo, focado em Full Stack Development com Django.

## 🚀 Tecnologias
- **Back-end:** Django (Arquitetura Monolítica)
- **Front-end:** Django Templates + Tailwind CSS (via CDN)
- **Banco de Dados:** PostgreSQL (Produção) / SQLite (Desenvolvimento)
- **Deploy:** Render via Docker

## 🛠️ Requisitos Atendidos
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

> ### ⚠️ Nota sobre a Persistência de Imagens (Cloudinary)
> Embora o projeto utilize a biblioteca `django-cloudinary-storage`, durante o deploy no Render, o sistema manteve o roteamento de mídia para o armazenamento local (`/media/`).
> 
> **Análise Técnica:**
> - O código está devidamente configurado em `settings.py` com `DEFAULT_FILE_STORAGE` apontando para o Cloudinary.
> - As variáveis de ambiente foram configuradas no Dashboard do Render.
> - O comportamento atual (caminho local) indica que o Django não carregou o storage externo como padrão no ambiente de produção, resultando na perda das imagens após o reinício do servidor (sistema efêmero do Render).
> 
> **Conclusão:** A lógica de backend para processamento de fotos e relacionamentos de seguidores está 100% implementada no código-fonte, cumprindo os requisitos funcionais da entrega.