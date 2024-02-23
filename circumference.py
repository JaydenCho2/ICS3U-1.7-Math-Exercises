"""
File: circumference.py
Author: Jayden Cho
Date: 2024-02-22 
Description: finding circumference using given radius
"""

radius=float(input("Enter Radius: "))
pi=3.14159

circumference=float(2*(radius*pi))
rounded_circumference= round(circumference, 2)

print("Result: " + str(rounded_circumference))
