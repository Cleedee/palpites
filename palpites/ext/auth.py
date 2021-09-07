from flask_login import LoginManager

from palpites.ext.database import Usuario

def init_app(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.filter(Usuario.id_alternativo == user_id).one_or_none()