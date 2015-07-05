#Isolate Login Manager stuff from rest of app
from flask.ext.login import LoginManager
from .models import *

#Create LoginManager Object
login_manager = LoginManager()

#Load user on login, helps decorate corruent_user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
