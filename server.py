"""Server for baby food tracker app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""
    
    return render_template("homepage.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")

    user = crud.get_user_by_email(email)
    if user:
        flash("User already exists. Try again.")
    else:
        user = crud.create_user(email, password, phone)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/user/<user_id>")
def show_user(user_id):
    """Show details on a user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


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
        flash(f"Hello again, {user.email}.")

    return redirect("/calendar") 


@app.route("/foods")
def all_foods():
    """View all foods."""

    foods = crud.get_foods()

    return render_template("all_foods.html", foods=foods)


@app.route("/foods/<food_id>/ratings", methods=["POST"]) 
def create_rating(food_id):
    """Create a new rating for a meal or food."""

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a food.")
    elif not rating_score:
        flash("Please select a score for this food.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        food = crud.get_food_by_id(food_id)

        rating = crud.create_rating(user, food, int(rating_score)) # how to convert this to an emoji?
        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this food {rating_score}.")

    return redirect(f"/food/{food_id}")


@app.route("/update_rating", methods=["POST"])
def update_rating():
    rating_id = request.json["rating_id"]
    updated_score = request.json["updated_score"]
    crud.update_rating(rating_id, updated_score)
    db.session.commit()

    return "Rating updated"


@app.route("/calendar")
def calendar():
    """View calendar with scheduled foods."""


@app.route("/ratings")
def view_ratings():
    """View a list of foods tried and ratings given."""

    ratings = crud.return_ratings()

    return render_template("ratings.html", ratings=ratings)


@app.route("/add-to-schedule")
def add_to_schedule():
    """Search for and select foods and add to calendar."""


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)