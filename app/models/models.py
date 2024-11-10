from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, func
import enum

db = SQLAlchemy()

class MealCategory(enum.Enum):
    BREAKFAST = "BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"
    SNACK = "SNACK"
    SALAD = "SALAD"
    DESSERT = "DESSERT"

class Goals():
    DAILY_CALORIE_GOAL = 2000
    DAILY_WATER_GOAL = 2000

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=func.now())
    in_diet = db.Column(db.Boolean, nullable=False, default=True)
    category = db.Column(Enum(MealCategory), nullable=True)
    calories = db.Column(db.Float, nullable=True)
    favorite = db.Column(db.Boolean, default=False)

class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=func.now())