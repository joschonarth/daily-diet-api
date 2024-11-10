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
    from app.routes.meal_routes import meal_bp
    app.register_blueprint(meal_bp)

    from app.routes.report_routes import report_bp
    app.register_blueprint(report_bp)

    from app.routes.water_routes import water_bp
    app.register_blueprint(water_bp)
