"""CRUD operations."""

from model import db, User, FoodSchedule, Food, Rating, connect_to_db

def create_user(email, password, phone):
    """Create and return a new user."""

    user = User(email=email, password=password, phone=phone) #may need to add in a default for phone in case they don't add one.

    return user

def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_food_schedule(food, user, to_try_date, tried):
    """Create and return a new food schedule."""

    food_schedule = FoodSchedule(food=food, user=user, to_try_date=to_try_date, tried=tried)

    return food_schedule


# def create_meal(meal_name, external_id):
#     """Create and return a new meal."""

#     meal = Meal(meal_name=meal_name, external_id=external_id)

#     return meal


def create_food(food_name, min_age, nutrition_rating, allergen, external_id):
    """Create and return a new food."""

    food = Food(food_name=food_name, min_age=min_age, nutrition_rating=nutrition_rating, allergen=allergen, external_id=external_id)

    return food


def get_food_by_id(food_id):
    """Return a food by primary key."""

    return Food.query.get(food_id)


def get_foods():
    """Return all foods."""

    return Food.query.all()


def create_rating(score, food, user, date_rated, comment):
    """Create and return new rating."""

    rating = Rating(score=score, food=food, user=user, date_rated=date_rated, comment=comment)

    return rating


def update_rating(rating_id, new_score):
    """Update a rating given rating_id and the updated score."""

    rating = Rating.query.get(rating_id)
    rating.score = new_score


# def create_meal_food(meal_id, food_id):
#     """Create and return new meal-food."""

#     meal_food = MealFood(meal_id=meal_id, food_id=food_id)

#     return meal_food

def return_food_schedule():
    """Return food schedule"""

    return FoodSchedule.query.all()


def return_ratings():
    """Return all ratings."""

    return Rating.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_schedule_by_id(schedule_id):
    """Return a schedule by primary key."""

    return FoodSchedule.query.get(schedule_id)


def get_schedule_id_by_user_id(user_id):
    """Return a schedule id from a user id."""

    schedule = FoodSchedule.query.filter(FoodSchedule.user_id == user_id).first()
    return schedule.schedule_id


if __name__ == '__main__':
    from server import app
    connect_to_db(app)