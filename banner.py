def banner_text(text, screen_width):

    if len(text) > screen_width - 4:
        raise ValueError("String {0} is too damn long for {1}".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)
