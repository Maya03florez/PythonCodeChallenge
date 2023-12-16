import random

def random_number():
    print(round((random.random() * 100) + 500))

# random_number()
    
#################################################################################
    
import random

def get_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

random_array = []

# Generate 20 random numbers in the range of 501 to 601
for _ in range(20):
    random_array.append(get_random_number(501, 601))

print(random_array)