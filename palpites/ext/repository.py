from typing import List

from sqlalchemy import or_, and_

from palpites.ext.database import Time, Jogador, Rodada, Partida, Palpite, db
from palpites.ext import utils

def traga_times():
    return Time.query.order_by(Time.nome).all()

def traga_jogadores():
    return Jogador.query.order_by(Jogador.pontos.desc()).all()

def traga_jogador(id):
    return Jogador.query.get(id)

def traga_rodadas():
    return Rodada.query.order_by(Rodada.id.desc()).all()

def traga_partidas_da_rodada(rodada_id):
    return Partida.query.filter(Partida.rodada_id == rodada_id).all()

def traga_ultimas_5_partidas_do(time: Time) -> List[Partida]:
    # TODO
    ...

def traga_rodada(rodada_id):
    return Rodada.query.get(rodada_id)

def traga_partida(partida_id):
    return Partida.query.get(partida_id)

def traga_palpite(id) -> Palpite:
    return Palpite.query.get(id)

def traga_palpites_da_rodada_do_jogador(rodada_id, jogador_id) -> List[Palpite]:
    return Palpite.query.join(Partida).filter(
        Palpite.apostador_id == jogador_id,
        Partida.rodada_id == rodada_id
    ).all()

def traga_palpites_da_rodada_do_jogador_nao_feitos(rodada_id, jogador_id) -> List[Palpite]:
    return Palpite.query.join(Partida).filter(
        Palpite.apostador_id == jogador_id,
        Partida.rodada_id == rodada_id,
        Palpite.resultado == 'S'
    ).all()

def traga_times_tuplados():
    times = Time.query.order_by(Time.nome).all()
    return [(t.id, t.nome) for t in times]

def traga_palpites_na_partida(partida_id):
    return Palpite.query.filter(Palpite.partida_id == partida_id).all()

def traga_palpites_da_rodada(rodada_id) -> List[Palpite]:
    return Palpite.query.join(Partida).filter(Partida.rodada_id == rodada_id).all()

def salve_partida(partida):
    db.session.add(partida)
    db.session.commit()

def salve_palpite(palpite):
    db.session.add(palpite)
    db.session.commit()

def gerar_palpites(partida_id):
    partida = traga_partida(partida_id)
    apostadores = Jogador.query.filter(
        Jogador.id.notin_(
            [p.apostador_id for p in partida.palpites]
        )
    ).all()
    for jogador in apostadores:
        db.session.add(Palpite(apostador_id=jogador.id,partida_id=partida_id,resultado='S'))
    db.session.commit()

def consolidar_rodada(rodada_id):
    players = {}
    jogadores = traga_jogadores()
    for j in jogadores:
        players[j.id] = j.pontos
    palpites = traga_palpites_da_rodada(rodada_id)
    for p in palpites:
        if p.resultado == p.partida.resultado:
            players[p.apostador_id] += 1
    for jogador in jogadores:
        jogador.pontos = players[jogador.id]
        db.session.add(jogador)
    db.session.commit()

def traga_parcial(rodada_id):
    players = {}
    jogadores = traga_jogadores()
    for j in jogadores:
        players[j] = 0
    palpites = traga_palpites_da_rodada(rodada_id)
    for p in palpites:
        if (p.resultado == p.partida.resultado) and (p.resultado != 'S'):
            players[p.apostador] += 1
    return utils.ordenar_pela_pontuacao_da_rodada(players)

def total_palpites_errados_por_time(time_id: int, jogador_id: int = None) -> int:
    if jogador_id is None:
        return Palpite.query.join(Partida).filter(
            or_(
                and_(
                    Partida.mandante_id == time_id,
                    Partida.resultado.in_(['V','E']),
                    Palpite.resultado == 'M'
                ),
                and_(
                    Partida.visitante_id == time_id,
                    Partida.resultado.in_(['M','E']),
                    Palpite.resultado == 'V'
                )
            )
        ).count()
    else:
        return Palpite.query.join(Partida).filter(
            or_(
                and_(
                    Partida.mandante_id == time_id,
                    Partida.resultado.in_(['V','E']),
                    Palpite.resultado == 'M'
                ),
                and_(
                    Partida.visitante_id == time_id,
                    Partida.resultado.in_(['M','E']),
                    Palpite.resultado == 'V'
                )
            ),
            Palpite.apostador_id == jogador_id
        ).count()    

def salve_rodada(rodada: Rodada):
    db.session.add(rodada)
    db.session.commit()
