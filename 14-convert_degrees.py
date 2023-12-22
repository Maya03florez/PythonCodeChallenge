#!/usr/bin/env python3

# Write a function to convert Celsius to Fahrenheit and vice versa.
#myFunction(0,"c") will return 32 F


def temperature_converter(degrees, unit):
    unit = unit.lower()  # Convert unit to lowercase for case-insensitive comparison
    if unit == "c":  # If Celsius input
        fahrenheit = (degrees * 9/5) + 32  # Convert Celsius to Fahrenheit
        return f"{degrees}°C = {round(fahrenheit)}°F"  # Return the result as a formatted string
    elif unit == "f":  # If Fahrenheit input
        celsius = (degrees - 32) * 5/9  # Convert Fahrenheit to Celsius
        return f"{degrees}°F = {round(celsius)}°C"  # Return the result as a formatted string
    else:
        return "Invalid temperature type. Please use 'c' for Celsius or 'f' for Fahrenheit."  # Invalid input message

result = temperature_converter(0, "c")  # Test case: 0 degrees Celsius
print(result)  # Print the result of the conversion