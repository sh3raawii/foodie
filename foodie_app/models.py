from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gwp = db.Column(db.Float, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),index=True, unique=True, nullable=False)
    email = db.Column(db.String(64),index=True, unique=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=True)

collection = db.Table('collection',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
                       db.Column('badge_id', db.Integer, db.ForeignKey('badge.id'), nullable=False),
                       db.PrimaryKeyConstraint('user_id', 'badge_id'))
