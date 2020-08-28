import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Recipe, Reviews, setup_db

publisher_token = 'Bearer ' + os.environ.get('PUBLISHER_TOKEN')
reader_token = 'Bearer ' + os.environ.get('READER_TOKEN')
publisher_headers = {'content-type': 'application/json', 'Authorization': publisher_token}
reader_headers = {'content-type': 'application/json', 'Authorization': reader_token}

class MyRecipesTestCase(unittest.TestCase):
    """This class represents MyRecipes test case"""

    unittest.TestLoader.sortTestMethodsUsing = None

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "myrecipes_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def test_add_recipe(self):
        test_data = {
            "name": "Lemon wih Chicken",
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
            "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps" : ["1. Marinate chicken with salt, lemon and pepper", "2. Bake chicken for 20 mins"]   
        }
        res = self.client().post('/recipes',headers=publisher_headers ,json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_fail_add_recipe(self):
        test_data = {
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
            "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps" : ["1. Marinate chicken with salt, lemon and pepper", "2. Bake chicken for 20 mins"]   
        }
        res = self.client().post('/recipes',headers=publisher_headers ,json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'Not found')

    def test_get_recipe(self):
        res = self.client().get('/recipes',headers=publisher_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(data['recipes']), 0)
    
    def test_patch_recipe(self):
        recipe = Recipe.query.filter(Recipe.name == 'Lemon wih Chicken').one_or_none()
        test_data = {
            "name": "Lemon Chicken 4",
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
	        "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps": ["Sous vide chicken"]
        }
        path = "/recipes/" + str(recipe.id)
        if path != None:
            res = self.client().patch(path,headers=publisher_headers, json=test_data)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)

    def test_404_patch_recipe(self):
        test_data = {
            "name": "Lemon Chicken 4",
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
	        "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps": ["Sous vide chicken"]
        }
        res = self.client().patch('/recipes/1000',headers=publisher_headers, json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_add_recipe_for_review_test(self):
        test_data = {
            "name": "Dill wih Chicken",
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
            "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps" : ["1. Marinate chicken with salt, lemon and pepper", "2. Bake chicken for 20 mins"]   
        }
        res = self.client().post('/recipes',headers=publisher_headers ,json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)    

    def test_add_recipe_review(self):
        test_data = {"review": "amazing recipe"}
        recipe = Recipe.query.filter(Recipe.name.like("Dill%")).first()
        path = "/recipes/" + str(recipe.id) + "/reviews"
        res = self.client().post(path,headers=reader_headers, json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_404_add_recipe_review(self):
        test_data = {"reviewsss": "amazing recipe"}
        recipe = Recipe.query.filter(Recipe.name.like("Lemon%")).first()
        path = "/recipes/" + str(recipe.id) + "/reviews"
        res = self.client().post(path,headers=reader_headers, json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_get_recipe_reviews(self):
        recipe = Recipe.query.filter(Recipe.name.like("Dill%")).first()
        path = "/reviews/" + str(recipe.id)
        res = self.client().get(path,headers=reader_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(data['reviews']), 0)

    def test_emptyResponse_get_recipe_reviews(self):
        path = "/reviews/" + str(10000)
        res = self.client().get(path,headers=reader_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['reviews'], [])

    def test_remove_404_recipe(self):
        path = "/recipes/" + str(1000)
        res = self.client().delete(path,headers=publisher_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_remove_recipe(self):
        recipe = Recipe.query.filter(Recipe.name.like("Lemon%")).first()
        path = "/recipes/" + str(recipe.id)
        res = self.client().delete(path,headers=publisher_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ################## ROLE BASED TESTS ########################
    def test_unauthorized_401_get_recipe_with_no_token(self):
        res = self.client().get('/recipes')
        self.assertEqual(res.status_code, 401)

    # Get 401 when reader attempts to remove recipe
    def test_unauthorized_401_remove_recipe(self):
        recipe = Recipe.query.filter(Recipe.name.like("Dill%")).first()
        path = "/recipes/" + str(recipe.id)
        res = self.client().delete(path,headers=reader_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    # Get 401 when reader attempts to patch recipe
    def test_unauthorized_401_patch_recipe(self):
        recipe = Recipe.query.filter(Recipe.name.like("Dill%")).first()
        test_data = {
            "name": "Dill Chicken 4",
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
	        "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps": ["Sous vide chicken"]
        }
        path = "/recipes/" + str(recipe.id)
        res = self.client().patch(path,headers=reader_headers, json=test_data)
        self.assertEqual(res.status_code, 401)

    # Get 401 when reader attempts to add recipe
    def test_unauthorized_401_fail_add_recipe(self):
        test_data = {
            "name": "Garlic Chicken 4",
            "ingredients": [ "1 lb chicken", "3 lemons", "1 pinch salt", "1 pinch pepper"],
            "imagelink": "https://natashaskitchen.com/wp-content/uploads/2020/02/Lemon-Chicken-3-728x1092.jpg",
            "videolink": "https://youtu.be/mIE2QXup-pk",
            "steps" : ["1. Marinate chicken with salt, lemon and pepper", "2. Bake chicken for 20 mins"]   
        }
        res = self.client().post('/recipes',headers=reader_headers ,json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)


    def test_unauthorized_401_add_recipe_review(self):
        test_data = {"review": "bad recipe"}
        recipe = Recipe.query.filter(Recipe.name.like("Dill%")).first()
        path = "/recipes/" + str(recipe.id) + "/reviews"
        res = self.client().post(path,headers=publisher_headers, json=test_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def tearDown(self):
        """Executed after reach test"""
        pass

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
