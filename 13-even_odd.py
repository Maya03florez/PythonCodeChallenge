#Program a function that determine wether a number is even or odd. myFunction(29)
#will return odd

def is_even_or_odd(input_number):
    if not input_number:
        raise ValueError("You must enter a number")
    
    return input_number % 2 == 0

def run():
    try:
        input_number = int(input("Enter a number: "))
        is_even = is_even_or_odd(input_number)
        if is_even:
            print("It is even.")
        else:
            print("It is odd.")
    except ValueError as e:
        print(f"Error: {e}")
        return

if __name__ == '__main__':
    run()