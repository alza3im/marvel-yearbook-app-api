"""Flask configuration."""
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# SECRET_KEY = environ.get('SECRET_KEY')
# PUBLIC_KEY = environ.get('PUBLIC_KEY')


class BaseConfig:
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ""
    CELERY_BROKER = ""


class ProductionConfig(BaseConfig):
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = ""
    CELERY_BROKER = ""


class TestConfig(BaseConfig):
    FLASK_ENV = "development"
    TESTING = True
    DEBUG = True
