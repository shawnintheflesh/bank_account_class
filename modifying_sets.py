numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "yellow", "red", "white"]
data_set = set(data)

print(data_set)

data_set = list(dict.fromkeys(data))
print(data_set)