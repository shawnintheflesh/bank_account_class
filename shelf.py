import shelve

with shelve.open("ShelveTest") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "a green, tangy fruit"
    fruit["lemon"] = "a sour, yellow, citrus fruit"
    fruit["grape"] = "a small, purple, sweet fruit"
    fruit["lime"] = "a green, sour, citrus fruit"

#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)

while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break

    description = fruit.get(shelf_key)
    print(description)

fruit.close()