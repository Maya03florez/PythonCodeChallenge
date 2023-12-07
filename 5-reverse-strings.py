#Program a function that reverses the words of a string.
#miFuncion("Hola") will return "odnuM aloH"

def reverse_string(string=""):
    if not string:
        print("You did not enter a string")
    else:
        print(string[::-1])

# reverse_string("Hola mundonon")

#/\/\/\//\/\\/\/\/\\/\\/\/\/\/\/\/\\/\/\\/\/\/\\/\/\/\/

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text

print(reverse("hola mundo"))

####################################################



def reverse(text):
    return ''.join(reversed(text))

print(reverse("hola mundo"))