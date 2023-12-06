#!/usr/bin/env python3

# Create a function that repeats a text a specified number of times. 
#   myFunction("Hello world", 2) will return:
#   Hello world
#   Hello world 


def repeat_text(text, times):
    if not text:
        return "You did not enter any text"

    if times is None:
        return "You did not enter the number of times to repeat the text"

    if times <= 0:
        return "Must be a positive integer"

    for idx in range(1, times + 1):
        print(f"{idx} -> {text}")


repeat_text("Hello world!", 4)