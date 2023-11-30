#Programming exercises
#Write a function that counts the number of characters in a string. myFunction('hello world') will return 11 

def countCharacters(string):
    if not string:
        print("Empty string provided")
    else:
        print(f'the amount of characters of "{string}" has {len(string)} characters')

countCharacters("")
countCharacters("hello world")

####################################################################

def count_characters(string):
    if not string:
        raise ValueError("Empty string provided")

    character_count = 0
    for character in string:
        character_count += 1

    return character_count

try:
    print(count_characters(""))
except ValueError as e:
    print(e)


total_characters = count_characters("")
print(f'\nThe total character are {total_characters}')
