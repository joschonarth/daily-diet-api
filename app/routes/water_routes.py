from flask import Blueprint, request, jsonify
from app.models.models import db, Water
from datetime import datetime

water_bp = Blueprint('water_bp', __name__)

@water_bp.route('/api/water/add', methods=['POST'])
def add_water_intake():
    data = request.json

    if 'quantity' not in data or data['quantity'] <= 0:
        return jsonify({"message": "Invalid quantity"}), 400

    water_intake = Water(
        quantity=data['quantity']
    )
    
    db.session.add(water_intake)
    db.session.commit()
    
    return jsonify({
        "message": "Water intake recorded successfully",
        "quantity": water_intake.quantity,
        "date_time": water_intake.date_time.strftime('%Y-%m-%d %H:%M:%S')
    }), 201