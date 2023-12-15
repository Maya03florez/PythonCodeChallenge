# Create a function that removes a specific pattern of characters from a given text.
# myFunction("xyz1,xyz2,xyz3,xyz4,xyz5","xyz") will return (1,2,3,4,5)

def remove_characters(text="", pattern=""):
    if not text:
        print("You did not enter any text")
    elif not pattern:
        print("You did not enter a character pattern")
    else:
        result = text.replace(pattern, "")
        print(result)

# Test cases
remove_characters()
remove_characters("xyz1,xyz2,xyz3,xyz4,xyz5")
remove_characters("xyz1,xyz2,xyz3,xyz4,xyz5", "xyz")