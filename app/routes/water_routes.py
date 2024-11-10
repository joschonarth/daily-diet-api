from flask import Blueprint, request, jsonify
from app.models.models import db, Water
from datetime import datetime, timedelta
from calendar import monthrange

water_bp = Blueprint('water_bp', __name__)

def get_date_range(period):
    today = datetime.now()

    if period == 'day':
        start_date = datetime.combine(today.date(), datetime.min.time())
        end_date = datetime.combine(today.date(), datetime.max.time())
    elif period == 'week':
        start_of_week = today - timedelta(days=today.weekday() + 1)
        start_date = datetime.combine(start_of_week.date(), datetime.min.time())
        end_of_week = start_of_week + timedelta(days=6)
        end_date = datetime.combine(end_of_week.date(), datetime.max.time())
    elif period == 'month':
        start_date = datetime.combine(today.replace(day=1).date(), datetime.min.time())
        last_day = monthrange(today.year, today.month)[1]
        end_date = datetime.combine(today.replace(day=last_day).date(), datetime.max.time())
    else:
        return jsonify({"message": "Invalid period"}), 400

    return start_date, end_date

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

@water_bp.route('/api/water', methods=['GET'])
def get_water_intake():
    period = request.args.get('period', 'day')

    try:
        start_date, end_date = get_date_range(period)
    except ValueError:
        return jsonify({"message": "Invalid period"}), 400

    water_intakes = Water.query.filter(Water.date_time >= start_date, Water.date_time <= end_date).all()

    history = [{"id": intake.id, "quantity": intake.quantity, "date_time": intake.date_time.strftime('%Y-%m-%d %H:%M:%S')} for intake in water_intakes]

    return jsonify(history)