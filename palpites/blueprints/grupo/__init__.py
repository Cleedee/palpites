from flask import render_template, Blueprint, request, redirect, url_for
from flask.helpers import flash
from flask_login import login_required, current_user

from palpites.ext.forms import GrupoForm

def init_app(app):

    bp = Blueprint('grupo', __name__, template_folder='templates'
        ,static_folder='static', url_prefix='/grupo')

    @bp.get('/')
    @login_required
    def index():
        return render_template('grupo/index.html')

    @bp.get('/novo_grupo')
    @login_required
    def novo_grupo():
        form = GrupoForm()
        form.dono.data = current_user.apelido
        return render_template('grupo/grupo.html', form=form)

    app.register_blueprint(bp)
