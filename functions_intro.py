def multiply(x, y):
    result = x * y
    return result



def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()


answer = multiply(18, 3)
print(answer)

# sentence = input("Please write a sentence here: ")
# if palindrome_sentence(sentence):
#     print("True. '{}' is a palindrome".format(sentence))
# else:
#     print("Nah bro. '{}' is not a palindrome".format(sentence))