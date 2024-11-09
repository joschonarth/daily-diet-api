from flask import Blueprint, jsonify, current_app, request
from datetime import datetime, timedelta
from app.models.models import Meal

report_bp = Blueprint('report', __name__)

@report_bp.route('/api/report', methods=['GET'])
def generate_report():      
    end_date = datetime.now()
    
    start_date = end_date - timedelta(weeks=1)

    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    meals = Meal.query.filter(Meal.date_time >= start_date, Meal.date_time <= end_date).all()
    
    if not meals:
        return jsonify({"message": "No meals found in the selected date range"}), 404

    meals_in_diet = sum(1 for meal in meals if meal.in_diet)
    meals_out_of_diet = len(meals) - meals_in_diet
    
    total_calories = sum(meal.calories for meal in meals)
    
    calorie_goal = current_app.config['CALORIE_GOAL']
    
    if calorie_goal is None or calorie_goal == 0:
        return jsonify({"message": "Calorie goal is not set or is invalid"}), 400
    
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

@report_bp.route('/api/report/goal', methods=['PUT'])
def update_calorie_goal():
    data = request.get_json()
    new_goal = data.get('calorie_goal')

    if not new_goal or not isinstance(new_goal, (int, float)) or new_goal <= 0:
        return jsonify({"message": "Invalid calorie goal. It must be a positive number"}), 400

    current_app.config['CALORIE_GOAL'] = new_goal
 
    return jsonify({"message": f"Calorie goal successfully updated to {new_goal}"}), 200