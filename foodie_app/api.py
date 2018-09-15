from flask import Blueprint, request, jsonify
import requests
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

@api.route('/recipes', methods=['POST'])
def get_recipes():
    db_ingredients = Ingredient.query.all()
    ingredients = request.json
    ingredients = ingredients["ingredients"]
    recipes = list()
    for ingredient in ingredients:
        res = requests.get('https://api.edamam.com/search?q={}&app_id=4624bf98&app_key=0b77cc1602cbb9dd8db2f1618f00006c'.format(ingredient))
        res = res.json().get("hits", None)
        for recipe in res:
            score = 0
            for res_ing in recipe["recipe"]["ingredientLines"]:
                for ing in ingredients:
                    if ing in res_ing:
                        for db_ing in db_ingredients:
                            if db_ing.name == ing:
                                score += db_ing.gwp
            recipes.append({"label": recipe["recipe"]["label"], "uri": recipe["recipe"]["shareAs"], "score": score})
    recipes = list({recipe["uri"]: recipe for recipe in recipes}.values())
    return jsonify({"recipes": [{"label": recipe["label"], "uri": recipe["uri"], "score": recipe["score"]} for recipe in recipes]})