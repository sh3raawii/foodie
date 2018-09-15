import requests
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from foodie_app.models import db, Ingredient, Badge, User

api = Blueprint('api', __name__)

# Ingredients
@api.route('/ingredients', methods=["POST"])
def create_ingredient():
    body = request.json
    ingredient = Ingredient(name=body["name"], gwp=body["gwp"])
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({"name": ingredient.name, "id": ingredient.id, "gwp": ingredient.gwp})

@api.route('/ingredients/<id>', methods=["GET"])
def get_ingredient_by_id(id):
    ingredient = Ingredient.query.filter(Ingredient.id == id).first()
    return jsonify({"id": ingredient.id, "gwp": ingredient.gwp})

@api.route('/ingredients', methods=["GET"])
def get_all_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify({"ingredients": [{"name": ingredient.name, "id": ingredient.id, "gwp": ingredient.gwp} for ingredient in ingredients]})

# Badges
@api.route('/badges', methods=["GET"])
def get_all_badges():
    badges = Badge.query.all()
    return jsonify({"badges": [{"name": badge.name, "id": badge.id} for badge in badges]})

@api.route('/badges', methods=["POST"])
def create_badge():
    body = request.json
    badge = Badge(name=body["name"])
    db.session.add(badge)
    db.session.commit()
    return jsonify({"id": badge.id, "name": badge.name})

@api.route('/badges/<id>', methods=["GET"])
def get_badge_by_id(id):
    badge = Badge.query.filter(Badge.id == id).first()
    return jsonify({"id": badge.id, "name": badge.name})

# Testing root endpoint
@api.route('/', methods=['GET'])
def test():
    return 'Welcome to foodie application'

# Recipes
@api.route('/recipes', methods=['POST'])
def get_recipes():
    db_ingredients = Ingredient.query.all()
    ingredients = request.json
    ingredients = ingredients["ingredients"]
    recipes = list()
    for ingredient in ingredients:
        ingredient = ingredient.lower()
        res = requests.get('https://api.edamam.com/search?q={}&app_id=4624bf98&app_key=0b77cc1602cbb9dd8db2f1618f00006c'.format(ingredient))
        res = res.json().get("hits", None)
        for recipe in res:
            score = 0
            for res_ing in recipe["recipe"]["ingredientLines"]:
                res_ing = res_ing.lower()
                for ing in ingredients:
                    if ing in res_ing:
                        for db_ing in db_ingredients:
                            if db_ing.name == ing:
                                score += db_ing.gwp
            recipes.append({"label": recipe["recipe"]["label"], "uri": recipe["recipe"]["shareAs"], "score": score, "image": recipe["recipe"]["image"]})
    recipes = list({recipe["uri"]: recipe for recipe in recipes}.values())
    recipes.sort(key=lambda x: x["score"])
    return jsonify({"recipes": [{"label": recipe["label"], "uri": recipe["uri"], "score": recipe["score"], "image": recipe["image"]} for recipe in recipes]})

# User
# @api.route('/users', methods=['POST'])
# def create_user():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400
#
#     name = request.json.get('name', None)
#     username = request.json.get('username', None)
#     email = request.json.get('email', None)
#     password = request.json.get('password', None)
#
#     if not name:
#         return jsonify({"msg": "Missing name parameter"}), 400
#     if not username:
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not email:
#         return jsonify({"msg": "Missing email parameter"}), 400
#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400
#
#
#
# @api.route('/login', methods=['POST'])
# def login():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400
#
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#
#     if not username:
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400
#
#     if username != 'test' or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401
#
#     # Identity can be any data that is json serializable
#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token), 200
