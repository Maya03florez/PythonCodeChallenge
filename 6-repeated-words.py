# Program a function to count the number of times a word is repeated in a long text.
# myFunction("hello world hello", "world") will return 2


def count_word_in_text(text, word):
    if not text or not word:
        print("You must provide both text and a word")
    else:
        occurrences = text.count(word)
        print(f'The word "{word}" appears {occurrences} times in the text.')

# Example usage:
# count_word_in_text("", "")
# count_word_in_text("large text with large words", "text")

#####################################################################################

import re


def count_word(text, word):
    if not text or not word:
        print("You must provide both text and a word")
    else:
        occurrences = re.findall(r'\b' + re.escape(word) + r'\b', text)
        print(f'The word "{word}" appears {len(occurrences)} times in the text.')

# Example usage:
count_word("", "")
count_word("large text with large words", "large")
