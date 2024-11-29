from flask import Blueprint, request
from flask_login import login_required
from app.views.water.water_views import add_water_intake, remove_water_intake, get_water_intake, get_total_water_intake, update_water_goal, water_streak

water_bp = Blueprint('water_bp', __name__)

@water_bp.route('/api/water/add', methods=['POST'])
@login_required
def add_water_intake_route():
    return add_water_intake(request.json)

@water_bp.route('/api/water/delete/<int:water_id>', methods=['DELETE'])
@login_required
def remove_water_intake_route(water_id):
    return remove_water_intake(water_id)

@water_bp.route('/api/water', methods=['GET'])
@login_required
def get_water_intake_route():
    return get_water_intake(request.args)

@water_bp.route('/api/water/total', methods=['GET'])
@login_required
def get_total_water_intake_route():
    return get_total_water_intake(request.args)

@water_bp.route('/api/water/goal', methods=['PUT'])
@login_required
def update_water_goal_route():
    return update_water_goal()

@water_bp.route('/api/water/streak', methods=['GET'])
@login_required
def water_streak_route():
    return water_streak()