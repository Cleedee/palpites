from flask import render_template, Blueprint, request, redirect, url_for
from flask.helpers import flash
from flask_login import login_user, login_required, logout_user

from palpites.ext.forms import LoginForm
import palpites.ext.repository as rep
from palpites.ext.database import Usuario

def init_app(app):

    bp = Blueprint('auth', __name__, template_folder='templates'
        ,static_folder='static', url_prefix='/auth')

    @bp.route('/login', methods = ['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            usuario: Usuario = rep.traga_usuario_por_apelido(form.apelido.data)
            if usuario and usuario.checar_senha(form.senha.data):
                login_user(usuario)
                proxima_pagina = request.args.get('next')
                return redirect(proxima_pagina or url_for('index'))
            flash('Usuário/senha inválida')
            return redirect(url_for('auth.login'))
        return render_template('auth/login.html', form=form)

    @bp.get('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('auth.login'))

    app.register_blueprint(bp)