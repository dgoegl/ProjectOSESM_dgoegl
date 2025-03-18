"""
converter.py - A simple temperature conversion tool.

Author: David Goegl
License: Apache License 2.0
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
"""

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.

    :param celsius: Temperature in Celsius (float).
    :return: Temperature in Fahrenheit (float).
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.

    :param fahrenheit: Temperature in Fahrenheit (float).
    :return: Temperature in Celsius (float).
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """
    Converts Celsius to Kelvin.

    :param celsius: Temperature in Celsius (float).
    :return: Temperature in Kelvin (float).
    """
    return celsius + 273.15

if __name__ == "__main__":

    temp_c = float(input("What number in Celsius would you liek to convert kind sir?"))
    temp_f = celsius_to_fahrenheit(temp_c)
    temp_k = celsius_to_kelvin(temp_c)

    print(f"{temp_c}°C is {temp_f:.2f}°F and {temp_k:.2f}K")
