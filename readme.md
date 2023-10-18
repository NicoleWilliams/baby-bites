# Baby Bites


## Project Description 

Baby Bites lets you search a database of baby-safe foods and add it to a schedule on your personal user page. Each food in the database has its own detail page that gives information such as its nutrition rating, the age at which it’s safe to introduce to your child, and whether it’s a common allergen. You can choose a date to add a food to your schedule. Once you've tried a food, you can check it off of your schedule. This takes you to the food's detail page where you can rate the food and leave any comments you have. Your schedule and ratings will appear on your user page.


## About the Developer

Baby Bites was created by Nicole Williams. Learn more about the Developer on [LinkedIn](https://www.linkedin.com/in/nicole-williams-14204880/)


## Technologies 

**Tech Stack:**

- Python 
- Flask
- JavaScript 
- JSON
- JQuery 
- AJAX 
- PostgreSQL 
- SQLAlchemy
- Jinja 
- HTML
- CSS


Baby Bites is an app built using Python on a Flask server. It uses a PostgreSQL database with SQLAlchemy as the ORM. The frontend utilizes HTML, Jinja and CSS. Data is imported to JavaScript from a JSON file. JavaScript uses AJAX and JQuery to interact with the backend. 


## Features

![alt text](https://github.com/NicoleWilliams/baby-bites/blob/main/static/screenshots/BB%20Homepage.png "Baby Bites Login")

From the homepage, a user is able to create an account. If an account already exists, the user can log in. 


![alt text](https://github.com/NicoleWilliams/baby-bites/blob/main/static/screenshots/BB%20Schedule.png "User Schedule")

On the personal user page, the user is able to view any foods they have scheduled. Foods are separated by date. Once a food has been tried, a user can click on the checkbox next to the food name to mark it as tried. This will navigate the user to the food detail page where a rating can be given. 

Above the user's schedule is a link to view all foods available to add. 


![alt text](https://github.com/NicoleWilliams/baby-bites/blob/main/static/screenshots/BB%20All%20Foods.png "All Foods")

The All Foods page shows a list of all foods contained in the baby-safe foods database. To improve usability, there is a search box at the top of the food list. 


![alt text](https://github.com/NicoleWilliams/baby-bites/blob/main/static/screenshots/BB%20Add%20to%20Schedule.png "Add to Schedule")

A user can add any food to their schedule by selecting a date from the calendar and clicking "Add To Schedule". Multiple foods can be added before navigating back to the user page. 


![alt text](https://github.com/NicoleWilliams/baby-bites/blob/main/static/screenshots/BB%20Food%20Detail.png "Food Detail")

A user can view a food's detail page by clicking on the food name. 

The Food Detail page shows nutritional information on the food such as the minimum age at which it's safe to feed a child, a nutrition score on a scale of 1-5 and whether or not it's a common allergen. 

This page is also where users can rate the food. Rating scores are given using emojis. There is an open text box to leave comments associated with the rating. Once a rating is submitted, it will appear in the user's ratings table on their user page. 


![alt text](https://github.com/NicoleWilliams/baby-bites/blob/main/static/screenshots/BB%20Ratings.png "Ratings")

On the personal user page, users are also able to view any ratings they have given. This includes the food name, score, date rated and any comments left with each rating. 



## Setup/Installation

To run this app on your local computer, follow these steps:

Clone repository:
```
$ git clone https://github.com/NicoleWilliams/baby-bites.git
```
Create a virtual environment:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip3 install -r requirements.txt
```
Run seed_database.py to create and populate a database.
```
$ python3 seed_database.py
```
Run the app from the command line.
```
$ python3 server.py
```



## Version 2.0 Features

- **Log out:** Ability to log out once finished.
- **Edit or Remove:** Ability to edit the date of or remove an already scheduled food.
- **Forgot Password:** Ability to retreive a password if forgotten.
- **Meals:** Ability to group foods together to create meals or add your own item not in the database.