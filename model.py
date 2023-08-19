"""Models for baby food tracking app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.Integer)

    ratings = db.relationship("Rating", back_populates="user")
    food_schedules = db.relationship("FoodSchedule", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
    

class FoodSchedule(db.Model):
    
    __tablename__ = "food_schedules"

    schedule_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    to_try_date = db.Column(db.Date, nullable=False)
    tried = db.Column(db.Boolean)

    user = db.relationship("User", back_populates="food_schedules")
    food = db.relationship("Food", back_populates="food_schedules")
    meal = db.relationship("Meal", back_populates="food_schedules")

    def __repr__(self):
        return f'<FoodSchedule schedule_id={self.schedule_id} meal_id={self.meal_id} food_id={self.food_id} user_id={self.user_id} to_try_date={self.to_try_date} tried={self.tried}>'
    

class Meal(db.Model):

    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    meal_name = db.Column(db.String(50), nullable=False)
    external_id = db.Column(db.String(50))

    rating = db.relationship("Rating", back_populates="meal")
    food_schedules = db.relationship("FoodSchedule", back_populates="meal")
    meal_foods = db.relationship("MealFood", back_populates="meal")

    def __repr__(self):
        return f'<Meal meal_id={self.meal_id} meal_name={self.meal_name}>'
    

class Food(db.Model):

    __tablename__ = "foods"

    food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_name = db.Column(db.String(30), nullable=False)
    min_age = db.Column(db.String(30))
    nutrition_rating = db.Column(db.Integer)
    allergen = db.Column(db.Boolean)
    external_id = db.Column(db.String(50))

    rating = db.relationship("Rating", back_populates="food")
    food_schedules = db.relationship("FoodSchedule", back_populates="food")
    meal_foods = db.relationship("MealFood", back_populates="food")

    def __repr__(self):
        return f'<Food food_id={self.food_id} food_name={self.food_name}>'
    

class Rating(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date_rated = db.Column(db.DateTime)
    comment = db.Column(db.Text)

    meal = db.relationship("Meal", back_populates="rating")
    user = db.relationship("User", back_populates="ratings")
    food = db.relationship("Food", back_populates="rating")

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score} meal_id={self.meal_id} food_id={self.food_id} user_id={self.user_id}>'
    

class MealFood(db.Model):

    __tablename__ = "meal_foods"

    meal_food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'), nullable=False)

    meal = db.relationship("Meal", back_populates="meal_foods")
    food = db.relationship("Food", back_populates="meal_foods")

    def __repr__(self):
        return f'<MealFood meal_food_id={self.meal_food_id} meal_id={self.meal_id} food_id={self.food_id}>'


def connect_to_db(flask_app, db_uri="postgresql:///baby-food-tracker", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)