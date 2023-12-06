#Program a function that returns the text trimmed according to the specified number of
#characters. myFunction("Hello world",2) will return "Hello"

def trim_text(text,length):
    if not isinstance(text,str) or not text:
        raise ValueError("You did not enter a valid text")
    
    if not isinstance(length, int) or length <= 0:
        raise ValueError("The lenght must be a positive integer")
    
    text_cut = text[:length]
    return f"The trimmed text is: {text_cut}"


def run():
    text = input("Enter a text: ")
    try:
        long = int(input("Enter the lenght: "))
        final_result = trim_text(text,long)
        return final_result
    except ValueError as e:
        return str(e)
    

if __name__ == '__main__':
    print(run())