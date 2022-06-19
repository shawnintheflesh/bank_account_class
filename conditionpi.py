age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("You better have a job")
else:
    if age < 16:
        print("Learn something at school bro")
    if age > 65:
        print("Don't break your hip while existing old bro")
print("-" * 80)
