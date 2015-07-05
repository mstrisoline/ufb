from flask import Flask
from .models import db
from .views import *
from .authentication import login_manager
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)

app.register_blueprint(site)

login_manager.init_app(app)
