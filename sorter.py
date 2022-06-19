pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 6.7, 8.9, 0.1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Shawn",
         "Rachel",
         "Diego",
         "Chris",
         "Aaron"
         ]
names.sort()
print(names)

name_letter = sorted(names)
print(name_letter)