from flask import Blueprint, request, jsonify
from flask_login import login_required, logout_user
from app.views.users.users_views import create_user, login

users_bp = Blueprint('users_bp', __name__)

@users_bp.route("/api/users", methods=['POST'])
def create_user_route():
    return create_user(request.json)

@users_bp.route("/api/users/login", methods=['POST'])
def login_route():
    return login(request.json)

@users_bp.route("/api/users/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"})