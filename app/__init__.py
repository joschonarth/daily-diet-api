from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from app.models.models import db, User
from app.config import Config

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    login_manager.init_app(app)
    login_manager.login_view = 'users_bp.login'

    register_blueprints(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def register_blueprints(app):
    from app.routes.meals_routes import meals_bp
    app.register_blueprint(meals_bp)

    from app.routes.meals_report_routes import meals_report_bp
    app.register_blueprint(meals_report_bp)

    from app.routes.water_routes import water_bp
    app.register_blueprint(water_bp)

    from app.routes.users_routes import users_bp
    app.register_blueprint(users_bp)
