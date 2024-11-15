from flask import Blueprint, request, jsonify
from app.models.models import db, User
import bcrypt
from flask_login import login_user, current_user, login_required, logout_user

users_bp = Blueprint('users_bp', __name__)

@users_bp.route("/api/users", methods=['POST'])
def create_user():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if email and password:
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "Email already exists"}), 409

        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User successfully registered"})
    
    return jsonify({"message": "Invalid credentials"}), 400

@users_bp.route("/api/users/login", methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if email and password:
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.checkpw(str.encode(password), user.password):
            login_user(user)

            if current_user.is_authenticated:
                return jsonify({"message": "Login successful", "user_id": current_user.id})
            else:
                return jsonify({"message": "Failed to authenticate user"}), 500
    
    return jsonify({"message": "Invalid credentials"}), 400

@users_bp.route("/api/users/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"})