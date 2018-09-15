from flask import Flask
from config import get_app_config
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from .models import db, migrate
from .api import api


def create_app(app_config=None):
    app = Flask(__name__)

    # setting foodie_app config
    app_config = app_config if app_config else get_app_config()
    app.config.from_object(app_config)

    # init db
    db.init_app(app)
    migrate.init_app(app, db)

    # register jwt manager
    flask_bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    # register blueprints
    app.register_blueprint(api)

    return app