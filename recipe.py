import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["Tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipe') as recipe:
    # recipe["blt"] = blt
    # recipe["beans_on_toast"] = beans_on_toast
    # recipe["scrambled_eggs"] = scrambled_eggs
    # recipe["soup"] = soup
    # recipe["pasta"] = pasta
    recipe["soup"] = soup

    recipe["blt"].append("butter")
    recipe["pasta"].append("tomato")
    
    for snack in recipe:
        print(snack, recipe[snack])
