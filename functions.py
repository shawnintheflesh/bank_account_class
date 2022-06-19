def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return  " " * left_margin, text

with open("centered", mode='w') as centered_file:
    center_text("First", "Second", 3, 4, "spam", file=centered_file)

