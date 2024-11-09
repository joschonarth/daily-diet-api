from flask import Blueprint, request, jsonify
from app.models.models import db, Meal, MealCategory

meal_bp = Blueprint('meal_bp', __name__)

@meal_bp.route('/api/meal/add', methods=['POST'])
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


@meal_bp.route('/api/meal/update/<int:meal_id>', methods=['PUT'])
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

@meal_bp.route('/api/meal/delete/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully"}), 201
    
    return jsonify({"message": "Meal not found"}), 404

@meal_bp.route('/api/meals', methods=['GET'])
def get_meals():
    category = request.args.get('category', None)
    in_diet = request.args.get('in_diet', None)

    query = Meal.query

    if category:
        query = query.filter(Meal.category == MealCategory[category.upper()])

    if in_diet is not None:
        in_diet_bool = in_diet.lower() == 'true'
        query = query.filter(Meal.in_diet == in_diet_bool)

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

@meal_bp.route('/api/meals/<int:meal_id>', methods=['GET'])
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

@meal_bp.route('/api/meals/<int:meal_id>/favorite', methods=['PATCH'])
def toggle_favorite(meal_id):
    meal = Meal.query.get(meal_id)
    
    if not meal:
        return jsonify({"message": "Meal not found."}), 404
    
    meal.favorite = not meal.favorite
    db.session.commit()
    
    return jsonify({
        "message": "Meal favorite status updated successfully.",
        "meal_id": meal.id,
        "favorite": meal.favorite
    })