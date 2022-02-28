from flask import render_template, Blueprint, request, redirect, url_for
from flask.helpers import flash
from flask_login import login_required

def init_app(app):

    bp = Blueprint('grupo', __name__, template_folder='templates'
        ,static_folder='static', url_prefix='/grupo')

    @bp.get('/')
    @login_required
    def index():
        return render_template('grupo/index.html')

    app.register_blueprint(bp)
