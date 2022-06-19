meal = [["eggs", "bacon", "cheese"],
        ["eggs", "cheese"],
        ["eggs", "bacon", "avocado"],
        ["eggs", "avocado"],
        ["eggs", "cheese", "avocado"]
        ]

for ingredients in meal:
        for index in range(len(ingredients) -1, -1, -1):
                if ingredients[index] == "cheese":
                        del ingredients[index]
        print(", ".join(ingredients))


