from flask import Blueprint, request, jsonify
from app.models.models import db, Water
from datetime import datetime, timedelta
from calendar import monthrange
from app.models.models import Goals
from flask_login import login_required, current_user

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
@login_required
def add_water_intake():
    data = request.json

    if 'quantity' not in data or data['quantity'] <= 0:
        return jsonify({"message": "Invalid quantity"}), 400

    water_intake = Water(
        quantity=data['quantity'],
        user_id=current_user.id
    )
    
    db.session.add(water_intake)
    db.session.commit()
    
    return jsonify({
        "message": "Water intake recorded successfully",
        "quantity": water_intake.quantity,
        "date_time": water_intake.date_time.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@water_bp.route('/api/water/delete/<int:id>', methods=['DELETE'])
@login_required
def remove_water_intake(id):
    water_intake = Water.query.filter_by(id=id, user_id=current_user.id).first()
    if not water_intake:
        return jsonify({"message": "Water intake not found"}), 404

    db.session.delete(water_intake)
    db.session.commit()

    return jsonify({"message": "Water intake removed successfully"}), 200

@water_bp.route('/api/water', methods=['GET'])
@login_required
def get_water_intake():
    period = request.args.get('period', 'day')

    try:
        start_date, end_date = get_date_range(period)
    except ValueError:
        return jsonify({"message": "Invalid period"}), 400

    water_intakes = Water.query.filter(
        Water.user_id == current_user.id,
        Water.date_time >= start_date,
        Water.date_time <= end_date
    ).all()

    history = [{"id": intake.id, "quantity": intake.quantity, "date_time": intake.date_time.strftime('%Y-%m-%d %H:%M:%S')} for intake in water_intakes]

    return jsonify(history)

@water_bp.route('/api/water/total', methods=['GET'])
@login_required
def get_total_water_intake():
    period = request.args.get('period', 'day')
    
    try:
        start_date, end_date = get_date_range(period)
    except ValueError:
        return jsonify({"message": "Invalid period"}), 400

    total_water = db.session.query(db.func.sum(Water.quantity)).filter(
        Water.user_id == current_user.id,
        Water.date_time >= start_date,
        Water.date_time <= end_date
    ).scalar() or 0

    water_goal = Goals.DAILY_WATER_GOAL

    if period == 'week':
        water_goal *= 7
    elif period == 'month':
        days_in_month = monthrange(end_date.year, end_date.month)[1]
        water_goal *= days_in_month

    progress = (total_water / water_goal) * 100

    return jsonify({
        "period": period,
        "total_water": total_water if total_water else 0,
        "water_goal": water_goal,
        "progress": round(progress, 2)
    })

@water_bp.route('/api/water/goal', methods=['PUT'])
@login_required
def update_water_goal():
    data = request.get_json()
    new_goal = data.get('daily_water_goal')

    if not new_goal or not isinstance(new_goal, (int, float)) or new_goal <= 0:
        return jsonify({"message": "Invalid calorie goal"}), 400

    Goals.DAILY_WATER_GOAL = new_goal

    return jsonify({"message": f"Daily calorie goal successfully updated to {new_goal}"}), 200