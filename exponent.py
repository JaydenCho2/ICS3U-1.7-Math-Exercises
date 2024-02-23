"""
File: exponent.py
Author: Jayden Cho
Date: 2024-02-22 
Description: creating and calculating exponent using given base and power
"""

Base=float(input("Enter Base: "))
Power=float(input("Enter Power: "))

exponent=Base ** Power
rounded_exponent=round(exponent, 2)

print("Result: a^b is " + str(exponent))