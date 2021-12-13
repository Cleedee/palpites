from flask.helpers import flash, url_for
from flask_login import LoginManager
from werkzeug.utils import redirect

from palpites.ext.database import Usuario

def init_app(app):
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'Por favor, logue-se para ter acesso à página.'

    @login_manager.user_loader
    def load_user(user_id):
        if user_id is not None:
            return Usuario.query.filter(Usuario.apelido == user_id).one_or_none()
        return None

    @login_manager.unauthorized_handler
    def unauthorized():
        flash('Logue-se primeiro para acessar a página.')
        return redirect(url_for('auth.login'))

    login_manager.init_app(app)        