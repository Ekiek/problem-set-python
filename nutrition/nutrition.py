item = input("Type a fruit: ").lower()

nutrition_info = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "lemon": 15,
    "lime": 20,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "strawberry": 50,
}

if item in nutrition_info:
    print(nutrition_info[item])
else:
    print("wrong input")