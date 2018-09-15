import os


class BaseConfig:
    ENV = "development"
    DEBUG = True
    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    SECRET_KEY = "development_key"

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Authentication
    JWT_SECRET_KEY = 'JWT_SECRET_KEY'
