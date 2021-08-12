from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Time(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column('nome', db.String(40))
    sigla = db.Column('sigla', db.String(10))

    @property
    def imagem(self):
        return f'{self.sigla}.png'

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column('nome', db.String(40))
    pontos = db.Column(db.Integer)

    @property
    def imagem(self):
        return f'token_{self.id}.png'    

class Rodada(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column('nome', db.String(40))

class Partida(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rodada_id = db.Column(db.Integer, db.ForeignKey('rodada.id'))
    rodada = db.relationship('Rodada', foreign_keys=[rodada_id])
    mandante_id = db.Column(db.Integer, db.ForeignKey('time.id'))
    mandante = db.relationship('Time', foreign_keys=[mandante_id])
    visitante_id = db.Column(db.Integer, db.ForeignKey('time.id'))
    visitante = db.relationship('Time', foreign_keys=[visitante_id])
    resultado = db.Column(db.String(1), default='S')
    palpites = db.relationship('Palpite', back_populates="partida")

class Palpite(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    apostador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'))
    apostador = db.relationship('Jogador', foreign_keys=[apostador_id])
    partida_id = db.Column(db.Integer, db.ForeignKey('partida.id'))
    partida = db.relationship('Partida', foreign_keys=[partida_id], back_populates="palpites")
    resultado = db.Column(db.String(1), default='E')

    @property
    def acertou(self):
        return (self.partida.resultado == self.resultado)

    @property
    def imagem(self):
        if self.resultado == 'S':
            return 'interrogacao.png'
        elif self.resultado == 'M':
            return self.partida.mandante.imagem
        elif self.resultado == 'V':
            return self.partida.visitante.imagem
        else:
            return 'e.png'

def init_app(app):
    db.init_app(app)
