shopping_list = ["eggs", "fish", "chicken", "carrots", "apples", "potatoes"]

item_to_find = "pussy"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
if item_to_find in shopping_list:
    item_to_find = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} is not here buddy".format(item_to_find))
