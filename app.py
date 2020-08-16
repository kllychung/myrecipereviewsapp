import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Recipe, Reviews, setup_db
from auth import AuthError, requires_auth

def create_app(test_config=None):

 # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
    @implement endpoint
        GET /recipes
            it should require the 'get:recipes' permission available to reader and recipe publisher
            it should contain only the drink.format() data representation
        returns status code 200 and json {"success": True, "recipes": recipe} where recipes is the list of recipes
            or appropriate status code indicating reason for failure
    '''
    @app.route('/')
    @app.route('/recipes', methods=['GET'])
    @requires_auth('get:recipes')
    def index(payload):
        data=[]
        recipes = Recipe.query.all()
        for recipe in recipes:
            data.append(recipe.format())
        return {'recipes' : data}

    '''
    @implement endpoint
        GET /reviews/<int:recipe_id>,
            it should require the 'get:reviews' permission available to reader and recipe publisher
            it should contain reviews tied to a given recipes
        returns status code 200 and json {"reviews": reviews} where reviews is the list of reviews
            or appropriate status code indicating reason for failure
    '''
    @app.route('/reviews/<int:recipe_id>', methods=['GET'])
    @requires_auth('get:reviews')
    def retrieve_recipe_reviews(payload, recipe_id):
        reviews = Reviews.query.filter(Reviews.recipe_id == recipe_id)
        data = []
        if reviews.count() == 0:
            return jsonify(data)
        else:
            for r in reviews:
                data.append(r.review)
            return {'reviews' : data}

    '''
    @implement endpoint
        PATCH /recipes/<int:recipe_id>,
            it should require the 'patch-recipes' permission restricted to recipe publisher
            it should contain updated recipe
        returns status code 200 and json {"success": True, "Recipe": updatedRecipe} where recipe is the updated recipe
            or appropriate status code indicating reason for failure
    '''
    @app.route('/recipes/<int:recipe_id>', methods=['PATCH'])
    @requires_auth('patch:recipes')
    def patch_recipe(payload,recipe_id):
        recipe = Recipe.query.filter(Recipe.id == recipe_id).one_or_none()
        body = request.get_json()
        name = body.get('name', None)
        steps = body.get('steps', None)
        ingredients = body.get('ingredients', None)
        image_link = body.get('image_link', None)
        video_link = body.get('video_link', None)
        if (recipe == None or name == None):
            abort(404) 
        try:
            recipe.name = name
            recipe.steps = steps
            recipe.imaimagege_link = image_link
            recipe.video_link = video_link
            recipe.ingredients = ingredients
            recipe.update()
            return {
            'success': True,
            'recipe':recipe.format()
            }
        except:
            abort(422)
    
    '''
    @implement endpoint
        POST /recipes,
            it should require the 'post-recipes' permission restricted to recipe publisher
            it should create a new row in the recipe table
        returns status code 200 and json {"success": True} when recipe is successfully created
            or appropriate status code indicating reason for failure
    '''
    @app.route('/recipes', methods=['POST'])
    @requires_auth('post:recipes')
    def create_recipe(payload):
        body = request.get_json()
        name = body.get('name', None)
        steps = body.get('steps', None)
        ingredients = body.get('ingredients', None)
        image_link = body.get('image_link', None)
        video_link = body.get('video_link', None)
        if (name == None or ingredients == None):
            abort(404) 
        try:

            recipe = Recipe(name=name,ingredients=ingredients, steps=steps, video_link=video_link,image_link=image_link )
            recipe.insert()
            return jsonify({
            'success': True
            })
        except:
            abort(422)

    '''
    @implement endpoint
        POST /recipes/<int:recipe_id>/add_review,
            it should require the 'add-review' permission restricted to recipe reader
            it should create a new row in the reviews table
        returns status code 200 and json {"success": True} when review is successfully created
            or appropriate status code indicating reason for failure
    '''
    @app.route('/recipes/<int:recipe_id>/add_review', methods=['POST'])
    @requires_auth('add:review')
    def create_recipe_review(payload,recipe_id):
        body = request.get_json()
        review = body.get('review', None)
        recipe = Recipe.query.filter(Recipe.id == recipe_id).one_or_none()
        if (review == None or recipe == None):
            abort(404) 
        try:
            review = Reviews(recipe_id = recipe_id, review = review)
            review.insert()
            return jsonify({
            'success': True
            })
        except:
            abort(422)
    '''
    DELETE /recipes/<int:recipe_id>
        where <recipe_id> is the existing model id
        it should respond with a 404 error if <recipe_id> is not found
        it should delete the corresponding row for <recipe_id>
        it should require the 'delete:recipes' permission
    returns status code 200 and json {"success": True} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
    '''
    @app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
    @requires_auth('delete:recipes')
    def delete_recipe(payload,recipe_id):
        recipe = Recipe.query.filter(Recipe.id == recipe_id).one_or_none()
        if recipe == None:
            abort(404)
        try:
            recipe.delete()
            return jsonify({
            'success': True
            })
        except:
            abort(422)

    '''
    @ error handler for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False, 
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    '''
    @ error handler for resource not found
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    '''
    @ error handler for internal server error
    '''
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
            }), 500

    '''
    @ error handler for AuthError
    '''
    @app.errorhandler(AuthError)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run()