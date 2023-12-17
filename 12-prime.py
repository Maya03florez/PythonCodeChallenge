#!/usr/bin/env python3

# Program a function that determines whether a number is prime (meaning it is only divisible by
# itself and 1) or not. myFunction(7) will return True

def is_prime(number):
    # Count the number of divisors
    count = 0

    # Check for divisors
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    # If there are exactly 2 divisors, the number is prime
    if count == 2:
        return True
    else:
        return False

def run():
    try:
        # Get user input for the number
        number = int(input('Enter an integer => '))

        # Validate that the number is positive
        if number < 1:
            raise ValueError("Number must be a positive integer")

        # Check if the number is prime
        if is_prime(number):
            print('It is prime')
        else:
            print('It is not prime')

    # Handle ValueError for non-integer input
    except ValueError as e:
        print("Error:", e)

if __name__ == '__main__':
    # run()
    pass


################################################################################################

def is_prime(n):
  """
  Determines whether a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """
  return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

# Example usage
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False
