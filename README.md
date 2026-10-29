Painel de gestão de servidores de jogos

Este é o projeto que vou desenvolver para o curso. A ideia é criar um painel web para criar e gerir servidores de jogos em máquinas que já tenho, como uma VPS e um Raspberry Pi.

Neste momento o projeto ainda está em fase inicial. A base de dados e a ideia do painel já foram pensadas, mas a aplicação ainda vai ser construída.

## Problema

Tenho alguns servidores de jogos em máquinas diferentes. Para criar, iniciar, parar ou ver um servidor tenho de entrar em cada máquina. A ideia deste projeto é juntar estas tarefas num só painel.

## O que quero que o painel faça

- Registar utilizadores.
- Mostrar os jogos disponíveis.
- Deixar escolher um plano com número de slots.
- Criar um servidor numa máquina que já esteja configurada.
- Iniciar, parar e ver o estado de um servidor.
- Dar acesso limitado a amigos de confiança.
- Guardar um histórico das ações feitas no painel.
- Ter uma loja/carrinho apenas simulada para o projeto do curso. Não existem pagamentos reais.

O primeiro jogo que quero usar como teste é o Palworld em Linux. Mais tarde quero tentar adicionar outros jogos, como Satisfactory e Euro Truck Simulator.

## Tecnologias previstas

- Python para a aplicação.
- Flask para criar o painel web.
- HTML e CSS para a interface.
- SQLite para a base de dados.
- Git e GitHub para guardar as versões do projeto.
- SteamCMD para instalar alguns servidores de jogos quando for necessário.

## Base de dados

O modelo inicial inclui tabelas para utilizadores, jogos, planos, pedidos, máquinas, servidores e histórico. Os pedidos representam a parte simulada do carrinho/loja.

As palavras-passe dos utilizadores não devem ser guardadas em texto normal. As contas Steam também não serão guardadas na base de dados.

## Estado do projeto

O projeto está no início. Os próximos passos são criar a estrutura em Python, ligar a base de dados SQLite e fazer primeiro as opções básicas de utilizador, jogo e servidor.

## Nota

Este projeto é para uso pessoal e para o curso. Não é um serviço de alojamento real nem processa pagamentos.
