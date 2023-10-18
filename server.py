"""Server for baby food tracker app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db
import crud
from datetime import datetime
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""
    
    return render_template("homepage.html")


@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    phone = request.form.get("phone")

    user = crud.get_user_by_email(email)
    if user:
        flash("User already exists. Try again.")
    else:
        user = crud.create_user(email, password, fname, phone)
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.user_id
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a user."""

    if int(user_id) != session["user_id"]:
        render_template("incorrect_user.html")

    user = crud.get_user_by_id(user_id)
    schedule_events = crud.get_schedule_ids_by_user_id(user_id)
    to_try_dates = set()
    
    for schedule_event in schedule_events:
        if schedule_event.tried == False:
            to_try_dates.add(schedule_event.to_try_date)

    to_try_dates = sorted(to_try_dates)

    if schedule_events == None:
        print("Your schedule is empty. Add some foods to try!")

    # if schedule_event.tried == True:
    #     return redirect(f"/foods/{schedule_event.food.food_id}")

    return render_template("user_details.html", user=user, 
                           schedule_events=schedule_events,
                           to_try_dates=to_try_dates)


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")
    

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password you entered is incorrect.")
    else:
        session["user_email"] = user.email
        session["user_id"] = user.user_id
        # flash(f"Hello again, {user.fname}.")

    return redirect(f"/users/{user.user_id}") 


@app.route("/foods")
def all_foods():
    """View all foods."""

    foods = crud.get_foods()
    user = session.get("user_id")

    return render_template("all_foods.html", foods=foods, user_id=user)
    


@app.route("/foods/<food_id>")
def show_food(food_id):
    """Show details on a particular food."""

    food = crud.get_food_by_id(food_id)
    user = crud.get_user_by_email(session.get("user_email"))

    return render_template("food_detail.html", food=food, user=user)


@app.route("/foods/<food_id>/ratings", methods=["POST"]) 
def create_rating(food_id):
    """Create a new rating for a meal or food."""

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")
    comment = request.form.get("comment")        
    date_rated = datetime.now().strftime("%x")

    if logged_in_email is None:
        flash("You must log in to rate a food.")
    elif not rating_score:
        flash("Please select a score for this food.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        food = crud.get_food_by_id(food_id)

        rating = crud.create_rating(int(rating_score), food, user, date_rated, comment) # how to convert this to an emoji?
        db.session.add(rating)
        db.session.commit()

        if rating_score == "1":
            message = "loved"
        elif rating_score == "2":
            message = "had neutral feelings about"
        elif rating_score == "3":
            message = "didn't like"

        flash(f"You {message} this food.")

    return redirect(f"/foods/{food_id}")


@app.route("/update_rating", methods=["POST"])
def update_rating():
    rating_id = request.json["rating_id"]
    updated_score = request.json["updated_score"]
    crud.update_rating(rating_id, updated_score)
    db.session.commit()

    return "Rating updated"


@app.route("/edit-calendar", methods=["POST"])
def edit_calendar():
    """Add or remove items from calendar."""

    food_id = request.json.get("id")
    food_name = request.json.get("name")
    try_date = request.json.get("date")

    logged_in_email = session.get("user_email")
    user = crud.get_user_by_email(logged_in_email)
    date = datetime.strptime(try_date, "%Y-%m-%d").date()

    schedule_event = crud.create_food_schedule(food_id, user.user_id, date)
    
    return jsonify({'status': 200, 'message': "Schedule updated"})


@app.route("/mark-as-tried", methods=["POST"])
def mark_as_tried():
    """Removes an event from the calendar once the tried button is clicked."""

    tried = request.json.get("tried")
    food_id = request.json.get("foodId")
    logged_in_email = session.get("user_email")
    user = crud.get_user_by_email(logged_in_email)
    food_schedule = crud.get_food_schedule(user=user, food_id=food_id)
    food_schedule.tried = True
    db.session.commit()

    return jsonify({'message': "removed from schedule"})


@app.route("/create-food-dict")
def create_food_dict():
    """Creates a food dictionary with name and external id from database."""

    foods_dict = {}
    foods = crud.get_foods()
    
    for food in foods:
        foods_dict[food.food_name.lower()] = {"name": food.food_name, "external_id": food.external_id, "food_id": food.food_id}

    return jsonify(foods_dict)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)