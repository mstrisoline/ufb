from flask import Flask
from .models import db
from .views import *
from .authentication import login_manager
import os


#Applicaiton Initialization
app = Flask(__name__)
#Load App Settings based on ENV Var
app.config.from_object(os.environ['APP_SETTINGS'])

#Initialize DB
db.init_app(app)

#Initialize Blueprint for Routes
app.register_blueprint(site)

#Initialize Login Manager from Flask-Login
login_manager.init_app(app)
