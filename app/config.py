class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///daily_diet.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CALORIE_GOAL = 2000