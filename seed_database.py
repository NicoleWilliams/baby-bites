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
with open("data/seed_data.json") as f:
    food_data = json.loads(f.read())

# Create foods, store them in list so we can use them to create fake ratings
for food in food_data:
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

print(all_foods_in_db, 'foods in database, line 39')

# Create 5 users; each user will make 5 ratings
for n in range(5):
    email = f"user{n}@test.com"
    password = "test"
    phone = "510-555-1234"

    user = crud.create_user(email, password, phone)
    model.db.session.add(user)
    model.db.session.commit()

    for _ in range(5):
        random_food = choice(all_foods_in_db)
        print(random_food, 'random food choice line 54')
        
        score = randint(1, 3)
        date_rated = datetime.now()
        comment = "test comment"
        rating = crud.create_rating(score, random_food, user,  
                                    date_rated.strftime("%x"), 
                                    comment)
        model.db.session.add(rating)
        model.db.session.commit()