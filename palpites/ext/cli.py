import click

from palpites.ext.database import db, Time

eventos = {
    'serie_a_2021': [
        ('América-MG','america'), ('Athletico-PR','athletico'), ('Atlético-GO','cag'),
        ('Atlético-MG','atletico_mg'), ('Bahia', 'bahia'), ('Bragantino', 'bragantino'),
        ('Ceará', 'ceara'), ('Chapecoense', 'chapecoense'), ('Corinthians','corinthians'),
        ('Cuiabá', 'cuiaba'), ('Flamengo', 'flamengo'), ('Fluminense', 'fluminense'),
        ('Fortaleza', 'fortaleza'), ('Grêmio', 'gremio'), ('Internacional', 'inter'),
        ('Juventude', 'juventude'), ('Palmeiras', 'palmeiras'), ('Santos', 'santos'),
        ('São Paulo', 'spfc'), ('Sport Recife', 'sport')
    ]
}


def init_app(app):

    @app.cli.command('init-database')
    def criar_tabelas():
        db.create_all()

    @app.cli.command('load-teams')
    @click.argument('event')
    def carregar_times(event):
        times = eventos[event]
        for time in times:
            db.session.add(Time(nome=time[0], sigla=time[1]))
        db.session.commit()
