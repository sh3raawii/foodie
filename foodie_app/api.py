from flask import Blueprint, request, jsonify
from foodie_app.models import Ingredient
from foodie_app.models import db
api = Blueprint('api', __name__)

@api.route('/ingredients', methods=["POST"])
def postNewIngredient():
    ingredient = Ingredient(gwp=11.34)
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({"id": ingredient.id, "gwp": ingredient.gwp})

@api.route('/ingredients/<id>', methods=["GET"])
def getIngredientWith(id):
    ingredient = Ingredient.query.filter(Ingredient.id == id).first()
    return jsonify({"id": ingredient.id, "gwp": ingredient.gwp})

# @api.route('/badges/<id>')
# @api.route('/collections/<id>')

@api.route('/', methods=['GET'])
def test():
    return 'hello world'
