available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mousepad",
                   "HDMI cable"
                   ]
computer_parts = []
current_choice = "-"

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

while current_choice != 0:
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        if current_choice in computer_parts:
            computer_parts.remove(current_choice)

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
if current_choice == 0:
    print("Thanks for shopping!")



    current_choice = input()



