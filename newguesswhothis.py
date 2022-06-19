import random

highest = 20
answer = random.randint(1, highest)
print(answer)
print("Pick a number between 1 and {}: ".format(highest))
print("If you would like to quit, press 0.")
guess = 18


if guess == 0:
    break
if guess == answer:
    print("Great guess. You want a cookie?")
while guess != answer:
    guess = int(input())
    if guess > answer:
        print("Damn bro that's too high. Try again.")
    if guess < answer:
        print("Damn bro you're too low. Go")
    if guess == answer:
        print("It took you long enough didn't it damn")

