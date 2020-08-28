# Project Motivation
Build an api using Auth0 Role Base Access Control in python

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

PUBLISHER_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldCR2ozZHoxYW1naFR1Y2lURFlFQSJ9.eyJpc3MiOiJodHRwczovL215cmVjaXBlcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNzA0ODIzOGQxYTIwMDZkMjEyZWVhIiwiYXVkIjoibXlyZWNpcGVzIiwiaWF0IjoxNTk4NjM3NTIwLCJleHAiOjE1OTg3MjM5MjAsImF6cCI6ImhnazdSVnIxUUw4OUYyVEtFSFRkTjVFWXAySks0M2xvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cmVjaXBlcyIsImdldDpyZWNpcGVzIiwiZ2V0OnJldmlld3MiLCJwYXRjaDpyZWNpcGVzIiwicG9zdDpyZWNpcGVzIl19.F45Sb9vHgY_ZQrQMVu3nwMnhnE2jdJ8MtwOWdd9TsiG4fuVeVZftdHVGB6f9tyCnnO7B6kUQs2LIfn3upKpgySNR0VgELIh4rp1tfYTI2me5ROILOJFP5YpQT97D0AFA15ASQ7UDLsdLU74QknUUb2zEKzBSaSyNLKkokwIuYyCcQU98dQPq_duND7HFT1P_ROt7aocBrZxqxeO4R8y9W_gqYdqXrcUsgnoMCTB16ns81KGpm5SjTyrnovN_RMTJSPs7vgydNGWYYJZIq1URsj--GTgITeoyGUwWdHNP-nbwz4jFC0cCBdpHlLjHEbeIHmoTlxG7DnxNczwBlz7ifw


READER_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldCR2ozZHoxYW1naFR1Y2lURFlFQSJ9.eyJpc3MiOiJodHRwczovL215cmVjaXBlcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmZlMWI4ZjE4YWEwMDY4OWQ3NzcyIiwiYXVkIjoibXlyZWNpcGVzIiwiaWF0IjoxNTk4NjM3NjcwLCJleHAiOjE1OTg3MjQwNzAsImF6cCI6ImhnazdSVnIxUUw4OUYyVEtFSFRkTjVFWXAySks0M2xvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6cmV2aWV3IiwiZ2V0OnJlY2lwZXMiLCJnZXQ6cmV2aWV3cyJdfQ.dmUt1hMeteUrMD92N0neLktVxt579sFumgo5PEOjel1D7t1dKmZL-6jelJxxthtNlqaRFvMAoKfPFL6068DkMRT5y1AoSDFOFDPdcpFnsdxHdSsB1YMnf_eC4gKM2RslqnadFIfydRxHwjWKbXsP-D6sHdm5RyAn83UBbJoIgvanEIKrjMpq6IOaGTJu8EOJ_mMbpBPe_4_to1Avt7h51YIgL4rqEbijKPjnr0S1Gk_sNEWuL2CYpLwnEYvQJv0QlhGpPgoLdSP-IwbJowTni1pXblkgY_aLLW3TTabZ8xPzlMB_ERWnrFL_mwbaZa6W7g71H1ee2kfgKiUTXtjhIw

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

1. To run the api tests, run

```
dropdb myrecipes_test
createdb myrecipes_test
python test_app.py
```
## Api doumentation
See apidoc.txt