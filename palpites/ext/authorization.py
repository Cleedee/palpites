from flask_rbac import RBAC
from flask_rbac.model import RoleMixin

class Role(RoleMixin):
    ...

anonymous = Role('anonymous')
player = Role('player')
admin = Role('admin')

rbac = RBAC()

def init_app(app):
    rbac.set_role_model(Role)

    rbac.init_app(app)