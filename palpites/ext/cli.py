import click

from palpites.ext.database import db, Time, Jogador, Usuario, TimeTorneio
from palpites.ext.database import Grupo, Torneio
from palpites.ext import fachada

EVENT0S = {
    'serie_a_2023': [
        ('América-MG', 'america'), 
        ('Athletico-PR','athletico'), 
        ('Atlético-MG', 'atletico_mg'), 
        ('Bahia', 'bahia'),
        ('Botafogo', 'botafogo'),
        ('Bragantino', 'bragantino'),
        ('Corinthians', 'corinthians'),
        ('Coritiba', 'coritiba'),
        ('Cruzeiro', 'cruzeiro'),
        ('Cuiabá', 'cuiaba'), 
        ('Flamengo', 'flamengo'),
        ('Fluminense', 'fluminense'),
        ('Fortaleza', 'fortaleza'), 
        ('Goiás', 'goias'), 
        ('Grêmio', 'gremio'),
        ('Internacional', 'inter'),
        ('Palmeiras', 'palmeiras'), 
        ('Santos', 'santos'),
        ('São Paulo', 'spfc'),
        ('Vasco', 'vasco')
    ],    
    'serie_a_2022': [
        ('América-MG', 'america'), ('Athletico-PR',
                                    'athletico'), ('Atlético-GO', 'cag'),
        ('Atlético-MG', 'atletico_mg'), ('Avaí', 'avai'),
        ('Botafogo', 'botafogo'),
        ('Bragantino', 'bragantino'),
        ('Ceará', 'ceara'), ('Corinthians', 'corinthians'),
        ('Coritiba', 'coritiba'),
        ('Cuiabá', 'cuiaba'), ('Flamengo', 'flamengo'),
        ('Fluminense', 'fluminense'),
        ('Fortaleza', 'fortaleza'), ('Goiás',
                                     'goias'), ('Internacional', 'inter'),
        ('Juventude', 'juventude'), ('Palmeiras',
                                     'palmeiras'), ('Santos', 'santos'),
        ('São Paulo', 'spfc')
    ],
    'serie_a_2021': [
        ('América-MG', 'america'), ('Athletico-PR',
                                    'athletico'), ('Atlético-GO', 'cag'),
        ('Atlético-MG', 'atletico_mg'), ('Bahia',
                                         'bahia'), ('Bragantino', 'bragantino'),
        ('Ceará', 'ceara'), ('Chapecoense',
                             'chapecoense'), ('Corinthians', 'corinthians'),
        ('Cuiabá', 'cuiaba'), ('Flamengo', 'flamengo'),
        ('Fluminense', 'fluminense'),
        ('Fortaleza', 'fortaleza'), ('Grêmio',
                                     'gremio'), ('Internacional', 'inter'),
        ('Juventude', 'juventude'), ('Palmeiras',
                                     'palmeiras'), ('Santos', 'santos'),
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
    ('serie_a_2022', 'Clubes da Série A do Campeonato Brasileiro 2022'),
    ('serie_a_2023', 'Clubes da Série A do Campeonato Brasileiro 2023'),
    ('premier2021', 'Clubes da Premier League 2021-2022')
]


def init_app(app):

    @app.cli.command('init-database')
    def criar_tabelas():
        db.create_all()

    @app.cli.command('load-teams')
    @click.argument('event')
    @click.argument('tournament')
    def carregar_times(event, tournament):
        tuplas = EVENT0S.get(event)
        if tuplas:
            for tupla in tuplas:
                # procurar o time
                time = fachada.traga_time_por_sigla(tupla[1])
                if time:
                    db.session.add(TimeTorneio(time_id=time.id, torneio_id=tournament))
                else:
                    # cadastrar novo time
                    time = Time(nome=tupla[0], sigla=tupla[1])
                    db.session.add(time)
                    time = fachada.traga_time_por_sigla(tupla[1])
                    db.session.add(TimeTorneio(time_id=time.id, torneio_id=tournament))
            db.session.commit()
        else:
            for descricao in DESCRICOES:
                print('{} - {}'.format(descricao[0], descricao[1]))
            print('Evento não encontrado.')

    @app.cli.command('new-player')
    @click.argument('name')
    @click.argument('nick')
    @click.argument('group')
    def novo_jogador(name, nick, group):
        usuario = fachada.traga_usuario_por_apelido(nick)
        if not usuario:
            print('Usuário não encontrado.')
        jogador = Jogador(nome=name, usuario_id=usuario.id, grupo_id=group)
        db.session.add(jogador)
        db.session.commit()
        print(f'Jogador {name} criado com id {jogador.id}.')
        print(
            f'Coloque a imagem avatar com o nome token_{jogador.id}.png em palpites/static.')

    @app.cli.command('events')
    def listar_eventos():
        for descricao in DESCRICOES:
            print('{} - {}'.format(descricao[0], descricao[1]))

    @app.cli.command('users')
    def users():
        usuarios = fachada.traga_usuarios()
        for usuario in usuarios:
            print('{} - {}'.format(usuario.id, usuario.apelido))

    @app.cli.command('groups')
    def groups():
        grupos = fachada.traga_grupos()
        for grupo in grupos:
            print('{} - {}'.format(grupo.id, grupo.nome))

    @app.cli.command('tournaments')
    def tournaments():
        torneios = fachada.traga_torneios()
        for torneio in torneios:
            print('{} - {}'.format(torneio.id, torneio.nome))

    @app.cli.command('players')
    @click.argument('group')
    def players(group):
        jogadores = fachada.traga_jogadores(group)
        for jogador in jogadores:
            print('{} - {}'.format(jogador.usuario.apelido, jogador.grupo.id))

    @app.cli.command('new-user')
    @click.argument('apelido')
    @click.argument('senha')
    def novo_usuario(apelido, senha):
        usuario = Usuario(apelido=apelido)
        usuario.set_senha(senha)
        db.session.add(usuario)
        db.session.commit()
        print('Usuario criado.')

    @app.cli.command('new-group')
    @click.argument('name')
    @click.argument('owner')
    @click.argument('tournament')
    def novo_grupo(name, owner, tournament):
        grupo = Grupo(nome=name, dono_id=int(owner), torneio_id=int(tournament))
        db.session.add(grupo)
        db.session.commit()
        print('Grupo Criado.')

    @app.cli.command('new-tournament')
    @click.argument('name')
    @click.argument('owner')
    def novo_torneio(name, owner):
        torneio = Torneio(nome=name, responsavel_id=owner)
        db.session.add(torneio)
        db.session.commit()
        print('Torneio Criado.')