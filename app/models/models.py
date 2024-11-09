from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from sqlalchemy import Enum
import enum

db = SQLAlchemy()

class MealCategory(enum.Enum):
    BREAKFAST = "BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"
    SNACK = "SNACK"
    SALAD = "SALAD"
    DESSERT = "DESSERT"

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    in_diet = db.Column(db.Boolean, nullable=False, default=True)
    category = db.Column(Enum(MealCategory), nullable=True)
    calories = db.Column(db.Float, nullable=True)