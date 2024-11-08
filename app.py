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


@app.route('/api/meal/add', methods=['POST'])
def add_meal():
    data = request.json
    if 'name' in data:
        meal = Meal(
            name=data["name"],
            description=data.get("description", ""),
            in_diet=data.get("in_diet", True)
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

if __name__ == "__main__":
    app.run(debug=True)