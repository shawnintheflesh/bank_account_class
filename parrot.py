name = input("Hey bro what's your name? ")
age = int(input("Can you go on this trip? How old are you? "))

#if 18 <= age <= 30:
if age in range(18, 31):
    print("Yes you can. Let's roll, {}!".format(name))
else:
    print("Man get your ass on somewhere!")
