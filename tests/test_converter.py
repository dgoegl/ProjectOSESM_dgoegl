import sys
import os

# Ensure src/ is in Python’s path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert round(celsius_to_fahrenheit(-40), 2) == -40.00  # Edge case

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert round(fahrenheit_to_celsius(-40), 2) == -40.00  # Edge case

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(-273.15) == 0  # Absolute zero
    assert celsius_to_kelvin(100) == 373.15

