import requests
from functools import wraps
from flask import Blueprint, request, jsonify, session, g
from foodie_app.models import db, Ingredient, Badge, User, UserHistory
from passlib.hash import pbkdf2_sha256

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
    return jsonify({"ingredients": [{"name": ingredient.name, "id": ingredient.id, "gwp": ingredient.gwp, "image": ingredient.image} for ingredient in ingredients]})

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
            score = 1
            count = 0
            for res_ing in recipe["recipe"]["ingredientLines"]:
                res_ing = res_ing.lower()
                for ing in ingredients:
                    if ing in res_ing:
                        for db_ing in db_ingredients:
                            if db_ing.name == ing:
                                score = min(score, db_ing.gwp)
            recipes.append({"label": recipe["recipe"]["label"], "uri": recipe["recipe"]["shareAs"], "score": 20/score-8, "image": recipe["recipe"]["image"]})
    recipes = list({recipe["uri"]: recipe for recipe in recipes}.values())
    recipes.sort(key=lambda x: x["score"])
    return jsonify({"recipes": [{"label": recipe["label"], "uri": recipe["uri"], "score": recipe["score"], "image": recipe["image"]} for recipe in recipes]})

# User
@api.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify({"users": [{"name": user.name, "id": user.id, "email": user.email, "username": user.username} for user in users]})


@api.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if user:
        return jsonify({"users": {"name": user.name, "id": user.id, "email": user.email, "username": user.username}})
    else:
        return 'Couldn\'t find user with id {}'.format(id), 400


@api.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    name = request.json.get('name', None)
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not name:
        return jsonify({"msg": "Missing name parameter"}), 400
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    password = pbkdf2_sha256.hash(password)
    user = User(name=name, username=username, email=email, password=password, score=0)
    db.session.add(user)
    try:
        db.session.commit()
        return '', 200
    except Exception as exception:
        db.session.rollback()
        db.session.flush()
        return 'User Already Exists', 400

@api.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter(User.username == username).first()
    authenticated = pbkdf2_sha256.verify(password, user.password)
    if authenticated:
        session["user_id"] = user.id
        session["authenticated"] = authenticated
        return jsonify({"status": "success", "id": user.id}), 200
    else:
        return 'Username or password is incorrect', 401

@api.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return '', 200


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "authenticated" in session:
            g.user = User.query.filter(User.id == session.get("user_id")).first()
            return f(*args, **kwargs)
        return 'You have to login again', 401
    return decorated_function


@api.route('/testauth', methods=['GET'])
@login_required
def test_my_auth():
    print(g.get('user'))
    print(session)
    return '', 200


@api.route('/users/badges/<id>', methods=["POST"])
@login_required
def assign_badge(id):
    badge = Badge.query.filter(Badge.id == id).first()
    if badge is None:
        return 'badge id not found', 400
    g.user.badges.append(badge)
    db.session.commit()
    return 'badge appended', 200


@api.route('/users/badges', methods=["GET"])
@login_required
def get_user_badges():
    return jsonify({"badges": [{"name": badge.name, "id": badge.id} for badge in g.user.badges]})

@api.route('/users/recipes', methods=["POST"])
@login_required
def assign_recipe_to_user():
    body = request.json
    user = UserHistory(user_id=g.user.id, recipe_name=body["label"], recipe_uri=body["uri"])
    db.session.add(user)
    db.session.commit()
    return "added recipe to history", 200

@api.route('/users/recipes', methods=["GET"])
@login_required
def get_all_recipes_of_user():
    recipes = UserHistory.query.filter(UserHistory.user_id==g.user.id)
    recipes = list(recipes)
    recipes.sort(key=lambda x:x.timestamp)
    return jsonify({"recipes": [{"label": recipe.recipe_name, "uri": recipe.recipe_uri, "timestamp": recipe.timestamp} for recipe in recipes]}), 200