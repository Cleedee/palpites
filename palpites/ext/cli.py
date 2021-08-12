from palpites.ext.database import db

def init_app(app):

    @app.cli.command('init-database')
    def criar_tabelas():
        db.create_all()
