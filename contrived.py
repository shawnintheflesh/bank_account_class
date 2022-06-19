numbers = [1, 12, 32, 45, 60]

for number in numbers:
    if number % 8 == 0:
        print("We can't have this shit!")
        break
else:
    print("These numbers are cool.")
