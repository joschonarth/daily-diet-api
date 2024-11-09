from flask import Blueprint, request, jsonify, current_app
from datetime import datetime, timedelta
from app.models.models import Meal

report_bp = Blueprint('report', __name__)

@report_bp.route('/api/report', methods=['GET'])
def generate_report():
    report_type = request.args.get('report_type', 'weekly').lower()
    
    if report_type not in ['weekly', 'monthly']:
        return jsonify({"message": "Invalid report type. Use 'weekly' or 'monthly'."}), 400
  
    end_date = datetime.now()
    
    if report_type == 'weekly':
        start_date = end_date - timedelta(weeks=1)
    elif report_type == 'monthly':
        start_date = datetime(end_date.year, end_date.month, 1) - timedelta(days=1)
        start_date = datetime(start_date.year, start_date.month, 1)
    
    meals = Meal.query.filter(Meal.date_time >= start_date, Meal.date_time <= end_date).all()
    
    if not meals:
        return jsonify({"message": "No meals found in the selected date range."}), 404

    meals_in_diet = sum(1 for meal in meals if meal.in_diet)
    meals_out_of_diet = len(meals) - meals_in_diet
    
    total_calories = sum(meal.calories for meal in meals)
    
    calorie_goal = current_app.config['CALORIE_GOAL']
    
    if calorie_goal is None or calorie_goal == 0:
        return jsonify({"message": "Calorie goal is not set or is invalid."}), 400
    
    progress = (total_calories / calorie_goal) * 100
    
    report = {
        "report_type": report_type,
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "meals_in_diet": meals_in_diet,
        "meals_out_of_diet": meals_out_of_diet,
        "total_calories": total_calories,
        "calorie_goal": calorie_goal,
        "progress": round(progress, 2)
    }

    return jsonify(report)
