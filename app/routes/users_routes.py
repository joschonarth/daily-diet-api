from flask import Blueprint, request, jsonify
from app.models.models import db, User
import bcrypt

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