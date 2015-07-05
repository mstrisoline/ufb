#Mnager from Flask-Script and Flask-Migrate to handle DB Migrations easily
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from ufb import app
from ufb.models import db
app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
