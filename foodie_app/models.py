import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gwp = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text)

collection = db.Table('collection',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
                       db.Column('badge_id', db.Integer, db.ForeignKey('badge.id'), nullable=False),
                       db.PrimaryKeyConstraint('user_id', 'badge_id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),index=True, unique=True, nullable=False)
    email = db.Column(db.String(64),index=True, unique=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Float, nullable=False, server_default="0")
    badges = db.relationship('Badge', secondary=collection, lazy='dynamic',
                                backref=db.backref('users', lazy='dynamic'))

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=True)
    extid = db.Column(db.Integer, nullable=True)

class UserHistory(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    recipe_name = db.Column(db.String(64), nullable=False)
    recipe_uri = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, primary_key=True)