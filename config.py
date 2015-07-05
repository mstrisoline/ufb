import os

#General Application Configuration
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    _cwd = os.path.dirname(os.path.abspath(__file__))

#Production Specific Configuration
class ProductionConfig(Config):
    DEBUG = False

#Dev Specific Configuration
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

#Testing Specific Configuration
class TestingConfig(Config):
    TESTING = True
