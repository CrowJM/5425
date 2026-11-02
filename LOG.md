# LOG - DrakeNest

## 02/11/2026 - Início da estrutura do projeto

Nesta fase comecei a estrutura inicial do DrakeNest. A ideia é criar um painel web para gerir servidores de jogos.

Foi criado o ficheiro `app.py`, que inicia a aplicação em Flask e mostra a página inicial quando se abre o endereço local no navegador.

Também foi criado o ficheiro `database.py`, que vai ficar responsável pela ligação à base de dados SQLite. A base de dados fica na pasta `DrakeNestBD` com o nome `DrakeNestPainel.db`.

Foi criado ainda o `init_db.py`, para criar a base de dados manualmente quando for preciso.

Na pasta `templates` foram criados os ficheiros HTML da página inicial. O ficheiro `base.html` tem a estrutura comum da página e o `index.html` é a página de teste que aparece ao iniciar o projeto.

Na pasta `static/css` foi criado o `style.css`, com o aspeto básico da página.

Também foi adicionado o `.gitignore`, para não colocar no GitHub ficheiros criados automaticamente pelo Python, ambientes virtuais e ficheiros que possam ter dados locais. Ainda é preciso corrigir uma regra para ignorar a base de dados que está na pasta `DrakeNestBD`.

## Estado atual

O projeto já tem uma página inicial de teste e a separação básica dos ficheiros. Ainda não cria nem gere servidores reais e não existe ligação a VPS ou a outras máquinas.

## Próximas coisas a fazer

- Criar o ficheiro `schema.sql` com as tabelas da base de dados.
- Testar corretamente a criação da base de dados.
- Criar as páginas para jogos, máquinas e servidores.
- Criar registo e início de sessão de utilizadores.
- Só mais à frente testar uma ligação a uma máquina de teste.