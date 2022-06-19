import copy

lion_list = ["scary", "strong", "king of the jungle looking ass boy"]
elephant_list = ["big", "gray as hell", "great memory"]
monkey_list = ["human like", "funny", "drakeo kept them in the chunky variety"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "monkey": monkey_list,
}

stuff = {}

def my_deepcopy (d: dict) -> dict:
    """
    Makes a copy of a dictionary.
    :param d:
    :return:
    """
animals_copy = my_deepcopy(animals)






things = copy.deepcopy(animals)
print()


monkey_list.append("crazy")
animals["monkey"].append("added via `animals`")
things["monkey"].append("added via `things`")
print(id(things["monkey"]), things["monkey"])
print(id(animals["monkey"]), animals["monkey"])