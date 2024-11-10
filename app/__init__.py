from flask import Flask
from flask_cors import CORS
from app.models.models import db
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
    from app.routes.meals_routes import meals_bp
    app.register_blueprint(meals_bp)

    from app.routes.meals_report_routes import meals_report_bp
    app.register_blueprint(meals_report_bp)

    from app.routes.water_routes import water_bp
    app.register_blueprint(water_bp)
