name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote!")
#     print("Put an X in the box.")
# else:
#     print("Come back in {0} years so you can vote bitch".format(18 - age))

if age < 18:
    print("Come back in {0} years so you can vote bitch".format(18 - age))
elif age == 900:
    print("Damn nig you're old as hell")
else:
    print("You are old enough to vote!")
    print("Fuck you waitin for? Put an X in the box bitch")

