#!/usr/bin/env python3

#Program a function that, given a string, returns an array of texts separated by a
#specific character. myFunction("Hello how are you"," ") will return ["Hello","how","are","you"] 

def convert_to_array(text,delimiter):
    try:
        if not text or not delimiter:
            raise ValueError("Please enter both a text and a delimiter")
        return text.split(delimiter)
    except ValueError as e:
        print(e)
        return []
    

def run():
    try:
        main_text = input("Enter a text: ")
        delimiter = input("Enter a delimiter: ")
        converted_text = convert_to_array(main_text,delimiter)
        return converted_text
    except KeyboardInterrupt:
        print("\nYou have interrupted the execution.")
        return []
    

if __name__ == '__main__':
    print(run())