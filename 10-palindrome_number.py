# Create a function that receives a number and evaluates whether it is a palindrome 
# (reads the same forwards and backwards). myFunction(2002) will return true

def is_palindrome(number: int) -> bool:
  if not isinstance(number, int):
    raise TypeError(f"Expected an integer, got {type(number)}")

  number_str = str(number)
  reversed_str = number_str[::-1]

  if number_str == reversed_str:
    print(f"It is a palindrome! Original number: {number}, reversed number: {reversed_str}")
    return True
  else:
    print(f"It is not a palindrome. Original number: {number}, reversed number: {reversed_str}")
    return False
  
# is_palindrome(2002)
# is_palindrome(5005)
# is_palindrome(500)
# is_palindrome("2002")


###################################################################################################

def is_palindrome(number: int) -> bool:
  if not isinstance(number, int):
    raise TypeError(f"Expected an integer, got {type(number)}")

  number_str = str(number)
  reversed_str = number_str[::-1]

  return number_str == reversed_str and print(f"It is a palindrome! Original number: {number}, reversed number: {reversed_str}")