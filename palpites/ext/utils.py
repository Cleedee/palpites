from collections import namedtuple

def ordenar_pela_pontuacao_da_rodada(jogadores: dict):
    ParcialJogador = namedtuple('ParcialJogador','jogador pontos')
    lista = list(jogadores.items())
    parciais = []
    for jogador, pontos in lista:
        parciais.append( ParcialJogador(jogador, pontos) )
    return sorted(parciais, key=lambda x: getattr(x, 'pontos'), reverse=True)