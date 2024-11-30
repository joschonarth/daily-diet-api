from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, func, ForeignKey
from sqlalchemy.orm import relationship
import enum
from flask_login import UserMixin
import uuid
from sqlalchemy.dialects.postgresql import UUID


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

class User(db.Model, UserMixin):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    meals = relationship('Meal', backref='user', cascade="all, delete")
    water_intakes = relationship('Water', backref='user', cascade="all, delete")
    daily_calorie_goal = db.Column(db.Float, nullable=False, default=Goals.DAILY_CALORIE_GOAL)
    daily_water_goal = db.Column(db.Float, nullable=False, default=Goals.DAILY_WATER_GOAL)

    calorie_streak_count = db.Column(db.Integer, nullable=False, default=0)
    last_calorie_streak_date = db.Column(db.Date, nullable=True)

    water_streak_count = db.Column(db.Integer, nullable=False, default=0)
    last_water_streak_date = db.Column(db.Date, nullable=True)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=func.now())
    in_diet = db.Column(db.Boolean, nullable=False, default=True)
    category = db.Column(Enum(MealCategory), nullable=True)
    calories = db.Column(db.Float, nullable=True)
    favorite = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=func.now())
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)