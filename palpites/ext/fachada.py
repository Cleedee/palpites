from sqlalchemy import select

from palpites.ext.database import Time, Usuario, Jogador, TimeTorneio, db
from palpites.ext.database import Grupo, Torneio

def traga_time_por_sigla(sigla):
    return Time.query.filter(Time.sigla == sigla).one_or_none()

def traga_times(torneio_id):
    stmt = select(Time).join(
        TimeTorneio, TimeTorneio.time_id == Time.id
        ).where(
            TimeTorneio.torneio_id == torneio_id
        ).order_by(Time.nome)
    return db.session.execute(stmt).scalars()

def traga_usuarios():
    return Usuario.query.all()

def traga_usuario_por_apelido(apelido):
    return Usuario.query.filter(Usuario.apelido == apelido).one_or_none()

def traga_jogadores(grupo_id):
    return Jogador.query.filter(Jogador.grupo_id == grupo_id).all()

def traga_jogador_por_usuario(usuario_id, grupo_id):
    return Jogador.query.filter(
        Jogador.usuario_id == usuario_id,
        Jogador.grupo_id == grupo_id
    ).one_or_none()

def traga_grupos():
    return Grupo.query.all()

def traga_torneios():
    return Torneio.query.all()