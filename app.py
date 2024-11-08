from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily_diet.db'

db = SQLAlchemy(app)
CORS(app)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    in_diet = db.Column(db.Boolean, nullable=False, default=True)
    category = db.Column(db.String(50), nullable=True)
    calories = db.Column(db.Float, nullable=True)

@app.route('/api/meal/add', methods=['POST'])
def add_meal():
    data = request.json
    if 'name' in data:
        meal = Meal(
            name = data["name"],
            description = data.get("description", ""),
            in_diet = data.get("in_diet", True),
            category = data.get("category", None),
            calories = data.get("calories", None)
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Meal added successfully"}), 201
    return jsonify({"message": "Invalid meal data"}), 400


@app.route('/api/meal/update/<int:meal_id>', methods=['PUT'])
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
    
    db.session.commit()

    return jsonify({"message": "Meal updated successfully"})

@app.route('/api/meal/delete/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully"}), 201
    
    return jsonify({"message": "Meal not found"}), 404

@app.route('/api/meals', methods=['GET'])
def get_meals():
    meals = Meal.query.all()
    meal_list = []
    for meal in meals:
        meal_data = {
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time,
            "in_diet": meal.in_diet
        }
        meal_list.append(meal_data)

    return jsonify(meal_list)

@app.route('/api/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meal.query.get(meal_id)
    
    if meal:
        return jsonify({
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time,
            "in_diet": meal.in_diet
        })

    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)