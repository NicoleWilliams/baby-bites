"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb baby-food-tracker")
os.system("createdb baby-food-tracker")

model.connect_to_db(server.app)
model.db.create_all()

# Load food data from JSON file
with open("data/food_data.json") as f:
    food_data = json.loads(f.read())

# Create foods, store them in list so we can use them to create fake ratings
for food in food_data.values():
    name, min_age, nutrition_rating, allergen, external_id = (
        food["name"],
        food["min_age"],
        food["nutrition_rating"],
        food["allergen"],
        food["external_id"],
    )
    
    db_food = crud.create_food(name, min_age, nutrition_rating, allergen, external_id)
    model.db.session.add(db_food)
    model.db.session.commit()

all_foods_in_db = crud.get_foods()

