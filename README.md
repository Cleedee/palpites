# palpites

Após você baixar o código via git clone, será necessário realizar algumas ações:

1) Criar um arquivo .env na pasta raiz para adicionar as seguintes variáveis

FLASK_APP=palpites

FLASK_ENV=development

SECRET_KEY=<coloque aqui uma senha complexa>

SQLALCHEMY_DATABASE_URI=sqlite:///banco.db

APP_NAME=Palpites

2) Criar um ambiente virtual com o seguinte comando na pasta raiz

$ python -m venv env

$ source env/bin/activate

3) Instalar as dependências

$ pip install -r requirements.txt

4) Com o ambiente ativado com o comando anterior, crie as tabelas do banco de dados:

$ flask init-database

5) Cadastre os jogadores

$ flask new-player "Nome do Jogador"

6) Carregue os times pela liga

$ flask load-teams serie_a_2021

Para criar os tokens dos jogadores, use a ferramenta online Token Stamp: http://rolladvantage.com/tokenstamp/