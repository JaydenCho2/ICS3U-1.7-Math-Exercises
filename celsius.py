"""
File: celsius.py
Author: Jayden Cho
Date: 2024-02-22 
Description: converting given fahreheit to celsius
"""

Fahrenheit= int(input("Enter Temperture in Fahrenheit: "))

Celsius=(5 / 9) * (Fahrenheit - 32)
rounded_celsius= round(Celsius)

print("Result: " + str(Fahrenheit) + "°F is " + str(rounded_celsius) + "°C")