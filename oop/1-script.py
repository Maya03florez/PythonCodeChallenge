#!/usr/bin/env python3


#Inheritance
#create a base class called 'Animal' with a method speak(). Then, create derived classes
#like dog and cat that inheritate from the Animal class and overwrite the speak() method.

class Animal:
    def __init__(self, id, age, genre, type_animal) -> None:
        # Constructor for the base class Animal
        self.id = id
        self.age = age
        self.genre = genre
        self.type_animal = type_animal

    def speak(self):
        # Speak method for the base class Animal
        return f"I'm a {self.type_animal}"

# Derived class Dog
class Dog(Animal):
    def __init__(self, id, age, genre, breed) -> None:
        # Calling the constructor of the base class using super()
        super().__init__(id, age, genre, type_animal="Dog")
        # Additional attribute specific to Dog
        self.breed = breed

    def speak(self):
        # Overriding the speak method for Dog
        return f"I'm a {self.type_animal} and I bark!"

# Derived class Cat
class Cat(Animal):
    def __init__(self, id, age, genre, color) -> None:
        # Calling the constructor of the base class using super()
        super().__init__(id, age, genre, type_animal="Cat")
        # Additional attribute specific to Cat
        self.color = color

    def speak(self):
        # Overriding the speak method for Cat
        return f"I'm a {self.type_animal} and I meow!"

# Example usage
dog_instance = Dog(id=1, age=3, genre="Male", breed="Golden Retriever")
cat_instance = Cat(id=2, age=2, genre="Female", color="Gray")

# Printing the results of the speak method for Dog and Cat instances
print(dog_instance.speak())  # Output: I'm a Dog and I bark!
print(cat_instance.speak())  # Output: I'm a Cat and I meow!