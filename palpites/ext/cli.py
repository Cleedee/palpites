import click

from palpites.ext.database import db, Time, Jogador

EVENT0S = {
    'serie_a_2021': [
        ('América-MG','america'), ('Athletico-PR','athletico'), ('Atlético-GO','cag'),
        ('Atlético-MG','atletico_mg'), ('Bahia', 'bahia'), ('Bragantino', 'bragantino'),
        ('Ceará', 'ceara'), ('Chapecoense', 'chapecoense'), ('Corinthians','corinthians'),
        ('Cuiabá', 'cuiaba'), ('Flamengo', 'flamengo'), ('Fluminense', 'fluminense'),
        ('Fortaleza', 'fortaleza'), ('Grêmio', 'gremio'), ('Internacional', 'inter'),
        ('Juventude', 'juventude'), ('Palmeiras', 'palmeiras'), ('Santos', 'santos'),
        ('São Paulo', 'spfc'), ('Sport Recife', 'sport')
    ],
    'premier2021': [
        ('Arsenal', 'arsenal'), ('Aston Villa', 'aston_villa'),
        ('Brenford', 'brentford'), ('Brighton', 'brighton'),
        ('Burnley', 'burnley'), ('Chelsea', 'chelsea'),
        ('Crystal Palace', 'crystal_palace'), ('Everton', 'everton'),
        ('Leeds United', 'leeds'), ('Leicester City', 'leicester'),
        ('Liverpool', 'liverpool'), ('Manchester City', 'man_city'),
        ('Manchester United', 'man_united'), ('Newcastle', 'newcastle'),
        ('Norwich', 'norwich'), ('Southampton', 'southampton'),
        ('Tottenham', 'tottenham'), ('Watford', 'watford'),
        ('West Ham', 'west_ham'), ('Wolves', 'wolves')
    ]
}

DESCRICOES = [
    ('serie_a_2021', 'Clubes da Série A do Campeonato Brasileiro 2021'),
    ('premier2021', 'Clubes da Premier League 2021-2022')
]


def init_app(app):

    @app.cli.command('init-database')
    def criar_tabelas():
        db.create_all()

    @app.cli.command('load-teams')
    @click.argument('event')
    def carregar_times(event):
        times = EVENT0S.get(event)
        if times:
            for time in times:
                db.session.add(Time(nome=time[0], sigla=time[1]))
            db.session.commit()
        else:
            for descricao in DESCRICOES:
                print('{} - {}'.format(descricao[0], descricao[1]))
            print('Evento não encontrado.')

    @app.cli.command('new-player')
    @click.argument('name')
    def novo_jogador(name):
        db.session.add(Jogador(nome=name))
        db.session.commit()
        print(f'Jogador {name} criado.')

    @app.cli.command('events')
    def listar_eventos():
        for descricao in DESCRICOES:
            print('{} - {}'.format(descricao[0], descricao[1]))
