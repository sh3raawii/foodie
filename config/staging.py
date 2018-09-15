import os
from .base import BaseConfig


class StagingConfig(BaseConfig):
    ENV = "production"
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)
