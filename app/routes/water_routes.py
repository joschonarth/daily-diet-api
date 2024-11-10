from flask import Blueprint, request, jsonify
from app.models.models import db, Water

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

@water_bp.route('/api/water/delete/<int:id>', methods=['DELETE'])
def remove_water_intake(id):
    water_intake = Water.query.get(id)
    if not water_intake:
        return jsonify({"message": "Water intake not found"}), 404

    db.session.delete(water_intake)
    db.session.commit()

    return jsonify({"message": "Water intake removed successfully"}), 200