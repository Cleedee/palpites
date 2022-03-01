from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, HiddenField,  SelectField, validators
from wtforms import SubmitField, PasswordField
from wtforms.validators import (DataRequired, Length, Optional,Email, ValidationError,
    InputRequired)

from palpites.ext.database import Partida, Palpite, Grupo

class PartidaForm(FlaskForm):
    partida_id = HiddenField()
    rodada_id = HiddenField()
    mandante = SelectField(u'Mandante', coerce=int, validators=[DataRequired()])
    visitante = SelectField(u'Visitante', coerce=int, validators=[DataRequired()])
    resultado = SelectField(u'Resultado',
        choices=[('E','Empate'),('M', 'Mandante'), ('V','Visitante'),('S','Sem Resultado')],
        default='S')
    submit_continuar = SubmitField('Salvar e Continuar')
    submit_salvar = SubmitField('Salvar e Sair')

class PalpiteForm(FlaskForm):
    palpite_id = HiddenField()
    resultado = SelectField(u'Palpite',
        choices=[('E','Empate'),('M', 'Mandante'), ('V','Visitante'),('S','Sem Palpite')])
    submit_salvar = SubmitField('Salvar e Sair')
    submit_seguir = SubmitField('Salvar e Seguir')

class LoginForm(FlaskForm):
    apelido = StringField(validators=[DataRequired()])
    senha = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Entrar')

class GrupoForm(FlaskForm):
    id = HiddenField()
    nome = StringField(validators=[DataRequired()], render_kw={'autofocus': True})
    dono = StringField()
    submit = SubmitField('Salvar')

def carregar_grupo(form: GrupoForm, grupo: Grupo, repository):
    form.id.data = grupo.id
    form.nome.data = grupo.nome
    forn.dono.data = grupo.dono.nome

def carregar_selecoes_partida(form, repository):
    times = repository.traga_times_tuplados()
    form.mandante.choices = times
    form.visitante.choices = times
    return form

def carregar_partida(form: PartidaForm, partida: Partida, repository):
    form.partida_id.data = partida.id
    form.rodada_id.data = partida.rodada_id
    form.mandante.data = partida.mandante_id
    form.visitante.data = partida.visitante_id
    form.resultado.data = partida.resultado

def atualizar_partida(form, partida: Partida):
    partida.mandante_id = form.mandante.data
    partida.visitante_id = form.visitante.data
    partida.resultado = form.resultado.data
    partida.rodada_id = form.rodada_id.data

def atualizar_palpite(form: PalpiteForm, palpite: Palpite):
    palpite.resultado = form.resultado.data
