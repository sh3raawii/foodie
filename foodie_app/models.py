from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# permissions = db.Table('permissions',
#                        db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False),
#                        db.Column('resource_id', db.Integer, db.ForeignKey('resource.id'), nullable=False, index=True),
#                        db.PrimaryKeyConstraint('group_id', 'resource_id'))
#
#
# class UserGroup(db.Model):
#     __table_args__ = (db.PrimaryKeyConstraint('user_id', 'group_id'),)
#     user_id = db.Column(db.String(128), nullable=False)
#     group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
#
#
#
#
# class Group(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#     description = db.Column(db.Text())
#     users = db.relationship('UserGroup', backref='group', lazy='dynamic')
#     resources = db.relationship('Resource', secondary=permissions, lazy='dynamic',
#                                 backref=db.backref('groups', lazy='dynamic'))
#
#
# class Resource(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#
#
# user_id_index = db.Index('user_id_index', UserGroup.user_id)
# resource_name_index = db.Index('resource_name_index', Resource.name)


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
