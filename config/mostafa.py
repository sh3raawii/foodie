import os
from .base import BaseConfig


class MostafaConfig(BaseConfig):
    SECRET_KEY = os.environ.get("SECRET_KEY", default="MostafaDevelopmentKey")
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
