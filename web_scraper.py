from bs4 import BeautifulSoup
import requests
import re

food_data = {}

foods = ["egg", "strawberry", "avocado", "tomato", "banana", "bread", "apple", "black-beans", "orange", "peanut",
         "cabbage","mango", "blueberries", "sweet-potato", "mushroom-white-button", "rice", "kidney-beans", "asparagus",
         "pineapple", "tortilla", "radish", "mandarin-orange", "steak", "salmon", "plantain", "pumpkin", "beet-beetroot",
         "corn", "queso-fresco", "cucumber", "garlic", "grape", "chicken", "lettuce", "pasta", "lemon", "yogurt", "oatmeal",
         "chayote-mirliton", "tacos", "kiwi", "rhubarb", "branzino", "paneer", "granadilla", "honeydew-melon", "raisins", "swiss-chard",
         "lima-bean", "pancakes", "papaya", "colby-cheese", "parsley", "guava-firm", "spaghetti-squash", "emmentaler-cheese",
         "acai", "ketchup", "taro", "edamame", "rutabaga-swede", "octopus", "pistachio", "goat-cheese", "dates", "parsnip",
         "sunflower-seed", "edam-cheese", "cloves", "romaine", "trout", "chickpea", "raspberry", "chives", "lentil","french-toast",
         "prickly-pear-cactus-fruit", "carrots", "blackberry", "cayenne-pepper", "oroblanco", "brie-cheese", "provolone",
         "north-atlantic-mackerel", "cotija-cheese", "bulgur", "leek", "crab", "hare", "pecorino-cheese", "galangal", "guava-soft",
         "mint", "zapote-mamey-sapote", "lotus-root", "seaweed", "tomatillo", "great-northern-bean", "chanterelle-mushroom",
         "labneh", "asian-pear", "portobello-portabella-mushroom", "pizza", "millet", "pulasan", "horned-melon-kiwano", "cardamom",
         "cod", "waffle", "collard-greens", "quail-egg", "duck", "allspice", "delicata-squash", "turkey", "turmeric",
         "kabocha-squash", "chia-seed", "sardines", "tuna", "snow-pea", "mayonnaise", "gruyere-cheese", "freekeh", "pinto-bean",
         "ghee", "fonio", "pork", "porcini-mushroom", "cranberry", "chamomile", "shrimp", "popcorn", "cacao-chocolate", "chicken-liver",
         "zucchini", "black-elderberry", "kumquat", "brussels-sprouts", "feijoa", "black-eye-peas", "cream-cheese", "cannellini-beans", 
         "king-trumpet-king-oyster-mushroom", "pomelo", "goose", "oyster", "stevia", "lime", "scallops", "macadamia-nut", "hemp-seed-hemp-heart",
         "artichoke", "monterey-jack-cheese", "navy-bean", "cashew", "olive-oil", "nectarine", "milk", "mutton-sheep", "kimchi",
         "soy-sauce", "morel-mushrooms", "butter", "farro-emmer", "peas-garden", "adzuki-bean", "plum", "quark", "summer-squash",
         "brisket", "bell-pepper", "ground-beef", "gouda-cheese", "burrata", "sunchoke-jerusalem-artichoke",
         "swiss-cheese", "mascarpone-cheese", "duck-eggs", "squid", "basil", "couscous", "cottage-cheese", "huckleberry", 
         "calamansi", "star-fruit-carambola", "yam", "juneberry", "bacon", "grapefruit", "spelt", "persimmon", "blood-sausage", 
         "cherry", "einkorn", "black-garlic", "buckwheat", "poppy-seed", "iceberg-lettuce", "brazil-nut", "havarti-cheese",
         "jicama", "sesame", "sour-cream", "anchovy", "hot-dog", "acorn-squash", "currants", "khorasan-wheat-kamut", "pine-nut", 
         "ramps", "spinach", "honey", "pecans", "venison-deer", "sugar", "nopales-prickly-pear-cactus", "matzah", "wood-ear-mushroom",
         "pumpkin-seed", "juice", "gooseberry", "maitake-hen-of-the-woods", "cantaloupe", "coconut", "feta-cheese", "eggplant", "camembert-cheese",
         "quince", "cheddar-cheese", "noodles", "watermelon", "miso", "straw-mushroom", "celeriac-celery-root","ostrich",
         "cauliflower", "chili-pepper", "bone-broth", "chipotle-pepper", "pear", "ham", "wheat", "barley", "mustard-seed",
         "mussels", "tofu", "onion", "sole", "sichuan-peppercorn", "cumin", "snap-pea", "string-cheese", "okra", "cranberry-bean",
         "walnut", "potato", "durian", "fennel", "kale", "crawfish-crayfish", "cheerios", "bok-choy", "cinnamon", "apricot",
         "yardlong-bean", "butternut-squash", "clementine", "catfish", "hibiscus-sorrel", "tilapia", "truffle", "parmesan", "mung-bean",
         "sapodilla", "lamb", "yuzu", "dragon-fruit-pitaya", "asiago-cheese", "fig", "manchego-cheese", "turnip", "coconut-milk",
         "celery", "lobster", "amaranth", "enoki-mushrooms", "fava-bean", "ricotta-cheese", "vanilla", "mozzarella-cheese", "la-tur-cheese",
         "lychee", "squash-blossoms", "quinoa", "herring", "black-pepper", "crackers", "clams", "shiitake-mushrooms", "quesillo-queso-oaxaca",
         "olives", "nutritional-yeast", "prune", "romanesco", "purple-potatoes", "flounder", "rambutan", "peach", "bitter-melon", 
         "jackfruit", "beech-mushrooms", "tamarind", "pomegranate", "pollock", "beef-liver", "rye", "broccoli", "mustard",
         "hazelnut", "nutmeg", "jalapeno-pepper", "vinegar", "almond", "spare-ribs", "ice-cream", "longan", "flaxseed-linseed",
         "tempeh", "kefir", "halibut", "oyster-mushroom", "haddock", "ginger", "loquat", "manoomin-wild-rice", "cilantro-coriander",
         "bone-marrow", "blue-cheese", "goldenberry-uchuva", "bison", "sausage", "green-beans", "rabbit", "chapulines-grasshoppers", 
         "passion-fruit", "cassava", 'sauerkraut', "teff", "maple-syrup", "plaice", "kohlrabi"]


for food in foods:

    URL = f"https://solidstarts.com/foods/{food}"
    page = requests.get(URL)
    soup = BeautifulSoup( page.content, 'html.parser')


    name = soup.find("h2", class_="font-sofia-bold text-3xl lg:text-4xl text-slate mb-4")
    # print(name.text)

    tags = soup.find_all("p", class_="font-sofia-medium tracking-normal text-slate text-lg lg:text-xl font-smooth")
    allergen = tags[1]
    # print(allergen.text)

    min_age = tags[2]
    # print(min_age.text)

    nutrition_rating = 5
    stars = soup.find_all("svg", class_="text-red")
    for star in stars:
        if "opacity-25" in str(star):
            nutrition_rating -= 1
            # print(nutrition_rating)

    food_data[food] = {}
    food_data[food]["name"] = name.text
    food_data[food]["min_age"] = min_age.text
    food_data[food]["nutrition_rating"] = nutrition_rating
    food_data[food]["allergen"] = allergen.text
    food_data[food]["external_id"] = food
    # print(food_data[food])

    
    # name, min_age, nutrition_rating, allergen, external_id = (
    #     food["name"],
    #     food["min_age"],
    #     food["nutrition_rating"],
    #     food["allergen"],
    #     food["external_id"],
    # )

# print(food_data)


import json
with open("food_data.json", 'w') as f:
    json.dump(food_data, f)





