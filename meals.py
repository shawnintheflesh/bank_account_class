meal = [["eggs", "bacon", "cheese"],
        ["eggs", "cheese"],
        ["eggs", "bacon", "avocado"],
        ["eggs", "avocado"],
        ["eggs", "cheese", "avocado"]
        ]

for items in meal:
    if "cheese" not in items:
        print(items)
    else:
        print("{0} has a cheese count of {1}".format(items, items.count("cheese")))