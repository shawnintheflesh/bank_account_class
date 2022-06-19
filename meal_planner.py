pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}


stuff_to_get = {}


def add_shopping_item(data: list, item: str, amount: int) -> None:
    """
    Add a dictionary that has the items and number of items.
    :param data: The list that the food comes from.
    :param item: The actual ingredients that need to be added.
    :param amount: The amount of the ingredients to be added.
    :return:
    """

    data[item] = data.setdefault(item, 0) + amount


display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe")
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input("Make your choice here: ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items:
            quantity_in_pantry = pantry.get(food_item, 0)
            if quantity_in_pantry <= required_quantity:
                print(f"/t {food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"/t You need to buy {quantity_to_buy} of {food_item} bro")
                add_shopping_item(stuff_to_get, food_item, quantity_to_buy)

for things in stuff_to_get.items():
    print(things)



