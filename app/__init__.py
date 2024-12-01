from flask import Flask, jsonify
from flask_cors import CORS
from flask_login import LoginManager
from app.models.models import db, User
from app.config import Config
import os
import uuid

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SECRET_KEY'] = "secret_key"

    db.init_app(app)
    CORS(app)

    login_manager.init_app(app)
    login_manager.login_view = 'users_bp.login'

    with app.app_context():
        if not os.path.exists('daily_diet.db'):
            db.create_all()

    register_blueprints(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(uuid.UUID(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"message": "You need to be logged in to access this route"}), 401

def register_blueprints(app):
    from app.routes.meals_routes import meals_bp
    app.register_blueprint(meals_bp)

    from app.routes.water_routes import water_bp
    app.register_blueprint(water_bp)

    from app.routes.users_routes import users_bp
    app.register_blueprint(users_bp)