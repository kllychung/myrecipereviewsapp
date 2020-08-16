# Myrecipes API Backend
This project contains  code written for myRecipes api which contain several endpoints which 

1. Allow recipe publishers to create, edit and remove recipes
2. Allow recipe readers to view published recipes from publishers and write recipe reviews
3. Publishers can also read reviews about their readers

# App Hosting
App is hosted at https://myrecipereviewsapp.herokuapp.com

# Authentication
Two roles have been created:
1. Reader
2. Publishers

Each role has been set with different permission:

Publisher 
"permissions": [
    "delete:recipes",
    "get:recipes",
    "get:reviews",
    "patch:recipes",
    "post:recipes"
  ]

Reader 
  "permissions": [
    "add:review",
    "get:recipes",
    "get:reviews"
  ]

Temporary Tokens:

Reader jwt(time sensitive): 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldCR2ozZHoxYW1naFR1Y2lURFlFQSJ9.eyJpc3MiOiJodHRwczovL215cmVjaXBlcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmZlMWI4ZjE4YWEwMDY4OWQ3NzcyIiwiYXVkIjoibXlyZWNpcGVzIiwiaWF0IjoxNTk3NTM4ODI4LCJleHAiOjE1OTc2MjUyMjgsImF6cCI6ImhnazdSVnIxUUw4OUYyVEtFSFRkTjVFWXAySks0M2xvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6cmV2aWV3IiwiZ2V0OnJlY2lwZXMiLCJnZXQ6cmV2aWV3cyJdfQ.C-sSAxaGBlSst1D-VWVfydLvRgxiyjgx3BCqqgMMqGgsRR4rRCIAHpxeZMSp2v0G4OPdeU6OHR5gqjR2iUKAv5VJV5eemXtdWiYeWseuUAsdvdB3GxKWK3IBQqNA3SCR66uYrXRyqoK-xzTnIwhxLcmjqL76MILsXEXFWBpc7Ypzp5JGQnP9Bb7TMN5P2RtHZ0GO_3HpFOcdsGsVtbUwErRIGViNaFz_5g5ZeW633CaVEoAhWK-0IkWtvK2Q_dI1HGtkc040dIGqWa3arhDpvLd1gQGLQ7T3TMkEa7rV88NAmmtxIsvoaseLFKTKT8CvB5tkJ4VNHlMXFi8lVzGQig

Publisher jwt(time sensitive): 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldCR2ozZHoxYW1naFR1Y2lURFlFQSJ9.eyJpc3MiOiJodHRwczovL215cmVjaXBlcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNzA0ODIzOGQxYTIwMDZkMjEyZWVhIiwiYXVkIjoibXlyZWNpcGVzIiwiaWF0IjoxNTk3NTMwNDM2LCJleHAiOjE1OTc2MTY4MzYsImF6cCI6ImhnazdSVnIxUUw4OUYyVEtFSFRkTjVFWXAySks0M2xvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cmVjaXBlcyIsImdldDpyZWNpcGVzIiwiZ2V0OnJldmlld3MiLCJwYXRjaDpyZWNpcGVzIiwicG9zdDpyZWNpcGVzIl19.ee582u-YGQQvwRkT3XK_H87LKAxGw-WelAxZI96AnUrPc0yWcOFNgMVLEBF-6Dex0WpvlrCLnfrHAai99CL-CZIQPgbdgi1PmHgGq33qJ8b6RrxLAh4CW3FnjIcu-wByA-K-CVB1LdleGK9XsNRmGsPXr43eiuaSjFub7L4BXuosjTFAKvwLf7QL79474pAX6TEsAvTX2UC7s42ut9uOXwVFAFmM6v3H2ilNxp-ZJHNPMZmIxmayzHjh33qUJtD3eAKV5NC51iGkehgzyn4IMOBqM2AuI-yLVYl1NyzDE41UHSf_-xeb-WriwJP8HiSACEE4VeqSwoa5Ncj3BM79Kg

## Getting Started

### Installing Dependencies

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 


## Database Setup
To run postgres in local environment, terminal run:
```bash
set DATABASE_URL = 'postgresql://postgres@localhost:5432/recipereviews'
```

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server

From within the first ensure you are working using your created virtual environment.

To run the server locally, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

## Running tests
Test your endpoints with [Postman](https://getpostman.com). 
    - Import the postman collection `MyRecipesTestCollection.postman_collection.json`
    - There are 2 folders, one for a publisher role and the other one for reader role containing tests for each role
    - The jwt token is already set for each folder at the authorization level

