import os
from .base import BaseConfig


class TestingConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI",
                                             "postgresql://swvl:password@localhost/swvl_auth_test")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)
