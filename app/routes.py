from app import app
from model import recipe as rp
from db import db
from flask import jsonify, request, abort, make_response
from utils import validation


db_obj = db.Db('csv', 'data')
db_connection = db_obj.get_db()


@app.route('/gousto/api/v1.0/recipes', methods=['POST'])
def add_recipe():
    """ Add a recipe
    """

    validate_request()

    recipe_obj = rp.Recipe(db_connection)
    row = recipe_obj.add_recipe(request.json)

    return jsonify(row)


@app.route('/gousto/api/v1.0/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    """ Update recipe
    Args:
        id (int): id of recipe to update
    """

    validate_request()

    recipe_obj = rp.Recipe(db_connection)
    row = recipe_obj.update_recipe(id, request.json)

    return jsonify(row)


@app.route('/gousto/api/v1.0/recipes/<int:id>', methods=['GET'])
def recipe(id):
    """ Display recipe by id
    Args:
        id (int): id of recipe to display
    """
    recipe_obj = rp.Recipe(db_connection)
    fields = request.args.get('fields', '*')
    row = recipe_obj.get_recipe_by_id(id, fields)

    return jsonify(row)


@app.route('/gousto/api/v1.0/recipes/cuisine/<string:cuisine>', methods=['GET'])
def recipes(cuisine):
    """ Display recipes by cuisine
    Args:
        cuisine (string): cuisine
    """
    recipe_obj = rp.Recipe(db_connection)
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 10)
    fields = request.args.get('fields', 'id,slug,title,recipe_cuisine,recipe_diet_type_id,gousto_reference,created_at,updated_at')
    results = recipe_obj.get_recipes_by_cuisine(cuisine, int(offset), int(limit), fields)

    return jsonify(results)


@app.route('/gousto/api/v1.0/recipes/rating/<int:id>', methods=['PUT'])
def rating_recipe(id):
    """ Rate recipe by id
    Args:
        id (int): id of recipe to rate
    """
    validate_rating()

    recipe_obj = rp.Recipe(db_connection)
    row = recipe_obj.rate_recipe(id, request.json)

    return jsonify(row)


@app.errorhandler(404)
def not_found(error):
    """ Not found error
     Args:
         error (dict): error
    """

    return make_response(jsonify({'error': str(error)}), 404)


@app.errorhandler(400)
def bad_request(error):
    """ bad request error
     Args:
         error (dict): error
     """

    return make_response(jsonify({'error': str(error)}), 400)


def validate_request():
    """ Validate request for create/update
    """

    val_obj = validation.Validation()

    mandatory_fields = ['title', 'marketing_description', 'recipe_diet_type_id', 'recipe_cuisine', 'gousto_reference']
    if not request.json:
        abort(404, 'not a json request')
    for field in mandatory_fields:
        if field not in request.json:
            abort(400, field+' not found')

    numeric_fields = ['calories_kcal', 'carbs_grams', 'fat_grams', 'gousto_reference', 'preparation_time_minutes', 'protein_grams', 'shelf_life_days']
    for field in numeric_fields:
        if field in request.json:
            if val_obj.is_numeric(request.json[field]) is False:
                abort(400, field+' should be numeric')


def validate_rating():
    """ Validate request for rating
    """
    val_obj = validation.Validation()

    if not request.json:
        abort(404, 'not a json request')

    if 'rating' not in request.json:
        abort(400, 'rating not found')

    if val_obj.is_in_range(request.json['rating'], 0, 5) is False:
        abort(400, 'rating should be between 0 to 5')

    if len(request.json) > 1:
        abort(400, 'only rating field is allowed')

