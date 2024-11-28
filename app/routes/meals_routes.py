from flask import Blueprint, request, jsonify
from app.models.models import db, Meal, MealCategory
from datetime import datetime, timedelta
from sqlalchemy import and_, func
from flask_login import login_required, current_user

meals_bp = Blueprint('meals_bp', __name__)

@meals_bp.route('/api/meals/add', methods=['POST'])
@login_required
def add_meal():
    data = request.json

    if 'category' in data and data['category'] not in [e.value for e in MealCategory]:
        return jsonify({"message": "Invalid category"}), 400
    
    if 'name' in data:
        meal = Meal(
            name = data["name"],
            description = data.get("description", None),
            in_diet = data.get("in_diet", True),
            category = data.get("category", None),
            calories = data.get("calories", None),
            user_id=current_user.id
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Meal added successfully"}), 201
    return jsonify({"message": "Invalid meal data"}), 400

@meals_bp.route('/api/meals/update/<int:meal_id>', methods=['PUT'])
@login_required
def update_meal(meal_id):
    meal = Meal.query.filter_by(id=meal_id, user_id=current_user.id).first()
    if not meal:
        return jsonify({"message": "Meal not found"}), 404

    data = request.json

    if 'name' in data:
        meal.name = data['name']
    if 'description' in data:
        meal.description = data['description']
    if 'date_time' in data:
        meal.date_time = data['date_time']
    if 'in_diet' in data:
        meal.in_diet = data['in_diet']
    if 'category' in data:
        if data['category'] not in [e.value for e in MealCategory]:
            return jsonify({"message": "Invalid category"}), 400
        meal.category = MealCategory(data['category'])
    if 'calories' in data:
        meal.calories = data['calories']
    
    db.session.commit()

    return jsonify({"message": "Meal updated successfully"})

@meals_bp.route('/api/meals/delete/<int:meal_id>', methods=['DELETE'])
@login_required
def delete_meal(meal_id):
    meal = Meal.query.filter_by(id=meal_id, user_id=current_user.id).first()

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully"}), 201
    
    return jsonify({"message": "Meal not found"}), 404

@meals_bp.route('/api/meals', methods=['GET'])
@login_required
def get_meals():
    category = request.args.get('category', None)
    in_diet = request.args.get('in_diet', None)
    period = request.args.get('period', None)
    start_date_str = request.args.get('start_date', None)
    end_date_str = request.args.get('end_date', None)

    query = Meal.query.filter_by(user_id=current_user.id)

    if category:
        query = query.filter(Meal.category == MealCategory[category.upper()])

    if in_diet is not None:
        in_diet_bool = in_diet.lower() == 'true'
        query = query.filter(Meal.in_diet == in_diet_bool)

    if period == 'day':
        today = datetime.now().date()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = datetime.combine(today, datetime.max.time())
        query = query.filter(and_(Meal.date_time >= start_of_day, Meal.date_time <= end_of_day))
    
    elif period == 'week':
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        query = query.filter(and_(Meal.date_time >= datetime.combine(start_of_week, datetime.min.time()), 
                                  Meal.date_time <= datetime.combine(end_of_week, datetime.max.time())))
    
    elif period == 'month':
        today = datetime.now().date()
        start_of_month = today.replace(day=1)
        next_month = today.replace(day=28) + timedelta(days=4)
        start_of_next_month = next_month.replace(day=1)
        end_of_month = start_of_next_month - timedelta(seconds=1)
        query = query.filter(and_(Meal.date_time >= datetime.combine(start_of_month, datetime.min.time()), 
                                  Meal.date_time <= datetime.combine(end_of_month, datetime.max.time())))

    if start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            query = query.filter(Meal.date_time >= start_date)
        except ValueError:
            return jsonify({"message": "Invalid start_date format. Use YYYY-MM-DD."}), 400
    
    if end_date_str:
        try:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            query = query.filter(Meal.date_time <= end_date)
        except ValueError:
            return jsonify({"message": "Invalid end_date format. Use YYYY-MM-DD."}), 400

    meals = query.all()
    meal_list = []
    
    for meal in meals:
        meal_data = {
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time,
            "in_diet": meal.in_diet,
            "category": meal.category.value if meal.category else None,
            "calories": meal.calories,
            "favorite": meal.favorite
        }
        meal_list.append(meal_data)

    return jsonify(meal_list)

@meals_bp.route('/api/meals/<int:meal_id>', methods=['GET'])
@login_required
def get_meal(meal_id):
    meal = Meal.query.filter_by(id=meal_id, user_id=current_user.id).first()
 
    if meal:
        return jsonify({
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time,
            "in_diet": meal.in_diet,
            "category": meal.category.value if meal.category else None,
            "calories": meal.calories,
            "favorite": meal.favorite
        })

    return jsonify({"message": "Product not found"}), 404

@meals_bp.route('/api/meals/<int:meal_id>/favorite', methods=['PATCH'])
@login_required
def toggle_favorite(meal_id):
    meal = Meal.query.filter_by(id=meal_id, user_id=current_user.id).first()
    
    if not meal:
        return jsonify({"message": "Meal not found"}), 404
    
    meal.favorite = not meal.favorite
    db.session.commit()
    
    return jsonify({
        "message": "Meal favorite status updated successfully",
        "meal_id": meal.id,
        "favorite": meal.favorite
    })

@meals_bp.route('/api/meals/favorites', methods=['GET'])
@login_required
def get_favorite_meals():
    favorite_meals = Meal.query.filter_by(favorite=True, user_id=current_user.id).all()
    
    if not favorite_meals:
        return jsonify({"message": "No favorite meals found"}), 404
    
    meals_list = [{
        "id": meal.id,
        "name": meal.name,
        "calories": meal.calories,
        "date_time": meal.date_time,
        "in_diet": meal.in_diet
    } for meal in favorite_meals]
    
    return jsonify({"favorite_meals": meals_list})

@meals_bp.route('/api/meals/calorie-goal', methods=['PUT'])
@login_required
def update_calorie_goal():
    data = request.get_json()
    new_goal = data.get('daily_calorie_goal')

    if not new_goal or not isinstance(new_goal, (int, float)) or new_goal <= 0:
        return jsonify({"message": "Invalid calorie goal. It must be a positive number"}), 400

    current_user.daily_calorie_goal = new_goal
    db.session.commit()
 
    return jsonify({"message": f"Daily calorie goal successfully updated to {new_goal}"}), 200

@meals_bp.route('/api/meals/calorie-goal/streak', methods=['GET'])
@login_required
def calorie_streak():
    calorie_goal = current_user.daily_calorie_goal

    daily_meals = db.session.query(
        func.date(Meal.date_time).label('date'),
        func.sum(Meal.calories).label('total_calories')
    ).filter(
        Meal.user_id == current_user.id
    ).group_by(
        func.date(Meal.date_time)
    ).order_by(
        func.date(Meal.date_time).desc()
    ).all()

    streak_count = 0
    previous_day = None

    for meal in daily_meals:
        meal_date = meal.date
        if meal.total_calories >= calorie_goal:
            if previous_day is None or (previous_day - datetime.strptime(meal_date, '%Y-%m-%d').date()).days in [1, 0]:
                streak_count += 1
                previous_day = datetime.strptime(meal_date, '%Y-%m-%d').date()
            else:
                break
        else:
            break

    current_user.calorie_streak_count = streak_count

    if previous_day:
        current_user.last_calorie_streak_date = previous_day
    else:
        current_user.last_calorie_streak_date = None

    db.session.commit()

    return jsonify({
        "streak": streak_count
    })