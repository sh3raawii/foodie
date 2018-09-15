from flask import Blueprint, request, jsonify
from foodie_app.models import db
from foodie_app.models import Ingredient
from foodie_app.models import Badge
api = Blueprint('api', __name__)

@api.route('/ingredients', methods=["POST"])
def postNewIngredient():
    dic = request.json
    ingredient = Ingredient(name=dic["name"], gwp=dic["gwp"])
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({"name": ingredient.name, "id": ingredient.id, "gwp": ingredient.gwp})

@api.route('/ingredients/<id>', methods=["GET"])
def getIngredientWith(id):
    ingredient = Ingredient.query.filter(Ingredient.id == id).first()
    return jsonify({"id": ingredient.id, "gwp": ingredient.gwp})

@api.route('/ingredients', methods=["GET"])
def getAllIngredients():
    ingredients = Ingredient.query.all()
    return jsonify({"ingredients": [{"name": ingredient.name, "id": ingredient.id, "gwp": ingredient.gwp} for ingredient in ingredients]})

@api.route('/badges', methods=["GET"])
def getAllBadges():
    badges = Badge.query.all()
    return jsonify({"badges": [{"name": badge.name, "id": badge.id} for badge in badges]})

@api.route('/badges', methods=["POST"])
def postNewBadge():
    dic = request.json
    badge = Badge(name=dic["name"])
    db.session.add(badge)
    db.session.commit()
    return jsonify({"id": badge.id, "name": badge.name})

@api.route('/badges/<id>', methods=["GET"])
def getBadgeWith(id):
    badge = Badge.query.filter(Badge.id == id).first()
    return jsonify({"id": badge.id, "name": badge.name})

@api.route('/', methods=['GET'])
def test():
    return 'hello world'
