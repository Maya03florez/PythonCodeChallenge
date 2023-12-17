#Write a function that calculates the factorial of a number (The factorial of a positive integer n is 
#defined as the product of all positive integers from 1 to n). For example, myFunction(5) should return 
#120.


def factorial(number: int) -> int:
  """
  Calculates the factorial of a non-negative integer.

  Args:
      number: The integer whose factorial to calculate.

  Returns:
      The factorial of the given number.

  Raises:
      TypeError: If the number is not an integer.
      ZeroDivisionError: If the number is 0.
      OverflowError: If the factorial calculation overflows the integer limit.
  """
  if not isinstance(number, int):
    raise TypeError(f"Expected an integer, got {type(number)}")

  if number == 0:
    raise ZeroDivisionError("Factorial of 0 is undefined")

  if number < 0:
    raise ValueError("Factorial cannot be calculated for negative numbers")

  factorial = 1
  for i in range(2, number + 1):  # range(start, stop + 1)
    factorial *= i

  return factorial

# Test cases
try:
  print(f"Factorial of 5: {factorial(5)}")
except OverflowError:
  print("Factorial of 5 overflows the integer limit")

try:
  factorial("5")
except TypeError as e:
  print(e)

try:
  factorial(0)
except ZeroDivisionError as e:
  print(e)

try:
  factorial(-1)
except ValueError as e:
  print(e)

try:
  print(f"Factorial of 8: {factorial(8)}")
except OverflowError:
  print("Factorial of 8 overflows the integer limit")



##############################################################################
  

def factorial(number: int) -> int:
  """
  Calculates the factorial of a non-negative integer.

  Args:
      number: The integer whose factorial to calculate.

  Returns:
      The factorial of the given number.

  Raises:
      TypeError: If the number is not an integer.
      ZeroDivisionError: If the number is 0.
  """
  if not isinstance(number, int):
    raise TypeError(f"Expected an integer, got {type(number)}")

  if number == 0:
    raise ZeroDivisionError("Factorial of 0 is undefined")

  if number < 0:
    raise ValueError("Factorial cannot be calculated for negative numbers")

  # Use recursion for a more concise and Pythonic approach
  def _factorial(n):
    if n == 0:
      return 1
    return n * _factorial(n - 1)

  return _factorial(number)