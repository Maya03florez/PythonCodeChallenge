#!/usr/bin/env python3

# Define a class called 'Person' with attributes with 'name' and 'age',
# create instances of this class and show information about them.


class Person():
    """Represent a person with name and age"""

    def __init__(self, name, age):
        """Initialize an instance of the Person class"""
        self.name = name
        self.age = age

    def __str__(self):
        """Retruns a chain representation of the person"""
        return f'My name is {self.name} and I\'m {self.age} years old.'

# an instance of the class Person
jhon = Person("John Connor", 25)
print(jhon)