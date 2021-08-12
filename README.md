# palpites

Após você baixar o código via git clone, será necessário realizar algumas ações:

1) Criar um arquivo .env na pasta raiz para adicionar as seguintes variáveis

FLASK_APP=palpites
FLASK_ENV=development
SECRET_KEY=<coloque aqui uma senha complexa>
SQLALCHEMY_DATABASE_URI=sqlite:///banco.db

2) Criar um ambiente virtual com o seguinte comando na pasta raiz

$ python -m venv env
$ source env/bin/activate

3) Com o ambiente ativado com o comando anterior, crie as tabelas do banco de dados:

$ flask init-database

4) Cadastre os jogadores

$ flask new-player "Nome do Jogador"

5) Carregue os times pela liga

$ flask load-teams serie_a_2021