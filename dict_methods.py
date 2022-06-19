d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']


d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

d.update(d2)
for key, value in d.items():
    print(key, value)


# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

values = d.values()
keys = d.keys()
print(keys)

d[10] = "ten"
print(values)

for key, value in d.items():
    if value == "five":
        print(f"d{key} was found with the key {key}")
    else:
        print("We couldn't find that one playa")


for item in d:
    print(item)

print()


