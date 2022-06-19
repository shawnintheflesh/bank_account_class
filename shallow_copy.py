animals = {
    "lion": ["scary", "strong", "king of the jungle looking ass boy"],
    "elephant": ["big", "gray as hell", "great memory"],
    "monkey": ["human like", "funny", "drakeo kept them in the chunky variety"],
}

things = animals.copy()

print(things["monkey"])
print(animals["monkey"])

print()

things["monkey"].append("crazy")
print(things["monkey"])
print(animals["monkey"])