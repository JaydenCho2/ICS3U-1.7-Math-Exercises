"""
File: rads.py
Author: Jayden Cho
Date: 2024-02-22 
Description: Calculating radians using given degrees
"""
Degrees=int(input("Enter Degrees: "))
pi=3.14159

radians=(Degrees * (pi / 180))
rounded_radians=round(radians, 4)

print("Result: " + str(Degrees) + " degrees is " + str(rounded_radians) + " radians")