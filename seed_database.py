"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

# Load food data from JSON file
with open("data/seed_data.json") as f:
    food_data = json.loads(f.read())

# Create foods, store them in list so we can use them to create fake ratings
foods_in_db = []
for food in food_data:
    name, min_age, nutrition_rating, allergen, external_id = (
        food["name"],
        food["min_age"],
        food["nutrition_rating"],
        food["allergen"],
        food["external_id"],
    )
    
    db_food = crud.create_food(name, min_age, nutrition_rating, allergen, external_id)
    foods_in_db.append(db_food)

model.db.session.add_all(foods_in_db)
model.db.session.commit()

# Create 5 users; each user will make 5 ratings
for n in range(5):
    email = f"user{n}@test.com"
    password = "test"
    phone = "510-555-1234"

    user = crud.create_user(email, password, phone)
    model.db.session.add(user)

    for _ in range(5):
        random_food = choice(foods_in_db)
        score = randint(1, 3)

        rating = crud.create_rating(user, random_food, score)
        model.db.session.add(rating)

model.db.session.commit()