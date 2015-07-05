from flask.ext.login import LoginManager
from .models import *

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
