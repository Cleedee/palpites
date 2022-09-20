from collections import namedtuple

import requests

def ordenar_pela_pontuacao_da_rodada(jogadores: dict):
    ParcialJogador = namedtuple('ParcialJogador','jogador pontos')
    lista = list(jogadores.items())
    parciais = []
    for jogador, pontos in lista:
        parciais.append( ParcialJogador(jogador, pontos) )
    return sorted(parciais, key=lambda x: getattr(x, 'pontos'), reverse=True)

def api_pega_partidas_rodada(api_key, campeonato_id, rodada):
    headers = {
        'Authorization': 'Bearer {}'.format(api_key)
    }

    URL_API = 'https://api.api-futebol.com.br/v1/'

    r = requests.get(URL_API + 'campeonatos/{}/rodadas/{}'.format(campeonato_id,rodada), headers=headers)
    retorno = r.json()
    partidas = retorno['partidas']
    return [(p['time_mandante']['nome_popular'], p['time_visitante']['nome_popular']) for p in partidas]