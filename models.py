
import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from sqlalchemy.ext.declarative import as_declarative
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "recipe_reviews"
database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.environ['DATABASE_URL']


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app) 
    # migrate = Migrate(app,db)
    db.create_all()
    
'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
#def db_drop_and_create_all():
#    db.drop_all()

'''
Recipe
a persistent recipe entity, extends the base SQLAlchemy Model
'''

class Recipe(db.Model):
    __tablename__ = 'recipe'
    # Autoincrementing, unique primary key
    id = Column(db.Integer,primary_key=True)
    # String Title
    name = Column(String(80), unique=True, nullable=False)

    steps =  Column(db.ARRAY(db.String(240)))

    ingredients =  Column(db.ARRAY(db.String(240)))

    image_link = db.Column(db.String(500))

    video_link = db.Column(db.String(500))

    reviews = db.relationship('Reviews', backref=db.backref('reviews', lazy=True), cascade="all, delete")

    '''
    format()
        short form representation of the recipe model
    '''
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'image_link' : self.image_link,
            'video_link' : self.video_link
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

'''
Reviews
a persistent reviews entity, extends the base SQLAlchemy Model
'''
class Reviews(db.Model):
    # Autoincrementing, unique primary key
    __tablename__ = 'reviews'

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable = False)

    review =  db.Column(String(180), nullable=False)

    def __init__(self, recipe_id, review):
        self.recipe_id = recipe_id
        self.review = review

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

