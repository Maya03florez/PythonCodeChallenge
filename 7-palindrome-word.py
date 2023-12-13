#Program a function that validates whether a given word or phrase is a palindrome
# (that reads the same forwards and backwards). myFunction("salas") will return true 


def is_palindrome(word):
    if not word:
        raise ValueError("You didn't enter a word")

    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]


def run():
    try:
        word = input("Enter a word: ")
        if is_palindrome(word):
            print(f"The word {word} is a palindrome")
        else:
            print(f"The word {word} is not a palindrome")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == '__main__':
    run()