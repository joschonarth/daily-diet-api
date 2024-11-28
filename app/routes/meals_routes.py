from flask import Blueprint, request
from flask_login import login_required
from app.views.meals.meals_views import add_meal, update_meal, delete_meal, get_meals, get_meal, toggle_favorite, get_favorite_meals, update_calorie_goal, calorie_streak

meals_bp = Blueprint('meals_bp', __name__)

@meals_bp.route('/api/meals/add', methods=['POST'])
@login_required
def add_meal_route():
    return add_meal(request.json)

@meals_bp.route('/api/meals/update/<int:meal_id>', methods=['PUT'])
@login_required
def update_meal_route(meal_id):
    return update_meal(meal_id, request.json)

@meals_bp.route('/api/meals/delete/<int:meal_id>', methods=['DELETE'])
@login_required
def delete_meal_route(meal_id):
    return delete_meal(meal_id) 

@meals_bp.route('/api/meals', methods=['GET'])
@login_required
def get_meals_route():
    return get_meals(request.args)

@meals_bp.route('/api/meals/<int:meal_id>', methods=['GET'])
@login_required
def get_meal_route(meal_id):
    return get_meal(meal_id)

@meals_bp.route('/api/meals/<int:meal_id>/favorite', methods=['PATCH'])
@login_required
def toggle_favorite_route(meal_id):
    return toggle_favorite(meal_id)

@meals_bp.route('/api/meals/favorites', methods=['GET'])
@login_required
def get_favorite_meals_route():
    return get_favorite_meals()

@meals_bp.route('/api/meals/calorie-goal', methods=['PUT'])
@login_required
def update_calorie_goal_route():
    return update_calorie_goal()
    
@meals_bp.route('/api/meals/calorie-goal/streak', methods=['GET'])
@login_required
def calorie_streak_route():
    return calorie_streak()