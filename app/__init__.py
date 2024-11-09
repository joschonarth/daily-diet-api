from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.models.models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily_diet.db'
    db.init_app(app)

    from app.routes.meal_routes import meal_bp
    app.register_blueprint(meal_bp)

    CORS(app)
    return app