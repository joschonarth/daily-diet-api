from flask import request, jsonify
from app.models.models import db, Water
from datetime import datetime, timedelta
from calendar import monthrange
from flask_login import current_user
from sqlalchemy import func

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

def add_water_intake(data):
    data = request.json

    if 'quantity' not in data or data['quantity'] <= 0:
        return jsonify({"message": "Invalid quantity"}), 400

    water_intake = Water(
        quantity=data['quantity'],
        user_id=current_user.id
    )
    
    db.session.add(water_intake)
    db.session.commit()

    calculate_water_streak(current_user)
    
    return jsonify({
        "message": "Water intake recorded successfully",
        "id": water_intake.id,
        "quantity": water_intake.quantity,
        "date_time": water_intake.date_time.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

def remove_water_intake(water_id):
    water_intake = Water.query.filter_by(id=water_id, user_id=current_user.id).first()
    if not water_intake:
        return jsonify({"message": "Water intake not found"}), 404

    db.session.delete(water_intake)
    db.session.commit()

    return jsonify({"message": "Water intake removed successfully"}), 200

def get_water_intake(query_params):
    period = query_params.get('period', 'day')

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

def get_total_water_intake(query_params):
    period = query_params.get('period', 'day')
    
    try:
        start_date, end_date = get_date_range(period)
    except ValueError:
        return jsonify({"message": "Invalid period"}), 400

    total_water = db.session.query(db.func.sum(Water.quantity)).filter(
        Water.user_id == current_user.id,
        Water.date_time >= start_date,
        Water.date_time <= end_date
    ).scalar() or 0

    water_goal = current_user.daily_water_goal

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

def update_water_goal():
    data = request.get_json()
    new_goal = data.get('daily_water_goal')

    if not new_goal or not isinstance(new_goal, (int, float)) or new_goal <= 0:
        return jsonify({"message": "Invalid water intake goal"}), 400

    current_user.daily_water_goal = new_goal
    db.session.commit()

    return jsonify({"message": f"Daily water intake goal successfully updated to {new_goal}"}), 200

def calculate_water_streak(user):
    water_goal = user.daily_water_goal

    daily_intakes = db.session.query(
        func.date(Water.date_time).label('date'),
        func.sum(Water.quantity).label('total_quantity')
    ).filter(
        Water.user_id == user.id
    ).group_by(
        func.date(Water.date_time)
    ).order_by(
        func.date(Water.date_time).desc()
    ).all()

    streak_count = 0
    previous_day = None

    for intake in daily_intakes:
        intake_date = intake.date
        if intake.total_quantity >= water_goal:
            if previous_day is None or (previous_day - datetime.strptime(intake_date, '%Y-%m-%d').date()).days in [1, 0]:
                streak_count += 1
                previous_day = datetime.strptime(intake_date, '%Y-%m-%d').date()
            else:
                break
        else:
            break

    user.water_streak_count = streak_count
    
    if previous_day:
        user.last_water_streak_date = previous_day
    else:
        user.last_water_streak_date = None

    db.session.commit()
    return streak_count

def water_streak():
    streak_count = calculate_water_streak(current_user)
    return jsonify({"streak": streak_count})