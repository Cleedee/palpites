from flask import render_template, Blueprint, request, redirect, url_for
from flask.helpers import flash
from flask_login import login_required, current_user

from palpites.ext.forms import GrupoForm
from palpites.ext.database import Grupo
import palpites.ext.repository as rep

def init_app(app):

    bp = Blueprint('grupo', __name__, template_folder='templates'
        ,static_folder='static', url_prefix='/grupo')

    @bp.get('/')
    @login_required
    def index():
        grupos = rep.traga_grupos_por_dono(current_user.id)
        return render_template('grupo/index.html', grupos=grupos)

    @bp.get('/novo_grupo')
    @login_required
    def novo_grupo():
        form = GrupoForm()
        form.dono.data = current_user.apelido
        return render_template('grupo/grupo.html', form=form)

    @bp.post('/grupo')
    @login_required
    def salvar_grupo():
        form = GrupoForm()
        if form.validate_on_submit():
            grupo = Grupo(
                nome = form.nome.data,
                dono_id = current_user.id,
            )
            rep.salve_grupo(grupo)
            flash('Grupo cadastrado com sucesso.')
            return redirect(url_for('grupo.index'))

    app.register_blueprint(bp)
