"""
File: celsius.py
Author: Jayden Cho
Date: 2024-02-22 
Description: converting given fahreheit to celsius
"""
#Inputs of Fahrenheit
Fahrenheit= int(input("Enter Temperture in Fahrenheit: "))

#Calculating the celsius using given fahrenheit and rounding
Celsius= (5 / 9) * (Fahrenheit - 32)
rounded_celsius= round(Celsius)

#Printing the reuslt
print("Result: " + str(Fahrenheit) + "°F is " + str(rounded_celsius) + "°C")