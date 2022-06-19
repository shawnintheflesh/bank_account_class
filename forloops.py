number = input("Enter whatever numbers you want and use separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
