from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from app.models.models import Meal, Goals
from calendar import monthrange

meals_report_bp = Blueprint('meals_report', __name__)

@meals_report_bp.route('/api/meals/report', methods=['GET'])
def generate_report():      
    today  = datetime.now()
    
    period = request.args.get('period', 'week').lower()

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
        return jsonify({"message": "Invalid range parameter"}), 400
    
    end_date = datetime.combine(end_date.date(), datetime.max.time())

    meals = Meal.query.filter(Meal.date_time >= start_date, Meal.date_time <= end_date).all()
    
    if not meals:
        return jsonify({"message": "No meals found in the selected date range"}), 404

    meals_in_diet = sum(1 for meal in meals if meal.in_diet)
    meals_out_of_diet = len(meals) - meals_in_diet
    
    total_calories = sum(meal.calories for meal in meals)
    
    calorie_goal = Goals.DAILY_CALORIE_GOAL
    
    if calorie_goal is None or calorie_goal == 0:
        return jsonify({"message": "Calorie goal is not set or is invalid"}), 400
    
    if period == 'week':
        calorie_goal *= 7
    elif period == 'month':
        calorie_goal *= last_day

    progress = (total_calories / calorie_goal) * 100
    
    report = {
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "meals_in_diet": meals_in_diet,
        "meals_out_of_diet": meals_out_of_diet,
        "total_calories": total_calories,
        "calorie_goal": calorie_goal,
        "progress": round(progress, 2)
    }

    return jsonify(report)

@meals_report_bp.route('/api/meals/report/goal', methods=['PUT'])
def update_calorie_goal():
    data = request.get_json()
    new_goal = data.get('daily_calorie_goal')

    if not new_goal or not isinstance(new_goal, (int, float)) or new_goal <= 0:
        return jsonify({"message": "Invalid calorie goal. It must be a positive number"}), 400

    Goals.DAILY_CALORIE_GOAL = new_goal
 
    return jsonify({"message": f"Daily calorie goal successfully updated to {new_goal}"}), 200