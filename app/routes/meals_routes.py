from flask import Blueprint, request, jsonify
from app.models.models import db, Meal, MealCategory
from datetime import datetime, timedelta
from sqlalchemy import and_

meals_bp = Blueprint('meals_bp', __name__)

@meals_bp.route('/api/meals/add', methods=['POST'])
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
            calories = data.get("calories", None)
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Meal added successfully"}), 201
    return jsonify({"message": "Invalid meal data"}), 400

@meals_bp.route('/api/meals/update/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = Meal.query.get(meal_id)
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
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully"}), 201
    
    return jsonify({"message": "Meal not found"}), 404

@meals_bp.route('/api/meals', methods=['GET'])
def get_meals():
    category = request.args.get('category', None)
    in_diet = request.args.get('in_diet', None)
    date_filter = request.args.get('period', None)
    start_date_str = request.args.get('start_date', None)
    end_date_str = request.args.get('end_date', None)

    query = Meal.query

    if category:
        query = query.filter(Meal.category == MealCategory[category.upper()])

    if in_diet is not None:
        in_diet_bool = in_diet.lower() == 'true'
        query = query.filter(Meal.in_diet == in_diet_bool)

    if date_filter == 'day':
        today = datetime.now().date()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = datetime.combine(today, datetime.max.time())
        query = query.filter(and_(Meal.date_time >= start_of_day, Meal.date_time <= end_of_day))
    
    elif date_filter == 'week':
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        query = query.filter(and_(Meal.date_time >= datetime.combine(start_of_week, datetime.min.time()), 
                                  Meal.date_time <= datetime.combine(end_of_week, datetime.max.time())))
    
    elif date_filter == 'month':
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
def get_meal(meal_id):
    meal = Meal.query.get(meal_id)
    
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
def toggle_favorite(meal_id):
    meal = Meal.query.get(meal_id)
    
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
def get_favorite_meals():
    favorite_meals = Meal.query.filter_by(favorite=True).all()
    
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