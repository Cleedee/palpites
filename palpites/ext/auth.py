from flask_login import LoginManager

from palpites.ext.database import Usuario

def init_app(app):
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'Por favor, logue-se para ter acesso à página.'

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.filter(Usuario.apelido == user_id).one_or_none()    

    login_manager.init_app(app)        