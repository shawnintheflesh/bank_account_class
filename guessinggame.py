import random

highest = 1000
answer = random.randint(1, 1000)


def get_integer(prompt):
    """
    Get an integer from standard input (stdin).

    The function will continue looping until the user gives a
    legit integer.

    :param prompt: The string that the user will see when they are prompted to enter information.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

print("Guess a number between 1 and 1000: ")
guess = int(input())

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

if guess == answer:
    print("Damn you're just right")
    print("Want a cookie nigga?")
else:
    if guess > answer:
        print("Damn you're way too high")
        guess = int(input())
        if guess == answer:
            print("Finally nigga")
        else:
            print("You've gone through half the options nigga hurry up")
    if guess < answer:
        print("Damn you're way too low")
        guess = int(input())
        if guess == answer:
            print("Finally nigga")
        else:
            print("You've gone through half the options nigga hurry up")

# if guess > answer:
#     print("You're way too high bro")
#     guess = int(input())
#     if guess == answer:
#         print("You catch on quick huh bitch")
#     else:
#         print("It ain't but ten options to choose from dummy hurry up")
# elif guess == answer:
#     print("Damn nig you got it right already?")
#     print("Want a cookie nigga?")
# else:
#     print("Damn you're too low now")
#     guess = int(input())
#     if guess == answer:
#         print("You catch on quick huh bitch")
#     else:
#         print("It ain't but ten options to choose from dummy hurry up")